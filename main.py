#Україна україна чел чел чел чел мда ех ех ех

#Алфавітний порядок

def sort_words(input):
    text = input.split()
    text = [w.lower() + w for w in text]
    text.sort()
    text = [w[len(w)//2:] for w in text]
    return ' '.join(text)
while True:
    print('a: Сортувати в алфавітному порядку \nb: Топ5 слів \nc: Найдовші слова \nВиберіть операцію: ')
    choose = input()

    print("Text: ")
    text = input()

    if choose =='a':
        print(sort_words(text))

#Top5

    elif choose == "b":
        lst_no = ['.', ',', ':', '!', '"', "'", '[', ']', '-', '—', '(', ')']
        lst = []

        for text in text.lower().split():
            if not text in lst_no:
                _word = text
                if text[-1] in lst_no:
                    _word = _word[:-1]
                if text[0] in lst_no:
                    _word = _word[1:]
                lst.append(_word)
        _dict = dict()
        for text in lst:
            _dict[text] = _dict.get(text, 0) + 1

        _list = []
        for key, value in _dict.items():
            _list.append((value, key))
            _list.sort(reverse=True)

        for freq, text in _list[0:5]:
            print(f'{text:>10} -> {freq:>3}')

#Найдовше слово

    elif choose == 'c':
        d = text.lower
        l = text.split()
        q = ""
        for i in sorted(l, key=lambda b: len(b), reverse=True):
            q = q + " " + i
        print(q[0:9])