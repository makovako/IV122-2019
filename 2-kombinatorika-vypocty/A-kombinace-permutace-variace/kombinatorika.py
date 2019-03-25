def variation(inlist,k,repeat = False):
    if len(inlist)==1 or k==0:
        return [inlist]
        
    outlist = []
    for p in inlist:
        origlist = inlist[:]
        if not repeat:
            origlist.remove(p)        
        for l in variation(origlist,k-1,repeat):                      
            outlist.append([p]+l[:k-1])
    return outlist

def permutation(inlist):
    return variation(inlist,len(inlist))

def combination(inlist,k,repeat = False):    
    if k==0:
        return [[]]
    if len(inlist)<k and not repeat:
        return []       
    outlist = []
    origlist = inlist[:]
    for p in inlist:
        if not repeat:
            origlist.remove(p)       
        for l in combination(origlist,k-1,repeat):
            if len([p]+l[:k-1]) == k:
                outlist.append([p]+l[:k-1])
            if len(l[:k-1]) == k:
                outlist.append(l[:k-1])
        if repeat:
            origlist.remove(p)
    return outlist

print("Testing some values")

pnr = permutation(['a','b','c'])
print("Permutations of [a,b,c], count {}:".format(len(pnr)))
for i in pnr:
    print(i)

for i in range(1,4):
    vnr = variation(['a','b','c','d'],i)
    print("Variations (not repeat) of [a,b,c,d], k = {}, count = {}:".format(i,len(vnr)))
    for v in vnr:
        print(v)
    
for i in range(1,4):
    vwr = variation(['a','b','c'],i,True)
    print("Variations (with repeat) of [a,b,c], k = {}, count = {}:".format(i,len(vwr)))
    for v in vwr:
        print(v)

for i in range(1,4):
    cnr = combination(['a','b','c','d'],i)
    print("Combination (not repeat) of [a,b,c,d], k = {}, count = {}:".format(i,len(cnr)))
    for c in cnr:
        print(c)

for i in range(1,4):
    cwr = combination(['a','b','c','d'],i,True)
    print("Combination (with repeat) of [a,b,c,d], k = {}, count = {}:".format(i,len(cwr)))
    for c in cwr:
        print(c)
