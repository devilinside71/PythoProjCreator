# -*- coding: utf-8 -*-
"""
This module creates python basic project files in a folder.
"""

import errno
import logging
import os
import sys
import shutil
# from tkinter import *
# from tkinter.ttk import *
from tkinter import Tk, Entry, Label, Button, Checkbutton, scrolledtext, messagebox, filedialog
from tkinter import BooleanVar, END, INSERT
from tkinter.ttk import Combobox
from pathlib import Path
# from textnormalizer import TextNormalizer

__author__ = 'Laszlo Tamas'
__copyright__ = 'Copyright 2027, Laszlo Tamas'
__license__ = 'GPL'
__version__ = '0.0.1'
__maintainer__ = 'Laszlo Tamas'
__email__ = 'laszlo.devil@gmail.com'
__status__ = 'Initial'


LOGGER = logging.getLogger('pythonprojcreator')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
LOGGER.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
LOGGER_FH = logging.FileHandler('pythonprojcreator.log')

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


class ProjCreatorProgram():
    """Main class.

    """

    def __init__(self):
        self.home = str(Path.home())
        self.documents_folder = str(os.path.join(self.home, 'Documents'))
        self.git_folder = str(os.path.join(self.documents_folder, 'GitHub'))
        self.project_folder = os.path.join(self.git_folder, 'Project')
        self.main_script = 'main.py'
        self.window = Tk()
        self.cmb_project_type = Combobox(self.window)
        self.cmb_project_type['values'] = ('CLI', 'Tkinter', 'PyQt')
        self.txt_project_name = Entry(self.window, width=20)
        self.txt_project_folder = Entry(self.window, width=50)
        self.txt_main_script = Entry(self.window, width=20)
        self.scr_description = scrolledtext.ScrolledText(
            self.window, width=40, height=10)
        self.project_author = 'Laszlo Tamas'

    @staticmethod
    def create_folder(folder_name):
        """Create folder for new project.

        Arguments:
            folder_name {str} -- target folder name

        Returns:
            bool -- folder created succesfuly
        """
        ret = False
        LOGGER.debug('Target folder: %s', folder_name)
        # Check if folder exists
        folder_exists = os.path.isdir(folder_name)
        if folder_exists:
            LOGGER.debug('Folder "%s" already exists', folder_name)
        else:
            # create folder
            try:
                os.makedirs(folder_name)
                LOGGER.debug('Folder "%s" created succesfuly', folder_name)
                ret = True
            except OSError as os_err:
                ret = False
                if os_err.errno != errno.EEXIST:
                    LOGGER.debug('Cannot create folder %s', folder_name)
                    LOGGER.debug('Exit program')
                    raise
        return ret

    @staticmethod
    def normalized_name(string_to_normalize):
        """Replace non US characters

        Arguments:
            string_to_normalize {str} -- string to normalize

        Returns:
            str -- normalized string
        """

        res = string_to_normalize
        res = res.replace('á', 'a')
        res = res.replace('Á', 'A')
        res = res.replace('é', 'e')
        res = res.replace('É', 'E')
        res = res.replace('ö', 'o')
        res = res.replace('Ö', 'O')
        res = res.replace('ő', 'o')
        res = res.replace('Ő', 'O')
        res = res.replace('ó', 'o')
        res = res.replace('Ó', 'O')
        res = res.replace('ü', 'u')
        res = res.replace('Ü', 'U')
        res = res.replace('ű', 'u')
        res = res.replace('Ű', 'U')
        res = res.replace('ú', 'u')
        res = res.replace('Ú', 'U')
        res = res.replace('í', 'i')
        res = res.replace('Í', 'i')
        res = res.replace(' ', '_')
        res = res.replace('.', '_')
        res = res.replace(':', '_')
        return res

    def btn_default_clicked(self):
        """Set back default values.
        """

        res = messagebox.askyesno(
            'Confirmation', 'Are you sure to set back the default values?')
        if res:
            self.cmb_project_type.current(2)
            self.txt_project_name.delete(0, END)
            self.txt_project_name.insert(0, 'Project')
            self.txt_project_folder.delete(0, END)
            self.txt_project_folder.insert(0, self.project_folder)
            self.txt_main_script.delete(0, END)
            self.txt_main_script.insert(0, 'main.py')
            self.scr_description.delete(1.0, END)
            self.scr_description.insert(
                INSERT, 'Multiline description of the program.\nWrite description here.')

    def create_cli(self):
        """Create CLI project.
        """
        self.create_folder(self.txt_project_folder.get())
        with open('sample_cli/sample01.py', 'r') as myfile:
            data = myfile.read()
            data = data.replace('__AUTHOR__', self.project_author)
            data = data.replace('__PROJECTNAME__',
                                self.txt_project_name.get())
            data = data.replace('__PROJECTNAMELCASE__',
                                self.txt_project_name.get().lower())
            data = data.replace('__DESCRIPTION__',
                                self.scr_description.get(1.0, END))
            text_file = open(os.path.join(self.txt_project_folder.get(),
                                          self.txt_main_script.get()), 'w', encoding='utf-8')
            text_file.write(data)
            text_file.close()
            LOGGER.debug('CLI-main file %s created',
                         self.txt_main_script.get())
        # Create unittest file
        with open('sample_cli/sample01_test.py', 'r') as myfile:
            data = myfile.read()
            data = data.replace('__AUTHOR__', self.project_author)
            data = data.replace('__PROJECTNAME__',
                                self.txt_project_name.get())
            data = data.replace('__PROJECTNAMELCASE__',
                                self.txt_project_name.get().lower())
            data = data.replace('__DESCRIPTION__',
                                self.scr_description.get(1.0, END))
            text_file = open(os.path.join(self.txt_project_folder.get(),
                                          os.path.splitext(self.txt_main_script.get())[0])
                             + '_test.py', 'w', encoding='utf-8')
            text_file.write(data)
            text_file.close()
            LOGGER.debug('CLI-unittest file %s created',
                         os.path.splitext(self.txt_main_script.get())[0]+'_test.py')
        # Create notes text file
        with open('sample_cli/sample01_notes.txt', 'r') as myfile:
            data = myfile.read()
            data = data.replace('__PROJECTNAME__',
                                self.txt_project_name.get())
            data = data.replace('__PROJECTNAMELCASE__',
                                self.txt_project_name.get().lower())
            data = data.replace('__DESCRIPTION__',
                                self.scr_description.get(1.0, END))
            text_file = open(os.path.join(self.txt_project_folder.get(),
                                          os.path.splitext(self.txt_main_script.get())[0])
                             + '_notes.txt', 'w', encoding='utf-8')
            text_file.write(data)
            text_file.close()
            LOGGER.debug('CLI-notes file %s created',
                         os.path.splitext(self.txt_main_script.get())[0]+'_notes.txt')

    def create_tkinter(self):
        """Create tkinter project.
        """
        self.create_folder(self.txt_project_folder.get())
        with open('sample_tkinter/sample01.py', 'r') as myfile:
            data = myfile.read()
            data = data.replace('__AUTHOR__', self.project_author)
            data = data.replace('__PROJECTNAME__',
                                self.txt_project_name.get())
            data = data.replace('__PROJECTNAMELCASE__',
                                self.txt_project_name.get().lower())
            data = data.replace('__DESCRIPTION__',
                                self.scr_description.get(1.0, END))
            text_file = open(os.path.join(self.txt_project_folder.get(),
                                          self.txt_main_script.get()), 'w', encoding='utf-8')
            text_file.write(data)
            text_file.close()
            LOGGER.debug('Tkinter-main file %s created',
                         self.txt_main_script.get())
        # Create unittest file
        with open('sample_tkinter/sample01_test.py', 'r') as myfile:
            data = myfile.read()
            data = data.replace('__AUTHOR__', self.project_author)
            data = data.replace('__PROJECTNAME__',
                                self.txt_project_name.get())
            data = data.replace('__PROJECTNAMELCASE__',
                                self.txt_project_name.get().lower())
            data = data.replace('__DESCRIPTION__',
                                self.scr_description.get(1.0, END))
            text_file = open(os.path.join(self.txt_project_folder.get(),
                                          os.path.splitext(self.txt_main_script.get())[0])
                             + '_test.py', 'w', encoding='utf-8')
            text_file.write(data)
            text_file.close()
            LOGGER.debug('Tkinter-unittest file %s created',
                         os.path.splitext(self.txt_main_script.get())[0]+'_test.py')
        # Create notes text file
        with open('sample_tkinter/sample01_notes.txt', 'r') as myfile:
            data = myfile.read()
            data = data.replace('__PROJECTNAME__',
                                self.txt_project_name.get())
            data = data.replace('__PROJECTNAMELCASE__',
                                self.txt_project_name.get().lower())
            data = data.replace('__DESCRIPTION__',
                                self.scr_description.get(1.0, END))
            text_file = open(os.path.join(self.txt_project_folder.get(),
                                          os.path.splitext(self.txt_main_script.get())[0])
                             + '_notes.txt', 'w', encoding='utf-8')
            text_file.write(data)
            text_file.close()
            LOGGER.debug('Tkinter-notes file %s created',
                         os.path.splitext(self.txt_main_script.get())[0]+'_notes.txt')

    def create_pyqt(self):
        """Create PyQt project.
        """
        dir_ui = os.path.join(self.txt_project_folder.get(), 'ui')
        dir_i18n = os.path.join(self.txt_project_folder.get(), 'i18n')
        dir_pics = os.path.join(self.txt_project_folder.get(), 'pics')
        name_qrc = os.path.splitext(self.txt_main_script.get())[0]+'.qrc'
        self.create_folder(self.txt_project_folder.get())
        self.create_folder(dir_i18n)
        self.create_folder(dir_ui)
        self.create_folder(dir_pics)
        shutil.copy2('sample_pyqt/tl_lupdate.py',
                     self.txt_project_folder.get())
        shutil.copy2('sample_pyqt/settings.ini',
                     self.txt_project_folder.get())
        shutil.copy2('sample_pyqt/sample01.qrc',
                     os.path.join(self.txt_project_folder.get(), name_qrc))
        shutil.copy2('sample_pyqt/pyqt.png', dir_pics)

        with open('sample_pyqt/MainWindow.ui', 'r') as myfile:
            data = myfile.read()
            data = data.replace('pyqtguitest.qrc', name_qrc)
            text_file = open(os.path.join(
                dir_ui, 'MainWindow.ui'), 'w', encoding='utf-8')
            text_file.write(data)
            text_file.close()

        with open('sample_pyqt/sample01.py', 'r') as myfile:
            data = myfile.read()
            data = data.replace('__AUTHOR__', self.project_author)
            data = data.replace('__PROJECTNAME__',
                                self.txt_project_name.get())
            data = data.replace('__PROJECTNAMELCASE__',
                                self.txt_project_name.get().lower())
            data = data.replace('__DESCRIPTION__',
                                self.scr_description.get(1.0, END))
            text_file = open(os.path.join(self.txt_project_folder.get(),
                                          self.txt_main_script.get()), 'w', encoding='utf-8')
            text_file.write(data)
            text_file.close()
            LOGGER.debug('PyQt  files created')

    def btn_ok_clicked(self):
        """Execute creation.
        """
        pr_type = self.cmb_project_type.current()
        if pr_type == 0:
            self.create_cli()
        elif pr_type == 1:
            self.create_tkinter()
        elif pr_type == 2:
            self.create_pyqt()

    def btn_project_folder_hint_clicked(self):
        """Hint for project folder.
        """
        self.project_folder = os.path.join(
            self.git_folder, self.normalized_name(self.txt_project_name.get()))
        self.txt_project_folder.delete(0, END)
        self.txt_project_folder.insert(0, self.project_folder)

    def btn_main_script_hint_clicked(self):
        """Hint for main script.
        """
        self.main_script = self.normalized_name(
            self.txt_project_name.get()).lower()+'.py'
        self.txt_main_script.delete(0, END)
        self.txt_main_script.insert(0, self.main_script)

    def btn_folder_browse_clicked(self):
        """Choose project folder.
        """

        pr_folder_init = self.txt_project_folder.get()
        pr_folder = filedialog.askdirectory(
            initialdir=os.path.dirname(pr_folder_init))
        if pr_folder == '':
            pr_folder = pr_folder_init
        self.txt_project_folder.delete(0, END)
        self.txt_project_folder.insert(0, pr_folder)

    def btn_mainscript_browse_clicked(self):
        """Choose main script file.
        """
        main_file_init = self.txt_main_script.get()
        pr_folder_init = self.txt_project_folder.get()
        main_file = filedialog.askopenfilename(filetypes=(("Python files", "*.py"),
                                                          ("all files", "*.*")),
                                               initialdir=os.path.dirname(pr_folder_init))
        main_file = os.path.basename(main_file)
        if main_file == '':
            main_file = main_file_init
        self.txt_main_script.delete(0, END)
        self.txt_main_script.insert(0, main_file)

    def execute_program(self):
        """Main program part.
        """

        self.window.title('Project creator')
        lbl_0_0 = Label(self.window, text='Project type:')
        lbl_0_0.grid(column=0, row=0, sticky='E')
        lbl_0_1 = Label(self.window, text='Project name:')
        lbl_0_1.grid(column=0, row=1, sticky='E')
        lbl_0_2 = Label(self.window, text='Folder:')
        lbl_0_2.grid(column=0, row=2, sticky='E')
        lbl_0_3 = Label(self.window, text='Main script:')
        lbl_0_3.grid(column=0, row=3, sticky='E')
        lbl_0_4 = Label(self.window, text='Description:')
        lbl_0_4.grid(column=0, row=4, sticky='E')

        chk_0_5_state = BooleanVar()
        chk_0_5_state.set(True)
        chk_0_5 = Checkbutton(self.window, text='SQLite', var=chk_0_5_state)
        chk_0_5.grid(column=0, row=5)

        self.cmb_project_type.current(2)
        self.cmb_project_type.grid(column=1, row=0, sticky='W')

        self.txt_project_name.delete(0, END)
        self.txt_project_name.insert(0, 'Project')
        self.txt_project_name.grid(column=1, row=1, sticky='W')

        self.txt_project_folder.delete(0, END)
        self.txt_project_folder.insert(0, self.project_folder)
        self.txt_project_folder.grid(column=1, row=2, sticky='W')

        self.txt_main_script.delete(0, END)
        self.txt_main_script.insert(0, self.main_script)
        self.txt_main_script.grid(column=1, row=3, sticky='W')

        self.scr_description.delete(1.0, END)
        self.scr_description.insert(
            INSERT, 'Multiline description of the program.\nWrite description here.')
        self.scr_description.grid(column=1, row=4)

        btn_project_folder_hint = Button(self.window, text='Hint',
                                         command=self.btn_project_folder_hint_clicked)
        btn_project_folder_hint.grid(column=2, row=2)
        btn_main_script_hint = Button(self.window, text='Hint',
                                      command=self.btn_main_script_hint_clicked)
        btn_main_script_hint.grid(column=2, row=3)

        btn_folder_browse = Button(self.window, text='Browse...',
                                   command=self.btn_folder_browse_clicked)
        btn_folder_browse.grid(column=3, row=2)
        btn_mainscript_browse = Button(self.window, text='Browse...',
                                       command=self.btn_mainscript_browse_clicked)
        btn_mainscript_browse.grid(column=3, row=3)

        btn_default = Button(self.window, text='Default',
                             command=self.btn_default_clicked)
        btn_default.grid(column=0, row=6)

        btn_ok = Button(self.window, text='OK',
                        command=self.btn_ok_clicked, width=25)
        btn_ok.grid(column=1, row=6)

        self.window.mainloop()


if __name__ == '__main__':
    LOGGER.debug('Start program')
    PROG = ProjCreatorProgram()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
