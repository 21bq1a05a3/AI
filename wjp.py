def wjp(start, end, J1, J2):
	path, front, visited = [], [], []
	front.append(start)
	while front:
		current = front.pop()
		x = current[0]
		y = current[1]
		path.append(current)
		if x == end or y == end:
			print ("Found!")
			return path
		
		if x < J1 and ([J1, y] not in visited):
			front.append([J1, y])
			visited.append([J1, y])

		if y < J2 and ([x, J2] not in visited):
			front.append([x, J2])
			visited.append([x, J2])

		if x >= J1 and ([0, y] not in visited):
			front.append([0, y])
			visited.append([0, y])

		if y >= J2 and ([J1, 0] not in visited):
			front.append([J1, 0])
			visited.append([J1, 0])

		if y > 0 and ([min(x + y, J1), max(0, x + y - J1)] not in visited):
			front.append([min(x + y, J1), max(0, x + y - J1)])
			visited.append([min(x + y, J1), max(0, x + y - J1)])

		if x > 0  and ([max(0, x + y - J2), min(x + y, J2)] not in visited):
			front.append([max(0, x + y - J2), min(x + y, J2)])
			visited.append([max(0, x + y - J2), min(x + y, J2)])

	return "Not found"

def gcd(a,b):
    if a==0:
        return b
    b=b%a
    return gcd(b,a)

print ("Solution for water jug problem")
J1 = int(input("Enter Jug 1 capacity:"))
J2 = int(input("Enter Jug 2 capacity:"))
end = int(input("Enter target volume:"))

start = [0, 0] 

if end % gcd(J1,J2) == 0:
	print(wjp(start, end, J1, J2))
else:
	print("No solution possible for this combination.")