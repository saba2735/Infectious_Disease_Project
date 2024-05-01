#!/bin/bash

set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running VE data...'
python scatterplot.py ../data/re_calculation_results.csv kids ve 

# echo '...running R_E data...'
# python scatterplot.py ../data/re_calculation_results.csv kids re ../data/kids_re.png
