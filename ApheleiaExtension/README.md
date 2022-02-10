# Apheleia Chrome Extension
Apheleia is a chrome extension that can be used to create a summarry of a web page. The extension uses natural language processing to highlight important statements. A serverless architecture is adopted for the summarization API. The process of summarizing is based on ranks of text sentences using a variation of the TextRank algorithm.

The project is distributed under the MIT License. The resources for this project are maintained by [Ashwin Raj](https://github.com/ashwinraj-in).

# Installation and Development
### Dependencies
- Python (>= 3.7.9)
- Gensim (>=3.8.3)

### Files and Folders
Folders that are necessary for the functioning of the chrome extension are as mentioned below:
- [ExtensionPackage](https://github.com/ashwinraj-in/Vulpex-WebApp/tree/master/Server):
  This folder contains all the necessary files that makes up the chrome extension.
- [Resources]():
  This folder contains the icons that are used in the extension.
- [ExtensionMain](https://github.com/ashwinraj-in/Workspace/blob/main/ApheleiaExtension/ExtensionMain.py):
  This file contains the code to generate summary of the input text.
  
# Running the Extension
The package necessary for running the extension include all the files of Extension Package folder, the content of icons folder within the resources folder and the ExtensionMain.py file. For the extension to run, keep all the files in the same folder and then follow the steps that are as mentioned below:
  1. On your chrome browser, Go to Customize and Control Google Chrome < More Options < Extensions.
  2. Toggle the Developers Mode to be switched ON, if not by default.
  3. Click on the Load Unpacked option and select the extension folder.
  
Once the upload completes, the extension will be added to your chrome browser, that you can verify by clicking on the extensions option next to the search bar. To run your extension, simply select the name of your extension and click on **Highlight Summary** option. 

This will take around 15 to 30 seconds to create a summary and highlight the text depending on the size of the text.
  
### Publishing the extension on Chrome Store
To publish the extension on chrome store, simply follow the below listed steps:
  1. Create your item’s zip file
  2. Create a developer account
  3. Upload your item
  4. Add assets for your listing
  5. Submit your item for publishing
  
For a detailed understanding of how to publish your chrome extension, visit their official website [here](https://developer.chrome.com/webstore/publish).

# Contribution
New contributors of all experience levels are welcomed to contribute to this project. Some basic information about the project has been included in this README. For major changes, it is recommended that you open an issue first to discuss what you would like to change.

### Clone the repository
To contribute to this project you have to clone the repository and send a pull request.
```
git clone https://github.com/ashwinraj-in/Workspace/tree/main/ApheleiaExtension
```
### Installing Required Libraries
The extension requires some requirements that can be installed using the following code.
```
sudo pip3 install -r requirements.txt
```

# License and Project Status
The extension package and other resources for developing this chrome extension are distributed under [MIT license](https://github.com/ashwinraj-in/Workspace/tree/main/LICENSE). The project is completed and all the files are available in this repository. Further improvements can be made by making the process quicker & improving the results.
