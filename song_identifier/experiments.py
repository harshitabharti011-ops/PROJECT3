# import os
# import numpy as np
# import matplotlib.pyplot as plt
# import librosa
# import librosa.display

# # =====================================
# # LOAD SONG
# # =====================================

# BASE_DIR = os.path.dirname(
#     os.path.abspath(__file__)
# )

# song_path = os.path.join(
#     BASE_DIR,
#     "..",
#     "songs",
#     "Under Pressure.wav"
# )

# audio, sr = librosa.load(
#     song_path,
#     sr=None
# )

# # # =====================================
# # # SHORT WINDOW
# # # =====================================

# # n_fft = 512

# # D = librosa.amplitude_to_db(
# #     np.abs(
# #         librosa.stft(
# #             audio,
# #             n_fft=n_fft
# #         )
# #     ),
# #     ref=np.max
# # )

# # plt.figure(figsize=(12,5))

# # librosa.display.specshow(
# #     D,
# #     sr=sr,
# #     x_axis="time",
# #     y_axis="hz"
# # )

# # plt.colorbar(format="%+2.0f dB")

# # plt.title(
# #     "Short Window Spectrogram (n_fft = 512)"
# # )

# # plt.tight_layout()
# # plt.show()

# # =====================================
# # LONG WINDOW
# # =====================================

# n_fft = 4096

# D = librosa.amplitude_to_db(
#     np.abs(
#         librosa.stft(
#             audio,
#             n_fft=n_fft
#         )
#     ),
#     ref=np.max
# )

# plt.figure(figsize=(12,5))

# librosa.display.specshow(
#     D,
#     sr=sr,
#     x_axis="time",
#     y_axis="hz"
# )

# plt.colorbar(format="%+2.0f dB")

# plt.title(
#     "Long Window Spectrogram (n_fft = 4096)"
# )

# plt.tight_layout()
# plt.show()