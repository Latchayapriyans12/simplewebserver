from http.server import HTTPServer, BaseHTTPRequestHandler

content ='''
<!DOCTYPE html>
    <head>
        <center>
        <TITLE> TYPES OF PROTOCOLS</TITLE></center>
    </head>
    <body>
        <center><table border="6" bgcolor="white" WIDTH="600PX" HEIGHT="400PX"></center>
        <caption> <h1>LIST OF PROTOCALS IN TCP/IP PROTOCOL SUITE</h1></caption>
        <br></br>
        5
            <tr bgcolor="pink">
                <th>S.no</th> <th>Name of the Layer</th> <th>Name of the Protocols</th>
            </tr>
            <tr>
                <td>1.</td> <td>Application layer</td> <td>HTTP, FTP, DNS</td>
            </tr>
            <tr>
                <td>2.</td> <td>Transport layer</td> <td>TCP, UDP</td>
            </tr>
            <tr>
                <td>3.</td> <td>Internet layer</td> <td>IPV4/IPV6</td>
            </tr>
            <tr>
                <td>4.</td> <td>Network access layer</td> <td>MAC, Ethernet</td>
            </tr>
        </table>
    </body>
</html>
'''



class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
