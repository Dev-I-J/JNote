from PyQt5.QtCore import pyqtSlot
from settings import Settings
from charamel import Detector
import sys
import os

try:
    import magic
except ImportError as e:
    if "failed to find libmagic" in str(e).lower():
        os.system("sudo apt-get install libmagic-dev")
        sys.exit()
    else:
        sys.exit()


class FileIO(Settings):

    """All the File I/O stuff of JNote goes Here"""

    def __init__(self, parent=None):
        super().__init__(parent)

    @pyqtSlot()
    def fileNew(self):
        """Update settings when a new document is created"""
        self.setSettingsBool("last-used-file", "untitled", True)
        self.setSettingsStr("last-used-file", "encoding" "utf-8")
        self.setSettingsStr("last-used-file", "path", "")
        self.setSettingsStr("last-used-file", "text", "")
        self.newDocumentCreated.emit()

    @pyqtSlot(str, result=str)
    def fileOpen(self, fPath):
        """Open File"""
        fileText = ""
        try:
            mime = magic.from_file(fPath, mime=True)
            if mime.startswith("text/"):
                with open(fPath, "rb") as binaryFile:
                    binary = binaryFile.read()
                    coding = Detector().detect(binary).value
                    fileText = binary.decode(coding)
                    self.setSettingsBool("last-used-file", "untitled", False)
                    self.setSettingsStr("last-used-file", "path", fPath)
                    self.setSettingsStr("last-used-file", "encoding", coding)
                    self.fileOpenSuccessful.emit()
            else:
                self.fileOpenError.emit()
        except UnicodeDecodeError:
            self.fileOpenError.emit()
        except FileNotFoundError:
            self.fileNotFound.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()
        return fileText

    @pyqtSlot(str)
    def fileSave(self, fText):
        """Save File"""
        try:
            untitled = self.getSettings("last-used-file")["untitled"]
            if not untitled:
                fPath = self.getSettings("last-used-file")["path"]
                fCoding = self.getSettings("last-used-file")["encoding"]
                with open(fPath, "w", encoding=fCoding) as outFile:
                    outFile.write(fText)
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
    def fileSaveAs(self, fPath, fText):
        """Save File As"""
        try:
            fCoding = self.getSettings("last-used-file")["encoding"]
            with open(fPath, "w+", encoding=fCoding) as outFile:
                outFile.write(fText)
                self.fileSavedAs.emit()
        except FileNotFoundError:
            self.fileNotFound.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()
        else:
            self.setSettingsBool("last-used-file", "untitled", False)
            self.setSettingsStr("last-used-file", "path", fPath)

    @pyqtSlot(result=str)
    def openLastOpenFile(self):
        """(re)Open last opened file"""
        fileText = ""
        try:
            fPath = self.getSettings("last-used-file")["path"]
            fCoding = self.getSettings("last-used-file")["encoding"]
            with open(fPath, "r", encoding=fCoding) as text:
                fileText = text.read()
        except FileNotFoundError:
            self.fileNotFound.emit()
        except UnicodeDecodeError:
            self.fileOpenError.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()
        return fileText
