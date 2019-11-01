"""
WARNING: Currently this code ignores hierarchies.
"""
from __future__ import print_function

import csv
import datetime
import re
import sys

from lxml import etree
from stats.common import budget_year
from stats.dashboard import ActivityStats

writer = csv.writer(sys.stdout)
writer.writerow(["iati-identifier", "First year to fail", "End dates", "Budget years"])


for fpath in sys.argv[1:]:
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
        budgets = activity.xpath("./budget")

        iati_identifier = activity.xpath("./iati-identifier/text()")[0]
        end_dates_str = ""
        budget_years_str = ""
        if end_dates:
            end_dates_str = ",".join(x.xpath("@iso-date")[0] for x in end_dates)
        else:
            end_dates_str = "No end dates"
        if budgets:
            budget_years = [budget_year(x) for x in budgets]
            budget_years_str = ",".join(str(x) for x in budget_years)
        else:
            budget_years_str = "No budgets"

        for year in sorted(current.keys()):
            if current[year] and not w_budgets[year]:
                writer.writerow(
                    [iati_identifier, year, end_dates_str, budget_years_str]
                )
                break
