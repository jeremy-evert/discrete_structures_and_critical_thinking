"""Made-up tracks. No real songs, no real people."""
from playlist.track import Track

# Three listings of one song, each a few seconds longer than the last.
SLOW_ORBIT_1 = Track(1, "Slow Orbit", "Lantern Hill", 200)
SLOW_ORBIT_2 = Track(2, "Slow Orbit (Remastered)", "Lantern Hill", 204)
SLOW_ORBIT_3 = Track(3, "slow orbit", "LANTERN HILL", 208)
PAPER_MOONS = Track(4, "Paper Moons", "Moss & Marrow", 204)
GLASS_HARBOR = Track(5, "Glass Harbor", "Moss & Marrow", 351)
NIGHT_BUS = Track(6, "Night Bus", "Rivet & Rye", 351)

TRACKS = [SLOW_ORBIT_1, SLOW_ORBIT_2, SLOW_ORBIT_3, PAPER_MOONS, GLASS_HARBOR, NIGHT_BUS]
