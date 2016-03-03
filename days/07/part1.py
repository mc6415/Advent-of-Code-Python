import re
get_cmd = re.compile("[A-Z]+")
get_args = re.compile("[a-z0-9]+")

# Dictionary of the functions AND, OR etc.
funcs = {
    'AND': lambda a,b: a & b,
    'OR': lambda a,b: a | b,
    'LSHIFT': lambda a,b: a << b,
    'RSHIFT': lambda a,b: a >> b,
    'NOT': lambda a: ~a,
}

def resolve(symbol):
    if isinstance(symbol, int):
        return symbol
    value = wires[symbol]
    if not isinstance(value, tuple):
        return value
    command, args = value
    if not command:
        result = resolve(args[0])
        wires[symbol] = result
        return result
    else:
        resolved_args = [resolve(x) for x in args]
        result = funcs[command](*resolved_args)
        wires[symbol] = result
        return result
    
wires = {}

with open('../../input/day7.txt') as f:
    for line in f:
        command = get_cmd.search(line)
        args = get_args.findall(line)
        
        args = [int(x) if x.isdigit() else x for x in args]
        
        if command:
            command = command.group()
            
        to_wire = args.pop()
        
        wires[to_wire] = (command,tuple(args))
        
print resolve('a')