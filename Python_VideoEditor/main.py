from main2 import renameFiles, mergeClips
from yt import * 
keyword = 'Random'
#finalVideoTitle = '51 Video Merge'
renameFiles(".",0,keyword)
mergeClips(keyword,finalVideoTitle)
