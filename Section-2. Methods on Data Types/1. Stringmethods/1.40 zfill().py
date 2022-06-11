"""
    String Method: zfill()
    ======================
    # Syntax : str.zfill( width )
    # zfill() does take a single parameter
    # 'width' needs to be greater in length because to fill's 0's leftover
      in the given the string.
    # Returns a shallow copy of the given string with 0's fill
      leftover the string.
    # Note: len(width) is lesser than len(given string), it leaves
            the string unmodified.

"""
print("======================================================")
# when len(width) is lesser than len(given str)
# Returns the unmodified string means same as given string
t = "programming is fun"
print(t)
r = t.zfill(6)
print(r)


print("======================================================")
# when len(width) is greater than len(given str)
# Returns fill with 0's on left in the given string
t = "programming is fun"
print(t)
print("Length of the String :", len(t))
r = t.zfill(19)
print(r)
r = t.zfill(24)
print(r)


print("======================================================")
n = "^%&*#randomtxt"
print(n)
r = n.zfill(20)
print(r)

print("======================================================")
# works with Sign Prefix
# Some Sign Prefix are say--> + , - , --
# when single - sign is given
n = "-23425"
print(n)
r = n.zfill(8)
print(r)

print("======================================================")
# when double -- sign is given
n = "--randomtxt"
print(n)
r = n.zfill(20)
print(r)

print("======================================================")
# when single + sign is given
n = "+23425"
print(n)
r = n.zfill(8)
print(r)

print("======================================================")
# when double ++ sign is given
n = "+23425"
print(n)
r = n.zfill(8)
print(r)

print("======================================================")
n = "++randomtxt"
print(n)
r = n.zfill(20)
print(r)

print("======================================================")

