from PyQt5.QtCore import pyqtSlot
from settings import Settings
from binaryornot import check
import cchardet
import chardet


class FileIO(Settings):

    """All the File I/O stuff of JNote goes Here"""

    def __init__(self, parent=None):
        super().__init__(parent)

    @pyqtSlot()
    def fileNew(self):
        """Update settings when a new document is created"""
        try:
            self.setSettingsBool("last-used-file", "untitled", True)
            self.setSettingsStr("last-used-file", "encoding", "utf-8")
            self.setSettingsStr("last-used-file", "path", "")
            self.setSettingsStr("last-used-file", "text", "")
            self.newDocumentCreated.emit()
        except BaseException:
            self.fatalError.emit()

    @pyqtSlot(str, result=str)
    def fileOpen(self, fPath):
        """Open File"""
        fileText = ""
        try:
            if not check.is_binary(fPath):
                with open(fPath, "rb") as binaryFile:
                    binary = binaryFile.read()
                    coding = cchardet.detect(binary)["encoding"]
                    fileText = binary.decode(coding)
                    self.setSettingsBool("last-used-file", "untitled", False)
                    self.setSettingsStr("last-used-file", "path", fPath)
                    self.setSettingsStr("last-used-file", "encoding", coding)
                    self.fileOpenSuccessful.emit()
            else:
                self.fileOpenError.emit()
        except (UnicodeDecodeError, LookupError):
            try:
                with open(fPath, "rb") as binaryFile:
                    binary = binaryFile.read()
                    coding = chardet.detect(binary)["encoding"]
                    fileText = binary.decode(coding)
                    self.setSettingsBool("last-used-file", "untitled", False)
                    self.setSettingsStr("last-used-file", "path", fPath)
                    self.setSettingsStr("last-used-file", "encoding", coding)
                    self.fileOpenSuccessful.emit()
            except (UnicodeDecodeError, LookupError):
                self.fileOpenError.emit()
            except IOError:
                self.fileHandleError.emit()
            except BaseException:
                self.fatalError.emit()
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
