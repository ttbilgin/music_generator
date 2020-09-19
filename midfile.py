from midiutil import MIDIFile

degrees  = [48,49 , 60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 0.5    # In beats
tempo    = 100   # In BPM
volume   = 100  # 0-127, as per the MIDI standard
program  = 3 #enstruman no

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    MyMIDI.addProgramChange(track, channel, time, program) # enstruman degistir
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
    print(track, channel, pitch, time + i, duration, volume)

with open("ornek_muzik.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
