from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from ui_designer_new import Ui_MainWindow
from functions import adjust_volume_and_save, run_additional_function
from pathlib import Path
import tempfile
import subprocess
import os
import requests
import json

class SubprocessThread(QThread):
    output_ready = pyqtSignal(str)

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        # Run your subprocess command here
        subprocess.run(self.command, check=True)
        

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set the background color using a stylesheet
        self.setStyleSheet("background-color: #1E1E1E;")

        # get license key through API check
        self.ROOT_DIR = Path(__file__).parent
        self.TEXT_FILE = self.ROOT_DIR / 'license.txt'
        self.key = self.TEXT_FILE.read_text()
        os.environ['KEYGEN_ACCOUNT_ID'] = '0f5dc36e-048c-4f0a-9424-eff14d0ae5bb'
        self.check_key(self.key)

        # Load the user settings
        with open('config.json') as config_file:
            self.data = json.load(config_file)
        self.master_output_dir = self.data['exportLocation']
        self.ui.settingsPg_exp_lbl.setText(self.master_output_dir)       

        # Setup License Page
        self.ui.licensePg_cnf_btn.clicked.connect(self.licenseBtn)

        # import buttons
        self.ui.importPg_btn_imp.clicked.connect(self.importBtn)
        self.ui.importPg_btn_spl.clicked.connect(self.split)

        # import button events
        self.ui.importPg_btn_imp.setFlat(True)
        self.ui.importPg_btn_imp.enterEvent = self.enter_button
        self.ui.importPg_btn_imp.leaveEvent = self.leave_button
        self.ui.importPg_btn_spl.enterEvent = self.spl_enter_button
        self.ui.importPg_btn_spl.leaveEvent = self.spl_leave_button
        
        # done buttons
        self.ui.donePg_btn_newSplt.clicked.connect(self.newSplit)

        # settings buttons
        self.ui.settingsBtn.clicked.connect(self.go_settings)
        self.ui.settingsPg_exp_btn.clicked.connect(self.export)
        self.ui.settingsPg_ext_btn.clicked.connect(self.exit_settings)

        # settings buttons events
        self.ui.settingsBtn.enterEvent = self.set_enter_button
        self.ui.settingsBtn.leaveEvent = self.set_leave_button

        # Disable buttons at the start
        self.ui.importPg_btn_spl.hide()

        # Wait for a file drag
        self.ui.importPg_wid_fileDrg.fileDropped.connect(self.retrieve_dropped_file)
        self.ui.importPg_wid_fileDrg.updateStyle(False)
  
    def enter_button(self, event):
        self.ui.importPg_btn_imp.setIcon(QIcon('C:\\Users\\Nener\\Documents\\GitHub\\DISERO_SPLITTER\\Splitter_GUI_Assets_3\\Browse Button Hover.png')) 

    def leave_button(self, event):
        self.ui.importPg_btn_imp.setIcon(QIcon('C:\\Users\\Nener\\Documents\\GitHub\\DISERO_SPLITTER\\Splitter_GUI_Assets_3\\Browse Button Default.png')) 

    def spl_enter_button(self, event):
        self.ui.importPg_btn_spl.setIcon(QIcon('C:\\Users\\Nener\\Documents\\GitHub\\DISERO_SPLITTER\\Splitter_GUI_Assets_3\\Split Button Hover.png'))

    def spl_leave_button(self, event):
        self.ui.importPg_btn_spl.setIcon(QIcon('C:\\Users\\Nener\\Documents\\GitHub\\DISERO_SPLITTER\\Splitter_GUI_Assets_3\\Split Button Default.png'))  

    def set_enter_button(self, event):
        self.ui.settingsBtn.setIcon(QIcon('C:\\Users\\Nener\\Documents\\GitHub\\DISERO_SPLITTER\\Splitter_GUI_Assets_3\\Settings_Icon_Hover.png'))

    def set_leave_button(self, event):
        self.ui.settingsBtn.setIcon(QIcon('C:\\Users\\Nener\\Documents\\GitHub\\DISERO_SPLITTER\\Splitter_GUI_Assets_3\\Settings Icon.png'))       

    def go_settings(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.settingsPg_stp_lbl.setText("Choose main directory to house stems")

    def exit_settings(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        
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
            self.ui.stackedWidget.setCurrentIndex(0)
            return True
        else:
            self.ui.stackedWidget.setCurrentIndex(3)
            return False

    def retrieve_dropped_file(self, file_path):
        self.file_path = file_path
        self.ui.importPg_wid_fileDrg.label.setText(f"File dropped: {os.path.basename(self.ui.importPg_wid_fileDrg.file_path)}")
        # Access the dropped file path from the promoted widget
        self.ui.importPg_btn_imp.hide()
        self.ui.importPg_btn_spl.show()
        self.ui.importPg_btn_spl.setEnabled(True)

    def licenseBtn(self):
        if self.check_key(self.ui.licensePg_text.toPlainText()):
            self.TEXT_FILE.write_text(self.ui.licensePg_text.toPlainText())
            if self.master_output_dir == None:
                self.ui.stackedWidget.setCurrentIndex(4)
                self.ui.settingsPg_ext_btn.setEnabled(False)
                self.ui.settingsPg_stp_lbl.setText("Choose main directory to house stems")
            else:
                self.ui.stackedWidget.setCurrentIndex(0)
        else:
            self.ui.licensePg_lb.setText("invalid key, try again loser")   

    def export(self):
        # Open File Dialog
        while True:
            master_output_dir = QFileDialog.getExistingDirectory(self, "Open File", "")
            if master_output_dir:
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
        self.file_path, _= QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if self.file_path:
            print(self.file_path)
            self.ui.importPg_wid_fileDrg.file_path = self.file_path
            self.ui.importPg_wid_fileDrg.label.setText(f"File dropped: {os.path.basename(self.ui.importPg_wid_fileDrg.file_path)}")
            self.ui.importPg_btn_imp.hide()
            self.ui.importPg_btn_spl.show()
            self.ui.importPg_btn_spl.setEnabled(True)
            
        else:
            pass
            
        
    def split(self):
        # First check if master directory still exists
        try:
            if not os.path.exists(self.master_output_dir):
                self.ui.importPg_lbl.setText("Export Directory does not exist, please choose another one in the settings")
                return

        except TypeError:
            self.ui.importPg_lbl.setText("Export Directory does not exist, please choose another one in the settings")
            return
        
        # Create temporary directories
        self.input_file = Path(self.ui.importPg_wid_fileDrg.file_path)
        self.input_file_name = self.input_file.stem

        # Create final directory for stems to be placed in
        self.final_output_dir = os.path.join(self.master_output_dir, str(self.input_file_name))
        error_occurred = False
        try:
            os.makedirs(self.final_output_dir)
        except FileExistsError:
            print("File exists already")
            error_occurred = True

        if error_occurred:
            self.ui.importPg_lbl.setText("File Exists Error")
            self.ui.importPg_btn_imp.show()
            self.ui.importPg_btn_spl.hide()
            self.ui.importPg_wid_fileDrg.label.setText("Drop a file here!")
            return
        else:
            print("no error occurred")
        '''
        if os.path.exists(self.final_output_dir):
            self.ui.settingsPg_stp_lbl.setText("Folder Exists Please Try Again")
        '''    
        
        self.ui.settingsBtn.setEnabled(False)
        self.ui.stackedWidget.setCurrentIndex(1) 
        self.temp_dir_path = Path(tempfile.mkdtemp(dir=self.final_output_dir))
        self.temp_input_file = self.temp_dir_path / f"{self.input_file_name}_temp.wav"
        adjust_volume_and_save(self.input_file, -10, self.temp_input_file)

        # Start splitting process
        command = ['python', '-m', 'demucs.separate', '--float32', '-d', 'cpu', '--out', str(self.temp_dir_path), str(self.temp_input_file)]
        self.subprocess_thread = SubprocessThread(command)
        self.subprocess_thread.start()
        print("Thread started")
        QTimer.singleShot(0, self.connect_finished)        

    def connect_finished(self):
        self.subprocess_thread.finished.connect(self.start_next_function)
        print("Connected to finished signal")

    def start_next_function(self):
        print("Next function started")
        run_additional_function(self.input_file_name, self.input_file, self.temp_dir_path, self.final_output_dir)
        self.ui.settingsBtn.setEnabled(True)
        self.ui.importPg_wid_fileDrg.label.setText("SPLITTING COMPLETE! DROP ANOTHER FILE?")
        self.ui.stackedWidget.setCurrentIndex(0) 
        self.ui.importPg_btn_spl.hide()
        self.ui.importPg_btn_imp.show()
    
    def newSplit(self):
        self.ui.importPg_btn_spl.setEnabled(False)
        self.ui.importPg_btn_spl.hide()
        self.ui.importPg_wid_fileDrg.file_path = None
        self.ui.importPg_wid_fileDrg.label.setText("Drop a file here!")
        self.ui.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":

    # Initialize The App
    app = QApplication(sys.argv)

    UIWindow = MainWindow()
    UIWindow.show()
    sys.exit(app.exec_())