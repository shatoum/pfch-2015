# pfch-2015
How to use the Victoria and Albert museum's API

#range="start, stop[, step])" start=0, stop=129 (the last record according to V&A API Query Builder)
offsetvalues = range(0, 129, 45)
#store results in dictionary
response_dict = {}

for offsetval in offsetvalues:
    payload = { 'q' : "Linnaeus+Tripe", 'images' : 1, 'limit' : 45, 'offset' : offsetval }
    r = requests.get("http://www.vam.ac.uk/api/json/museumobject/", params=payload)
    response_dict = json.loads(r.text)
    for a_record in response_dict['records']:
        #print(a_record)
        #create rows for  metadata I want to print and save to csv
        
        row = [a_record['pk'], a_record['fields']['primary_image_id'],a_record['fields']['latitude'],a_record['fields']['longitude'],a_record['fields']['place'],
            a_record['fields']['title'],a_record['fields']['date_text']]
        #note that "\n" is necessary; otherwise, your csv will be a mess. \n and "" provide spaces between words
        #row = [str(x).replace("\n", "") for x in row]
        #a_open_file.write(','.join(row)+'\n')
       
        #try to use regex to piece together a URL for all photographs
        #our_text = a_record['fields']['primary_image_id']
        #compile  pattern with regex
        #p = re.compile('^[0-9]{4}..')

        #"broad approach to finding all texts that match pattern"
        #m = p.findall(our_text)
        #print('http://media.vam.ac.uk/media/thira/collection_images/'+ m + ['primary_image_id'])

