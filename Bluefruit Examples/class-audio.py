import board
from digitalio import DigitalInOut, Direction, Pull

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

# Enable the speaker
speaker_enable = DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = Direction.OUTPUT
speaker_enable.value = True

# class DigitalInputOutput(object):
#     def __init__(self, button):
#         self._button = DigitalInOut(button)

#     def set_direction(self, direction, pull):
#         self._button.direction = direction
#         self._button.pull = pull


# # Make the 2 input buttons
# button_a = DigitalInputOutput(board.BUTTON_A)
# button_a.set_direction(Direction.OUTPUT, Pull.DOWN)

# button_a = digitalio.DigitalInOut(board.BUTTON_A)
# button_a.direction = digitalio.Direction.INPUT
# button_a.pull = digitalio.Pull.DOWN

# button_b = digitalio.DigitalInOut(board.BUTTON_B)
# button_b.direction = digitalio.Direction.INPUT
# button_b.pull = digitalio.Pull.DOWN

audiofiles = ["rimshot.wav", "laugh.wav"]

def play_file(filename):
    print("Playing file: " + filename)
    wave_file = open(filename, "rb")
    with WaveFile(wave_file) as wave:
        with AudioOut(board.SPEAKER) as audio:
            audio.play(wave)
            while audio.playing:
                pass
    print("Finished")

# while True:
    # if button_a.value:
    #     play_file(audiofiles[0])
