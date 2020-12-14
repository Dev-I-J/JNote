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
        return {}
