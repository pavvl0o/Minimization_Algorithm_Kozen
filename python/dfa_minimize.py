#!/usr/bin/env python3
"""
DFA Minimization using Table-Filling Algorithm (Marking Algorithm)
Based on Kozen's Automata and Computability, Lecture 14
"""

import sys


def solve():
    lines = sys.stdin.readlines()
    line_idx = 0
    
    # Skip empty lines at start
    while line_idx < len(lines) and not lines[line_idx].strip():
        line_idx += 1
    if line_idx >= len(lines):
        return
    
    c = int(lines[line_idx].strip())
    line_idx += 1
    
    out_lines = []
    for _ in range(c):
        # Skip empty lines
        while line_idx < len(lines) and not lines[line_idx].strip():
            line_idx += 1
        n = int(lines[line_idx].strip())
        line_idx += 1
        
        # Alphabet
        while line_idx < len(lines) and not lines[line_idx].strip():
            line_idx += 1
        alphabet = lines[line_idx].strip().split()
        line_idx += 1
        k = len(alphabet)
        
        # Final states
        while line_idx < len(lines) and not lines[line_idx].strip():
            line_idx += 1
        final_states = set(map(int, lines[line_idx].strip().split())) if lines[line_idx].strip() else set()
        line_idx += 1
        
        # Transitions
        trans = [[0] * k for _ in range(n)]
        for i in range(n):
            while line_idx < len(lines) and not lines[line_idx].strip():
                line_idx += 1
            parts = list(map(int, lines[line_idx].strip().split()))
            line_idx += 1
            # parts[0] is state index, parts[1:] are transitions
            for j in range(k):
                trans[i][j] = parts[j + 1]
        
        # Table-filling algorithm
        distinguished = [[False] * n for _ in range(n)]
        
        # Base case: mark pairs where one is final and other is not
        for i in range(n):
            for j in range(i + 1, n):
                if (i in final_states) != (j in final_states):
                    distinguished[i][j] = True
        
        # Iterative marking
        changed = True
        while changed:
            changed = False
            for i in range(n):
                for j in range(i + 1, n):
                    if not distinguished[i][j]:
                        for s in range(k):
                            ni = trans[i][s]
                            nj = trans[j][s]
                            u, v = (ni, nj) if ni < nj else (nj, ni)
                            if u != v and distinguished[u][v]:
                                distinguished[i][j] = True
                                changed = True
                                break
        
        # Collect equivalent pairs
        equiv = []
        for i in range(n):
            for j in range(i + 1, n):
                if not distinguished[i][j]:
                    equiv.append(f"({i}, {j})")
        
        out_lines.append(" ".join(equiv))
    
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()