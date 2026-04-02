"""
L1: Basic Speech-to-Text
Record → Save → Transcribe → Visualize Waveform
"""
import threading
import sys
import time
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wave
import speech_recognition as sr
from speech_recognition import AudioData

stop_event = threading.Event()

def wait_for_enter():
    input("\n🎤 Press Enter to stop recording...\n")
    stop_event.set()

def spinner():
    chars = '|/-\\'
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f'\r🔴 Recording... {chars[i % 4]}')
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    print("\r✅ Recording complete!          ")

def record_audio():
    # TODO: Initialize PyAudio
    # p = pyaudio.PyAudio()
    p = None  # placeholder

    # TODO: Open microphone stream
    # stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
    #                 input=True, frames_per_buffer=1024)
    stream = None  # placeholder

    frames = []
    
    threading.Thread(target=wait_for_enter, daemon=True).start()
    threading.Thread(target=spinner, daemon=True).start()
    
    while not stop_event.is_set():
        # TODO: Read audio chunk and store it
        # frames.append(stream.read(1024))
        pass
    
    # TODO: Stop and close stream
    # stream.stop_stream()
    # stream.close()

    # TODO: Get sample width and terminate PyAudio
    # width = p.get_sample_size(pyaudio.paInt16)
    # p.terminate()
    width = 2  # placeholder for 16-bit audio

    # TODO: Return recorded bytes, sample rate, and width
    # return b''.join(frames), 16000, width
    return b''.join(frames), 16000, width

def save_audio(data, rate, width, filename="recording.wav"):
    # TODO: Save audio bytes into a .wav file using wave
    # with wave.open(filename, 'wb') as wf:
    #     wf.setnchannels(1)
    #     wf.setsampwidth(width)
    #     wf.setframerate(rate)
    #     wf.writeframes(data)
    print(f"💾 Saved: {filename}")

def transcribe(data, rate, width):
    recognizer = sr.Recognizer()
    audio = AudioData(data, rate, width)
    try:
        # TODO: Transcribe using Google Speech Recognition
        # text = recognizer.recognize_google(audio)
        # print(f"📝 Transcription: {text}")
        pass
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")

def plot_waveform(data, rate):
    # TODO: Convert bytes to samples and plot waveform
    # samples = np.frombuffer(data, dtype=np.int16)
    # time_axis = np.linspace(0, len(samples) / rate, len(samples))
    # plt.figure(figsize=(10, 4))
    # plt.plot(time_axis, samples, color='blue')
    # plt.title("Your Voice Waveform")
    # plt.xlabel("Time (seconds)")
    # plt.ylabel("Amplitude")
    # plt.grid(True, alpha=0.3)
    # plt.tight_layout()
    # plt.show()
    pass

def main():
    print("=" * 40)
    print("🎙️  HELLO AI, CAN YOU HEAR ME?")
    print("=" * 40)
    print("\nSpeak into your microphone...")
    
    audio_data, rate, width = record_audio()
    save_audio(audio_data, rate, width)
    transcribe(audio_data, rate, width)
    plot_waveform(audio_data, rate)

if __name__ == "__main__":
    main()
