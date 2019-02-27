# How to setup properly his base installation with Anaconda
## Fresh installation Anaconda
- on Windows, just use the AXA package
- on Linux install    
  ```https://repo.continuum.io/archive/Anaconda3-X.Y.0-Linux-x86_64.sh```

## Setup of Anaconda python 
 When Anaconda/python installation is done ("base") and before creating env, do the following :
- ```python --version```  
  if this is not python 3.6 update it to python 3.6  
  ```conda install python=3.6```  
- ```conda update conda``` (should be done weekly)
- ```conda install jupyter_nbextensions_configurator -c conda-forge```
- ```conda install notebook=5.6.0``` (missing NbExtension tab with Jupyter 5.7.0)
- ```conda install nb_conda```
- ```pip install jupyter_tensorboard``` (for TensorFlow users)
- ```conda install -c conda-forge jupyter_contrib_nbextensions```
- ```jupyter contrib nbextension install --user```
- ```jupyter nbextensions_configurator enable --user```
- ```conda install autopep8```
- ```conda install pep8=1.7.1```
- ```conda install nbdime```
## Now you can create your python env

## Starting Jupyter notebbok
- always start jupyter notebook from the base python installation
- ```jupyter notebook```
- you should see all the python env you created
