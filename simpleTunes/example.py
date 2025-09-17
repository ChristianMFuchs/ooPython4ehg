import numpy as np
import simpleaudio as sa
#
# calculate note frequencies
A_freq = 440
Csh_freq = A_freq * 2 ** (4 / 12)
E_freq = A_freq * 2 ** (7 / 12)

# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100
T = 0.25
# t = np.linspace(0, T, T * sample_rate, False)
t = np.linspace(0, T, round((T * sample_rate)))

# generate sine wave notes
A_note = np.sin(A_freq * t * 2 * np.pi)
Csh_note = 0.5*np.sin(Csh_freq * t * 2 * np.pi)
E_note= 0.5*np.sin(E_freq * t * 2 * np.pi)
Total_note = A_note + Csh_note

# concatenate notes
audio = np.hstack((A_note,  Csh_note, E_note, Total_note))
# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

# wait for playback to finish before exiting
play_obj.wait_done()