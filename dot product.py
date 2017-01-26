__author__ = 'johnstivers'

print("Welcome to Dot Product Calculator")

VectorOne = input("Please enter the components of vector one, separated by commas.")
VectorTwo = input("Please enter the components of vector two, separated by commas.")

VectorOne = VectorOne.split(',')
VectorTwo = VectorTwo.split(',')

VectorOne = [int(num) for num in VectorOne]
VectorTwo = [int(num) for num in VectorTwo]

DotProduct = ((VectorOne[0]*VectorTwo[0]) + (VectorTwo[1]*VectorOne[1]) + (VectorTwo[2]*VectorOne[2]))


print("The Dot Product is:",DotProduct )
print("Have a nice day!")

