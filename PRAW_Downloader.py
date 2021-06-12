import praw,requests,re
# There are countless tutorials on getting the client id and secret.
r = praw.Reddit(
    client_id="", # place client_id here
    client_secret="", # place client_secret
    user_agent="", # Here describe the purpose of the script and your username. This is just good habit. 
)
for post in r.subreddit('EarthPorn').top(limit=1):  #Here change EarthPorn to the subreddit you want and change limit to the pics you want.
    url = (post.url) # Here it grabs the url of the top post on r/EarthPorn
    file_name = url.split("/") # Splits the URL based on the backslash character
    if len(file_name) == 0: # if the list is empty which is an error then:  
        file_name = re.findall("/(.*?)", url) # the new file_name is equal to a regular expression search of 
                                              # of the url for "/.jpg" or png or jpeg
    file_name = file_name[-1] # After checking for that error, the new value of file_name is the last value in the list
    if "." not in file_name: # if "." is not in the file_name value then append .jpg to it.
        file_name += ".jpg"
r = requests.get(url) # Get the image and assign it to r
with open(file_name,"wb") as f: # Open a file with the name of it being the value of file_name
                                # as a binary with write permissions.
    f.write(r.content) # write the content of the image as binary into the file