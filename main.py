from PyQt5.QtCore import QUrl, QObject, pyqtSlot, pyqtSignal
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from requests import get, RequestException
from version_parser.version import Version
import sys


class PyQML(QObject):

    fileOpenSuccessful = pyqtSignal(str, str, arguments=['text', 'path'])
    fileSavedAs = pyqtSignal(str, str, arguments=['path', 'newText'])
    updateAvailable = pyqtSignal(str, arguments=['newVersionStr'])
    upToDate = pyqtSignal(str, arguments=['currentVersionStr'])
    confirmExitSignal = pyqtSignal()
    fileHandleError = pyqtSignal()
    apiConnectError = pyqtSignal()
    fileOpenError = pyqtSignal()
    fileNotFound = pyqtSignal()
    fileUntitled = pyqtSignal()
    fatalError = pyqtSignal()
    fileSaved = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    @pyqtSlot()
    def openLast(self):
        try:
            path = open("log.txt", "r").read()
            if path != "":
                text = open(path, "r").read()
                self.fileOpenSuccessful.emit(text, path)
        except FileNotFoundError:
            self.fileNotFound.emit()
        except UnicodeDecodeError:
            try:
                text = open(path, "r", encoding="utf-8").read()
                self.fileOpenSuccessful.emit(text, path)
            except UnicodeDecodeError:
                self.fileOpenError.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()

    @pyqtSlot()
    def fileNew(self):
        open("log.txt", "w").write("")

    @pyqtSlot(str)
    def checkUpdates(self, state):
        try:
            url = "https://api.github.com/repos/Dev-I-J/JNote/releases/latest"
            r = get(url)
            currentVersion = Version("v1.1.0")
            currentVersionStr = "v1.1.0"
            newVersion = Version(r.json()['tag_name'])
            newVersionStr = r.json()['tag_name']
            if newVersion > currentVersion:
                self.updateAvailable.emit(newVersionStr)
            else:
                if state != "startup":
                    self.upToDate.emit(currentVersionStr)
        except RequestException:
            self.apiConnectError.emit()
        except BaseException:
            self.fatalError.emit()

    @pyqtSlot(str)
    def fileOpen(self, path):
        try:
            text = open(path, "r").read()
            open("log.txt", "w").write(path)
            self.fileOpenSuccessful.emit(text, path)
        except UnicodeDecodeError:
            try:
                text = open(path, "r", encoding="utf-8").read()
                open("log.txt", "w").write(path)
                self.fileOpenSuccessful.emit(text, path)
            except UnicodeDecodeError:
                self.fileOpenError.emit()
        except FileNotFoundError:
            self.fileNotFound.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()

    @pyqtSlot(str)
    def fileSave(self, text):
        try:
            path = open("log.txt", "r").read()
            if path != "":
                write = open(path, "w")
                write.write(text)
                self.fileSaved.emit()
            else:
                self.fileUntitled.emit()
        except FileNotFoundError:
            self.fileNotFound.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()

    @pyqtSlot(str, str)
    def fileSaveAs(self, path, text):
        try:
            open(path, "w+").write(text)
            open("log.txt", "w").write(path)
            newText = open(path, "r").read()
            self.fileSavedAs.emit(path, newText)
        except FileNotFoundError:
            self.fileNotFound.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()


def run():

    pyqml = PyQML()

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('Icons/favicon.png'))
    app.setOrganizationName("JNote")
    app.setOrganizationDomain("jnote.ml")

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("PyQML", pyqml)
    engine.load(QUrl('main.qml'))

    if not engine.rootObjects():
        return -1

    return app.exec_()


if __name__ == '__main__':

    sys.exit(run())
