# cc_plus.py

TOKEN_MAP = {
    "pofjjiojo0jig": "+",
    "fijofoifsjio": "-",
    "aesdrxtc": ">",
    "efekwpofe": "<",
    "oapofapfedpo": ".",
    "nierfdjni": ",",
    "poewkfwpoe": "[",
    "n": "]",
}

def CC_plus(code, input_func=input, output_func=print):
    # Convert CC+ code to Brainfuck code using 'b' as separator
    bf_code = ""
    for token in code.split('b'):
        if token in TOKEN_MAP:
            bf_code += TOKEN_MAP[token]

    # Run as Brainfuck
    code_ptr = 0
    tape = [0] * 30000
    tape_ptr = 0
    loop_stack = []

    while code_ptr < len(bf_code):
        cmd = bf_code[code_ptr]

        if cmd == '>':
            tape_ptr += 1
        elif cmd == '<':
            tape_ptr -= 1
        elif cmd == '+':
            tape[tape_ptr] = (tape[tape_ptr] + 1) % 256
        elif cmd == '-':
            tape[tape_ptr] = (tape[tape_ptr] - 1) % 256
        elif cmd == '.':
            output_func(chr(tape[tape_ptr]))
        elif cmd == ',':
            tape[tape_ptr] = ord(input_func()[0])
        elif cmd == '[':
            if tape[tape_ptr] == 0:
                open_brackets = 1
                while open_brackets != 0:
                    code_ptr += 1
                    if bf_code[code_ptr] == '[':
                        open_brackets += 1
                    elif bf_code[code_ptr] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(code_ptr)
        elif cmd == ']':
            if tape[tape_ptr] != 0:
                code_ptr = loop_stack[-1]
            else:
                loop_stack.pop()

        code_ptr += 1
