def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        while x % 5 != 0:
            x += 1
        return x
      
#or in

def closest_mod_5(x):
    return (x + 4) // 5 * 5
