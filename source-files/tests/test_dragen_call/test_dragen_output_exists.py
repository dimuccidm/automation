import unittest
from bin.make_dragen_call import check_dragen_fastqs_exist, check_fastqcomplete


class TestJob(unittest.TestCase):
    def test_fastqs_not_made(self):
        results = check_dragen_fastqs_exist(
            output_directory="/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/tests/test_finding_latest_run/RUNDIR2/RUN4_34_900_DKJCN",
        )
        answer = False
        self.assertEqual(results, answer)

    def test_fastqs_already_made(self):
        results = check_dragen_fastqs_exist(
            output_directory="/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/pretend_reads/processed_data/Pretend_Validly_Named_Run",
        )
        answer = True
        self.assertEqual(results, answer)

    def test_demultiplexing_already_finished(self):
        results = check_fastqcomplete(
            output_directory="/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/pretend_reads/processed_data/Pretend_Validly_Named_Run",
        )
        answer = True
        self.assertEqual(results, answer)

    def test_demultiplexing_not_finished(self):
        results = check_fastqcomplete(
            output_directory="/Users/ddimucci/PycharmProjects/Synthetic_Biology_Pipeline/source-files/pretend_reads/processed_data/RUN4_34_900_DKJCN",
        )
        answer = False
        self.assertEqual(results, answer)


if __name__ == "__main__":
    unittest.main()
