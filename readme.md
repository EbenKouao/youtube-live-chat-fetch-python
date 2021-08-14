# Youtube Live Chat Fetch - Python Application

## This repo creates a basic python application that would fetch a stream of youtube live chats.

The purpose of the YouTube Live Stream Fetch Python application would be used to listen to input commands to control droiid. (The 6 wheeled package Delviery Robot).

However, the use cases can be expanded to work for your project. Here's a basic application example.

[Credits PytChat GitHub Repo:](https://github.com/taizan-hokuto/pytchat)

Create a virtual environment: `python3 -m venv env`
Activate virtual environment: `source env/bin/activate`
Install requirements: `pip install -r requirements.txt`

To fetch Youtube live stream chats, we’re using the Pytchat library: pip install pytchat.

The base template example:

``` python
import pytchat
chat = pytchat.create(video_id="5qap5aO4c9A")
while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"{c.datetime} [{c.author.name}]- {c.message}")
```

## How it Works:
This library takes your video ID and fetches data based (via http request). 

The selected video ID  can be within the Youtube - URL:
URL: https://www.youtube.com/watch?v={videoID} e.g. https://www.youtube.com/watch?v=5qap5aO4i9A

**Note:** The above example/ repo only works with YouTube live streams.
The Pytchat library provides attributes of author objects, which be used to fetch super chats, Supersuckers etc.
