import re
import numpy as np
from scipy.spatial.distance import cosine


words = []
sentences = []
count_of_sentences = 0
for line in open("sentences.txt"):
    count_of_sentences += 1
    s = line
    y = s.lower()
    text = re.split('[^a-z]', y)
    lines = list(filter(bool, map(str.rstrip, text)))
    words += lines
    sentences.append(lines)
    print("Предложение номер {}".format(count_of_sentences), lines)

words_set = set(words)
i = iter(range(len(words_set)))
words_dict = {next(i):word for word in words_set}
print(words_dict)

n, d = len(sentences), len(words_dict)
word_matrix = np.zeros(shape=(n, d))
for i in range(n):
    for j in range(d):
        word_matrix[i][j] = sentences[i].count(words_dict[j])

print(word_matrix.shape)
print(word_matrix)


cos_0 = []
for i in range(n):
    cos_0.append(cosine(word_matrix[0], word_matrix[i]))

cos_0 = np.array(cos_0)
cos_0[1:].argsort()
print(cos_0)
first_answer = (cos_0[1:].argmin() + 1)
cos_0 = np.delete(cos_0, first_answer)
second_answer = (cos_0[1:].argmin() + 1)
print("Индекс первого наименьшего элемента: ", first_answer)
print("Индекс второго наименьшего элемента: ", second_answer)


with open('task_1.txt', 'w') as f:
    f.write("{} {}".format(first_answer, second_answer))