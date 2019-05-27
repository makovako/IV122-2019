# Monty hall

![montyhall](A-Monty-Hall/Screenshot_20190505_101427.png)

# Nenahodna cisla

Pocetnost:

![pocetnost](B-Nenahodna-cisla/frequency-of-numbers.png)

Pre lepsi prehlad, rozdiel od priemeru:

![rozdiel](B-Nenahodna-cisla/difference-from-average.png)

Odtial vidime:

- random 2 - ma velke vykyvy v pocetnosti cisel, malo dvojek a vela patiek
- random 1 - ma zase az presne pocty cisel, vsetky cisla su +- 1 rovnako zastupene

Preto si myslim, ze tieto 2 sekvencie su nenahodne.

Dalej porovnam dvojice dvoch po sebe iducich cisel a ich pocty.

![random4](B-Nenahodna-cisla/random4-tuples.png)

- pre random 4, je vidiet ze niektore dvojice vobec neexistuju, je preto menej moznosti/vyssia pravdepodobnost uhadnut, ake cislo bude nasledovat.
- preto si myslim, ze tato sekvencia je tiez nenahodna

![random5](B-Nenahodna-cisla/random5-tuples.png)

- pre random 5 su niektore dvojice tiez castejsie, opat vyssia pravdepodobnost na uhadnutie dalsieho cisla.
- nenahodne

![random6](B-Nenahodna-cisla/random6-tuples.png)

- v random 6 je vacsina dvojic zastupena v priblizne rovnakom pocte, no v kazdom stlpci/riadku sa nachadza dvojica/dvojice s vyrazne nizsou a vyssou pocetnostou
- tiez to zavana nenahodnostou
  
![random3](B-Nenahodna-cisla/random3-tuples.png)
![random7](B-Nenahodna-cisla/random7-tuples.png)

- pre random 3 a random 7 su uz dvojice v priblizne rovnakom pocte, ziadne vacsie vykyvy
- preto by som povedal, ze tieto dve postupnosti by mohli byt nahodnymi

# Centralni limitni veta

- pri metode 1 a 2 to vyzera na priblizne normalnu distribuciu
- pri metode 3 uz nie, velmi caste su 2 hodnoty, priemery kociek

## n = 10

![n10](C-Centralni-limitni-veta/n-10_k-10.png)

![n10](C-Centralni-limitni-veta/n-10_k-100.png)

![n10](C-Centralni-limitni-veta/n-10_k-1000.png)

## n = 1000

![n1000](C-Centralni-limitni-veta/n-1000_k-10.png)

![n1000](C-Centralni-limitni-veta/n-1000_k-100.png)

![n1000](C-Centralni-limitni-veta/n-1000_k-1000.png)

## n = 100000

![n100000](C-Centralni-limitni-veta/n-100000_k-10.png)

![n100000](C-Centralni-limitni-veta/n-100000_k-100.png)

![n100000](C-Centralni-limitni-veta/n-100000_k-1000.png)

# Bayesova veta

- vypocet je prilozeny v [pdf](9-pravdepodobnost/D-Bayesova-veta/IV122__vypocet_bayesova_veta.pdf)

## n = 10, x = 5

Moj odhad: 0.10

Vypocet: 0.001156

Simulacia: 0.0013

## n = 100, x = 3

Moj odhad: 0.20

Vypocet: 0.3143

Simulacia: 0.31344

## n = 1000, x = 5

Moj odhad: 0.10

Vypocet: 0.1138

Simulacia: 0.1108