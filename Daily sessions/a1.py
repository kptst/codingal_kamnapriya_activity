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
    input("\nPress Enter to stop recording...\n")
    stop_event.set()

def spinner():
    spinner_chars = '|/-\\'
    idx = 0
    while not stop_event.is_set():
        sys.stdout.write('\rRecording... ' + spinner_chars[idx % len(spinner_chars)])
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    sys.stdout.write('\rRecording stopped.          \n')


# 4. FUNCTION spinner():
#    - While stop_event is not set:
#      - Print rotating spinner in console
#      - Sleep briefly
#    - Once stopped, print "Recording stopped."

# 5. FUNCTION record_until_enter():
#    - Initialize PyAudio
#    - Open an input stream with format=paInt16, rate=16kHz, channels=1
#    - Start threads:
#        - wait_for_enter()
#        - spinner()
#    - While stop_event is not set:
#        - Read audio data from stream
#        - Append data to a list of frames
#    - Stop and close stream
#    - Combine frames into a single bytes object
#    - Return (audio_data, rate, sample_width)

# 6. FUNCTION save_audio(data, rate, width, filename="audio.wav"):
#    - Open a wave file in write-binary mode
#    - Set channels=1, setsampwidth=width, setframerate=rate
#    - Write frames (data) to file
#    - Print confirmation

# 7. FUNCTION transcribe_audio(data, rate, width, filename="transcription.txt"):
#    - Create an sr.Recognizer
#    - Convert raw data to AudioData
#    - Use Google recognizer to get text
#    - Handle errors appropriately
#    - Save result to file, print text

# 8. FUNCTION show_waveform(data, rate):
#    - Convert data to numpy array of int16
#    - Create a time axis based on sample count and rate
#    - Plot the waveform with matplotlib
#    - Show the plot

# 9. FUNCTION main():
#    - Print "Start speaking..." message
#    - Call record_until_enter() to get audio data
#    - save_audio(...) the data
#    - transcribe_audio(...) the data
#    - show_waveform(...) the data

# 10. IF __name__ == "__main__":
#    - main()



# Full-code

# import threading
# import sys
# import time
# import pyaudio
# import numpy as np
# import matplotlib.pyplot as plt
# import wave
# import speech_recognition as sr
# from speech_recognition import AudioData

# # Global stop event
# stop_event = threading.Event()


# def wait_for_enter():
#     input("\nPress Enter to stop recording...\n")
#     stop_event.set()


# def spinner():
#     spinner_chars = '|/-\\'
#     idx = 0
#     while not stop_event.is_set():
#         sys.stdout.write('\rRecording... ' + spinner_chars[idx % len(spinner_chars)])
#         sys.stdout.flush()
#         idx += 1
#         time.sleep(0.1)
#     sys.stdout.write('\rRecording stopped.          \n')


# def record_until_enter(rate=16000, channels=1):
#     p = pyaudio.PyAudio()
#     format = pyaudio.paInt16
#     chunk = 1024

#     stream = p.open(format=format,
#                     channels=channels,
#                     rate=rate,
#                     input=True,
#                     frames_per_buffer=chunk)

#     frames = []

#     t1 = threading.Thread(target=wait_for_enter)
#     t2 = threading.Thread(target=spinner)

#     t1.start()
#     t2.start()

#     while not stop_event.is_set():
#         data = stream.read(chunk, exception_on_overflow=False)
#         frames.append(data)

#     stream.stop_stream()
#     stream.close()
#     p.terminate()

#     audio_data = b''.join(frames)
#     sample_width = p.get_sample_size(format)

#     return audio_data, rate, sample_width


# def save_audio(data, rate, width, filename="audio.wav"):
#     with wave.open(filename, 'wb') as wf:
#         wf.setnchannels(1)
#         wf.setsampwidth(width)
#         wf.setframerate(rate)
#         wf.writeframes(data)

#     print(f"Audio saved as {filename}")


# def transcribe_audio(data, rate, width, filename="transcription.txt"):
#     recognizer = sr.Recognizer()
#     audio = AudioData(data, rate, width)

#     try:
#         text = recognizer.recognize_google(audio)
#         print("\nTranscription:")
#         print(text)

#         with open(filename, "w") as f:
#             f.write(text)

#         print(f"Transcription saved as {filename}")

#     except sr.UnknownValueError:
#         print("Speech could not be understood")
#     except sr.RequestError as e:
#         print(f"Could not request results; {e}")


# def show_waveform(data, rate):
#     audio_np = np.frombuffer(data, dtype=np.int16)
#     time_axis = np.linspace(0, len(audio_np) / rate, num=len(audio_np))

#     plt.figure(figsize=(10, 4))
#     plt.plot(time_axis, audio_np)
#     plt.title("Audio Waveform")
#     plt.xlabel("Time (seconds)")
#     plt.ylabel("Amplitude")
#     plt.tight_layout()
#     plt.show()


# def main():
#     print("Start speaking...")
#     audio_data, rate, width = record_until_enter()

#     save_audio(audio_data, rate, width)
#     transcribe_audio(audio_data, rate, width)
#     show_waveform(audio_data, rate)


# if __name__ == "__main__":
#     main()
