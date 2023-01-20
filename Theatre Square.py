    import math
    inp=input()
    s =inp.split()
    m_update=math.ceil(int(s[0])/int(s[-1]))
    n_update=math.ceil(int(s[1])/int(s[-1]))
    print(m_update*n_update)
