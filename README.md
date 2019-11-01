# IATI publishingstats details

Ad-hoc scripts to display per activity information for the [IATI publishingstats](http://publishingstats.iatistandard.org/).

Note: This repo requires Python 2.7, because they IATI-Publishing-Statistics code that it depends on requires this.

```
git clone git@github.com:OpenDataServices/iati-publishingstats-details.git
cd iati-publishingstats-details
# then put some IATI activities files into data/subdir
git submodule init
git submodule update
virtualenv .ve
source .ve/bin/activate
pip install -r requirements.txt
./fetch_helpers.sh
python forward_looking_details.py > forward_looking_details.csv
```
