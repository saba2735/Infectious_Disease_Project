#!/bin/bash

set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running simulation data for kids...'
python bar_charts.py \
    --file_name simulation_results.csv \
    --age_group 'kids' \
    --output_file kids.png \