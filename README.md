# YouTube Scrapper
------------------
### A batch pre-processor to scrap and download trailers along with info from *YouTube*, process the videos to specific *Resolution*, *Frame Rate* and *Frame Count* and finally compress the videos and their like-dislike ratio into *hdf5* format.
------------------
### Do not misuse and download YouTube videos against their policy. This application is strictly for educational purpose.
------------------
## Required Libraries

>1. pafy
>2. bs4 *(optional for now)*
>3. requests *(generally comes preinstalled)*
>4. re *(generally comes preinstalled)*
>5. youtube_dl
>6. numpy
>7. cv2
>8. sk-video
>9. h5py *(generally comes preinstalled)*

**Install using *pip* or *conda*.**

------------------
## Default Directories

All information, by default are saved as:
> *python/out/data.json*

All the downloaded videos, by default are saved under:
> *python/out/videos/*

All processed videos, by default are saved under:
> *python/out/processedvideos/*

All compressed data, by default are saved under:
> *python/out/compresseddata/*

**Make the directories beforehand if you are working with default settings and clean the directories before each run manually. Run and work with only */python/batchdriver.py* which includes all the settings in the beginning of the file. Alternatively you can write your own driver. The APIs are *vidcomp*, *vidproc* and *yscrappper*.**