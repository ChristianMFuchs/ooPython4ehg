import simpleMusicLib as sml
#
#
fstTune = sml.tune()
print(fstTune.getRelativeLength()," ", fstTune.getOctave(), " ", fstTune.getName())
#
sndTune = sml.tune("1/3", "contra", "c")
print(sndTune.getRelativeLength()," ", sndTune.getOctave(), " ", sndTune.getName())
#
trdTune = sml.tune("1", "badcontra")
print(trdTune.getRelativeLength()," ", trdTune.getOctave(), " ", trdTune.getName())