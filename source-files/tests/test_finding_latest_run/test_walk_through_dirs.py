import unittest
from bin.querydirectories import walk_through_dirs, list_dirs


class TestJob(unittest.TestCase):
    def test_walk_through(self):
        "Test that directories with valid names can be found"
        run_dirs = list_dirs(
            "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/"
            "source-files/tests/test_finding_latest_run/RUNDIR2/"
        )
        answer = "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/RUN4_34_900_DKJCN"
        results = walk_through_dirs(run_dirs)[0]
        self.assertEqual(
            results,
            answer,
        )


if __name__ == "__main__":
    unittest.main()
