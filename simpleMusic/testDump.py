import simpleMusicLib as sml

myPlayer = sml.player()

myPiece = sml.piece()
myPiece.setRhythm("4/4")
myPiece.setTiming(1)

myBar = sml.bar()
myVoice = sml.voice()
myVoice.setName("Voice A")

aTune = sml.tune("1/4", "contra", "a")
myBar.appendTune(aTune)

aTune = sml.tune("1/4", "contra", "c")
myBar.appendTune(aTune)

aTune = sml.tune("1/4", "contra", "a")
myBar.appendTune(aTune)

aTune = sml.tune("1/4", "contra", "c")
myBar.appendTune(aTune)

myVoice.appendBar(myBar)
myVoice.appendBar(myBar)
myPiece.appendVoice(myVoice)


myPlayer.dump(myPiece)
