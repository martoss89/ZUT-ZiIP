import pyautogui, time
from math import pi, sin, cos, radians

time.sleep (5)

R = 75 #promień dużego koła
r = 50 #promień małego koła
N = 40 #liczba małych kół
M = 50 #liczba boków figury


def koło(x0, y0, R): #współrzedne koła i jego promien
    pyautogui.moveTo(x=x0 + R, y=y0)
    for k in range(M + 1): #rysowanie centralnego koła z domknieciem
        x = x0 + R * cos(k * 2 * pi / M) #zamiana kątów na radiany
        y = y0 + R * sin(k * 2 * pi / M)
        pyautogui.dragTo(x=x, y=y) #przesuniecie myszy


x0, y0 = pyautogui.position() #położenie myszki

koło(x0, y0, R) #położenie koła

for k in range(N): #rozmieszczenie małych kół
    xc = x0 + R * cos(k * 2 * pi / N) #zamiana kątów na radiany
    yc = y0 + R * sin(k * 2 * pi / N)
    koło(xc, yc, r)

#import modułów pyautogui, math
#czas przełaczenia na program paint
#okrelenie promieni dużego i małyh kół
#okreslenie liczby małych kół
#okreslenie ilosci bokow figury, tak by powstało koło
#ustalenie polozenia myszy do narysowania centralnego kola
#okreslenie promienia koła
#okreslenie domkniecia koła
#zamiana kątów na radiany
#narysowanie centralnego koła poprzez przesuniecie myszy do okreslonych wspołrzednych
#ustalenie rozmieszczenia małych kół względem centralnego koła
#zamiana kątów na radiany
#narysowanie małych kół 
