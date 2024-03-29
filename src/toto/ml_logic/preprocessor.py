from midi2audio import FluidSynth
import matplotlib.pyplot as plt
import librosa
import numpy as np
import pandas as pd
import os


def convert_midi_to_wav(
    path="./data/midis",
    soundfont="./soundfont/FluidR3_GM.sf2",
):

    files = list(os.scandir(path))
    wav_list = []
    for file in files[0:100]:

        fs = FluidSynth(soundfont)

        fs.midi_to_audio(file, f"{file.name}.wav")
        output = f"{file.name}.wav"

        wav_list.append(output)

    return wav_list


def spectogram_stft():

    files = convert_midi_to_wav()

    result_stft = []
    for file in files[0:100]:

        # using a fourier transform from librosa - stft
        y, sr = librosa.load(file, duration=15, sr=None)
        S = np.abs(librosa.stft(y))

        # fig, ax = plt.subplots()
        # img = librosa.display.specshow(librosa.amplitude_to_db(S,
        #                                                ref=np.max),
        #                         y_axis='log', x_axis='time', ax=ax)
        # ax.set_title('Power spectrogram')
        # fig.colorbar(img, ax=ax, format="%+2.0f dB")

        result_stft.append(S)

    return result_stft


def spectogram_cqt():

    files = convert_midi_to_wav()

    result_cqt = []
    for file in files[0:100]:

        y, sr = librosa.load(file, duration=15, sr=None)
        C = np.abs(librosa.cqt(y, sr=sr))
        # fig, ax = plt.subplots()
        # img = librosa.display.specshow(librosa.amplitude_to_db(C, ref=np.max),
        #                             sr=sr, x_axis='time', y_axis='cqt_note', ax=ax)
        # ax.set_title('Constant-Q power spectrum')
        # fig.colorbar(img, ax=ax, format="%+2.0f dB")

        result_cqt.append(C)

    return result_cqt


if __name__ == '__main__':
    convert_midi_to_wav
    spectogram_stft
    spectogram_cqt
