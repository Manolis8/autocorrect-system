import csv
import Levenshtein

def load_words_from_csv(file_path):
    words = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            words.append(row[0].lower())
    return words

def get_recommendations(word, valid_words):
    distances = [(valid_word, Levenshtein.distance(word, valid_word)) for valid_word in valid_words]
    distances.sort(key=lambda x: x[1])
    return [word for word, distance in distances[:5]]

def spell_check(word, valid_words):
    if word in valid_words:
        return f"'{word}' is spelled correctly!"
    else:
        recommendations = get_recommendations(word, valid_words)
        return f"'{word}' is not spelled correctly. Did you mean: {', '.join(recommendations)}?"

word_list = load_words_from_csv('nltk_words.csv')

while True:
    user_word = input("Enter a word (or type 'exit' to quit): ").lower()
    if user_word == 'exit':
        break
    result = spell_check(user_word, word_list)
    print(result)
