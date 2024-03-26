from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from ui_splitter_gui import Ui_MainWindow
from functions import adjust_volume_and_save, run_additional_function
from pathlib import Path
import tempfile
import demucs.separate
import os
import requests
import json

class SubprocessThread(QThread):
    output_ready = pyqtSignal(str)

    def __init__(self, temp_dir_path, temp_input_file):
        super().__init__()
        self.temp_dir_path = temp_dir_path
        self.temp_input_file = temp_input_file

    def run(self):
        # Run your subprocess command here
        print("started my thing")
        demucs.separate.main(["--float32", "-d", "cpu", "--out", str(self.temp_dir_path), str(self.temp_input_file)])

        

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # get license key through API check
        self.ROOT_DIR = Path(__file__).parent
        self.TEXT_FILE = self.ROOT_DIR / 'license.txt'
        self.key = self.TEXT_FILE.read_text()
        os.environ['KEYGEN_ACCOUNT_ID'] = '0f5dc36e-048c-4f0a-9424-eff14d0ae5bb'

        # create directory for pngs
        self.icons_path = os.path.join(self.ROOT_DIR, 'Splitter_GUI_Assets_3')

        # check key
        
        if self.check_key(self.key):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.settingsBtn.show()
            self.ui.settingsPg_ext_btn.hide()
            self.ui.settingsPg_exp_btn.hide()
            self.ui.settingsPg_lic_lbl.setText("LICENSE KEY VERIFIED")
            #self.ui.settingsPg_licens_enter_btn.setEnabled(False)
        else:
            self.ui.settingsBtn.hide()
            self.ui.settingsPg_ext_btn.hide()
            self.ui.stackedWidget.setCurrentIndex(4)
            self.ui.settingsPg_licens_enter_btn.setEnabled(True) 


        # Load the user settings
        with open('config.json') as config_file:
            self.data = json.load(config_file)
        self.master_output_dir = self.data['exportLocation']
        self.ui.settingsPg_exp_lbl.setText(self.master_output_dir)  

        # import buttons
        self.ui.importPg_btn_imp.clicked.connect(self.importBtn)
        self.ui.importPg_btn_spl.clicked.connect(self.split)

        # import button events
        self.ui.importPg_btn_imp.setFlat(True)
        self.ui.importPg_btn_imp.enterEvent = self.enter_button
        self.ui.importPg_btn_imp.leaveEvent = self.leave_button
        self.ui.importPg_btn_spl.enterEvent = self.spl_enter_button
        self.ui.importPg_btn_spl.leaveEvent = self.spl_leave_button

        # settings buttons
        self.ui.settingsBtn.clicked.connect(self.go_settings)
        self.ui.settingsPg_exp_btn.clicked.connect(self.export)
        self.ui.settingsPg_ext_btn.clicked.connect(self.exit_settings)
        self.ui.settingsPg_licens_enter_btn.returnPressed.connect(self.licenseInputTest)

        # settings buttons events
        self.ui.settingsBtn.enterEvent = self.set_enter_button
        self.ui.settingsBtn.leaveEvent = self.set_leave_button

        # exit button events
        self.ui.settingsPg_ext_btn.enterEvent = self.set_ext_enter_button
        self.ui.settingsPg_ext_btn.leaveEvent = self.set_ext_leave_button

        # Disable buttons at the start
        self.ui.importPg_btn_spl.hide()

        # Wait for a file drag
        self.ui.importPg_wid_fileDrg.fileDropped.connect(self.retrieve_dropped_file)
        self.ui.importPg_wid_fileDrg.updateStyle(False)
  
    def enter_button(self, event):
        self.ui.importPg_btn_imp.setIcon(QIcon(os.path.join(self.icons_path, 'Browse Button Hover 2.png')))
        
    def leave_button(self, event):
        self.ui.importPg_btn_imp.setIcon(QIcon(os.path.join(self.icons_path, 'Browse Button Default 2.png'))) 

    def spl_enter_button(self, event):
        self.ui.importPg_btn_spl.setIcon(QIcon(os.path.join(self.icons_path, 'Split Button 2 Hover.png')))

    def spl_leave_button(self, event):
        self.ui.importPg_btn_spl.setIcon(QIcon(os.path.join(self.icons_path, 'Split Button 2 Default.png')))  

    def set_enter_button(self, event):
        self.ui.settingsBtn.setIcon(QIcon(os.path.join(self.icons_path, 'Settings_Icon_Hover 2.png')))

    def set_leave_button(self, event):
        self.ui.settingsBtn.setIcon(QIcon(os.path.join(self.icons_path, 'Settings Icon.png')))    

    def set_ext_enter_button(self, event):
        self.ui.settingsPg_ext_btn.setIcon(QIcon(os.path.join(self.icons_path, 'Exit Icon Hover.png')))

    def set_ext_leave_button(self, event):
        self.ui.settingsPg_ext_btn.setIcon(QIcon(os.path.join(self.icons_path, 'Exit Icon Default.png')))     

    def go_settings(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.settingsPg_exp_btn.show()
        self.ui.settingsPg_ext_btn.show() 
        self.ui.settingsBtn.hide()

    def exit_settings(self):
        self.ui.settingsPg_ext_btn.hide()  
        self.ui.settingsPg_exp_btn.hide()
        self.ui.settingsBtn.show() 
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.settingsPg_lic_lbl.setText("LICENSE KEY VERIFIED")
        
    def check_key(self, key):
        validation = requests.post(
            "https://api.keygen.sh/v1/accounts/{}/licenses/actions/validate-key".format(os.environ['KEYGEN_ACCOUNT_ID']),
            headers={
            "Content-Type": "application/vnd.api+json",
            "Accept": "application/vnd.api+json"
            },
            data=json.dumps({
            "meta": {
                "key": key
            }
            })
        ).json()

        if "errors" in validation:
            errs = validation["errors"]

            print(
            "license validation failed: {}".format(
                '\n'.join(map(lambda e: "{} - {}".format(e["title"], e["detail"]).lower(), errs))
            )
            )

            return

        valid = validation["meta"]["valid"]

        if valid:
            return True
        else:
            return False

    def retrieve_dropped_file(self, file_path):
        self.file_path = file_path
        self.ui.importPg_top_lbl.setText(f"FILE DROPPED:")
        self.ui.importPg_file_lbl.setText(os.path.basename(self.ui.importPg_wid_fileDrg.file_path))
        # Access the dropped file path from the promoted widget
        self.ui.importPg_btn_imp.hide()
        self.ui.importPg_btn_spl.show()
        self.ui.importPg_btn_spl.setEnabled(True)
        self.ui.importPg_file_lbl.show()
        self.ui.importPg_dot_lbl.setPixmap(QPixmap(os.path.join(self.icons_path, 'Rectangle Default.png')))
        #self.ui.filesLogo.hide()

    def licenseInputTest(self):
        text = self.ui.settingsPg_licens_enter_btn.text()
        if self.check_key(text):
            self.TEXT_FILE.write_text(text)
            self.ui.settingsPg_licens_enter_btn.clear()
            self.ui.settingsPg_lic_lbl.setText("LICENSE KEY VERIFIED")
            #self.ui.settingsPg_licens_enter_btn.setEnabled(False)
        else:
            self.ui.settingsPg_licens_enter_btn.clear()
            self.ui.settingsPg_lic_lbl.setText("Incorrect: Try Again")

    def export(self):
        # Open File Dialog
        while True:
            master_output_dir = QFileDialog.getExistingDirectory(self, "Open File", "")
            if master_output_dir:
                self.ui.settingsPg_ext_btn.show()
                self.master_output_dir = master_output_dir
                self.data['exportLocation'] = self.master_output_dir
                self.ui.settingsPg_exp_lbl.setText(self.master_output_dir)
                with open('config.json', 'w') as config_file:
                    json.dump(self.data, config_file)
                break
            else:
                break
    
    def importBtn(self):
        # Open File Dialog
        file_path, _= QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if file_path:
            #print(self.file_path)
            self.file_path = file_path
            self.ui.importPg_top_lbl.setText(f"FILE DROPPED:")
            self.ui.importPg_file_lbl.setText(os.path.basename(self.file_path))
            self.ui.importPg_btn_imp.hide()
            self.ui.importPg_btn_spl.show()
            self.ui.importPg_btn_spl.setEnabled(True)
            self.ui.importPg_file_lbl.show()
            self.ui.importPg_dot_lbl.setPixmap(QPixmap(os.path.join(self.icons_path, 'Rectangle Default.png')))
            #self.ui.filesLogo.hide()
            
        else:
            pass

    def split(self):
        # First check if master directory still exists
        try:
            if not os.path.exists(self.master_output_dir):
                self.ui.importPg_top_lbl.setText("Export Directory does not exist\nPlease choose another one in the settings")
                return

        except TypeError:
            self.ui.importPg_top_lbl.setText("Export Directory does not exist\nPlease choose another one in the settings")
            return
        
        # Create temporary directories
        self.input_file = Path(self.file_path)
        self.input_file_name = self.input_file.stem

        # Create final directory for stems to be placed in
        self.final_output_dir = os.path.join(self.master_output_dir, str(self.input_file_name) + " - Stems")
        error_occurred = False
        try:
            os.makedirs(self.final_output_dir)
        except FileExistsError:
            error_occurred = True

        if error_occurred:
            self.ui.importPg_btn_imp.show()
            self.ui.importPg_btn_spl.hide()
            self.ui.importPg_dot_lbl.setPixmap(QPixmap(os.path.join(self.icons_path, 'Rectangle Default_browse.png')))
            #self.ui.filesLogo.show()
            self.ui.importPg_file_lbl.hide()
            self.ui.importPg_top_lbl.setText("FOLDER WITH SONG NAME EXISTS")
            return
        else:
            self.ui.stackedWidget.setCurrentIndex(1)
            print("page switched") 
        
        self.ui.settingsBtn.setEnabled(False)
        self.ui.settingsBtn.hide() 
        self.temp_dir_path = Path(tempfile.mkdtemp(dir=self.final_output_dir))
        self.temp_input_file = self.temp_dir_path / f"{self.input_file_name}_temp.wav"
        adjust_volume_and_save(self.input_file, -10, self.temp_input_file)
        print(self.temp_input_file)

        # Start splitting process


        self.subprocess_thread = SubprocessThread(self.temp_dir_path, self.temp_input_file)
        self.subprocess_thread.start()
        print("Thread started")
        QTimer.singleShot(0, self.connect_finished)  


    def connect_finished(self):
        self.subprocess_thread.finished.connect(self.start_next_function)
        print("Connected to finished signal")

    def start_next_function(self):
        print("Next function started")
        if run_additional_function(self.input_file_name, self.input_file, self.temp_dir_path, self.final_output_dir):
            self.ui.settingsBtn.setEnabled(True)
            self.ui.importPg_top_lbl.setText("ERROR OCCURRED")
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.settingsBtn.show() 
            self.ui.importPg_btn_spl.hide()
            self.ui.importPg_btn_imp.show()
            self.ui.importPg_file_lbl.hide()
            self.ui.importPg_dot_lbl.setPixmap(QPixmap(os.path.join(self.icons_path, 'Rectangle Default_browse.png')))
            #self.ui.filesLogo.show()
        else:
            self.ui.settingsBtn.setEnabled(True)
            self.ui.importPg_top_lbl.setText("SPLITTING COMPLETE! DROP ANOTHER FILE?")
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.settingsBtn.show() 
            self.ui.importPg_btn_spl.hide()
            self.ui.importPg_btn_imp.show()
            self.ui.importPg_file_lbl.hide()
            self.ui.importPg_dot_lbl.setPixmap(QPixmap(os.path.join(self.icons_path, 'Rectangle Default_browse.png')))
            #self.ui.filesLogo.show()

if __name__ == "__main__":

    # Initialize The App
    app = QApplication(sys.argv)

    UIWindow = MainWindow()
    UIWindow.show()
    sys.exit(app.exec_())