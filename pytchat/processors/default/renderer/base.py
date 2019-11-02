from datetime import datetime

class Author:
    pass
class BaseRenderer:
    def __init__(self, item, chattype):
        self.renderer = list(item.values())[0]
        self.chattype = chattype
        self.author = Author()

    def get_snippet(self):
        self.type = self.chattype
        self.id = self.renderer.get('id')
        timestampUsec = int(self.renderer.get("timestampUsec",0))
        self.timestamp = int(timestampUsec/1000)
        self.datetime = self.get_datetime(timestampUsec)
        self.message = self.get_message(self.renderer)
        self.id =  self.renderer.get('id')
        self.amountValue= 0.0
        self.amountString = ""
        self.currency= ""
        self.bgColor = 0

    def get_authordetails(self):
        self.author.badgeUrl = ""
        (self.author.isVerified, 
        self.author.isChatOwner, 
        self.author.isChatSponsor, 
        self.author.isChatModerator) = (
            self.get_badges(self.renderer)
        )
        self.author.channelId = self.renderer.get("authorExternalChannelId")
        self.author.channelUrl = "http://www.youtube.com/channel/"+self.author.channelId
        self.author.name      = self.renderer["authorName"]["simpleText"]
        self.author.imageUrl= self.renderer["authorPhoto"]["thumbnails"][1]["url"] 
        


    def get_message(self,renderer):
        message = ''
        if renderer.get("message"):
            runs=renderer["message"].get("runs")
            if runs:
                for r in runs:
                    if r:
                        if r.get('emoji'):
                            message += r['emoji'].get('shortcuts',[''])[0]
                        else:
                            message += r.get('text','')
        return message

    def get_badges(self,renderer):
        isVerified = False
        isChatOwner = False
        isChatSponsor = False
        isChatModerator = False
        badges=renderer.get("authorBadges")
        if badges:
            for badge in badges:
                author_type  = badge["liveChatAuthorBadgeRenderer"]["accessibility"]["accessibilityData"]["label"]
                if author_type == '確認済み':
                    isVerified = True
                if author_type == '所有者':
                    isChatOwner = True
                if 'メンバー' in author_type:
                    isChatSponsor = True
                    self.get_badgeurl(badge)
                if author_type == 'モデレーター':
                    isChatModerator = True
        return isVerified, isChatOwner, isChatSponsor, isChatModerator
    

    def get_badgeurl(self,badge):
        self.author.badgeUrl = badge["liveChatAuthorBadgeRenderer"]["customThumbnail"]["thumbnails"][0]["url"]



    def get_datetime(self,timestamp):
        dt = datetime.fromtimestamp(timestamp/1000000)
        return dt.strftime('%Y-%m-%d %H:%M:%S')