def integer(act, num1, num2):
    if act == "+":
        return(num1 + num2)
    elif act == "-":
        return(num1 - num2)
    elif act == "*":
        return(num1 * num2)
    elif act == "/":
        if num2 == 0:
            return("∞")
        elif num2 == 0 and num1 == 0:
            return("nan")
        else:
            return(num1 / num2)