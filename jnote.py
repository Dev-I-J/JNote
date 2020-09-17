from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, pyqtProperty
from mdx_gfm import GithubFlavoredMarkdownExtension
from version_parser.version import Version
from requests import get, RequestException
from markdown import markdown
import datetime
import re


class JNote(QObject):

    """Base Class For JNote"""

    settingsFileNotFound = pyqtSignal()
    fileOpenSuccessful = pyqtSignal()
    newDocumentCreated = pyqtSignal()
    dateTimeInserted = pyqtSignal()
    fileHandleError = pyqtSignal()
    updateAvailable = pyqtSignal()
    apiConnectError = pyqtSignal()
    fileOpenError = pyqtSignal()
    settingsError = pyqtSignal()
    fileNotFound = pyqtSignal()
    fileUntitled = pyqtSignal()
    fileSavedAs = pyqtSignal()
    fatalError = pyqtSignal()
    fileSaved = pyqtSignal()
    upToDate = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._updateInfo = {}

    @pyqtSlot(bool)
    def checkUpdates(self, isSatrtup):
        """Check For Updates"""

        try:
            url = "https://api.github.com/repos/Dev-I-J/JNote/releases/latest"
            with get(url) as r:
                currentVersionStr = "v1.4.1"
                currentVersion = Version(currentVersionStr)
                newVersionStr = r.json()['tag_name']
                newVersion = Version(newVersionStr)
                if currentVersion < newVersion:
                    raw_info = markdown(r.json()['body'], extensions=[
                        GithubFlavoredMarkdownExtension()
                    ])
                    details, sep, exclude = raw_info.partition("Package Table")
                    published_at = r.json()['published_at']
                    date = published_at[0:10]
                    self.updateInfo["newVersion"] = newVersionStr
                    self.updateInfo["currentVersion"] = currentVersionStr
                    self.updateInfo["details"] = details
                    self.updateInfo["date"] = date
                    self.updateAvailable.emit()
                else:
                    if not isSatrtup:
                        self.updateInfo["currentVersion"] = currentVersionStr
                        self.upToDate.emit()
        except RequestException:
            self.apiConnectError.emit()
        except BaseException:
            self.fatalError.emit()

    @pyqtSlot(result=str)
    def insertDateTime(self):
        """Get Current Date and Time"""

        datetimestr = ""
        try:
            dtobject = datetime.datetime.now()
            datetimestr = dtobject.strftime("%I:%M %p %d/%m/%Y")
            self.dateTimeInserted.emit()
        except BaseException:
            self.fatalerror.emit()
        return datetimestr

    @pyqtSlot(str, str, bool, bool, result=list)
    def findText(self, pattern, text, casesensitive, regex):
        """Find Given Text"""
        result = []
        if regex:
            if not casesensitive:
                for match in re.finditer(pattern, text, re.IGNORECASE):
                    result.append([match.span()[0], match.span()[1]])
            else:
                for match in re.finditer(pattern, text):
                    result.append([match.span()[0], match.span()[1]])
        else:
            pattern = re.escape(pattern)
            if not casesensitive:
                for match in re.finditer(pattern, text, re.IGNORECASE):
                    result.append([match.span()[0], match.span()[1]])
            else:
                for match in re.finditer(pattern, text):
                    result.append([match.span()[0], match.span()[1]])
        return result

    @pyqtProperty("QVariant", constant=True)
    def updateInfo(self):
        return self._updateInfo

    @updateInfo.setter
    def updateInfo(self, arg):
        if arg == self._updateInfo:
            return
        self._updateInfo = arg
