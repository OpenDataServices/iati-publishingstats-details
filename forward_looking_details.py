"""
WARNING: Currently this code ignores hierarchies.
"""
from __future__ import print_function

import csv
import datetime
import glob
import re
import sys

from lxml import etree
from stats.common import budget_year
from stats.dashboard import ActivityStats

writer = csv.writer(sys.stdout)

for fpath in glob.glob("data/*/*"):
    for activity in etree.parse(fpath).xpath("/iati-activities/iati-activity"):
        activity_stats = ActivityStats()
        activity_stats.element = activity
        current = activity_stats.forwardlooking_activities_current()
        w_budgets = activity_stats.forwardlooking_activities_with_budgets()
        end_dates = activity.xpath(
            "./activity-date[@type='{}' or @type='{}']".format(
                activity_stats._planned_end_code(), activity_stats._actual_end_code()
            )
        )

        iati_identifier = activity.xpath("./iati-identifier/text()")[0]
        reason_current = ""
        reason_budget = ""
        if not end_dates:
            reason_current = "No end dates"
        if not activity.xpath("./budget"):
            reason_budget = "No budgets"

        for year in sorted(current.keys()):
            if current[year] and not w_budgets[year]:
                writer.writerow([iati_identifier, year, reason_current, reason_budget])
                break
