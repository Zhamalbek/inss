import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Load the profile from a username
username = 'likelook.by'
profile = instaloader.Profile.from_username(L.context, username)

# Loop through the posts and get the captions
for post in profile.get_posts():
    print(post.caption)
