import unittest
from bin.querydirectories import get_recently_modified_dir


class TestJob(unittest.TestCase):
    def test_get_newest_dir_path(self):
        "Test that the most recently modified directory can be found"
        results = get_recently_modified_dir(
            [
                "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/RUN4_34_900_DKJCN",
                "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/RUN_1_34_DJD",
                "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/THE_NEWEST_GOOD_DIR",
            ]
        )
        answer = "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/THE_NEWEST_GOOD_DIR"
        self.assertEqual(
            results,
            answer,
        )


if __name__ == "__main__":
    unittest.main()
