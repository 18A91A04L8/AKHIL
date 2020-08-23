import fbchat
from getpass import getpass
username = str(input("username: "))
client = fbchat.Client(username,getpass())
no_of_friends = int(input("Number of friends:"))
for i in range(no_of_friends):
    name =str(input("Name:"))
    friends = client.getusers(name)
    msg = str(input("Message:"))
    sent = client.send(friend.uid,msg)
    if sent:
        print("Message sent successfully!")
