from PyQt5.QtCore import pyqtSlot
from settings import Settings
from binaryornot import check
import cchardet
import chardet


class FileIO(Settings):

    """All the File I/O stuff of JNote goes Here"""

    def __init__(self) -> None:
        Settings.__init__(self)

    @ pyqtSlot()
    def fileNew(self) -> None:
        """Update settings when a new document is created"""
        try:
            self.setSettingsBool("last-used-file", "untitled", True)
            self.setSettingsStr("last-used-file", "encoding", "utf-8")
            self.setSettingsStr("last-used-file", "path", "")
            self.setSettingsStr("last-used-file", "text", "")
            self.newDocumentCreated.emit()
        except Exception:
            self.fatalError.emit()

    @ pyqtSlot(str, result=str)
    def fileOpen(self, fPath: str) -> str:
        """Open File"""
        fileText: str = ""
        try:
            if not check.is_binary(fPath):
                with open(fPath, "rb") as binaryFile:
                    binary: str = binaryFile.read()
                    coding: str = cchardet.detect(binary)["encoding"]
                    fileText: str = binary.decode(coding)
                    self.setSettingsBool("last-used-file", "untitled", False)
                    self.setSettingsStr("last-used-file", "path", fPath)
                    self.setSettingsStr("last-used-file", "encoding", coding)
                    self.fileOpenSuccessful.emit()
                    return fileText
            else:
                self.fileOpenError.emit()
        except (UnicodeDecodeError, LookupError):
            try:
                with open(fPath, "rb") as binaryFile:
                    binary: str = binaryFile.read()
                    coding: str = chardet.detect(binary)["encoding"]
                    fileText: str = binary.decode(coding)
                    self.setSettingsBool("last-used-file", "untitled", False)
                    self.setSettingsStr("last-used-file", "path", fPath)
                    self.setSettingsStr("last-used-file", "encoding", coding)
                    self.fileOpenSuccessful.emit()
                    return fileText
            except (UnicodeDecodeError, LookupError):
                self.fileOpenError.emit()
            except IOError:
                self.fileHandleError.emit()
            except Exception:
                self.fatalError.emit()
        except FileNotFoundError:
            self.fileNotFound.emit(fPath)
        except IOError:
            self.fileHandleError.emit()
        except Exception:
            self.fatalError.emit()
        return ""

    @ pyqtSlot(str)
    def fileSave(self, fText: str) -> None:
        """Save File"""
        fPath: str = self.getSettings("last-used-file")["path"]
        try:
            untitled: bool = self.getSettings("last-used-file")["untitled"]
            if not untitled:
                fCoding: str = self.getSettings("last-used-file")["encoding"]
                with open(fPath, "w", encoding=fCoding) as outFile:
                    outFile.write(fText)
                self.fileSaved.emit()
            else:
                self.fileUntitled.emit()
        except FileNotFoundError:
            self.fileNotFound.emit(fPath)
        except IOError:
            self.fileHandleError.emit()
        except Exception:
            self.fatalError.emit()

    @ pyqtSlot(str, str)
    def fileSaveAs(self, fPath: str, fText: str) -> None:
        """Save File As"""
        try:
            fCoding: str = self.getSettings("last-used-file")["encoding"]
            with open(fPath, "w+", encoding=fCoding) as outFile:
                outFile.write(fText)
                self.fileSavedAs.emit()
        except FileNotFoundError:
            self.fileNotFound.emit(fPath)
        except IOError:
            self.fileHandleError.emit()
        except Exception:
            self.fatalError.emit()
        else:
            self.setSettingsBool("last-used-file", "untitled", False)
            self.setSettingsStr("last-used-file", "path", fPath)

    @ pyqtSlot(result=str)
    def openLastOpenFile(self) -> str:
        """(re)Open last opened file"""
        fPath: str = self.getSettings("last-used-file")["path"]
        try:
            fCoding: str = self.getSettings("last-used-file")["encoding"]
            with open(fPath, "r", encoding=fCoding) as text:
                return text.read()
        except FileNotFoundError:
            self.fileNotFound.emit(fPath)
        except UnicodeDecodeError:
            self.fileOpenError.emit()
        except IOError:
            self.fileHandleError.emit()
        except Exception:
            self.fatalError.emit()
        return ""
