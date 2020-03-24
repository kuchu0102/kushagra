import requests
from pprint import pprint
categories_url_template = 'https://data.police.uk/api/crime-categories?date={date}'
my_latitude = '51.52369'
my_longitude = '-0.0395857'
my_date = '2018-11'
crime_url = crime_url_template.format(lat = my_latitude,lng = my_longitude,data = my_date)
resp = requests.get(crime_url)
if resp.ok:
	crimes = resp.json()
else:
	print(resp.reason)

crime_outcome_stats = {'None':0}
for crime in crimes:
	outcome = crime["outcome_status"]
	if not outcome:
		crime_outcome_stats['None'] += 1
	elif outcome['category'] not in crime_outcome_stats.keys():
		crime_outcome_stats.update({outcome['category']:1})
	else:
		crime_outcome_stats[outcome['category']]+=1
print(crime_outcome_stats)

