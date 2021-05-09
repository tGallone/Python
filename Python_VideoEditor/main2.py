import os
from moviepy import * 
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip#, VideoFileClip, concatenate_videoclips
from moviepy.editor import VideoFileClip, concatenate_videoclips

def renameFiles(path, inc, name):
    files = os.listdir(path)
    for file in files:
        #if file.startswith("TikTok"):
        if file.endswith(".mp4"):
            inc+=1
            os.rename(os.path.join(path,file), os.path.join(path, f"{name}" + str(inc) + '.mp4'))
        
def mergeClips(startsWith,finalVideoTitle):
    clips = []
    for filename in os.listdir('.'):
        if filename.endswith(".mp4"):
            clips.append(VideoFileClip(filename))
    video = concatenate_videoclips(clips, method='compose')
    video.write_videofile(f"{finalVideoTitle}.mp4")
      