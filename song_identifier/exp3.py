import os

from spectrogram import *
from peaks import *
from fingerprint import *
from matcher import *


def generate_single_peak_hashes(peaks):

    hashes = []

    for freq, time in peaks:

        hash_key = freq

        hashes.append(
            (
                hash_key,
                time
            )
        )

    return hashes


SONGS_DIR = "songs"

pair_song_hashes = {}

single_song_hashes = {}

print("Building databases...\n")

for filename in os.listdir(SONGS_DIR):

    if not filename.endswith(".wav"):
        continue

    path = os.path.join(
        SONGS_DIR,
        filename
    )

    audio, sr = load_audio(path)

    spec = compute_spectrogram(
        audio,
        sr
    )

    peaks = find_peaks(
        spec
    )

    pair_song_hashes[filename] = generate_hashes(
        peaks
    )

    single_song_hashes[filename] = generate_single_peak_hashes(
        peaks
    )


pair_database = build_database(
    pair_song_hashes
)

single_database = build_database(
    single_song_hashes
)


print("Databases Ready!\n")


query = os.path.join(
    SONGS_DIR,
    "A Day In The Life.wav"
)

audio, sr = load_audio(
    query
)

spec = compute_spectrogram(
    audio,
    sr
)

query_peaks = find_peaks(
    spec
)


pair_hashes = generate_hashes(
    query_peaks
)

single_hashes = generate_single_peak_hashes(
    query_peaks
)


pair_result = match_song(
    pair_hashes,
    pair_database
)

single_result = match_song(
    single_hashes,
    single_database
)


print("===== Pair-Based Fingerprinting =====\n")

if pair_result is None:

    print("No Match")

else:

    song, votes = pair_result

    print(f"Matched Song : {song}")

    print(f"Votes        : {votes}")


print("\n===== Single-Peak Fingerprinting =====\n")

if single_result is None:

    print("No Match")

else:

    song, votes = single_result

    print(f"Matched Song : {song}")

    print(f"Votes        : {votes}")