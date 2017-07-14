#from database/database.py import Database


#for all song files:
	#add to database
import os
rootDir = "music"
fileSet = set()

for dir_, _, files in os.walk(rootDir):
    for fileName in files:
        relDir = os.path.relpath(dir_, rootDir)
        relFile = os.path.join(relDir, fileName)
        fileSet.add(relFile)

database = Database()
for path in fileSet:
	#Audio.read_audio_file(path)
	database.add_songs(path)

#get mic input
mic_input = Audio.read_mic(seconds=5)
#Convert to spectrogram and find peaks
differences = DFT.get_features(mic_input)



#Look for matches
match = DFT.best_match(differences)
	#Output best match TODO: format data better
print(database.get_song(match))