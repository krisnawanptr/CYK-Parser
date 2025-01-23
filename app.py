import streamlit as st
from Modules.CYK import * 


def test_sentences():
    st.subheader("Sentences")

    with open('Modules/sentences.txt', 'r') as file:
        list_sentences = file.read().splitlines()

    file_path = 'Modules/cnf.txt' 
    cnf = read_cnf_file(file_path)

    for sentence in list_sentences:
        cyk_parse(cnf, sentence)  
        st.write(sentence)
        st.markdown('---')

def main():
    test_sentences()

if __name__ == "__main__":
    main()
