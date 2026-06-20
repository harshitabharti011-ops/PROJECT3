import os

from spectrogram import *
from peaks import *
from fingerprint import *
from matcher import *
import matplotlib.pyplot as plt

song_hashes = {}

for filename in os.listdir("songs"):

    path = os.path.join("songs", filename)

    print("Processing:", filename)

    audio, sr = load_audio(path)

    spec_db = compute_spectrogram(audio, sr)

    peaks = find_peaks(spec_db)

    hashes = generate_hashes(peaks)

    song_hashes[filename] = hashes

database = build_database(song_hashes)

print("Database created")
# ---------------------
# QUERY SONG
# ---------------------

query_audio, query_sr = load_audio(
    "query/query.wav"
)

query_spec = compute_spectrogram(
    query_audio,
    query_sr
)

query_peaks = find_peaks(
    query_spec
)

query_hashes = generate_hashes(
    query_peaks
)

result = match_song(
    query_hashes,
    database
)

if result is None:

    print("No match found")

else:

    best_song, offset_counts = result

    print("\nMatched Song:")
    print(best_song)

    print("\nTop Offset Matches:")

    top_matches = sorted(
        offset_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    for match, count in top_matches:

        print(match, "->", count)

song_offsets = {}

for (song, offset), count in offset_counts.items():

    if song == best_song:

        song_offsets[offset] = count

plt.figure(figsize=(10,5))

plt.bar(
    song_offsets.keys(),
    song_offsets.values()
)

plt.title(
    f"Offset Histogram - {best_song}"
)

plt.xlabel("Offset")
plt.ylabel("Match Count")

plt.show()