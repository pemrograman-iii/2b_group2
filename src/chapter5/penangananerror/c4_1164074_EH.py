import serial

def tryExceptError():
    try:
        ser = serial.Serial('COM3',9600)
        print(sre.readline().decode("utf-8").strip('\n').strip('\r'))
    except SyntaxError:
        print("Syntax Error")
    except NameError:
        print("Variable tidak dimiliki")
    except TypeError:
        print("Tipe data tidak benar")
    except:
        print("Terjadi sebuah kesalahan pada code")
tryExceptError()