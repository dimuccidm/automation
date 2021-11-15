import unittest
from bin.querydirectories import keep_valid_run_names


class TestJob(unittest.TestCase):
    def test_keep_valid_run_names(self):
        "Test that directories with valid names can be found"
        directory_names = sorted(
            [
                "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/SAMPLE_SHEETS",
                "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/RUN4_34_900_DKJCN",
                "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/@NOTRIGHT",
                "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/RUN_WITH_TOO_MANY_UNDER_SCORES",
                "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/RUN_1_34_DJD",
            ]
        )
        results = keep_valid_run_names(directory_names)
        answer = [
            "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/RUN4_34_900_DKJCN",
            "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/RUN_1_34_DJD",
        ]
        self.assertEqual(
            results,
            answer,
        )


if __name__ == "__main__":
    unittest.main()
