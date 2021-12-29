#!/usr/bin/env python3
import os
import sys

try:
    source_path = sys.argv[1]
except IndexError:
    print(f"No source directory specified")
    sys.exit()

if not os.path.exists(source_path):
    print(f"source {source_path} does not exists")
    sys.exit()
elif not os.path.isdir(source_path):
    print(f"source {source_path} is a file")
    sys.exit()

try:
    dest_path = sys.argv[2]
except IndexError:
    print(f"No destination directory specified")
    sys.exit()

if not os.path.exists(dest_path):
    print(f"destination {dest_path} does not exists")
    sys.exit()
elif not os.path.isdir(dest_path):
    print(f"destination {dest_path} is a file")
    sys.exit()


tiktoks = []
for root, dirs, files in os.walk(source_path):
	for file in files:
            print(file)
            if file.endswith(".mp4") and len(file) == 36:
                tiktoks.append(file)

for tiktok in tiktoks:
    source = os.path.join(source_path, tiktok)
    dest = os.path.join(dest_path, tiktok)
    print(source + " -> " + dest)
    os.rename(source, dest)