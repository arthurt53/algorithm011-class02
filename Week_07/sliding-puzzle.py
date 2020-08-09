class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''.join(str(c) for row in board for c in row)
        moves = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        if s == "123450":
            return 0
        bq, eq, nq, res, visited = {(s, s.index('0'))}, {
            ("123450", 5)}, set(), 0, set()

        while bq:
            res += 1
            visited |= bq
            for x, ind in bq:
                for n_ind in moves[ind]:
                    _x = list(x)
                    _x[ind], _x[n_ind] = _x[n_ind], _x[ind]
                    e = (''.join(_x), n_ind)
                    if e not in visited:
                        if e in eq:
                            return res
                        nq.add(e)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1
