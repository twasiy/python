import pyaudio
import wave
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
p = pyaudio.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate= RATE,
    frames_per_buffer=FRAMES_PER_BUFFER,
    input = True
)

second = 5
frames = []
print('start recording...')
for i in range(0,RATE//FRAMES_PER_BUFFER*second):
    data = stream . read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open('output.wav','wb')
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b''. join(frames))
obj.close 