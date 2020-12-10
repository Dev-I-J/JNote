from mdx_gfm import GithubFlavoredMarkdownExtension
from PyQt5.QtCore import pyqtSlot, pyqtProperty
from version_parser.version import Version
from requests import get, RequestException
from markdown import markdown
from fileio import FileIO
import datetime
import sys
import re

# Typing Imports
from typing import Dict, List, Any


class JNote(FileIO):

    """Class Exposed to QML"""

    def __init__(self, parent: None = None) -> None:
        super().__init__(parent)
        self._updateInfo: Dict[str, str] = {}

    @pyqtSlot(bool)
    def checkUpdates(self, isStartup: bool) -> None:
        """Check For Updates"""
        try:
            url: str = (
                "https://api.github.com/repos/Dev-I-J/JNote/releases/latest"
            )
            with get(url) as r:
                currentVersionStr: str = "v1.6.0"
                currentVersion: Version = Version(currentVersionStr)
                newVersionStr: str = r.json()['tag_name']
                newVersion: Version = Version(newVersionStr)
                if currentVersion < newVersion:
                    raw_info: str = markdown(r.json()['body'], extensions=[
                        GithubFlavoredMarkdownExtension()
                    ])
                    info: str = raw_info.partition(
                        "<h1>Downloads Table</h1>")[0]
                    date: str = r.json()['published_at'][0:10]
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
        except Exception:
            self.fatalError.emit()
        finally:
            sys.exit()

    @pyqtSlot(str, str, bool, bool, result=list)
    def findText(
        self, pattern: str, text: str, casesensitive: bool, regex: bool
    ) -> List[List[int]]:
        """Find Given Text"""
        try:
            result: List[List[int]] = []
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
        except Exception:
            self.fatalError.emit()

    @pyqtSlot(bool, str)
    def render(md: bool, source: str):
        pass

    @pyqtProperty(str, constant=True)
    def about(self) -> str:
        """About JNote"""
        try:
            with open("data/about.html", "r", encoding="utf-8") as aboutfile:
                return aboutfile.read()
        except FileNotFoundError:
            self.readmeFileNotFound.emit()
            return "data/about.html Not Found."
        except Exception:
            self.fatalError.emit()
            return ""

    @pyqtProperty(str, constant=True)
    def gplLicense(self) -> str:
        """GNU GPL License"""
        try:
            with open(
                    "data/license.html", "r", encoding="utf-8") as licensefile:
                return licensefile.read()
        except FileNotFoundError:
            self.licenseFileNotFound.emit()
            return "data/license.html Not Found."
        except Exception:
            self.fatalError.emit()
            return ""

    @pyqtProperty("QVariant", constant=True)
    def updateInfo(self) -> Dict[str, str]:
        """Update Information"""
        return self._updateInfo

    @pyqtProperty(str)
    def dateTime(self) -> str:
        try:
            dtobject: datetime = datetime.datetime.now()
            datetimestr: str = dtobject.strftime("%I:%M %p %d/%m/%Y")
            self.dateTimeInserted.emit()
            return datetimestr
        except Exception:
            self.fatalerror.emit()
            return ""

    @updateInfo.setter
    def updateInfo(self, arg: Any) -> None:
        self._updateInfo = arg
