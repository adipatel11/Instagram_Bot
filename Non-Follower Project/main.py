import instaloader
    

    
    
def main():
    # Get instance
    L = instaloader.Instaloader()

    # Optionally, login or load session
    L.login('burnerUsername', 'burnerPassword')

    searchee = 'username_of_profile_of_interest'

    profile = instaloader.Profile.from_username(L.context, searchee) # get user profile

    followers = set(profile.get_followers()) # get both followers and followees

    followees = set(profile.get_followees())

    intersection = followers.intersection(followees) # find the intersection and subtract from followees to find non-followers
    non_follow_backs = list(followees - intersection)

    createFile(non_follow_backs) # creates a file with all of the profiles listed in the same directory

        
def createFile(givenList):
    outputFile = open('Non_Followers_List.txt', 'w')

    for profile in givenList:
        outputFile.write(f'{profile}\n')

    outputFile.close()
        
        
        
main()
