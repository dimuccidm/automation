import argparse
import getsamplesheet as gs

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
        "--sheet_path",
        help="File path to where the sample sheet is stored",
        type=str,
        required=True,
    )
    return parser.parse_args()


####################
#
# DEFINE THE PROGRAM
#
####################
def main(sheet_path):
    """

    :return:
    """
    sheetloc = gs.find_sample_sheet(sheet_path)
    sheetid = gs.get_scitable_id(sheetloc)
    scitable_id = gs.format_scitable_id(sheetid)
    print(scitable_id)


####################
#
# RUN THE PROGRAM
#
####################
if __name__ == "__main__":
    args = parse_args()
    main(
        sheet_path=args.sheet_path,
    )
