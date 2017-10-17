var HTTP = require("http"); //Protocol

HTTP.createServer(function(request, response) {
        var body = "";
        function respond(status) {
                response.writeHead(status, { "Content-Type": "text/plain" });
                response.end(body);
                respond = null;
        }
        
        console.log("Client IP is: " + request.connection.remoteAddress); //Client IP from req
        console.log("Request URL: " + request.url); //URL from req 
        // Directing the flow
	if (request.url === "/url_1") {
                console.log("URL 1");
        } else if (request.url === "/url_2") {
                console.log("URL 2");
        } else {
                respond(404); //error handling
        }
}).listen(8080); //listening port 
