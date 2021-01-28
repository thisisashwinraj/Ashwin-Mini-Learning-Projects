# Extension Package
This folder contains the setup and configuration files for the web application. 

### [setup.py](https://github.com/ashwinraj-in/Workspace/blob/main/PandoraNLPWebApp/AppPackage/setup.py)
setup.py is a python file that allows you to easily install Python packages. In this project we have used setuptools instead of disutils. distutils is the standard library, bare-bones packaging toolset but setuptools wraps the basic features in distutils and has additional features in it.

```
$ pip install . 
```

### [setup.cfg](https://github.com/ashwinraj-in/Workspace/blob/main/PandoraNLPWebApp/AppPackage/setup.cfg)
setup.cfg is an ini file that contains option defaults for setup.py commands. A seprate setup.cfg file is required as it's cleaner to keep code and data separate. It makes it more readable and there is a central location to make modifications. 
