**D3 VISUALIZATION LIVE IN BROWSER**
http://bl.ocks.org/tjaensch/ee2685d323bde1a6cb0574de15d7d47b

**GIST**
https://gist.github.com/tjaensch/ee2685d323bde1a6cb0574de15d7d47b

**TO RUN D3 EXAMPLE LOCALLY**
Navigate to project directory and run "python -m SimpleHTTPServer" (Python version 2.*), then go to localhost:8000 (or replace 'localhost' with server IP address you're on)

**TEST QUERY**
request address encoded:
https://sciapps.colorado.edu/#/collections?%7B%22queries%22%3A%5B%7B%22type%22%3A%22queryText%22%2C%22value%22%3A%22space%22%7D%5D%2C%22filters%22%3A%5B%7B%22type%22%3A%22facet%22%2C%22name%22%3A%22locations%22%2C%22values%22%3A%5B%22Ocean%20%3E%20Pacific%20Ocean%20%3E%20North%20Pacific%20Ocean%20%3E%20Aleutian%20Islands%22%5D%7D%5D%2C%22facets%22%3Atrue%7D

request address decoded:
https://sciapps.colorado.edu/#/collections?{"queries":[{"type":"queryText","value":"space"}],"filters":[{"type":"facet","name":"locations","values":["Ocean > Pacific Ocean > North Pacific Ocean > Aleutian Islands"]}],"facets":true}

**NOTES**
- This example works with D3 version 3 and breaks when referencing version 4 which is the current one (see https://d3js.org/)
- The test query above produces 22 different keywords from the JSON response; a similar query with hundreds of different keywords takes a long time to load in the browser and the pie chart becomes too fragmented to be usable/make sense, also the legend won't fit on the canvas anymore




