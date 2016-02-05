__author__ = 'grk'
import sys
import os
import shutil

"""
Description :
This script move files from a directory's subdirectories to its root by a given extension to look for.
Usage : python file_extractor.py [dir] [file type]
example: $ python file_extractor.py /home/ubuntu/Documents txt
"""


""" check for path arg"""
if not (len(sys.argv) == 3):
    print("ERROR: {} [dir_path] [extension]".format(sys.argv[0]))
    exit(-1)

root_path = sys.argv[1]
extension = sys.argv[2]

""" check path existence """
if not os.path.exists(root_path):
    print("ERROR: '{}' does not exists".format(root_path))
    exit(-1)

""" check if it's a directory """
if os.path.isfile(root_path):
    print("ERROR: '{}' is a file".format(root_path))
    exit(-1)

""" moving the files """
for dirname, dirnames, filenames in os.walk(root_path):
    for filename in filenames:
        the_file = os.path.join(dirname, filename)
        if the_file.endswith('.{}'.format(extension)):
            try:
                shutil.move(the_file, root_path)
                print "moving [{}]".format(the_file)
            except:
                pass