import unittest
from bin.getsamplesheet import find_sample_sheet, get_scitable_id, format_scitable_id


class TestJob(unittest.TestCase):
    def test_find_sample_sheet(self):
        results = find_sample_sheet(
            "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/"
            "source-files/tests/test_finding_latest_run/RUNDIR2/THE_NEWEST_GOOD_DIR/"
        )
        answer = (
            "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/"
            "source-files/tests/test_finding_latest_run/RUNDIR2/THE_NEWEST_GOOD_DIR/Reports/SampleSheet.csv"
        )
        self.assertEqual(
            results[0],
            answer,
        )

    def test_get_scitable_id(self):
        results = get_scitable_id(
            "/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/"
            "source-files/tests/test_finding_latest_run/RUNDIR2/"
            "THE_NEWEST_GOOD_DIR/Reports/SampleSheet.csv"
        )
        answer = "A20211105"
        self.assertEqual(results, answer)

    def test_format_scitable_id(self):
        results = format_scitable_id("A20211105")
        answer = "A-2021-1105"
        self.assertEqual(results, answer)


if __name__ == "__main__":
    unittest.main()
