def test_function():
    def inner_function():
        print("I am in the function scope test_function")

    inner_function()


test_function()