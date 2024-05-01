#!/bin/bash

set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running RE data for kids...'
python reve.py ../data/re_calculation_results.csv kids ../data/re_kids.png

echo '...running RE data for adults...'
python reve.py ../data/re_calculation_results.csv adults ../data/re_adults.png

echo '...running RE data for grandparents...'
python reve.py ../data/re_calculation_results.csv grandparents ../data/re_grandparents.png