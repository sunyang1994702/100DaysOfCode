from apiclient.discovery import build
import json


def get_api():
    with open('config.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        
    return json_data['APP_KEY']


def build_youtube(YOUTUBE_API_KEY):
    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    except Exception as e:
        print("ERROR MSG: {}".format(e))
        print("YOUTUBE BUILD FAILED!! CHECK YOUR API KEY!!")

    return youtube


def videos_youtube(my_youtube):
    ### get one specific channel's all of the video info
    nextpageToken = ""
    while True:
        videos_request = my_youtube.search().list(
            part="id,snippet",
            channelId="UC8raYDyn0Y_27MGDcHzpLkQ",
            type="video",
            order="date",
            maxResults=10,
            pageToken=nextpageToken
        ).execute()
        
        try:
            ## Once nextPageToken doesn't exsit in request result, it means the current page is a final. It will throw a keyerror exception.
            for each_video in videos_request['items']:
                print(each_video['id']['videoId'] + " ---> " + each_video['snippet']['title'])
            nextpageToken = videos_request['nextPageToken']

        except KeyError as e:
            print("This is all videos!!")
            break


if __name__ == '__main__':
    YOUTUBE_API_KEY = get_api()
    my_youtube = build_youtube(YOUTUBE_API_KEY)
    videos_youtube(my_youtube)

