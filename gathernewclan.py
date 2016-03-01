import sys
import csv
import os
from shutil import copy


start_dir = ""
output_dir = ""

newclan_files = []
newclan_file_list = ""

def walk_tree_find_newclan_files():

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if filename_matches(file):
                newclan_files.append(file[0:5])
                print "Found newclan file: {}".format(file)
                # copy(os.path.join(root, file), output_dir)



def walk_tree_copy_newclan_originals():

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file_in_newclan_dictionary(file):
                if (len(files) == 1) and ".cex" in file:
                    copy(os.path.join(root, file), output_dir)
                    print "Found newclan original: {}".format(file)
                if "consensus_final" in file and not file.startswith(".") and ".cex" in file:
                    copy(os.path.join(root, file), output_dir)
                    print "Found newclan original: {}".format(file)
                    continue
                if "consensus" in file and not file.startswith(".") and ".cex" in file:
                    copy(os.path.join(root, file), output_dir)
                    print "Found newclan original: {}".format(file)
                    continue
                if "_final" in file and not file.startswith(".") and ".cex" in file:
                    copy(os.path.join(root, file), output_dir)
                    print "Found newclan original: {}".format(file)

                # copy(os.path.join(root, file), output_dir)



def filename_matches(file):
    if ("newclan_merged.cha" in file) and \
            (not file.startswith("."))\
            and (".bak" not in file):
        return True
    return False


def file_in_newclan_dictionary(file):
    if file[0:5] in newclan_files:
        return True
    return False


def newclanfiles_to_csv():
    with open("newclan_files.csv", "wb") as file:
        writer = csv.writer(file)
        writer.writerow("newclan_file")
        writer.writerows(newclan_files)


def load_newclan_filelist():
    with open(newclan_file_list, "rU") as file:
        reader = csv.reader(file)
        reader.next()
        for row in reader:
            newclan_files.append(row[0])


if __name__ == "__main__":

    start_dir = sys.argv[1]
    output_dir = sys.argv[2]

    if len(sys.argv) > 3:
        newclan_file_list = sys.argv[3]
        load_newclan_filelist()


    # walk_tree_find_newclan_files()
    # newclanfiles_to_csv()

    walk_tree_copy_newclan_originals()