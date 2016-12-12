import os
import pydub
from pydub import AudioSegment as audio

song = audio.from_wav('/home/cc/dir/track00.wav')
#chunks = pydub.silence.split_on_silence(song)
#for i, chunk in enumerate(chunks):
#    chunk.export("/home/cc/dir/chunk{0}.wav".format(i), format="wav")
a = pydub.effects.strip_silence(song, silence_len=50, padding=10)
print(song.duration_seconds, a.duration_seconds)
a.export('/home/cc/dir/test.wav','wav')
