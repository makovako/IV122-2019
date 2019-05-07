from transformation import transformation, rotation, scaling, translation, shear

lines = [[[50,50],[-50,50]],[[-50,50],[-50,-50]],[[-50,-50],[50,-50]],[[50,-50],[50,50]]]

transformation('square.svg',lines,0)

transformation('rotation45.svg',lines,1,rotation(45))

transformation('rotation17x10.svg',lines,17,rotation(10))

# uloha 2

transformation('ukazka-2.svg',lines,15,rotation(10),scaling(1.1,0.8))

# uloha 3

transformation('ukazka-3.svg',lines,25,shear(1.3),rotation(10),scaling(0.9,0.9),translation(50,50))

# uloha 1
lines = [[[-25,0],[25,0]],[[25,0],[25,50]],[[25,50],[-25,50]],[[-25,50],[-25,0]]]

transformation('ukazka-1.svg',lines,10,rotation(20),scaling(1.1,1.1),translation(5,10))

transformation('ukazka-1-uprava.svg',lines,10,rotation(20),scaling(1.1,1.1),translation(5,0))
