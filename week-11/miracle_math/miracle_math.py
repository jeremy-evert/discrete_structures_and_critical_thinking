def probability_of_streak(chance_per_try, streak_length):
    return chance_per_try ** streak_length


def chance_at_least_once(chance_per_try, number_of_tries):
    chance_of_no_success = 1 - chance_per_try
    chance_of_no_success_in_all_tries = chance_of_no_success ** number_of_tries
    chance_of_at_least_one_success = 1 - chance_of_no_success_in_all_tries
    return chance_of_at_least_one_success
