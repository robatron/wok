import logging
from os.path import isdir, isfile
from shutil import copytree, rmtree

class output_backup(object):

    def __init__(self, out_dir, bkp_dir):
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
