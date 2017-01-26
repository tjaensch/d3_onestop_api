import json

with open('json_response_raw.json', 'r') as blahJson:
	parsedBlahJson = json.load(blahJson)

# pretty print raw JSON response
print json.dumps(parsedBlahJson, indent=4, sort_keys=True)