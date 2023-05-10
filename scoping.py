def d():
    animal = "dog"

    def e():
        nonlocal animal
        animal = "cat"
        print("inside nested function:"+animal)

    print("before calling nested function:"+animal)
    e()
    print("after calling nested function:"+animal)


animal = "wombat"
d()
print("at top level:"+animal)
