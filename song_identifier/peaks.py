# peaks.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter


def find_peaks(spec_db,
               neighborhood_size=20,
               threshold=-40):
    """
    Find local maxima in spectrogram.

    Parameters
    ----------
    spec_db : spectrogram in dB

    neighborhood_size :
        size of area used to check local maxima

    threshold :
        minimum intensity (dB)

    Returns
    -------
    peaks : list of (freq_bin, time_bin)
    """

    local_max = maximum_filter(
        spec_db,
        size=neighborhood_size
    )

    peak_mask = (
        (spec_db == local_max)
        &
        (spec_db > threshold)
    )

    freq_bins, time_bins = np.where(peak_mask)

    peaks = list(zip(freq_bins, time_bins))

    return peaks


def plot_constellation(spec_db, peaks):
    """
    Plot constellation map.
    """

    plt.figure(figsize=(12, 6))

    plt.imshow(
        spec_db,
        aspect='auto',
        origin='lower'
    )

    if len(peaks) > 0:

        freqs = [p[0] for p in peaks]
        times = [p[1] for p in peaks]

        plt.scatter(
            
            times,
            freqs,
            s=40,
            c='red'
            
        )

    plt.title("Constellation Map")
    plt.xlabel("Time Bin")
    plt.ylabel("Frequency Bin")

    plt.show()