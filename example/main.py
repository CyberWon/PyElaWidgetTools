import sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from PySide6ElaWidgetTools import *
from mainwindow import *
# t

try:
    QT_VERSION_STR
except:
    QT_VERSION_STR = "6.8.3"

if QT_VERSION_STR < "6.0.0":
    QGuiApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
    if QT_VERSION_STR >= "5.14.0":
        QGuiApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
        QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
        )

app = QApplication(sys.argv)
eApp.init()
eApp.setWindowDisplayMode(ElaApplicationType.WindowDisplayMode.Mica)
w = MainWindow()
w.show()
app.exec()
