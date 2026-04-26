# EXAM03-42-1337

A collection of Python mini-exercises (algorithmic/string/list manipulation tasks), each in its own folder with:
- a solution script (`*.py`)
- a task statement (`subject.txt` or `subjext.txt`)

## Project Structure

| Folder | Main file | What it does |
|---|---|---|
| `bracket_validator/` | `bracket_validator.py` | Validates whether brackets in a string are properly balanced and ordered (`()[]{}`). |
| `cryptic_sorter/` | `cryptic_sorter.py` | Sorts a list of strings using custom criteria (vowels, length, lexicographic order). |
| `echo_validator/` | `echo_validator.py` | Checks if a string is a palindrome while ignoring case and non-alphanumeric characters. |
| `mirror_matrix/` | `mirror_matrix.py` | Reverses each row of a 2D matrix while keeping row order unchanged. |
| `pattern_tracker/` | `pattern_tracker.py` | Counts adjacent digit pairs where the second is exactly first + 1. |
| `py_base_converter/` | `Converter_Base.py` | Converts a number string from one base to another (intended range: 2 to 36). |
| `shadow_merge/` | `shadow_merge.py` | Merges two integer lists and returns a single sorted list; handles `None`/empty inputs. |
| `string_permutation_checker/` | `string_permutation_checker.py` | Checks whether two strings are anagrams/permutations of each other. |
| `string_sculptor/` | `string_sculptor.py` | Alternates alphabetic characters between lowercase/uppercase, skipping non-letters. |
| `twist_sequence/` | `twist_sequence.py` | Rotates a list by `n` positions (supports positive and negative values). |
| `whisper_cipher/` | `whisper_cipher.py` | Caesar-style alphabet shift cipher with case preservation and wrap-around behavior. |

## Notes

- Most scripts include inline `print(...)` tests for quick manual verification.

## Run Any Exercise

From repository root:

```bash
python3 bracket_validator/bracket_validator.py
python3 cryptic_sorter/cryptic_sorter.py
python3 echo_validator/echo_validator.py
python3 mirror_matrix/mirror_matrix.py
python3 pattern_tracker/pattern_tracker.py
python3 py_base_converter/Converter_Base.py
python3 shadow_merge/shadow_merge.py
python3 string_permutation_checker/string_permutation_checker.py
python3 string_sculptor/string_sculptor.py
python3 twist_sequence/twist_sequence.py
python3 whisper_cipher/whisper_cipher.py
```

## Goal

This repository is designed as practice for coding-exam style problems: correctness, edge cases, and clean problem decomposition in Python.
