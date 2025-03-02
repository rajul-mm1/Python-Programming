a = 'abcdefghijklmnopqrstuvwxyz'
def print_rangoli(size):
    lines = []
    
    for row in range(size):
        alpha = '-'.join(a[row:size])
        lines.append(alpha[::-1] + alpha[1:])
        
    width = len(lines[0])
        
    for row in range(size-1, 0, -1):
        print(lines[row].center(width, '-'))
            
    for row in range(size):
        print(lines[row].center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)