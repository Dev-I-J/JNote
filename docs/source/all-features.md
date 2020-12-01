# All Features

This page lists and documents all the features of JNote.

## General Features

All the general features of JNote. Eg:- Create New Document, Open File, etc.

### Create New Document

Creates a new document, ie:- Clears the Editing Area.
Also displays the message "New Document Created" in The Status Bar.

#### Errors That Can Occur While Creating a New Document

| Dialog Title | Meaning |
| :---: | :---: |
| Fatal Error | Fatal internal error |

If failed, a "Fatal Error" dialog will appear.

### Open File

Opens an Existing file.
The opened file path is appended to the title like `JNote: A Free NotePad - /path/to/file.txt`.
Also displays a Status Bar message.

#### Errors That Can Occur While Opening a File

| Dialog Title | Meaning |
| :---: | :---: |
| Unsupported File Type| Selected a binary file or a file that uses an unsupported encoding |
| Unknown Error While Opening File | An unknown error that had occurred while handling the file |
| File Not Found | The file was not found |
| Fatal Error | Fatal internal error |
