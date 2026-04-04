# # Create a list of favorite song.
# songs = ['song1', 'song2', 'song3', 'song4', 'song5']
# #print(len(songs))
# # Use for loop to print each song title along with its sr number in the list
# for i in range (len(songs)):
#     print(f"{i+1}. {songs[i]}")

secret_nmber = 7
user_input = int(input("Guess a Number"))
while user_input != 7:
    if user_input > 7:
        print("Too High")
    else:
        print("Too Low")
    user_input = int(input("Guess a Number"))
print("Congratulations, you guessed the number")