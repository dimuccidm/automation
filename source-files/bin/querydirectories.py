"""
Code to identify which DNA seq directory to call the synbio plasmid sequencing pipeline

Written by Demetrius DiMucci (LifeMine Therapeutics) 2021

usage: TODO
"""
# Import libraries
import fnmatch
import os

####################
#
# DEFINE FUNCTIONS
#
####################
def list_dirs(run_path):
    """
    Get the full paths for all directories in the target directory.
    :param run_path: file path to a directory containing directory of DNA seq runs
    :return:
    List of sub-directories found in the path
    """
    dirs = os.listdir(run_path)
    run_dirs = []
    for dir in dirs:
        full_path = os.path.join(run_path, dir)
        if os.path.exists(full_path):
            run_dirs.append(full_path)
    run_dirs = sorted(run_dirs)
    return run_dirs


def keep_valid_run_names(directory_names):
    """
    Identify target directories that meet the format of CHAR_CHAR_CHAR_CHAR/.
    Returns the full path to those directories.
    :param directory_names:  A list of full paths of directory names
    :return: A subsetted list of names with 3 underscores in their names
    """
    kept = []
    # For each name in directory_names keep if "_" appears exactly 3 times
    for name in directory_names:
        last = name.split("/")[-1]
        if last.count("_") == 3:
            kept.append(name)
    return kept


def check_bcls_exist(run_dir):
    """
    Given a run directory path check if there is at least 1 file with .cbcl extension in the C1.1 directory.
    :param run_dir:
    :return: boolean
    """
    extension = run_dir + "/Data/Intensities/BaseCalls/L001/C1.1"
    return os.path.exists(extension)


def get_recently_modified_dir(run_directories):
    """
    Identify the most recently modified directory from a list of directories
    :param run_paths: A list of valid run directories
    :return: tuple (
    The full path to the most recently created directory,
    Base name of the directory,
    )
    """
    latest_dir = max(run_directories, key=os.path.getctime)
    return latest_dir


# Integrate the previous functions into one
def newest_dir(run_path):
    run_dir = list_dirs(run_path)
    kept = keep_valid_run_names(run_dir)
    newest = get_recently_modified_dir(kept)
    return newest


# Use the previous functions to cycle through directories until either a valid one is found or the list is exhausted
def walk_through_dirs(run_paths):
    """
    Given a path to a directory where the runs are kept, find the newest directory that has bcl files to process
    :param run_paths:
    :return:
    valid_dir = ""
    """
    valid_dir = ""
    bcls = False
    while valid_dir == "" and len(run_paths) > 0:
        candidate = get_recently_modified_dir(run_paths)
        bcls = check_bcls_exist(candidate)
        if bcls:
            valid_dir = candidate
        else:
            run_paths.remove(candidate)
    return valid_dir, bcls
