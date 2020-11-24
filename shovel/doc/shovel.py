from shovel import task

from os import chdir
from shutil import rmtree
from os.path import abspath, join
from subprocess import run as shell
from webbrowser import open_new_tab


@task
def installDevDeps():
    """Install Dependencies For Building Docs"""
    shell("pip install pipenv")
    shell("pipenv install --dev")


@task
def cleanDoc():
    """Clean Docs Build Output"""
    rmtree('docs/build', ignore_errors=True)


@task
def runDoc():
    """Open Docs In New Browser Tab"""
    open_new_tab(
        "file://{}".format(join(abspath("."), "docs/build/html/index.html"))
    )


@task
def buildDoc():
    """Build Docs With 'make.bat' Or 'MakeFile'"""
    chdir("docs")
    shell("pipenv run make html")
    chdir("../")


@task
def assembleDocRun():
    """Install Dependencies, Clean, Build And Open Docs"""
    installDevDeps()
    cleanDoc()
    buildDoc()
    runDoc()
