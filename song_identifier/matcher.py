# matcher.py

from collections import defaultdict


def match_song(query_hashes, database):

    offset_counts = defaultdict(int)

    for hash_key, query_time in query_hashes:

        if hash_key not in database:
            continue

        matches = database[hash_key]

        for song_name, song_time in matches:

            offset = song_time - query_time

            offset_counts[(song_name, offset)] += 1

    if not offset_counts:
        return None

    best_match = max(
        offset_counts,
        key=offset_counts.get
    )

    best_song = best_match[0]

    return best_song, offset_counts