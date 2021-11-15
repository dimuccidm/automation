import unittest
from bin.querydirectories import list_dirs


class TestJob(unittest.TestCase):
    def test_list_dirs(self):
        "Test that it can list the full paths for directories"
        results = list_dirs(
            "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/"
            "source-files/tests/test_finding_latest_run/RUNDIR/"
        )
        answer = [
            "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR/RUN1",
            "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR/RUN2",
            "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR/RUN3",
            "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR/RUN4",
        ]
        self.assertEqual(
            results,
            answer,
        )


if __name__ == "__main__":
    unittest.main()
