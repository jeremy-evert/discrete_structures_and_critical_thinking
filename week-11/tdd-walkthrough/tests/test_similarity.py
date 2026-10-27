from merger.names import similar_names


def test_nickname_and_full_name_look_alike():
    assert similar_names("Jon Smith", "John Smith")
    assert similar_names("John Smith", "Jonathan Smith")


def test_different_people_do_not_match():
    assert not similar_names("Jon Smith", "Maria Garcia")
    assert not similar_names("Jon Smith", "Jon Jones")  # same first name, different family


def test_case_does_not_matter():
    assert similar_names("jon smith", "JON SMITH")
