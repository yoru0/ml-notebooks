# GSLC Natural Language Processing – Pertemuan 9

## 1. Apa itu Context-Free Grammar (CFG) dan berdasarkan analisa kamu apa kegunaan dari CFG dalam NLP?

Context-Free Grammar (CFG) adalah sistem formal yang digunakan untuk mendeskripsikan class bahasa yang dikenal dengan Context-Free Language (CFL). CFG terdiri dari:

- **V** -> Nonterminal symbols (variables): Merepresentasikan kategori abstrak (misalnya kalimat, frasa)
- **Σ** -> Terminal symbols (alphabet): Token dasar dari bahasa (misalnya kata-kata seperti 'anjing', 'berjalan')
- **P** -> Production rules: Aturan yg mendefinisikan bagaimana simbol non terminal dapat diubah menjadi simbol terminal atau non terminal lainnya.
- **S** -> Start symbol: Simbol non terminal dari mana derivasi dimulai.

Dalam NLP, CFG ini digunakan untuk generate kalimat dalam suatu bahasa atau untuk parsing kalimat, dimana input kalimat akan dianalisis untuk menentukan apakah kalimat tersebut dapat digenerate oleh grammar, dan jika iya, bagaimana cara menghasilkannya.

## 2. Apa itu Grammar Rules dan berdasarkan analisa kamu apa kegunaannya dalam menyusun CFG menjadi sebuah parse tree?

Grammar rules (production rules) adalah elemen-elemen himpunan P dalam CFG yang berbentuk:

A ->

Parse Tree (derivation tree) adalah pohon berakar yang merepresentasikan struktur sintaksis suatu string menurut CFG.

- Node internal merepresentasikan non terminal
- Daun (leaf nodes) merepresentasikan terminal sesuai urutan input
- Setiap cabang mengikuti production rules yang diterapkan saat proses parsing

Peran production rules dalam menyusun parse tree:

- **Instruksi derivasi:** production rules memberikan blurprint bagaimana sebuah node non terminal diperluas menjadi anak-anaknya, sesuai aturan simbol pada sisi kanan aturan
- **Kontrol ambiguitas:** dalam grammar yang ambiguous, satu string bisa memiliki beberapa parse tree karena pilihan aturan produksi berbeda.
- **Dasar algorita parsing:** Algoritma seperti Earley, CYK, atau LALR menggunakan production rules untuk mencari derivasi yabg valid dan membangun struktur pohon secara efisien

## 3. Eksplor dan berikan 1 library python yang dapat digunakan untuk membantumu membuat CFG!

Bisa menggunakan library Natural Language Toolkit (NLTK) di python yang memberikan tools untuk bekerja dengan CFG. Implementasinya:

```python
import nltk

grammar_string = """
    S -> NP VP
    NP -> Det N | NP PP
    VP -> V | V NP | V NP PP
    PP -> P NP
    Det -> 'a' | 'the'
    N -> 'cat' | 'dog' | 'man'
    V -> 'saw' | 'chased'
    P -> 'in' | 'on'
"""
grammar = nltk.CFG.fromstring(grammar_string)
print(grammar)

sentence = "the cat saw a man in the park".split()
parser = nltk.ChartParser(grammar)
trees = list(parser.parse(sentence))

for tree in trees:
    print(tree)
    tree.pretty_print() # Displays the tree graphically (requires installation of ghostscript)

from nltk.parse.generate import generate

for sentence in generate(grammar, n=10): # Generates at most 10 sentences
    print(' '.join(sentence))
```

code diatas digenerate dari AI google

Menggunakan library NLTK ini untuk CFG cukup simple, dengan mendefinisikan grammar menggunakan CFG.fromstring(), lalu pilih parser yang sesuai di nltk.parse, lalu panggil metode parse() pada token kalimat.

## Referensi

- <https://www.geeksforgeeks.org/what-is-context-free-grammar/>
- <https://en.wikipedia.org/wiki/Context-free_grammar>
- <https://medium.com/@avinashmachinelearninginfo/cfg-in-nlp-fcf812baa939>
- <https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computation_Fundamentals/Foundations_of_Computation_(Critchlow_and_Eck)/04%3A_Grammars/4.01%3A_Context-free_Grammars>
- <https://medium.com/@ivarrvinter/context-free-grammar-in-python-using-nltk-for-nlp-examples-d76726514897>
- <https://www.nltk.org/api/nltk.grammar.CFG.html>
