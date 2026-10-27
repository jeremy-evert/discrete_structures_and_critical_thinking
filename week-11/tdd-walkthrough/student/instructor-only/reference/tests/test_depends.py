from playlist.depends import leaves_first

# "X": {"Y"} means "X needs Y". Written dependents-first on purpose.
PLAYLIST_GRAPH = {
    "clean_playlist": {"song_key"},
    "is_duplicate": {"same_song"},
    "same_song": {"song_key"},
    "song_key": set(),
    "looks_alike": set(),
    "cluster_by_chain": set(),
    "compare": set(),
    "length_label": set(),
}


def test_every_function_comes_after_the_things_it_needs():
    order = leaves_first(PLAYLIST_GRAPH)
    for function, needs in PLAYLIST_GRAPH.items():
        for needed in needs:
            assert order.index(needed) < order.index(function), (
                "{0} is listed before {1}, which it needs".format(function, needed)
            )


def test_every_function_appears_exactly_once():
    order = leaves_first(PLAYLIST_GRAPH)
    assert sorted(order) == sorted(PLAYLIST_GRAPH)
