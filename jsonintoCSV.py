import requests
import json
import csv

# response = requests.get('http://universities.hipolabs.com/search?country=United+States',
	# headers={"Content-Type": "application/json"}
# )
response = requests.get('http://universities.hipolabs.com/search?country=United+States',
	headers={"Content-Type": "application/json"}
)

print(response.status_code)
print(response.encoding)

if response:
  print('Request is successful.')
else:
  print('Request returned an error.')
  
#print(response.text)


# Using a JSON string
with open('jjjson_data.json', 'w') as outfile:
    outfile.write(response.text)

outfile.close()

	
with open('fjson_data.json', encoding="utf-8", errors='ignore') as json_file:
    jsondata = json.load(json_file)
 
data_file = open('fjson_data.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
 
count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
 
data_file.close()











# with open('fjson_data.json', 'r') as json_file:
	# data= json.load(json_file)
	
# college_data = data[]

# data_file = open('data_file.csv', 'w')







# # create the csv writer object
# csv_writer = csv.writer(data_file)
 
# # Counter variable used for writing
# # headers to the CSV file
# count = 0
 
# for emp in college_data:
    # if count == 0:
 
        # # Writing headers of CSV file
        # header = emp.keys()
        # csv_writer.writerow(header)
        # count += 1
 
    # # Writing data of CSV file
    # csv_writer.writerow(emp.values())

# data_file.close()


