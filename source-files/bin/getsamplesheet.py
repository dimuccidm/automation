"""
Code to find the sample sheet relevant to a specific experiment and extract the scitable ID

Written by Demetrius DiMucci (LifeMine Therapeutics) 2021

usage: TODO
"""
import csv
import os
import fnmatch


def find_first_sample_sheet(run_dir):
    csvs = fnmatch.filter(os.listdir(run_dir), "*.csv")
    if len(csvs) > 1:
        csvs.remove("streaming_log_lm-admin.csv")
        csvs.remove("dragen.time_metrics.csv")
    sampsheet = csvs[0]
    sampid = sampsheet[0:-4]
    return sampsheet, sampid


def find_sample_sheet(run_dir):
    """
    Given the path to a target run directory, identifies if a sample sheet is present and returns the file path and a
    boolean if about its existence.
    :param run_dir:
    :return: file path.
    """
    if run_dir[-1] == "/":
        sampsheet = run_dir + "Reports/SampleSheet.csv"
    else:
        sampsheet = run_dir + "/Reports/SampleSheet.csv"
    if os.path.exists(sampsheet):
        return sampsheet, True
    else:
        return sampsheet, False


def get_scitable_id(sheet_path):
    """
    Given the file path to the sample sheet, works through each line until it finds the Experiment Name field
    then returns the associated scitable ID.
    :param sheet_path:
    :return: A20211104
    """
    with open(sheet_path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] != "Experiment Name":
                continue
            break
    return row[1]


def format_scitable_id(scitableid):
    """
    Given a scitable ID, insert '-' at the appropriate points and return the ID.
    :param scitableid: A20211104
    :return: A-2021-1104
    """
    formatted_id = scitableid[:1] + "-" + scitableid[1:5] + "-" + scitableid[5:]
    return formatted_id


def process_scitable(run_dir):
    scitableid, formatted_id = find_first_sample_sheet(run_dir)
    return scitableid, formatted_id
