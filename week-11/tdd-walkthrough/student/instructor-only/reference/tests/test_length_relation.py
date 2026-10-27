from playlist.lengths import length_label
from relations import reflexive_failure, symmetric_failure, transitive_failure

LENGTHS = [0, 90, 179, 180, 240, 299, 300, 450, 599, 600, 1800, 3600]


def same_label(a, b):
    return length_label(a) == length_label(b)


def test_same_label_is_reflexive():
    assert reflexive_failure(same_label, LENGTHS) is None


def test_same_label_is_symmetric():
    assert symmetric_failure(same_label, LENGTHS) is None


def test_same_label_is_transitive():
    assert transitive_failure(same_label, LENGTHS) is None


def test_the_labels_cut_the_lengths_into_four_bins():
    bins = {}
    for seconds in LENGTHS:
        bins.setdefault(length_label(seconds), []).append(seconds)
    assert sorted(bins) == ["epic", "long", "normal", "short"]
    assert bins["normal"] == [180, 240, 299]
