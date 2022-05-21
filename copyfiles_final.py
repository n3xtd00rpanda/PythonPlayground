# @author: n3xtd00rpanda was here ***

# #!/usr/bin/env python3 
from fileinput import filename
import os, subprocess, shutil, sys
from re import search

files = []
full_file_path = ""

def fileCopy(nwd): 

    for file in os.listdir():
        file_name, file_extension = os.path.splitext(file)
        full_file_path = os.getcwd() + "/" + file_name + file_extension
        new_file_path = nwd + file_name + file_extension
        subs = ".git"
        if file_name.find(".git") == -1 and file_extension != ".git" and os.path.isfile(full_file_path) and file_name != "wp_config" and file_name != "copyfiles_nogitignore":
            print("Copying from: ", full_file_path)
            print("Copying to: ", new_file_path)
            shutil.copyfile(full_file_path, new_file_path)
        elif file_extension == ".git" or file_name.find("git") != -1 or file_name == "wp_config" and os.path.isfile(full_file_path):
            print("Found file: ", file_name, file_extension, " in working directory. Not copied.")

if __name__ == '__main__':
    fileCopy(sys.argv[1])