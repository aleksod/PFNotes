# Solves the equation (a + (b - c) * d - e) * f = 75

for a in range(1, 6):
    for b in range(1,6):
        for c in range(1, 6):
            for d in range(1,6):
                for e in range(1,6):
                    for f in range(1,6):
                        if (a + (b - c) * d - e) * f == 38: # and \
                        #a!=b and a!=c and a!=d and a!=e and a!=f and \
                        #b!=c and b!=d and b!=e and b!=f and \
                        #c!=d and c!=e and c!=f and \
                        #d!=e and d!=f and \
                        #e!=f:
                            print 'The solution is:'
                            print 'a =', a
                            print 'b =', b
                            print 'c =', c
                            print 'd =', d
                            print 'e =', e
                            print 'f =', f
                            break
