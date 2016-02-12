import os
import sys
from shutil import copy

start_dir = ""
output_dir = ""

subject= ""
month = ""

def walk_tree():
    for root, dirs, files in os.walk(start_dir):
        if os.path.split(root)[1] == "Audio_Annotation":
            for file in files:
                if month:
                    print "file[3:5] = {}".format(file[3:5])
                    print "file = {}".format(file)
                    if correct_clanname(file) and int(file[3:5]) == int(month):
                        copy(os.path.join(root, file), output_dir)
                else:
                    if correct_clanname(file):
                        copy(os.path.join(root, file), output_dir)

def correct_clanname(name):
    if ("_final.cha" in name or "newclan_merged.cha" in name)\
            and not name.startswith("."):
        return True

if __name__ == "__main__":

    start_dir = sys.argv[1]
    output_dir = sys.argv[2]

    subject = sys.argv[3]
    month = sys.argv[4]

    if subject == "--all":
        subject = ""
    if month == "--all":
        month = ""


    walk_tree()
