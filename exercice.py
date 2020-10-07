#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
# TODO: Importez vos modules ici
def ellipse(mass_volum, a = 8, b = 9, c = 22):
    volume = 4/3 * (math.pi) * a * b * c
    mass = volume/mass_volum
    
    return volume, mass
    

# TODO: Définissez vos fonction ici


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    volume, mass = ellipse(a = 10, b = 22, c = 33)
    print (volume, mass)

