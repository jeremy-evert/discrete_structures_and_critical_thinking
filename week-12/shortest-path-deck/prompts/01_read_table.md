# Prompt 01: read the distance table

Paste the block below into Claude. `prompt-a` is the first box on the slide.

```prompt-a
Make a folder called tour_demo. Put data/distances.csv in it (I will paste it).
Write tour.py with a function read_table(path) that reads the CSV and returns a dictionary
{(from_city, to_city): distance} using whole numbers. The diagonal cells are blank, so skip them.
Do not add anything else yet.
Then add a few lines at the bottom (under an if __name__ == "__main__": block) that print
the distance from 1 to 2 and from 2 to 1. Run it and show me the output.
```
