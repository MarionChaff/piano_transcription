import streamlit as st
from midi2audio import FluidSynth
from toto.ml_logic.preprocessor import *
import midi
from os import path
from pydub import AudioSegment

st.title(":musical_note: Convert a mp3 file to Musical Sheet")

uploaded_file = st.file_uploader("Upload mp3 file", type=[".mp3"])

st.button("Convert MIDI to Score Sheet")

mp3_file = None

if uploaded_file is None:
    st.error("File type is not mp3")
    st.stop()

else:
    mp3_file = uploaded_file


completeName = os.path.join("./data/mp3", mp3_file.name)
saved_mp3 = open(completeName, "w")
saved_mp3.write()
saved_mp3.close()


sound = AudioSegment.from_mp3(mp3_file)
wav_output = "./data/wav_output/test.wav"
sound.export(wav_output, format="wav")


def generate_x_pred():
    print("ITS IN HERE!!")
    y, sr = librosa.load(wav_output, duration=15, sr=None)
    S = np.abs(librosa.stft(y))
    return S


# x_pred = generate_x_pred(midi_file)

# def convert_to_midi_note(model_outcome):
#     midi_note_number = []
#     for idx, note in enumerate(model_outcome):
#         if note == 1:
#             midi_note_number.append(idx)
#     return midi_note_number

# def create_midi_from_pitches(pitches, output_file="output.mid", tempo=120):
#     pattern = midi.Pattern()
#     track = midi.Track()
#     pattern.append(track)

#     # Set the tempo (microseconds per beat)
#     track.append(midi.SetTempoEvent(bpm=tempo))

#     # Add notes to the track based on the array of pitches
#     ticks_per_beat = 960  # Adjust as needed

#     for pitch in pitches:
#         time = 0
#         # Note On event
#         track.append(midi.NoteOnEvent(tick=time, velocity=64, pitch=pitch))

#         # Note Off event (assuming a duration of 480 ticks for each note)
#         time += ticks_per_beat
#         track.append(midi.NoteOffEvent(tick=time, pitch=pitch))

#     # Save the MIDI file
#     midi.write_midifile(output_file, pattern)
#     print("pattern", pattern)

# def predict(x_pred):
#     # TO DO: y_pred = model.predict(x_pred)
#     # convert y_pred to MIDI

#     degrees_array = []
#     for pred in y_pred:
#         degrees_array.append(convert_to_midi_note(pred))

#     pitches_sequence = flatten(degrees_array)
#     pitches_sequence

#     def flatten(xss):
#         return [x for xs in xss for x in xs]

#     pitches_sequence = flatten(degrees_array)
#     pitches_sequence

#     create_midi_from_pitches(pitches_sequence, output_file="test_test_output.mid")

#     return output_file


# on_click=generate_x_pred(midi_file)
