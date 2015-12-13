#How to use the Victoria and Albert Museum's API
#Detailed API documentation is available at: http://www.vam.ac.uk/api/

 

       import requests
       import json
       import re
       import csv
  To write to csv:     
  
       with open("NAME OF PROJECT.csv","w") as a_file:
  The range function = "start, stop[, step])" start=0, stop=TOTAL RECORDS, step=45. 45 is the greatest number of items the V&A museum allows you to view at once. When you run your script, you will see records appear in groups of 45.
       
       offsetvalues = range(0, TOTAL RECORDS, 45)
    
  Store results in dictionary:
    
       response_dict = {}
   
  Set parameters:
  
    for offsetval in offsetvalues:
        payload = { 'q' : "COLLECTION OF INTEREST", 'images' : 1, 'limit' : 45, 'offset' : offsetval }
        r = requests.get("http://www.vam.ac.uk/api/json/museumobject/", params=payload)
        response_dict = json.loads(r.text)
        for a_record in response_dict['records']:
        
You can print(a_record) to make sure it works.
        
Now create rows for metadata you want and save everything to a csv:
        
            row = [a_record['METADATA TYPE'],a_record['METADATA TYPE']['METADATA TYPE'],a_record['METADATA TYPE']['METADATA     
            type'],a_record['METADATA    
            type']['longitude'],a_record['METADATA type']['METADATA TYPE WITHIN METADATA TYPE'],a_record['METADATA TYPE']['METADATA 
            TYPE WITHIN METADATA TYPE'],a_record['METADATA TYPE']['METADATA TYPE WITHIN METADATA TYPE']]
            
            row = [str(x).replace("\n", "") for x in row]
Note that "\n" is necessary; otherwise, your csv will be a mess. \n and "" provide spaces between words
           
           a_file.write(','.join(row)+'\n')
       
Either concatenate in Excel or try to use regex to piece together a full URL needed to view each individual photograph (see documentation). Here's the first step for using regex:
        
       our_text = a_record['fields']['primary_image_id']

Compile pattern with regex:
            p = re.compile('^[0-9]{4}..')

"Broad approach to finding all texts that match pattern":
            m = p.findall(our_text)
 
