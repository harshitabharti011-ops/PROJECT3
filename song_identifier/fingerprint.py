# fingerprint.py

from collections import defaultdict


def generate_hashes(
        peaks,
        fan_value=5):
    """
    Generate fingerprints from peaks.

    Parameters
    ----------
    peaks : list of (freq_bin, time_bin)

    fan_value :
        number of future peaks to pair with

    Returns
    -------
    hashes :
        list of
        (hash_key, time_anchor)
    """

    hashes = []

    for i in range(len(peaks)):

        freq1, time1 = peaks[i]

        for j in range(1, fan_value + 1):

            if i + j >= len(peaks):
                break

            freq2, time2 = peaks[i + j]

            delta_t = time2 - time1

            if delta_t <= 0:
                continue

            hash_key = (
                freq1,
                freq2,
                delta_t
            )

            hashes.append(
                (
                    hash_key,
                    time1
                )
            )

    return hashes


def build_database(song_hashes):
    """
    Build searchable database.

    Parameters
    ----------
    song_hashes :

    {
      song_name :
      hashes
    }

    Returns
    -------
    database
    """

    database = defaultdict(list)

    for song_name, hashes in song_hashes.items():

        for hash_key, time_anchor in hashes:

            database[hash_key].append(
                (
                    song_name,
                    time_anchor
                )
            )

    return database