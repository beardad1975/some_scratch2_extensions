#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:45:49 2013

@author: Alan Yorinks
Copyright (c) 2013-14 Alan Yorinks All right reserved.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import logging
from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from string import split

import os, sys, thread, time

from math import floor,degrees

import urllib, random





class GetHandler(BaseHTTPRequestHandler):
    """
    This class contains the HTTP server that Scratch2 communicates with
    Scratch sends HTTP GET requests and this class processes the requests.

    HTTP GET requests are accepted and the appropriate command handler is
    called to process the command.
    """

    counter = 0
    counter_paused = 0
    counter_waiting = False
    wait_target = 0
    wait_id = ""

    # tcp server port - must match that in the .s2e descriptor file
    #port = 50333
    end_of_line = "\r\n"


    #noinspection PyPep8Naming
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
        #leo
        if not GetHandler.counter_paused:
            GetHandler.counter += 1

        #print cmd + " |counter: " + str(GetHandler.counter)

        if not cmd.startswith("poll"): print "[query]: " + self.path

        if cmd.startswith("playBeep"): print " Beep! Beep! "

        if cmd.startswith("sendText"):
            print cmd_list[1] + "  " + urllib.unquote(cmd_list[1])

        if cmd.startswith("sendTwo"):
            print cmd_list[1] + "  " + urllib.unquote(cmd_list[2])

        if cmd.startswith("resetCounter"):
            GetHandler.counter = 0

        if cmd.startswith("resumeCounter"):
            GetHandler.counter_paused = 0 

        if cmd.startswith("pauseCounter"):
            GetHandler.counter_paused = 1

        if cmd.startswith("waiting"):
            time.sleep(float(cmd_list[2]))

        if cmd.startswith("waitCounter"):
            GetHandler.counter_waiting = True
            GetHandler.wait_id = cmd_list[1]
            GetHandler.wait_target = int(cmd_list[2])
            print "wait_id " + cmd_list[1] + "   wait_target " + cmd_list[2]
        
        if cmd.startswith("reset_all"):
            GetHandler.counter = 0

        """
        if  cmd.startswith("poll"):
            #leap_data.update()
            #s = leap_data.resultString()
            #print "counter: " , GetHandler.counter
            s = "volume " + str(GetHandler.counter) + "\n"
            s = s + "willYou " + ( "true" if GetHandler.counter_paused else "false")     + "\n"
            s = s + urllib.quote("name/父") + " " + urllib.quote("張文宏") + "\n"
            s = s + urllib.quote("name/母") + " " + urllib.quote("楊惠甄") + "\n"
            s = s + urllib.quote("name/子") + " " + urllib.quote("張晨熙") + "\n"
            s = s + urllib.quote("food/漢堡") + " true" + "\n"
            s = s + urllib.quote("food/炸雞") + " false" + "\n"
        """
        if  cmd.startswith("poll"):
            s = "_problem some thing wrong!!!!"


            if GetHandler.counter_waiting :
                if GetHandler.counter < GetHandler.wait_target:
                    #remain wait
                    s = s + "_busy " + GetHandler.wait_id + "\n"
                    print "[wait report] " + s
                else:
                    # waiting time up
                    print "waiting time up"
                    GetHandler.counter_waiting = False
            
            #print "[report] " + s
          
            
        """
        elif cmd.startswith("crossdomain"):
            s = "<cross-domain-policy>\n"
            s += "  <allow-access-from domain=\"*\" to-ports=\""
            s += str(self.port)
            s += "\"/>\n"
            s += "</cross-domain-policy>\n\0"
        """
        
        self.send_resp(s)

    # we can't use the standard send_response since we don't conform to its
    # standards, so we craft our own response handler here
    def send_resp(self, response):
        """
        This method sends Scratch an HTTP response to an HTTP GET command.
        """

        crlf = "\r\n"
        # http_response = str(response + crlf)
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


    try:
        server = HTTPServer(('localhost', 50333), GetHandler)
        print 'Starting Scratch Leap HTTP Server!'
        print 'Use <Ctrl-C> to exit the extension\n'
        print 'Please start Scratch !'
    except Exception:
        logging.debug('Exception in scratch_http_server.py: HTTP Socket may already be in use - restart Scratch')
        print 'HTTP Socket may already be in use - restart Scratch'
        raise
    try:
        #start the server
        server.serve_forever()
    except KeyboardInterrupt:

        print "Goodbye !"
        raise KeyboardInterrupt
    except Exception:

        raise
        
if __name__ == "__main__":

        start_server()
