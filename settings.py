from PyQt5.QtCore import pyqtSlot
from jnote import JNote
import toml


class Settings(JNote):

    """All the Settings releted stuff for JNote goes Here"""

    def __init__(self, parent=None):
        super().__init__(parent)

    @pyqtSlot(str, str, str)
    def setSettingsStr(self, category, key, value):
        """Set string settings"""
        try:
            with open("settings.toml", "r") as settings:
                toml_object = toml.load(settings)
            toml_object[category][key] = value
            with open("settings.toml", "w") as settings:
                toml.dump(toml_object, settings)
        except FileNotFoundError:
            self.settingsFileNotFound.emit()
        except toml.TomlDecodeError:
            self.settingsError.emit()
        except BaseException:
            self.fatalError.emit()

    @pyqtSlot(str, str, int)
    def setSettingsInt(self, category, key, value):
        """Set integer settings"""
        try:
            with open("settings.toml", "r") as settings:
                toml_object = toml.load(settings)
            toml_object[category][key] = value
            with open("settings.toml", "w") as settings:
                toml.dump(toml_object, settings)
        except FileNotFoundError:
            self.settingsFileNotFound.emit()
        except toml.TomlDecodeError:
            self.settingsError.emit()
        except BaseException:
            self.fatalError.emit()

    @pyqtSlot(str, str, bool)
    def setSettingsBool(self, category, key, value):
        """Set Boolean Settings"""
        try:
            with open("settings.toml", "r") as settings:
                toml_object = toml.load(settings)
            toml_object[category][key] = value
            with open("settings.toml", "w") as settings:
                toml.dump(toml_object, settings)
        except FileNotFoundError:
            self.settingsFileNotFound.emit()
        except toml.TomlDecodeError:
            self.settingsError.emit()
        except BaseException:
            self.fatalError.emit()

    @pyqtSlot(str, result='QVariant')
    def getSettings(self, category):
        """Get any setting"""
        try:
            with open("settings.toml", "r") as settings:
                toml_object = toml.load(settings)
            return toml_object[category]
        except FileNotFoundError:
            self.settingsFileNotFound.emit()
        except toml.TomlDecodeError:
            self.settingsError.emit()
        except BaseException:
            self.fatalError.emit()
