import unittest
from bin.make_dragen_call import refactor_output_dir


class TestJob(unittest.TestCase):
    def test_refactor_raw_data(self):
        results = refactor_output_dir(
            run_directory="/mnt/SAN/NovaSeq/raw_data/DNAseq/211015_A01452_0039_AHM73LDRXY",
        )
        answer = "/mnt/SAN/NovaSeq/processed_data/DNAseq/211015_A01452_0039_AHM73LDRXY"
        self.assertEqual(results, answer)

    def test_refactor_no_raw_data(self):
        results = refactor_output_dir(
            run_directory="/mnt/SAN/NovaSeq/raw_milk_data/DNAseq/211015_A01452_0039_AHM73LDRXY",
        )
        answer = "/mnt/SAN/NovaSeq/raw_milk_data/DNAseq/211015_A01452_0039_AHM73LDRXY"
        self.assertEqual(results, answer)


if __name__ == "__main__":
    unittest.main()
