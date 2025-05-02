from itertools import permutations

def solve_send_more_money():
    letters = 'SENDMORY'
    for perm in permutations(range(10), len(letters)):
        s, e, n, d, m, o, r, y = perm
        if s == 0 or m == 0:
            continue  # leading digits can't be 0
        send = s*1000 + e*100 + n*10 + d
        more = m*1000 + o*100 + r*10 + e
        money = m*10000 + o*1000 + n*100 + e*10 + y
        if send + more == money:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            return
    print("No solution found")

solve_send_more_money()


from itertools import permutations


def solve_send_more_money():
    letters = 'SENDMORY'

    for perm in permutations(range(10), len(letters)):

        s,e,n,d,m,o,r,y = perm
        if s == 0 or m == 0:
            continue
        send = s*1000 + e*100 + n*10 + d
        more = m*1000 + o*100 + r*10 + e
        money = m*10000 + o*1000 + n*100 + e*10 +y

        if send + more == money:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            return 
        
        print("No solution found")

    solve_send_more_money()
    
