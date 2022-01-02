import os
import time
import datetime
import shutil

# Creare a folder if it doesn't exist in the giving path.
# Returns the giving path with folder name append.
def createFolderIfNecessary(path, folderName):
  updatedPath = "{}\\{}".format(path, folderName)

  if (os.path.isdir(updatedPath) is False):
    os.makedirs(updatedPath)
  
  return updatedPath

# Sample path C:\Users\krzys\Desktop
filesLocation = r"{}".format(input("Where are the files located?\n"))

# 0: Moving the original files to the new organize folders. 
# 1: Make a copy of the original files and place them to the organize folders.
keepOriginalFiles = bool(int(input("Do you want to keep the original files? 1 for yes, 0 for no\n")))

# Go over all of the files
for fileName in os.listdir(filesLocation):
  fileLocation = "{}\\{}".format(filesLocation, fileName)
  createdTime = time.ctime(os.path.getctime(fileLocation))
  createdDateTime = datetime.datetime.strptime(createdTime, "%a %b %d %H:%M:%S %Y")
  
  # Create the year folder if necessary.
  path = createFolderIfNecessary(filesLocation, createdDateTime.year)
  # Create the month folder if necessary.
  path = createFolderIfNecessary(path, createdDateTime.strftime("%B"))

  # Base on user preferences keep the original files or move them to the organize folders.
  if (keepOriginalFiles is True):
    shutil.copy(fileLocation, path)
  else:
    shutil.move(fileLocation, path)