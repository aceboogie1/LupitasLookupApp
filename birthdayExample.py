# Gabriel Solomon, 2020

import json

#
# this is a relative path to the .json data file
# you can also use a "full" or "absolute path" to the file
# windows and mac paths are different.  You should google and youttube to learn about paths if you are
# not familiar with them.  They are important fundamental computer concepts.
#
# this is a full windows path, note the forward slashes "/" used in python
# pathToFile = "E:/Users/jerome/GitHub/evc-cit134a-python/birthday/birthday.json"
#
# mac (which is built on linux) and linux paths are like this: "a/b/c/d/e/f.json"
#

# relative path
# pathToFile = "./birthday/birthday.json"

# full path to file
pathToFile = "C:/Users/alexm/OneDrive/Documents/CIS-24 PYTHON/LupitasLookupApp/birthday.json"

# try to open a file and throw a error if it is not found
try:
    jsonFile = open(pathToFile, 'r')
except OSError:
    print("ERROR: Unable to open the file %s" % pathToFile)
    exit(-1)


# read the whole json file into a variable
birthdayList = json.load(jsonFile)


user_in=input("Who's birthday are you looking for?")
print(user_in)

for dict in birthdayList:
    if dict["name"] == user_in:
        print(dict["birthday"])