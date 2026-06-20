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

st.title("🎵 Sonic Signature Song Identifier")
tab1, tab2 = st.tabs(
    ["📚 Library", "🔍 Identify"]
)
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

with tab1:

    st.header("Songs in Database")

    st.success(
        f"{len(song_hashes)} songs indexed"
    )

    for song in song_hashes:

        st.markdown(
            f"""
            **{song}**

            Hashes: {len(song_hashes[song])}
            """
        )

with tab2:

    st.header("Identify Song")

    uploaded_file = st.file_uploader(
        "Upload WAV file",
        type=["wav"]
    )

    # -----------------------------
    # WAIT FOR USER TO UPLOAD FILE
    # -----------------------------
    if uploaded_file is None:
        st.info("Please upload a WAV file.")
        st.stop()

    # -----------------------------
    # SAVE TEMP FILE
    # -----------------------------
    with open(
        "temp_query.wav",
        "wb"
    ) as f:

        f.write(
            uploaded_file.getbuffer()
        )

    query_path = "temp_query.wav"

    # -----------------------------
    # LOAD QUERY
    # -----------------------------
    query_audio, query_sr = load_audio(
        query_path
    )

    query_spec = compute_spectrogram(
        query_audio,
        query_sr
    )

    # -----------------------------
    # SPECTROGRAM
    # -----------------------------
    st.subheader("Spectrogram")

    fig = plt.figure(figsize=(10, 5))

    plt.imshow(
        query_spec,
        aspect="auto",
        origin="lower"
    )

    plt.title("Spectrogram")

    plt.tight_layout()

    st.pyplot(fig)

    # -----------------------------
    # CONSTELLATION MAP
    # -----------------------------
    query_peaks = find_peaks(
        query_spec
    )

    st.subheader("Constellation Map")

    fig = plt.figure(figsize=(10, 5))

    times = [p[1] for p in query_peaks]
    freqs = [p[0] for p in query_peaks]

    plt.scatter(
        times,
        freqs,
        s=2
    )

    plt.title("Constellation Map")

    plt.tight_layout()

    st.pyplot(fig)

    # -----------------------------
    # HASHES
    # -----------------------------
    query_hashes = generate_hashes(
        query_peaks
    )

    st.write(
        "Query Peaks:",
        len(query_peaks)
    )

    st.write(
        "Query Hashes:",
        len(query_hashes)
    )

    st.write(
        "Database Size:",
        len(database)
    )

    # -----------------------------
    # MATCH SONG
    # -----------------------------
    result = match_song(
        query_hashes,
        database
    )

    if result is None:

        st.error(
            "No match found"
        )

    else:

        best_song, offset_counts = result

        st.subheader(
            "Match Result"
        )

        st.success(
            f"🎵 {best_song}"
        )

        # -----------------------------
        # TOP MATCHES
        # -----------------------------
        st.subheader(
            "Top Offset Matches"
        )

        top_matches = sorted(
            offset_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]

        for match, count in top_matches:

            song, offset = match

            st.write(
                f"{song} | Offset {int(offset)} | Matches {count}"
            )

        # -----------------------------
        # HISTOGRAM
        # -----------------------------
        song_offsets = {}

        for (song, offset), count in offset_counts.items():

            if song == best_song:

                song_offsets[offset] = count

        fig = plt.figure(
            figsize=(10, 5)
        )

        plt.bar(
            song_offsets.keys(),
            song_offsets.values()
        )

        plt.yscale("log")

        plt.title(
            f"Offset Histogram - {best_song}"
        )

        plt.xlabel(
            "Offset"
        )

        plt.ylabel(
            "Match Count"
        )

        plt.tight_layout()

        st.subheader(
            "Offset Histogram"
        )

        st.pyplot(fig)