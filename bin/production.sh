#!/bin/bash

apt-get update --assume-yes
apt-get install zip --assume-yes
apt-get install virtualenv --assume-yes

# # Update to that version
echo "creating zappa Application Version ..."
virtualenv venv;\
. venv/bin/activate; pip install -r requirements.txt;\
pip install --upgrade pip==9.0.3; zappa create;\
make pmigrate pcollectstatic
echo "Done!"

# # Update to that version
# echo "Updating zappa Application Version ..."
# virtualenv venv;\
# . venv/bin/activate; pip install -r requirements.txt;\
# pip install --upgrade pip==9.0.3; zappa update;\
# make pmigrate pcollectstatic
# echo "Done!"
