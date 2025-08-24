#Exercise 16: Count Unique Words
sentence = "dog is a simple animal dogs is selfless animal"
words = sentence.lower().split()
set_sentence=set(words)
print(f"Number of unique words: {len(set_sentence)}")
