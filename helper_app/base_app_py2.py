#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
inspired by s2a_fm

"""

from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from string import split

import os, sys

import urllib


class GetHandler(BaseHTTPRequestHandler):
    """
    This class contains the HTTP server that Scratch2 communicates with
    Scratch sends HTTP GET requests and this class processes the requests.

    HTTP GET requests are accepted and the appropriate command handler is
    called to process the command.
    """
    #class variable for consistent use    
    
  


  
    def do_GET(self):
        """
        Scratch2 only sends HTTP GET commands. This method processes them.
        It differentiates between a "normal" command request and a request
        to send policy information to keep Flash happy on Scratch.
        (This may change when Scratch is converted to HTML 5
        """

        # skip over the / in the command
        cmd = self.path[1:]

        # create a list containing the command and all of its parameters
        cmd_list = split(cmd, '/')
        
        s = "okay"

        #handle string s , and cal send_resp

        #print command text
        if not cmd.startswith("poll"): print "[query]: " + self.path

 

            
        if  cmd.startswith("poll"):
             pass

        self.send_resp(s)


    def send_resp(self, response):
        """
        This method sends Scratch an HTTP response to an HTTP GET command.
        """

        crlf = "\r\n"
        http_response = "HTTP/1.1 200 OK" + crlf
        http_response += "Content-Type: text/html; charset=ISO-8859-1" + crlf
        http_response += "Content-Length" + str(len(response)) + crlf
        http_response += "Access-Control-Allow-Origin: *" + crlf
        http_response += crlf
        #add the response to the nonsense above
        if response != 'okay':
            http_response += str(response + crlf)
        # send it out the door to Scratch
        self.wfile.write(http_response)
        

def start_server():
    """
       This function populates class variables with essential data and
       instantiates the HTTP Server
    """
    port = 50333

    try:
        server = HTTPServer(('localhost', port), GetHandler)
        print 'Starting Scratch HTTP Server!(port ' + str(port) + ')'
        print 'Use <Ctrl-C> to exit the extension\n'
        print 'Please start Scratch !'
    except Exception:
        print 'HTTP Socket may already be in use - restart Scratch'
        raise

    try:
        #start the server
        server.serve_forever()
    except Exception:
        raise
        
if __name__ == "__main__":

        start_server()
