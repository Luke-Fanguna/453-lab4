import sys

def read_file() -> list:
    request = []
    with open(sys.argv[-1], 'r') as file:
        content = file.read().strip()
    request = content.split('\n')
    request = [int(req) for req in request]
    return request

# handle each request as it comes
def fcfs(request : list,position : int):
    total,request = 0,request.copy()
    # finds the distance between the current position and the next request
    for r in request:
        total += abs(position - r)
        position = r
    return total
    
def sstf(request : list,position : int):
    total, request = 0, sorted(request.copy())
    while request:
        closest = min(request, key=lambda r: abs(position - r))
        total += abs(position - closest)
        request.remove(closest)
        position = closest
    return total

def scan(request : list,direction : str,position : int):
    total,max,min = 0,4999,0
    request = sorted(request.copy())
    left = []
    right = []
    for req in request:
        if position >= req:
            left.append(req)
    for req in request:
        if position < req:
            right.append(req)
    if direction == '+':
        if len(right) != 0 and len(left) != 0:
            total += abs(max-position) + left[0]
        elif len(left) != 0 and len(right) == 0:
            total += abs(left[0] - position)
        elif len(right) != 0 and len(left) == 0:
            total += abs(position - right[-1])
        else:
            total = 0
    elif direction == '-':
        if len(right) != 0 and len(left) != 0:
            total += position + right[-1]
        elif len(left) != 0 and len(right) == 0:
            total += abs(left[0] - position)
        elif len(right) != 0 and len(left) == 0:
            total += abs(position - right[-1])
        else:
            total = 0
    return total

def cscan(request : list,direction : str,position : int):
    total,max,min = 0,4999,0
    request = sorted(request.copy())
    left = []
    right = []

    for req in request:
        if position >= req:
            left.append(req)
    for req in request:
        if position < req:
            right.append(req)
    if direction == '+':
        if len(right) != 0 and len(left) != 0:
            total += abs(max-position) + abs(min-left[-1])
        elif len(left) != 0 and len(right) == 0:
            total += abs(left[0] - position)
        elif len(right) != 0 and len(left) == 0:
            total += abs(position - right[-1])
        else:
            total = 0
    elif direction == '-':
        if len(right) != 0 and len(left) != 0:
            total += abs(0-position) + abs(4999 - right[0])
        elif len(left) != 0 and len(right) == 0:
            total += abs(left[0] - position)
        elif len(right) != 0 and len(left) == 0:
            total += abs(position - right[-1])
        else:
            total = 0
    return total

def look(request : list,direction : str,position : int):
    total = 0
    request = sorted(request.copy())
    left = []
    right = []
    for req in request:
        if position >= req:
            left.append(req)
    for req in request:
        if position < req:
            right.append(req)
    if direction == '+':
        if len(right) != 0 and len(left) != 0:
            total += abs(right[-1]-position) + abs(right[-1]-left[0])
        elif len(left) != 0 and len(right) == 0:
            total += abs(left[0] - position)
        elif len(right) != 0 and len(left) == 0:
            total += abs(position - right[-1])
        else:
            total = 0
    elif direction == '-':
        if len(right) != 0 and len(left) != 0:
            total += abs(left[0]-position) + abs(left[0] - right[-1])
        elif len(left) != 0 and len(right) == 0:
            total += abs(left[0] - position)
        elif len(right) != 0 and len(left) == 0:
            total += abs(position - right[-1])
        else:
            total = 0
    return total

def clook(request : list,direction : str,position : int):
    total = 0
    request = sorted(request.copy())
    left = []
    right = []
    for req in request:
        if position >= req:
            left.append(req)
    for req in request:
        if position < req:
            right.append(req)
    if direction == '+':
        if len(right) != 0 and len(left) != 0:
            total += abs(right[-1]-position) + abs(left[-1] - left[0])
        elif len(left) != 0 and len(right) == 0:
            total += abs(left[0] - position)
        elif len(right) != 0 and len(left) == 0:
            total += abs(position - right[-1])
        else:
            total = 0
    elif direction == '-':
        if len(right) != 0 and len(left) != 0:
            total += abs(left[0]-position) + abs(right[-1] - right[0])
        elif len(left) != 0 and len(right) == 0:
            total += abs(left[0] - position)
        elif len(right) != 0 and len(left) == 0:
            total += abs(position - right[-1])
        else:
            total = 0
    return total

def main():
    if sys.argv[1][0].isdigit():
        position = int(sys.argv[1][0])
        direction = '+'
    else:
        position = int(sys.argv[1][1:])
        direction = sys.argv[1][0]

    request = read_file()

    print("FCFS",fcfs(request,position))
    print("SSTF",sstf(request,position))
    print("SCAN",scan(request,direction,position))
    print("C-SCAN",cscan(request,direction,position))
    print("LOOK",look(request,direction,position))
    print("C-LOOK",clook(request,direction,position))
    
if __name__ == '__main__':
    main()