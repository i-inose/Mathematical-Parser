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
	global number
	global symbol
	print("式を入力してください")
	n = input()
	num = ""
	for i in n:
		if i.isdigit():
			num += i
		else:
			number.append(int(num))
			num = ""
			symbol = i
	number.append(int(num))
	print(calc())

if __name__ == "__main__":
	solve()