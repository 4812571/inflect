#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    import inflect

def testOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    num = fdp.ConsumeIntInRange(0, 2)
    str = fdp.ConsumeUnicodeNoSurrogates(256)
    p = inflect.engine()

    if num == 0:
        p.plural_adj(str)
    if num == 1:
        p.plural_noun(str)
    if num == 2:
        p.plural_verb(str)
        
def main():
    atheris.Setup(sys.argv, testOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()