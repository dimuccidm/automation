import argparse
import querydirectories as qd

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
    return parser.parse_args()


####################
#
# DEFINE THE PROGRAM
#
####################
def main(run_dir):
    """

    :return:
    """
    dirs = qd.list_dirs(run_dir)
    valid_dirs = qd.keep_valid_run_names(dirs)
    newest_valid_dir = qd.get_recently_modified_dir(valid_dirs)
    print(newest_valid_dir)


####################
#
# RUN THE PROGRAM
#
####################
if __name__ == "__main__":
    args = parse_args()
    main(
        run_dir=args.run_directory,
    )
