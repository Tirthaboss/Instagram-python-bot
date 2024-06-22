from instabot import *
bot = Bot
username = input("Enter your username/mobile no/email id:")
password = input("Enter yor strong password:")
bot.login(username=username,password=password)
print("Try to login")
print("sussesfuly login")
searcher = input("Enter search terget username:")
bot.search_users(searcher)
print(searcher)
print("Count followers and make list")
followers = bot.get_user_followers(searcher)
print(followers)
print("Count following and make list")
following = bot.get_user_following(searcher)
print(following)

# Find users you are following who are not following you back
unfollow_list = [user_id for user_id in following if user_id not in followers]

# Unfollow users from the unfollow list
for user_id in unfollow_list:
   # bot.unfollow(user_id)
    print(f"Unfollowed user with ID: {user_id}")
# Print and save unfollow list to a text file
print(f"Unfollow list saved to unfollow_list.txt")
unfollow_list_username = bot.get_username_from_user_id(user_id)
with open('unfollow_list_username.txt', 'w') as file:
    for user_id in unfollow_list:
        file.write(f"{unfollow_list_username}\n")
        print(f"Unfollowed user with ID and USERNAME: {user_id},{unfollow_list_username}")
        # Uncomment the line below to actually unfollow users
        bot.unfollow(user_id)
      print(f"Unfollowed successfully {user_id}")
