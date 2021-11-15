import unittest
import os

from bin.submit_plseq import argument_generator, construct_pl_seq_command


class TestJob(unittest.TestCase):
    """
    Class to hold future tests
    """

    def test_argument_generator(self):
        """
        Given:
        relative path to reads directory
        relative path to output directory
        :return:
        Absolute path to reads directory
        Absolute patht o output directory
        """
        results = argument_generator("reads", "output")
        self.assertEqual(
            results[0],
            os.path.abspath(os.getcwd()) + "/reads/",
        )

    def test_construct_pl_seq_command(self):
        """
        Given:
        Absolute path to reads directory
        Absolute path to output directory
        :return:
        Command to invoke docker run command with correct sub-directories in output directory
        """
        self.assertEqual(
            construct_pl_seq_command(
                "/home/ddimucci/SYNBIO/sequencing/sub_sequencing/reads/",
                "/home/ddimucci/SYNBIO/sequencing/sub_sequencing/results/",
                "A-2021-0949",
                "pLM1615,pLM1616,pLM1618",
            ),
            "docker run -v /home/ddimucci/SYNBIO/sequencing/sub_sequencing/reads/:/code/reads/ "
            "-v /home/ddimucci/SYNBIO/sequencing/sub_sequencing/results/analysis_pipeline/:/code/analysis-pipeline/ "
            "-v /home/ddimucci/SYNBIO/sequencing/sub_sequencing/results/tmp/:/code/tmp/ "
            "test2 python py_plseq_plasmids_basefile.py -pinc pLM1615,pLM1616,pLM1618 -scitable A-2021-0949 -threads 2",
        )


if __name__ == "__main__":
    unittest.main()
