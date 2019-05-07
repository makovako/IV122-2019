filenames = ["random1.txt","random2.txt","random3.txt","random4.txt","random5.txt","random6.txt","random7.txt"]

def import_data():
    out = []
    for file_name in filenames:
        l = []
        with open(file_name,"r") as file:
            l = file.readline().split()
        out.append(l)
    return out

def counts(l):
    out = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}
    for n in l:
        out[n] += 1
    return out

def print_counts(data):
    print('Frequency of numbers:')
    print('\t\t1\t2\t3\t4\t5\t6')
    for i in range(len(filenames)):
        count = counts(data[i]).values()
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(filenames[i],*count))

def difference_from_average(data):
    print('Difference from average:')
    print('\t\taverage\t1\t2\t3\t4\t5\t6')
    for i in range(len(filenames)):
        average = len(data[i]) // 6
        count = list(map(lambda x: x-average,counts(data[i]).values()))
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(filenames[i],average,*count))

def patterns(data):
    out = [[0 for x in range(6)] for y in range(6)] 
    for i in range(len(data) - 1):
        out[int(data[i])-1][int(data[i+1])-1] += 1 # -1 because indexes start from 0, number on cube from 1
    return out

def find_patternds(data):
    print('Find patterns of 2 subsequent numbers')
    for i in range(len(filenames)):
        pattern_matrix = patterns(data[i])
        print('File: {}'.format(filenames[i]))
        print('\t1\t2\t3\t4\t5\t6')
        for j in range(len(pattern_matrix)):
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(j+1,*pattern_matrix[j]))

data = import_data()
print_counts(data)
difference_from_average(data)
find_patternds(data)

#TODO NOTES
# jednotka prilis pravidlena
# dvojka prilis divoke cisla
# postupnosti
# stvorka divna
# patka niektore dvojice vyssia pravdepodobnost, viem predikovat
# sestka menej divoka
# trojka a sedmicka sa tvaria rovnomerne