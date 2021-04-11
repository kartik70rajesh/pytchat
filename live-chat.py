import pytchat
import json
from datetime import datetime, timedelta
from halo import Halo


# past live - ZmYDoMeWnu4
# live - Se3hl0YlFNs
VIDEO_ID = "zWqedWZXidM"
MESSAGE_STRING = "😂😂😂"
BASE_URL = "https://www.youtube.com/watch?v="
BUFFER_SECS = 5


def create_url(split_time):
    while len(split_time) < 3:
        split_time.insert(0, 0)
    h, m, s = map(int, split_time)
    dt = datetime(2021, 1, 1, h, m, s)
    if h > 0 or m > 0 or s >= 20:
        dt = dt-timedelta(seconds=20)
    return BASE_URL+VIDEO_ID+"&t="+str(dt.hour)+"h"+str(dt.minute)+"m"+str(dt.second)+"s"


chat = pytchat.create(video_id=VIDEO_ID)
all_chats_json = '{"chats":['
live_file = open("chat.txt", "w", encoding="utf-8")

spinner = Halo(text='Downloading chats', spinner='dots')
spinner.start()
while chat.is_alive():
    for c in chat.get().items:
        chat_details = json.loads(c.json())
        if MESSAGE_STRING in chat_details["message"]:
            # timed_url = create_url(msg["elapsedTime"].split(":"))
            all_chats_json += c.json()+','
            live_file.write('%s %s %s\n' % (
                chat_details["datetime"], chat_details["message"], chat_details["elapsedTime"]))
            live_file.flush()
spinner.stop()

final_json = open("chat.json", "w", encoding="utf-8")
all_chats_json = all_chats_json[:-1]+"]}"
final_json.write(all_chats_json)

live_file.close()
final_json.close()
