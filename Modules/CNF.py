def read_cfg(file_name):
    grammar = {}
    with open(file_name, 'r') as file:
        cfg = file.read().splitlines()

    for rule in cfg:
        lhs, rhs = rule.split(' -> ')
        if lhs not in grammar:
            grammar[lhs] = []
        grammar[lhs].extend(rhs.split(' | '))

    return grammar


def convert_to_cnf(grammar):
    start_symbol = 'K'
    new_ls = []
    new_rs = []

    while max(len(item.split(' ')) for item in grammar[start_symbol]) > 2:
        keys = list(grammar.keys())
        for lhs in keys:
            for rhs_key in keys:
                if lhs in grammar[rhs_key]:
                    grammar[rhs_key].remove(lhs)
                    grammar[rhs_key].extend(grammar[lhs])

        for rule in grammar[start_symbol]:
            if len(rule.split(' ')) > 2:
                lst_check_val = rule.split(' ')
                temp = ''
                index = next((i for i, val in enumerate(new_rs) if val in rule), -1)
                if index == -1:
                    add_val = ' '.join(lst_check_val[0:2])
                    new_ls.append('X' + str(len(new_ls)+1))
                    new_rs.append(add_val)
                    temp = rule.replace(add_val, new_ls[-1])
                    grammar[new_ls[-1]] = [add_val]
                else:
                    temp = rule.replace(new_rs[index], new_ls[index])
                grammar[start_symbol][grammar[start_symbol].index(rule)] = temp

    return grammar


def write_to_file(grammar, file_name):
    with open(file_name, 'w') as write_cnf:
        for lhs in grammar:
            write_cnf.write(f"{lhs} -> {' | '.join(grammar[lhs])}\n")

def main():
    input_file = 'cfg.txt'
    output_file = 'cnf.txt'
    cfg = read_cfg(input_file)
    cnf = convert_to_cnf(cfg)
    write_to_file(cnf, output_file)


if __name__ == "__main__":
    main()

