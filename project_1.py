import math

operator = str(input("enter operator (+, -, *, /, pow, sqrt, cos, sin, tan, ctan, !): "))

try:
    if operator == "cos" or operator == "sin" or operator == "tan" or operator == "!" or operator == "sqrt":
        num = int(input("enter value: "))
    else:
        first_num = int(input("enter first number: "))
        second_num = int(input("enter second number: "))
except ValueError:
    print("please enter valid value")
    
flag = 0
result = 0

while True:
    match operator:
        case "+":
            if flag == 0:
                result += first_num + second_num
            else:
                result += cont_num
            print("result: ", result)
        case "-":
            if flag == 0:
                result += first_num + second_num
            else:
                result -= cont_num
            print("result: ", result)
        case "*":
            if flag == 0:
                result += first_num * second_num
            else:
                result *= cont_num
            print("result: ", result)
        case "/":
            if flag == 0:
                if second_num == 0:
                    print("div wrong")
                    break
                else:
                    result += first_num / second_num
            else:
                if cont_num == 0:
                    print("div wrong")
                    break
                else:
                    result /= cont_num
            print("result: ", result)
        case "!":
            if flag == 0:
                if num > 0:
                    result += math.factorial(num)
                else:
                    print("fatal error")
            else:
                if cont_num > 0:
                    result += math.factorial(cont_num)
                else:
                    print("fatal error")            
            print("result: ", result)
        case "pow":
            if flag == 0:
                result += math.pow(first_num, second_num)
            else:
                result += math.pow(cont_num, cont_num2)
            print("result: ", result)
        case "sqrt":
            if flag == 0:
                if num > 0:
                    result += math.sqrt(num)
                else:
                    print("fatal error")            
            else:
                if num > 0:
                    result += math.sqrt(cont_num)
                else:
                    print("fatal error")              
            print("result: ", result)
        case "sin":
            if flag == 0:
                result += math.sin(num)
                print("result: ", result)
            else:
                result += math.sin(cont_num)
                print("result: ", result)
        case "cos":
            if flag == 0:
                result += math.cos(num)
                print("result: ", result)
            else: 
                result += math.cos(cont_num)
                print("result: ", result)        
        case "tan":
            if flag == 0:
                result += math.tan(num)
                print("result: ", result)
            else:
                result += math.tan(cont_num)
                print("result: ", result)        
        case "ctan":
            if flag == 0:
                result += math.tan(num)
                print("result: ", result)
            else: 
                result += math.tan(cont_num)
                print("result: ", result)
        case _:
            print("something wrong")
    flag = 1
    print("do you wnat more? y/n")
    v68 = str(input())
    if v68 == "y":
        operator = str(input("enter new operator (+, -, *, /, pow, sqrt, cos, sin, tan, ctan, !): "))
        try:
            cont_num = int(input("enter num: "))
            if operator == "pow":
                cont_num2 = int(input("enter next number: "))
        except ValueError:
            break
        continue
    elif v68 == "n":
        print("cya <3")
        break
    else:
        break
