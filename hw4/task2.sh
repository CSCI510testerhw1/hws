#!/bin/bash
grep "CSC510" \dataset1/file* | sort | uniq -c | cut -d: -f1 | grep -E -v "[1-2] " | grep -E -o "file_[0-9]*"
