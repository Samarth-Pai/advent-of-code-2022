with open("input.txt") as f:
    lines = f.read().splitlines()
hpos = [0, 0]
tpos = [0, 0]
poses = [(0, 0)]
for line in lines:
    splits = line.split(" ")
    dir, val = splits[0].strip(), int(splits[1])
    itpos = tpos[:]
    if dir == "R":
        if hpos == tpos:
            if val > 1:
                tpos = [tpos[0] + val - 1, tpos[1]]
        elif tpos == [hpos[0] - 1, hpos[1] + 1]:
            tpos = [tpos[0] + val, tpos[1] - 1]
        elif tpos == [hpos[0], hpos[1] + 1]:
            if val > 1:
                tpos = [tpos[0] + val - 1, tpos[1] - 1]
        elif tpos == [hpos[0] + 1, hpos[1] + 1]:
            if val > 2:
                tpos = [tpos[0] + val - 2, tpos[1] - 1]
        elif tpos == [hpos[0] - 1, hpos[1]]:
            tpos = [tpos[0] + val, tpos[1]]
        elif tpos == [hpos[0] + 1, hpos[1]]:
            if val > 2:
                tpos = [tpos[0] + val - 2, tpos[1]]
        elif tpos == [hpos[0] - 1, hpos[1] - 1]:
            tpos = [tpos[0] + val, tpos[1] + 1]
        elif tpos == [hpos[0], hpos[1] - 1]:
            if val > 1:
                tpos = [tpos[0] + val - 1, tpos[1] + 1]
        elif tpos == [hpos[0] + 1, hpos[1] - 1]:
            if val > 2:
                tpos = [tpos[0] + val - 2, tpos[1] + 1]
        else:print(hpos,tpos,dir,val)
        for i in range(itpos[0]+1,tpos[0]+1):
            poses.append((i,tpos[1]))
        hpos = [hpos[0] + val, hpos[1]]
    elif dir == "L":
        if hpos == tpos:
            if val > 1:
                tpos = [tpos[0] - val + 1, tpos[1]]
        elif tpos == [hpos[0] - 1, hpos[1] + 1]:
            if val > 2:
                tpos = [tpos[0] - val + 2, tpos[1] - 1]
        elif tpos == [hpos[0], hpos[1] + 1]:
            if val > 1:
                tpos = [tpos[0] - val + 1, tpos[1] - 1]
        elif tpos == [hpos[0] + 1, hpos[1] + 1]:
            tpos = [tpos[0] - val, tpos[1] - 1]
        elif tpos == [hpos[0] - 1, hpos[1]]:
            if val > 2:
                tpos = [tpos[0] - val + 2, tpos[1]]
        elif tpos == [hpos[0] + 1, hpos[1]]:
            tpos = [tpos[0] - val, tpos[1]]
        elif tpos == [hpos[0] - 1, hpos[1] - 1]:
            if val > 2:
                tpos = [tpos[0] - val + 2, tpos[1] + 1]
        elif tpos == [hpos[0], hpos[1] - 1]:
            if val > 1:
                tpos = [tpos[0] - val + 1, tpos[1] + 1]
        elif tpos == [hpos[0] + 1, hpos[1] - 1]:
            tpos = [tpos[0] - val, tpos[1] + 1]
        else:
            print(hpos,tpos)
        for i in range(itpos[0]-1,tpos[0]-1,-1):
            poses.append((i,tpos[1]))
        hpos = [hpos[0] - val, hpos[1]]
    elif dir == "U":
        if hpos == tpos:
            if val > 1:
                tpos = [tpos[0], tpos[1] + val - 1]
        elif tpos == [hpos[0] - 1, hpos[1] + 1]:
            if val > 2:
                tpos = [tpos[0] + 1, tpos[1] + val - 2]
        elif tpos == [hpos[0], hpos[1] + 1]:
            if val > 2:
                tpos = [tpos[0], tpos[1] + val - 2]
        elif tpos == [hpos[0] + 1, hpos[1] + 1]:
            if val > 2:
                tpos = [tpos[0] - 1, tpos[1] + val - 2]
        elif tpos == [hpos[0] - 1, hpos[1]]:
            if val > 1:
                tpos = [tpos[0] + 1, tpos[1] + val - 1]
        elif tpos == [hpos[0] + 1, hpos[1]]:
            if val > 1:
                tpos = [tpos[0] - 1, tpos[1] + val - 1]
        elif tpos == [hpos[0] - 1, hpos[1] - 1]:
            tpos = [tpos[0] + 1, tpos[1] + val]
        elif tpos == [hpos[0], hpos[1] - 1]:
            tpos = [tpos[0], tpos[1] + val]
        elif tpos == [hpos[0] + 1, hpos[1] - 1]:
            tpos = [tpos[0] - 1, tpos[1] + val]
        else:
            print(hpos,tpos)
        for i in range(itpos[1]+1,tpos[1]+1):
            poses.append((tpos[0],i))
        hpos = [hpos[0], hpos[1] + val]
    elif dir == "D":
        if hpos == tpos:
            if val > 1:
                tpos = [tpos[0], tpos[1] - val + 1]
        elif tpos == [hpos[0] - 1, hpos[1] + 1]:
            tpos = [tpos[0] + 1, tpos[1] - val]
        elif tpos == [hpos[0], hpos[1] + 1]:
            tpos = [tpos[0], tpos[1] - val ]
        elif tpos == [hpos[0] + 1, hpos[1] + 1]:
            tpos = [tpos[0] - 1, tpos[1] - val]
        elif tpos == [hpos[0] - 1, hpos[1]]:
            if val > 1:
                tpos = [tpos[0] + 1, tpos[1] - val + 1]
        elif tpos == [hpos[0] + 1, hpos[1]]:
            if val > 1:
                tpos = [tpos[0] - 1, tpos[1] - val + 1]
        elif tpos == [hpos[0] - 1, hpos[1] - 1]:
            if val > 2:
                tpos = [tpos[0] + 1, tpos[1] - val + 2]
        elif tpos == [hpos[0], hpos[1] - 1]:
            if val > 2:
                tpos = [tpos[0], tpos[1] - val + 2]
        elif tpos == [hpos[0] + 1, hpos[1] - 1]:
            if val > 2:
                tpos = [tpos[0] - 1, tpos[1] - val + 2]
        else:
            pass
        for i in range(itpos[1]-1,tpos[1]-1,-1):
            poses.append((tpos[0],i))
        hpos = [hpos[0], hpos[1] - val]
    else:
        print(hpos,tpos)
    # print(hpos,tpos)
print(len(set(poses)))