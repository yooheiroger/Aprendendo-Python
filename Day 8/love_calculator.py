from itertools import count


def calculate_love_score(name1, name2):
    t = 't'
    r = 'r'
    u = 'u'
    e = 'e'
    count_t1 = name1.count(t)
    count_r1 = name1.count(r)
    count_u1 = name1.count(u)
    count_e1 = name1.count(e)
    total_name_true1 = count_t1 + count_r1 + count_u1 + count_e1
    print(total_name_true1)
    count_t2 = name2.count(t)
    count_r2 = name2.count(r)
    count_u2 = name2.count(u)
    count_e2 = name2.count(e)
    total_name_true2 = count_t2 + count_r2 + count_u2 + count_e2

    l = 'l'
    o = 'o'
    v = 'v'
    e = 'e'
    count_l1 = name1.count(l)
    count_o1 = name1.count(o)
    count_v1 = name1.count(v)
    count_ee1 = name1.count(e)
    total_name_love1 = count_l1 + count_o1 + count_v1 + count_ee1

    count_l2 = name2.count(l)
    count_o2 = name2.count(o)
    count_v2 = name2.count(v)
    count_ee2 = name2.count(e)
    total_name_love2 = count_l2 + count_o2 + count_v2 + count_ee2

    total_name_count1 = total_name_love1 + total_name_true1
    total_name_count2 = total_name_true2 + total_name_love2

    print(f'Your love score is = {total_name_count1}{total_name_count2}')

def calculate_love_score2(name1, name2):
    letter_true1 = set('true')# Conjunto com as letras da palavra "True"
    count_true1 = sum(1 for letter in name1 if letter in letter_true1)

    letter_true2 = set('true')# Conjunto com as letras da palavra "True"
    count_true2 = sum(1 for letter in name2 if letter in letter_true2)

    letter_love1 = set('love')
    count_love1 = sum(1 for letter in name1 if letter in letter_love1)

    letter_love2 = set('love')
    count_love2 = sum(1 for letter in name2 if letter in letter_love2)

    count1 = count_true1 + count_love1
    count2 = count_true2 + count_love2

    print(f'your love score is {count1}{count2}')
#   for letra in nome → Percorre cada letra da variável nome.
#   if letra in letras_true → Verifica se a letra atual está dentro da string ou lista letras_true.
#   1 for letra in nome if ... → Gera um 1 sempre que a condição for verdadeira.
#   sum(...) → Soma todos esses 1, ou seja, conta quantas vezes a condição foi atendida.

