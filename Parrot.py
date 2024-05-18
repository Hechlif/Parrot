import pyaudio
import wave
import os
import keyboard
import random
import time

const = True

def get_audio():
    filename = 'recording.wav'

    chunk = 1024

    FORMAT = pyaudio.paInt16

    channels = 2

    sample_rate = 44100
    record_seconds = 10

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)

    frames = []

    print('Recording...')

    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
    print('Recording finished.')

    stream.stop_stream()
    stream.close()

    p.terminate()

    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))
    wf.close()

def play_audio():
    chunk = 1024

    f = wave.open(r'recording.wav', 'rb')
    h = pyaudio.PyAudio()
    stream = h.open(format = h.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    
    data = f.readframes(chunk)

    while data:
        stream.write(data)
        data = f.readframes(chunk)
    stream.stop_stream()
    stream.close()

    h.terminate()

def delete_audio():
    file_path = 'recording.wav'

    if os.path.exists(file_path):
        os.remove(file_path)
        print('File has been deleted.')
    else:
        print('File does not exist.')

while const == True:
    get_audio()
    play_audio()
    delete_audio()
    time.sleep(random.randint(2, 4 ))
    if keyboard.is_pressed('esc'):
        const = False