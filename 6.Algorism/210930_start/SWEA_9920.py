'''
이진수1
- 16진수 1자리 -> 2진수 4자리

'''

for tc in range(1, int(input())+1):
    n, hexa = input().split()
    binary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    res = ''
    for i in hexa:
        res += binary[i]
    print(f'#{tc} {res}')