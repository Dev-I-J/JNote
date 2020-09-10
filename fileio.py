from PyQt5.QtCore import pyqtSlot
from settings import Settings


class FileIO(Settings):

    """All the File I/O stuff of JNote goes Here"""

    def __init__(self, parent=None):
        super().__init__(parent)

    @pyqtSlot()
    def fileNew(self):
        """Update settings when a new document is created"""
        self.setSettingsBool("last-used-file", "untitled", True)
        self.setSettingsStr("last-used-file", "path", "")
        self.setSettingsStr("last-used-file", "text", "")
        self.newDocumentCreated.emit()

    @pyqtSlot(str, result=str)
    def fileOpen(self, fPath):
        """Open File"""
        fileText = ""
        try:
            with open(fPath, "r", encoding="utf-8") as text:
                self.fileOpenSuccessful.emit()
                fileText = text.read()
                self.setSettingsBool("last-used-file", "untitled", False)
                self.setSettingsStr("last-used-file", "path", fPath)
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
                with open(fPath, "w") as outFile:
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
            with open(fPath, "w+") as outFile:
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
    def getLastOpenFilePath(self):
        """(re)Open last opened file"""
        filePath = ""
        try:
            untitled = self.getSettings("last-used-file")["untitled"]
            if not untitled:
                path = self.getSettings("last-used-file")["path"]
                filePath = path
        except FileNotFoundError:
            self.fileNotFound.emit()
        except UnicodeDecodeError:
            self.fileOpenError.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()
        return filePath
