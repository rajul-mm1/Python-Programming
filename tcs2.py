def calc_vehicles(v, w):
    if w < 2 or w % 2 != 0 or v>=w:
        print("invalid input")
        return 

    fw = (w - (2 * v)) // 2
    tw = v - fw

    if tw < 0 or fw < 0:
        print("invalid input")

    print(f"TW={tw} FW={fw}")

v = int(input().strip())
w = int(input().strip())
calc_vehicles(v,w)