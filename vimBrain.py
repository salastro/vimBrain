def interpreter(code):
    array, starts, user, loops, i, pointer = [0]*30000, [], [], {}, 0, 0
    for index, instruction in enumerate(code):
        match instruction:
            case "q": starts.append(index)
            case "@": start = starts.pop(); loops[start] = index; loops[index] = start
    while i < len(code):
        match code[i]:
            case 'h': pointer -= 1
            case 'l': pointer += 1
            case 'k': array[pointer] += 1
            case 'j': array[pointer] -= 1
            case 'p': print(chr(array[pointer]), end='')
            case 'i': user = list(input() + "\n") if user == [] else user; array[pointer] = ord(user.pop(0))
            case 'q': i = loops[i] if not array[pointer] else i
            case '@': i = loops[i] if array[pointer] else i
        i += 1


interpreter("""
kkkkqlkkkkkhj@lqhkkkkklj@khkqlqlklkhhj@kkllqhhkllj@lllqj@kklqj@klllkqqj@kkkkkklll@hhhqqhkkkkkkkkhkkllj@khphqljjjjhj@h@hhqlllllqlllqj@kkkkkkkkkhqljhj@kkkkkkkkklqjqhjlj@kqhhh@@hqlkhj@l@hhj@hhj@
""")
