# -*- coding: utf-8 -*-
"""
__DESCRIPTION__
"""

import argparse
import logging
import sys
import os
from tkinter import Tk, Entry, Label, Button, Checkbutton, scrolledtext, messagebox, filedialog
from tkinter import BooleanVar, END, INSERT
from tkinter.ttk import Combobox
from pathlib import Path


__author__ = '__AUTHOR__'
__copyright__ = 'Copyright 2027, __AUTHOR__'
__license__ = 'GPL'
__version__ = '0.0.1'
__maintainer__ = '__AUTHOR__'
__email__ = 'noreply@gmail.com'
__status__ = 'Initial'

LOGGER = logging.getLogger('__PROJECTNAMELCASE__')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
LOGGER.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
LOGGER_FH = logging.FileHandler('__PROJECTNAMELCASE__.log')

# create console handler with a higher log level
LOGGER_CH = logging.StreamHandler()
LOGGER_CH.setLevel(logging.INFO)

# create FORMATTER and add it to the handlers
FORMATTER = \
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                      )
LOGGER_FH.setFormatter(FORMATTER)
LOGGER_CH.setFormatter(FORMATTER)

# add the handlers to the LOGGER
LOGGER.addHandler(LOGGER_FH)
LOGGER.addHandler(LOGGER_CH)


class __PROJECTNAME__():
    """Main class.

    """

    def __init__(self):
        self.par_input = ''
        self.par_output = ''
        self.home = str(Path.home())
        self.documents_folder = str(os.path.join(self.home, 'Documents'))
        self.git_folder = str(os.path.join(self.documents_folder, 'GitHub'))
        self.project_folder = os.path.join(self.git_folder, 'Project')
        self.window = Tk()
        self.cmb_01 = Combobox(self.window)
        self.cmb_01['values'] = ('CLI', 'Tkinter', 'PyQt')
        self.txt_01 = Entry(self.window, width=20)
        self.txt_02 = Entry(self.window, width=50)
        self.txt_03 = Entry(self.window, width=50)
        self.scr_01 = scrolledtext.ScrolledText(
            self.window, width=40, height=10)
        self.chk_01_state = BooleanVar()
        self.chk_01_state.set(True)

    @staticmethod
    def parse_arguments():
        """Parse arguments.

        Returns:
            parser args -- parser argumnents
        """

        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--input',
                            help='input file')
        parser.add_argument('-o', '--output',
                            help='output file')
        parser.add_argument('-v', '--verbose', action='store_true',
                            help='increase output verbosity')
        return parser.parse_args()

    def btn_folder_browse_clicked(self):
        """Choose project folder.
        """

        pr_folder_init = self.txt_02.get()
        pr_folder = filedialog.askdirectory(
            initialdir=os.path.dirname(pr_folder_init))
        if pr_folder == '':
            pr_folder = pr_folder_init
        self.txt_02.delete(0, END)
        self.txt_02.insert(0, pr_folder)

    def btn_file_browse_clicked(self):
        """Choose file.
        """

        pr_file_init = self.txt_03.get()
        pr_file = filedialog.askopenfilename(filetypes=(("Python files", "*.py"),
                                                        ("all files", "*.*")),
                                             initialdir=os.path.dirname(pr_file_init))
        if pr_file == '':
            pr_file = pr_file_init
        self.txt_03.delete(0, END)
        self.txt_03.insert(0, pr_file)

    def btn_ok_clicked(self):
        """Button OK clicked.
        """

        res = messagebox.askyesno(
            'Confirmation', 'Are you sure to set back the default values?')
        if res:
            print('OK')

    def execute_program(self):
        """Execute the program by arguments.
        """
        args = self.parse_arguments()
        self.par_input = args.input
        self.par_output = args.output
        LOGGER.debug('Input: %s', self.par_input)
        LOGGER.debug('Output: %s', self.par_output)

        lbl_01 = Label(self.window, text='Project type:')
        lbl_01.grid(column=0, row=0, sticky='E')
        self.cmb_01.current(2)
        self.cmb_01.grid(column=1, row=0, sticky='W')
        lbl_02 = Label(self.window, text='Project name:')
        lbl_02.grid(column=0, row=1, sticky='E')
        self.txt_01.delete(0, END)
        self.txt_01.insert(0, 'Project')
        self.txt_01.grid(column=1, row=1, sticky='W')
        lbl_03 = Label(self.window, text='Folder:')
        lbl_03.grid(column=0, row=2, sticky='E')
        self.txt_02.delete(0, END)
        self.txt_02.insert(0, self.project_folder)
        self.txt_02.grid(column=1, row=2, sticky='W')
        btn_folder_browse = Button(self.window, text='Browse...',
                                   command=self.btn_folder_browse_clicked)
        btn_folder_browse.grid(column=2, row=2)
        lbl_03 = Label(self.window, text='File:')
        lbl_03.grid(column=0, row=3, sticky='E')
        self.txt_03.delete(0, END)
        self.txt_03.insert(0, 'Project')
        self.txt_03.grid(column=1, row=3, sticky='W')
        btn_file_browse = Button(self.window, text='Browse...',
                                 command=self.btn_file_browse_clicked)
        btn_file_browse.grid(column=2, row=3)
        lbl_04 = Label(self.window, text='Description:')
        lbl_04.grid(column=0, row=4, sticky='E'+'N')
        self.scr_01.delete(1.0, END)
        self.scr_01.insert(
            INSERT, 'Multiline description of the program.\nWrite description here.')
        self.scr_01.grid(column=1, row=4)
        chk_01 = Checkbutton(self.window, text='SQLite', var=self.chk_01_state)
        chk_01.grid(column=0, row=5)
        btn_ok = Button(self.window, text='OK',
                        command=self.btn_ok_clicked)
        btn_ok.grid(column=1, row=6)

        self.window.mainloop()

    def sample_function(self):
        """Sample function
        """
        res = self.par_input
        return res


if __name__ == '__main__':
    LOGGER.debug('Start program')
    PROG = __PROJECTNAME__()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
