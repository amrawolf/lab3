from collections import Counter

#Алфавітний порядок

def sort_words(input):
    text = input.split()
    text = [w.lower() + w for w in text]
    text.sort()
    text = [w[len(w)//2:] for w in text]
    return ' '.join(text)

print('Choose a, b ,c: ')
choose = input()

print("Text: ")
text = input()

if choose =='a':
    print(sort_words(text))

## СЛОВА ПО КІЛЬКОСТІ СИМВОЛІВ

#text=str(input("Enter text: "))
#newList = sorted(text)
#n=sorted(text.split())
#print(n)
#w=text.split()
#e=""
#for r in sorted(w):
    #e=e+" " +r
#print(e)
#l = text.split()
#q=""
#for i in sorted(l,key=lambda a: len(a)):
    #q = q + " " + i
#print(q)

if choose == 'b':
    d = Counter(text)
    print(d)
