import random
from turtle import Turtle

# entities for lsystem
# start - start string
# rules - list of rules as tuples
# angle - angle for rotation
# forwards - letters on which we should draw

koch = {
    "start" : "F--F--F",
    "rules" : [
        ("F","F+F--F+F")
    ],
    "angle" : 60,
    "forwards" : ["F"]
}

sierpinski = {
    "start" : "A",
    "rules" : [
        ("A","B-A-B"),
        ("B","A+B+A")
    ],
    "angle" : 60,
    "forwards" : ["A","B"]
}

hilbert = {
    "start" : "B",
    "rules" : [
        ("A","-BF+AFA+FB-"),
        ("B","+AF-BFB-FA+")
    ],
    "angle" : 90,
    "forwards" : ["F"]
}

tree1 = {
    "start" : "A",
    "rules" : [
        ("A","F[+A]-A"),
        ("F","FF")
    ],
    "angle" : 45,
    "forwards" : ["F","A"]
}

tree2 = {
    "start" : "A",
    "rules" : [
        ("A","F-[[A]+A]+F[+FA]-A"),
        ("F","FF")
    ],
    "angle" : 25,
    "forwards" : ["F","A"]
}

tree_random_rule = {
    "start" : "F",
    "rules" : [
        ("F","F[+F]F[-F]F"),
        ("F","F[+F]F"),
        ("F","F[-F]F")
    ],
    "angle" : 30,
    "forwards" : ["F"]
}

# other - source http://paulbourke.net/fractals/lsys/

dragoncurve = {
    "start" : "FX",
    "rules" : [
        ("X","X+YF+"),
        ("Y","-FX-Y")
    ],
    "angle" : 90,
    "forwards" : ["F"]
}

bush = {
    "start" : "Y",
    "rules" : [
        ("X","X[-FFF][+FFF]FX"),
        ("Y","YFX[+Y][-Y]"),
    ],
    "angle" : 25,
    "forwards" : ["F"]
}

# experiments

hilbert_91degrees = {
    "start" : "B",
    "rules" : [
        ("A","-BF+AFA+FB-"),
        ("B","+AF-BFB-FA+")
    ],
    "angle" : 91,
    "forwards" : ["F"]
}

def get_rules(nonterminal, rules):
    out = []
    for rule in rules:
        if rule[0] == nonterminal:
            out.append(rule[1])
    return out

def rewrite(string, rules):
    out = ""
    for c in string:
        if c in ["+","-","[","]"]:
            out += c
        elif c.isalpha():
            work_rules = get_rules(c,rules)
            if len(work_rules) == 0: # No rule
                out += c
            elif len(work_rules) == 1: # One rule, rewrite it
                out += work_rules[0]
            else: # More rules, choose random one
                out += random.choice(work_rules)
    return out

def draw(filename,string,angle,forwards):
    t = Turtle()
    for c in string:
        if c == "-":
            t.left(angle)
        elif c == "+":
            t.right(angle)
        elif c == "[":
            t.push()
        elif c == "]":
            t.pop()
        elif c in forwards:
            t.forward(10)
    t.save_to_file(filename)


def lsystem(entity,filename, rewrites = 3):
    string = entity["start"]
    for _ in range(rewrites):
        string = rewrite(string,entity["rules"])
    draw(filename,string,entity["angle"],entity["forwards"])

for i in range(5):
    lsystem(koch, "koch{}.svg".format(i),i)

for i in range(4,8):
    lsystem(sierpinski, "sierpinski{}.svg".format(i),i)

for i in range(1,7):
    lsystem(hilbert,"hilbert{}.svg".format(i),i)
    lsystem(hilbert_91degrees,"hilbert_91degrees{}.svg".format(i),i)
    
for i in range(1,7):
    lsystem(tree1,"tree1-{}.svg".format(i),i)
    lsystem(tree2,"tree2-{}.svg".format(i),i)

for i in range(5):
    lsystem(tree_random_rule,"tree-random-rule-{}.svg".format(i),5)

for i in [9,10,11,12,13]:
    lsystem(dragoncurve,"dragoncurve{}.svg".format(i),i)

for i in range(3,7):
    lsystem(bush,"bush{}.svg".format(i),i)
