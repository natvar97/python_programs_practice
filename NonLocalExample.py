def outer_function():
    var = 10

    def inner_function():
        nonlocal var
        var = 14
        print(f"Value of var inside inner_function() = {var}")

    inner_function()
    print(f"Value of var inside outer_function() = {var}")


outer_function()
