"""Checks for the Week 10 code. Run: python3 test_screening.py"""
import v2_function
import v3_two_conditionals as v3


def test_cells_total_n():
    t = v2_function.screening_table(0.01, 0.90, 0.95)
    assert round(sum(t.values())) == 10000


def test_v1_numbers_match_function():
    t = v3.screening_table(0.01, 0.90, 0.95)
    assert (round(t["true_pos"]), round(t["false_neg"]),
            round(t["false_pos"]), round(t["true_neg"])) == (90, 10, 495, 9405)


def test_the_two_conditionals_differ():
    t = v3.screening_table(0.01, 0.90, 0.95)
    assert abs(v3.p_pos_given_c(t) - 0.90) < 1e-9
    assert abs(v3.p_c_given_pos(t) - 90 / 585) < 1e-9


def test_higher_prevalence_raises_p_c_given_pos():
    low = v3.p_c_given_pos(v3.screening_table(0.01, 0.90, 0.95))
    high = v3.p_c_given_pos(v3.screening_table(0.20, 0.90, 0.95))
    assert high > low
    assert abs(high - 1800 / 2200) < 1e-9


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
    print("all passed")
