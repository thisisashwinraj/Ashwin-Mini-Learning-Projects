# PandoraNLP Web App
PandoraNLP is a serverles web application built using streamlit that uses Natural Language Processing modules such as Spacy, Gensim and Sumy to perform various NLU operations such as Text Summarization, Tokenization, Entity Extraction and Sentiment Analysis.

The project is distributed under the MIT License. The resources for this project are maintained by [Ashwin Raj](https://github.com/ashwinraj-in).

# Installation and Development
### Dependencies
- Gensim (>=3.8.3)
- Python (>= 3.7.9)
- SpaCy (>=2.3.5)
- Streamlit (>=0.68.0)
- Sumy (>=0.8.1)
- TextBlob (>=0.15.3)

### Files and Folders
Folders that are necessary for the functioning of web app are as mentioned below:
- [AppPackage](https://github.com/ashwinraj-in/Workspace/tree/main/PandoraNLPWebApp/AppPackage):
  This folder contains the setup and configuration files for the serverless Web App. 
- [NLPApp](https://github.com/ashwinraj-in/Workspace/tree/main/PandoraNLPWebApp/NLPApp.py):
  This file contains the program for deploying the web app including the predictive model.
- [Resources](https://github.com/ashwinraj-in/Workspace/tree/main/FloraWebApp/Resources):
  This folder contains the visual graphics and modules that are used in the project.
  
# Running the Web App
The program necessary for deploying the web app is stored in the file NLPApp.py. To run the program, download the file to the working directory in your local system and run the following command on in the terminal/command prompt:
```
streamlit run NLPApp.py
```
  
Once the command is run, an internet browser window should pop-up that directs you to the created WebApp.

Local URL: http://localhost:8501
Network URL: http://192.168.42.172:8501
  
# Contribution
New contributors of all experience levels are welcomed to contribute to this project. Some basic information about the project has been included in this README. For major changes, it is recommended that you open an issue first to discuss what you would like to change.

### Clone the repository
To contribute to this project you have to first clone the repository and then send a pull request with proposed changes.
```
git clone https://github.com/ashwinraj-in/Workspace/tree/main/PandoraNLPWebApp
```
### Installing Required Libraries
The web application requires some requirements that are present in the requirements.txt file. These can be installed by running:
```
sudo pip3 install -r requirements.txt
```

# License and Project Status
The software and other resources for deploying the web app are distributed under MIT license. The project is completed and all the files are available in this repository. Further improvements can be done by hosting the web app on the server and improving the User interface.
