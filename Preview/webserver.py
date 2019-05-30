"""
Реализация веб-сервера на языке Python, способная запускать серверные
CGI-сценарии на языке Python; обслуживает файлы и сценарии в текущем
рабочем каталоге; сценарии на языке Python должны находиться в каталоге
webdir\cgi-bin или webdir\htbin;
"""
import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.' # расположение файлов html и п/каталога cgi-bin
port = 80

os.chdir(webdir)
srvraddr=("",port) # имя хоста и номер порта
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever() #старт бесконечного фонового процесса