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


def get_youtube_comment(my_youtube):
    ### get one specific video's all of review
    nextpageToken = ""
    while True:
        videos_request = my_youtube.commentThreads().list(
            part="id,snippet",
            videoId="mi3oiZMcU_w",
            order="time",
            maxResults=100,
            pageToken=nextpageToken
        ).execute()
        
        try:
            ## Once nextPageToken doesn't exsit in request result, it means the current page is a final. It will throw a keyerror exception.
            for each_video in videos_request['items']:
                print(each_video['snippet']['topLevelComment']['snippet']['authorDisplayName'] + " ---> " + each_video['snippet']['topLevelComment']['snippet']['textDisplay'])
            nextpageToken = videos_request['nextPageToken']

        except KeyError as e:
            print("This is all videos!!")
            break


def get_vedio_info(my_youtube):
    ### get one specific channel's subscribers_numbers
    videos_request = my_youtube.videos().list(
        part="id,snippet, statistics",
        id="mi3oiZMcU_w"
    ).execute()

    print("Video title : {}".format(videos_request['items'][0]["snippet"]["title"]))
    print("Video View : {}".format(videos_request['items'][0]["statistics"]["viewCount"]))
    print("Video Like : {}".format(videos_request['items'][0]["statistics"]["likeCount"]))
    print("Video Dislike : {}".format(videos_request['items'][0]["statistics"]["dislikeCount"]))


if __name__ == '__main__':
    YOUTUBE_API_KEY = get_api()
    my_youtube = build_youtube(YOUTUBE_API_KEY)
    get_youtube_comment(my_youtube)
    get_vedio_info(my_youtube)

