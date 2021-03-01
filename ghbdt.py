import random as rnd
HP=100
while HP>0:
    print('Приветствую в своём казино')
    Ch=rnd.randint(0,36)
    type_st=input('Выберите тип ставки: 1-single, 2-Чет/Нечет, 3- Красное/Черное')
    if type_st=='1':
        st=int(input('Введите число от 0 до 36-'))
        f=int(input('Введите кол-во фишек-'))
        if st==Ch:
            print('Congrattulations! You are win!')
            winning=f*35
        else:
            print('Congratulations! You LOSER  ;( !')
            winning=-f
            HP=HP+winning
        print('Ваш выигрыш = ',winning)
        print('Ваш HP=',HP)
        
        print('Вы должны казино')
    elif type_st=='2':
        Ch=rnd.randint(0,36)
        st=input('Введите ставку в формате "чет" или "нечет"+')
        f=int(input('Введите кол-во фишек-'))
        if Ch%2==0:
            Ch="чет"
        else:
            Ch=="нечет"
        if Ch==st:
            print('You are win')
            winning=f
        else:
            winning=-f
        HP=HP+winning
    elif type_st=='3':
        Ch=rnd.randint(0,36)
        st=input('Введите ставку в формате "Red" или "Black"+')
        f=int(input('Введите кол-во фишек-'))
        print('На рулетке выпало ',Ch)
        if Ch==1 or Ch==14 or Ch==9 or Ch==18 or Ch==7 or Ch==12 or Ch==3 or Ch==32 or Ch==19 or Ch==21 or Ch==25 or Ch==34 or Ch==27 or Ch==36 or Ch==30 or Ch==23 or Ch==5 or Ch==16:
            Ch="Red"
        else:
            Ch=="Black"
        if Ch==st:
            print('You are win')
            winning=f
        else:
            winning=-f
        HP=HP+winning
        print('Ваш выигрыш = ',winning)
        print('Ваш HP=',HP)
    if HP<0:
        print('У вас закончились фишки, вы проиграли')





















