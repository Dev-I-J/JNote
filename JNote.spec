# -*- mode: python ; coding: utf-8 -*-

from os.path import abspath as path
from sys import platform

block_cipher = None

excluded_libs = [
    'tcl',
    'tcl86t',
    'tk',
    'tk86t',
    '_tkinter'
]

data = [
    ("main.qml", "."),
    ("settings.toml", "."),
    ("LICENSE.md", "."),
    ("README.md", "."),
    ("icons", "icons")
]


a = Analysis(['main.py'],
             pathex=[path(".")],
             binaries=[],
             datas=data,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=excluded_libs,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='JNote',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False, icon="icons/favicon.ico")

if platform == "darwin":
    app = BUNDLE(exe,
         name='JNote.app',
         icon="icons/favicon.icns",
         bundle_identifier=None)
else:
    coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='JNote')