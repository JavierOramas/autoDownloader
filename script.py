import requests
import urllib
from os import popen,path,makedirs
import time
from pytube import YouTube
import pytube

urls = []

def download(f):
    makedirs('download', exist_ok=True)
    if not 'https://www.youtube.com' in f:
        urllib.request.urlretrieve(f, path.join('download',f.split('/')[-1]))
    
    else:
        video = YouTube(f)
        video = video.streams.filter(res='720p')
        
        video.download('download')
        
        if not video.captions.get_by_language_code('es') == None:
            with open(video.title+'.srt', 'w') as capt:
                caption = video.captions.get_by_language_code('es')
                for i in caption.generate_srt_captions():
                    capt.write(i)
                    
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
          if  not i in urls: 
              urls.append(i)
           
    f.close()
    

get_files()

while(len(urls) > 0):
    time.sleep(1)
    get_files()



