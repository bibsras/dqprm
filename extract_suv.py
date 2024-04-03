# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
"""
fichier = open("20200527152905.861802.ig.tum", "r")

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
"""
import re 
fic = "20200527152905.861802.ig.tum"
def do_it():
    with open(fic,"r") as f:
        lines = f.read()
    m=re.findall("(M.*)(?<!RC)SUVValue = (\d+\.\d+)",lines, re.M)
    d={el[0]: float (el[1]) for el in m}
    print(m)

if __name__=="__main__":
    do_it()