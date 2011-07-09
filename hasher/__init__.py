#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Just a simple hasher function
"""

import hashlib

def get_hash(file_path):
    """
    return the MD5 hash of the file_path file
    """
    hashed_file = open(file_path, 'rb')
    content = hashed_file.read()
    hashed_file.close()
    return(hashlib.md5(content).hexdigest())