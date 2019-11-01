"""
WARNING: Currently this code ignores hierarchies.

Budget years are also currently hardcoded.
"""
from __future__ import print_function

import datetime
import glob
import re

from lxml import etree
from stats.common import budget_year
from stats.dashboard import ActivityStats

xsDateRegex = re.compile("(-?[0-9]{4,})-([0-9]{2})-([0-9]{2})")

count = 0

for fpath in glob.glob("data/*/*"):
    for activity in etree.parse(fpath).xpath("/iati-activities/iati-activity"):
        activity_stats = ActivityStats()
        activity_stats.element = activity
        current = activity_stats.forwardlooking_activities_current()
        w_budgets = activity_stats.forwardlooking_activities_with_budgets()
        if current[2019] and not w_budgets[2019]:
            print(activity.xpath("./iati-identifier/text()")[0])
        elif current[2020] and not w_budgets[2020]:
            print(activity.xpath("./iati-identifier/text()")[0])
        elif current[2021] and not w_budgets[2021]:
            print(activity.xpath("./iati-identifier/text()")[0])
