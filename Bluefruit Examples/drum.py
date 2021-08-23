import time
import board
import touchio
import digitalio

try:
    from audiocore import WaveFile
except:
    from audioio import WaveFile

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass

bpm = 120 # beats per minute

speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True

capPins = (board.A1, board.A2, board.A3, board.A4, board.A5, board.A6, board.TX)

touchPad = []

for i in range(7):
    touchPad.append(touchio.TouchIn(capPins[i]))

# audiofiles = ["bd_tek.wav", "elec_hi_snare.wav", "elec_cymbal.wav",
#     "elec_blip2.wav", "bd_zome.wav", "bass_hit_c.wav", "drum_cowbell.wav"]
audiofiles = ["kill.wav", "jump.wav", "hit.wav", "empty-block.wav", "death.wav", "coin.wav"]

audio = AudioOut(board.SPEAKER)


def play_file(filename):
    print("playing file " + filename)
    file = open(filename, "rb")
    wave = WaveFile(file)
    audio.play(wave)
    time.sleep(bpm / 960) # sixteenth note delay


while True:
    for i in range(7):
        if touchPad[i].value:
            play_file(audiofiles[i])
