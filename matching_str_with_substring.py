def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)  #will give length of substring
    
    for i in range(len(string) - sub_len + 1): # 7 - 3 + 1 this ensures the running of loop in 3 pairs 
            if string[i:i+sub_len] == sub_string: # this will work as [0:3], [1:4], [2:5], [3:6], [4:7] -> the last indices are not included in slicing
                count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)