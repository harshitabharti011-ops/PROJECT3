
# import os
# import streamlit as st
# import matplotlib
# matplotlib.use("Agg")
# import matplotlib.pyplot as plt
# import numpy as np

# from spectrogram import *
# from peaks import *
# from fingerprint import *
# from matcher import *

# # =====================================
# # PAGE CONFIG & GLOBAL STYLES
# # =====================================
# st.set_page_config(
#     page_title="EE200: Audio Fingerprinting",
#     page_icon="🎵",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# st.markdown(
#     """
#     <style>
#     /* ---- Base & font ---- */
#     @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Inter:wght@300;400;500;600&display=swap');

#     html, body, [class*="css"] {
#         font-family: 'Inter', sans-serif;
#         background-color: #0a0d10;
#         color: #c9d1d9;
#     }

#     /* ---- App background ---- */
#     .stApp {
#         background-color: #0a0d10;
#     }

#     /* ---- Hide default Streamlit chrome ---- */
#     #MainMenu, footer, header { visibility: hidden; }
#     .block-container {
#         padding-top: 2rem;
#         padding-bottom: 3rem;
#         max-width: 1200px;
#     }

#     /* ---- Top header banner ---- */
#     .page-header {
#         display: flex;
#         align-items: center;
#         gap: 1rem;
#         padding: 0.5rem 0 1.5rem 0;
#         border-bottom: 1px solid #1e2530;
#         margin-bottom: 0.5rem;
#     }
#     .header-icon {
#         background: #0d1117;
#         border: 1px solid #1e2530;
#         border-radius: 8px;
#         padding: 10px 12px;
#         font-size: 1.6rem;
#         line-height: 1;
#     }
#     .header-text h1 {
#         margin: 0;
#         font-size: 1.9rem;
#         font-weight: 700;
#         color: #e6edf3;
#         letter-spacing: -0.5px;
#     }
#     .header-text h1 span {
#         color: #39d353;
#     }
#     .header-text .subtitle {
#         font-family: 'IBM Plex Mono', monospace;
#         font-size: 0.72rem;
#         letter-spacing: 0.12em;
#         color: #484f58;
#         text-transform: uppercase;
#         margin-top: 3px;
#     }
#     .header-text .desc {
#         font-size: 0.88rem;
#         color: #8b949e;
#         margin-top: 4px;
#     }

#     /* ---- Tabs ---- */
#     .stTabs [data-baseweb="tab-list"] {
#         background: transparent;
#         border-bottom: 1px solid #1e2530;
#         gap: 0;
#         padding: 0;
#     }
#     .stTabs [data-baseweb="tab"] {
#         font-family: 'IBM Plex Mono', monospace;
#         font-size: 0.78rem;
#         letter-spacing: 0.08em;
#         color: #484f58;
#         background: transparent;
#         border: none;
#         border-bottom: 2px solid transparent;
#         padding: 0.7rem 1.4rem;
#         text-transform: uppercase;
#     }
#     .stTabs [aria-selected="true"] {
#         color: #39d353 !important;
#         border-bottom: 2px solid #39d353 !important;
#         background: transparent !important;
#     }
#     .stTabs [data-baseweb="tab-highlight"] { display: none; }
#     .stTabs [data-baseweb="tab-border"] { display: none; }

#     /* ---- Section label ---- */
#     .section-label {
#         font-family: 'IBM Plex Mono', monospace;
#         font-size: 0.68rem;
#         letter-spacing: 0.14em;
#         color: #484f58;
#         text-transform: uppercase;
#         margin: 1.5rem 0 0.8rem 0;
#         padding-bottom: 0.4rem;
#         border-bottom: 1px solid #1e2530;
#     }

#     /* ---- Info banner ---- */
#     .info-banner {
#         background: #0d1117;
#         border: 1px solid #1e2530;
#         border-radius: 6px;
#         padding: 1.2rem 1.5rem;
#         text-align: center;
#         color: #484f58;
#         font-size: 0.88rem;
#         font-family: 'IBM Plex Mono', monospace;
#         margin-bottom: 1.5rem;
#         line-height: 1.8;
#     }

#     /* ---- Song card grid ---- */
#     .song-grid {
#         display: grid;
#         grid-template-columns: repeat(4, 1fr);
#         gap: 14px;
#         margin-top: 0.5rem;
#     }
#     .song-card {
#         background: #0d1117;
#         border: 1px solid #1e2530;
#         border-radius: 8px;
#         overflow: hidden;
#         transition: border-color 0.2s;
#     }
#     .song-card:hover { border-color: #39d353; }
#     .song-card .card-img {
#         width: 100%;
#         aspect-ratio: 1.5;
#         object-fit: cover;
#         display: block;
#         background: #111820;
#     }
#     .song-card .card-body {
#         padding: 10px 12px 12px 12px;
#     }
#     .song-card .card-title {
#         font-size: 0.85rem;
#         font-weight: 600;
#         color: #e6edf3;
#         margin: 0 0 4px 0;
#         white-space: nowrap;
#         overflow: hidden;
#         text-overflow: ellipsis;
#     }
#     .song-card .card-hashes {
#         font-family: 'IBM Plex Mono', monospace;
#         font-size: 0.72rem;
#         color: #484f58;
#     }

#     /* ---- Stat pills ---- */
#     .stat-row {
#         display: flex;
#         gap: 10px;
#         margin: 1rem 0;
#     }
#     .stat-pill {
#         background: #0d1117;
#         border: 1px solid #1e2530;
#         border-radius: 6px;
#         padding: 0.5rem 1rem;
#         font-family: 'IBM Plex Mono', monospace;
#         font-size: 0.78rem;
#         color: #8b949e;
#     }
#     .stat-pill span { color: #39d353; font-weight: 600; }

#     /* ---- Match result ---- */
#     .match-banner {
#         background: #0d2119;
#         border: 1px solid #39d353;
#         border-radius: 8px;
#         padding: 1rem 1.4rem;
#         font-size: 1rem;
#         font-weight: 600;
#         color: #39d353;
#         display: flex;
#         align-items: center;
#         gap: 0.6rem;
#         margin: 1rem 0;
#     }
#     .no-match-banner {
#         background: #1a0d0d;
#         border: 1px solid #6e2929;
#         border-radius: 8px;
#         padding: 1rem 1.4rem;
#         font-size: 0.95rem;
#         color: #f85149;
#         margin: 1rem 0;
#     }

#     /* ---- File uploader ---- */
#     [data-testid="stFileUploader"] {
#         background: #0d1117;
#         border: 1px dashed #1e2530;
#         border-radius: 8px;
#         padding: 0.5rem;
#     }
#     [data-testid="stFileUploader"]:hover {
#         border-color: #39d353;
#     }

#     /* ---- Subheaders ---- */
#     .sub-label {
#         font-family: 'IBM Plex Mono', monospace;
#         font-size: 0.72rem;
#         letter-spacing: 0.12em;
#         color: #39d353;
#         text-transform: uppercase;
#         margin: 1.5rem 0 0.5rem 0;
#     }

#     /* ---- Dataframe ---- */
#     [data-testid="stDataFrame"] {
#         background: #0d1117;
#         border: 1px solid #1e2530;
#         border-radius: 6px;
#     }

#     /* ---- Button ---- */
#     .stButton > button {
#         background: #0d2119;
#         border: 1px solid #39d353;
#         color: #39d353;
#         font-family: 'IBM Plex Mono', monospace;
#         font-size: 0.8rem;
#         letter-spacing: 0.08em;
#         border-radius: 6px;
#         padding: 0.5rem 1.4rem;
#         transition: background 0.2s;
#     }
#     .stButton > button:hover {
#         background: #163324;
#         border-color: #39d353;
#         color: #39d353;
#     }

#     /* ---- Offset table ---- */
#     .offset-row {
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#         padding: 6px 12px;
#         border-bottom: 1px solid #1e2530;
#         font-family: 'IBM Plex Mono', monospace;
#         font-size: 0.78rem;
#     }
#     .offset-row:last-child { border-bottom: none; }
#     .offset-row .song-name { color: #8b949e; }
#     .offset-row .offset-val { color: #484f58; }
#     .offset-row .match-count { color: #39d353; font-weight: 600; }
#     .offset-table {
#         background: #0d1117;
#         border: 1px solid #1e2530;
#         border-radius: 8px;
#         overflow: hidden;
#         margin-top: 0.5rem;
#     }

#     /* ---- Matplotlib dark theme ---- */
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # =====================================
# # MATPLOTLIB DARK THEME HELPER
# # =====================================
# def dark_fig(w=10, h=4):
#     fig, ax = plt.subplots(figsize=(w, h))
#     fig.patch.set_facecolor("#0d1117")
#     ax.set_facecolor("#0d1117")
#     ax.tick_params(colors="#484f58", labelsize=8)
#     ax.xaxis.label.set_color("#8b949e")
#     ax.yaxis.label.set_color("#8b949e")
#     ax.title.set_color("#c9d1d9")
#     for spine in ax.spines.values():
#         spine.set_edgecolor("#1e2530")
#     return fig, ax


# def constellation_fig(peaks, title="Constellation Map"):
#     fig, ax = dark_fig(10, 3.5)
#     times = [p[1] for p in peaks]
#     freqs = [p[0] for p in peaks]
#     # colour by frequency band for the colourful dot look in the screenshot
#     colours = plt.cm.plasma(np.array(freqs) / (max(freqs) + 1))
#     ax.scatter(times, freqs, s=2, c=colours, alpha=0.8, linewidths=0)
#     ax.set_title(title, fontsize=9)
#     ax.set_xlabel("Time frame", fontsize=8)
#     ax.set_ylabel("Frequency bin", fontsize=8)
#     fig.tight_layout()
#     return fig


# def spectrogram_fig(spec_db):
#     fig, ax = dark_fig(10, 3.5)
#     img = ax.imshow(
#         spec_db,
#         aspect="auto",
#         origin="lower",
#         cmap="inferno",
#         interpolation="nearest",
#     )
#     plt.colorbar(img, ax=ax, pad=0.02).ax.tick_params(colors="#484f58", labelsize=7)
#     ax.set_title("Spectrogram (dB)", fontsize=9)
#     ax.set_xlabel("Time frame", fontsize=8)
#     ax.set_ylabel("Frequency bin", fontsize=8)
#     fig.tight_layout()
#     return fig


# def histogram_fig(song_offsets, best_song):
#     fig, ax = dark_fig(10, 3)
#     offsets = list(song_offsets.keys())
#     counts = list(song_offsets.values())
#     ax.bar(offsets, counts, color="#39d353", width=0.8, alpha=0.85)
#     ax.set_yscale("log")
#     ax.set_title(f"Offset Histogram — {best_song}", fontsize=9)
#     ax.set_xlabel("Offset (frames)", fontsize=8)
#     ax.set_ylabel("Match count", fontsize=8)
#     fig.tight_layout()
#     return fig


# # =====================================
# # PAGE HEADER
# # =====================================
# st.markdown(
#     """
#     <div class="page-header">
#       <div class="header-icon">📊</div>
#       <div class="header-text">
#         <h1><span>EE200</span>: Audio Fingerprinting</h1>
#         <div class="subtitle">Signals, Systems &amp; Networks &nbsp;·&nbsp; Project by Harshita </div>
#         <div class="desc">Index a library of songs as spectrogram fingerprints, then identify any short clip against it.</div>
#       </div>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# # =====================================
# # BUILD DATABASE
# # =====================================
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# SONGS_DIR = os.path.join(BASE_DIR, "..", "songs")

# song_hashes = {}
# song_peaks_map = {}   # store peaks so we can render constellation thumbnails

# for filename in os.listdir(SONGS_DIR):
#     if not filename.endswith(".wav"):
#         continue
#     path = os.path.join(SONGS_DIR, filename)
#     try:
#         audio, sr = load_audio(path)
#     except Exception as e:
#         st.error(f"Failed loading: {filename}")
#         st.write(e)
#         continue

#     spec_db = compute_spectrogram(audio, sr)
#     peaks = find_peaks(spec_db)
#     hashes = generate_hashes(peaks)
#     song_hashes[filename] = hashes
#     song_peaks_map[filename] = peaks

# database = build_database(song_hashes)

# # =====================================
# # TABS
# # =====================================
# tab1, tab2, tab3 = st.tabs(["◆ LIBRARY", "◎ IDENTIFY", "▣ BATCH"])

# # ─────────────────────────────────────
# # TAB 1 — LIBRARY
# # ─────────────────────────────────────
# with tab1:
#     st.markdown('<div class="section-label">Library</div>', unsafe_allow_html=True)
#     st.markdown(
#         """
#         <div class="info-banner">
#             Song indexing is managed by the admin.<br>
#             Drop a clip in the Identify tab to test the library.
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     st.markdown(
#         f'<div class="section-label">In The Database &nbsp;·&nbsp; {len(song_hashes)} songs indexed</div>',
#         unsafe_allow_html=True,
#     )

#     songs_list = list(song_hashes.keys())
#     cols_per_row = 4

#     # Render cards in rows of 4
#     for row_start in range(0, len(songs_list), cols_per_row):
#         row_songs = songs_list[row_start : row_start + cols_per_row]
#         cols = st.columns(cols_per_row)
#         for col, song in zip(cols, row_songs):
#             with col:
#                 # Render mini constellation map as card thumbnail
#                 peaks = song_peaks_map.get(song, [])
#                 if peaks:
#                     thumb_fig, thumb_ax = plt.subplots(figsize=(3, 2))
#                     thumb_fig.patch.set_facecolor("#0d1117")
#                     thumb_ax.set_facecolor("#0d1117")
#                     times = [p[1] for p in peaks]
#                     freqs = [p[0] for p in peaks]
#                     colours = plt.cm.plasma(
#                         np.array(freqs) / (max(freqs) + 1)
#                     )
#                     thumb_ax.scatter(times, freqs, s=1, c=colours, alpha=0.7)
#                     thumb_ax.axis("off")
#                     thumb_fig.tight_layout(pad=0)
#                     st.pyplot(thumb_fig, use_container_width=True)
#                     plt.close(thumb_fig)

#                 display_name = os.path.splitext(song)[0].replace("_", " ").title()
#                 st.markdown(
#                     f"""
#                     <div style="padding:6px 2px 10px 2px;">
#                       <div style="font-size:0.84rem;font-weight:600;color:#e6edf3;
#                                   white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">
#                         {display_name}
#                       </div>
#                       <div style="font-family:'IBM Plex Mono',monospace;font-size:0.71rem;
#                                   color:#484f58;margin-top:3px;">
#                         {len(song_hashes[song]):,} hashes
#                       </div>
#                     </div>
#                     """,
#                     unsafe_allow_html=True,
#                 )

# # ─────────────────────────────────────
# # TAB 2 — IDENTIFY
# # ─────────────────────────────────────
# with tab2:
#     st.markdown('<div class="section-label">Identify Song</div>', unsafe_allow_html=True)

#     st.markdown(
#     '<div class="section-label">Or Try A Sample</div>',
#     unsafe_allow_html=True
#     )

#     sample_files = [
#         "sample1.wav",
#         "sample2.wav",
#         "sample3.wav",
#         "sample4.wav",
#         "sample5.wav"
#     ]

#     selected_sample = None

#     for sample in sample_files:

#         col1, col2 = st.columns([5,1])

#         sample_path = os.path.join(
#             BASE_DIR,
#             "..",
#             "samples",
#             sample
#         )

#         with col1:
#             st.audio(sample_path)

#         with col2:
#             if st.button(
#                 "Try",
#                 key=sample
#             ):
#                 selected_sample = sample_path

#     uploaded_file = st.file_uploader(
#     "Upload a WAV clip to identify",
#     type=["wav"],
#     label_visibility="collapsed",
#     )

#     query_path = None

#     if uploaded_file is not None:

#         with open(
#             "temp_query.wav",
#             "wb"
#         ) as f:

#             f.write(
#                 uploaded_file.getbuffer()
#             )

#         query_path = "temp_query.wav"

#     elif selected_sample:

#         query_path = selected_sample

#     if query_path is None:

#         st.markdown(
#             '<div class="info-banner">Upload a WAV file or try one of the sample clips.</div>',
#             unsafe_allow_html=True,
#         )

#         st.stop()

#     # Save temp file
#     query_audio, query_sr = load_audio(query_path)
#     query_spec = compute_spectrogram(query_audio, query_sr)
#     query_peaks = find_peaks(query_spec)
#     query_hashes = generate_hashes(query_peaks)

#     # Stats row
#     st.markdown(
#         f"""
#         <div class="stat-row">
#           <div class="stat-pill">Peaks &nbsp;<span>{len(query_peaks):,}</span></div>
#           <div class="stat-pill">Query hashes &nbsp;<span>{len(query_hashes):,}</span></div>
#           <div class="stat-pill">DB entries &nbsp;<span>{len(database):,}</span></div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     col_a, col_b = st.columns(2)

#     with col_a:
#         st.markdown('<div class="sub-label">Spectrogram</div>', unsafe_allow_html=True)
#         st.pyplot(spectrogram_fig(query_spec), use_container_width=True)

#     with col_b:
#         st.markdown('<div class="sub-label">Constellation Map</div>', unsafe_allow_html=True)
#         st.pyplot(constellation_fig(query_peaks), use_container_width=True)

#     # Match
#     result = match_song(query_hashes, database)

#     st.markdown('<div class="section-label">Match Result</div>', unsafe_allow_html=True)

#     if result is None:
#         st.markdown(
#             '<div class="no-match-banner">✗ No match found in the library.</div>',
#             unsafe_allow_html=True,
#         )
#     else:
#         best_song, offset_counts = result

#         candidate_scores = {}

#         for (song, offset), count in offset_counts.items():

#             candidate_scores[song] = (
#                 candidate_scores.get(song, 0)
#                 + count
#             )

#         candidate_scores = sorted(
#             candidate_scores.items(),
#             key=lambda x: x[1],
#             reverse=True
#         )

#         display_best = os.path.splitext(best_song)[0].replace("_", " ").title()
#         st.markdown(
#             f'<div class="match-banner">🎵 {display_best}</div>',
#             unsafe_allow_html=True,
#         )

#         st.markdown(
#             '<div class="section-label">Candidate Scores</div>',
#             unsafe_allow_html=True
#         )

#         for song, score in candidate_scores[:5]:
#             st.write(
#                 os.path.splitext(song)[0]
#             )

#             st.progress(
#                 score /
#                 candidate_scores[0][1]
#             )

#         col_c, col_d = st.columns([1, 1])

#         with col_c:
#             st.markdown('<div class="sub-label">Top Offset Matches</div>', unsafe_allow_html=True)
#             top_matches = sorted(
#                 offset_counts.items(), key=lambda x: x[1], reverse=True
#             )[:10]
#             rows_html = "".join(
#                 f"""
#                 <div class="offset-row">
#                   <span class="song-name">{os.path.splitext(s)[0]}</span>
#                   <span class="offset-val">+{int(o)}</span>
#                   <span class="match-count">{c}</span>
#                 </div>
#                 """
#                 for (s, o), c in top_matches
#             )
#             st.markdown(
#                 f'<div class="offset-table">{rows_html}</div>',
#                 unsafe_allow_html=True,
#             )

#         with col_d:
#             st.markdown('<div class="sub-label">Offset Histogram</div>', unsafe_allow_html=True)
#             song_offsets = {
#                 offset: count
#                 for (song, offset), count in offset_counts.items()
#                 if song == best_song
#             }
#             st.pyplot(histogram_fig(song_offsets, display_best), use_container_width=True)
        
    

# # ─────────────────────────────────────
# # TAB 3 — BATCH
# # ─────────────────────────────────────
# with tab3:
#     st.markdown('<div class="section-label">Batch Identification</div>', unsafe_allow_html=True)

#     uploaded_files = st.file_uploader(
#         "Upload multiple WAV clips",
#         type=["wav"],
#         accept_multiple_files=True,
#         label_visibility="collapsed",
#     )

#     if uploaded_files:
#         st.markdown(
#             f"""
#             <div class="stat-row">
#               <div class="stat-pill">Files selected &nbsp;<span>{len(uploaded_files)}</span></div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )
#         for f in uploaded_files:
#             st.markdown(
#                 f'<span style="font-family:\'IBM Plex Mono\',monospace;font-size:0.78rem;'
#                 f'color:#8b949e;">✓ {f.name}</span><br>',
#                 unsafe_allow_html=True,
#             )

#         if st.button("Process Batch"):
#             results = []
#             with st.spinner("Matching songs..."):
#                 for uf in uploaded_files:
#                     temp_name = uf.name
#                     with open(temp_name, "wb") as f:
#                         f.write(uf.getbuffer())
#                     audio, sr = load_audio(temp_name)
#                     spec = compute_spectrogram(audio, sr)
#                     peaks = find_peaks(spec)
#                     hashes = generate_hashes(peaks)
#                     result = match_song(hashes, database)
#                     if result is None:
#                         prediction = "No Match"
#                     else:
#                         best_song, _ = result
#                         prediction = os.path.splitext(best_song)[0].replace("_", " ").title()
#                     results.append({"filename": uf.name, "prediction": prediction})

#             import pandas as pd
#             df = pd.DataFrame(results)
#             st.markdown(
#                 '<div class="match-banner">✓ Batch processing complete!</div>',
#                 unsafe_allow_html=True,
#             )
#             st.dataframe(df, use_container_width=True, hide_index=True)
#             csv = df.to_csv(index=False).encode("utf-8")
#             st.download_button(
#                 "Download results.csv",
#                 csv,
#                 file_name="results.csv",
#                 mime="text/csv",
#             )
#     else:
#         st.markdown(
#             '<div class="info-banner">Upload multiple WAV clips above, then click Process Batch.</div>',
#             unsafe_allow_html=True,
#         )

# import os
# import streamlit as st
# import matplotlib
# matplotlib.use("Agg")
# import matplotlib.pyplot as plt
# import numpy as np

# from spectrogram import *
# from peaks import *
# from fingerprint import *
# from matcher import *

# # =====================================
# # PAGE CONFIG & GLOBAL STYLES
# # =====================================
# st.set_page_config(
#     page_title="EE200: Audio Fingerprinting",
#     page_icon="🎵",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# st.markdown(
#     """
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Inter:wght@300;400;500;600&display=swap');

#     html, body, [class*="css"] {
#         font-family: 'Inter', sans-serif;
#         background-color: #0a0d10;
#         color: #c9d1d9;
#     }
#     .stApp { background-color: #0a0d10; }
#     #MainMenu, footer, header { visibility: hidden; }
#     .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1200px; }

#     .page-header {
#         display: flex; align-items: center; gap: 1rem;
#         padding: 0.5rem 0 1.5rem 0;
#         border-bottom: 1px solid #1e2530; margin-bottom: 0.5rem;
#     }
#     .header-icon {
#         background: #0d1117; border: 1px solid #1e2530; border-radius: 8px;
#         padding: 10px 12px; font-size: 1.6rem; line-height: 1;
#     }
#     .header-text h1 {
#         margin: 0; font-size: 1.9rem; font-weight: 700;
#         color: #e6edf3; letter-spacing: -0.5px;
#     }
#     .header-text h1 span { color: #39d353; }
#     .header-text .subtitle {
#         font-family: 'IBM Plex Mono', monospace; font-size: 0.72rem;
#         letter-spacing: 0.12em; color: #484f58; text-transform: uppercase; margin-top: 3px;
#     }
#     .header-text .desc { font-size: 0.88rem; color: #8b949e; margin-top: 4px; }

#     .stTabs [data-baseweb="tab-list"] {
#         background: transparent; border-bottom: 1px solid #1e2530; gap: 0; padding: 0;
#     }
#     .stTabs [data-baseweb="tab"] {
#         font-family: 'IBM Plex Mono', monospace; font-size: 0.78rem;
#         letter-spacing: 0.08em; color: #484f58; background: transparent;
#         border: none; border-bottom: 2px solid transparent;
#         padding: 0.7rem 1.4rem; text-transform: uppercase;
#     }
#     .stTabs [aria-selected="true"] {
#         color: #39d353 !important;
#         border-bottom: 2px solid #39d353 !important;
#         background: transparent !important;
#     }
#     .stTabs [data-baseweb="tab-highlight"] { display: none; }
#     .stTabs [data-baseweb="tab-border"] { display: none; }

#     .section-label {
#         font-family: 'IBM Plex Mono', monospace; font-size: 0.68rem;
#         letter-spacing: 0.14em; color: #484f58; text-transform: uppercase;
#         margin: 1.5rem 0 0.8rem 0; padding-bottom: 0.4rem; border-bottom: 1px solid #1e2530;
#     }
#     .info-banner {
#         background: #0d1117; border: 1px solid #1e2530; border-radius: 6px;
#         padding: 1.2rem 1.5rem; text-align: center; color: #484f58;
#         font-size: 0.88rem; font-family: 'IBM Plex Mono', monospace;
#         margin-bottom: 1.5rem; line-height: 1.8;
#     }
#     .stat-row { display: flex; gap: 10px; margin: 1rem 0; }
#     .stat-pill {
#         background: #0d1117; border: 1px solid #1e2530; border-radius: 6px;
#         padding: 0.5rem 1rem; font-family: 'IBM Plex Mono', monospace;
#         font-size: 0.78rem; color: #8b949e;
#     }
#     .stat-pill span { color: #39d353; font-weight: 600; }

#     .match-banner {
#         background: #0d2119; border: 1px solid #39d353; border-radius: 8px;
#         padding: 1rem 1.4rem; font-size: 1rem; font-weight: 600; color: #39d353;
#         display: flex; align-items: center; gap: 0.6rem; margin: 1rem 0;
#     }
#     .no-match-banner {
#         background: #1a0d0d; border: 1px solid #6e2929; border-radius: 8px;
#         padding: 1rem 1.4rem; font-size: 0.95rem; color: #f85149; margin: 1rem 0;
#     }
#     [data-testid="stFileUploader"] {
#         background: #0d1117; border: 1px dashed #1e2530; border-radius: 8px; padding: 0.5rem;
#     }
#     [data-testid="stFileUploader"]:hover { border-color: #39d353; }

#     .sub-label {
#         font-family: 'IBM Plex Mono', monospace; font-size: 0.72rem;
#         letter-spacing: 0.12em; color: #39d353; text-transform: uppercase;
#         margin: 1.5rem 0 0.5rem 0;
#     }
#     [data-testid="stDataFrame"] {
#         background: #0d1117; border: 1px solid #1e2530; border-radius: 6px;
#     }
#     .stButton > button {
#         background: #0d2119; border: 1px solid #39d353; color: #39d353;
#         font-family: 'IBM Plex Mono', monospace; font-size: 0.8rem;
#         letter-spacing: 0.08em; border-radius: 6px;
#         padding: 0.5rem 1.4rem; transition: background 0.2s;
#     }
#     .stButton > button:hover { background: #163324; border-color: #39d353; color: #39d353; }

#     .offset-row {
#         display: flex; justify-content: space-between; align-items: center;
#         padding: 6px 12px; border-bottom: 1px solid #1e2530;
#         font-family: 'IBM Plex Mono', monospace; font-size: 0.78rem;
#     }
#     .offset-row:last-child { border-bottom: none; }
#     .offset-row .song-name { color: #8b949e; }
#     .offset-row .offset-val { color: #484f58; }
#     .offset-row .match-count { color: #39d353; font-weight: 600; }
#     .offset-table {
#         background: #0d1117; border: 1px solid #1e2530;
#         border-radius: 8px; overflow: hidden; margin-top: 0.5rem;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # =====================================
# # MATPLOTLIB DARK THEME HELPERS
# # =====================================
# def dark_fig(w=10, h=4):
#     fig, ax = plt.subplots(figsize=(w, h))
#     fig.patch.set_facecolor("#0d1117")
#     ax.set_facecolor("#0d1117")
#     ax.tick_params(colors="#484f58", labelsize=8)
#     ax.xaxis.label.set_color("#8b949e")
#     ax.yaxis.label.set_color("#8b949e")
#     ax.title.set_color("#c9d1d9")
#     for spine in ax.spines.values():
#         spine.set_edgecolor("#1e2530")
#     return fig, ax


# def constellation_fig(peaks, title="Constellation Map"):
#     fig, ax = dark_fig(10, 3.5)
#     times = [p[1] for p in peaks]
#     freqs = [p[0] for p in peaks]
#     colours = plt.cm.plasma(np.array(freqs) / (max(freqs) + 1))
#     ax.scatter(times, freqs, s=2, c=colours, alpha=0.8, linewidths=0)
#     ax.set_title(title, fontsize=9)
#     ax.set_xlabel("Time frame", fontsize=8)
#     ax.set_ylabel("Frequency bin", fontsize=8)
#     fig.tight_layout()
#     return fig


# def spectrogram_fig(spec_db):
#     fig, ax = dark_fig(10, 3.5)
#     img = ax.imshow(spec_db, aspect="auto", origin="lower",
#                     cmap="inferno", interpolation="nearest")
#     plt.colorbar(img, ax=ax, pad=0.02).ax.tick_params(colors="#484f58", labelsize=7)
#     ax.set_title("Spectrogram (dB)", fontsize=9)
#     ax.set_xlabel("Time frame", fontsize=8)
#     ax.set_ylabel("Frequency bin", fontsize=8)
#     fig.tight_layout()
#     return fig


# def histogram_fig(song_offsets, best_song):
#     fig, ax = dark_fig(10, 3)
#     ax.bar(list(song_offsets.keys()), list(song_offsets.values()),
#            color="#39d353", width=0.8, alpha=0.85)
#     ax.set_yscale("log")
#     ax.set_title(f"Offset Histogram — {best_song}", fontsize=9)
#     ax.set_xlabel("Offset (frames)", fontsize=8)
#     ax.set_ylabel("Match count", fontsize=8)
#     fig.tight_layout()
#     return fig


# # =====================================
# # PAGE HEADER
# # =====================================
# st.markdown(
#     """
#     <div class="page-header">
#       <div class="header-icon">📊</div>
#       <div class="header-text">
#         <h1><span>EE200</span>: Audio Fingerprinting</h1>
#         <div class="subtitle">Signals, Systems &amp; Networks &nbsp;·&nbsp; Project by Harshita</div>
#         <div class="desc">Index a library of songs as spectrogram fingerprints, then identify any short clip against it.</div>
#       </div>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# # =====================================
# # BUILD DATABASE — cached, runs once
# # =====================================
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# SONGS_DIR = os.path.join(BASE_DIR, "..", "songs")


# @st.cache_resource(show_spinner=False)
# def load_database(songs_dir: str):
#     """
#     Pure computation only — NO st.* calls allowed inside cache_resource.
#     Streamlit runs this exactly once per server process; all subsequent
#     page loads (and every user) get the pre-built result from memory.
#     """
#     _song_hashes = {}
#     _song_peaks_map = {}
#     _errors = []

#     for filename in os.listdir(songs_dir):
#         if not filename.endswith(".wav"):
#             continue
#         path = os.path.join(songs_dir, filename)
#         try:
#             audio, sr = load_audio(path)
#             spec_db = compute_spectrogram(audio, sr)
#             peaks = find_peaks(spec_db)
#             hashes = generate_hashes(peaks)
#             _song_hashes[filename] = hashes
#             _song_peaks_map[filename] = peaks
#         except Exception as e:
#             _errors.append((filename, str(e)))

#     _database = build_database(_song_hashes)
#     return _song_hashes, _song_peaks_map, _database, _errors


# # st.spinner lives OUTSIDE the cached fn — safe to call st.* here
# if "db_loaded" not in st.session_state:
#     with st.spinner("🎵 Indexing song library — this only happens once…"):
#         song_hashes, song_peaks_map, database, load_errors = load_database(SONGS_DIR)
#     st.session_state["db_loaded"] = True
# else:
#     song_hashes, song_peaks_map, database, load_errors = load_database(SONGS_DIR)

# for bad_file, err_msg in load_errors:
#     st.error(f"Failed loading: {bad_file} — {err_msg}")

# # =====================================
# # TABS
# # =====================================
# tab1, tab2, tab3 = st.tabs(["◆ LIBRARY", "◎ IDENTIFY", "▣ BATCH"])

# # ─────────────────────────────────────
# # TAB 1 — LIBRARY
# # ─────────────────────────────────────
# with tab1:
#     st.markdown('<div class="section-label">Library</div>', unsafe_allow_html=True)
#     st.markdown(
#         """
#         <div class="info-banner">
#             Song indexing is managed by the admin.<br>
#             Drop a clip in the Identify tab to test the library.
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
#     st.markdown(
#         f'<div class="section-label">In The Database &nbsp;·&nbsp; {len(song_hashes)} songs indexed</div>',
#         unsafe_allow_html=True,
#     )

#     songs_list = list(song_hashes.keys())
#     cols_per_row = 4

#     for row_start in range(0, len(songs_list), cols_per_row):
#         row_songs = songs_list[row_start : row_start + cols_per_row]
#         cols = st.columns(cols_per_row)
#         for col, song in zip(cols, row_songs):
#             with col:
#                 peaks = song_peaks_map.get(song, [])
#                 if peaks:
#                     thumb_fig, thumb_ax = plt.subplots(figsize=(3, 2))
#                     thumb_fig.patch.set_facecolor("#0d1117")
#                     thumb_ax.set_facecolor("#0d1117")
#                     times = [p[1] for p in peaks]
#                     freqs = [p[0] for p in peaks]
#                     colours = plt.cm.plasma(np.array(freqs) / (max(freqs) + 1))
#                     thumb_ax.scatter(times, freqs, s=1, c=colours, alpha=0.7)
#                     thumb_ax.axis("off")
#                     thumb_fig.tight_layout(pad=0)
#                     st.pyplot(thumb_fig, use_container_width=True)
#                     plt.close(thumb_fig)

#                 display_name = os.path.splitext(song)[0].replace("_", " ").title()
#                 st.markdown(
#                     f"""
#                     <div style="padding:6px 2px 10px 2px;">
#                       <div style="font-size:0.84rem;font-weight:600;color:#e6edf3;
#                                   white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">
#                         {display_name}
#                       </div>
#                       <div style="font-family:'IBM Plex Mono',monospace;font-size:0.71rem;
#                                   color:#484f58;margin-top:3px;">
#                         {len(song_hashes[song]):,} hashes
#                       </div>
#                     </div>
#                     """,
#                     unsafe_allow_html=True,
#                 )

# # ─────────────────────────────────────
# # TAB 2 — IDENTIFY
# # ─────────────────────────────────────
# with tab2:
#     st.markdown('<div class="section-label">Identify Song</div>', unsafe_allow_html=True)

#     # --- Sample clips ---
#     SAMPLES_DIR = os.path.join(BASE_DIR, "..", "samples")
#     if os.path.isdir(SAMPLES_DIR):
#         sample_files = sorted(
#             f for f in os.listdir(SAMPLES_DIR) if f.endswith(".wav")
#         )
#         if sample_files:
#             st.markdown('<div class="section-label">Or Try A Sample</div>', unsafe_allow_html=True)

#     selected_sample = None
#     if os.path.isdir(SAMPLES_DIR) and sample_files:
#         for sample in sample_files:
#             sample_path = os.path.join(SAMPLES_DIR, sample)
#             col1, col2 = st.columns([5, 1])
#             with col1:
#                 st.audio(sample_path)
#             with col2:
#                 if st.button("Try", key=f"sample_{sample}"):
#                     selected_sample = sample_path

#     uploaded_file = st.file_uploader(
#         "Upload a WAV clip to identify",
#         type=["wav"],
#         label_visibility="collapsed",
#     )

#     query_path = None
#     if uploaded_file is not None:
#         with open("temp_query.wav", "wb") as f:
#             f.write(uploaded_file.getbuffer())
#         query_path = "temp_query.wav"
#     elif selected_sample:
#         query_path = selected_sample

#     if query_path is None:
#         st.markdown(
#             '<div class="info-banner">Upload a WAV file above, or try one of the sample clips.</div>',
#             unsafe_allow_html=True,
#         )
#         st.stop()

#     query_audio, query_sr = load_audio(query_path)
#     query_spec = compute_spectrogram(query_audio, query_sr)
#     query_peaks = find_peaks(query_spec)
#     query_hashes = generate_hashes(query_peaks)

#     # Stats
#     st.markdown(
#         f"""
#         <div class="stat-row">
#           <div class="stat-pill">Peaks &nbsp;<span>{len(query_peaks):,}</span></div>
#           <div class="stat-pill">Query hashes &nbsp;<span>{len(query_hashes):,}</span></div>
#           <div class="stat-pill">DB entries &nbsp;<span>{len(database):,}</span></div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     col_a, col_b = st.columns(2)
#     with col_a:
#         st.markdown('<div class="sub-label">Spectrogram</div>', unsafe_allow_html=True)
#         st.pyplot(spectrogram_fig(query_spec), use_container_width=True)
#     with col_b:
#         st.markdown('<div class="sub-label">Constellation Map</div>', unsafe_allow_html=True)
#         st.pyplot(constellation_fig(query_peaks), use_container_width=True)

#     # Match
#     result = match_song(query_hashes, database)
#     st.markdown('<div class="section-label">Match Result</div>', unsafe_allow_html=True)

#     if result is None:
#         st.markdown(
#             '<div class="no-match-banner">✗ No match found in the library.</div>',
#             unsafe_allow_html=True,
#         )
#     else:
#         best_song, offset_counts = result
#         display_best = os.path.splitext(best_song)[0].replace("_", " ").title()

#         st.markdown(
#             f'<div class="match-banner">🎵 {display_best}</div>',
#             unsafe_allow_html=True,
#         )

#         # Candidate scores
#         candidate_scores = {}
#         for (song, offset), count in offset_counts.items():
#             candidate_scores[song] = candidate_scores.get(song, 0) + count
#         candidate_scores = sorted(candidate_scores.items(), key=lambda x: x[1], reverse=True)

#         st.markdown('<div class="section-label">Candidate Scores</div>', unsafe_allow_html=True)
#         top_score = candidate_scores[0][1] if candidate_scores else 1
#         for song, score in candidate_scores[:5]:
#             st.write(os.path.splitext(song)[0].replace("_", " ").title())
#             st.progress(score / top_score)

#         col_c, col_d = st.columns(2)
#         with col_c:
#             st.markdown('<div class="sub-label">Top Offset Matches</div>', unsafe_allow_html=True)
#             top_matches = sorted(offset_counts.items(), key=lambda x: x[1], reverse=True)[:10]
#             rows_html = "".join(
#                 f"""
#                 <div class="offset-row">
#                   <span class="song-name">{os.path.splitext(s)[0]}</span>
#                   <span class="offset-val">+{int(o)}</span>
#                   <span class="match-count">{c}</span>
#                 </div>
#                 """
#                 for (s, o), c in top_matches
#             )
#             st.markdown(f'<div class="offset-table">{rows_html}</div>', unsafe_allow_html=True)

#         with col_d:
#             st.markdown('<div class="sub-label">Offset Histogram</div>', unsafe_allow_html=True)
#             song_offsets = {
#                 offset: count
#                 for (song, offset), count in offset_counts.items()
#                 if song == best_song
#             }
#             st.pyplot(histogram_fig(song_offsets, display_best), use_container_width=True)

# # ─────────────────────────────────────
# # TAB 3 — BATCH
# # ─────────────────────────────────────
# with tab3:
#     st.markdown('<div class="section-label">Batch Identification</div>', unsafe_allow_html=True)

#     uploaded_files = st.file_uploader(
#         "Upload multiple WAV clips",
#         type=["wav"],
#         accept_multiple_files=True,
#         label_visibility="collapsed",
#     )

#     if uploaded_files:
#         st.markdown(
#             f"""
#             <div class="stat-row">
#               <div class="stat-pill">Files selected &nbsp;<span>{len(uploaded_files)}</span></div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )
#         for f in uploaded_files:
#             st.markdown(
#                 f'<span style="font-family:\'IBM Plex Mono\',monospace;font-size:0.78rem;'
#                 f'color:#8b949e;">✓ {f.name}</span><br>',
#                 unsafe_allow_html=True,
#             )

#         if st.button("Process Batch"):
#             results = []
#             progress_bar = st.progress(0, text="Starting…")
#             total = len(uploaded_files)

#             for i, uf in enumerate(uploaded_files):
#                 progress_bar.progress(
#                     (i + 1) / total,
#                     text=f"Matching {i + 1}/{total}: {uf.name}",
#                 )
#                 temp_name = f"batch_temp_{uf.name}"
#                 with open(temp_name, "wb") as f:
#                     f.write(uf.getbuffer())
#                 audio, sr = load_audio(temp_name)
#                 spec = compute_spectrogram(audio, sr)
#                 peaks = find_peaks(spec)
#                 hashes = generate_hashes(peaks)
#                 result = match_song(hashes, database)
#                 if result is None:
#                     prediction = "No Match"
#                 else:
#                     best_song, _ = result
#                     prediction = os.path.splitext(best_song)[0].replace("_", " ").title()
#                 results.append({"filename": uf.name, "prediction": prediction})
#                 try:
#                     os.remove(temp_name)
#                 except OSError:
#                     pass

#             progress_bar.empty()

#             import pandas as pd
#             df = pd.DataFrame(results)
#             st.markdown(
#                 '<div class="match-banner">✓ Batch processing complete!</div>',
#                 unsafe_allow_html=True,
#             )
#             st.dataframe(df, use_container_width=True, hide_index=True)
#             csv = df.to_csv(index=False).encode("utf-8")
#             st.download_button(
#                 "Download results.csv",
#                 csv,
#                 file_name="results.csv",
#                 mime="text/csv",
#             )
#     else:
#         st.markdown(
#             '<div class="info-banner">Upload multiple WAV clips above, then click Process Batch.</div>',
#             unsafe_allow_html=True,
#         )

import os
import streamlit as st
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from spectrogram import *
from peaks import *
from fingerprint import *
from matcher import *

# =====================================
# PAGE CONFIG & GLOBAL STYLES
# =====================================
st.set_page_config(
    page_title="EE200: Audio Fingerprinting",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Inter:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #0a0d10;
        color: #c9d1d9;
    }
    .stApp { background-color: #0a0d10; }
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1200px; }

    .page-header {
        display: flex; align-items: center; gap: 1rem;
        padding: 0.5rem 0 1.5rem 0;
        border-bottom: 1px solid #1e2530; margin-bottom: 0.5rem;
    }
    .header-icon {
        background: #0d1117; border: 1px solid #1e2530; border-radius: 8px;
        padding: 10px 12px; font-size: 1.6rem; line-height: 1;
    }
    .header-text h1 {
        margin: 0; font-size: 1.9rem; font-weight: 700;
        color: #e6edf3; letter-spacing: -0.5px;
    }
    .header-text h1 span { color: #39d353; }
    .header-text .subtitle {
        font-family: 'IBM Plex Mono', monospace; font-size: 0.72rem;
        letter-spacing: 0.12em; color: #484f58; text-transform: uppercase; margin-top: 3px;
    }
    .header-text .desc { font-size: 0.88rem; color: #8b949e; margin-top: 4px; }

    .stTabs [data-baseweb="tab-list"] {
        background: transparent; border-bottom: 1px solid #1e2530; gap: 0; padding: 0;
    }
    .stTabs [data-baseweb="tab"] {
        font-family: 'IBM Plex Mono', monospace; font-size: 0.78rem;
        letter-spacing: 0.08em; color: #484f58; background: transparent;
        border: none; border-bottom: 2px solid transparent;
        padding: 0.7rem 1.4rem; text-transform: uppercase;
    }
    .stTabs [aria-selected="true"] {
        color: #39d353 !important;
        border-bottom: 2px solid #39d353 !important;
        background: transparent !important;
    }
    .stTabs [data-baseweb="tab-highlight"] { display: none; }
    .stTabs [data-baseweb="tab-border"] { display: none; }

    .section-label {
        font-family: 'IBM Plex Mono', monospace; font-size: 0.68rem;
        letter-spacing: 0.14em; color: #484f58; text-transform: uppercase;
        margin: 1.5rem 0 0.8rem 0; padding-bottom: 0.4rem; border-bottom: 1px solid #1e2530;
    }
    .info-banner {
        background: #0d1117; border: 1px solid #1e2530; border-radius: 6px;
        padding: 1.2rem 1.5rem; text-align: center; color: #484f58;
        font-size: 0.88rem; font-family: 'IBM Plex Mono', monospace;
        margin-bottom: 1.5rem; line-height: 1.8;
    }
    .stat-row { display: flex; gap: 10px; margin: 1rem 0; }
    .stat-pill {
        background: #0d1117; border: 1px solid #1e2530; border-radius: 6px;
        padding: 0.5rem 1rem; font-family: 'IBM Plex Mono', monospace;
        font-size: 0.78rem; color: #8b949e;
    }
    .stat-pill span { color: #39d353; font-weight: 600; }

    .match-banner {
        background: #0d2119; border: 1px solid #39d353; border-radius: 8px;
        padding: 1rem 1.4rem; font-size: 1rem; font-weight: 600; color: #39d353;
        display: flex; align-items: center; gap: 0.6rem; margin: 1rem 0;
    }
    .no-match-banner {
        background: #1a0d0d; border: 1px solid #6e2929; border-radius: 8px;
        padding: 1rem 1.4rem; font-size: 0.95rem; color: #f85149; margin: 1rem 0;
    }
    [data-testid="stFileUploader"] {
        background: #0d1117; border: 1px dashed #1e2530; border-radius: 8px; padding: 0.5rem;
    }
    [data-testid="stFileUploader"]:hover { border-color: #39d353; }

    .sub-label {
        font-family: 'IBM Plex Mono', monospace; font-size: 0.72rem;
        letter-spacing: 0.12em; color: #39d353; text-transform: uppercase;
        margin: 1.5rem 0 0.5rem 0;
    }
    [data-testid="stDataFrame"] {
        background: #0d1117; border: 1px solid #1e2530; border-radius: 6px;
    }
    .stButton > button {
        background: #0d2119; border: 1px solid #39d353; color: #39d353;
        font-family: 'IBM Plex Mono', monospace; font-size: 0.8rem;
        letter-spacing: 0.08em; border-radius: 6px;
        padding: 0.5rem 1.4rem; transition: background 0.2s;
    }
    .stButton > button:hover { background: #163324; border-color: #39d353; color: #39d353; }

    .offset-row {
        display: flex; justify-content: space-between; align-items: center;
        padding: 6px 12px; border-bottom: 1px solid #1e2530;
        font-family: 'IBM Plex Mono', monospace; font-size: 0.78rem;
    }
    .offset-row:last-child { border-bottom: none; }
    .offset-row .song-name { color: #8b949e; }
    .offset-row .offset-val { color: #484f58; }
    .offset-row .match-count { color: #39d353; font-weight: 600; }
    .offset-table {
        background: #0d1117; border: 1px solid #1e2530;
        border-radius: 8px; overflow: hidden; margin-top: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =====================================
# MATPLOTLIB DARK THEME HELPERS
# =====================================
def dark_fig(w=10, h=4):
    fig, ax = plt.subplots(figsize=(w, h))
    fig.patch.set_facecolor("#0d1117")
    ax.set_facecolor("#0d1117")
    ax.tick_params(colors="#484f58", labelsize=8)
    ax.xaxis.label.set_color("#8b949e")
    ax.yaxis.label.set_color("#8b949e")
    ax.title.set_color("#c9d1d9")
    for spine in ax.spines.values():
        spine.set_edgecolor("#1e2530")
    return fig, ax


def constellation_fig(peaks, title="Constellation Map"):
    fig, ax = dark_fig(10, 3.5)
    times = [p[1] for p in peaks]
    freqs = [p[0] for p in peaks]
    colours = plt.cm.plasma(np.array(freqs) / (max(freqs) + 1))
    ax.scatter(times, freqs, s=2, c=colours, alpha=0.8, linewidths=0)
    ax.set_title(title, fontsize=9)
    ax.set_xlabel("Time frame", fontsize=8)
    ax.set_ylabel("Frequency bin", fontsize=8)
    fig.tight_layout()
    return fig


def spectrogram_fig(spec_db):
    fig, ax = dark_fig(10, 3.5)
    img = ax.imshow(spec_db, aspect="auto", origin="lower",
                    cmap="inferno", interpolation="nearest")
    plt.colorbar(img, ax=ax, pad=0.02).ax.tick_params(colors="#484f58", labelsize=7)
    ax.set_title("Spectrogram (dB)", fontsize=9)
    ax.set_xlabel("Time frame", fontsize=8)
    ax.set_ylabel("Frequency bin", fontsize=8)
    fig.tight_layout()
    return fig


def histogram_fig(song_offsets, best_song):
    fig, ax = dark_fig(10, 3)
    ax.bar(list(song_offsets.keys()), list(song_offsets.values()),
           color="#39d353", width=0.8, alpha=0.85)
    ax.set_yscale("log")
    ax.set_title(f"Offset Histogram — {best_song}", fontsize=9)
    ax.set_xlabel("Offset (frames)", fontsize=8)
    ax.set_ylabel("Match count", fontsize=8)
    fig.tight_layout()
    return fig


# =====================================
# PAGE HEADER
# =====================================
st.markdown(
    """
    <div class="page-header">
      <div class="header-icon">📊</div>
      <div class="header-text">
        <h1><span>EE200</span>: Audio Fingerprinting</h1>
        <div class="subtitle">Signals, Systems &amp; Networks &nbsp;·&nbsp; Project by Harshita</div>
        <div class="desc">Index a library of songs as spectrogram fingerprints, then identify any short clip against it.</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =====================================
# BUILD DATABASE — cached, runs once
# =====================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SONGS_DIR = os.path.join(BASE_DIR, "..", "songs")


@st.cache_resource(show_spinner=False)
def load_database(songs_dir: str):
    """
    Pure computation only — NO st.* calls allowed inside cache_resource.
    Streamlit runs this exactly once per server process; all subsequent
    page loads (and every user) get the pre-built result from memory.
    """
    _song_hashes = {}
    _song_peaks_map = {}
    _errors = []

    for filename in os.listdir(songs_dir):
        if not filename.endswith(".wav"):
            continue
        path = os.path.join(songs_dir, filename)
        try:
            audio, sr = load_audio(path)
            spec_db = compute_spectrogram(audio, sr)
            peaks = find_peaks(spec_db)
            hashes = generate_hashes(peaks)
            _song_hashes[filename] = hashes
            _song_peaks_map[filename] = peaks
        except Exception as e:
            _errors.append((filename, str(e)))

    _database = build_database(_song_hashes)
    return _song_hashes, _song_peaks_map, _database, _errors


# st.spinner lives OUTSIDE the cached fn — safe to call st.* here
if "db_loaded" not in st.session_state:
    with st.spinner("🎵 Indexing song library — this only happens once…"):
        song_hashes, song_peaks_map, database, load_errors = load_database(SONGS_DIR)
    st.session_state["db_loaded"] = True
else:
    song_hashes, song_peaks_map, database, load_errors = load_database(SONGS_DIR)

for bad_file, err_msg in load_errors:
    st.error(f"Failed loading: {bad_file} — {err_msg}")

# =====================================
# TABS
# =====================================
tab1, tab2, tab3 = st.tabs(["◆ LIBRARY", "◎ IDENTIFY", "▣ BATCH"])

# ─────────────────────────────────────
# TAB 1 — LIBRARY
# ─────────────────────────────────────
with tab1:
    st.markdown('<div class="section-label">Library</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="info-banner">
            Song indexing is managed by the admin.<br>
            Drop a clip in the Identify tab to test the library.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="section-label">In The Database &nbsp;·&nbsp; {len(song_hashes)} songs indexed</div>',
        unsafe_allow_html=True,
    )

    songs_list = list(song_hashes.keys())
    cols_per_row = 4

    for row_start in range(0, len(songs_list), cols_per_row):
        row_songs = songs_list[row_start : row_start + cols_per_row]
        cols = st.columns(cols_per_row)
        for col, song in zip(cols, row_songs):
            with col:
                peaks = song_peaks_map.get(song, [])
                if peaks:
                    thumb_fig, thumb_ax = plt.subplots(figsize=(3, 2))
                    thumb_fig.patch.set_facecolor("#0d1117")
                    thumb_ax.set_facecolor("#0d1117")
                    times = [p[1] for p in peaks]
                    freqs = [p[0] for p in peaks]
                    colours = plt.cm.plasma(np.array(freqs) / (max(freqs) + 1))
                    thumb_ax.scatter(times, freqs, s=1, c=colours, alpha=0.7)
                    thumb_ax.axis("off")
                    thumb_fig.tight_layout(pad=0)
                    st.pyplot(thumb_fig, use_container_width=True)
                    plt.close(thumb_fig)

                display_name = os.path.splitext(song)[0].replace("_", " ").title()
                st.markdown(
                    f"""
                    <div style="padding:6px 2px 10px 2px;">
                      <div style="font-size:0.84rem;font-weight:600;color:#e6edf3;
                                  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">
                        {display_name}
                      </div>
                      <div style="font-family:'IBM Plex Mono',monospace;font-size:0.71rem;
                                  color:#484f58;margin-top:3px;">
                        {len(song_hashes[song]):,} hashes
                      </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

# ─────────────────────────────────────
# TAB 2 — IDENTIFY
# ─────────────────────────────────────
with tab2:
    st.markdown('<div class="section-label">Identify Song</div>', unsafe_allow_html=True)

    # --- Sample clips ---
    SAMPLES_DIR = os.path.join(BASE_DIR, "..", "samples")
    if os.path.isdir(SAMPLES_DIR):
        sample_files = sorted(
            f for f in os.listdir(SAMPLES_DIR) if f.endswith(".wav")
        )
        if sample_files:
            st.markdown('<div class="section-label">Or Try A Sample</div>', unsafe_allow_html=True)

    selected_sample = None
    if os.path.isdir(SAMPLES_DIR) and sample_files:
        for sample in sample_files:
            sample_path = os.path.join(SAMPLES_DIR, sample)
            col1, col2 = st.columns([5, 1])
            with col1:
                st.audio(sample_path)
            with col2:
                if st.button("Try", key=f"sample_{sample}"):
                    selected_sample = sample_path

    uploaded_file = st.file_uploader(
        "Upload a WAV clip to identify",
        type=["wav"],
        label_visibility="collapsed",
    )

    query_path = None
    if uploaded_file is not None:
        with open("temp_query.wav", "wb") as f:
            f.write(uploaded_file.getbuffer())
        query_path = "temp_query.wav"
    elif selected_sample:
        query_path = selected_sample

    if query_path is None:
        st.markdown(
            '<div class="info-banner">Upload a WAV file above, or try one of the sample clips.</div>',
            unsafe_allow_html=True,
        )
        st.stop()

    query_audio, query_sr = load_audio(query_path)
    query_spec = compute_spectrogram(query_audio, query_sr)
    query_peaks = find_peaks(query_spec)
    query_hashes = generate_hashes(query_peaks)

    # Stats
    st.markdown(
        f"""
        <div class="stat-row">
          <div class="stat-pill">Peaks &nbsp;<span>{len(query_peaks):,}</span></div>
          <div class="stat-pill">Query hashes &nbsp;<span>{len(query_hashes):,}</span></div>
          <div class="stat-pill">DB entries &nbsp;<span>{len(database):,}</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<div class="sub-label">Spectrogram</div>', unsafe_allow_html=True)
        st.pyplot(spectrogram_fig(query_spec), use_container_width=True)
    with col_b:
        st.markdown('<div class="sub-label">Constellation Map</div>', unsafe_allow_html=True)
        st.pyplot(constellation_fig(query_peaks), use_container_width=True)

    # Match
    result = match_song(query_hashes, database)
    st.markdown('<div class="section-label">Match Result</div>', unsafe_allow_html=True)

    if result is None:
        st.markdown(
            '<div class="no-match-banner">✗ No match found in the library.</div>',
            unsafe_allow_html=True,
        )
    else:
        best_song, offset_counts = result
        display_best = os.path.splitext(best_song)[0].replace("_", " ").title()

        st.markdown(
            f'<div class="match-banner">🎵 {display_best}</div>',
            unsafe_allow_html=True,
        )

        # Candidate scores
        candidate_scores = {}
        for (song, offset), count in offset_counts.items():
            candidate_scores[song] = candidate_scores.get(song, 0) + count
        candidate_scores = sorted(candidate_scores.items(), key=lambda x: x[1], reverse=True)

        st.markdown('<div class="section-label">Candidate Scores</div>', unsafe_allow_html=True)
        top_score = candidate_scores[0][1] if candidate_scores else 1
        for song, score in candidate_scores[:5]:
            st.write(os.path.splitext(song)[0].replace("_", " ").title())
            st.progress(score / top_score)

        col_c, col_d = st.columns(2)
        with col_c:
            st.markdown('<div class="sub-label">Top Offset Matches</div>', unsafe_allow_html=True)
            top_matches = sorted(offset_counts.items(), key=lambda x: x[1], reverse=True)[:10]
            rows_html = "".join(
                f"""
                <div class="offset-row">
                  <span class="song-name">{os.path.splitext(s)[0]}</span>
                  <span class="offset-val">+{int(o)}</span>
                  <span class="match-count">{c}</span>
                </div>
                """
                for (s, o), c in top_matches
            )
            st.markdown(f'<div class="offset-table">{rows_html}</div>', unsafe_allow_html=True)

        with col_d:
            st.markdown('<div class="sub-label">Offset Histogram</div>', unsafe_allow_html=True)
            song_offsets = {
                offset: count
                for (song, offset), count in offset_counts.items()
                if song == best_song
            }
            st.pyplot(histogram_fig(song_offsets, display_best), use_container_width=True)

# ─────────────────────────────────────
# TAB 3 — BATCH
# ─────────────────────────────────────
with tab3:
    st.markdown('<div class="section-label">Batch</div>', unsafe_allow_html=True)
    st.markdown('<div class="batch-title">Identify many clips at once</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="batch-desc">
            Upload a set of query clips. Each is identified against the
            <strong>currently indexed library</strong>, and the results are written to a
            standardised <code>results.csv</code> with columns <code>filename</code>,
            <code>prediction</code>. The <code>prediction</code> is the matched track's
            filename without its extension, or <code>none</code> when no candidate
            clears the confidence threshold.
        </div>
        """,
        unsafe_allow_html=True,
    )

    uploaded_files = st.file_uploader(
        "Upload WAV clips",
        type=["wav"],
        accept_multiple_files=True,
        label_visibility="collapsed",
    )

    if uploaded_files:
        if st.button("Run batch"):
            results = []
            progress_bar = st.progress(0, text="Starting…")
            total = len(uploaded_files)

            for i, uf in enumerate(uploaded_files):
                progress_bar.progress(
                    (i + 1) / total,
                    text=f"Matching {i + 1}/{total}: {uf.name}",
                )
                temp_name = f"batch_temp_{uf.name}"
                with open(temp_name, "wb") as f:
                    f.write(uf.getbuffer())
                audio, sr = load_audio(temp_name)
                spec = compute_spectrogram(audio, sr)
                peaks = find_peaks(spec)
                hashes = generate_hashes(peaks)
                match_result = match_song(hashes, database)
                if match_result is None:
                    prediction = "none"
                else:
                    best_song, _ = match_result
                    prediction = os.path.splitext(best_song)[0].replace("_", " ").title()
                results.append({"filename": uf.name, "prediction": prediction})
                try:
                    os.remove(temp_name)
                except OSError:
                    pass

            progress_bar.empty()
            st.session_state["batch_results"] = results

    # Show results from session state so they persist after button click
    if "batch_results" in st.session_state and st.session_state["batch_results"]:
        results = st.session_state["batch_results"]
        matched = sum(1 for r in results if r["prediction"] != "none")
        none_count = len(results) - matched

        # Custom results table
        st.markdown('<div class="section-label">Results</div>', unsafe_allow_html=True)

        rows_html = ""
        for r in results:
            pred_class = "pred-none" if r["prediction"] == "none" else "pred-match"
            rows_html += f"""
            <tr>
              <td>{r['filename']}</td>
              <td class="{pred_class}">{r['prediction']}</td>
            </tr>"""

        st.markdown(
            f"""
            <div class="results-table-wrap">
              <table class="results-table">
                <thead>
                  <tr><th>File</th><th>Prediction</th></tr>
                </thead>
                <tbody>{rows_html}</tbody>
              </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Summary line
        st.markdown(
            f"""
            <div class="batch-summary">
              <span>{matched} / {len(results)}</span> clips matched to a track
              ({none_count} returned <code>none</code>).
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Download
        import pandas as pd
        csv = pd.DataFrame(results).to_csv(index=False).encode("utf-8")
        st.download_button(
            "↓ Download results.csv",
            csv,
            file_name="results.csv",
            mime="text/csv",
        )
    elif not uploaded_files:
        st.markdown(
            '<div class="info-banner">Upload WAV clips above, then click Run batch.</div>',
            unsafe_allow_html=True,
        )