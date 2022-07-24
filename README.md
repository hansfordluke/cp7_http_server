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
1. [Start up the server]
	* $python3 http_server.py

2. [Start up the client]
	* $python3 http_client.py
3. Identify file type: [text] or [file]
	* [T] for text; [F] for file

4. (a) For [File], **Provide Pathway**
4. (b) For [Text], **Enter Message**

5. Specify path to [Server] or [Website]
	* The server [temporary] stores message
	* The website [permanently] logs message

6. [Automatic Message encoding] 
	* The ASCII text converts to Hex bytes
	* Hex on a base of 16 [0 to 15] adjusted to [1 to 16]
	* Random generation of URI separated by '/' between each hex byte
		* The URI length = Hex value [1 to 16]
	* The URL request concludes with a file type from a list of file types 
		* '.zip'
		* '.txt'
		* '.html'
		* '.jpg'
		* '.pdf'
		* '.html'
		
7. The client sends the HTTP GET request to the server

_Server Reponse_:
1. Receives the GET request
2. [Decodes the message]
	* Reverses the process that the client used to encode the message

8. Login credentials to frozen-ravine-68174.herokuapp.com/admin/
	* username: admin
	* password: password
	* Go to this admin website to view the live changes to the online database of decoded messages
	* Run the client and then refresh the admin page to view the new database entry

