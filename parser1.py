number = []
symbol = ""

def calc():
	if symbol == "+":
		return number[0] + number[1]
	elif symbol == "-":
		return number[0] - number[1]
	elif symbol == "*":
		return number[0] * number[1]
	else:
		return number[0] / number[1]
	return

def solve():
	global symbol
	global number
	print("式を入力してください")
	n = input()
	for i in n:
		if i.isdigit():
			number.append(int(i))
		else:
			symbol = i
	print(calc())

if __name__ == "__main__":
	solve()