from apiclient.discovery import build
import json


def get_api():
    with open('config.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        
    return json_data['APP_KEY']


def build_youtube(YOUTUBE_API_KEY):

    youtube = ''

    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    except Exception as e:
        print("ERROR MSG: {}".format(e))
        print("YOUTUBE BUILD FAILED!! CHECK YOUR API KEY!!")

    return youtube


def search_youtube(my_youtube):
    if my_youtube:
        search_response = my_youtube.search().list(
            q="Python",
            part="snippet",
            type="video",
            videoCategoryId="27",
            publishedBefore="2021-02-28T00:00:00Z",
            publishedAfter="2020-02-28T00:00:00Z"
        ).execute()

        # search_response.keys() : ['kind', 'etag', 'nextPageToken', 'regionCode', 'pageInfo', 'items']
        print(search_response["items"])

    else:
        print("CHEKC YOUTUBE BUILDING!!")


def channel_youtube(my_youtube):
    ### one specific channel's infomation.
    if my_youtube:
        channel_response = my_youtube.channels().list(
            part = 'snippet, statistics',
            id = "UC8raYDyn0Y_27MGDcHzpLkQ"
        ).execute()
        print(json.dumps(channel_response, indent=2, ensure_ascii=False))

    else:
        print("CHEKC YOUTUBE BUILDING!!")


def videos_youtube(my_youtube):
    ### get one specific channel's all of the video info
    if my_youtube:
        videos_request = my_youtube.search().list(
            part="id,snippet",
            channelId="UC8raYDyn0Y_27MGDcHzpLkQ",
            type="video",
            order="date",
            maxResults=50
        ).execute()

        #print(videos_request['nextPageToken'])
        #print(json.dumps(videos_response, indent=2, ensure_ascii=False))

        print(videos_request['items'][0]['id']['videoId'] + " ---> " + videos_request['items'][0]['snippet']['title'])
            

    else:
        print("CHEKC YOUTUBE BUILDING!!")


def video_youtube(my_youtube):
    ### get one video's completed info.
    if my_youtube:
        pass
    else:
        print("CHEKC YOUTUBE BUILDING!!")



if __name__ == '__main__':
    YOUTUBE_API_KEY = get_api()
    my_youtube = build_youtube(YOUTUBE_API_KEY)
    #search_youtube(my_youtube)
    videos_youtube(my_youtube)
