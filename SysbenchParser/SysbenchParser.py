# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os


class TestCase():

    def __init__(self, path):
        self.path = path
        self.fin = open(path, "r")

    def parse(self):

        while True:
            #print "head"
            line = self.fin.readline()
            if line.startswith("Threads started!"):
                break

        while True:
            #print "content"
            line = self.fin.readline()
            if line.startswith("Done."):
                break
            line = self.fin.readline()
            print line.split(" ")[0],
            line = self.fin.readline().lstrip(" \t")
            print line.split(" ")[0]
            self.fin.readline()

    def print_case(self, f):
        pass


def get_testcase_list(base_dir):
    """
    Get the file list of test results in the path base_dir.
    """
    entry_list = []
    for entry in os.listdir(base_dir):
        path = os.path.join(base_dir, entry)
        # ext = os.path.splitext(path)[1].lower()
        if os.path.isfile(path):
            entry_list.append(path)

    return entry_list


def main():

    flist = get_testcase_list("/home/titi/mnt/Documents/Lab/Test4")

    for f in flist:
        #print f
        case = TestCase(f)
        case.parse()

if __name__ == "__main__":
    main()
