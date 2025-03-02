with open("practice.txt", "w+") as f:
    f.write("hi everyone\nwe are learning file i/o\nusing java.\ni like programming in java.")
    f.seek(0)
    letter = f.read()
    print(letter)