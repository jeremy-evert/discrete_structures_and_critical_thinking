# Prompt 03: check 1-2-3-4-5-6-1 against my hand total

`prompt-a` runs the check; `prompt-b` adds the tests.

```prompt-a
In tour_demo, run legs([1, 2, 3, 4, 5, 6], dist) and tour_length on the same tour.
Print the six legs and the total. I will compare them with the legs and total I added up by hand.
If they differ, do not change my numbers: tell me which leg differs and why.
```

```prompt-b
Create test_tour.py with pytest tests using read_table("data/distances.csv"):
1. the leg 1 to 2 and the leg 2 to 1 are NOT equal (the table is asymmetric);
2. tour_length([1, 2, 3, 4, 5, 6]) equals the total I give you (I will paste my hand total).
Run pytest and show me the one-line summary.
```
