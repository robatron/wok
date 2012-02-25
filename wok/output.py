import logging
import unittest
import os
from os.path import isdir, isfile
import shutil
from shutil import copytree, rmtree

class output_backup(object):
    """
    Backup and restore the output directory.
    """

    def __init__(self, out_dir, bkp_dir):
        """ 
        Initialize new output backup specifying hte output directory and the
        backup directory names.
        """
        self.out_dir = out_dir 
        self.bkp_dir = bkp_dir

    
    def backup(self):
        """
        Backup output directory. Delete any existing backups, copy output
        directory tree -> `self.bkp_dir`
        """
        logging.info("Backing up %s -> %s"%(self.out_dir, self.bkp_dir))
        if isdir(self.bkp_dir):
            rmtree(self.bkp_dir)
        if isdir(self.out_dir):
            copytree(self.out_dir, self.bkp_dir)
        else:
            logging.warn('Problem creating output backup. Output directory '
                    'not found.')


    def restore(self):
        """
        Restore output directory. Delete existing output directory, copy
        backup directory tree -> output
        """
        logging.info("Restoring %s -> %s"%(self.bkp_dir, self.out_dir))
        if isdir(self.out_dir):
            rmtree(self.out_dir)
        if isdir(self.bkp_dir): 
            copytree(self.bkp_dir, self.out_dir)
        else:
            logging.error('Error restoring output backup: Backup directory '
                    'not found.')


    def delete(self):
        """
        Delete backup directory if it exists.
        """
        logging.info("Deleting output backup %s"%self.bkp_dir)
        if isdir(self.bkp_dir):
            rmtree(self.bkp_dir)
        else:
            logging.warn('Error deleting output backup: Backup directory not '
                    'found.')


class test_output_backup(unittest.TestCase):
    """ 
    Unit tests for output backup module.
    """

    TESTBED = '.output_backup_testbed'
    ORIG_WD = os.getcwd()

    def setUp(self):
        """ To do before every unit test """
        os.mkdir(self.TESTBED)
        os.chdir(self.TESTBED) 

    def tearDown(self):
        """ To do after every unit test """
        os.chdir(self.ORIG_WD)
        shutil.rmtree(self.TESTBED)

    def test_backup(self):
        pass

    def test_restore(self):
        pass

    def test_delete(self):
        pass


if __name__ == "__main__":
    # run tests if module run standalone
    unittest.main()
