print("Contoh Rekursif Function".center(75, "="))


def rekursif(k):
    if(k > 0):
        result = k + rekursif(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nHasil")
rekursif(int(input("Input Angka : ")))
