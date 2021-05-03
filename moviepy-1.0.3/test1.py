#import threading
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
videoFileName = 'Impractical_jokers_SXX_EXX'
video = VideoFileClip(f"{videoFileName}.mp4")
timeStamps=[(5,35),(120,240),(111,155)]

for start,end in timeStamps:
    print(ffmpeg_extract_subclip(f"{videoFileName}.mp4", start, end, targetname=(f"{videoFileName}_{start}_{end}.mp4")))
    
