#How to use the Victoria and Albert Museum's API
#Detailed API documentation is available at: http://www.vam.ac.uk/api/
For my project, I used the Victoria & Albert Museum’s API (http://www.vam.ac.uk/api/). I found the API to be more usable than other museum APIs because it offers a Query Builder (http://www.vam.ac.uk/api/qb), which allowed me to build a URL; the Builder made it clear which parameters I needed to use when writing my script.
 
I chose to work with the V&A’s collection of Linnaeus Tripe’s photography of South India and Burma (Myanmar) because it offered latitude and longitude metadata, and my plan was to visually map where each photograph was taken. Unfortunately, after mapping my data in CartoDB, the photographs were concentrated in only a few areas and weren’t visually appealing. 

The first coding difficulty I had was determining how to view all records. After experimenting with the range function, I found that I needed to start at 0, stop at 129 (total records), and “step” in increments of 45 (the maximum amount of records that the V&A museum allows to be viewed at once). After defining the range function, I kept getting inaccurate results when I first ran the script; I wasn’t getting the 129 photograph records I knew existed in return. I then realized “'images' : 1” needed to be added as a parameter in order to indicate I was only interested in images. The most difficulty I had was writing my results to a .csv file. Once the script finally wrote to the csv, the columns were a mess, there wasn’t much spacing. Using “row = [str(x).replace("\n", "") for x in row” allowed for spaces.

For my visualization, I chose to work with Northwestern University Knight Lab's Timeline JS, a tool for creating interactive timelines. It is a usable program; you download a template and add your data into the template’s columns accordingly. The data needs to be structured properly to Timeline JS’s constraints or else it will not be viewable. I wanted to use the Wikipedia API in order pull URLs of websites pertaining to the monuments and locations mentioned in the V&A’s description of each photograph (though, some photographs are missing cataloged descriptions)--however, many of the described monuments do not have Wikipedia pages, so I had to manually search for each description in the V&A’s catalog and add the links to my Timeline. 

Lastly, since it was my main reason for choosing the Tripe collection, I wanted to incorporate latitude and longitude somehow. I concatenated the latitude and longitude and a standard Google Maps URL to come up with a direct link to that latitude and longitude in Google Maps. It seems that the given latitudes and longitudes are only for the city, not the exact location of where the photograph was taken. Regardless, it is interesting to view the setting of the mid-19th century photograph in a modern context. Sadly, one can’t quite see these incredibly constructed monuments and architecture in Google Maps today.

#Here's how to use the API and write your data to a csv:

 

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
       p = re.compile('^[0-9]{4}..')
       m = p.findall(our_text)

