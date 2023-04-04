import sys
import inflect
p = inflect.engine()
def main():
    l=[]
    while True:
        try:
            name = input("Name: ")
            l.append(name)
        except:
            EOFError
            d = p.join((l))
            print()
            print("Adieu, adieu, to", d)
            sys.exit(1)
main()