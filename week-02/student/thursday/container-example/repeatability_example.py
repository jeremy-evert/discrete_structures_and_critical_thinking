"""Tiny deterministic output for the DSCT Week 2 receipt exercise."""

raw_name = "  Ada Lovelace  "
normalized = raw_name.strip()
expected = "Ada Lovelace"

print(f"normalized={normalized}")
print(f"check={'PASS' if normalized == expected else 'FAIL'}")
