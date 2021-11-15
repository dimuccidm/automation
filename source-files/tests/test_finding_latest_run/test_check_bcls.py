import unittest
from bin.querydirectories import check_bcls_exist


class TestJob(unittest.TestCase):
    def test_bcls_found(self):
        "Test that directories with valid names can be found"
        directory_name = "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR3"
        results = check_bcls_exist(directory_name)
        self.assertEqual(
            results,
            True,
        )

    def test_bcls_absent(self):
        "Test that directories with valid names can be found"
        directory_name = "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/RUN_1_34_DJD"
        results = check_bcls_exist(directory_name)
        self.assertEqual(
            results,
            False,
        )


if __name__ == "__main__":
    unittest.main()
