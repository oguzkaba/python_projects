
from instabot import Bot
import os

try:
    os.remove("config/lindanikah_uuid_and_cookie.json")
except:
    pass    

bot = Bot()
bot.login(username="lindanikah", password="pass")

######  upload a picture #######
# bot.upload_photo(
#     "D:/indir.jpg", caption="Test test test.\n--------------------\n#hashtag #test")

# ######  follow someone #######
#bot.follow("instagramforbusiness")

# ######  send a message #######
# bot.send_message("Hello from Dhaval", ['user1','user2'])

#####  get follower info #######
# my_followers = bot.get_user_followers("lindanikah")
# i=1
# for follower in my_followers:
#     friends=open("config/friends.txt","a")
#     friends.write(str(i)+"->"+bot.get_username_from_user_id(follower)+"\n")
#     print(str(i)+"->"+bot.get_username_from_user_id(follower))
#     i+=1

####  get follow info #######
my_follow = bot.get_user_following("lindanikah")
i=1
for follower in my_follow:
    friends=open("config/followed.txt","a")
    friends.write(str(i)+"->"+bot.get_username_from_user_id(follower)+"\n")
    print(str(i)+"->"+bot.get_username_from_user_id(follower))
    i+=1



# bot.unfollow_everyone()
