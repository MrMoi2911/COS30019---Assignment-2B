import math

def flow_to_speed(flow):
    # Case 1: low traffic
    if flow <= 351:
        return 60  # km/h
    
    # Case 2: solve quadratic
    a = -1.4648375
    b = 93.75
    c = -flow

    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return 60  # fallback

    sqrt_d = math.sqrt(discriminant)

    # two solutions
    s1 = (-b + sqrt_d) / (2*a)
    s2 = (-b - sqrt_d) / (2*a)

    # pick realistic speed (positive and ≤ 60)
    speeds = [s for s in [s1, s2] if s > 0]
    
    if not speeds:
        return 60

    return min(max(speeds), 60)
