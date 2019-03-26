class najib:
	def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def penambahan(self):
        r = self.a + self.b
        return r
		
def no1(x):
    i = 3
    if (x % i) == 1:
        print("# # ###   #   #    #  #")
        print("# #   #  ##  # #  ## # #")
        print("# #   # ###  # # ###  #")
        print("# #   #   #   #    # ###")
    else:
        print("tetot")
    return x
	
def no2(x):
    a = 0
    b = int(x[5:7])
    while a < b :
        a += 1
        print("Hello, " + x + " Apa Kabar?")
    return x
	
def no3(x):
    a = 0
    k = int(x[4])
    p = int(x[5])
    i = int(x[6])
    b = x[4:7]
    c = k+p+i

    while a < c:
        a += 1
        print("Hello, " + b + " Apa Kabar?")
    return x
	
def no4(x):
    p = x[4]
    print("Hello, " + p + " Apa Kabar?")
    return x
	
a = 1
b = 1
c = 7
d = 4
e = 0
f = 4
g = 2

def no5(x):
    npm = [a,b,c,d,e,f,g]

    for n in npm:
        print(n)
    return n
	
def no6(x):
    npm = [a+b+c+d+e+f+g]

    for n in npm:
        print(n)
    return n
	
def no7(x):
    npm = [a*b*c*d*e*f*g]

    for n in npm:
        print(n)
    return n
	
def no8(x):
    npm = [a,b,c,d,e,f,g]

    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end ="")
    return n
	
def no9(x):
    npm = [a,b,c,d,e,f,g]

    for n in npm:
        if(n % 2 != 0):
            print(n, end ="")
    return n
	
def no10(x):
    npm = [a,b,c,d,e,f,g]

    for n in npm:
        if(n % 2) == 0:
            print(end="")
        else:
            print(n, end ="")
    return n