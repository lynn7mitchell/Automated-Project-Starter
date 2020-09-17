# example command: python project_starter.py todo-list(new project folder name)
import os
import sys
# login info
from login_info import username, password
from selenium import webdriver
chrome_browser = webdriver.Chrome('./chromedriver')


# create variables for argvs and path
template = sys.argv[1]
project_name = sys.argv[2]
path = os.path.abspath('.')
print(template, project_name)


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

# run npm install
# os.system('npm i')


# open chrome
# you can also put in in your path
chrome_browser.maximize_window()
# go to github
chrome_browser.get('https://github.com/')

# check for words 'Sign In'
print('Sign in' in chrome_browser.page_source)
assert 'Sign in' in chrome_browser.page_source

# grab login button
login_button = chrome_browser.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]');

# click login button
login_button.click()

# enter username and password
username = username
password = password
username_form_field = chrome_browser.find_element_by_xpath('//*[@id="login_field"]')
password_form_field = chrome_browser.find_element_by_xpath('//*[@id="password"]')

username_form_field.clear()
username_form_field.send_keys(username)

password_form_field.clear()
password_form_field.send_keys(password)

login_submit_button = chrome_browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')

login_submit_button.click()
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



# NOTES FOR FUTURE VERSIONS
# future needs to have name of heroku package to install
# future also needs other options than heroku
