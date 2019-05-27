# Zakladni utvary

![triangle](A-zakladni-utvari/triangle.png)

![Spiral](A-zakladni-utvari/spiral.png)

![Spiral-color](A-zakladni-utvari/spiral_color.png)

![Circle](A-zakladni-utvari/circle.png)

![Circle-depth](A-zakladni-utvari/circle_depth.png)

![Circle-par](A-zakladni-utvari/circle_par.png)

# Vypln mnohouholnika

![polygon1](B-mnohouhelnik/polygon1.png)

![polygon2](B-mnohouhelnik/polygon2.png)

![square](B-mnohouhelnik/square.png)

## Explanation

Vela pokusov kym sa mi to podarilo sfinalizovat, oznaceny kod sa nepouziva, no nemazal som ho.

Posledna funkcia je funkcna.

Ked je priamka vodorovna, tak len kontrolujem, ci sa bod nachadza na priamke, ak ano vyfarbim na cierno, ak nie pokracujem s dalsimi praimkami bez dalsieho spracovania tejto usecky.

Dalej je tam magicky riadok s poznamkou explanation in readme. Snazim sa pomcoou parametrickeho vyjadrenia dvoch useciek najst ich prienik.

x,y - suradnice bodu

Ax,Ay - suradnice bodu A, a[0],a[1]
Vx,Vy - smerovy vektor usecky, vector[0], vector[1]

Parametricke vyjadrenie usecky y = 0
X = x - 1*s
Y = y + 0*s

Parametricke vyjadrenie usecky line
X = Ax + Vx*t
Y = Ay + Vy*t

dosadim

x - s = Ax + Vy*t
y = Ay + Vy*t

z druhej vyjadrim t a dostanem

x - s = Ax + Vx * (y - Ay)/Vy

na tom magickom riadku si vypocitam s a porovnam s x, ci priesecnik lezi na usecke.

# Efekty

Chessboard borders

![Normal-chessboard](C-efekty/normal_chessboard.png)

![Chessboard-border](C-efekty/chessboard_border.png)

![Chessboard-custom-border](C-efekty/chessboard_custom_border.png)

Chessboard sin

![CHessboard-sin](C-efekty/chessboard_sin.png)
![CHessboard-sin](C-efekty/chessboard_sin_2.png)
![CHessboard-sin](C-efekty/chessboard_sin_3.png)
![CHessboard-sin](C-efekty/chessboard_sin_4.png)
![CHessboard-sin](C-efekty/chessboard_sin_5.png)
![CHessboard-sin](C-efekty/chessboard_sin_6.png)
![CHessboard-sin](C-efekty/chessboard_sin_7.png)

Sincut

![sincut](C-efekty/sin_cut.png)
![sincut](C-efekty/sin_cut_2.png)
![sincut](C-efekty/sin_cut_3.png)

Sin wave

![sinwave](C-efekty/sin_wave.png)
![sinwave](C-efekty/sin_wave_2.png)
![sinwave](C-efekty/sin_wave_3.png)
![sinwave](C-efekty/sin_wave_4.png)
![sinwave](C-efekty/sin_wave_5.png)

Colors

![colors](C-efekty/colors.png)
![colors](C-efekty/colors2.png)
![colors](C-efekty/colors3.png)
![colors](C-efekty/colors4.png)