# Day 2 - Learn from Home (Python track)
Okay, so there are quite a few things that we discussed today.


![](https://paper-attachments.dropbox.com/s_9279DA2F73FD024B960A9A4C0128446D3FC84ADBBB3A48D87D331A736EA64568_1584796400258_client-server.png)



## Basic client-server model

### Request
When you type in the address of a website in your browsers address bar, the browser constructs an http request. An http request contains the address you typed in along with some other relevant data. This data is then sent over to the server (we don’t need to know how). As far as the client is concerned, the server then processes the request and returns the appropriate response.

### Response
The response can be of different types. The most common types are HTML, CSS and JS. It is the job of the web browser to process HTML, CSS and JS and display the content appropriately.

### Client vs Server
Let us mark the distinction between client and server clearly. The primary role of a client is to send http requests and receive http responses. In most cases your client is web browser, which means it has the added responsibility of rendering the webpage as per the http response. Whereas the job of server is to receive requests and return the appropriate response. There are two primary methods of doing this. See next section.


## Dynamic vs Static websites

Now let us talk a bit about the right side of that image. In it, I’ve drawn an arrow from server to Flask (ignore the WSGI). The truth is, frameworks like Flask is not always necessary. This is where we need to differentiate between static websites  and dynamic websites. 

### Static websites
Static websites have their responses already stored in their server as webpages. When servers for such websites receives a request from the client they simply return the corresponding webpage. They do not have a program sitting behind the server, creating the response then and there.

For example, if you have a personal webpage containing your contact information, you can publish it as a static website. You can write the html code for the website and store it on your server as an html file. You can then configure your server to simply return the contents of that html file every time a request is received.

### Dynamic websites
Dynamic websites have a different approach. Consider that you want to build a website that displays the current date. It is not possible to store the appropriate response for such a webpage in our server because the appropriate response depends on the date on which the request is made. Instead, every time a user visits your website, you have to identify the current date on the spot and then return it. This is where a dynamic website come into play. Whenever a request is received by a server for such a website, the server passes on the request to an appropriate web app. This web app first reads the current date. It then generates the appropriate html code with the date injected in between and returns it to the server. The server further sends the response back to the client.

A more relatable example would be your facebook feed page. Even though you asked for www.facebook.com, you always get your own feed. The response depends on the username and password that you had entered.


## Flask

I hope now you can guess by now why we need a framework like Flask. Flask helps us build dynamic web applications. Simply put it helps us build appropriate responses to requests on the go.


![](https://paper-attachments.dropbox.com/s_9279DA2F73FD024B960A9A4C0128446D3FC84ADBBB3A48D87D331A736EA64568_1584803321170_flaskapp.png)


### Routes
Whenever a request is passed to the flask app, it is passed to the `routes.py`. This file contains a bunch of view functions associated with different addresses. Remember that the request contains the address. Depending on that address, Flask will call the appropriate view function.

### View function
This is where most of the job gets done. It is job of various view functions to generate the appropriate http response. The view function has access to all the data within the request. It can use this data to determine the appropriate response to send back.

If you remember the example we mentioned, this is where the code to find date should live.

Templates, db and sql-alchemy

- I’ll add it after the next sessions

> I had mistakenly said that the names of certain files had to be the ones I mentioned. That is not the case. You can name it whatever you want as long as you import it correctly. Sorry for the error.
