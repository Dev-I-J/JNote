from PyQt5.QtCore import QObject, pyqtSignal


class Signals(QObject):

    """Base Class For JNote"""

    def __init__(self, parent=None):
        super().__init__(parent)

    settingsFileNotFound = pyqtSignal()
    licenseFileNotFound = pyqtSignal()
    readmeFileNotFound = pyqtSignal()
    fileOpenSuccessful = pyqtSignal()
    newDocumentCreated = pyqtSignal()
    dateTimeInserted = pyqtSignal()
    fileHandleError = pyqtSignal()
    updateAvailable = pyqtSignal()
    apiConnectError = pyqtSignal()
    fileNotFound = pyqtSignal(str)
    fileOpenError = pyqtSignal()
    settingsError = pyqtSignal()
    fileUntitled = pyqtSignal()
    fileSavedAs = pyqtSignal()
    fatalError = pyqtSignal()
    fileSaved = pyqtSignal()
    upToDate = pyqtSignal()
    apiError = pyqtSignal()
