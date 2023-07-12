import csv
import spacy

def lemmatized_csv():
    ### Utility used to lemmetize the .csv of common French words to their dictionary form 
    # Not part of the main pipeline - keeping script in case the top_1000_french_words.csv is updated with a different wordlist
    wordfile = "assets/top_1000_french_words.csv"
    lemmatized_wordfile = "assets/top_1000_french_words_lem.csv"
    with open(wordfile, "r") as f:
        data_raw = f.readlines()
        data = list(map(lambda x: x.strip(), data_raw))
    with open(lemmatized_wordfile, "w") as f:
        writer = csv.writer(f)
        nlp = spacy.load("fr_core_news_md")
        lemmatized_words = []

        for word in data:
            doc = nlp(word)
            for token in doc:
                lemmatized_word = token.lemma_
                if lemmatized_word not in lemmatized_words:
                    lemmatized_words.append(lemmatized_word)
        for word in lemmatized_words:
            writer.writerow([word])
        print(len(lemmatized_words))


lemmatized_csv()