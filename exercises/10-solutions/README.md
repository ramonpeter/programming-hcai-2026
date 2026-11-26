# Sheet 10 — solution files

Run every program from its own folder, for example `cd B3-staircase` and then
`python staircase.py`. No data files are needed.

| Folder | Run | Shows |
|---|---|---|
| `A1-trace` | `python p1_mystery.py` … `python p4_gcd.py` | the four programs from the sheet |
| | `python traced.py` | the calls of `mystery` and `gcd`, indented by depth, with what each returns |
| `A2-broken` | `python broken.py` | the three functions as given, the tests that pass, and the inputs that break them |
| | `python fixed.py` | the fixed versions |
| `A3-numbers` | `python numbers.py` | `power` and `to_binary`, checked against `bin` for 0 to 99 |
| `A4-power` | `python power_versions.py` | `power(2, 1000)` crashing, the 11 calls of `fast_power`, 2047 calls without `half`, and `power_loop` |
| `B1-strings` | `python strings.py` | `count`, `is_palindrome` on both base cases, and the phrase palindrome |
| `B2-flatten` | `python flatten.py` | `flatten` and `deep_sum` on the nested list, `[]` and `[[[]]]` |
| `B3-staircase` | `python staircase.py` | 9 135 460 calls for `ways(25)`, 76 with the memo, then `ways(100)` |
| `B4-merge-sort` | `python merge_sort.py` | `merge`, `merge_sort`, 1000 random tests, the depth for a million items, and the time against `sorted` |
| `extra` | `python permutations.py` | the six orderings of `"abc"`, and the counts for 4 and 8 letters |
