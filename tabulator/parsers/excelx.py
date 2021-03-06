# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import openpyxl

from .. import helpers
from .api import API


# Module API

class Excelx(API):
    """Parser to parse Excel modern `xlsx` data format.
    """

    # Public

    def __init__(self, sheet_index=0):
        self.__sheet_index = sheet_index
        self.__bytes = None
        self.__items = None

    def open(self, loader):
        self.close()
        self.__loader = loader
        self.__bytes = loader.load(mode='b')
        self.__book = openpyxl.load_workbook(self.__bytes, read_only=True)
        self.__sheet = self.__book.worksheets[self.__sheet_index]
        self.reset()

    def close(self):
        if not self.closed:
            self.__bytes.close()

    @property
    def closed(self):
        return self.__bytes is None or self.__bytes.closed

    @property
    def items(self):
        return self.__items

    def reset(self):
        helpers.reset_stream(self.__bytes)
        self.__items = self.__emit_items()

    # Private

    def __emit_items(self):
        for row in self.__sheet.rows:
            yield (None, tuple(cell.value for cell in row))
