from querydirectories import get_recently_modified_dir, check_bcls_exist
from getsamplesheet import find_sample_sheet
from make_dragen_call import refactor_output_dir, check_dragen_fastqs_exist

# Use the previous functions to cycle through directories until either a valid one is found or the list is exhausted
def find_first_valid_dir(run_paths):
    """
    Given a path to a directory where the runs are kept, find the newest directory that has bcl and sample sheet files to process
    :param run_paths:
    :return:
    valid_dir = ""
    """
    valid_dir = ""
    requirements = False
    samplesheet = ""
    while valid_dir == "" and len(run_paths) > 0:
        # TODO It would be more efficient to get the list once, sort it, and pop bad candidates off
        candidate = get_recently_modified_dir(run_paths)
        bcls_exist = check_bcls_exist(candidate)
        samplesheet, samplesheet_exists = find_sample_sheet(candidate)
        output_dir = refactor_output_dir(candidate)
        fastqs = check_dragen_fastqs_exist(output_dir)
        if bcls_exist and samplesheet_exists and not fastqs:
            valid_dir = candidate
            requirements = True
            return valid_dir, requirements, samplesheet
        else:
            run_paths.remove(candidate)
    return valid_dir, requirements, samplesheet
    # TODO
    # Create status report for each run directory
    # dir name, bcls, sample sheet, fastqs, fastqcomplete
    # If no valid dir detected - return the status report

