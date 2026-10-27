def compare(a, b):
    """First draft: order records by family name. Returns -1, 0 or 1."""
    return (a.name.split()[-1] > b.name.split()[-1]) - (a.name.split()[-1] < b.name.split()[-1])
