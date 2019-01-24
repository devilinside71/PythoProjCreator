# -*- coding: utf-8 -*-
"""
__DESCRIPTION__
"""
import argparse
import logging
import os
import sys
from pathlib import Path

from PyQt5 import QtCore, QtWidgets

from ui.mainwindow import MainWindow


__author__ = '__AUTHOR__'
__copyright__ = 'Copyright 2027, __AUTHOR__'

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


def parse_arguments():
    """
    Parse program arguments.

    @return arguments

    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose',
                        help='increase output verbosity',
                        action='store_true')
    return parser.parse_args()


if __name__ == '__main__':

    ARGS = parse_arguments()
    LOGGER.debug('Start program')
    # Read loc_lang from settings file
    SETTINGS = QtCore.QSettings('settings.ini', QtCore.QSettings.IniFormat)
    SETTINGS.beginGroup('UserSettings')
    LOC_LANG = SETTINGS.value('Language')
    SETTINGS.endGroup()
    APP = QtWidgets.QApplication(sys.argv)
    PARENT_PATH = os.path.join(__file__, os.path.pardir)
    DIR_PATH = os.path.abspath(PARENT_PATH)
    FILE_PATH = os.path.join(DIR_PATH, 'i18n', LOC_LANG + '.qm')
    if Path(FILE_PATH).exists():
        TRANSLATOR = QtCore.QTranslator()
        TRANSLATOR.load(FILE_PATH)
        APP.installTranslator(TRANSLATOR)
    UI = MainWindow(ARGS)
    UI.show()
    sys.exit(APP.exec_())
    LOGGER.debug('Exit program')
