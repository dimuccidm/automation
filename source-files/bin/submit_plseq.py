#!/usr/bin/python3
"""
Code to call the synbio plasmid sequencing pipeline on a target reads directory

Written by Demetrius DiMucci (LifeMine Therapeutics) 2021

usage: TODO
"""
# Import libraries
import argparse
import os

####################
#
# DEFINE FUNCTIONS
#
####################


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter
    )

    # Required user inputs
    parser.add_argument(
        "-reads_directory",
        help="Directory holding the reads to be analyzed.",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-output_directory",
        help="Target directory where the results will be held",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-scitable",
        help="Name of the relevant scinamic reference table.",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-pinc",
        help="Which plasmids to include, comma separated e.g.: pLM1615,pLM1616,pLM1618",
        type=str,
        required=False,
        default="",
    )
    return parser.parse_args()


def argument_generator(reads, output):
    """
    Given:
    :param reads: Directory
    :param output: Directory
    :return:
    Absolute path to reads directory
    Absolute path to output/analysis-pipeline
    Absolute path to output/tmp
    """
    # If '/' is not on the end of reads or output add it
    if not reads[-1] == "/":
        reads = reads + "/"

    if not output[-1] == "/":
        output = output + "/"

    reads_dir = [
        os.path.abspath(os.getcwd()) + "/" + reads,
        os.path.abspath(os.getcwd()) + "/" + output,
    ]
    return reads_dir


def create_output_directories(analysis, tmp):
    """
    Given path directories
    :param analysis:
    :param tmp:
    :return:
    Create the directories if they do not exist
    """

    # Check if analysis directory exists
    if not os.path.exists(analysis):
        os.mkdir(analysis)

    if not os.path.exists(tmp):
        os.mkdir(tmp)


def construct_pl_seq_command(reads, output, scitable, pinc):
    """
    Given path to reads file
    Given path to output directory

    :return:
    Docker run command feeding in reads file and appropriate output directories
    """
    if pinc:
        command = (
            f"docker run -v {reads}:/code/reads/ -v {output}analysis_pipeline/:/code/analysis-pipeline/ "
            f"-v {output}tmp/:/code/tmp/ test2 python py_plseq_plasmids_basefile.py -pinc {pinc} "
            f"-scitable {scitable} -threads 2"
        )
    else:
        command = (
            f"docker run -v {reads}:/code/reads/ -v {output}analysis_pipeline/:/code/analysis-pipeline/ "
            f"-v {output}tmp/:/code/tmp/ test2 python py_plseq_plasmids_basefile.py "
            f"-scitable {scitable} -threads 2"
        )

    return command


####################
#
# RUN THE PROGRAM
#
####################
def main(reads, output, scitable, pinc):

    reads, output = argument_generator(reads, output)

    invoke_pipeline = construct_pl_seq_command(
        reads,
        output,
        scitable,
        pinc,
    )
    print(invoke_pipeline)


if __name__ == "__main__":
    args = parse_args()
    main(
        reads=args.reads_directory,
        output=args.output_directory,
        pinc=args.pinc,
        scitable=args.scitable,
    )
