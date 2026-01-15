
- So when we go, for example, to "reddit . com / chickens" and we hit enter
	- The web browser is sending an HTTP request
	- Request will eventually find its way to the reddit servers
	- The reddit servers response with the webpage 
	- Then we see the webpage magically 

- In reality... web servers do not respond with a complete webpage 
- Instead, the servers respond with instructions, with code, that the browser can understand and then display for us (so we can see the fully complete websites)
	- So the job of the browser is to essentially display or to render content for us, for humans, for human eyes
	- But really to just take code that comes from a server, or from some HTTP response, and "render it in some way" for us users / humans

# Example using `google.com`

- Here is another example using Google search engine, what will happen?:
	- Your browser will send that message "`google.com`" to your internet provider or your (the people you pay to to be able to access the internet)
	- The message for example then will be "I want to see `google.com`" 
	- The ISP will then relay that message to something called the "DNS server" (domain name system server)
	- Think of the DNS server as a "super phone book"

- The DNS server then will look up in its database to find the exact IP address of that website you are trying to access
	- every single computer that is connected to the internet has an IP address
	- so each computer can be located, and contacted, using their unique IP address 

- Once that DNS server finds the IP address, it will send it back to your browser through the ISP over the internet, back to your client computer 
- This is so, now with the IP address, you can make a direct request to that IP address

- And at that IP address, will be the website servers (because we were using `google.com`) 
- So they will be able to send you back all the files and data that you need and were looking for using their website


# Summary

- So, when your client uses a browser to make a request for a website, the requests are sent to the website server, and then the server sends back the appropriate answer with the Javascript, HTML, CSS files that your browser needs to use in order to actually build the requested website in your local browser
