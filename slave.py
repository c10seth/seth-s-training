import os
import sys

def myfunk(directory):
    #directory = sys.argv[1]

    if not os.path.isdir(directory):
        os.makedirs(directory)

    print("SCANNING ", directory)
    print(os.listdir(directory))
    print()

