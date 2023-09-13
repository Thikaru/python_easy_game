import datetime
import random

alphabet_lists = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
num_lists = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
alphabet_num_lists = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                      "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                      "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
selected_lists = ""
answer = ""

game_explains = [
    "=============================================================",
    "文字消えゲームを開始します．下記のルールのどれで行うかを選択してください．",
    "=============================================================",
    "1.アルファベットのみで一つ消えたものを探すゲームモード(簡単:10文字)",
    "2.アルファベットのみで一つ消えたものを探すゲームモード(普通:26文字)",
    "3.アルファベットのみで一つ消えたものを探すゲームモード(難しい:100文字)",
    "4.数字のみで一つ消えたものを探すゲームモード(簡単:10文字)",
    "5.数字とアルファベットから一つ消えたものを探すゲームモード(難しい:100文字)",
    "6.数字とアルファベットから一つ消えたものがあるまたはないことを探すゲームモード(鬼むず:100文字)",
    "-1.ゲームを終了する．",
    "=============================================================",
]


# ゲームの内容を表示する部分
def ShowSelectGameDetail():
    for i in range(len(game_explains)):
        print(game_explains[i])


# lucky_numがtotal_numからランダムに生み出されたかどうかをTrueとFalseを返す．
# ★引数
# ・lucky_num：あたりの数字
# ・total_num：lucky_numより大きい整数
# ★返り値
# True:指定した数字の時 False:指定した数字以外の時
def IsRandom(lucky_num, total_num):
    if 1 <= lucky_num and lucky_num < total_num:
        if random.randint(1, total_num) == lucky_num:
            return True
        else:
            return False
    else:
        print("Error")
        return "Error"


# 表示するランダム文字列を作成する
# ★引数の説明
# ・option:0のとき一文字だけ使用しない文字を決定する．1：一文字だけ使用しない文字列を決めるか全て使用するかランダムで決まる
# ・use_num：使用する文字の個数 0の場合は全て．配列以上の大きさを指定しても全ての文字を使用する．
# ・create_string_num：作成する文字列の長さ
# ・use_string_lists：使用してよい文字の配列
# ★戻り値
# ・ランダムに使わなかった文字1つまたは，全て使った場合は，空文字と使用した文字列(配列のインデックス0)，
#   結果的に使用した文字(配列のインデックス1)，
#   作成した文字列の配列を返す(配列のインデックス3)
def CreateRandomString(option, use_num, create_string_num, use_string_lists):
    # 使用する文字列群をcopy関数で複製する
    copy_use_string_lists = use_string_lists.copy()

    # 使用する文字数を決定する
    decided_use_num = 0
    result_used_string = []
    result_string = ""
    original_answer = ""
    if use_num == 0 or use_num >= len(copy_use_string_lists):
        print("全ての文字を使用してランダム文字列を作成します")
        decided_use_num = len(copy_use_string_lists)
        result_used_string = copy_use_string_lists
    else:
        print("一定の文字列を使用してランダム文字列を作成する")
        decided_use_num = use_num
        for i in range(decided_use_num):
            decided_word = random.choice(copy_use_string_lists)
            result_used_string.append(decided_word)
            copy_use_string_lists.remove(decided_word)

    # 答えとなる文字または，空白を決める処理
    original_used_list = result_used_string.copy()
    if option == 0:
        original_answer = random.choice(result_used_string)
        result_used_string.remove(original_answer)
    elif option == 1:
        if IsRandom(int((len(result_used_string)+1)/2), len(result_used_string)+1):
            original_answer = ""
        else:
            original_answer = random.choice(result_used_string)
            result_used_string.remove(original_answer)

    # ランダムな文字列を生成する処理
    copy_result_used_string = result_used_string.copy()
    i = len(result_used_string)
    while i < create_string_num:
        i += 1
        random_word = random.choice(copy_result_used_string)
        result_used_string.append(random_word)

    random.shuffle(result_used_string)
    for i in range(create_string_num):
        result_string += result_used_string.pop() + "  "
        if (i+1) % 10 == 0:
            result_string += "\n"

    return [original_answer, original_used_list, result_string]


# 問題の表示部分
def ShowQuestion(answer, used_lists, strings):
    print("---------------------------")
    print(answer)
    print("使用している文字は下記です．")
    print(used_lists)
    print("---------------------------")
    print("\n問題を始めますか？始める場合はエンターを押してください")
    input()
    start_time = datetime.datetime.now()
    print("\n以下から使用している文字列で使われていないものを見つけてください！！\n")
    print(strings)
    while True:
        your_answer = input("答えを入力してください．\nyour answer = ")
        end_time = datetime.datetime.now()
        if your_answer == answer:
            print("あなたの答えは正解です．！")
            print("答え ： " + answer)
            print("解答までにかかった時間は : " + str((end_time-start_time).seconds))
            break
        else:
            print("違います．焦らず探してください!")

    # MAIN処理
    # ゲーム選択画面
while True:
    ShowSelectGameDetail()
    option = input("入力 = ")
    if option == "-1":
        print("ゲームを終了します！\n")
        break
    elif option == "1":
        print(game_explains[3]+"\n")
        results = CreateRandomString(
            0, 10, 10, alphabet_lists)
        # 問題表示
        ShowQuestion(results[0], results[1], results[2])

    elif option == "2":
        print(game_explains[4]+"\n")
        results = CreateRandomString(
            0, 0, 26, alphabet_lists)
        # 問題表示
        ShowQuestion(results[0], results[1], results[2])
    elif option == "3":
        print(game_explains[5]+"\n")
        results = CreateRandomString(
            0, 0, 100, alphabet_lists)
        # 問題表示
        ShowQuestion(results[0], results[1], results[2])
    elif option == "4":
        print(game_explains[6]+"\n")
        results = CreateRandomString(
            0, 0, 10, num_lists)
        # 問題表示
        ShowQuestion(results[0], results[1], results[2])
    elif option == "5":
        print(game_explains[7]+"\n")
        results = CreateRandomString(
            0, 0, 100, alphabet_num_lists)
        # 問題表示
        ShowQuestion(results[0], results[1], results[2])
    elif option == "6":
        print(game_explains[8]+"\n")
        results = CreateRandomString(
            1, 0, 100, alphabet_num_lists)
        # 問題表示
        ShowQuestion(results[0], results[1], results[2])
    else:
        print("-1または1〜5の数字を入力してください!!\n")
