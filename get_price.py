import pprint
import ystockquote

__author__ = 'albertogonzalezpaje'

def main():
    pprint.pprint(ystockquote.get_price('POP.MC'))

if __name__=="__main__":
    main()
