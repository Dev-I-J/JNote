from shovel import task

from shutil import rmtree
from subprocess import run as shell


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
def cleanApp():
    rmtree('build', ignore_errors=True)
    rmtree('dist', ignore_errors=True)


@task
def buildApp():
    shell("pipenv run PyInstaller JNote.spec")


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
