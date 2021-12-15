# creates a program to reverse a sentence
def reverse(sentence):
    newsentence = sentence.replace(".", "")
    words = sentence.split(" ")
    connect = ' '.join(reversed(words))
    return connect + "."


if __name__ == "__main__":
    input = "geeks quiz practice code."
    print (reverse(input))