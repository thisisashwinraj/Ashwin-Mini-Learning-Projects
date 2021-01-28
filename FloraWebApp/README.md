# Flora Web App
Flora is a serverles web application built using streamlit. The application uses machine learning to predict the species of Iris flower based on its dendrometric features. Random Forest Clasifier is used for building the predictive model.

The project is distributed under the MIT License. The resources for this project are maintained by [Ashwin Raj](https://github.com/ashwinraj-in).

# Installation and Development
### Dependencies
- Python (>= 3.7.9)
- Streamlit (>=0.68.0)

### Files and Folders
Folders that are necessary for the functioning of web app are as mentioned below:
- [Data](https://github.com/ashwinraj-in/Workspace/tree/main/FloraWebApp/Data):
  This folder contains the datasets that are used to develop the model.
- [PredictionApp](https://github.com/ashwinraj-in/Workspace/tree/main/FloraWebApp/Resources):
  This file contains the program for the web app including the predictive model.
- [Resources](https://github.com/ashwinraj-in/Workspace/tree/main/FloraWebApp/Resources):
  This folder contains the visual graphics that are used in the project.
  
# Running the Web App
The program necessary for deploying the web app is stored in the file PredictionApp.py. To run the program, download the file to the working directory in your local system and run the following command on in the terminal/command prompt:
```
streamlit run PredictionApp.py
```
  
Once the command is run, an internet browser window should pop-up that directs you to the created web app at http://localhost:8501.
  
# Contribution
New contributors of all experience levels are welcomed to contribute to this project. Some basic information about the project has been included in this README. For major changes, it is recommended that you open an issue first to discuss what you would like to change.

### Clone the repository
To contribute to this project you have to clone the repository and send a pull request.
```
git clone https://github.com/ashwinraj-in/Workspace/tree/main/FloraWebApp
```
### Installing Required Libraries
The web application requires some requirements that can be installed using the following code.
```
sudo pip3 install -r requirements.txt
```

# License and Project Status
The software and other resources for deploying the web app are distributed under MIT license. The project is completed and all the files are available in this repository. Further improvements can be done by hosting the web app on the server and improving the User interface.
