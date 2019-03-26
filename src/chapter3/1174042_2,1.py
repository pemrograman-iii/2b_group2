def mod(x):
    i = 3
    if (x % i) == 1:
        print("# # ###   #   #    #  #")
        print("# #   #  ##  # #  ## # #")
        print("# #   # ###  # # ###  #")
        print("# #   #   #   #    # ###")
    else:
        print("tetot")
    return x

x = int(input("Masukkan NPM: "))
c = mod(x)