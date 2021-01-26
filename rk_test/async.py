async def a_hi(name):
    return 'Hi '+ name

def hi(name):
    return 'Hi '+name

print(hi("Rokib"))
print(a_hi("Rokib"))

def drive_a_hi(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value 
# ------------------
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for i in countdown(10):
    print(i)
x =countdown(20)
print(x)
print(next(x))
print(next(x))
print("--")
for i in x:
    print(i,  next(x))

print(x)