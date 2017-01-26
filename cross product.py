__author__ = 'johnstivers'

print("Welcome to Cross Product Calculator")

VectorOne = input("Please enter the components of vector one, separated by commas.")
VectorTwo = input("Please enter the components of vector two, separated by commas.")

VectorOne = VectorOne.split(',')
VectorTwo = VectorTwo.split(',')

VectorOne = [int(num) for num in VectorOne]
VectorTwo = [int(num) for num in VectorTwo]

Xcomponent = ((VectorOne[1]*VectorTwo[2]) - (VectorTwo[1]*VectorOne[2]))
Ycomponent = -((VectorOne[0]*VectorTwo[2])-(VectorTwo[0]*VectorOne[2]))
Zcomponent = ((VectorOne[0]*VectorTwo[1])-(VectorOne[1]*VectorTwo[0]))

print("<",Xcomponent,",",Ycomponent,",",Zcomponent,">")
print("Have a nice day!")

