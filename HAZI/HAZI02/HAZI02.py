import numpy as np
from datetime import datetime, timedelta


# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait. Bemenetként egy array-t vár.
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()

def column_swap(array):
    array[:, [1, 0]] = array[:, [0, 1]]
    return array

#print(column_swap(np.array([[1,2],[3,4]])))

# Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön

def compare_two_array(array1, array2):
    return array1 == array2

# Készíts egy olyan függvényt, ami vissza adja string-ként a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!

def get_array_shape(array):
    shape = np.shape(array)
    print("Sor: " + str(shape[0]) + ", oszlop: " + str(shape[1]) + ", melyseg: " + str(len(shape)-1))

#get_array_shape([[[1,2,3], [4,5,6], [4,5,6]],[[1,2,3], [4,5,6], [4,5,6]]])

# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges pred-et egy numpy array-ből. 
# Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek.
# Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli. 
# Pl. ha 1 van a bemeneten és 4 classod van, akkor az adott sorban az array-ban a [1] helyen álljon egy 1-es, a többi helyen pedig 0.
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()

def encode_Y(array, numofclasses):
    return np.eye(numofclasses)[array].astype(int)

# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()

def decode_Y(array):
    return np.argmax(array, 1)

# Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét!
# Bemenetként egy listát és egy array-t és adja vissza azt az elemet, aminek a legnagyobb a valószínüsége(értéke) a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. # Az ['alma', 'körte', 'szilva'] egy lista!
# Ki: 'szilva'
# eval_classification()

def eval_classification(list, array):
    return list[np.argmax(array)]

# Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# repalce_odd_numbers()

def replace_odd_numbers(array):
    array[np.where(array % 2 == 1)] = -1
    return array

# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, attól függően, hogy az adott elem nagyobb vagy kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()

def replace_by_value(array, value):
    v1 = np.where(array >= value)
    v2 = np.where(array < value)

    array[v1] = 1
    array[v2] = -1

    return array

# Készíts egy olyan függvényt, ami egy array értékeit összeszorozza és az eredményt visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza

def array_multi(array):
    return np.prod(array)

# Készíts egy olyan függvényt, ami egy 2D array értékeit összeszorozza és egy olyan array-el tér vissza, aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()

def array_multi_2d(array):
    return np.prod(array, 1)

# Készíts egy olyan függvényt, amit egy meglévő numpy array-hez készít egy bordert nullásokkal. Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()

def add_border(array):
    x, y = array.shape
    bordered = np.zeros((x+2, y+2))
    bordered[1:-1, 1:-1] = array
    return bordered

# A KÖTVETKEZŐ FELADATOKHOZ NÉZZÉTEK MEG A NUMPY DATA TYPE-JÁT!

# Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot és ezt adja vissza egy numpy array-ben. A fgv ként str vár paraméterként 'YYYY-MM' formában.
# Be: '2023-03', '2023-04'  # mind a kettő paraméter str.
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()

def list_days(date1, date2):
    start = datetime.strptime(date1, '%Y-%m')
    end = datetime.strptime(date2, '%Y-%m')
    days = np.arange(start, end + timedelta(days=1), timedelta(days=1)).astype(datetime)
    return np.char.array(days.strftime('%Y-%m-%d'))

# Írj egy fügvényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD. Térjen vissza egy 'numpy.datetime64' típussal.
# Be:
# Ki: 2017-03-24

def get_current_date():
    today = np.datetime64('today')
    return np.datetime_as_string(today, 'D')

# Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:02:00 óta. Int-el térjen vissza
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()

def sec_from_1970():
    start_time = np.datetime64('1970-01-01T00:02:00')
    current_time = np.datetime64('now')
    return int((current_time - start_time) / np.timedelta64(1, 's'))