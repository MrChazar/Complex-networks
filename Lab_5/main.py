import googleapiclient.discovery
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "not_your_business"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)


def getcomments(video):
    request = youtube.commentThreads().list(
      part="snippet",
      videoId=video,
      maxResults=100
    )

    comments = []

    # Execute the request.
    response = request.execute()

    # Get the comments from the response.
    for item in response['items']:
      comment = item['snippet']['topLevelComment']['snippet']
      public = item['snippet']['isPublic']
      comments.append([
          comment['authorDisplayName'],
          comment['publishedAt'],
          comment['likeCount'],
          comment['textOriginal'],
          comment['videoId'],
          public
      ])

    while True:
        try:
            nextPageToken = response['nextPageToken']
        except KeyError:
            break
        nextPageToken = response['nextPageToken']
        # Create a new request object with the next page token.
        nextRequest = youtube.commentThreads().list(part="snippet", videoId=video, maxResults=100, pageToken=nextPageToken)
        # Execute the next request.
        response = nextRequest.execute()
        # Get the comments from the next response.
        for item in response['items']:
          comment = item['snippet']['topLevelComment']['snippet']
          public = item['snippet']['isPublic']
          comments.append([
              comment['authorDisplayName'],
              comment['publishedAt'],
              comment['likeCount'],
              comment['textOriginal'],
              comment['videoId'],
              public
          ])

    df2 = comments
    return df2


def sentiment_analysis(comments, game):
    sia = SentimentIntensityAnalyzer()
    sentiments = {'neg': 0, 'neu': 0, 'pos': 0}
    for comment in comments['text']:
        temp = sia.polarity_scores(comment)
        print(temp)
        if temp['neg'] > temp['neu'] and temp['neg'] > temp['pos']:
            sentiments['neg'] += 1
        if temp['pos'] > temp['neu'] and temp['pos'] > temp['neg']:
            sentiments['pos'] += 1

    plt.bar(sentiments.keys(), sentiments.values())
    plt.title(f"{game}")
