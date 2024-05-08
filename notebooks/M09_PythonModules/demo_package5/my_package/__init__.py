# import my_package.my_module
# print(1, "import my_package.my_module")

# from my_package import my_module
# print(2, "from my_package import my_module")

# from my_package.my_module import my_function
# print(3, "from my_package.my_module import my_function")

from .my_module import my_function
print(4, "from .my_module import my_function")