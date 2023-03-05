# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests
from database.database import findbots
from database.testdbconnection import connect

#hostName = "0.0.0.0"
hostName = "localhost"
serverPort = 25566


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Purls' Bot status page</title></head>", "utf-8"))
        self.wfile.write(bytes("<h1>Bot statuses:</h1>", "utf-8"))
        if connect():
            self.wfile.write(bytes("<h2>Database Connection Verified</h2>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        try:
            for a in findbots():
                response = requests.get(a[1], timeout=10)
                if response.status_code == 200:
                    self.wfile.write(bytes(f"<p>{a[0]}: Online</p>", "utf-8"))
        except requests.exceptions.Timeout:
            self.wfile.write(bytes(f"<p>{a[0]}: Offline</p>", "utf-8"))
        except requests.exceptions.ConnectionError:
            self.wfile.write(bytes(f"<p>{a[0]}: Offline</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
