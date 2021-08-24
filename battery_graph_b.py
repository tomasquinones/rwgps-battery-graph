#! Python3
# Graph battery usage over time for iPhone and Android logs. 
# Switching to Bokeh for visualizations 
# https://docs.bokeh.org/en/latest/docs/first_steps/first_steps_1.html

import re, pyperclip, time
import time
from bokeh.plotting import figure, show



dateRegex = re.compile(r'''(
    (\d{4}-\d\d-\d\d)\s             # date
    (\d\d:\d\d:\d\d)                # time
    (.{2,100})                      # log info
    (Battery\slevel:|Battery:)\s?   # Delimiter
    (\d\.\d\d|\d\d)\%?              # Percent as a int or float
    )''', re.VERBOSE)               # re.VERBOSE so I can multiline and comment

txt = str(pyperclip.paste())

times = []                          # x coordinate
percents = []                       # y coordinate

# TODO: Normalize the float to an int
for groups in dateRegex.findall(txt):
    times.append(groups[2])
    percents.append(float(groups[5]))

if times == [] or percents == []:
    print('No matches')
    exit
else:
    print(f'{len(times)} matches found')
    p = figure(title="Simple Battery Graph", x_axis_label='time', y_axis_label='Percent')
    p.line(times, percents, line_width=2)
    show(p)