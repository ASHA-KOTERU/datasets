import pytube
from pytube import YouTube
import pandas as pd
columns=['a','b','c','d','e']
df = pd.read_csv("avspeech_train.csv",header=None)
df.columns=columns

yt_ids = list(df.a)
yt_st = list(df.b)
yt_et = list(df.c)
import os
import itertools
count=0
import pandas as pd
for i,st,et in itertools.izip(yt_ids,yt_st,yt_et):
    if count==3:
        break
    url = 'https://www.youtube.com/watch?v='+i
    os.system('youtube-dl -g '+url+' > b.csv')
    df=pd.read_csv('b.csv',header=None)
    video=df[0][0]
    audio=df[0][1]
    print video
    print audio
    dur=str(et-st)
    st=str(st)
    et=str(et)
    count=count+1

    os.system('ffmpeg -ss '+st+ ' -i "'+video+'" -ss '+st+' -i "'+audio+'" -map 0:v -map 1:a -ss '+st+' -t '+dur+' -c:v libx264 -strict experimental -c:a aac '+i+'.mp4')
    