# https://en.wikipedia.org/wiki/List_of_numeral_systems
BASE_16 = '0123456789ABCDEF'
BASE_58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
BASE_64 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
BASE_91 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"'

def baseToBase(n, base, symbols=''):
    if symbols and base > len(symbols):
        return 'Invalid base'
    if not symbols:
        if base <= 16: symbols = BASE_16
        elif base == 58: symbols = BASE_58
        elif base <= 64: symbols = BASE_64
        elif base <= 91: symbols = BASE_91
        else: return 'Invalid base'
    return ''.join(symbols[i] for i in numberToArr(n, base))

def numberToArr(n, base):
    if n == 0: return [0]
    digits = []
    while n:
        digits.append(n % base)
        n //= base
    return digits[::-1]

def arrToDecimal(arr, base):
    res = 0
    for i,n in enumerate(arr[::-1]):
        res += n * base ** i
    return res

def main():
    number = int(input('Number: '))
    base = int(input('Base: '))
    symbols = input('Symbols (empty for auto up to base 91): ')
    print(baseToBase(number, base, symbols))

main()