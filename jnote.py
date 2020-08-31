from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from version_parser.version import Version
from requests import get, RequestException
from markdown import markdown


class JNote(QObject):

    """Base Class For JNote"""

    updateArgs = ['newVersionStr', 'currentVersionStr', 'info', 'date']

    updateAvailable = pyqtSignal(str, str, str, str, arguments=updateArgs)
    fileOpenSuccessful = pyqtSignal(str, str, arguments=['text', 'path'])
    fileSavedAs = pyqtSignal(str, str, arguments=['path', 'newText'])
    upToDate = pyqtSignal(str, arguments=['currentVersionStr'])
    clipboardStatusChanged = pyqtSignal()
    settingsFileNotFound = pyqtSignal()
    confirmExitSignal = pyqtSignal()
    fileHandleError = pyqtSignal()
    apiConnectError = pyqtSignal()
    fileOpenError = pyqtSignal()
    settingsError = pyqtSignal()
    fileNotFound = pyqtSignal()
    fileUntitled = pyqtSignal()
    fatalError = pyqtSignal()
    fileSaved = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    @pyqtSlot(bool)
    def checkUpdates(self, isSatrtup):
        """Check for updates"""
        try:
            url = "https://api.github.com/repos/Dev-I-J/JNote/releases/latest"
            with get(url) as r:
                currentVersionStr = "v1.3.0"
                currentVersion = Version(currentVersionStr)
                newVersionStr = r.json()['tag_name']
                newVersion = Version(newVersionStr)
                if currentVersion < newVersion:
                    raw_info = markdown(r.json()['body'])
                    info, sep, exclude = raw_info.partition("Package Table")
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
