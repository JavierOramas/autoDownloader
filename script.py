import requests
import urllib
from os import popen,path,makedirs
import time

urls = []

def download(f):
    makedirs('download', exist_ok=True)
    urllib.request.urlretrieve(f, path.join('download',f.split('/')[-1]))

def get_list(f,list_done):
    output = []
    for i in f.readlines():
        if not i in list_done:
            output.append(i)
    return  output

def get_files():
    f = open('list.txt')
    list_done_read = [i for i in open('list_done.txt', 'r').readlines()]
    _list = get_list(f,list_done_read)
    for i in _list:
        try:
            download(i)
            with open('list_done.txt', 'a') as lista:
                lista.write(i)
                lista.close()
        except:
            urls.append(i)
    f.close()
    
get_files()
while(len(urls) > 0):
    time.sleep(1000)
    get_files()
