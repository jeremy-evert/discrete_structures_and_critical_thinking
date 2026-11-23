# Week 7 Classroom Websites

Supplementary teaching tools for the Week 7 activity. They do not replace the lesson plan
(`../README.md`, `../instructor/`, `../student/`) and are not part of any graded submission
(Checkpoint 1 is unchanged).

1. `01_crack_the_shift_cipher.html`
   - Same convention as `../student/tuesday-activity.md`: `A=0 … Z=25`, `E(x) = x + k (mod 26)`, `D(y) = y − k (mod 26)`.
   - Predict-first, then attack an illustrative ciphertext by trying keys one at a time or all 26 at once.
   - Bridges to activity question 3 ("nobody knows my key"): the attack needs a small keyspace, knowledge of the method,
     and a way to recognize success. A random-looking preset shows what happens when recognition fails.
   - Optional gcd companion using the activity's own numbers (`53 mod 12`, `−5 mod 12`, `gcd(35, 26)`).
   - Built before the class met; contains no classroom dialogue. Scope is this small system only, not real-world security.
