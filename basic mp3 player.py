from random import choice

class MP3Player():
    def __init__(self, songlist = []):
        self.currentSong = ""
        self.volume = 100
        self.songlist = songlist
        self.status = True

    def choose_song(self):
        if len(self.songlist)>1:
            counter = 1
            for song in self.songlist:
                print("{}){}".format(counter, song))
                counter += 1

            selected_song = int(input("Enter the number of the song you want to select: "))
            while selected_song < 1 or selected_song > len(self.songlist):
                selected_song = int(input("Please enter a correct number (1-{}): ".format(len(self.songlist))))

            self.currentSong = self.songlist[selected_song - 1]
        else:
            print("There is no song to choose.")

    def incr_volume(self):
        if self.volume == 100:
            pass
        else:
            self.volume += 10

    def decr_volume(self):
        if self.volume == 0:
            pass
        else:
            self.volume -= 10

    def chooseRandomSong(self):

        try:
            chooseRandomSong = choice(self.songlist)
            self.currentSong = chooseRandomSong
        except IndexError:
            print("The song list is empty.")

    def AddSong(self):
        artist = input("Enter artist/group: ")
        song = input("Enter song: ")

        self.songlist.append(artist + " - " + song)

    def DeleteSong(self):
        if len(self.songlist) >1:
            counter = 1
            for song in self.songlist:
                print("{}){}".format(counter, song))
                counter += 1

            songtobeDeleted = int(input("Enter the number of the song you want to delete: "))
            while songtobeDeleted < 1 or songtobeDeleted > len(self.songlist):
                songtobeDeleted = int(input("Please enter a correct number (1-{}): ".format(len(self.songlist))))
            self.songlist.pop(songtobeDeleted - 1)
        else:
            print("There is no song to be deleted.")

    def exit(self):
        self.status = False

    def menu(self):
        print("""
<<<Welcome to Emel Tugce's MP3 Player>>>

Song List: {}
Currently Playing Song: {}
Sound Level: {}

1)Choose Song
2)Increase Volume
3)Decrease Volume
4)Select Random Song
5)Add Song
6)Delete Song
7)Exit
""".format(self.songlist, self.currentSong, self.volume))

    def choice(self):
        choice = int(input("Enter your choice: "))

        while choice<1 or choice>7:
            sec = int(input("Please enter a value within the specified range (1-7): "))

        return choice

    def run(self):
        self.menu()
        choice = self.choice()

        if choice == 1:
            self.choose_song()
        if choice == 2:
            self.incr_volume()
        if choice == 3:
            self.decr_volume()
        if choice == 4:
            self.chooseRandomSong()
        if choice == 5:
            self.AddSong()
        if choice == 6:
            self.DeleteSong()
        if choice == 7:
            self.exit()

mp3player = MP3Player()
while mp3player.status:
    mp3player.run()
    print("The program has been ended.")


