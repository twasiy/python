import matplotlib.pyplot as plt 
import numpy as np
import wave
obj = wave. open('sound.wav', 'rb') # Open the audio file 
framerate = obj .getframerate() # Get the frame rate
frames = obj . getnframes() # Get the number of frames
sample_frames = obj . readframes(-1) # Read all the frames
channels = obj.getnchannels() # Get the number of channels
obj.close() # Close the audio file

time_audio = frames // framerate # Calculate the time of the audio file
print(time_audio) 

signal_array = np.frombuffer(sample_frames, dtype= np.int16) # Convert the frames to a NumPy array
if channels == 2:
    signal_array = signal_array[0::2]

times = np.linspace(0,time_audio,num=len(signal_array)) # Create a time array
plt.figure(figsize=(15,5)) # Set the figure size
plt.plot(times,signal_array,'g') # Plot the audio waveform
plt.title('Audio waveform') # Set the title
plt.xlabel('Time(s)') # Set the x-axis label
plt.ylabel('Amplitude') # Set the y-axis label 
plt.xlim(0,time_audio)  # Set the x-axis limit
plt.grid(True) # Enable the grid
plt.show() 


