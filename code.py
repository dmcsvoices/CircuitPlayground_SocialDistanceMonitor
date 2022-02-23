# Write your code here :-)
import os
print(os.uname())
import time
import board
import adafruit_hcsr04
import digitalio
from audiocore import WaveFile
from audioio import AudioOut

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A2, echo_pin=board.A1)


spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

audiofiles = ["plsstepbk.wav", "psst.wav", "excuseme.wav"]

def play_file(filename):
    print("Playing file: " + filename)
    wave_file = open(filename, "rb")
    with WaveFile(wave_file) as wave:
        with AudioOut(board.SPEAKER) as audio:
            audio.play(wave)
            while audio.playing:
                pass
    print("Finished")

while True:
	dist=sonar.distance
	if dist>100:
 		pass
	elif dist<50:
		play_file(audiofiles[0])
	elif dist<100:
		play_file(audiofiles[1])
	else:
	    pass
	time.sleep(0.1)


#    try:
#        print((sonar.distance,))
#    except RuntimeError:
#        print("Retrying!")
