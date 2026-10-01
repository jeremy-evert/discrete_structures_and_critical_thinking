# Codex Task: Complete Rabbit War

## Goal
Implement the complete Rabbit War concept requested by the student. Do not stop at manifests or placeholder metadata. The final project must actually use visual assets where the runtime supports them.

## Existing program
`rabbit_war.py` contains the Fibonacci-style rabbit population and a pool of American historical-event references. Preserve that basic behavior while extending the project.

## Dictator reference set
Create/acquire and normalize one usable reference image for each subject below, then create a rabbit reinterpretation that preserves recognizable visual cues from the reference:
- Adolf Hitler
- Joseph Stalin
- Mao Zedong
- Pol Pot
- Leopold II
- Saddam Hussein
- Idi Amin
- Mengistu Haile Mariam
- Kim Il Sung
- Francisco Macías Nguema
- Rafael Trujillo
- Hissène Habré
- Augusto Pinochet
- Jorge Rafael Videla
- Jean-Bédel Bokassa

Reference imagery does NOT need to be official propaganda. Period photographs, propaganda posters, political cartoons, personality-cult imagery, murals, stamps, currency, newspaper art, anti-regime imagery, and later historical illustrations are acceptable. Label the source/type accurately. Do not falsely describe anti-regime imagery as official regime propaganda.

## American event reference set
Rabbit War must support visual rabbit reinterpretations for:
- Pearl Harbor
- Japanese American incarceration
- atomic bombings / WWII nuclear imagery
- Cold War
- Second Red Scare / McCarthyism
- Korean War
- Civil Rights Movement
- Emmett Till memorial/reference imagery
- Montgomery Bus Boycott
- Little Rock Nine
- Bay of Pigs
- Cuban Missile Crisis
- JFK assassination / Dallas motorcade
- Freedom Summer
- Gulf of Tonkin
- Vietnam War
- Selma / Bloody Sunday
- Watts unrest
- COINTELPRO
- Detroit unrest
- Tet Offensive
- MLK assassination memorial/reference imagery
- RFK assassination memorial/reference imagery
- 1968 unrest
- 1968 Chicago DNC protests
- Apollo 11
- Woodstock
- Manson-era crime imagery
- Kent State
- Pentagon Papers
- Attica
- Watergate
- Wounded Knee occupation
- U.S. Vietnam withdrawal
- 1973 oil crisis
- Nixon resignation
- Fall of Saigon
- Jonestown
- Three Mile Island
- Iran hostage crisis
- Mount St. Helens
- 1980s crack epidemic
- HIV/AIDS crisis
- Reagan assassination attempt
- MOVE bombing
- Challenger disaster
- Iran-Contra
- Black Monday
- Pan Am 103
- Exxon Valdez
- Gulf War
- Rodney King
- 1992 Los Angeles unrest
- Ruby Ridge
- 1993 World Trade Center bombing
- Waco
- Oklahoma City bombing
- Centennial Olympic Park bombing
- Columbine
- Bush-Gore 2000 election/recount
- September 11 attacks
- 2001 anthrax attacks
- Afghanistan War
- Iraq War
- Abu Ghraib scandal
- Hurricane Katrina
- 2008 financial crisis
- Deepwater Horizon
- Occupy Wall Street
- Sandy Hook memorial/reference imagery
- Boston Marathon bombing
- Snowden / NSA disclosures
- Ferguson protests
- Charleston church memorial/reference imagery
- Pulse memorial/reference imagery
- Las Vegas shooting memorial/reference imagery
- Charlottesville
- Parkland memorial/reference imagery
- COVID-19 pandemic
- George Floyd protests
- January 6 U.S. Capitol attack
- Afghanistan withdrawal
- Uvalde memorial/reference imagery
- Maui wildfires
- East Palestine derailment
- Baltimore Key Bridge collapse

## Asset contract
Use:
- `reference_images/dictators/`
- `reference_images/american_events/`

Normalize raster assets to:
- JPEG
- RGB
- 1024x1024
- snake_case filenames

For each reference, preserve enough visual composition, architecture, clothing, signage, props, silhouettes, or other recognizable cues that the rabbit reinterpretation still reads as the intended reference.

## Rabbit transformation rule
Replace human figures with expressive rabbits while retaining the recognizable scene. The tone may be absurd/darkly comic, but for assassinations, terrorism, mass shootings, disasters, hate crimes, and mass-casualty events, keep imagery non-graphic: no gore, exposed wounds, corpses, or victim mockery. Use aftermath, memorial, skyline, vehicle, architecture, newspaper, emergency-response, or symbolic compositions where appropriate.

## Runtime behavior
`rabbit_war.py` should:
1. Preserve Fibonacci rabbit population growth.
2. Randomly choose Rabbit War events.
3. Expose stable event IDs and corresponding asset paths.
4. Use an image when the chosen runtime/UI can display one.
5. Degrade gracefully to text when graphics are unavailable.
6. Never crash solely because an optional image is absent.
7. Keep the event/reference pool easy to extend.

## Important completion rule
A JSON manifest, README, downloader, URL, or filename by itself is NOT completion when an actual image asset is required. If an asset is missing, acquire/create it, normalize it, and place it at the expected path when tooling permits. If the current environment cannot write a binary asset, leave the exact expected path and generation/acquisition requirement explicit for the next capable Codex run.

## Existing standardized assets
Earlier work produced standardized reference files for Hitler, Stalin, two Mao references, Kim Il Sung, and a Khmer Rouge reference. If these binaries are not present in the repository, recreate/acquire them instead of assuming the manifest means they exist.

## Student intent
The student wants all of the above incorporated into Rabbit War and does not want repeated clarification questions about this scope.
