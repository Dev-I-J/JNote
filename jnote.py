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
        self._about = ""
        self._license = ""
        self._updateInfo = {}

    @pyqtSlot()
    def updateProperty(self):
        with open("README.md", "r", encoding="utf-8") as aboutfile:
            abouthtml = markdown(aboutfile.read())
            self.about = abouthtml
        with open("LICENSE.md", "r", encoding="utf-8") as licensefile:
            licensehtml = markdown(licensefile.read())
            self.gplLicense = licensehtml

    @pyqtSlot(bool)
    def checkUpdates(self, isStartup):
        """Check For Updates"""

        try:
            url = "https://api.github.com/repos/Dev-I-J/JNote/releases/latest"
            with get(url) as r:
                currentVersionStr = "v1.4.0"
                currentVersion = Version(currentVersionStr)
                newVersionStr = r.json()['tag_name']
                newVersion = Version(newVersionStr)
                if currentVersion < newVersion:
                    raw_info = markdown(r.json()['body'], extensions=[
                        GithubFlavoredMarkdownExtension()
                    ])
                    details, sep, exclude = raw_info.partition("Package Table")
                    date = r.json()['published_at'][0:10]
                    self.updateInfo["newVersion"] = newVersionStr
                    self.updateInfo["currentVersion"] = currentVersionStr
                    self.updateInfo["details"] = details
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

    @pyqtProperty(str, constant=True)
    def about(self):
        return self._about

    @pyqtProperty(str, constant=True)
    def gplLicense(self):
        return self._license

    @pyqtProperty("QVariant", constant=True)
    def updateInfo(self):
        return self._updateInfo

    @about.setter
    def about(self, arg):
        if arg == self._about:
            return
        self._about = arg

    @gplLicense.setter
    def gplLicense(self, arg):
        if arg == self._license:
            return
        self._license = arg

    @updateInfo.setter
    def updateInfo(self, arg):
        if arg == self._updateInfo:
            return
        self._updateInfo = arg
