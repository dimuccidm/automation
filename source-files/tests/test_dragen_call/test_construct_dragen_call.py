import unittest
from bin.make_dragen_call import construct_dragen_call


class TestJob(unittest.TestCase):
    def test_construct_dragen_call(self):
        results = construct_dragen_call(
            run_directory="/mnt/SAN/NovaSeq/raw_data/DNAseq/211015_A01452_0039_AHM73LDRXY",
            samplesheet="/mnt/SAN/NovaSeq/raw_data/DNAseq/211015_A01452_0039_AHM73LDRXY/A20211061.csv",
        )
        answer = (
            "dragen --bcl-conversion-only true --bcl-input-directory "
            "/mnt/SAN/NovaSeq/raw_data/DNAseq/211015_A01452_0039_AHM73LDRXY "
            "--output-directory /mnt/SAN/NovaSeq/processed_data/DNAseq/211015_A01452_0039_AHM73LDRXY "
            "--force --sample-sheet /mnt/SAN/NovaSeq/raw_data/DNAseq/211015_A01452_0039_AHM73LDRXY/A20211061.csv "
            "--no-lane-splitting true"
        )
        self.assertEqual(results[0], answer)

    def test_construct_dragen_call_no_raw_data(self):
        results = construct_dragen_call(
            run_directory="/mnt/SAN/NovaSeq/raw_milk_data/DNAseq/211015_A01452_0039_AHM73LDRXY",
            samplesheet="/mnt/SAN/NovaSeq/raw_milk_data/DNAseq/211015_A01452_0039_AHM73LDRXY/A20211061.csv",
        )
        answer = (
            "dragen --bcl-conversion-only true --bcl-input-directory "
            "/mnt/SAN/NovaSeq/raw_milk_data/DNAseq/211015_A01452_0039_AHM73LDRXY "
            "--output-directory /mnt/SAN/NovaSeq/raw_milk_data/DNAseq/211015_A01452_0039_AHM73LDRXY "
            "--force --sample-sheet /mnt/SAN/NovaSeq/raw_milk_data/DNAseq/211015_A01452_0039_AHM73LDRXY/A20211061.csv "
            "--no-lane-splitting true"
        )
        self.assertEqual(results[0], answer)

    def test_construct_dragen_call_override_reformat(self):
        results = construct_dragen_call(
            run_directory="/mnt/SAN/NovaSeq/raw_data/DNAseq/211015_A01452_0039_AHM73LDRXY",
            samplesheet="/mnt/SAN/NovaSeq/raw_data/DNAseq/211015_A01452_0039_AHM73LDRXY/A20211061.csv",
            override=True,
        )
        answer = (
            "dragen --bcl-conversion-only true --bcl-input-directory "
            "/mnt/SAN/NovaSeq/raw_data/DNAseq/211015_A01452_0039_AHM73LDRXY "
            "--output-directory /mnt/SAN/NovaSeq/raw_data/DNAseq/211015_A01452_0039_AHM73LDRXY "
            "--force --sample-sheet /mnt/SAN/NovaSeq/raw_data/DNAseq/211015_A01452_0039_AHM73LDRXY/A20211061.csv "
            "--no-lane-splitting true"
        )
        self.assertEqual(results[0], answer)


if __name__ == "__main__":
    unittest.main()
