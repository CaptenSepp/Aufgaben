# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:47:20 2020

"""

from math import sin


def sinusliste(xmin, xmax, step):
    '''
    Erzeugt eine Liste mit sin(x).
    Die entsprechenden x-Wert werden zwischen xmin, xmax mit Schrittweite
    step erzeugt.

    Parameters
    ----------
    xmin : float
        minimaler x-Wert.
    xmax : float
        maximaler x-Wert.
    step : float
        Schrittweite.

    Returns
    -------
    Liste mit x-Werten und den entsprechenden y-Werten, die sich aus sin(x) berechnen

    '''

    result = []
    i = xmin
    while i <= xmax:
        y_wert = [i, sin(i)]
        result.append(y_wert)
        i += step
    return result
