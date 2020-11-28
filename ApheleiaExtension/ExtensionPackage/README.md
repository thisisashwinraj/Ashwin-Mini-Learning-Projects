# Extension Package
This folder contains all the necesary files for developing the frontend and backend of the extension. All the files of this folder are important for the proper functioning of the web app.
# Files and Folders
### jquery-2.2.js
This is a front end javascript file used for adding ready-made elements to the project. These elements can be customised as necessary.

### content.js
In this file, remember to replace the api_url with your google cloud function url before deploying the extension to chrome store.

### manifest.json
json file is the only file that every extension using WebExtension APIs must contain. Manifest.json is used to specify basic metadata about the extension such as the name and version. It is also used to specify aspects of the extension's functionality (such as background scripts, content scripts, and browser actions).

### popup.html
This is the html file of the chrome extension. Extensions may have many forms, but this extension uses a popup.

### popup.js
This file contains the code to interact with the browser's tab system and feed the code to the content.js file.

### styles.css
This file is used to describe the presentation of the chrome extension, including colors, layout, and fonts.This can be edited to alter the look of the extension.
