import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import sys
import os
from itertools import chain


def hide_warnings():
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")


def line_marker():
    print('----------------------------------------------------------')
    print('\n')


def main():


    hide_warnings()

    pdata = pd.read_csv('Population-by-state.csv', skiprows=[0, 10])
    hdata = pd.read_csv('2007-2016-Homelessness-USA.csv')[14365:19142]

    print('Looking at the top rows of the data')
    print(pdata.head)
    line_marker()

    state_total = hdata[['State', 'Measures', 'Count']]
    is_useful = np.logical_or(state_total['Measures'] == 'Total Homeless', state_total['Measures'] == 'Unsheltered Homeless')
    state_total = state_total[is_useful][['State', 'Count']].reset_index(drop=True)
    print(state_total.head())
    print(state_total.tail())
    line_marker()

    abbr = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
        'American Samoa': 'AS',
        'District of Columbia': 'DC',
        'Federated States of Micronesia': 'FM',
        'Guam': 'GU',
        'Marshall Islands': 'MH',
        'Northern Mariana Islands': 'MP',
        'Palau': 'PW',
        'Puerto Rico': 'PR',
        'Virgin Islands': 'VI',
    }

    saplist = {abbr[pdata['Geography'][i]]: pdata['April 1, 2010 - Census'][i] for i in range(len(pdata))}
    print('Columns of interest')
    print(saplist)





main()

"""
import os
import csv
os.system("clear")

with open("usadb.csv") as usaf:
  usadb = list(csv.reader(usaf))[14372:19139:2]
with open("statedb.csv") as statef:
  statedb = list(csv.reader(statef))

#usadb = list(map(lambda s : s[:-1].split(",")[1:], open("usadb.csv").readlines()))[14372:19139:2]

#statedb = list(map(lambda s : int(s.split(",")[3]), open("statedb.csv").readlines()[2:]))
"""
