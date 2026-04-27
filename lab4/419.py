import math, sys

def solve_shortest_path():
    data = sys.stdin.read().split()
    if not data: return
    r, x1, y1, x2, y2 = map(float, data)
    
    d1 = math.sqrt(x1**2 + y1**2)
    d2 = math.sqrt(x2**2 + y2**2)
    dist_ab = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    cross_product = abs(x1*y2 - x2*y1)
    h = cross_product / dist_ab if dist_ab > 0 else d1#координаталар басынан АВ түзуіне дейінгі биіктік
    
    # Check if the projection of O onto AB falls within the segment
    dot1 = (x2-x1)*(-x1) + (y2-y1)*(-y1)
    dot2 = (x1-x2)*(-x2) + (y1-y2)*(-y2)
    
    if h >= r or dot1 <= 0 or dot2 <= 0:
        print(f"{dist_ab:.10f}")#utirgen kein 10tanba
    else:
        # Path: tangent from A + arc + tangent to B
        alpha1 = math.acos(r / d1) #А нүктесі мен жанама нүктесі арасындағы бұрышты табады
        alpha2 = math.acos(r / d2)
        total_angle = math.acos(max(-1, min(1, (x1*x2 + y1*y2) / (d1*d2))))#А және В нүктелерінің арасындағы орталық бұрыш.
        arc_angle = total_angle - alpha1 - alpha2#доғаның бұрышы.
        length = math.sqrt(d1**2 - r**2) + math.sqrt(d2**2 - r**2) + (arc_angle * r)#Жанамалардың ұзындығы мен доғаның ұзындығын косу
        print(f"{length:.10f}")

solve_shortest_path()