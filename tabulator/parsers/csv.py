# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import csv
import six
from codecs import iterencode

from .. import helpers
from .api import API


# Module API

class CSV(API):
    """Parser to parse CSV data format.
    """

    # Public

    def __init__(self, **options):
        self.__options = options
        self.__loader = None
        self.__chars = None
        self.__items = None

    def open(self, loader):
        self.close()
        self.__loader = loader
        self.__chars = loader.load(mode='t')
        self.reset()

    def close(self):
        if not self.closed:
            self.__chars.close()

    @property
    def closed(self):
        return self.__chars is None or self.__chars.closed

    @property
    def items(self):
        return self.__items

    def reset(self):
        helpers.reset_stream(self.__chars)
        self.__items = self.__emit_items()

    # Private

    def __emit_items(self):

        # For PY2 encode/decode
        if six.PY2:
            # Reader requires utf-8 encoded stream
            bytes = iterencode(self.__chars, 'utf-8')
            items = csv.reader(bytes, **self.__options)
            for item in items:
                values = []
                for value in item:
                    value = value.decode('utf-8')
                    values.append(value)
                yield (None, tuple(values))

        # For PY3 use chars
        else:
            items = csv.reader(self.__chars, **self.__options)
            for item in items:
                yield (None, tuple(item))
