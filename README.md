# Workspace Mini Projects
The repository contains the source code and resources for various projects that are as listed below. These projects use different technologies & the dependencies for each of the project are specified seprately in their respt sub-directories

This repository was started in October 2020 and all software and the resources used are shared under the [EPL License](https://github.com/ashwinraj-in/Workspace/blob/main/LICENSE)
The code and resources for the projects are available in their respective folders. You can check for the project status of each of the project in their respective readme.md. The various projects maintained in this repository are as mentioned

### [Flora Web App](https://github.com/ashwinraj-in/Workspace/tree/main/FloraWebApp)
Flora is a serverles web application built using StreamLit. The application uses machine learning to predict the species of Iris flower based on its dendrometric features. Random Forest clasifier is used for building the ML predictive model
> **Technical Stack**: Python, Streamlit, Machine Learning

### [Apheleia Extension](https://github.com/ashwinraj-in/Workspace/tree/main/ApheleiaExtension)
Apheleia is an AI enabled chrome extension, that uses natural language processing to generate summary of a site, by highlighting the important text. Extractive Summarization is used, and summarizing is done using the gensim module
> **Technical Stack**: Python, Natural Language Processing, HTML5, CSS3, Javascript

### [Mercury Payroll System](https://github.com/ashwinraj-in/Workspace/tree/main/MercuryPayrollSystem)
Mercury Payroll System is a terminal application, that enables your business to handle all of your employee's financial records in a hassle-free, & automated fashion. This software has multiple classes with numerous features within them
> **Technical Stack**: C++

### [PandoaNLP Web App](https://github.com/ashwinraj-in/Workspace/tree/main/PandoraNLP)
Pandora NLP is a serverles web application built using streamlit that uses Natural Language Processing modules such as Spacy, Gensim and Sumy to perform various natural language tasks such as Summarization, Sentiment Analysis etc
> **Technical Stack**: Python, Natural Language Processing, Streamlit

# Contribution and Guidelines

To start contributing to the project, clone the repository into your local system subdirectory using the below git code:
```
https://github.com/thisisashwinraj/Jovian-Bot.git
```
Before cloning the repository, make sure to navigate to the working subdirectory of your command line interface and ensure that no folder with same name exists. Other ways to clone the repository includes using a password protected SSH key, or by using [Git CLI](https://cli.github.com/). The changes may additionally be performed by opening this repo using [GitHub Desktop](https://desktop.github.com/)

### Edit the Source Code and Make Desired Changes

Goto the DialogflowConsole and select custom intent option. Import the code into Dialogflow. Make the appropriate changes, test the dialogflow agent on the simulator, download the ZIP file and make a pull request on this repository.

### Submitting a Pull Request
Before opening a Pull Request, it is recommended to have a look at the full contributing page to make sure your code complies with all the pull request guidelines. Please ensure that you satisfy the [~/checklist](https://github.com/thisisashwinraj/JovianBot-ChatBot-For-Social-Good/blob/main/.github/PULL_REQUEST_TEMPLATE/pull_request_template.md) before submitting your PR.

Navigate to this subdirectory, & check status of all files that were altered (red) by running the below code in Git Bash:
```
git status
```
Stage all your files that are to be pushed into your pull request. This can be done in two ways - stage all or some files:
```
git add .            // adds every single file that shows up red when running git status
```
```
git add <filename>   // type in the particular file that you would like to add to the PR
```

Commit all the changes that you've made and describe in brief the changes that you have made using this command:
```
git commit -m "<commit_message>"
```
Push all of your updated work into this GitHub repo in the form of a Pull Request by running the following command:
```
git push origin main
```
All pull requests are reviewed on a monthly rolling basis. Your understanding is appreciate during this review process.

# License and Project Status
Workspace, & all other resources are distributed under [Eclipse Public License 2.0](https://github.com/thisisashwinraj/JovianBot-ChatBot-For-Social-Good/blob/main/LICENSE). The bot is integrated with Telegram and Messenger. The latest released stable version of Jovian Bot is v1.0.0, and is available in English Language. All new releases are logged in the [/Versions](https://github.com/thisisashwinraj/JovianBot-ChatBot-For-Social-Good/tree/main/versions). The agent is currently in beta phase, and more updates will be released in future

Upcoming versions will include support for more policies, new platform integrations, & better user-intents matchings.
