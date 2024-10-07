#!/bin/bash
grep -c "CSC510" \dataset1/file*| grep -E ":[3-9]$" | cut -d: -f1