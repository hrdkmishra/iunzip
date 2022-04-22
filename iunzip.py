#!/usr/bin/env python3
import os
import zipfile
import threading
import tarfile
directory = '//home//hardman//archives//'
extractdir = '//home//hardman//extracts//'
def runit():
    threading.Timer(1.0, runit).start()
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
        else:
            if filename.endswith('.tar.xz'):
                tar = tarfile.open(directory + filename)
                tar.extractall(extractdir)
                tar.close()
                os.remove(directory + filename)
if __name__ == '__main__':
    runit()
