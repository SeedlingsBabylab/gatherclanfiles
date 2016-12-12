import os
import sys
from shutil import copy

start_dir = ""
output_dir = ""

subject= ""
month = ""

def filter_files_by_type(root, files):
    cha_paths = []
    cex_paths = []
    other_paths = []
    for file in files:
        if file.endswith(".cha"):
            cha_paths.append(os.path.join(root, file))
        elif file.endswith(".cex"):
            cex_paths.append(os.path.join(root, file))
        else:
            other_paths.append(os.path.join(root, file))
    return cha_paths, cex_paths, other_paths

def find_finals(cha_files):
    final = []
    newclan_merged_final = []
    newclan_merged = []

    for file in cha_files:
        if file.endswith("_final.cha") and not file.endswith("newclan_merged_final.cha"):
            final.append(file)
        elif file.endswith("newclan_merged_final.cha"):
            newclan_merged_final.append(file)
        elif file.endswith("newclan_merged.cha"):
            newclan_merged.append(file)
    return final, newclan_merged_final, newclan_merged

def find_final_final(final, nc_merged_final, nc_merged, errors_file):
    final_final = None
    if len(final) > 1:
        print "\tmore than one final.cha in this Annotation folder: {}".format(final[0][:5])
        errors_file.write("\tmore than one final.cha in this Annotation folder: {}\n".format(final[0][:5]))
    elif len(final) == 1:
        final_final = final[0]
        return final_final
    elif len(final) == 0:
        if len(nc_merged_final) > 1:
            print "\tmore than one newclan_merged_final.cha in this Annotation folder: {}".format(nc_merged_final[0][:5])
            errors_file.write("\tmore than one newclan_merged_final.cha in this Annotation folder: {}\n".format(nc_merged_final[0][:5]))
        elif len(nc_merged_final) == 1:
            final_final = nc_merged_final[0]
            return final_final
        elif len(nc_merged_final) == 0:
            if len(nc_merged) > 1:
                print "\tmore than one newclan_merged.cha in this Annotation folder: {}".format(nc_merged[0][:5])
                errors_file.write("\tmore than one newclan_merged.cha in this Annotation folder: {}\n".format(nc_merged[0][:5]))
            elif len(nc_merged) == 1:
                final_final = nc_merged[0]
                return final_final
            elif len(nc_merged) == 0:
                return final_final
    return final_final

def walk_tree(errors_file):
    for root, dirs, files in os.walk(start_dir):
        if os.path.basename(root) == "Audio_Annotation":
            chas, cex, other = filter_files_by_type(root, files)
            final, nc_merged_final, nc_merged = find_finals(chas)
            final_final = find_final_final(final, nc_merged_final, nc_merged, errors_file)

            if not final_final:
                print "\t**NO FINAL FILE IN THIS FOLDER**: {}".format(root)
                errors_file.write("\n\ninside: {}\n".format(root))
                errors_file.write("\t**NO FINAL FILE IN THIS FOLDER**: {}\n".format(root))
            else:
                if month:
                    print "file[3:5] = {}".format(file[3:5])
                    print "file = {}".format(file)
                    if int(file[3:5]) == int(month):
                        copy(final_final, output_dir)
                else:
                    copy(final_final, output_dir)


# def correct_clanname(name, chosen_files):
#     if name.endswith("_final.cha") and "newclan_merged" not in name:
#         return True
#     if name.endswith("newclan_merged.cha") and
#
#     if ("_final.cha" in name or "newclan_merged.cha" in name)\
#             and not name.startswith("."):
#         return True

if __name__ == "__main__":

    start_dir = sys.argv[1]
    output_dir = sys.argv[2]

    subject = sys.argv[3]
    month = sys.argv[4]

    if subject == "--all":
        subject = ""
    if month == "--all":
        month = ""

    with open ("walk_errors.txt", "wb") as errors_file:
        walk_tree(errors_file)
