#!/usr/bin/env python
import threading
import sys
import os
import subprocess
from datetime import datetime

# ===========================================================
# NOTE:
# This was originally intended to work with multiple threads,
# although it doesn't seem to work, only permiting a single
# thread to execute.
# ===========================================================

def discoverFiles(location):
    """Returns a list of all filenames in target location
    
    Keyword arguments:
    location - An absolute path to the directory being searched 
    """
    return [os.path.join(location, f) for f in os.listdir(location) if os.path.isfile(os.path.join(location, f))]

def splitFiles(files, num_of_splits):
    """Splits parameters files into num_of_splits equal chunks. Returns a list of lists.
    
    Keyword arguments:
    files - A list of all filenames (absolute pathing) in a target directory
    num_of_splits - The number of threads to divide the files amongst
    """
    return [files[i:i + num_of_splits] for i in range(0, len(files), num_of_splits)]

def processFiles(files, open_face_loc):
    for f in files:
        try:
            command = [open_face_loc + "build/bin/FeatureExtraction", "-f", f]
            start = datetime.now()
            # # Limiting thread to single file execution
            p = subprocess.call(command, stdout=subprocess.PIPE)
            print("COMPLETE: {} in {}".format(f, (datetime.now() - start)))
        except:
            print("ERROR: {}".format(f))

if __name__ == "__main__":
    # Check if the program has been given sufficient parameters
    number_of_args = len(sys.argv) - 1
    if number_of_args < 3:
        sys.exit("Usage: python3 process_vids.py <number of threads> <video folder location> <open face install dir>")

    # Get program arguments
    try:
        thread_count = int(sys.argv[1])
    except:
        sys.exit("Invalid number of threads")
    video_folder_loc = sys.argv[2]
    open_face_loc = sys.argv[3]

    # Get all files in target location and split evenly amonst the threads
    files_for_threads = splitFiles(discoverFiles(video_folder_loc), thread_count)
    time1 = datetime.now()
    # Build and begin thread execution
    threads = []
    for i in range(thread_count):
        t = threading.Thread(target=processFiles, args=(files_for_threads[i], open_face_loc,))
        t.run()
        threads.append(t)

    print("TOTAL TIME: {}".format(datetime.now() - time1))
    # Wait for all threads to finish
    for t in threads:
        t.join()