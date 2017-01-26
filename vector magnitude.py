__author__ = 'johnstivers'

print("Welcome to Vector Magnitude Calculator")
choice = input("Is the vector in two dimensions or three dimensions? Specify with 2 or 3.")
VectorOne = input("Please enter the components of the vector, separated by commas.")

VectorOne = VectorOne.split(',')

VectorOne = [int(num) for num in VectorOne]

if choice == "2":
    VectorMagnitude = ((((VectorOne[0])**2)+(VectorOne[1])**2)**.5)
elif choice == '3':
    VectorMagnitude = ((((VectorOne[0])**2)+((VectorOne[1])**2)+((VectorOne[2])**2))**.5)



print("The Dot Product is:",VectorMagnitude )
print("Have a nice day!")