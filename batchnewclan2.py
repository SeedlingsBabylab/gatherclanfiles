import sys
import os
import subprocess as sp

start_dir = ""



if __name__ == "__main__":


    start_dir = sys.argv[1]


    files = os.listdir(start_dir)

    base = ["python", "newclan2.py", "nothing"]

    for file in files:
        command = base + [os.path.join(start_dir, file), "nothing" , file]
        # abbrev_command = [os.path.split(element)[1] for element in command]
        # print "command: {}".format(abbrev_command)
        pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=10**8)
        # pipe.stdout.flush()
        stdout = pipe.communicate()[0]  # blocks until the subprocess in complete

        print "output: {}".format(stdout)

        # processed.write(key+":\tcommand: {}\n".format(abbrev_command))
        # files_processed_count += 1