# Import public modules
import argparse

# Import custom modules
import getsamplesheet as gs
import make_dragen_call as mk
import querydirectories as qd
import walkthroughdirs as wk


####################
#
# DEFINE THE ARGUMENTS
#
####################
def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "--run_directory",
        help="Directory where Novaseq runs are stored",
        type=str,
        required=True,
    )

    parser.add_argument(
        "--override",
        help="Set to True to force fastqs to be deposited into raw_data directory instead of processed_data",
        type=str,
        required=False,
        default=False,
    )
    return parser.parse_args()


####################
#
# DEFINE THE PROGRAM
#
####################
def main(run_dir, override):
    """
    Takes the target run directory,
     Identifies the newest valid run directory
     Submits the proper command for demultiplexing with dragen.

     Identifies which pipeline applies (plasmid seq, transformation verification)
     Submits the proper Docker command
     Loads results to scinamic
     Emails end-users location of reports and results
    """

    """
    Before submitting a demultiplexing call
    Identify all of the run directories with valid name formats
    Find the newest one that meets the requirements to be demultiplexed
        has:
        bcls
        sample sheet

        missing:
        fastqs 
    """
    run_paths = qd.list_dirs(run_dir)
    valid_paths = qd.keep_valid_run_names(run_paths)
    newest_valid_dir, requirements, samplesheet = wk.find_first_valid_dir(valid_paths)

    # print(samplesheet)
    if requirements:
        """
        # Construct the dragen call
        # fastqs get sent to processed_data directory.
        # Can force fastqs to be deposited in raw_data directory by setting override = True
        """
        dragen_call, output_dir = mk.construct_dragen_call(
            run_directory=newest_valid_dir, samplesheet=samplesheet, override=override
        )

        # Submit the dragen call with subprocess(dragen_call)
        # mk.submit_dragen_call(dragen_call)
        # Construct the function to monitor the process and fire off docker upon completion
        #print(dragen_call)
        #print("is the dragen done?")
        # subprocess to submit drops - blocking
        # Construct function to determine which pipeline needs to be run

        # Construct the docker call to run plasmid seq pipeline
        # TODO:
        # Define arg for reads directory
        # Define arg for results directory

        # Construct the docker call to run transformation verification pipeline
        # TODO:
        # Define arg for reads directory
        # Define arg for results directory

        # Construct function to determine who the creators are.

        # Construct the function to monitor the process and fire off emails to the creators upon completion

        return dragen_call

    # Construct function to check if it's already been processed - stop if true, but allow override

    raise Exception(
        "No run directories under %s containing *.cbcl files were identified." % run_dir
    )


####################
#
# RUN THE PROGRAM
#
####################
if __name__ == "__main__":
    args = parse_args()
    main(
        run_dir=args.run_directory,
        override=args.override,
    )
