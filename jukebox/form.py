#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep, listdir
import cgi
from os.path import isfile, join
from subprocess import call

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        print("GET" + self.path)
        if self.path=="/":
            self.path="/index.html"

            try:
                #Check the file extension required and
                #set the right mime type

                sendReply = False
                if self.path.endswith(".html"):
                    mimetype='text/html'
                    sendReply = True
                if self.path.endswith(".jpg"):
                    mimetype='image/jpg'
                    sendReply = True
                if self.path.endswith(".gif"):
                    mimetype='image/gif'
                    sendReply = True
                if self.path.endswith(".js"):
                    mimetype='application/javascript'
                    sendReply = True
                if self.path.endswith(".css"):
                    mimetype='text/css'
                    sendReply = True

                if sendReply == True:
                    #Open the static file requested and send it
                    f = open(curdir + sep + self.path) 
                    self.send_response(200)
                    self.send_header('Content-type',mimetype)
                    self.end_headers()
                    self.wfile.write(f.read())
                    f.close()
                return

            except IOError:
                self.send_error(404,'File Not Found: %s' % self.path)

        elif self.path=="/Files":
            self.send_response(200)
            mypath="/media/Expansion Drive/Entertainment/Music/English/"
            mimetype='text/html'
            self.send_header('Content-type',mimetype)
            self.end_headers()
            #self.wfile.write('<br/>'.join([ f for f in listdir(mypath) if isfile(join(mypath,f)) ]))
            files=[ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
            self.wfile.write('<table>')
            for file in files:
                self.wfile.write('<tr><td>' + file + '</td></tr>')
            self.wfile.write('</table>')
            f.close()
            
            
    #Handler for the POST requests
    def do_POST(self):
        print("POST" + self.path)
        if self.path=="/send":
            form = cgi.FieldStorage(
                fp=self.rfile, 
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
            })

            print "Your name is: %s" % form["your_name"].value
            mypath="/media/Expansion Drive/Entertainment/Music/English/"
            onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
            self.send_response(200)
            self.end_headers()
            call(["mpg123",mypath+str(form["your_name"].value)])
            self.wfile.write("Thanks %s !" % form["your_name"].value)
            self.wfile.write(onlyfiles)
            return
        elif self.path=="/play":
            form = cgi.FieldStorage(
                fp=self.rfile, 
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
            })

            print "Your name is: %s" % form["playSel"][0].value
            print form["playSel"]
            self.send_response(200)
            self.end_headers()
            #self.wfile.write("Thanks %s !" % form["playSel"].value)
            self.wfile.write(form["playSel"])
            return          
            
            
try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER
    
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()

