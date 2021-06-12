import praw,requests,re

r = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
)
for post in r.subreddit('EarthPorn').top(limit=1):  #Here change EarthPorn to the subreddit you want and change limit to the pics you want.
    url = (post.url)
    file_name = url.split("/")
    if len(file_name) == 0:
        file_name = re.findall("/(.*?)", url)
    file_name = file_name[-1]
    if "." not in file_name:
        file_name += ".jpg"
    print(file_name)
r = requests.get(url)
with open(post,"wb") as f:
    f.write(r.content)