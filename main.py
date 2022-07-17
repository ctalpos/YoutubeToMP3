from pytube import YouTube
import ffmpy
import os
import re



def download_youtube_to_mp4():
    """ This function downloads an MP4 file from each link that it provided in list_of_songs.txt
    """
    
    with open("list_of_songs.txt", mode="r") as file:

        linkuri_melodii = file.readlines()
        #print(lista_melodii)

        for link_melodie in linkuri_melodii:
            yt = YouTube(str(link_melodie))
            #print(link_melodie)


            # extract only audio
            video = yt.streams.filter(only_audio=True).first()

            # download the file
            out_file = video.download(output_path="Downloaded")      
            
            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp4'
            os.rename(out_file, new_file)

            

            # result of success
            print(yt.title + " has been successfully downloaded.")

download_youtube_to_mp4()




def convert_mp4_to_mp3():
    """This function identifies mp4 files and convert them into mp3 using FFmpeg.
    It also cleans the name format. The files shoud be in the same directory as the main.py
    """

    path_downloaded_folder = r"C:\Users\Cristian\Python Scripts\YoutubeMP3\Downloaded\\"
    path_converted_folder = r"C:\Users\Cristian\Python Scripts\YoutubeMP3\Converted\\"

    for input_file_mp4 in os.listdir(r"C:\Users\Cristian\Python Scripts\YoutubeMP3\Downloaded"):
        if input_file_mp4.endswith(".mp4"):

            regex_patern = r"\s?\[.*\]|\s?\(.*\)|\.mp4" # delete all between [], () and replace .mp4 with .mp3
            substitut = ""
            output_file_mp3 = re.sub(regex_patern, substitut, input_file_mp4)
            
            ff = ffmpy.FFmpeg(
                executable = r'C:\Users\Cristian\Python Scripts\YoutubeMP3\ffmpeg.exe',
                inputs = {path_downloaded_folder + f'{input_file_mp4}': None},
                outputs = {path_converted_folder + f'{output_file_mp3}.mp3': None}
                #https://stackoverflow.com/questions/60561571/ffmpy-ffexecutablenotfounderror-executable-ffmpeg-not-found
            )
            
            ff.run()
            print(f'{output_file_mp3} -> CONVERTED!')

convert_mp4_to_mp3()