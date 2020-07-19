from PyQt5.QtCore import QUrl, QObject, pyqtSlot, pyqtSignal
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from requests import get, RequestException
from version_parser.version import Version
from markdown import markdown
import sys


class JNote(QObject):

    args = ['newVersionStr', 'currentVersionStr', 'info', 'date']
    fileOpenSuccessful = pyqtSignal(str, str, arguments=['text', 'path'])
    fileSavedAs = pyqtSignal(str, str, arguments=['path', 'newText'])
    updateAvailable = pyqtSignal(str, str, str, str, arguments=args)
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
        oPath = open("log.txt", "r")
        fPath = oPath.read()
        try:
            if fPath != "":
                with open(fPath, "r") as fText:
                    self.fileOpenSuccessful.emit(fText.read(), fPath)
        except FileNotFoundError:
            self.fileNotFound.emit()
        except UnicodeDecodeError:
            try:
                with open(fPath, "r", encoding="utf-8") as fText:
                    self.fileOpenSuccessful.emit(fText.read(), fPath)
            except UnicodeDecodeError:
                self.fileOpenError.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()
        oPath.close()

    @pyqtSlot()
    def fileNew(self):
        with open("log.txt", "w") as log:
            log.write("")

    @pyqtSlot(bool)
    def checkUpdates(self, isSatrtup):
        try:
            url = "https://api.github.com/repos/Dev-I-J/JNote/releases/latest"
            with get(url) as r:
                currentVersionStr = "v1.2.2"
                currentVersion = Version(currentVersionStr)
                newVersionStr = r.json()['tag_name']
                newVersion = Version(newVersionStr)
                if currentVersion < newVersion:
                    info = markdown(r.json()['body'])
                    published_at = r.json()['published_at']
                    date = published_at[0:10]
                    self.updateAvailable.emit(newVersionStr,
                                              currentVersionStr,
                                              info,
                                              date)
                else:
                    if not isSatrtup:
                        self.upToDate.emit(currentVersionStr)
        except RequestException:
            self.apiConnectError.emit()
        except BaseException:
            self.fatalError.emit()

    @pyqtSlot(str)
    def fileOpen(self, fPath):
        log = open("log.txt", "w")
        log.write(fPath)
        try:
            with open(fPath, "r") as fText:
                self.fileOpenSuccessful.emit(fText.read(), fPath)
        except UnicodeDecodeError:
            try:
                open("log.txt", "w").write(fPath)
                with open(fPath, "r", encoding="utf-8") as fText:
                    self.fileOpenSuccessful.emit(fText.read(), fPath)
            except UnicodeDecodeError:
                self.fileOpenError.emit()
        except FileNotFoundError:
            self.fileNotFound.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()
        log.close()

    @pyqtSlot(str)
    def fileSave(self, fText):
        oPath = open("log.txt", "r")
        fPath = oPath.read()
        try:
            if fPath != "":
                with open(fPath, "w") as writeText:
                    writeText.write(fText)
                self.fileSaved.emit()
            else:
                self.fileUntitled.emit()
        except FileNotFoundError:
            self.fileNotFound.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()
        oPath.close()

    @pyqtSlot(str, str)
    def fileSaveAs(self, fPath, fText):
        log = open("log.txt", "w")
        log.write(fPath)
        try:
            with open(fPath, "w+") as writeText:
                writeText.write(fText)
            with open(fPath, "r") as newText:
                self.fileSavedAs.emit(fPath, newText.read())
        except FileNotFoundError:
            self.fileNotFound.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()
        log.close()


def run():

    jnote = JNote()

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('Icons/favicon.png'))
    app.setOrganizationName("JNote")
    app.setOrganizationDomain("jnote.ml")

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("JNote", jnote)
    engine.load(QUrl('main.qml'))

    if not engine.rootObjects():
        return -1

    return app.exec_()


if __name__ == '__main__':

    sys.exit(run())
