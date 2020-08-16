def read_txt(filename):
    with open(filename, 'r') as file_handle:
        string = (file_handle.read()).lower().replace(',', ' ').replace('.', ' ')
        l = string.split(' ')
    return l

def create_txt(data):
    with open('sequences.txt', 'a') as file_created:
        file_created.write(data)


def positions(filename, token_words):
    positions = {}
    with open(filename, 'r') as file_ocurr:
        read = file_ocurr.read().lower().replace(',', ' ').replace('.', ' ')
        for pos, i in enumerate(read.split(' ')):
            if i == token_words:
                positions[pos] = i
    return positions

def sequences(lst):   
    for count_seq in range(1, 5): # 21
        if count_seq == 1:
            sequence = (list(dict.fromkeys([' '.join(lst[i:i+count_seq]) for i in range(len(lst))])))
            for token_word in sequence:
                positions('result.txt', token_words=token_word)
        else:
            sequence = ', '.join([' '.join(lst[i:i+count_seq]) for i in range(len(lst))])
            create_txt(data=sequence + '.\n')

        
if __name__ == "__main__":
    filename = 'result.txt'
    file_handle = read_txt(filename)
    LENGHT = 20
    words = []

    for word in file_handle:
        words.append(word)
        if len(words) == LENGHT:
            LENGHT += 20
            sequences(lst=words)
            words = []

    #token_words = input(f'\nInput word/s to search on {filename}\n\t> ')
    file_result = 'sequences.txt'

    print(f'\nFrom {file_result}, positions of {token_words}')
    d_pos = positions(filename=file_result, token_words=token_words)
    for key, value in d_pos.items():
        print(f'Pos: {key} | Word: {value}') 
    print(f'\n- Total of {token_words} ocurrences: {len(d_pos)}\n')
    
    enter = input('\nenter to quit...')
