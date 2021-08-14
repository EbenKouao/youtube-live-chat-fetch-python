import pytchat
#Documentation: https://pypi.org/project/pytchat/

#vdeo_id refers to the YouTube channel ID: 
# https://www.youtube.com/watch?v=5qap5aO4i9A, 
# e.g. video_id is 5qap5aO4i9A

# Modified: 20/08/21
# More Projects: https://smartbuilds.io

video_id = "5qap5aO4i9A"

def main():
    chat = pytchat.create(video_id)
    try:
        while chat.is_alive():
            for c in chat.get().sync_items():
                print(f"{c.datetime} [{c.author.name}]- {c.message}")
                
                if(c.type == "superChat"):
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