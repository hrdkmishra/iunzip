import os
import zipfile
directory = '//home//hardman//archives//'
extractdir = '//home//hardman//extracts//'
# listdir returns a list of files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.zip'):  # if the file ends with .zip
        # join the directory and the filename
        zippath = os.path.join(directory, filename)
        zfile = zipfile.ZipFile(zippath)  # open zip file
        # extracts all files in the zip file to the specified directory
        zfile.extractall(extractdir)
        zfile.close()  # close the zip file
        os.remove(zippath)  # delete the zip file
