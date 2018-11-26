#!/usr/bin/env python
import os
# import SimpleHTTPServer
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer


class DemoHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write( "%s at %d\n" % (env['MESSAGE'], int(env['PORT'])))
		return


env = os.environ.copy()
if "MESSAGE" in env and "PORT" in env:
    try:
        port = int(env['PORT'])
        httpd = SocketServer.TCPServer(("", port), DemoHandler)
        httpd.serve_forever()
    except ValueError:
        raise Exception("usage: MESSAGE=SomeMessage PORT=NNNN %s" % (__file__))
else:
    raise Exception("usage: MESSAGE=SomeMessage PORT=NNNN %s" % (__file__))
