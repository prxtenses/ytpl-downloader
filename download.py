from pytube import YouTube
from pytube import Playlist
from rich import print
from math import ceil
import sys
import threading
import os

try:
    dir = str(input("Coloque o nome da pasta: "))
    os.mkdir(dir)
except:
    pass

try:
    p = Playlist(input("Coloque o link da playlist: "))
except:
    pass

print("\n[deep_sky_blue1]:round_pushpin: Nome da playlist:[/deep_sky_blue1] [bright_white]{}[/bright_white]\n[deep_sky_blue1]:round_pushpin: Dono da playlist:[/deep_sky_blue1] [bright_white]{}[/bright_white]\n[deep_sky_blue1]:round_pushpin: Total de videos:[/deep_sky_blue1] [bright_white]{}[/bright_white]\n".format(p.title, p.owner, p.length))

links = []
size = 0

try:
    for url in p.video_urls:
        links.append(url)
except:
    print(':x: Link da playlist não é valido.')
    sys.exit(0)

size = ceil(len(links)/4)

def split_link(links,size):
    for i in range(0,len(links),size):
        yield links[i:i+size]

link = list(split_link(links,size))

print(":zap: Download iniciado... | [deep_sky_blue1]{}[/deep_sky_blue1]\n".format(dir))

def downloader1():
    for i in link[0]:
      yt = YouTube(i)
      ys = yt.streams.get_highest_resolution()
      filename = ys.download(dir)
      print("[1] | " + filename.split('/')[-1] + ' | Baixado')

def downloader2():
    for i in link[1]:
      yt = YouTube(i)
      ys = yt.streams.get_highest_resolution()
      filename = ys.download(dir)
      print("[2] | " + filename.split('/')[-1] + ' | Baixado')

def downloader3():
    for i in link[2]:
      yt = YouTube(i)
      ys = yt.streams.get_highest_resolution()
      filename = ys.download(dir)
      print("[3] | " + filename.split('/')[-1] + ' | Baixado')

def downloader4():
    for i in link[3]:
      yt = YouTube(i)
      ys = yt.streams.get_highest_resolution()
      filename = ys.download(dir)
      print("[4] | " + filename.split('/')[-1] + ' | Baixado')

t1 = threading.\
    Thread(target=downloader1, name='d1')
t2 = threading.\
    Thread(target=downloader2,name='d2')
t3 = threading.\
    Thread(target=downloader3, name='d3')
t4 = threading.\
    Thread(target=downloader4,name='d4')

t1.start()
t2.start()
t3.start()
t4.start()