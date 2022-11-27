global cte
cte = (float,int)

def isConstant(*args):
    for arg in args:
        if type(arg) in cte: continue
        elif type(arg) in (list,tuple):
            result = [isConstant(a) for a in arg]
            if not all(result): return False
            continue
        elif arg in ('x'): return False
    return True