import re
import os

filename = 'script_content_37.txt'

with open(filename, 'r', encoding='utf-8') as f:
    script_content = f.read()


# pattern = re.compile(r'cluster_id ?= ?\"(\d+(?:,\d+)*)\"')
pattern = re.compile(r'cluster_id ?= ?\"(\d+(?:,\d+)*)\"')
pattern.findall(script_content)