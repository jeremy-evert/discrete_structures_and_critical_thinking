"""Synthetic data only. No real students."""

SMITH_NAMES = ["Jon Smith", "John Smith", "Jonathan Smith", "Maya Smith", "Maria Garcia"]

from merger.records import Record

RECORDS = [
    Record(1, "Jon Smith"),
    Record(2, "John Smith", "js@example.edu"),
    Record(3, "Jonathan Smith", "js@example.edu"),
    Record(4, "Maya Smith", "maya@example.edu"),
    Record(5, "Maria Garcia", "mg@example.edu"),
]
