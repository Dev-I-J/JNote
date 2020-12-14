from mdx_gfm import GithubFlavoredMarkdownExtension
from PyQt5.QtCore import pyqtSlot, pyqtProperty
from version_parser.version import Version
from requests import get, RequestException
from markdown import markdown
from tempfile import mkstemp
from fileio import FileIO
import webbrowser
import subprocess
import datetime
import sys
import os
import re

# Typing Imports
from typing import Dict, List, Tuple, Any


class JNote(FileIO):

    """Class Exposed to QML"""

    def __init__(self) -> None:
        FileIO.__init__(self)
        self.__updateInfo: Dict[str, str] = {}
        self.__cleanupFiles: List[Tuple[int, str]] = []

    @pyqtSlot(bool)
    def checkUpdates(self, isStartup: bool) -> None:
        """Check For Updates"""
        try:
            url: str = (
                "https://api.github.com/repos/Dev-I-J/JNote/releases/latest"
            )
            with get(url) as r:
                currentVersionStr: str = "v1.6.6"
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
        except Exception:
            self.fatalError.emit()
        return []

    @pyqtSlot(bool, str)
    def render(self, md: bool, source: str) -> None:
        try:
            file, name = mkstemp(suffix=".html", text=True)
            self.__cleanupFiles.append((file, name))
            with open(name, "w") as tmpFile:
                tmpFile.write(source if not md else markdown(source))
                webbrowser.open_new_tab(name)
        except Exception:
            self.fatalError.emit()

    @pyqtSlot(str)
    def shellExec(self, script: str) -> None:
        try:
            if sys.platform == "win32":
                file, name = mkstemp(suffix=".bat", text=True)
                self.__cleanupFiles.append((file, name))
                with open(name, "w") as tmpFile:
                    tmpFile.write(script)
                    subprocess.run(f"start cmd /k {name}", shell=True)
            elif sys.platform == "darwin":
                file, name = mkstemp(suffix=".sh", text=True)
                self.__cleanupFiles.append((file, name))
                with open(name, "w") as tmpFile:
                    tmpFile.write(script)
                    subprocess.run(f"open -W -a Terminal.app {name}")
            else:
                self.platformNotSupported.emit(sys.platform)
        except Exception:
            self.fatalError.emit()

    @pyqtSlot()
    def clean(self) -> None:
        try:
            self.__addComments()
            for file in self.__cleanupFiles:
                try:
                    os.close(file[0])
                    os.remove(file[1])
                except OSError:
                    pass
                except Exception:
                    self.fatalError.emit()
        except Exception:
            self.fatalError.emit()

    @staticmethod
    def __addComments() -> None:
        comments: str = """\
# DO NOT DELETE OR MODIFY THIS FILE! DOING SO WILL DAMAGE JNOTE!!
# This File is Automatically Generated and is not for adding
# user's preferences.
# These are some small settings used to enhance your experience with
# JNote but not to, Edit or DELETE.
# Doing so will do nothing but only ruin your experience!!!

"""
        with open("settings.toml", "r") as settings:
            settingsString: str = settings.read()
        with open("settings.toml", "w") as settings:
            settings.write(comments + settingsString)

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
        return self.__updateInfo

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
        self.__updateInfo = arg
