def chessboard(n = 8):
    for i in range(0, n):
        if(i % 2):
            i = "# " * int(n / 2)
            print(i)
        else:
            i = " #" * int(n / 2)
            print(i)

c = chessboard()
print(c)