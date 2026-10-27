from fixtures import GLASS_HARBOR, NIGHT_BUS, PAPER_MOONS, SLOW_ORBIT_1, SLOW_ORBIT_2, SLOW_ORBIT_3, TRACKS
from playlist.grouping import cluster_by_chain
from playlist.songs import looks_alike


def test_a_chain_of_matches_lands_in_one_cluster():
    clusters = cluster_by_chain(TRACKS, looks_alike)
    assert [SLOW_ORBIT_1, SLOW_ORBIT_2, SLOW_ORBIT_3] in clusters


def test_unrelated_tracks_stay_alone():
    clusters = cluster_by_chain(TRACKS, looks_alike)
    assert [PAPER_MOONS] in clusters
    assert [GLASS_HARBOR] in clusters
    assert [NIGHT_BUS] in clusters


def test_every_track_lands_in_exactly_one_cluster():
    clusters = cluster_by_chain(TRACKS, looks_alike)
    assert sorted(t.id for c in clusters for t in c) == [1, 2, 3, 4, 5, 6]
