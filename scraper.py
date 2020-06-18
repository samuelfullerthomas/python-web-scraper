import requests
import re

#  make a request to get a specific page
r = requests.get('https://www.basketball-reference.com/playoffs/')

# get the response text (the HTML)
webpage_HTML = r.text

# write a regex to parse the champions
champions_regex = r"<td class=\"left \" data-stat=\"champion\" ><a href=\".*?([\d]*?).html\">([A-Za-z\S\s]*?)<\/a><\/td>"

# this regex isn't working - it's also returning the champions! can you fix it?
runners_up_regex = r"<td class=\"left \" data-stat=\"champion\" ><a href=\".*?([\d]*?).html\">([A-Za-z\S\s]*?)<\/a><\/td>"

# find all instances that match that regex
champions = re.findall(champions_regex, webpage_HTML)
runners_up = re.findall(runners_up_regex, webpage_HTML)

print(champions)

# further learning: can you write a regex to finall all of the finals mvps?
# it might be useful to see the whole webpage html so you can know what to write the regex for
