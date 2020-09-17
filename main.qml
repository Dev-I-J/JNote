import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.14
import QtQuick.Dialogs 1.3

ApplicationWindow{
    id: windowM
    property string winTitle: "JNote: A Free NotePad"
    property bool closing: false
    visible: true
    width: 800
    height: 600
    title: winTitle + " - Untitled"

    Component.onCompleted: JNote.checkUpdates(true)

    menuBar: MenuBar{

        Menu{
            title: "File"

            MenuItem{
                text: "New"
                id: newDoc
                icon.source: "icons/new.png"
                onTriggered: FileIO.fileNew()
            }

            MenuItem{
                text: "Open"
                icon.source: "icons/open.png"
                onTriggered: fileOpenDialog.open()
            }

            MenuItem{
                text: "Save"
                icon.source: "icons/save.png"
                onTriggered: FileIO.fileSave(mainTextArea.text)
            }

            MenuItem{
                text: "Save As"
                icon.source: "icons/save-as.png"
                onTriggered: fileSaveDialog.open()
            }

            MenuItem{
                text: "Exit"
                icon.source: "icons/exit.png"
                onTriggered: confirmExit.open()
            }
        }

        Menu{
            title: "Edit"

            MenuItem{
                text: "Copy"
                icon.source: "icons/copy.png"
                enabled: mainTextArea.selectedText
                onTriggered: mainTextArea.copy()
            }

            MenuItem{
                text: "Cut"
                icon.source: "icons/cut.png"
                enabled: mainTextArea.selectedText
                onTriggered: mainTextArea.cut()
            }

            MenuItem{
                text: "Paste"
                icon.source: "icons/paste.png"
                enabled: mainTextArea.canPaste
                onTriggered: mainTextArea.paste()
            }

            MenuItem{
                text: "Undo"
                icon.source: "icons/undo.png"
                enabled: mainTextArea.canUndo
                onTriggered: mainTextArea.undo()
            }

            MenuItem{
                text: "Redo"
                icon.source: "icons/redo.png"
                enabled: mainTextArea.canRedo
                onTriggered: mainTextArea.redo()
            }

            MenuItem{
                text: "Insert Date and Time"
                icon.source: "icons/date-time.png"
                onTriggered: mainTextArea.text += JNote.insertDateTime()
            }

            MenuItem{
                text: "Find"
                icon.source: "icons/find.png"
                onTriggered: find.open()
            }
        }

        Menu{
            title: "Formatting"

            MenuItem{
                text: "Font"
                icon.source: "icons/font.png"
                onTriggered: fontDialog.open()
            }

            MenuItem{
                text: "Select Wrap Mode"
                icon.source: "icons/word-wrap.png"
                onTriggered: wrap.open()
            }
        }

        Menu{
            title: "Help"

            MenuItem{
                text: "About"
                icon.source: "icons/about.png"
                onTriggered: about.open()
            }

            MenuItem{
                text: "License"
                icon.source: "icons/software-license.png"
                onTriggered: license.open()
            }

            MenuItem{
                text: "Check For Updates"
                icon.source: "icons/check-update.png"
                onTriggered: JNote.checkUpdates(false)
            }
        }
    }

    header: ToolBar{

        RowLayout{
            anchors.fill: parent

            ToolButton{
                text: "New"
                icon.source: "icons/new.png"
                onClicked: FileIO.fileNew()
            }

            ToolButton{
                text: "Open"
                icon.source: "icons/open.png"
                onClicked: fileOpenDialog.open()
            }

            ToolButton{
                text: "Save"
                icon.source: "icons/save.png"
                onClicked: FileIO.fileSave(mainTextArea.text)
            }

            ToolButton{
                text: "Save As"
                icon.source: "icons/save-as.png"
                onClicked: fileSaveDialog.open()
            }

            ToolSeparator {}

            ToolButton{
                text: "Copy"
                icon.source: "icons/copy.png"
                enabled: mainTextArea.selectedText
                onClicked: mainTextArea.copy()
            }

            ToolButton{
                text: "Cut"
                icon.source: "icons/cut.png"
                enabled: mainTextArea.selectedText
                onClicked: mainTextArea.cut()
            }

            ToolButton{
                text: "Paste"
                icon.source: "icons/paste.png"
                enabled: mainTextArea.canPaste
                onClicked: mainTextArea.paste()
            }

            ToolButton{
                text: "Undo"
                icon.source: "icons/undo.png"
                enabled: mainTextArea.canUndo
                onClicked: mainTextArea.undo()
            }

            ToolButton{
                text: "Redo"
                icon.source: "icons/redo.png"
                enabled: mainTextArea.canRedo
                onClicked: mainTextArea.redo()
            }

            ToolSeparator {}

            ToolButton{
                text: "Font"
                icon.source: "icons/font.png"
                onClicked: fontDialog.open()
            }
        }
    }

    footer: ToolBar{

        palette{
            base: "grey"
        }

        RowLayout{
            anchors.fill: parent

            Text{
                id: statusText
                text: "Ready"
                Layout.alignment: Qt.AlignRight
                rightPadding: 15
                leftPadding: 2
            }
        }
    }

    FocusScope{
        anchors.fill: parent
        focus: true

        Flickable {
            anchors.fill: parent

            TextArea.flickable: TextArea {
                id: mainTextArea
                property string tmpText: ""
                property int lastUsedFontIndex: 2
                property int lastUsedSizeIndex: 0
                property string lastUsedColor: "#000000"
                property string lastUsedFont: "Arial"
                property int lastUsedSize: 8
                property bool lastUsedUnderline: false
                property bool lastUsedStrikeout: false
                property bool lastUsedBold: false
                property bool lastUsedItalic: false
                font.family: "Arial"
                font.pointSize: 8
                wrapMode: TextArea.Wrap
                selectByMouse: true
                selectByKeyboard: true
                persistentSelection: true
                onPressed: statusText.text = "Ready"
                Component.onCompleted: {
                    mainTextArea.font = Settings.getSettings("last-used-formatting")["font"]
                    mainTextArea.font.pointSize = Settings.getSettings("last-used-formatting")["size"]
                    mainTextArea.color = Settings.getSettings("last-used-formatting")["color"]
                    mainTextArea.font.underline = Settings.getSettings("last-used-formatting")["underline"]
                    mainTextArea.font.strikeout = Settings.getSettings("last-used-formatting")["strikeout"]
                    mainTextArea.font.bold = Settings.getSettings("last-used-formatting")["bold"]
                    mainTextArea.font.italic = Settings.getSettings("last-used-formatting")["italic"]
                    if (Settings.getSettings("last-used-file")["untitled"]) {
                        mainTextArea.text = Settings.getSettings("last-used-file")["text"]
                    }
                    else {
                        mainTextArea.text = FileIO.fileOpen(FileIO.getLastOpenFilePath())
                        statusText.text = "Document " + Settings.getSettings("last-used-file")["path"] + " Opened Successfuly"
                        windowM.title = windowM.winTitle + " - " + Settings.getSettings("last-used-file")["path"]
                    }
                }
            }

            ScrollBar.vertical: ScrollBar {}
            ScrollBar.horizontal: ScrollBar {}
        }
    }

    Dialog{
        id: license
        visible: false
        title: 'License - JNote'
        width: 400
        height: 400

        ColumnLayout{
            anchors.fill: parent

            Image{
                source: "icons/logo.png"
                Layout.alignment: Qt.AlignHCenter
            }

            TextArea{
                text: 'JNote is licensed under The GNU General Public License v3
(https://www.gnu.org/licenses/gpl-3.0.txt)'
                readOnly: true
                selectByMouse: true
                selectByKeyboard: true
                Layout.alignment: Qt.AlignHCenter
            }
        }
    }

    Dialog{
        id: update
        visible: false
        title: 'Update - JNote'
        standardButtons: Dialog.No | Dialog.Yes
        width: 400
        height: 600
        onYes: Qt.openUrlExternally("https://github.com/Dev-I-J/JNote/releases/latest")

        ColumnLayout{
            anchors.fill: parent

            Image{
                source: "icons/logo.png"
                Layout.alignment: Qt.AlignHCenter
            }

            Text{
                id: updateText
                property string newVersion: ""
                property string currentVersion: ""
                property string info: ""
                property string date: ""
                text: '<p>An Update is available for JNote.<br><br>Updates may contain bugfixes, security patches or new features.<br><br>You can see the details of the update below.<br><br>Current Version = ' + updateText.currentVersion + '<br>New Version = ' + updateText.newVersion + '<br>Published At = ' + updateText.date +'<br>' + updateText.info + '<br><br>Do You Want To Update?'
                Layout.alignment: Qt.AlignHCenter
            }
        }
    }

    Dialog{
        id: fontDialog
        property string fontFamily: "Arial"
        property int fontSize: 8
        property int fontSizeIndex: 0
        property int fontIndex: 2
        property string fontColor: "Black"
        property bool underline: false
        property bool strikeout: false
        property bool bold: false
        property bool italic: false
        width: 600
        height: 400
        title: "Select Font"
        standardButtons: Dialog.Cancel | Dialog.Ok
        visible: false

        ColumnLayout{
            anchors.fill: parent

            RowLayout{
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignHCenter | Qt.AlignTop

                ComboBox{
                    id: fontSelector
                    model: Qt.fontFamilies()
                    currentIndex: fontDialog.fontIndex
                    onActivated: {
                        fontDialog.fontFamily = fontSelector.currentText
                        fontDialog.fontIndex = fontSelector.currentIndex
                        fontDialog.fontSize = sizeSelector.currentText
                        fontDialog.fontSizeIndex = sizeSelector.currentIndex
                        previewText.font = fontSelector.currentText
                        previewText.font.pointSize = sizeSelector.currentText
                    }
                    onModelChanged: {
                        var _maxWidth = 0
                        for(var i = 0; i < model.length; i++){
                            _maxWidth = Math.max((model[i].length+1)*Qt.application.font.pixelSize, _maxWidth)
                        }
                        Layout.minimumWidth = _maxWidth + implicitIndicatorWidth + leftPadding + rightPadding
                    }
                }

                ComboBox {
                    id: sizeSelector
                    model: []
                    onActivated: {
                        previewText.font.pointSize = sizeSelector.currentText
                        fontDialog.fontSize = sizeSelector.currentText
                        fontDialog.fontSizeIndex = sizeSelector.currentIndex
                    }
                    Component.onCompleted: {
                        var tempSizeModel = new Array()
                        for (var i=8; i<=100; i++) {
                            tempSizeModel.push(i)
                        }
                        sizeSelector.model = tempSizeModel
                    }
                }

                Button{
                    text: "Select Color"
                    onClicked: colorSelector.open()
                }
            }
            RowLayout {
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignHCenter | Qt.AlignTop

                CheckBox {
                    Layout.minimumWidth: 100
                    Layout.margins: 20
                    id: underlineText
                    text: "Underline"
                    font.underline: true

                    onToggled: {
                        fontDialog.underline = underlineText.checked
                        previewText.font.underline = underlineText.checked
                    }
                }

                CheckBox {
                    Layout.minimumWidth: 100
                    Layout.margins: 20
                    id: strikeoutText
                    text: "Strikeout"
                    font.strikeout: true

                    onToggled: {
                        fontDialog.strikeout = strikeoutText.checked
                        previewText.font.strikeout = strikeoutText.checked
                    }
                }

                CheckBox {
                    Layout.minimumWidth: 100
                    Layout.margins: 20
                    id: boldText
                    text: "Bold"
                    font.bold: true

                    onToggled: {
                        fontDialog.bold = boldText.checked
                        previewText.font.bold = boldText.checked
                    }
                }

                CheckBox {
                    Layout.minimumWidth: 100
                    Layout.margins: 20
                    id: italicText
                    text: "Italic"
                    font.italic: true

                    onToggled: {
                        fontDialog.italic = italicText.checked
                        previewText.font.italic = italicText.checked
                    }
                }
            }
            TextArea{
                id: previewText
                text: "ABCD efg"
                font.family: "Arial"
                Layout.alignment: Qt.AlignHCenter
            }
        }

        ColorDialog{
            id: colorSelector
            onAccepted: {
                previewText.color = colorSelector.color
                fontDialog.fontColor = colorSelector.color
            }
        }
        onAccepted: {
            mainTextArea.font = fontDialog.fontFamily
            mainTextArea.lastUsedFontIndex = fontDialog.fontIndex
            mainTextArea.lastUsedFont = fontDialog.fontFamily
            mainTextArea.font.pointSize = fontDialog.fontSize
            mainTextArea.lastUsedSize = fontDialog.fontSize
            mainTextArea.lastUsedSizeIndex = fontDialog.fontSizeIndex
            mainTextArea.color = fontDialog.fontColor
            mainTextArea.lastUsedColor = fontDialog.fontColor
            mainTextArea.font.underline = fontDialog.underline
            mainTextArea.lastUsedUnderline = fontDialog.underline
            mainTextArea.font.strikeout = fontDialog.strikeout
            mainTextArea.lastUsedStrikeout = fontDialog.strikeout
            mainTextArea.font.bold = fontDialog.bold
            mainTextArea.lastUsedBold = fontDialog.bold
            mainTextArea.font.italic = fontDialog.italic
            mainTextArea.lastUsedItalic = fontDialog.italic
        }
        onRejected: {
            fontSelector.currentIndex = mainTextArea.lastUsedFontIndex
            sizeSelector.currentIndex = mainTextArea.lastUsedSizeIndex
            colorSelector.color = mainTextArea.lastUsedColor
            underlineText.checked = mainTextArea.lastUsedUnderline
            strikeoutText.checked = mainTextArea.lastUsedStrikeout
            boldText.checked = mainTextArea.lastUsedBold
            italicText.checked = mainTextArea.lastUsedItalic
            fontDialog.fontColor = mainTextArea.lastUsedColor
            fontDialog.fontIndex = mainTextArea.lastUsedFontIndex
            fontDialog.fontSizeIndex = mainTextArea.lastUsedSizeIndex
            fontDialog.fontFamily = mainTextArea.lastUsedFont
            fontDialog.fontSize = mainTextArea.lastUsedSize
            fontDialog.underline = mainTextArea.lastUsedUnderline
            fontDialog.strikeout = mainTextArea.lastUsedStrikeout
            fontDialog.bold = mainTextArea.lastUsedBold
            fontDialog.italic = mainTextArea.lastUsedItalic
            previewText.font = mainTextArea.lastUsedFont
            previewText.font.pointSize = mainTextArea.lastUsedSize
            previewText.color = mainTextArea.lastUsedColor
            previewText.font.underline = mainTextArea.lastUsedUnderline
            previewText.font.strikeout = mainTextArea.lastUsedStrikeout
            previewText.font.bold = mainTextArea.lastUsedBold
            previewText.font.italic = mainTextArea.lastUsedItalic
        }
        Component.onCompleted: {
            fontSelector.currentIndex = Settings.getSettings("last-used-formatting")["fontIndex"]
            sizeSelector.currentIndex = Settings.getSettings("last-used-formatting")["sizeIndex"]
            colorSelector.color = Settings.getSettings("last-used-formatting")["color"]
            underlineText.checked = Settings.getSettings("last-used-formatting")["underline"]
            strikeoutText.checked = Settings.getSettings("last-used-formatting")["strikeout"]
            boldText.checked = Settings.getSettings("last-used-formatting")["bold"]
            italicText.checked = Settings.getSettings("last-used-formatting")["italic"]
            fontDialog.fontColor = Settings.getSettings("last-used-formatting")["color"]
            fontDialog.fontIndex = Settings.getSettings("last-used-formatting")["fontIndex"]
            fontDialog.fontSizeIndex = Settings.getSettings("last-used-formatting")["sizeIndex"]
            fontDialog.fontFamily = Settings.getSettings("last-used-formatting")["font"]
            fontDialog.fontSize = Settings.getSettings("last-used-formatting")["size"]
            fontDialog.underline = Settings.getSettings("last-used-formatting")["underline"]
            fontDialog.strikeout = Settings.getSettings("last-used-formatting")["strikeout"]
            fontDialog.bold = Settings.getSettings("last-used-formatting")["bold"]
            fontDialog.italic = Settings.getSettings("last-used-formatting")["italic"]
            previewText.font = Settings.getSettings("last-used-formatting")["font"]
            previewText.font.pointSize = Settings.getSettings("last-used-formatting")["size"]
            previewText.color = Settings.getSettings("last-used-formatting")["color"]
            previewText.font.underline = Settings.getSettings("last-used-formatting")["underline"]
            previewText.font.strikeout = Settings.getSettings("last-used-formatting")["strikeout"]
            previewText.font.bold = Settings.getSettings("last-used-formatting")["bold"]
            previewText.font.italic = Settings.getSettings("last-used-formatting")["italic"]
            mainTextArea.lastUsedFont = Settings.getSettings("last-used-formatting")["font"]
            mainTextArea.lastUsedFontIndex = Settings.getSettings("last-used-formatting")["fontIndex"]
            mainTextArea.lastUsedSize = Settings.getSettings("last-used-formatting")["size"]
            mainTextArea.lastUsedSizeIndex = Settings.getSettings("last-used-formatting")["sizeIndex"]
            mainTextArea.lastUsedColor = Settings.getSettings("last-used-formatting")["color"]
            mainTextArea.lastUsedUnderline = Settings.getSettings("last-used-formatting")["underline"]
            mainTextArea.lastUsedStrikeout = Settings.getSettings("last-used-formatting")["strikeout"]
            mainTextArea.lastUsedBold = Settings.getSettings("last-used-formatting")["bold"]
            mainTextArea.lastUsedItalic = Settings.getSettings("last-used-formatting")["italic"]
        }
    }

    Dialog{
        id: about
        width: 400
        height: 400
        title: "About - JNote"
        visible: false

        ColumnLayout{
            anchors.fill: parent

            Image{
                source: "icons/logo.png"
                Layout.alignment: Qt.AlignHCenter
            }

            TextArea{
                text: 'JNote is a Free and Open Source Plain Text Editor licensed
under the GNU GPL v3 Open Source License Tou can use this application for free for
Personal use, Educational Use, and even Commercial Use for free! The code is available
on GiHub for free at this url - https://www.github.com/Dev-I-J/JNote.

All the icons used in this application is provided by Icons8 for FREE.

Developer info - This application is written in Python and QML.
The modules PyQt5, requests, version_parser and sys are used.
The GitHub API Service is used to detect new versions.'
                Layout.alignment: Qt.AlignHCenter
                readOnly: true
                selectByMouse: true
                selectByKeyboard: true
            }
        }
    }

    Dialog{
        id: wrap
        width: 200
        height: 100
        title: "Select Wrap Mode"
        visible: false

        ColumnLayout{
            RadioButton{
                id: wrapText
                text: "Wrap"
                checked: true
                onClicked: {
                    mainTextArea.wrapMode = TextArea.Wrap
                    mainTextArea.tmpText = mainTextArea.text
                    mainTextArea.text = ""
                    mainTextArea.text = mainTextArea.tmpText
                    mainTextArea.tmpText = ""
                }
            }

            RadioButton{
                id: doNotWrapText
                text: "Don't Wrap"
                onClicked: mainTextArea.wrapMode = TextArea.NoWrap
            }
        }
        Component.onCompleted: {
            if (Settings.getSettings("last-used-formatting")["wrap"]) {
                wrapText.checked = true
                mainTextArea.wrapMode = TextArea.Wrap
                mainTextArea.tmpText = mainTextArea.text
                mainTextArea.text = ""
                mainTextArea.text = mainTextArea.tmpText
                mainTextArea.tmpText = ""
            }
            else {
                doNotWrapText.checked = true
                mainTextArea.wrapMode = TextArea.NoWrap
            }
        }
    }

    Dialog {
        id: find
        title: "Find"
        width: 200
        height: 100
        standardButtons: StandardButton.NoButton
        visible: false

        ColumnLayout {
            anchors.fill: parent

            TextField {
                Layout.alignment: Qt.AlignHCenter
                id: findInput
                text: ""
                placeholderText: "Put your text here!"
                selectByMouse: true
                persistentSelection: true
                maximumLength: findInput.length + 1
                onAccepted: findButton.clicked()
            }

            RowLayout {
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignHCenter

                CheckBox {
                    id: isRegex
                    text: "Use RegEx"
                }

                CheckBox {
                    id: isCasesensitive
                    text: "Case Sensitive"
                }
            }

            Button {
                Layout.alignment: Qt.AlignHCenter
                id: findButton
                property int pos: 0
                text: "Find Text"
                enabled: findInput.text
                onClicked: {
                    var results = JNote.findText(findInput.text, mainTextArea.text, isCasesensitive.checked, isRegex.checked)
                    if (results.length == 0) {
                        findMatchNotFound.pattern = findInput.text
                        findMatchNotFound.open()
                    }
                    mainTextArea.select(results[pos][0], results[pos][1])
                    pos++
                    if (pos == results.length) {
                        pos = 0
                    }
                }
            }
        }
    }

    MessageDialog{
        id: openError
        title: "Cannot Open File"
        text: "An Error Occured While Opening the File Because The File Type Is not Supported. Try a different File"
        icon: StandardIcon.Warning
        visible: false
    }

    MessageDialog{
        id: handleError
        title: "An Unknown Error Occured"
        text: "An Unknown Error Occured While Handeling The Document."
        icon: StandardIcon.Warning
        visible: false
    }

    MessageDialog{
        id: upToDate
        property string currentVersion: ""
        title: "JNote is Up-To-Date"
        text: "Congratulations!! JNote is up to date - " + upToDate.currentVersion
        icon: StandardIcon.Information
        visible: false
    }

    MessageDialog{
        id: fatalError
        title: "Fatal Error"
        text: "A Fatal Error Occured!"
        icon: StandardIcon.Critical
        onAccepted: Qt.quit()
        onRejected: Qt.quit()
        visible: false
    }

    MessageDialog{
        id: fileNotFoundError
        title: "File Not Found"
        text: "Unable to Find That File!"
        icon: StandardIcon.Warning
        visible: false
    }

    MessageDialog{
        id: apiConnectError
        title: "Failed To Connect to API"
        text: "JNote was unable to conect to the GitHub API to check for new updates."
        icon: StandardIcon.Warning
        visible: false
    }

    MessageDialog{
        id: settingsError
        title: "Failed To Save Settings"
        text: "A Fatal Error Occured While JNote is Saving Your Preferenses."
        icon: StandardIcon.Critical
        onAccepted: Qt.quit()
        onRejected: Qt.quit()
        visible: false
    }

    MessageDialog{
        id: settingsNotFoundError
        title: "Failed To Find Settings File"
        text: "JNote Was Not Able To Find settings.json. JNote will not work correctly without it!"
        icon: StandardIcon.Critical
        onAccepted: Qt.quit()
        onRejected: Qt.quit()
        visible: false
    }

    MessageDialog {
        id: findMatchNotFound
        property string pattern: ""
        title: "Match Not Found"
        text: 'Unable to Find Any Match for "' + findMatchNotFound.pattern + '"!'
        icon: StandardIcon.Information
        visible: false
    }

    MessageDialog{
        id: confirmExit
        title: "Confirm Exit"
        text: "Do You Really Want To Quit?"
        icon: StandardIcon.Warning
        standardButtons: Dialog.No | Dialog.Yes
        visible: false
        onAccepted: {
            if (Settings.getSettings("last-used-file")["untitled"]) {
                Settings.setSettingsStr("last-used-file", "text", mainTextArea.text)
            }
            else {
                Settings.setSettingsStr("last-used-file", "text", "")
            }
            Settings.setSettingsStr("last-used-formatting", "font", fontDialog.fontFamily)
            Settings.setSettingsStr("last-used-formatting", "color", fontDialog.fontColor)
            Settings.setSettingsInt("last-used-formatting", "fontIndex", fontDialog.fontIndex)
            Settings.setSettingsInt("last-used-formatting", "size", fontDialog.fontSize)
            Settings.setSettingsInt("last-used-formatting", "sizeIndex", fontDialog.fontSizeIndex)
            Settings.setSettingsBool("last-used-formatting", "wrap", wrapText.checked)
            Settings.setSettingsBool("last-used-formatting", "underline", fontDialog.underline)
            Settings.setSettingsBool("last-used-formatting", "strikeout", fontDialog.strikeout)
            Settings.setSettingsBool("last-used-formatting", "bold", fontDialog.bold)
            Settings.setSettingsBool("last-used-formatting", "italic",fontDialog.italic)
            Settings.addComments()
            windowM.closing = true
            windowM.close()
      }
    }

    FileDialog{
        id: fileOpenDialog
        property string path: ""
        visible: false
        folder: shortcuts.documents
        nameFilters: ["Text Documents (*.txt)", "All Files (*)"]
        onAccepted: {
            fileOpenDialog.path = fileUrl.toString()
            fileOpenDialog.path = fileOpenDialog.path.replace(/^(file:\/{3})/,"")
            mainTextArea.text = FileIO.fileOpen(fileOpenDialog.path)
        }
    }

    FileDialog{
        id: fileSaveDialog
        property string path: ""
        visible: false
        folder: shortcuts.documents
        selectExisting: false
        nameFilters: ["Text Document (*.txt)", "All Files (*)"]
        onAccepted: {
            fileSaveDialog.path = fileUrl.toString()
            fileSaveDialog.path = fileSaveDialog.path.replace(/^(file:\/{3})/,"")
            FileIO.fileSaveAs(fileSaveDialog.path, mainTextArea.text)
        }
    }

    Shortcut{
        sequence: "Ctrl+N"
        onActivated: FileIO.fileNew()
    }

    Shortcut{
        sequence: "Ctrl+O"
        onActivated: fileOpenDialog.open()
    }

    Shortcut{
        sequence: "Ctrl+S"
        onActivated: FileIO.fileSave(mainTextArea.text)
    }

    Shortcut{
        sequence: "Ctrl+Shift+S"
        onActivated: fileSaveDialog.open()
    }

    Shortcut{
        sequence: "Ctrl+F"
        onActivated: find.open()
    }

    Shortcut{
        sequence: "F5"
        onActivated: mainTextArea.text += JNote.insertDateTime()
    }

    Connections {
        target: JNote

        function onUpdateAvailable() {
            statusText.text = "A Newer Version of JNote is Available - " + JNote.updateInfo["newVersion"]
            updateText.newVersion = JNote.updateInfo["newVersion"]
            updateText.currentVersion = JNote.updateInfo["currentVersion"]
            updateText.info = JNote.updateInfo["details"]
            updateText.date = JNote.updateInfo["date"]
            update.open()
        }

        function onUpToDate() {
            statusText.text = "JNote is up to date - " + JNote.updateInfo["currentVersion"]
            upToDate.currentVersion = JNote.updateInfo["currentVersion"]
            upToDate.open()
        }

        function onFatalError() {
            statusText.text = "A Fatal Error Occured!"
            fatalError.open()
        }

        function onDateTimeInserted() {
            statusText.text = "Date and Time Inserted"
        }
    }
    Connections{
        target: FileIO

        function onNewDocumentCreated() {
            windowM.title = windowM.winTitle + " - Untitled"
            mainTextArea.text = ""
            statusText.text = "New Document Created"
        }

        function onFileOpenSuccessful() {
            statusText.text = "Document " + fileOpenDialog.path + " Opened Successfuly"
            windowM.title = windowM.winTitle + " - " + fileOpenDialog.path
        }

        function onFileHandleError() {
            statusText.text = "An Unknown Error Occured While Handeling The Document"
            windowM.title = windowM.winTitle + " - Untitled"
            mainTextArea.text = ""
            handleError.open()
        }

        function onFileOpenError() {
            statusText.text = "Failed to Open File: File Type Not Supported"
            windowM.title = windowM.winTitle + " - Untitled"
            mainTextArea.text = ""
            openError.open()
        }

        function onFileUntitled() {
            statusText.text = "Document Not Saved: Save Now"
            fileSaveDialog.open()
        }

        function onFileSaved() {
            statusText.text = "Document Saved"
        }

        function onFileSavedAs() {
            statusText.text = "Document Saved At " + fileSaveDialog.path
            windowM.title = windowM.winTitle + " - " + fileSaveDialog.path
        }

        function onFatalError() {
            statusText.text = "A Fatal Error Occured!"
            fatalError.open()
        }

        function onFileNotFound() {
            statusText.text = "JNote was unable to find that File!"
            fileNotFoundError.open()
        }

        function onApiConnectError() {
            apiConnectError.open()
            statusText.text = "Unable to connect to API"
        }
    }

    Connections {
        target: Settings

        function onSettingsFileNotFound() {
            settingsNotFoundError.open()
            statusText.text = "Unable to Find Settings File"
        }
        function onSettingsError() {
            settingsError.open()
            statusText.text = "Fatal Error While Saving Settings"
        }

        function onFatalError() {
            statusText.text = "A Fatal Error Occured!"
            fatalError.open()
        }
    }

    onClosing: {
        close.accepted = windowM.closing
        onTriggered: if(!windowM.closing) confirmExit.open()
    }
}
