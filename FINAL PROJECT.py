import requests
import json


               #range = (start, stop, offset)
offsetvalues = range(0, 129, 45)
response_dict = {}

#since we only want images, want the maximum amount of records (45), and need to see all records, add to payload
for offsetval in offsetvalues:
    payload = { 'q' : "Linnaeus+Tripe", 'images' : 1, 'limit' : 45, 'offset' : offsetval }
    r = requests.get("http://www.vam.ac.uk/api/json/museumobject/", params=payload)
    response_dict = json.loads(r.text)
    for a_record in response_dict['records']:
        row = [a_record['pk'],a_record['fields']['primary_image_id'],a_record['fields']['longitude'],a_record['fields']['latitude'],a_record['fields']['place'],
            a_record['fields']['title'],a_record['fields']['date_text']]

        print(row)    

##response_dict = json.loads(r.text)
##
##for a_record in response_dict['records']:
##    try:
##        print(a_record)
##    except:
##        print("No record.")
##
##for a_title in response_dict['records']['fields'][15]:
##    try:
##        print(a_title)
##    except:
##        print("None.")
##
##
##
##             

##for a_record in response_dict['records']['fields']:
##    print(response_dict)
##    try:
##        #lets store the name in its own variable
##	#the [0] is because it is an list, so we only want the first author
##        year_start = a_record['records']['fields']
##        print("Looking at",year_start)
##    except:
##        print("No year.")


