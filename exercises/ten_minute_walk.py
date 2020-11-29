#! python3

def is_valid_walk(walk):
    vertical = 0
    horizontal = 0
    for elem in walk:
        if elem == 'n':
            vertical += 1
        elif elem == 's':
            vertical -= 1
        elif elem == 'w':
            horizontal += 1
        elif elem ==  'e':
            horizontal -= 1
    return (len(walk) == 10 and vertical == 0 and horizontal == 0)

is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])
is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])

### Found this pretty easy tbh. I could have writen it more elegantly as:

def is_valid_walk_elegant(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

###what I 've learned
#I had no idea there was a .count method for list eleemnts! Maybe I had seen it and forgotten it...
#anyway, new tool added! gained some exp.
