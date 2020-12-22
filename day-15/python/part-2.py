import re
import sys

RE = re.compile(r'-?\d+')

ingredients = []
for line in open(sys.argv[1]).readlines():
    ingredients.append([int(v) for v in RE.findall(line)])

def score(amounts):
    negative = False
    product = 1
    for i in range(len(ingredients[0])-1):
        iscore = sum([amounts[j]*ingredients[j][i] for j in range(len(ingredients))])
        product *= abs(iscore)
        if iscore < 0:
            negative = True
    return -product if negative else product

def calories(amounts):
    return sum([amounts[i]*ingredients[i][-1] for i in range(len(ingredients))])

maxscore = 0

iter = 0
for a in range(101):
    for b in range(101):
        for c in range(101):
            for d in range(101):
                iter += 1
                #if iter % 1000000 == 0:
                #    print(iter, maxscore)
                if a+b+c+d != 100 or calories([a,b,c,d]) != 500:
                    continue
                maxscore = max(score([a,b,c,d]), maxscore)

print(maxscore)

