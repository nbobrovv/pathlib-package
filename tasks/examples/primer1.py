#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import collections

print(collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir()))