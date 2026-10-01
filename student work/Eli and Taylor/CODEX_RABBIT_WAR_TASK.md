# Codex Task: Complete Rabbit War

## ABSOLUTE PROJECT PRIORITY: NOTHING GETS SKIPPED

Completeness of Rabbit War is more important than preserving the original Fibonacci exercise.

- Include EVERY dictator/person/reference and EVERY American event recorded in this specification.
- Turn EVERY depicted human/person into rabbit/bunny form, including background people and crowds.
- Do not drop an item because it is difficult, because an image is missing, because the original program was small, or because implementing it would disturb the Fibonacci logic.
- Fibonacci accuracy is NOT a project requirement. It may be simplified, altered, made approximate, or removed if necessary to make the complete Rabbit War work.
- Do not sacrifice requested images, events, characters, transformations, asset loading, or presentation merely to keep the Fibonacci sequence mathematically exact.
- The implementation should prioritize: (1) nothing requested is omitted, (2) everything visual is bunny/rabbit form, (3) all assets/events are actually wired into Rabbit War, and only then (4) preserve Fibonacci behavior where convenient.
- An item is not complete merely because it appears in documentation. It must be represented in the program/asset system so Rabbit War can actually use it.
- Do not silently skip failed/missing assets. Track them as unfinished and complete them when the environment has the necessary capability.
- Do not ask the student to choose which requested items to omit. The intended scope is ALL of them.

## NON-NEGOTIABLE: EVERYTHING BECOMES RABBIT/BUNNY FORM

This is the student's highest-priority visual requirement and overrides any weaker or ambiguous wording elsewhere in this project.

- EVERY human/person shown in a selected source/reference image must be transformed into a rabbit/bunny character.
- This applies to ALL dictator references and ALL American historical-event references listed in this file.
- Do not leave ordinary human faces, heads, hands, or bodies in the finished Rabbit War reinterpretation when they represent people in the scene.
- Preserve the source image's recognizable composition as closely as practical: pose, camera angle, number/placement of figures, clothing/uniform cues, facial-expression equivalent, flags, signs, furniture, microphones, vehicles, buildings, landscapes, smoke, lighting, and other important props.
- Replace the people, not the identity of the scene. The finished image should still be recognizable as a bunny/rabbit reinterpretation of its source reference.
- Rabbits may wear the corresponding period clothing, uniforms, suits, hats, glasses, medals, or other non-humanizing visual identifiers needed to preserve the reference.
- Groups/crowds also become rabbit/bunny crowds. Do not transform only the central figure while leaving background people human.
- Portrait references become rabbit portraits. Rally images become rabbit rallies. Political scenes become rabbit political scenes. War scenes become rabbit war scenes. Protest scenes become rabbit protests. Disaster/emergency scenes become rabbit emergency scenes.
- For sensitive events, keep the rabbit conversion non-graphic. Do not depict gore, exposed wounds, corpses, or victim mockery. Use recognizable aftermath, memorial, architecture, vehicles, skyline, emergency response, newspapers, or symbolic scene elements as necessary.
- Do not substitute a generic unrelated bunny picture. Each output must be tied to its intended reference/event through recognizable visual cues.
- Do not consider an item complete merely because a filename, prompt, URL, manifest entry, or reference image exists. The requested end state is an actual usable Rabbit War bunny/rabbit-form asset whenever the environment provides image-generation/editing capability.
- Do not ask the student again whether a listed item should be turned into rabbit/bunny form. The answer is YES for every listed person and event.

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

## Charlie Kirk assassination — user-supplied visual reference

Add the assassination of Charlie Kirk (Utah Valley University, September 10, 2025) to the American-event Rabbit War set.

The student supplied a specific visual reference frame. Treat that frame as the requested composition reference for this entry.

Expected asset identifiers/paths:
- source/reference: `reference_images/american_events/charlie_kirk_assassination_reference.jpg`
- rabbit-form output: `reference_images/american_events/charlie_kirk_assassination_rabbit.jpg`
- event ID: `charlie_kirk_assassination`

Rabbit transformation requirements for this specific frame:
- Convert the seated human figure into a rabbit/bunny.
- Preserve the green Robin Hood-style hat and feather.
- Preserve the green tunic/costume, brown belt, cross-body strap, arm guards, and quiver/arrows.
- Preserve the seated pose and approximate framing.
- Preserve the arrow crossing the foreground/neck-area composition as a recognizable visual cue, but render the scene non-graphically: no blood, wound, gore, exposed injury, or corpse imagery.
- Reproduce the event-stage/backdrop composition closely enough to remain recognizable, while avoiding the need to reproduce third-party logos perfectly.
- Do not replace this with a generic bunny portrait.
- Wire this event into Rabbit War's selectable event/asset pool.
- As with every other requested item, the human figure must not remain human in the final Rabbit War asset.

