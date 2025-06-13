from collections import Counter

def divide_and_conquer():
    wordsList = ['python', 'java', 'ottawa', 'ottawa', 'java', 'new']
    
    print(wordsList)
    
    wordPairs = [(word, 1) for word in wordsList]
    print(wordPairs)
    
    wordCounts = Counter()
    for word, count in wordPairs:
        wordCounts[word] += count
    
    wordCountsCollected = list(wordCounts.items())
    print(wordCountsCollected)
    
def dynamic_strategy():
    
    
    
def main():
    divide_and_conquer()
    
if __name__ == "__main__":
    main()