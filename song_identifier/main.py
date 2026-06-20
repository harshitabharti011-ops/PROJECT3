import os
import streamlit as st
import matplotlib.pyplot as plt

from spectrogram import *
from peaks import *
from fingerprint import *
from matcher import *

# =====================================
# PAGE TITLE
# =====================================
st.write("Current directory:", os.getcwd())
st.write("Root contents:", os.listdir("."))
st.title("🎵 Sonic Signature Song Identifier")

# =====================================
# BUILD DATABASE
# =====================================
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)
SONGS_DIR = os.path.join(
    BASE_DIR,
    "..",
    "songs"
)
song_hashes = {}

for filename in os.listdir(SONGS_DIR):

    if not filename.endswith(".wav"):
        continue

    path = os.path.join(SONGS_DIR,filename)

    audio, sr = load_audio(path)

    spec_db = compute_spectrogram(audio, sr)

    peaks = find_peaks(spec_db)

    hashes = generate_hashes(peaks)

    song_hashes[filename] = hashes

database = build_database(song_hashes)

st.success("Database created successfully!")

# =====================================
# LOAD QUERY FILE
# =====================================

query_path = "query/query.wav"

query_audio, query_sr = load_audio(query_path)

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

# =====================================
# MATCH SONG
# =====================================
st.write("Songs in database:", list(song_hashes.keys()))
st.write("Number of query peaks:", len(query_peaks))
st.write("Number of query hashes:", len(query_hashes))
st.write("Database size:", len(database))

result = match_song(
    query_hashes,
    database
)

if result is None:

    st.error("No match found")

else:

    best_song, offset_counts = result

    st.subheader("Matched Song")

    st.success(best_song)

    # =====================================
    # TOP OFFSET MATCHES
    # =====================================

    st.subheader("Top Offset Matches")

    top_matches = sorted(
        offset_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    for match, count in top_matches:

        st.write(
            f"{match}  →  {count}"
        )

    # =====================================
    # OFFSET HISTOGRAM
    # =====================================

    song_offsets = {}

    for (song, offset), count in offset_counts.items():

        if song == best_song:

            song_offsets[offset] = count

    fig = plt.figure(figsize=(10, 5))

    plt.bar(
        song_offsets.keys(),
        song_offsets.values()
    )

    plt.title(
        f"Offset Histogram - {best_song}"
    )

    plt.xlabel("Offset")

    plt.ylabel("Match Count")

    st.subheader("Offset Histogram")

    st.pyplot(fig)