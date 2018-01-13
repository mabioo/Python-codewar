# -*- coding:utf-8 -*-
#将字串中的长度大于5的单词反向

def spin_words(sentence):
    sentences = sentence.split(" ")
    print (sentences)
    targetstr = []
    for i in sentences:
        print (len(i))
        if len(i)>5:
            targetstr.append( i[::-1] )
        else:
            targetstr.append(i)
    return " ".join( i for i in targetstr)

if __name__ == "__main__":
    print (spin_words("Hey fellow warriors"))

#best solution:
# def spin_words(sentence):
#     # Your code goes here
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

