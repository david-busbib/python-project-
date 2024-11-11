from hangman_helper import *
def update_word_pattern(word,pattern,letter):
    n_pattern =''
    for b in range(len(word)):
        if word[b] == letter :
            n_pattern += letter
        elif pattern[b] != '_' :
            n_pattern += pattern[b]
        else:
            n_pattern += '_'
    return n_pattern
def run_single_game(word_list,score):
    wrong_guess_lst = []
    word_gues = get_random_word(word_list)
    pattern = '_' * len(word_gues)
    msg = 'good lack'
    while not score == 0 or pattern == word_gues:
        display_state(pattern,wrong_guess_lst,score,msg)
        parameter, guess = get_input()
        if parameter == LETTER:
            if (len(guess) > 1) or not guess.isalpha()  or (guess != guess.lower()):
                msg = 'wrong input think again plaese'
                continue
            if guess in pattern :
                    msg ='alraerdy use that gues please think again and choose your next guess carfully'
                    continue
            else:
                score -=1
                if guess in word_gues:
                    pattern = update_word_pattern(word_gues, pattern, guess)
                    n = word_gues.count(guess)
                    score += (n*( n + 1 ))//2
                    continue
                elif word_gues.count(guess) == 0:
                    if guess in wrong_guess_lst :
                        score +=1
                        continue
                    wrong_guess_lst.append(guess)
                    continue
        if parameter == WORD:
            score -=1
            count = 0
            for a in guess:
                if a not in pattern:
                    count += 1
            if guess.__eq__(word_gues):
                pattern =word_gues
                msg = 'won and the word was {}'.format(word_gues)
                score += (count * (count + 1)) // 2
        elif parameter == HINT:
            msg ='good hint'
            score -=1
            neW_lst = filter_words_list(word_list,pattern,wrong_guess_lst)
            if len(neW_lst) > HINT_LENGTH :
                new_hint_lst = []
                for i in range(HINT_LENGTH) :
                    new_hint_lst.append(neW_lst[i*len(neW_lst)//HINT_LENGTH])
                neW_lst = new_hint_lst
            show_suggestions(neW_lst)
        if score <=0:
            msg='you just loose and the word was{}'.format(word_gues)
        display_state(pattern,wrong_guess_lst,score,msg)
        return score
    if  score == 0 or not pattern == word_gues:
        msg = 'you are a noob and the word was{}'.format(word_gues)
    display_state(pattern,wrong_guess_lst,score,msg)
    return score



def filter_words_list(words,pattern,wrong_guess_lst):
    n_lst =[]
    for wrd in words :
        if len(wrd) != len(pattern):
            continue
        for j in range(len(wrd)):
            f = True
            if (pattern[j] !='_' and wrd[j] != pattern[j]) or wrd[j]  in wrong_guess_lst:
                f =False
                break
            if wrd[j] in pattern and pattern[j] == '_':
                f =False
                break
        if f:
                n_lst.append(wrd)
    return n_lst
def main():
    words_list = load_words('words.txt')
    game_play =1
    points =run_single_game(words_list,POINTS_INITIAL)
    index =True
    while index:

        if points >0:
            msg = 'you already play {} game and your score is {} '.format(game_play,points)
            index= play_again(msg)
            if index:
                points = run_single_game(words_list,points)
        else:
            msg='you already play {} game and your score is {},and do you want to start new p '.format(game_play, points)
            index = play_again(msg)
            if index:
                game_play = 0
                points = run_single_game(words_list,POINTS_INITIAL)
        game_play+=1
if __name__ == '__main__':
    main()

