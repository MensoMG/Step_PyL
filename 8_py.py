one = float(input())
two = float(input())
oper = input()

if two == 0 and (oper == "mod" or oper =="/" or oper =="div"):
    print("Деление на 0!")
elif oper == "+":   print(one + two)
elif oper == "-":   print(one - two)
elif oper == "/":   print(one / two)
elif oper == "*":   print(one*two)
elif oper == "mod": print(one % two)
elif oper == "pow": print(one**two)
elif oper == "div": print(one//two)
