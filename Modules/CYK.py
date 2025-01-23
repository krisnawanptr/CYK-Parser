import streamlit as st
import pandas as pd


rhs_set = set()

def read_cnf_file(file):
    cnf = {}
    with open(file, 'r') as f:
        for line in f.readlines():
            lhs, rhs = line.strip().split(' -> ')
            cnf[lhs] = rhs.split(' | ')
    return cnf

def collect_rhs(cnf):
    for lhs, rule in cnf.items():
        for rhs in rule:
            rhs_set.update(rhs.split())

#MIT License: Copyright (c) 2023 gdapriana
def fill_diagonal(cnf, words, parsing_table):
    for i, word in enumerate(words):
        for lhs, rule in cnf.items():
            for rhs in rule:
                if len(rhs.split()) == 1 and rhs == word:
                    parsing_table[i][i].append(lhs)

#MIT License: Copyright (c) 2023 gdapriana
def fill_remaining(cnf, words, parsing_table):
    word_count = len(words) 
    for i in range(word_count):
        for j in range(i, -1, -1):
            for k in range(j, i + 1):
                for lhs, rule in cnf.items():
                    for rhs in rule:
                        rhs_split = rhs.split()
                        if len(rhs_split) == 2 and rhs_split[0] in parsing_table[j][k] and rhs_split[1] in parsing_table[k + 1][i]:
                            parsing_table[j][i].append(lhs)

def display_parsing_table(table):
    df = pd.DataFrame(table)
    st.dataframe(df)

def check_word_existence(words, rhs_set):
    for word in words:
        if word not in rhs_set:
            return -1
    return 1

def check_validity(parsing_table, cnf, exists):
    start_symbol = list(cnf.keys())[0]
    word_count = len(parsing_table) - 1

    if start_symbol in parsing_table[0][word_count - 1] and exists == 1:
        st.success('Kalimat sesuai dengan kaidah Bahasa Indonesia')
    elif exists == -1:
        st.warning('Kata dalam kalimat tidak terdapat pada rule')
    else:
        st.error('Kalimat tidak valid')

def cyk_parse(cnf, string):
    words = string.split()
    word_count = len(words)
    parsing_table = [[[] for _ in range(word_count)] for _ in range(word_count + 1)]

    collect_rhs(cnf)
    fill_diagonal(cnf, words, parsing_table)
    fill_remaining(cnf, words, parsing_table)

    exists = check_word_existence(words, rhs_set)
    check_validity(parsing_table, cnf, exists)
    
    st.write("### Tabel Parsing CYK:")
    display_parsing_table(parsing_table)


def main():
    file_path = 'cnf.txt'
    cnf = read_cnf_file(file_path)
    st.title("CYK Parser Kelompok F2")

    string_to_parse = st.text_input("Masukkan kalimat Bahasa Indonesia:")
    if st.button("Parse"):
        cyk_parse(cnf, string_to_parse)

if __name__ == "__main__":
    main()