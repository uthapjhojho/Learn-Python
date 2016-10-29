s = input()
while True:
    try:
        int(s)
        print(s)
        break
    except ValueError:
        print("Bad String")
