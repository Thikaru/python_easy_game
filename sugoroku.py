import random

# 自分の場所
my_posi = 1
# 相手の場所
comp_posi = 1

total_mass = 30
point = "・"


# 双六の盤面を作成する
def MakeBoard(posi, player_obj):
    if total_mass-posi > 0:
        print((posi-1)*point + player_obj + (total_mass-posi)*point + "Goal\n")
    else:
        print((total_mass-1)*point + player_obj + "\n")


# どのサイコロを振るのかを決める処理
def NextJudge(option):
    if option == 1:
        print("あなたは1〜6のサイコロを振りました！")
        random_num = random.randint(1, 6)
        print(str(random_num) + "進みました")
        return random_num
    elif option == 2:
        print("あなたは1か6のサイコロを振りました！")
        random_num = random.choice([1, 6])
        print(str(random_num) + "進みました")
        return random_num
    elif option == 3:
        print("あなたは2〜5のサイコロを振りました！")
        random_num = random.randint(2, 5)
        print(str(random_num) + "進みました")
        return random_num
    elif option == 4:
        print("あなたは3進むことを決めました！")
        print("3進みました")
        return 3
    else:
        print("1〜4の数字を入力してください！！\n")
        return -1


# Goalしているかを判定する処理
def JudgeWin(posi):
    if posi >= 30:
        return True
    else:
        return False


# 先手後手の判定を行う
is_first = False
if random.randint(1, 2) == 1:
    is_first = True
else:
    is_first = False


# Mainの双六の処理
while True:
    if is_first == False:
        # 相手の動き
        print("相手の番です!!")
        print("===================================")
        comp_option = random.randint(1, 4)
        comp_posi += NextJudge(comp_option)
        MakeBoard(my_posi, "P")
        MakeBoard(comp_posi, "C")
        print("===================================")
        if JudgeWin(comp_posi):
            print("相手の勝利です！\n")
            break

    # 自分の動き
    print("自分の番です")
    print("===================================")
    print("双六ゲームを開始します！\nサイコロをまず選んで降ります．\n1：1〜6がランダムで出る\n2：1か６がランダムで出る\n3：2〜5がランダムで出るサイコロ\n4：3だけ進む\n")
    option = input("上記の数字を入力してください=")
    while True:
        move = NextJudge(int(option))
        if move > 0:
            my_posi += move
            break
        else:
            option = input("上記の数字を入力してください=")
    MakeBoard(my_posi, "P")
    MakeBoard(comp_posi, "C")
    print("===================================")
    if JudgeWin(my_posi):
        print("あなたの勝利です！\n")
        break

    if is_first == True:
        # 相手の動き
        print("相手の番です!!\n")
        print("===================================")
        comp_option = random.randint(1, 4)
        comp_posi += NextJudge(comp_option)
        MakeBoard(my_posi, "P")
        MakeBoard(comp_posi, "C")
        print("===================================")
        if JudgeWin(comp_posi):
            print("相手の勝利です！\n")
            break
