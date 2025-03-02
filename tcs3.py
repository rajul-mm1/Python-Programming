def count_all(s):
    count_star = s.count('*')
    count_hash = s.count('#')
    return count_star - count_hash

s = input()
print(count_all(s))