from collections import defaultdict


def match_song(query_hashes,
               database,
               min_votes=20):

    offset_counts = defaultdict(int)

    for hash_key, query_time in query_hashes:

        if hash_key not in database:
            continue

        for song_name, song_time in database[hash_key]:

            offset = song_time - query_time

            offset_counts[(song_name, offset)] += 1

    if not offset_counts:
        return None

    best_match = max(
        offset_counts,
        key=offset_counts.get
    )

    best_song = best_match[0]

    best_votes = offset_counts[best_match]

    if best_votes < min_votes:
        return None

    return best_song, best_votes