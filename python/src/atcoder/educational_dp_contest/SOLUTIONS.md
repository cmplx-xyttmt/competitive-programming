# Educational DP Contest — Solution Notes

---

## A — Frog 1
**Approach:** Forward DP. `dp[i]` = minimum cost to reach stone `i`.
Transition: `dp[i] = min(dp[i-1] + |h[i]-h[i-1]|, dp[i-2] + |h[i]-h[i-2]|)`

**Critique highlights:**
- Original used backwards DP, which forced pre-loop special casing and manual index arithmetic. Forward DP is more natural and eliminates all of that.
- `if i >= 2` guard belongs in loop bounds or as a simple conditional — no pre-loop initialization needed.

**Learnt:**
- Prefer the DP direction that matches the problem's natural flow (start → end).
- Use `float('inf')` over `int(1e18)` in Python.
- Encode constraints in loop bounds rather than runtime guards inside the loop.

---

## B — Frog 2
**Approach:** Forward DP. Same as Frog 1 but inner loop tries all `k` possible jumps.
Transition: `dp[i] = min(dp[i-j] + |h[i]-h[i-j]|)` for `j` in `1..min(i, k)`

**Critique highlights:**
- `if j > i: break` inside the loop → cleaner as `range(1, min(i, k) + 1)`.

**Learnt:**
- Encode constraints in the loop range, not as runtime checks inside the loop body.

---

## C — Vacation
**Approach:** Forward DP with rolling array. `dp[j]` = max happiness on current day doing activity `j`.
Transition: `dp[j] = happiness[j] + max(prev[k] for k in range(3) if k != j)`

**Critique highlights:**
- Original used modular arithmetic `(j+1)%3`, `(j+2)%3` to express "other activities" — clever but `k != j` is clearer.
- `if i > 0` guard inside loop → eliminated by handling day 0 as the base case before the loop.
- Full N×3 table unnecessary — only the previous row is ever needed.

**Learnt:**
- Use a rolling array (`prev`/`curr`) when only the previous row is needed — reduces space from O(N) to O(1).
- Separating the base case from the loop avoids `if i > 0` style guards.

---

## D — Knapsack 1
**Approach:** Rolling array DP. `dp[j]` = max value achievable with capacity `j`.
Transition: `dp[j] = max(dp[j], v + prev[j - w])` for `j` in `w..W`

**Critique highlights:**
- Original had `if i == 0` guard to avoid `dp[-1]` wraparound — rolling array eliminates it entirely.
- Inner loop starts at `w`, not 0 — capacities below `w` can't be affected by the current item.
- Running `best` variable unnecessary — answer is always `prev[W]`.

**Learnt:**
- Rolling array knapsack: `curr = list(prev)` then update `curr[j]` reading from `prev`.
- Starting inner loop at `w` is both correct and more efficient.

---

## E — Knapsack 2
**Approach:** Flipped DP. `dp[v]` = minimum weight needed to achieve exactly value `v`.
Answer: largest `v` where `dp[v] <= W`.

**Why flip?** W can be up to 10^9 (too large for weight-indexed DP), but total value is at most N × 1000 = 100,000.

**Critique highlights:**
- `n * 1000` is a magic number — derive the actual max value from `sum(v for _, v in items)`.
- `next(j for j in range(max_v, -1, -1) if prev[j] <= W)` finds the answer with early exit.

**Learnt:**
- When W is huge but values are small, flip the DP to index by value instead of weight.
- `next()` returns the first element from a generator and stops — useful for early-exit max/min over a filtered range.

---

## F — LCS
**Approach:** Rolling array for lengths + full `index` table for path reconstruction.
`index[i][j]` stores the coordinates of the last match cell contributing to `dp[i][j]`.
Self-pointer convention: `index[i][j] = (i, j)` marks that cell itself as a match.

**Backtracking:** Start at `index[m][n]`, follow pointers; when a self-pointer is found, append `s[r-1]` and manually step to `(r-1, c-1)`.

**Why not build the string during DP?** String concatenation inside the inner loop is O(L) per cell, making the total complexity O(N × M × L) ≈ O(N³) — TLE.

**Critique highlights:**
- TLE solution stored `(length, substring)` tuples and concatenated strings in the inner loop.
- The dead `else` branch (when chars don't match, check if diagonal is better than max(left, above)) is unreachable: `dp[i-1][j-1] <= max(dp[i][j-1], dp[i-1][j])` always holds since dp is non-decreasing in both dimensions.
- The self-pointer convention is load-bearing — storing `(i-1, j-1)` for matches instead breaks backtracking because non-match cells forward the predecessor of the match, not the match cell itself.

**Learnt:**
- Never build strings inside a DP inner loop — always reconstruct afterwards.
- Separate the DP (track lengths with rolling array) from reconstruction (full index table).
- dp non-decreasing in both dimensions ⟹ diagonal value never exceeds max(left, above) in the no-match case.

---

## G — Longest Path
**Approach:** Kahn's algorithm (BFS topological sort) + DP.
`dp[node]` = longest path ending at `node`. Process nodes in topological order; when a node's indegree hits 0, all its predecessors are finalized.

```
queue ← all nodes with indegree 0
for each node popped:
    for each neighbour nxt:
        dp[nxt] = max(dp[nxt], dp[node] + 1)
        decrement indegree[nxt]; if 0, enqueue
answer = max(dp)
```

**Why not memoized recursion?**
- Python's default recursion limit (1000) can be exceeded on large DAGs.
- Memoization check `if longest[node]` is broken for nodes with longest path 0 (falsy) — they are never cached. Fix: use `None` as the "not yet computed" sentinel.

**Learnt:**
- **Kahn's algorithm**: process a DAG in topological order using a queue of zero-indegree nodes; decrement indegree as edges are consumed.
- Use `None` (not `0`) as the sentinel for uncomputed memoization values when `0` is a valid result.
- Kahn's approach eliminates recursion limits and the sentinel problem simultaneously.
