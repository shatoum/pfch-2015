import requests
import json
import re
import csv

with open("finalproject.csv","w") as a_file:

    offsetvalues = range(0, 129, 45)
    response_dict = {}

    for offsetval in offsetvalues:
        payload = { 'q' : "Linnaeus+Tripe", 'images' : 1, 'limit' : 45, 'offset' : offsetval }
        r = requests.get("http://www.vam.ac.uk/api/json/museumobject/", params=payload)
        response_dict = json.loads(r.text)
        for a_record in response_dict['records']:
                    
            row = [a_record['pk'], a_record['fields']['primary_image_id'],a_record['fields']['latitude'],a_record['fields']['longitude'],a_record['fields']['place'],
                a_record['fields']['title'],a_record['fields']['date_text']]
            row = [str(x).replace("\n", "") for x in row]
            a_file.write(','.join(row)+'\n')


           
        
        #our_text = a_record['fields']['primary_image_id']
        #compile  pattern with regex
        #p = re.compile('^[0-9]{4}..')
        #m = p.findall(our_text)
        







        
