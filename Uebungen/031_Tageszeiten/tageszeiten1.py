#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:49:00 2020

@author: student
"""


def tageszeit(uhrzeit):
    """
    Gibt die Tageszeit entsprechend der Uhrzeit als String zurück.

    Uhrzeit        Rückgabe
    00:00 - 04:59  Nacht
    05:00 - 10:59  Morgen
    11:00 - 12:59  Mittag
    13:00 - 16:59  Nachmittag
    17:00 - 22:29  Abend
    22:30 - 23:59  Nacht

    Wenn die Uhrzeit nicht dem Format HH:MM entspricht, wird eine ValueError-Exception erzeugt
    --- Beispiel dafür "raise ValueError("Falsches Format")

    Parameters
    ----------
    uhrzeit : str
        Die Uhrzeit als String in der Form HH:MM

    Returns
    -------
    String mit der Tageszeit (siehe oben)

    """
    uhrzeit = uhrzeit.replace(":", "")
    if len(uhrzeit)!=4:
        raise ValueError
    uhrzeit=int(uhrzeit)
    # if len(uhrzeit)!=4:
    #     raise ValueError
    if not 0<=uhrzeit<=2359:
        raise ValueError
    if 0 <= uhrzeit < 500 or 2230 <= uhrzeit <= 2359:
        return ("Nacht")
    elif 500 <= uhrzeit <= 1059:
        return ("Morgen")
    elif 1100 <= uhrzeit <= 1259:
        return ("Mittag")
    elif 1300 <= uhrzeit <= 1659:
        return ("Nachmittag")
    elif 1700 <= uhrzeit <= 2259:
        return ("Abend")


if __name__ == '__main__':
    print(tageszeit("03:06"))
    print(tageszeit("13:32"))
    print(tageszeit("22:06"))
