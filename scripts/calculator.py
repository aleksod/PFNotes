import math

exit_status = False
stack = list()

while not exit_status:

    line = str(raw_input("User Input: ")).strip()

    if line == "exit":
        exit_status = True
    else:
        tokens = line.split()

        for token in tokens:
            if token == "+":
                temp_result = stack.pop(-2) + stack.pop(-1)
                stack.append(float(temp_result))
            elif token == "-":
                temp_result = stack.pop(-2) - stack.pop(-1)
                stack.append(float(temp_result))
            elif token == "*":
                temp_result = stack.pop(-2) * stack.pop(-1)
                stack.append(float(temp_result))
            elif token == "/":
                temp_result = stack.pop(-2) / stack.pop(-1)
                stack.append(float(temp_result))
            elif token == "sin":
                temp_result = math.sin(stack.pop())
                stack.append(float(temp_result))
            elif token == "cos":
                temp_result = math.cos(stack.pop())
                stack.append(float(temp_result))
            elif token == "tan":
                temp_result = math.tan(stack.pop())
                stack.append(float(temp_result))
            elif token == "pi":
                stack.append(float(math.pi))
            else:
                stack.append(float(token))

        if len(stack)>1:
            print "Stack size greater than 1"
        else:
            print stack[0]

        stack = list()
