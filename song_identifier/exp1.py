import os
import numpy as np

from spectrogram import *
from peaks import *
from fingerprint import *
from matcher import *
def add_noise(audio, noise_level):
    
    # noise_level = 0.05 means 5% Gaussian noise
    
    noise = np.random.normal(
        0,
        noise_level,
        len(audio)
    )

    noisy_audio = audio + noise

    noisy_audio = np.clip(
        noisy_audio,
        -1,
        1
    )

    return noisy_audio
SONGS_DIR = "songs"

song_hashes = {}

for filename in os.listdir(SONGS_DIR):

    if not filename.endswith(".wav"):
        continue

    path = os.path.join(SONGS_DIR, filename)

    audio, sr = load_audio(path)

    spec = compute_spectrogram(audio, sr)

    peaks = find_peaks(spec)

    song_hashes[filename] = generate_hashes(peaks)

database = build_database(song_hashes)

query = os.path.join(
    SONGS_DIR,
    "A Day In The Life.wav"
)

audio, sr = load_audio(query)

duration = 20
audio = audio[:duration * sr]


noise_levels = [0,0.05,0.10,0.20,0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1]

for level in noise_levels:

    noisy = add_noise(audio, level)

    spec = compute_spectrogram(noisy, sr)

    peaks = find_peaks(spec)

    hashes = generate_hashes(peaks)

    result = match_song(hashes, database)

    if result is None:

        print(f"{int(level*100)}% Noise -> No Match")

    else:

        song, votes = result
        print(
        f"{int(level*100)}% Noise -> {song} ({votes} votes)"
        )

