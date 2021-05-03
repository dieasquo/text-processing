from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import nltk
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

#Anggota Kelompok :

#Dimas Ibnu Malik - 1855201002
#Utrodus Said Albaqi - 1855201006
#Siti Robiatul Adawiyah - 1855201060
#Ahmad Ryan Noer Y. - 1855201062
#M. Haekal Azaim - 1855201064
#Yusup Komarudi A. - 1855201026
#Rifka Faridatul Maulida - 1855201042
#Subana - 1855201048



# Input String
def readFile():
    f = open("textcoba.txt", "r")
    input_file = f.read()
    return input_file

# Casefolding


def textCasefolding(input_file):
    casefolding = input_file.lower()
    return casefolding


# Transtlating
def translatingText(casefolded):
    translatedText = casefolded.translate(
        str.maketrans('', '', string.punctuation))
    return translatedText

# Steeming
def steemingProcess(translatedText):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    katadasar = stemmer.stem(translatedText)
    return katadasar

# Tokenization
def tokenizeText(katadasar):
    tokens = nltk.tokenize.word_tokenize(katadasar)
    return tokens


# Stop Word List dari Sastrawi
listStopword = set(stopwords.words('indonesian'))

# Penggunaan Stopword


def compareTextWithStopword(tokens):
    hasilTextProcessing = []
    for t in tokens:
        if t not in listStopword:
            hasilTextProcessing.append(t)
    return hasilTextProcessing





def main():
    #membaca file dan menyimpan value dalam variabel
    text_input = readFile()

    #casefolding / lowercase
    casefolded = textCasefolding(text_input)

    #translate text 
    translated = translatingText(casefolded)

    #steeming
    steemed = steemingProcess(translated)

    #Tokenization
    result = tokenizeText(steemed)




    print(result)

#run the App
main()

