TO RUN D3 EXAMPLE navigate to project directory and run "python -m SimpleHTTPServer"

TEST QUERY

request address:

encoded:
https://sciapps.colorado.edu/#/collections?%7B%22queries%22%3A%5B%7B%22type%22%3A%22queryText%22%2C%22value%22%3A%22space%22%7D%5D%2C%22filters%22%3A%5B%7B%22type%22%3A%22facet%22%2C%22name%22%3A%22locations%22%2C%22values%22%3A%5B%22Ocean%20%3E%20Pacific%20Ocean%20%3E%20North%20Pacific%20Ocean%20%3E%20Aleutian%20Islands%22%5D%7D%5D%2C%22facets%22%3Atrue%7D

decoded:
https://sciapps.colorado.edu/#/collections?{"queries":[{"type":"queryText","value":"space"}],"filters":[{"type":"facet","name":"locations","values":["Ocean > Pacific Ocean > North Pacific Ocean > Aleutian Islands"]}],"facets":true}

copy as cURL (cmd):

curl "https://sciapps.colorado.edu/onestop/api/search" -H "Origin: https://sciapps.colorado.edu" -H "Accept-Encoding: gzip, deflate, br" -H "Accept-Language: en-US,en;q=0.8" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36" -H "content-type: application/json" -H "accept: application/json" -H "Referer: https://sciapps.colorado.edu/" -H "Connection: keep-alive" --data-binary "^{^\^"queries^\^":^[^{^\^"type^\^":^\^"queryText^\^",^\^"value^\^":^\^"space^\^"^}^],^\^"filters^\^":^[^{^\^"type^\^":^\^"facet^\^",^\^"name^\^":^\^"locations^\^",^\^"values^\^":^[^\^"Ocean ^> Pacific Ocean ^> North Pacific Ocean ^> Aleutian Islands^\^"^]^}^],^\^"facets^\^":true^}" --compressed

copy as cURL (bash):

curl 'https://sciapps.colorado.edu/onestop/api/search' -H 'Origin: https://sciapps.colorado.edu' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36' -H 'content-type: application/json' -H 'accept: application/json' -H 'Referer: https://sciapps.colorado.edu/' -H 'Connection: keep-alive' --data-binary '{"queries":[{"type":"queryText","value":"space"}],"filters":[{"type":"facet","name":"locations","values":["Ocean > Pacific Ocean > North Pacific Ocean > Aleutian Islands"]}],"facets":true}' --compressed


