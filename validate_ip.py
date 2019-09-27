#!/usr/bin/python3
#############################################
#                                           #
#  Script  to carry out a sanity check on   #
#  provided cidr blocks                     #
#  Author: Erick Soi                        #
#  version 1.0                              #
#                                           #
#############################################

import csv, json, os, sys, ipaddress, yaml


## initializing empty lists to to hold named items
valid_blocks = []
invalid_blocks = []
public = []
private = []


## take and validate csv file containing CIDR blocks from user
file = input('Filename(a .csv file) $ ')
if not file.endswith('.csv'):
	sys.exit('csv file required')
try:
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile)
		rows = list(reader)
except FileNotFoundError:
	sys.exit("No file '{}' in the current path".format(file))


## create a json file, convert input from csv to json fomat for easy manipulation, 
## dump the data into the json file
json_file = 'json_output.json'
with open(json_file, "w") as f:
	json.dump(rows, f, sort_keys=True, indent=4, separators=(',', ': '))

with open('json_output.json', 'r') as f:
	data = json.load(f)
col_name = input('IP column name $ ')


## Iterate through the json data, validate addresses, append them on
## respective lists above, 
for ip in data:
	try:
		cidr_blocks = ipaddress.ip_network(ip[col_name])
		if cidr_blocks.is_private:
			private.append(str(cidr_blocks))
			valid_blocks.append(str(cidr_blocks))
		elif cidr_blocks.is_global:
			public.append(str(cidr_blocks))
			valid_blocks.append(str(cidr_blocks))
		else:
			valid_blocks.append(str(cidr_blocks))
		
	except KeyError:
		sys.exit("check collumn '{}' in '{}'".format(col_name, file))
	except ValueError:
		invalid_blocks.append(ip[col_name])#.format(cidr_blocks))


## remove the json file after serving its purpose.
os.remove("json_output.json")


## create yaml data to dump valid addresses 
data = dict(
	CidrBlock = '',
	)


## function to output valid addresses to respective yaml files.
def ToYamlFile(IpList, yamlfile):
	with open(yamlfile, 'w') as outfile:
		for ip in IpList:
			data["CidrBlock"] = ip
			yaml.dump(data, outfile, default_flow_style=False)
			


## Function to display addresses. 
def display(description, validity):
	print("\n",description)
	for ip in validity:
		print(ip)


## ToYamlFile Function call
ToYamlFile(valid_blocks, "all_valid.yaml")
ToYamlFile(public, "public.yaml")
ToYamlFile(private, "private.yaml")


## display Function call
display("Invalid block: ", invalid_blocks)


print('All valid, private and public adresses output: "private.yaml", "public.yaml", "all_valid.yaml"')
