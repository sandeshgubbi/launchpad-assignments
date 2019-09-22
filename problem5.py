def reve(sen):
    word=sen.split(" ")
    word=word[-1::-1]
    y=' '.join(word)
    return y
if __name__ == "__main__":
    sen=input("enter the sentence: ")
    sen=str(sen)
    print((reve(sen)).capitalize())