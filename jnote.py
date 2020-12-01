from mdx_gfm import GithubFlavoredMarkdownExtension
from PyQt5.QtCore import pyqtSlot, pyqtProperty
from version_parser.version import Version
from requests import get, RequestException
from markdown import markdown
from fileio import FileIO
import datetime
import re


class JNote(FileIO):

    """Class Exposed to QML"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._updateInfo = {}

    @pyqtSlot(bool)
    def checkUpdates(self, isStartup):
        """Check For Updates"""

        try:
            url = "https://api.github.com/repos/Dev-I-J/JNote/releases/latest"
            with get(url) as r:
                currentVersionStr = "v1.5.2"
                currentVersion = Version(currentVersionStr)
                newVersionStr = r.json()['tag_name']
                newVersion = Version(newVersionStr)
                if currentVersion < newVersion:
                    info = markdown(r.json()['body'], extensions=[
                        GithubFlavoredMarkdownExtension()
                    ])
                    date = r.json()['published_at'][0:10]
                    self.updateInfo["newVersion"] = newVersionStr
                    self.updateInfo["currentVersion"] = currentVersionStr
                    self.updateInfo["details"] = info
                    self.updateInfo["date"] = date
                    self.updateAvailable.emit()
                else:
                    if not isStartup:
                        self.updateInfo["currentVersion"] = currentVersionStr
                        self.upToDate.emit()
        except RequestException:
            self.apiConnectError.emit()
        except KeyError:
            self.apiError.emit()
        except BaseException:
            self.fatalError.emit()

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

    @pyqtProperty(str, constant=True)
    def about(self):
        """About JNote"""
        try:
            with open("README.md", "r", encoding="utf-8") as aboutfile:
                abouthtml = markdown(aboutfile.read())
                return abouthtml
        except FileNotFoundError:
            self.readmeFileNotFound.emit()
            return "README.md Not Found."
        except BaseException:
            self.fatalError.emit()
            return ""

    @pyqtProperty(str, constant=True)
    def gplLicense(self):
        """GNU GPL License"""
        try:
            with open("LICENSE.md", "r", encoding="utf-8") as licensefile:
                licensehtml = markdown(licensefile.read())
                return licensehtml
        except FileNotFoundError:
            self.licenseFileNotFound.emit()
            return "LICENSE.md Not Found."
        except BaseException:
            self.fatalError.emit()
            return ""

    @pyqtProperty("QVariant", constant=True)
    def updateInfo(self):
        """Update Information"""
        return self._updateInfo

    @pyqtProperty(str)
    def dateTime(self):
        try:
            dtobject = datetime.datetime.now()
            datetimestr = dtobject.strftime("%I:%M %p %d/%m/%Y")
            self.dateTimeInserted.emit()
            return datetimestr
        except BaseException:
            self.fatalerror.emit()
            return ""

    @updateInfo.setter
    def updateInfo(self, arg):
        self._updateInfo = arg
