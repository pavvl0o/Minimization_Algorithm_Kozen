# DFA Minimization - Kozen Algorithm

Implementation of the DFA minimization algorithm (Table-Filling / Marking Algorithm) from Kozen's *Automata and Computability*, Lecture 14.

## Project Structure

```
.
├── cpp/          # C++17 implementation
│   ├── dfa_minimize.cpp
│   └── README.md
├── python/       # Python 3 implementation
│   ├── dfa_minimize.py
│   └── README.md
```

## Quick Start

### C++
```bash
cd cpp
g++ -std=c++17 -O2 dfa_minimize.cpp -o dfa_minimize
./dfa_minimize < input.txt
```

### Python
```bash
cd python
python3 dfa_minimize.py < input.txt
```

## Input Format

```
c                    # number of test cases
n                    # number of states (0 to n-1, initial state = 0)
a b c ...            # alphabet (space-separated lowercase letters)
f1 f2 ...            # final states (space-separated integers)
# n lines of transitions:
state dest_a dest_b ...  # state index followed by |alphabet| destinations
```

## Output Format

Equivalent state pairs in lexicographical order: `(i, j) (k, l) ...` (one line per test case)

## Example

Input:
```
1
6
a b
1 2 5
0 1 2
1 3 4
2 4 3
3 5 5
4 5 5
5 5 5
```

Output:
```
(1, 2) (3, 4)
```

## Reference

Kozen, Dexter C. (1997). *Automata and Computability*. Springer-Verlag. Lecture 13 & 14.