import jsgf
from os import listdir
from os.path import isfile, join


gram_dir = './gramatyki/'
grammar_files = [file for file in listdir(gram_dir) if isfile(join(gram_dir, file))]

grammars = []

for grammarFile in grammar_files:
    grammar = jsgf.parse_grammar_file(gram_dir + grammarFile)
    grammars.append(grammar)

lines = []

data_dir = './data/'
data_files = [file for file in listdir(data_dir) if isfile(join(data_dir, file))]

detected = 0

for file in data_files:
    f = open(f'{data_dir}{file}', "r")
    for line in f:
        sep = line.split('\t')
        if sep[0] == 'user':
            lines.append([sep[1], sep[2]])


def get_dialog_act(rule):
    slots = []
    get_slots(rule.expansion, slots)
    global detected
    detected = detected + 1
    return {'act': rule.grammar.name, 'slots': slots}


def get_slots(expansion, slots):
    if expansion.tag != '':
        slots.append((expansion.tag, expansion.current_match))
        return

    for child in expansion.children:
        get_slots(child, slots)

    if not expansion.children and isinstance(expansion, jsgf.NamedRuleRef):
        get_slots(expansion.referenced_rule.expansion, slots)


def nlu(utterance):
    matched = None
    for _grammar in grammars:
        matched = _grammar.find_matching_rules(utterance)
        if matched:
            break

    if matched:
        return get_dialog_act(matched[0])
    else:
        return {'act': 'null', 'slots': []}


for line in lines:
    nlu(line[0])

print(f'{round((detected/len(lines)*100),2)}%')