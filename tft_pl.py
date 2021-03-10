from itertools import combinations

import mip

def pl_tft(n):
    m = mip.Model()
    m.verbose = 1
    E = range(n)
    colors = range(1, 2)

    x = {s : m.add_var(var_type=mip.BINARY) for s in combinations(E, 4)}
    c = {(k, s) : m.add_var(var_type=mip.BINARY) for k in colors for s in combinations(E, 4)}
    # c[k, s] == True iff s has color k

    for p in combinations(E, 2):
        S_i = []
        for s in combinations(E, 4):
            if p[0] in s and p[1] in s:
                S_i.append(x[s])
        m += mip.xsum(S_i) == 2

    for s in combinations(E, 4):
        m += x[s] <= mip.xsum(c[(k, s)] for k in colors) <= 1

    for k in colors:
        for s1 in combinations(E, 4):
            for s2 in combinations(E, 4):
                set_s1, set_s2 = set(s1), set(s2)
                if len(set_s1 & set_s2) != 0 and set_s1 != set_s2:
                    m += c[k, s1] + c[k, s2] <= 1

    # m.objective = mip.minimize(mip.xsum(c))
    print(f"{m.num_cols} variables")
    print(f"{m.num_rows} constraints")

    m.optimize()

    for k, s in c:
        if c[k, s] == 1:
            print(k, s)

pl_tft(16)
