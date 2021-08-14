#Documentation: https://pypi.org/project/pytchat/

#vdeo_id refers to the YouTube channel ID: 
# https://www.youtube.com/watch?v=5qap5aO4i9A, 
# e.g. video_id is 5qap5aO4i9A

# Modified: 20/08/21
# More Projects: https://smartbuilds.io

import pytchat
import json
from emoji import demojize


video_id = "5qap5aO4i9A"

def main():
    chat = pytchat.create(video_id)
    try:
        while chat.is_alive():
            for c in chat.get().sync_items():
                livechat_obj = c.json()
                live_chat = json.loads(livechat_obj)
                
                print(live_chat['datetime'] + " : " + live_chat['author']['name'] + " : " + live_chat['message'])
                #print(live_chat)

                #convert emojis from into string
                print(demojize(live_chat['datetime'] + " : " + live_chat['author']['name'] + " : " + live_chat['message']))

                #get a super chat and do something!
                if(live_chat['type'] == "superChat"):
                    print("Thanks for the Super chat")
    except Exception as e:
        # TODO: Parse error logs
        print(e)
        print(f"Exception occured with the payload: {c.message}")
        exit()

if __name__ == "__main__":
    print("********Started YouTube Server********")
    print("======================================")
    main()

# How it Works
# Get's the client ID: client .get https://github.com/taizan-hokuto/pytchat/blob/master/pytchat/util/__init__.py