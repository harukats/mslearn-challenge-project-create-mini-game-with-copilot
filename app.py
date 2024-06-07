# じゃんけんをするコンソールゲームを作成してください。
# じゃんけんの手は、グー、チョキ、パーのいずれかを選択できるようにしてください。
# ユーザーがじゃんけんの手を選択したら、コンピューターの手をランダムに選択し、勝敗を判定してください。
# 勝敗の判定は、以下の通りです。
# - グー vs チョキ -> 勝ち
# - チョキ vs パー -> 勝ち
# - パー vs グー -> 勝ち
# - 同じ手同士 -> あいこ
# 勝敗の結果を表示してください。
# 勝敗の結果の累計を記録するようにしてください。
# また、ユーザーに再度じゃんけんを続けるか尋ね、続ける場合はじゃんけんを再度実行できるようにしてください。
# じゃんけんを続けない場合は、勝敗の結果の累計を表示してゲームを終了してください。
# なお、じゃんけんの手の選択肢は、以下の通りです。
# - Rock
# - Scissors
# - Paper
# また、じゃんけんの手の選択肢を選択する際には、以下のように表示してください。
# - 1: Rock
# - 2: Scissors
# - 3: Paper
# じゃんけんの手の選択肢の番号を入力して、じゃんけんの手を選択できるようにしてください。
# じゃんけんの手の選択肢以外の番号が入力された場合は、再度じゃんけんの手の選択肢の番号を入力できるようにしてください。

import random

score = {
    'win': 0,
    'lose': 0,
    'draw': 0
}

def janken():
    hands = ['Rock', 'Scissors', 'Paper']
    print('1: Rock')
    print('2: Scissors')
    print('3: Paper')

    try:
        user_hand = int(input('Choose your hand: ')) - 1
        if user_hand < 0 or user_hand > 2:
            raise ValueError
    except ValueError:
        print('Please input a number between 1 and 3.')
        janken()
    
    computer_hand = random.randint(0, 2)
    
    print('Your hand:', hands[user_hand])
    print('Computer hand:', hands[computer_hand])
    
    if user_hand == computer_hand:
        score['draw'] += 1
        print('Draw!')
    elif (user_hand == 0 and computer_hand == 1) or (user_hand == 1 and computer_hand == 2) or (user_hand == 2 and computer_hand == 0):
        score['win'] += 1
        print('You win!')
    else:
        score['lose'] += 1
        print('You lose!')

    print('Win:', score['win'], 'Lose:', score['lose'], 'Draw:', score['draw'])

    if input('Do you want to continue? [y/n] ') == 'y':
        janken()
    else:
        print('Bye!')

if __name__ == '__main__':
    janken()
