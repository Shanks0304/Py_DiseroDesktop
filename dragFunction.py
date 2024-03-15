from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Drag(QWidget):
    fileDropped = pyqtSignal(str)

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        self.file_path = None
        self.setAcceptDrops(True)  # Enable drag and drop for this widget
        self.setLayout(QVBoxLayout())
        
        self.setAutoFillBackground(True)
        
        self.setGraphicsEffect(self.createShadow(0))  # Soft drop shadow 
        
        # label
        self.label = QLabel("Drop a file here!")
        self.palette = self.label.palette()
        self.palette.setColor(self.label.foregroundRole(), QColor(86, 86, 86))
        self.label.setPalette(self.palette)
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setFont(QFont('Source Sans Pro', 24))
        self.label.setStyleSheet("padding-top: 20px;")
        self.setGraphicsEffect(self.createShadow(0))  # Soft drop shadow 
        self.layout().addWidget(self.label)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            self.updateStyle(True)
            event.acceptProposedAction()
        else:
            event.ignore()
    
    def dragLeaveEvent(self, event):
        self.updateStyle(False)

    def dropEvent(self, event: QDropEvent):
        self.updateStyle(False)
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            self.file_path = file_path
            self.fileDropped.emit(file_path)

    def updateStyle(self, hovered=False):
        bgColor = "#333333" if hovered else "#1E1E1E"
        self.setStyleSheet(f"""
            QLabel {{
                border: 2px dashed #AAAAAA;
                border-radius: 20px;
                background-color: {bgColor};
            }}
        """)

    def createShadow(self, blurRadius):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(blurRadius)
        shadow.setColor(QColor('grey'))
        shadow.setOffset(0, 0)
        return shadow


            


