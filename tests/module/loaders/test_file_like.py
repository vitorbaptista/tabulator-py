# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest
from importlib import import_module
module = import_module('tabulator.loaders.file_like')


class FileLikeTest(unittest.TestCase):
    def test_load_returns_source(self):
        filelike = module.FileLike('filelike-object')
        self.assertEqual(filelike.load(), 'filelike-object')
