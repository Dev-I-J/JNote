from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from jnote import JNote
import sys


def run() -> int:
    """
    Function To Run The Script

    Returns:
        int: App Exit Code
    """

    jnote: JNote = JNote()

    app: QApplication = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icons/favicon.png'))
    app.setOrganizationName("JNote")
    app.setOrganizationDomain("jnote.ml")

    engine: QQmlApplicationEngine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("JNote", jnote)
    engine.load(QUrl('main.qml'))

    if not engine.rootObjects():
        return -1

    return app.exec()


if __name__ == '__main__':
    sys.exit(run())
