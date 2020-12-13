from PyQt5.QtCore import pyqtSlot
from signals import Signals
import toml

# Typing Imports
from typing import Dict, Any


class Settings(Signals):

    """All the Settings related stuff for JNote goes Here"""

    def __init__(self) -> None:
        Signals.__init__(self)

    @pyqtSlot(str, str, str)
    def setSettingsStr(self, category: str, key: str, value: str) -> None:
        """Set string settings"""
        try:
            with open("settings.toml", "r") as settings:
                toml_object: Dict[str, Any] = toml.load(settings)
            toml_object[category][key] = value
            with open("settings.toml", "w") as settings:
                toml.dump(toml_object, settings)
        except FileNotFoundError:
            self.settingsFileNotFound.emit()
        except toml.TomlDecodeError:
            self.settingsError.emit()
        except Exception:
            self.fatalError.emit()

    @pyqtSlot(str, str, int)
    def setSettingsInt(self, category: str, key: str, value: int) -> None:
        """Set integer settings"""
        try:
            with open("settings.toml", "r") as settings:
                toml_object: Dict[str, Any] = toml.load(settings)
            toml_object[category][key] = value
            with open("settings.toml", "w") as settings:
                toml.dump(toml_object, settings)
        except FileNotFoundError:
            self.settingsFileNotFound.emit()
        except toml.TomlDecodeError:
            self.settingsError.emit()
        except Exception:
            self.fatalError.emit()

    @pyqtSlot(str, str, bool)
    def setSettingsBool(self, category: str, key: str, value: bool) -> None:
        """Set Boolean Settings"""
        try:
            with open("settings.toml", "r") as settings:
                toml_object: Dict[str, Any] = toml.load(settings)
            toml_object[category][key] = value
            with open("settings.toml", "w") as settings:
                toml.dump(toml_object, settings)
        except FileNotFoundError:
            self.settingsFileNotFound.emit()
        except toml.TomlDecodeError:
            self.settingsError.emit()
        except Exception:
            self.fatalError.emit()

    @pyqtSlot(str, result='QVariant')
    def getSettings(self, category: str) -> Dict[str, Any]:
        """Get any setting"""
        try:
            with open("settings.toml", "r") as settings:
                toml_object: Dict[str, Any] = toml.load(settings)
                return toml_object[category]
        except FileNotFoundError:
            self.settingsFileNotFound.emit()
        except toml.TomlDecodeError:
            self.settingsError.emit()
        except Exception:
            self.fatalError.emit()

    @staticmethod
    def addComments() -> None:
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
