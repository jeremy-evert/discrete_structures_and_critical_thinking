from fixtures import RECORDS
from merger.pipeline import merge_duplicates


def test_duplicates_are_merged_and_others_left_alone():
    merged = merge_duplicates(RECORDS)
    # The merged record keeps the name of its lowest-id member.
    assert [(m.ids, m.name) for m in merged] == [
        ((1,), "Jon Smith"),
        ((2, 3), "John Smith"),
        ((4,), "Maya Smith"),
        ((5,), "Maria Garcia"),
    ]


def test_every_input_record_ends_up_in_exactly_one_merged_record():
    merged = merge_duplicates(RECORDS)
    all_ids = sorted(i for m in merged for i in m.ids)
    assert all_ids == sorted(r.id for r in RECORDS)


def test_result_does_not_depend_on_input_order():
    assert merge_duplicates(RECORDS) == merge_duplicates(list(reversed(RECORDS)))
