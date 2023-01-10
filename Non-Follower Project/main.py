import instaloader

# Get instance
L = instaloader.Instaloader()

# Optionally, login or load session
L.login('jdonne233', 'hello'*3)

searchee = 'johndavidhagood'

profile = instaloader.Profile.from_username(L.context, searchee)

followers = set(profile.get_followers())

followees = set(profile.get_followees())

intersection = followers.intersection(followees)
non_follow_backs = list(followees - intersection)

for profile in non_follow_backs:
    print(profile)