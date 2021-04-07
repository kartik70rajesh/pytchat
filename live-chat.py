import pytchat
import json

VIDEO_ID = "F183_mEw1qg"
MESSAGE_STRING = "😂😂😂"
BASE_URL = "https://www.youtube.com/watch?v="
BUFFER_SECS = 5
def create_url(split_time):
    if len(split_time) > 2 :
        #split_time[2]-=BUFFER_SECS
        return BASE_URL+VIDEO_ID+"&t="+split_time[0]+"h"+split_time[1]+"m"+split_time[2]+"s"
    else :
        return BASE_URL+VIDEO_ID+"&t="+split_time[0]+"m"+split_time[1]+"s"

chat = pytchat.create(video_id=VIDEO_ID)
chat_json=""
chats=[]
file = open("chat.txt", "w", encoding="utf-8")
print("--------------DOWNLOADING CHATS-------------")
while chat.is_alive():
    chat_json=chat.get().json()
    chats = json.loads(chat_json)
    for msg in chats:
        if MESSAGE_STRING in msg["message"]:
            timed_url = create_url(msg["elapsedTime"].split(":"))
            file.write(msg["elapsedTime"]+" "+msg["message"]+" "+timed_url+"\n")
print("--------------CHATS DOWNLOADED-------------")
file.close()
