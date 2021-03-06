import sys

stack = []
while True:
    line = sys.stdin.readline().rstrip() ##복습
    if line == '.':
        sys.exit()
    else:
        for i in range(len(line)):
            if (line[i] == '(') or (line[i] == '['):
                stack.append(line[i])
                continue
            elif (line[i] == ')') or (line[i] == ']'):
                if len(stack) > 0:
                    if stack[-1] == '(':
                        if line[i] == ')':
                            stack.pop(-1)
                        else:
                            stack.append(line[i])
                    elif stack[-1] == '[':
                        if line[i] == ']':
                            stack.pop(-1)
                        else:
                            stack.append(line[i])
                    else:
                        continue
                else:
                    stack.append(line[i])
            else:
                continue
        if len(stack) == 0:
            print('yes')
        else:
            print('no')
        stack = []
