"""

L2: Voice Analysis Lab

Record → Analyze → Compare Two Recordings

 

============== DEPENDENCY SETUP ==============

CHECK IF INSTALLED: pip show SpeechRecognition pyaudio numpy matplotlib

 

INSTALL - WINDOWS:

pip install SpeechRecognition pyaudio numpy matplotlib

 

INSTALL - macOS:

brew install portaudio

pip install SpeechRecognition pyaudio numpy matplotlib

==============================================

"""

 

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

stop_event = threading.Event() # shared event to signal when to stop recording

# WHY threading? We need the program to do two things simultaneously: (1) continuously record audio, and (2) wait for the user to press Enter. Without threading, we'd have to choose one - either record blindly for a fixed time, or stop recording to check for input. Threading lets both happen at once.

# ANALOGY: The Parallel Workers
# Threading is like having two workers in a factory. One worker (wait_for_enter) watches the stop button. Another worker (the recording loop) operates the machine. They share a walkie-talkie (stop_event). When the button-watcher sees the button pressed, they radio 'STOP' and the machine operator immediately stops. Neither worker has to pause their job to check on the other - they work in parallel.

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
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, # 16 bit samples(65,536 precision levels), channels 1(mono): simpler for speech, rate 16000 samples/sec (CD quality). input= True means we're recording, frames_per_buffer=1024 means we read 1024 samples at a time (about 64ms of audio) for smooth processing.
                    input=True, frames_per_buffer=1024)
    frames = []
    
# WHY these specific values?
# paInt16: 16-bit gives us 65,536 levels of precision - enough for clear speech without excessive file size
# channels=1: Mono audio. Stereo would double file size but add nothing for speech recognition - AI doesn't need spatial audio
# rate=16000: Standard for speech recognition APIs. Human speech maxes out around 3,400 Hz; 16,000 Hz captures it perfectly (Nyquist theorem)
# frames_per_buffer=1024: Balance between latency and CPU usage. Smaller = more responsive but more CPU. 1024 is the sweet spot

    threading.Thread(target=wait_for_enter, daemon=True).start()
    threading.Thread(target=spinner, daemon=True).start()
    
    while not stop_event.is_set():
        frames.append(stream.read(1024))
    
    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    return b''.join(frames), 16000, width

def save_audio(data, rate, width, filename="recording.wav"):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(data)
    print(f"💾 Saved: {filename}")

def transcribe(data, rate, width):
    recognizer = sr.Recognizer()
    audio = AudioData(data, rate, width) # wrap raw bytes with metadata so SpeechRecognition can process it
    try:
        text = recognizer.recognize_google(audio) # (send to Google's free API for transcription. Note: this requires internet and may have limits on usage. ) Send to google, get text
# WHY AudioData wrapper? Raw bytes are just numbers. The API needs to know: What sample rate? What bit depth? How many channels? AudioData packages this metadata with the audio so Google's servers know how to interpret the numbers.

        print(f"📝 Transcription: {text}")
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")

def plot_waveform(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)
    time_axis = np.linspace(0, len(samples) / rate, len(samples))
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, samples, color='blue')
    plt.title("Your Voice Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

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