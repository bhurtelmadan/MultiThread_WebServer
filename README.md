# MultiThread_WebServer
How to handle different type of HTTP response
i. 202 OK : localhost:[serverPort]/test.html
ii. 301 Moved Permanently : localhost:[serverPort]/tes.html
-> If you enter this, it will re-direct to localhost:
[serverPort]/test.html
iii. 404 error: Any file name except test.html or tes.html will get this error 404 error


Reference: 
https://emalsha.wordpress.com/2016/11/24/how-create-http-server-using-python-socketpart-
ii/
https://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/
