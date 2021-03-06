#! Python3
#Graph battery usage over time for iPHone and Android logs. 

import re, pyperclip
import plotly.express as px

dateRegex = re.compile(r'''(
    (\d{4}-\d\d-\d\d)\s             # date
    (\d\d:\d\d:\d\d)                # time
    (.{2,100})                      # log info
    (Battery\slevel:|Battery:)\s?   # Delimiter
    (\d\.\d\d|\d\d)\%?              # Percent as a int or float
    )''', re.VERBOSE)               # re.VERBOSE so I can multiline and comment

txt = str(pyperclip.paste())

times = []
percents = []

# TODO: Normalize the float to an int
for groups in dateRegex.findall(txt):
    times.append(groups[2])
    percents.append(float(groups[5]))

if times == [] or percents == []:
    print('No matches')
    exit
else:
    print(f'{len(times)} matches found')
    fig = px.line(
        x = times,
        y = percents,
        labels = {'x':'time', 'y':'percent'}
    )
    fig.show()