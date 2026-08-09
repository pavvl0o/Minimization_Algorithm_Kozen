# DFA Minimization Assignment

## Student Information
- **Full Name**: [TU NOMBRE COMPLETO]
- **Class Number**: [TU NÚMERO DE CLASE]

## Environment
- **Operating System**: Linux Omarchy versión 3.8.4 (Arch-based)
- **Compiler**: g++ (GCC) 15.x
- **C++ Standard**: C++17
- **Build Tool**: g++ directly (no CMake/Make required)

## Algorithm Explanation

This implementation uses the **Table-Filling Algorithm** (also known as the Marking Algorithm) for DFA minimization, as presented in Kozen's *Automata and Computability* (Lecture 14).

### Overview
Given a DFA with no inaccessible states, the algorithm identifies pairs of equivalent states that can be collapsed to produce a minimized DFA.

### Steps

1. **Input Parsing**: Read multiple test cases. Each case provides:
   - Number of states `n` (states are 0 to n-1, initial state is always 0)
   - Alphabet Σ (space-separated lowercase letters)
   - Final states F (space-separated integers)
   - Transition table: n lines, each starting with the state index followed by k = |Σ| destination states

2. **Initialization**: Create an `n × n` boolean matrix `distinguished` (only upper triangle used, where `i < j`). Initially all `false`.

3. **Base Case (Marking)**: For all pairs `(i, j)` where `i < j`, mark `distinguished[i][j] = true` if exactly one of `i, j` is a final state. These pairs are trivially distinguishable.

4. **Iterative Marking**: Repeat until no new pairs are marked:
   - For each unmarked pair `(i, j)`, check all alphabet symbols `a ∈ Σ`
   - Let `ni = δ(i, a)` and `nj = δ(j, a)` be the transitions
   - If `ni ≠ nj` and the pair `(min(ni, nj), max(ni, nj))` is already marked as distinguished, then mark `(i, j)` as distinguished
   - This works because if two states transition to distinguishable states on the same symbol, they themselves are distinguishable

5. **Output**: After convergence, all unmarked pairs `(i, j)` with `i < j` are equivalent. Output them in lexicographical order as `(i, j)` separated by spaces, one line per test case.

### Complexity
- Time: O(n² × |Σ|) per iteration, worst-case O(n³ × |Σ|) but typically much faster
- Space: O(n²) for the distinction matrix

## Build Instructions

```bash
g++ -std=c++17 -O2 dfa_minimize.cpp -o dfa_minimize
```

## Run Instructions

```bash
# From stdin
./dfa_minimize < input.txt

# Or pipe directly
cat input.txt | ./dfa_minimize
```

## Input Format Example

```
4
6
a b
1 2 5
0 1 2
1 3 4
2 4 3
3 5 5
4 5 5
5 5 5
6
a b
3 4 5
0 1 2
1 3 4
2 4 3
3 5 5
4 5 5
5 5 5
6
a
1 4
0 1
1 2
2 3
3 4
4 5
5 0
4
a b
0 1
0 1 2
1 1 2
2 3 1
3 3 3
```

## Output Format Example

```
(1, 2) (3, 4)
(1, 2) (3, 4) (3, 5) (4, 5)
(0, 3) (1, 4) (2, 5)
(0, 1)
```

## References
- Kozen, Dexter C. (1997). *Automata and Computability*. 1st ed. Berlin, Heidelberg: Springer-Verlag. ISBN: 0387949070. DOI: https://doi.org/10.1007/978-1-4612-1844-9
- Lecture 13: Construction for DFA minimization
- Lecture 14: Table-filling algorithm