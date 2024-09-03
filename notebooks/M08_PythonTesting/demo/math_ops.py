# math_ops.py

class MathOps:
    
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

if __name__ == '__main__':
    print("This is the MathOps class. It's meant to be imported into another module.")
    print("But since you called it directly, I'll show you how it works!")
    
    x = 5
    y = 10
    print("5 + 10 =", MathOps.add(x, y))
    print("5 - 10 =", MathOps.subtract(x, y))
    print("5 * 10 =", MathOps.multiply(x, y))
    print("5 / 10 =", MathOps.divide(x, y))