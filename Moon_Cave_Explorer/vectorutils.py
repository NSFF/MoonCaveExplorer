from visual import vector

def dot_product(v, w):
    v = vector(v)
    w = vector(w)
    return float((v[0] * w[0]) + (v[1] * w[1]))

def intersect(A, B, C, D):
    A = vector(A)
    B = vector(B)
    C = vector(C)
    D = vector(D)
    E = vector(B[0] - A[0], B[1] - A[1], 0) # B-A
    F = vector(D[0] - C[0], D[1] - C[1], 0) # D-C
    P = vector(-E[1], E[0], 0)
    Q = vector(-F[1], F[0], 0)
    par1 = dot_product(F, P)
    if par1 == 0:
        return False
    par2 = dot_product(E, Q)
    if par2 == 0:
        return False
    h = dot_product((A - C), P) / par1
    g = dot_product((C - A), Q) / par2
    if ((g >= 0 and g <= 1) and (h >= 0 and h <= 1)):
        cross = C + F*h
        return True
    return False





