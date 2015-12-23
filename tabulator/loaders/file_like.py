# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from .api import API


class FileLike(API):
    """Loader to load source from file-like objects.
    """

    def __init__(self, source, encoding=None, **options):
        self.__source = source

    def load(self, mode=None):
        return self.__source
