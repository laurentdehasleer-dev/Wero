#!/bin/bash
set -e
python final_lcl_fix.py
python fix_cic.py
python fix_lcl.py
echo "All scripts completed successfully"
