def initial_state():
    return (8, 0, 0)


def is_goal(s):
    return s == (4, 4, 0)


def successors(s):
    x, y, z = s

    tx = 8 - x
    # y -> x
    if tx > 0 and y > 0:
        if y > tx:
            yield ((8, y - tx, z), tx)
        else:
            yield ((x + y, 0, z), y)
    # z -> x
    if tx > 0 and z > 0:
        if z > tx:
            yield ((8, y, z - tx), tx)
        else:
            yield ((x + z, y, 0), z)

    ty = 5 - y
    # x -> y
    if ty > 0 and x > 0:
        if x > ty:
            yield ((x - ty, 5, z), ty)
        else:
            yield ((0, y + x, z), x)
    # z -> y
    if ty > 0 and z > 0:
        if z > ty:
            yield ((x, 5, z - ty), ty)
        else:
            yield ((x, y + z, 0), z)

    tz = 3 - z
    # x -> z
    if tz > 0 and x > 0:
        if x > tz:
            yield ((x - tz, y, 3), tz)
        else:
            yield ((0, y, z - x), x)
    # y -> z
    if tz > 0 and y > 0:
        if y > tz:
            yield ((x, y - tz, 3), tz)
        else:
            yield ((x, 0, z - y), y)