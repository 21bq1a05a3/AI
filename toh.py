def toh(n , src, dest, aux, step=1):
    if n==1:
        print ('Step ',step, ": Move disk 1 from peg",src,"to peg",dest)
        if src == 'A':
            A.remove(1)
        elif src == 'B':
            B.remove(1)
        else:
            C.remove(1)
        if dest == 'A':
            A.append(1)
        elif dest == 'B':
            B.append(1)
        else:
            C.append(1)
        print("A:", *A,'\nB:',*B,'\nC:',*C)
        return step+1
    step = toh(n-1, src, aux, dest, step)
    print ('Step ',step, ": Move disk",n,"from peg",src,"to peg",dest)
    if src == 'A':
        A.remove(n)
    elif src == 'B':
        B.remove(n)
    else:
        C.remove(n)
    if dest == 'A':
        A.append(n)
    elif dest == 'B':
        B.append(n)
    else:
        C.append(n)
    print("A:", *A,'\nB:',*B,'\nC:',*C)
    step = toh(n-1, aux, dest, src, step+1)
    return step

n = int(input('Enter number of disks : '))
A,B,C = [i for i in range(n, 0, -1)],[],[]
print('Initial State : ')
print("A:", *A,'\nB:',*B,'\nC:',*C)
toh(n,'A','C','B', 1)
print('\nGoal State reached')
