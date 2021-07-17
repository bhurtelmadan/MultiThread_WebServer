# MultiThread_WebServer

 Develop a Web server in two steps. In the end, you will have built a multi-threaded Web server that is capable of processing multiple simultaneous service requests in parallel. You should be able to demonstrate that your Web server is capable of delivering your home page to a Web browser.

We are going to implement version 1.0 of HTTP, where separate HTTP requests are sent for each component of the Web page. The server will be able to handle multiple simultaneous service requests in parallel. This means that the Web server is multi-threaded. In the main thread, the server listens to a fixed port. When it receives a TCP connection request, it sets up a TCP connection through another port and services the request in a separate thread. 


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
