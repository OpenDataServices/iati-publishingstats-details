"""
Hierarchies ???
"""
from __future__ import print_function

import csv
import datetime
import sys

from lxml import etree
from stats.dashboard import ActivityStats

writer = csv.writer(sys.stdout)
writer.writerow(["iati-identifier", "publishingstats_comprehensiveness_current"])


for fpath in sys.argv[1:]:
    for activity in etree.parse(fpath).xpath("/iati-activities/iati-activity"):
        activity_stats = ActivityStats()
        activity_stats.element = activity
        activity_stats.today = datetime.date.today()

        iati_identifier = activity.xpath("./iati-identifier/text()")[0]
        is_current = activity_stats._comprehensiveness_is_current()

        writer.writerow([iati_identifier, is_current])
