OPCODES={
    #R-Format Instructions
    "ADD": 0b0000,
    "SUB": 0b0001,
    "MUL":0b0010,
    "MOD":0b0011,
    "AND":0b0100,
    "OR":0b0101,
    "XOR":0b0110,
    "LSL":0b0111,
    "LSR":0b1000,
    "CHECK":0b1001,

    #I-Format Instructions
    "ADDI":0b1010,
    "SUBI":0b1011,
    "SETI":0b1100,

    #D-Format Instructions
    "LOAD":0b1101,
    "STORE":0b1110,
    "BRANCH":0b1111,

}

REGISTERS={
    "T0":0b000, # Hardwired to the constant value "0"
    "T1":0b001,
    "T2":0b010,
    "T3":0b011,
    "T4":0b100,
    "T5":0b101,
    "T6":0b110,
    "T7":0b111,
}

R_FORMAT = {"ADD","SUB","MUL","MOD","AND","OR","XOR","LSL","LSR","CHECK"}
I_FORMAT = {"ADDI","SUBI","SETI"}
D_FORMAT = {"LOAD","STORE","BRANCH"}