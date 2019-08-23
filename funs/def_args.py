def hello(name, msg="Hello"):
    print(msg, name)


hello("Van", "Good morning")   # Positional
hello("Bill")
hello(msg="Hi", name="Scott")  # keyword argument (names)
