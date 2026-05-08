"""Memory, puzzle game of word pairs."""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')

tiles = [
    'sol', 'luna', 'mar', 'flor',
    'gato', 'pez', 'ave', 'oso',
    'rojo', 'azul', 'casa', 'auto',
    'pan', 'té', 'rey', 'nube',
    'libro', 'hoja', 'fuego', 'agua',
    'oro', 'copa', 'tren', 'mesa',
    'silla', 'mano', 'ojo', 'pie',
    'río', 'luz', 'sal', 'uva'
] * 2

colors = {
    'sol': 'orange',
    'luna': 'gray',
    'mar': 'blue',
    'flor': 'pink',
    'gato': 'purple',
    'pez': 'deepskyblue',
    'ave': 'gold',
    'oso': 'brown',
    'rojo': 'red',
    'azul': 'blue',
    'casa': 'darkred',
    'auto': 'black',
    'pan': 'sandybrown',
    'té': 'green',
    'rey': 'gold',
    'nube': 'gray',
    'libro': 'navy',
    'hoja': 'green',
    'fuego': 'red',
    'agua': 'cyan',
    'oro': 'gold',
    'copa': 'purple',
    'tren': 'darkgreen',
    'mesa': 'sienna',
    'silla': 'chocolate',
    'mano': 'tan',
    'ojo': 'darkblue',
    'pie': 'peru',
    'río': 'dodgerblue',
    'luz': 'orange',
    'sal': 'black',
    'uva': 'violet'
}

state = {'mark': None}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        palabra = tiles[mark]

        up()
        goto(x + 25, y + 15)
        color(colors[palabra])
        write(palabra, align='center', font=('Arial', 12, 'bold'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
