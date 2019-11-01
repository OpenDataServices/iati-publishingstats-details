#!/bin/bash
set -e

# For how to do this properly see:
# https://github.com/IATI/IATI-Publishing-Statistics/blob/623498143ad809a57b87d357ea0dd0f65afd11b0/IATI-Stats/git.sh#L19
# This script does much less, as we only need a limited amount of the helpers
# to run the forwardlooking stats
cd helpers
./get_codelists.sh
touch registry_id_relationships.csv
echo '{}' > ckan.json
