Python Video Merger (Less than 1KB!)
A basic tool to bulk rename videos, merge them together into a final video, complete with audio.
Installation
Use the package manager pip to install moviepy.
pip install moviepy
Usage
This tool consists of 2 parts, a frontend(main.py) and a backend(backend.py).
The logic resides in the backend whilst the functions are called from main.py.
from main2 import renameFiles, mergeClips
keyword = 'Random' #Sets the file name for renaming.
finalVideoTitle = '51 Video Merge' #The title of the final merged video
renameFiles(".",0,keyword) #Renames files in the home folder, incrementing by 0.
mergeClips(keyword,finalVideoTitle) #Merges all the clips together and sets the title.
Contributing
Pull requests are more than welcome, thanks!