a = input()
global email

def test(a):
    print("var",a)
    global email
    email =a
    print(email)

def test1():
    global email
    email+="hello"
    print(email)

test(a)
test1()