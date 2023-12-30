# File app.py

import streamlit as st
from CYK import *  # Mengimpor fungsi cyk_parse dari CYK.py

# Fungsi utama untuk pengujian kalimat
def test_sentences():
    st.subheader("Sentences")

    with open('sentences.txt', 'r') as file:
        list_sentences = file.read().splitlines()

    # Inisialisasi file CNF
    file_path = 'cnf.txt'  # Ganti dengan nama file CNF Anda
    cnf = read_cnf_file(file_path)

    for sentence in list_sentences:
        cyk_parse(cnf, sentence)  # Memanggil fungsi cyk_parse dari CYK.py
        st.write(sentence)
        st.markdown('---')

def main():
    test_sentences()

if __name__ == "__main__":
    main()
