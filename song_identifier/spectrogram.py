import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def load_audio(file_path):
    """
    Load an audio file.

    Returns:
        y  -> audio samples
        sr -> sampling rate
    """
    y, sr = librosa.load(file_path, sr=None)

    return y, sr


def compute_spectrogram(y, sr):
    """
    Compute STFT spectrogram.

    Returns:
        spectrogram in dB scale
    """

    stft = librosa.stft(
        y,
        n_fft=2048,
        hop_length=512
    )

    magnitude = np.abs(stft)

    spectrogram_db = librosa.amplitude_to_db(
        magnitude,
        ref=np.max
    )

    return spectrogram_db


def plot_spectrogram(spec_db, sr):
    """
    Display spectrogram.
    """

    plt.figure(figsize=(12, 6))

    librosa.display.specshow(
        spec_db,
        sr=sr,
        x_axis='time',
        y_axis='hz'
    )

    plt.colorbar(format="%+2.0f dB")

    plt.title("Spectrogram")

    plt.tight_layout()

    plt.show()