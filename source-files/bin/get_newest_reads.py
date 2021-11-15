#!/usr/bin/python3
"""
Code to identify the most recently created valid directory of DNA sequencing on the Dragen server.
Prepare the commands to be passed to getParameters.py

Written by Demetrius DiMucci (LifeMine Therapeutics 2021)

Assumed this will be called from the /home/lm-admin on the Dragen server.
usage:
run_path = '/mnt/SAN/NovaSeq/raw_data/DNAseq/'
TODO
"""
import argparse
import querydirectories as lr


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "--reads_directory",
        help="Target directory where the DNAseq results are stored",
        type=str,
        required=True,
    )


####################
#
# RUN THE PROGRAM
#
####################
def main(reads_dir):
    newest = lr.get_recently_modified_dir(reads_dir)
    if newest[0].count("_") == 3:
        print(newest)


if __name__ == "__main__":
    args = parse_args()
    main(
        reads_dir=args.reads_directory,
    )
