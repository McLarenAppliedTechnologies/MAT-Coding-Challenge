# Code written by Jerin Rajan on 09th Dec 2019
# Email - jrajan @jprtech.co.uk
# This is the header file to the main application mApp.py
# The file must be in the same location as mApp.py and must be included in
# mApp.py

import json

# Function to open, read & load a JSON file, with a filename as an INPUT parameter.
# The function returns the JSON data as an OUTPUT
def openJSON(filename):

    # Open a
    file = open(filename,'r').read()

    # Error handling
    try:
        js = json.loads(file)
    except:
        js = None

    # Returns the JSON Data
    return js
