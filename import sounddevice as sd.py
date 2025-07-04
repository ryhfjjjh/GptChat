import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000  # 16 кГц
duration = 5  # 5 секунд
print("🎙️ Айта беріңіз...")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()

write("ztwo_voice.wav", fs, recording)
print("✅ Дыбыс сақталды: ztwo_voice.wav")
