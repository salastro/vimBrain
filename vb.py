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


def converter(code):
    return code.replace('<', 'h').replace('>', 'l').replace('+', 'k').replace('-', 'j').replace('.', 'p').replace(',', 'i').replace('[', 'q').replace(']', '@')
