try:
    xrange
except:
    xrange = range
 
def totalvalue(comb):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for item, wt, val in comb:
        totwt  += wt
        totval += val
    return (totval, -totwt) if totwt <= 400 else (0, 0)
 
items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )
items = ((" 0 ", 382745 , 825594 ) ,
(" 1 ", 799601 , 1677009 ) ,
(" 2 ", 909247 , 1676628 ) ,
(" 3 ", 729069 , 1523970 ) ,
(" 4 ", 467902 , 943972 ) ,
(" 5 ", 44328 , 97426 ) ,
(" 6 ", 34610 , 69666 ) ,
(" 7 ", 698150 , 1296457 ) ,
(" 8 ", 823460 , 1679693 ) ,
(" 9 ", 903959 , 1902996 ) ,
(" 10 ", 853665 , 1844992 ) ,
(" 11 ", 551830 , 1049289 ) ,
(" 12 ", 610856 , 1252836 ) ,
(" 13 ", 670702 , 1319836 ) ,
(" 14 ", 488960 , 953277 ) ,
(" 15 ", 951111 , 2067538 ) ,
(" 16 ", 323046 , 675367 ) ,
(" 17 ", 446298 , 853655 ) ,
(" 18 ", 931161 , 1826027 ) ,
(" 19 ", 31385 , 65731 ) ,
(" 20 ", 496951 , 901489 ) ,
(" 21 ", 264724 , 577243 ) ,
(" 22 ", 224916 , 466257 ) ,
(" 23 ", 169684 , 369261 ) ,)
def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]
 
    for j in xrange(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)
 
    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]
 
        if was_added:
            item, wt, val = items[j-1]
            result.append(items[j-1])
            w -= wt
 
    return result
 
import pdb; pdb.set_trace()
bagged = knapsack01_dp(items, 6404180)
print("Bagged the following items\n  " +
      '\n  '.join(sorted(item for item,_,_ in bagged)))
val, wt = totalvalue(bagged)
print("for a total value of %i and a total weight of %i" % (val, -wt))