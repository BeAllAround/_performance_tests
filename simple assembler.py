# performance tip - reduce the number of functions as much as possible and instead - write one - liners

def dec(scope, args):
    a = args[0]
    scope[a] -= 1
    return scope[a]

def inc(scope, args):
    a = args[0]
    scope[a] += 1
    return scope[a]

def get_v(scope, v):
    if v[0] == '-' or v[0].isdigit():
        return int(v)
    return scope[v]

def mov(scope, args):
    a = args[0]
    b = args[1]
    scope[a] = get_v(scope, b)
    
def jnz(scope, args):
    a = args[0]
    b = args[1]
    if get_v(scope, a) != 0:
        return get_v(scope, b)
    return 0

'''
def get_instruction(keyword):
    # has to be parsed each time we can this function therefore it is a tick more inefficient
    # move it to the scope where it is strictly used - which in this case will be 'simple assembler'
    ops = {'mov': mov, 'dec': dec, 'inc': inc, 'jnz': jnz,}
    return ops.get(keyword)
'''
    
def simple_assembler(program):
    # return a dictionary with the registers
    ops = {'mov': mov, 'dec': dec, 'inc': inc, 'jnz': jnz,}
    scope = {}
    map_instruct = {}
    for x, i in enumerate(program):
        options = i.split(' ')
        map_instruct[x] = {'op': options[0], 'args': options[1:]}
    # print(map_instruct)
    i = 0
    size = len(map_instruct) # static size
    while i < size:
        instruct = map_instruct[i]
        name = instruct['op']
        args = instruct['args']
        do = ops[name]
        if(do == jnz):
            d = do(scope, args)
            if d != 0:
                i += d - 1
        else:
            do(scope, args)
        i += 1
    return scope

'''
def simple_assembler(program):
    d, i = {}, 0
    while i < len(program):
        cmd, r, v = (program[i] + ' 0').split()[:3]
        if cmd == 'inc': d[r] += 1
        if cmd == 'dec': d[r] -= 1        
        if cmd == 'mov': d[r] = d[v] if v in d else int(v)
        if cmd == 'jnz' and (d[r] if r in d else int(r)): i += int(v) - 1
        i += 1
    return d

'''
'''
class Interpret:

    def __init__(self):
        self.vars = {}
        self.ins = {}
        self.pc = 0
        self.ins['mov'] = self.__ins_mov
        self.ins['inc'] = self.__ins_inc
        self.ins['dec'] = self.__ins_dec
        self.ins['jnz'] = self.__ins_jnz

    def get_value(self, v):
        if v in self.vars:
            return self.vars[v]
        else:
            return int(v)
    
    def run(self, code):
        while self.pc < len(code):
            ins = code[self.pc][:3]
            args = code[self.pc][3:].split()
            self.pc += 1;
            self.ins[ins](*args)

        return self.vars

    def __ins_mov(self, a, b):
        self.vars[a] = self.get_value(b)
        
    def __ins_inc(self, a):
        self.vars[a] += 1
        
    def __ins_dec(self, a):
        self.vars[a] -= 1
        
    def __ins_jnz(self, a, b):
        if self.get_value(a) != 0:
            self.pc += self.get_value(b) -1

def simple_assembler(program):
    # return a dictionary with the registers
    return Interpret().run(program)
'''
'''
# Blind4Basics
import re

def simple_assembler(program):
    registers, pointer = {}, 0
    while 0 <= pointer < len(program):
        cmd, x, _, y = re.findall(r'(\w+) (\S+)( (.+))?', program[pointer])[0]
        
        if   cmd == 'mov':    registers[x] = registers[y] if y.isalpha() else int(y)
        elif cmd == 'inc':    registers[x] = registers.get(x, 0) + 1
        elif cmd == 'dec':    registers[x] = registers.get(x, 0) - 1
        
        pointer += int(y) if cmd == 'jnz' and (registers[x] if x.isalpha() else int(x)) else 1
        
    return registers
'''

'''
#Keozon
actions = {}


def action(f):
    actions[f.__qualname__] = f
    return f


@action
def mov(line: str, state: dict):
    reg, val = line.split(" ")
    if val.isalpha():
        val = state[val]
    state[reg] = int(val)

    
@action
def inc(line: str, state: dict):
    state[line] += 1


@action
def dec(line: str, state: dict):
    state[line] -= 1

    
@action
def jnz(line: str, state: dict):
    condition, val = line.split(' ')
    if condition.isalpha():
        condition = state[condition]
    if condition:
        state["ptr"] += (int(val) -1)


def simple_assembler(program):
    state = {"ptr": 0}
    while state["ptr"] < len(program):
        instruction, args = program[state["ptr"]].split(" ", 1)
        actions[instruction](args, state)
        state["ptr"] += 1
    
    del state["ptr"]
    return state
'''

from time import time
i = 0
while i < 10:
    code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
    start = time()
    print(simple_assembler(code.splitlines()))
    print(time() - start)
    i += 1


code = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a
bob a
'''
# print(simple_assembler(['mov a -10', 'mov b a', 'inc a', 'dec b', 'jnz a -2',]))

