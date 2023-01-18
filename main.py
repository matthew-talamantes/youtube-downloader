from pytube import YouTube

def download(ytObject):
    try:
        ytObject.download(output_path='./vids/')
    except:
        print('An error has occured during download')
    print('done')

def downloadVidio(link):
    ytObject = YouTube(link)
    ytObject = ytObject.streams.get_highest_resolution()
    download(ytObject)
    

def downloadAudio(link):
    ytObject = YouTube(link)
    ytObject = ytObject.streams.get_audio_only()
    download(ytObject)


link = input('Insert youtube link: ')
downloadAudio(link)