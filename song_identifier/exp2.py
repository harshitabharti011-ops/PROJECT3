import os
import librosa

from spectrogram import *
from peaks import *
from fingerprint import *
from matcher import *

SONGS_DIR = "songs"

song_hashes = {}

print("Building database...\n")

for filename in os.listdir(SONGS_DIR):

    if not filename.endswith(".wav"):
        continue

    path = os.path.join(SONGS_DIR, filename)

    audio, sr = load_audio(path)

    spec = compute_spectrogram(audio, sr)

    peaks = find_peaks(spec)

    song_hashes[filename] = generate_hashes(peaks)

database = build_database(song_hashes)

print("Database Ready!\n")


query = os.path.join(
    SONGS_DIR,
    "A Day In The Life.wav"
)

audio, sr = load_audio(query)

pitch_steps = [
    0,
    1,
    2,
    3,
    4,
    -1,
    -2,
    -3,
    -4
]

print("Pitch Shift Robustness Test\n")

for step in pitch_steps:

    shifted = librosa.effects.pitch_shift(
        y=audio,
        sr=sr,
        n_steps=step
    )

    spec = compute_spectrogram(
        shifted,
        sr
    )

    peaks = find_peaks(
        spec
    )

    hashes = generate_hashes(
        peaks
    )

    result = match_song(
        hashes,
        database
    )

    if result is None:

        print(
            f"{step:+} semitone -> No Match"
        )

    else:

        song, votes = result

        print(
            f"{step:+} semitone -> {song} ({votes} votes)"
        )
        