#define JAppName "JNote"
#define JAppVersion "1.6.7"
#define JAppPublisher "Induwara Jayaweera"
#define JAppURL "http://www.github.com/dev-i-j/jnote"
#define JAppExeName "JNote.exe"

[Setup]
AppId={{FF21436A-C5D8-442A-9CC4-6FA8C6D0E84A}
AppName={#JAppName}
AppVersion={#JAppVersion}
AppPublisher={#JAppPublisher}
AppPublisherURL={#JAppURL}
AppSupportURL={#JAppURL}
AppUpdatesURL={#JAppURL}
DefaultDirName={commonpf}\{#JAppName}
DefaultGroupName={#JAppName}
AllowNoIcons=yes
LicenseFile=.\LICENSE.txt
OutputDir=.
OutputBaseFilename={#JAppName}_{#JAppVersion}_Installer
SetupIconFile=.\icons\favicon.ico
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest
DisableWelcomePage=no
DisableDirPage=no

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[CustomMessages]
CurrentUser=For the current user only
AllUsers=For all users

[Tasks]
Name: desktopicon; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "Additional icons:";
Name: desktopicon\common; Description: "{cm:AllUsers}"; GroupDescription: "Additional icons:"; Flags: exclusive
Name: desktopicon\user; Description: "{cm:CurrentUser}"; GroupDescription: "Additional icons:"; Flags: exclusive unchecked

[Files]
Source: "D:\Dev\Wing\JNote\dist\JNote\JNote.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dev\Wing\JNote\dist\JNote\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#JAppName}"; Filename: "{app}\{#JAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#JAppName}}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\{#JAppName}"; Filename: "{app}\{#JAppExeName}"; Tasks: desktopicon/common
Name: "{userdesktop}\{#JAppName}"; Filename: "{app}\{#JAppExeName}"; Tasks: desktopicon/user

[Run]
Filename: "{app}\{#JAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(JAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
