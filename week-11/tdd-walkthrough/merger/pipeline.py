from collections import namedtuple

from merger.names import canonical_key

Merged = namedtuple("Merged", ["ids", "name", "email"])


def duplicate_key(record):
    """Two records are duplicates exactly when this key is equal (same rule as is_duplicate)."""
    return (canonical_key(record.name), record.email)


def group_records(records):
    groups = {}
    for record in records:
        groups.setdefault(duplicate_key(record), []).append(record)
    return list(groups.values())


def merge_group(group):
    ordered = sorted(group, key=lambda r: r.id)
    return Merged(ids=tuple(r.id for r in ordered), name=ordered[0].name, email=ordered[0].email)


def merge_duplicates(records):
    return sorted((merge_group(g) for g in group_records(records)), key=lambda m: m.ids)
