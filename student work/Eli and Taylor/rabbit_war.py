# RABBIT WAR CODEX CONTRACT
# Before changing this project, read CODEX_RABBIT_WAR_TASK.md and AGENTS.md
# in this directory. Those files are the authoritative project requirements.
# Do not ask the student to restate dictator/event/image scope already recorded there.
# Missing image binaries are unfinished work, not optional requirements.
#
import random

EVENTS = [
    ("pearl_harbor", "reenacted a rabbit version of Pearl Harbor", "pearl_harbor.jpg"),
    ("cold_war", "started a Cold Carrot War", "cold_war.jpg"),
    ("cuban_missile_crisis", "triggered the Cuban Carrot Crisis", "cuban_missile_crisis.jpg"),
    ("jfk_motorcade", "staged a rabbit presidential motorcade", "jfk_assassination.jpg"),
    ("vietnam_war", "sent helicopter rabbits into the jungle", "vietnam_war.jpg"),
    ("apollo_11", "put the first rabbit on the Moon", "apollo_11.jpg"),
    ("woodstock", "held the largest rabbit music festival in history", "woodstock.jpg"),
    ("kent_state", "staged a tense rabbit campus protest", "kent_state.jpg"),
    ("pentagon_papers", "leaked the Pentagon Carrot Papers", "pentagon_papers.jpg"),
    ("watergate", "broke into the Watergate Warren", "watergate.jpg"),
    ("nixon_resignation", "watched President Rabbit resign", "nixon_resignation.jpg"),
    ("jonestown", "entered an ominous jungle rabbit settlement", "jonestown.jpg"),
    ("three_mile_island", "nearly melted down the Three Carrot Island reactor", "three_mile_island.jpg"),
    ("iran_hostage_crisis", "began the Great Rabbit Hostage Crisis", "iran_hostage_crisis.jpg"),
    ("mount_st_helens", "survived Mount St. Hare-lens erupting", "mount_st_helens.jpg"),
    ("crack_epidemic", "got caught in the 1980s crack-era rabbit underworld", "crack_epidemic.jpg"),
    ("aids_crisis", "faced the rabbit version of the AIDS crisis", "aids_crisis.jpg"),
    ("reagan_assassination_attempt", "survived an attempt on President Rabbit", "reagan_assassination_attempt.jpg"),
    ("move_bombing", "witnessed a rabbit-city MOVE confrontation", "move_bombing.jpg"),
    ("challenger", "watched the Rabbit Challenger disaster unfold", "challenger.jpg"),
    ("iran_contra", "got tangled in the Iran-Carrot affair", "iran_contra.jpg"),
    ("black_monday", "lost the carrot market on Black Monday", "black_monday.jpg"),
    ("exxon_valdez", "spilled the strategic carrot-oil reserve", "exxon_valdez.jpg"),
    ("gulf_war", "launched Operation Desert Rabbit", "gulf_war.jpg"),
    ("rodney_king", "entered a rabbit version of the Rodney King era", "rodney_king.jpg"),
    ("la_riots", "survived the Los Angeles rabbit unrest", "la_riots.jpg"),
    ("ruby_ridge", "entered a rabbit standoff at Ruby Ridge", "ruby_ridge.jpg"),
    ("waco", "entered a rabbit version of the Waco siege", "waco.jpg"),
    ("world_trade_center_1993", "survived the 1993 Rabbit Trade Center bombing", "world_trade_center_1993.jpg"),
    ("oklahoma_city", "responded to the Oklahoma City rabbit bombing aftermath", "oklahoma_city_bombing.jpg"),
    ("olympic_park", "survived the Centennial Olympic Rabbit Park bombing", "centennial_olympic_park.jpg"),
    ("columbine", "entered a solemn rabbit-school memorial scene", "columbine.jpg"),
    ("bush_gore", "recounted every last rabbit ballot", "bush_gore_2000.jpg"),
    ("september_11", "entered a solemn rabbit version of the September 11 skyline", "september_11.jpg"),
    ("anthrax_attacks", "opened suspicious rabbit mail", "anthrax_attacks.jpg"),
    ("afghanistan_war", "deployed into the mountains of Afghanistan", "afghanistan_war.jpg"),
    ("iraq_war", "launched Operation Rabbit Freedom", "iraq_war.jpg"),
    ("abu_ghraib", "entered a rabbit version of the Abu Ghraib scandal", "abu_ghraib.jpg"),
    ("hurricane_katrina", "floated through Hurricane Katrina in carrot boats", "hurricane_katrina.jpg"),
    ("financial_crisis", "crashed the global carrot-backed economy", "financial_crisis_2008.jpg"),
    ("deepwater_horizon", "spilled carrot oil in the Gulf", "deepwater_horizon.jpg"),
    ("occupy_wall_street", "occupied Wall Street with thousands of rabbits", "occupy_wall_street.jpg"),
    ("boston_marathon", "entered a solemn rabbit Boston Marathon aftermath scene", "boston_marathon_bombing.jpg"),
    ("snowden_nsa", "leaked the NSA's secret rabbit files", "snowden_nsa.jpg"),
    ("ferguson", "joined a rabbit protest in Ferguson", "ferguson.jpg"),
    ("charlottesville", "entered a rabbit version of the Charlottesville confrontation", "charlottesville.jpg"),
    ("covid_19", "locked down the Great Rabbit Republic", "covid_19.jpg"),
    ("george_floyd_protests", "joined nationwide rabbit protests", "george_floyd_protests.jpg"),
    ("january_6", "stormed the Rabbit Capitol", "january_6.jpg"),
    ("afghanistan_withdrawal", "rushed through the final rabbit evacuation from Afghanistan", "afghanistan_withdrawal.jpg"),
    ("east_palestine", "derailed a rabbit freight train in East Palestine", "east_palestine.jpg"),
    ("key_bridge", "watched the Rabbit Key Bridge collapse", "baltimore_key_bridge.jpg"),
]

FALLBACK_EVENTS = [
    ("carrot_fortress", "captured a carrot fortress", "carrot_fortress.jpg"),
    ("celery_republic", "invaded the Celery Republic", "celery_republic.jpg"),
    ("lettuce_strike", "launched tactical lettuce strikes", "lettuce_strike.jpg"),
    ("moon_burrow", "built a moon burrow", "moon_burrow.jpg"),
]


def get_event():
    return random.choice(EVENTS or FALLBACK_EVENTS)


def main():
    try:
        months = int(input("Months of rabbit warfare: "))
        if months < 1:
            raise ValueError
    except ValueError:
        print("Enter a whole number greater than 0.")
        return

    a = 1
    b = 1

    print("\\n=== OFFICIAL BUNNY WAR REPORT ===\\n")

    for month in range(1, months + 1):
        if month == 1:
            rabbits = a
        elif month == 2:
            rabbits = b
        else:
            rabbits = a + b
            a = b
            b = rabbits

        event_id, action, image = get_event()
        print(f"Month {month}: {rabbits} rabbits {action}.")
        print(f"  EVENT_ID: {event_id}")
        print(f"  IMAGE: reference_images/american_events/{image}")

    print("\\nThe war ended when everyone forgot why it started.")


if __name__ == "__main__":
    main()
