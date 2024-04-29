#!/bin/bash

set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running simulation data for kids...'
python bar_charts.py simulation_results.csv kids kids.png

echo '...running simulation data for adults...'
python bar_charts.py simulation_results.csv adults adults.png

echo '...running simulation data for grandparents...'
python bar_charts.py simulation_results.csv grandparents grandparents.png