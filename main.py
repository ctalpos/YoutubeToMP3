from pytube import YouTube
from pathlib import Path
import ffmpy
import os
import re




def download_youtube_to_mp4():
    """ This function downloads an MP4 file from each link that is provided in list_of_songs.txt
    """
    
    with open("list_of_songs.txt", mode="r") as file:

        list_of_url_songs = file.readlines()

        for url_song in list_of_url_songs:
            yt = YouTube(str(url_song))

            # extract audio in mp4 format from YouTube
            video = yt.streams.filter(only_audio=True).first()


            # download the file 
            downloaded_folder_path = Path.cwd() / "Downloaded"
            downloaded_folder_path.mkdir(exist_ok=True)  # ignore "FileExistsError" if the targhet directory exists
            out_file = video.download(output_path=downloaded_folder_path)    
            

            # save the file in Downloaded directory
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp4'
            os.rename(out_file, new_file)

            
            # result of success
            print(yt.title + " has been successfully downloaded.")

download_youtube_to_mp4()




def convert_mp4_to_mp3():
    """This function identifies each MP4 files that is in Donwloaded directory (folder) and convert into MP3 using FFmpeg (https://ffmpeg.org/download.html).
    The FFmpeg shoud be in the same directory as the main.py. Function also cleans the name format and save them in Converted directory (folder).
    """

    path_downloaded_folder = Path.cwd() / "Downloaded"
    path_downloaded_folder.mkdir(exist_ok=True)

    path_converted_folder = Path.cwd() / "Converted"
    path_converted_folder.mkdir(exist_ok=True)

    for input_file_mp4 in os.listdir(path_downloaded_folder):
        if input_file_mp4.endswith(".mp4"):

            regex_patern = r"\s?\[.*?\]|\s?\(.*?\)|\.mp4" # delete all between [], () and replace .mp4 with .mp3
            substitut = ""
            output_file_mp3 = re.sub(regex_patern, substitut, input_file_mp4)
            
            ff = ffmpy.FFmpeg(
                executable = Path.cwd() / "ffmpeg.exe", # make sure that ffmpeg.exe is in the same directory as the main.py
                inputs = {path_downloaded_folder / f'{input_file_mp4}': None},
                outputs = {path_converted_folder / f'{output_file_mp3}.mp3': None}
            )
            
            ff.run()
            print(f'{output_file_mp3} -> CONVERTED!')

convert_mp4_to_mp3()