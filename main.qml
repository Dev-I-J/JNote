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

	Component.onCompleted: {
		PyQML.checkUpdates("startup");
		PyQML.openLast();
	}

	menuBar: MenuBar{

		Menu{
			title: "File"

			MenuItem{
				text: "New"
				id: newDoc
				icon.source: "Icons/new.png"
				onTriggered: {
					windowM.title = windowM.winTitle + " - Untitled";
					mainTextArea.text = "";
					PyQML.fileNew();
					statusText.text = "New Document Created";
				}
			}

			MenuItem{
				text: "Open"
				icon.source: "Icons/open.png"
				onTriggered: fileOpenDialog.open();
			}

			MenuItem{
				text: "Save"
				icon.source: "Icons/save.png"
				onTriggered: PyQML.fileSave(mainTextArea.text);
			}

			MenuItem{
				text: "Save As"
				icon.source: "Icons/save-as.png"
				onTriggered: fileSaveDialog.open();
			}

			MenuItem{
				text: "Exit"
				icon.source: "Icons/exit.png"
				onTriggered: confirmExit.open();
			}
		}

		Menu{
			title: "Edit"

			MenuItem{
				text: "Copy"
				icon.source: "Icons/copy.png"
				enabled: mainTextArea.selectedText
				onTriggered: mainTextArea.copy();
			}

			MenuItem{
				text: "Cut"
				icon.source: "Icons/cut.png"
				enabled: mainTextArea.selectedText
				onTriggered: mainTextArea.cut();
			}

			MenuItem{
				text: "Paste"
				icon.source: "Icons/paste.png"
				onTriggered: mainTextArea.paste();
			}

			MenuItem{
				text: "Undo"
				icon.source: "Icons/undo.png"
				enabled: mainTextArea.canUndo
				onTriggered: mainTextArea.undo();
			}

			MenuItem{
				text: "Redo"
				icon.source: "Icons/redo.png"
				enabled: mainTextArea.canRedo
				onTriggered: mainTextArea.redo();
			}
		}

		Menu{
			title: "Formatting"

			MenuItem{
				text: "Font"
				icon.source: "Icons/font.png"
				onTriggered: fontDialog.open();
			}

			MenuItem{
				text: "Select Wrap Mode"
				icon.source: "Icons/word-wrap.png"
				onTriggered: wrap.open();
			}
		}

		Menu{
			title: "Help"

			MenuItem{
				text: "About"
				icon.source: "Icons/about.png"
				onTriggered:{
					about.open();
				}
			}

			MenuItem{
				text: "License"
				icon.source: "Icons/software-license.png"
				onTriggered: license.open();
			}

			MenuItem{
				text: "Check For Updates"
				icon.source: "Icons/check-update.png"
				onTriggered: PyQML.checkUpdates("");
			}
		}
	}

	header: ToolBar{

		RowLayout{
			anchors.fill: parent

			ToolButton{
				text: "New"
				icon.source: "Icons/new.png"
				onClicked: {
					windowM.title = windowM.winTitle + " - Untitled";
					mainTextArea.text = "";
					PyQML.fileNew();
					statusText.text = "New Document Created";
				}
			}

			ToolButton{
				text: "Open"
				icon.source: "Icons/open.png"
				onClicked: fileOpenDialog.open();
			}

			ToolButton{
				text: "Save"
				icon.source: "Icons/save.png"
				onClicked: PyQML.fileSave(mainTextArea.text);
			}

			ToolButton{
				text: "Save As"
				icon.source: "Icons/save-as.png"
				onClicked: fileSaveDialog.open();
			}

			ToolSeparator {}

			ToolButton{
				text: "Copy"
				icon.source: "Icons/copy.png"
				enabled: mainTextArea.selectedText
				onClicked: mainTextArea.copy();
			}

			ToolButton{
				text: "Cut"
				icon.source: "Icons/cut.png"
				enabled: mainTextArea.selectedText
				onClicked: mainTextArea.cut();
			}

			ToolButton{
				text: "Paste"
				icon.source: "Icons/paste.png"
				onClicked: mainTextArea.paste();
			}

			ToolButton{
				text: "Undo"
				icon.source: "Icons/undo.png"
				enabled: mainTextArea.canUndo
				onClicked: mainTextArea.undo()
			}

			ToolButton{
				text: "Redo"
				icon.source: "Icons/redo.png"
				enabled: mainTextArea.canRedo
				onClicked: mainTextArea.redo();
			}

			ToolSeparator {}

			ToolButton{
				text: "Font"
				icon.source: "Icons/font.png"
				onClicked: fontDialog.open();
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
				property var tmpText: ""
				font.family: "Arial"
				wrapMode: TextArea.Wrap
		        selectByMouse: true
			    selectByKeyboard: true
			    persistentSelection: true
			    onPressed: statusText.text = "Ready"
			    focus: true
		    }

		    ScrollBar.vertical: ScrollBar {policy: ScrollBar.AlwaysOn}
			ScrollBar.horizontal: ScrollBar {policy: ScrollBar.AlwaysOn}
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
				source: "Icons/logo.png"
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
				source: "Icons/logo.png"
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
		width: 600
		height: 400
		title: "Select Font"
		standardButtons: Dialog.Cancel | Dialog.Ok

		ColumnLayout{
			anchors.fill: parent

			RowLayout{
				Layout.fillWidth: true
				Layout.alignment: Qt.AlignHCenter | Qt.AlignTop

				ComboBox{
					id: fontSelector
					model: Qt.fontFamilies()
					currentIndex: 2
					onActivated: {
						previewText.font = fontSelector.currentText;
						previewText.font.pointSize = sizeSelector.currentText;
						mainTextArea.font = fontSelector.currentText;
						mainTextArea.font.pointSize = sizeSelector.currentText;
					}
				}

				ComboBox{
					id: sizeSelector
					model: ["8","11","14","16","20","24","28","32","40","56","64","72"]
					onActivated: {
						previewText.font.pointSize = sizeSelector.currentText;
						mainTextArea.font.pointSize = sizeSelector.currentText;
					}
				}

				Button{
					text: "Select Color"
					onClicked: colorSelector.open();
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
				previewText.color = colorSelector.color;
				mainTextArea.color = colorSelector.color;
			}
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
				source: "Icons/logo.png"
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
		width: 100
		height: 100
		title: "Select Wrap Mode"
		visible: false

		ColumnLayout{
			RadioButton{
				text: "Wrap"
				checked: true
				onClicked: {
					mainTextArea.wrapMode = TextArea.Wrap;
					mainTextArea.tmpText = mainTextArea.text;
					mainTextArea.text = "";
					mainTextArea.text = mainTextArea.tmpText;
					mainTextArea.tmpText = "";
				}
			}

			RadioButton{
				text: "Don't Wrap"
				onClicked: mainTextArea.wrapMode = TextArea.NoWrap;
			}
		}
	}

	MessageDialog{
		id: openError
		title: "Cannot Open File"
		text: "An Error Occured While Opening the File Because The File Type Is not Supported; Try a different File"
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
		title: "JNote is Up-To-Date"
		text: "Congratulations!! JNote is up to date."
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
		id: confirmExit
		title: "Confirm Exit"
		text: "Do You Really Want No Quit?"
		icon: StandardIcon.Warning
		standardButtons: Dialog.No | Dialog.Yes
		visible: false
		onAccepted: {
        	closing = true;
        	windowM.close();
      }
	}

	FileDialog{
		id: fileOpenDialog
		visible: false
		folder: shortcuts.documents
		signal file_path(string path)
		nameFilters: ["Text Documents (*.txt)", "All Files (*)"]
		onAccepted: {
			var path = fileUrl.toString();
	        path = path.replace(/^(file:\/{3})/,"");
	        PyQML.fileOpen(path);
	        file_path(path);
		}
	}

	FileDialog{
		id: fileSaveDialog
		visible: false
		folder: shortcuts.documents
		selectExisting: false
		nameFilters: ["Text Document (*.txt)", "All Files (*)"]
		onAccepted: {
			var path = fileUrl.toString();
	        path = path.replace(/^(file:\/{3})/,"");
	        PyQML.fileSaveAs(path, mainTextArea.text);
		}
	}

	Shortcut{
		sequence: "Ctrl+N"
		onActivated: {
			windowM.title = windowM.winTitle + " - Untitled";
			mainTextArea.text = "";
			PyQML.fileNew();
			statusText.text = "New Document Created";
		}
	}

	Shortcut{
		sequence: "Ctrl+O"
		onActivated: fileOpenDialog.open();
	}

	Shortcut{
		sequence: "Ctrl+S"
		onActivated: PyQML.fileSave(mainTextArea.text);
	}

	Shortcut{
		sequence: "Ctrl+Shift+S"
		onActivated: fileSaveDialog.open();
	}

	Shortcut{
		sequence: "Alt+F4"
		onActivated: confirmExit.open();
	}

	Connections{
		target: PyQML

		function onFileOpenSuccessful(text, path) {
			mainTextArea.text = text;
			statusText.text = "Document Opened";
			windowM.title = windowM.winTitle + " - " + path;
		}

		function onFileHandleError() {
			statusText.text = "An Unknown Error Occured While Handeling The Document";
			windowM.title = windowM.winTitle + " - Untitled";
			mainTextArea.text = "";
			handleError.open();
		}

		function onFileOpenError() {
			statusText.text = "Failed to Open File: File Type Not Supported";
			windowM.title = windowM.winTitle + " - Untitled";
			mainTextArea.text = "";
			openError.open();
		}

		function onFileUntitled() {
			statusText.text = "Document Not Saved: Save Now";
			fileSaveDialog.open();
		}

		function onFileSaved() {
			statusText.text = "Document Saved";
		}

		function onFileSavedAs(path, newText) {
			statusText.text = "Document Saved At " + path;
			windowM.title = windowM.winTitle + " - " + path;
			mainTextArea.text = newText;
		}

		function onUpdateAvailable(newVersionStr, currentVersionStr, info, date) {
		    statusText.text = "A Newer Version of JNote is Available - " + newVersionStr;
			updateText.newVersion = newVersionStr;
			updateText.currentVersion = currentVersionStr;
			updateText.info = info;
			updateText.date = date;
			update.open();
		}

		function onUpToDate(currentVersionStr) {
		    statusText.text = "JNote is up to date - " + currentVersionStr;
			updateText.currentVersion = currentVersionStr;
			upToDate.open();
		}

		function onFatalError() {
		    statusText.text = "A Fatal Error Occured!";
			fatalError.open();
		}

		function onFileNotFound() {
		    statusText.text = "JNote was unable to find that File!";
			fileNotFoundError.open();
		}

		function onApiConnectError() {
		    apiConnectError.open();
			statusText.text = "Unable to connect to API";
		}
	}

	onClosing: {
		close.accepted = closing;
		onTriggered: if(!closing) confirmExit.open();
	}
}
