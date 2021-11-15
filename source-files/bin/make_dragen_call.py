import shlex
import subprocess
import fnmatch
import os


def check_dragen_fastqs_exist(output_directory):
    if os.path.exists(output_directory):
        fastqs = fnmatch.filter(os.listdir(output_directory), "*.fastq.gz")
        return len(fastqs) > 0
    else:
        return False


def check_fastqcomplete(output_directory):
    fastqtxt = output_directory + "/Logs/FastqComplete.txt"
    return os.path.exists(fastqtxt)


def construct_dragen_call(run_directory, samplesheet, override=False):
    if not override:
        output = refactor_output_dir(run_directory)
    else:
        output = run_directory

    command = (
        "dragen --bcl-conversion-only true --bcl-input-directory "
        + run_directory
        + " --output-directory "
        + output
        + " --force --sample-sheet "
        + samplesheet
        + " --no-lane-splitting true"
    )
    return command, output


def refactor_output_dir(run_directory):
    """
    Given a path that contains a raw_data directory
    Refactor the path to change raw_data to processed_data
    :param run_directory:
    :return:
    """
    if "/raw_data/" in run_directory:
        run_directory = run_directory.replace("/raw_data/", "/processed_data/")
        return run_directory
    else:
        return run_directory


def submit_dragen_call(command):
    """
    Given a command line argument, submits the command and waits until process completes before moving on.
    :param command:
    """
    args = shlex.split(command)
    subprocess.check_call(args)
