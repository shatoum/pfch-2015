import requests
import json

#create lists for the metadata I want:

pk = []
primary_image_id = []
longitude = []
latitude = []
place = []
title = []
date_text = []
#And I only want photographs, so:
object_type = []

payload = { 'q' : "Linnaeus+Tripe", 'limit' : 45, 'offset' : 3 }
r = requests.get("http://www.vam.ac.uk/api/json/museumobject/", params=payload)

response_dict = json.loads(r.text)

for a_record in response_dict['records']:
    try:
        print(a_record)
    except:
        print("No record.")

for a_title in response_dict['records']['fields'][15]:
    try:
        print(a_title)
    except:
        print("None.")




        
#write to csv:



              

##for a_record in response_dict['records']['fields']:
##    print(response_dict)
##    try:
##        #lets store the name in its own variable
##	#the [0] is because it is an list, so we only want the first author
##        year_start = a_record['records']['fields']
##        print("Looking at",year_start)
##    except:
##        print("No year.")


