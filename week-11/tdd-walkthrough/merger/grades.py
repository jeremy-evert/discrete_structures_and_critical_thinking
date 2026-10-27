def letter_grade(score):
    """Return the letter for an integer score 0-100."""
    if score < 0 or score > 100:
        raise ValueError(f"score out of range: {score}")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
