from shovel import task

from os import chdir, remove
from subprocess import run as shell
from shutil import rmtree, copyfile, copytree


@task
def installDeps():
    shell("pip install --upgrade pipenv")
    shell("pipenv install --dev")


@task
def runConsole():
    shell("pipenv run python main.py")


@task
def runWindow():
    shell("pipenv run pythonw main.py")


@task
def runApp():
    shell("dist/JNote/JNote")


@task
def runAppDebug():
    shell(".test/dist/JNote/JNote")


@task
def cleanApp():
    rmtree('build', ignore_errors=True)
    rmtree('dist', ignore_errors=True)


@task
def cleanAppDebug():
    rmtree('.test/build', ignore_errors=True)
    rmtree('.test/dist', ignore_errors=True)
    rmtree('.test/icons', ignore_errors=True)
    remove(".test/fileio.py")
    remove(".test/settings.py")
    remove(".test/main.py")
    remove(".test/main.qml")
    remove(".test/settings.toml")
    remove(".test/README.md")
    remove(".test/LICENSE.md")


@task
def buildApp():
    shell("pipenv run PyInstaller JNote.spec")


@task
def buildAppDebug():
    copyfile("fileio.py", ".test/fileio.py")
    copyfile("settings.py", ".test/settings.py")
    copyfile("main.py", ".test/main.py")
    copyfile("main.qml", ".test/main.qml")
    copyfile("settings.toml", ".test/settings.toml")
    copyfile("README.md", ".test/README.md")
    copyfile("LICENSE.md", ".test/LICENSE.md")
    copytree("icons", ".test/icons")
    chdir(".test")
    shell("pipenv run PyInstaller JNote.spec")
    chdir("../")


@task
def assembleConsoleRun():
    installDeps()
    runConsole()


@task
def assembleWindowRun():
    installDeps()
    runWindow()


@task
def assembleAppRun():
    installDeps()
    cleanApp()
    buildApp()
    runApp()
