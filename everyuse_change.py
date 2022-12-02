def f(x, y):
    return x//y, x%y
def dec_to_any(num,system):
    if num < 0:
        return "-"+dec_to_any(abs(num))
    base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('a'), ord('a')+system-10)]
    ls = []
    print(base)
    while True:
        num, r = f(num, system)
        ls.append(base[r])
        print(ls)
        if num == 0:
            return "".join(ls[::-1])
def ask():
    anynum=int(input('Enter in the number of system: '))
    num=int(input('Enter in the number: '))
    print(dec_to_any(num,anynum))
if __name__=='__main__':
    ask()