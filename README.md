# cp7_http_server
## Challenge Problem 7 - Covert HTTP channel - Red Kraken
## ACE-2022
## Contributors: Luke Hansford | Micah Karchner | Wei Wei Kellmann

As a challenge posed by AFRL Advanced Course in Engineering (ACE) internship, our team created a HTTP Covert Channel based on size and case modulation patterns with the URI.

To access the Git repository: [github](https://github.com/hansfordluke/cp7_http_server)

_Relevant Materials_ included within this repository:

* http_client.py
* http_server.py

_To Run_:

* Python http_client.py
* [Enter Message]
* The ASCII converts to Hex
* Hex on a base of 16 [0 to 15] to [1 to 16]
* Random generation of URN separated by '/' between each hex
* The URN length = Hex value [1 to 16]
* The URL request concludes with a file type from a list of file types 
- '.zip'
- '.txt'
- '.html'
- '.jpg'
- '.pdf'
- '.html'

_Server reponse_: error code 404

