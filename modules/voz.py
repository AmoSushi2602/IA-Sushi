from TTS.api import TTS
import sounddevice as sd
from config import MODELO_VOZ

tts = TTS(model_name=MODELO_VOZ)

def falar(texto):
    wav = tts.tts(texto)
    sd.play(wav, samplerate=tts.synthesizer.output_sample_rate)
    sd.wait()