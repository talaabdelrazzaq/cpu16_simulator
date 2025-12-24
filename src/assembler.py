from isa import OPCODES, REGISTERS, R_FORMAT, I_FORMAT, D_FORMAT

def tokenize(line: str) -> list[str]:
    line = line.split("#", 1)[0]
    line = line.replace(","," ")
    line = line.replace("["," ")
    line = line.replace("]"," ")
    parts = line.split()
    return parts

def encode_r(tokens: list[str]) -> int:
    opcode = OPCODES[tokens[0]]
    rd = REGISTERS[tokens[1]]
    rn = REGISTERS[tokens[2]]
    rm = REGISTERS[tokens[3]]
    shift = 0
    # R-format: opcode[15-12] rd[11-9] rn[8-6] rm[5-3] shift[2-0]
    code = (opcode<<12|rd<<9|rn<<6|rm<<3|shift)
    code &= 0xFFFF
    return code

def encode_i(tokens: list[str]) -> int:
    opcode = OPCODES[tokens[0]]
    rd = REGISTERS[tokens[1]]
    rn = REGISTERS[tokens[2]]
    immediate = int(tokens[3], 0)
    immediate &= 0b111111 # mask immediate to 6 bits
    # I-format: opcode[15-12] rd[11-9] rn[8-6] immediate[5-0]
    code = (opcode<<12|rd<<9|rn<<6|immediate)
    code &= 0xFFFF
    return code

def encode_d(tokens: list[str]) -> int:
    opcode = OPCODES[tokens[0]]
    rt = REGISTERS[tokens[1]]
    rn = REGISTERS[tokens[2]]
    address = int(tokens[3])
    address &= 0b111111 # mask address to 6 bits
    # D-format: opcode[15-12] rt[11-9] rn[8-6] immediate[5-0]
    code = (opcode<<12|rt<<9|rn<<6|address)
    code &= 0xFFFF
    return code

def choose_encode(line: str):
    tokens = tokenize(line)
    if not tokens:
        return None
    
    op = tokens[0]

    if op in R_FORMAT: return encode_r(tokens)
    elif op in I_FORMAT: return encode_i(tokens)
    elif op in D_FORMAT: return encode_d(tokens)
    else: raise ValueError(f"Unknown opcode: {op}")



