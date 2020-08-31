from PyQt5.QtCore import pyqtSlot
from settings import Settings


class FileIO(Settings):

    """All the File I/O stuff of JNote goes Here"""

    def __init__(self, parent=None):
        super().__init__(parent)

    @pyqtSlot()
    def fileNew(self):
        """Clear the path in settings when new doc is created"""
        self.setSettingsBool("last-used-file", "untitled", True)
        self.setSettingsStr("last-used-file", "path", "")

    @pyqtSlot(str)
    def fileOpen(self, fPath):
        """Open File"""
        try:
            with open(fPath, "r", encoding="utf-8") as fText:
                self.fileOpenSuccessful.emit(fText.read(), fPath)
        except UnicodeDecodeError:
            self.fileOpenError.emit()
        except FileNotFoundError:
            self.fileNotFound.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()
        else:
            self.setSettingsBool("last-used-file", "untitled", False)
            self.setSettingsStr("last-used-file", "path", fPath)

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
                self.fileSavedAs.emit(fPath)
        except FileNotFoundError:
            self.fileNotFound.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()
        else:
            self.log(fPath, False)

    @pyqtSlot()
    def openLast(self):
        """(re)Open last opened file"""
        try:
            untitled = self.getSettings("last-used-file")["untitled"]
            if not untitled:
                fPath = self.getSettings("last-used-file")["path"]
                with open(fPath, "r", encoding="utf-8") as fText:
                    self.fileOpenSuccessful.emit(fText.read(), fPath)
        except FileNotFoundError:
            self.fileNotFound.emit()
        except UnicodeDecodeError:
            self.fileOpenError.emit()
        except IOError:
            self.fileHandleError.emit()
        except BaseException:
            self.fatalError.emit()
