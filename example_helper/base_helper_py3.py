#! /usr/bin/env python3
"""
Inspired and Modified from s2a_fm(THanks a lot, Sir Alan Yorinks)

Created on Sat Aug  15 11:50:15 2015

@author: Wen-Hung , Chang
Copyright (c) 2015 Wen-Hung, Chang All right reserved.

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

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

import os, sys, urllib

######  全域變數建議區  #####
####################################################

HELPER_NAME = "基本的Helper"
HELPER_PORT = 50000


####################################################

class CmdHandler(BaseHTTPRequestHandler):
    """
    This class handles HTTP GET requests sent from  Scratch2.

    """
  
    def do_GET(self):
        """
        process HTTP GET requests

        """

        # skip over the first / . example:  /poll -> poll  
        cmd = self.path[1:]

        # create a command list .  
        cmd_list = cmd.split('/')
        
        s = "不回傳資料"

        ###### 處理Scratch送出的命令
        ###### 若需回應Scratch的Poll命令，再把文字存在變數s ##
        ##############################################################
            
        if cmd_list[0] == "hello" :
            print ("Hello World!")

        if cmd_list[0] != "poll" : print (self.path)

            
        
        #############################################################
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

        if response != '不回傳資料':
            http_response += str(response + crlf)
            # send it out the door to Scratch

        self.wfile.write(http_response.encode('utf-8'))
        

def start_server():
    """
       This function populates class variables with essential data and
       instantiates the HTTP Server
    """
    

    try:
        server = HTTPServer(('localhost', HELPER_PORT ), CmdHandler)
        print ('啟動<' + HELPER_NAME + '>伺服程式!(port ' + str(HELPER_PORT) + ')')
        print ('要退出請按 <Ctrl-C> \n')
        print ('請執行Scrath2(記得要開啟對應的s2e檔案!)')
    except Exception:
        print ('HTTP Socket may already be in use - restart Scratch')
        raise

    try:
        #start the server
        server.serve_forever()
    except KeyboardInterrupt:
        print ('\n\n退出程式……\n')
        sys.exit()
        
if __name__ == "__main__":

        start_server()
