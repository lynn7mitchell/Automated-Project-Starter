import os
import sys
import subprocess

# example command: python project_starter.py todo-list(new project folder name)
# create variables for argvs
template = sys.argv[1]
project_name = sys.argv[2]
path = os.path.abspath('.')
print(template, project_name)

# future needs to have name of heroku package to install
# future also needs other options than heroku

# Clone template
if template.lower() == 'mern':
    os.system('git clone https://github.com/lynn7mitchell/MERN-Template.git')

# Change name of downloaded template folder
# works but need more research to understand. Found on https://stackoverflow.com/questions/2014554/find-the-newest-folder-in-a-directory-in-python
all_directories = [directories for directories in os.listdir('.') if os.path.isdir(directories)]
latest_directory = os.path.abspath(max(all_directories, key=os.path.getmtime))
os.rename(latest_directory, path + '\\' + project_name)

# cd into folder

os.chdir(os.path.abspath(project_name))
os.system('npm i')
# run npm install
# open chrome
# go to github
# create github repo
# run github create commands
# run github add commit and push commmands
# open chrome
# go to heroku
# create a project
# add mlab
# go to settings
# reveal config variables
# copy the mongodb uri
# type SECRET_OR_KEY in the second variable and set the value to randomly generated key
# touch .env
# paste mongodb uri in .env
# run npm run start
