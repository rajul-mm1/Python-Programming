def merge_the_tools(string, k):
    for i in range(0, len(string), k):  # Loop through substrings of length 'k'
        t = string[i:i + k]  # Extract substring
        u = ""  # Unique character string
        for char in t:
            if char not in u:  # Keep only the first occurrence
                u += char
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
