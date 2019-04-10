def tryExceptError():
    try:
        from p1174063_titik import batang as bar
    except SyntaxError:
        print("error boss")

tryExceptError()