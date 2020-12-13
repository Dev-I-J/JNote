from PyQt5.QtCore import QObject, pyqtSignal


class Signals(QObject):

    """Base Class For JNote"""

    def __init__(self) -> None:
        QObject.__init__(self)

    platformNotSupported: pyqtSignal = pyqtSignal(str)
    settingsFileNotFound: pyqtSignal = pyqtSignal()
    licenseFileNotFound: pyqtSignal = pyqtSignal()
    readmeFileNotFound: pyqtSignal = pyqtSignal()
    fileOpenSuccessful: pyqtSignal = pyqtSignal()
    newDocumentCreated: pyqtSignal = pyqtSignal()
    dateTimeInserted: pyqtSignal = pyqtSignal()
    fileHandleError: pyqtSignal = pyqtSignal()
    updateAvailable: pyqtSignal = pyqtSignal()
    apiConnectError: pyqtSignal = pyqtSignal()
    fileNotFound: pyqtSignal = pyqtSignal(str)
    fileOpenError: pyqtSignal = pyqtSignal()
    settingsError: pyqtSignal = pyqtSignal()
    fileUntitled: pyqtSignal = pyqtSignal()
    fileSavedAs: pyqtSignal = pyqtSignal()
    fatalError: pyqtSignal = pyqtSignal()
    fileSaved: pyqtSignal = pyqtSignal()
    upToDate: pyqtSignal = pyqtSignal()
    apiError: pyqtSignal = pyqtSignal()
