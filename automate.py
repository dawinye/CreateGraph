from matplotlib import pyplot as plt

#lists used to store the 
input_x = []
input_y = []
n = int(input("How many points do you want to graph?"))

for i in range(0, n):
    print("Enter the x-coordinate at location", i, ":")
    item = int(input())
    input_x.append(item)

for i in range(0, n):
    print("Enter the y-coordinate at location", i, ":")
    item = int(input())
    input_y.append(item)

title = input("What is the title of the graph?")
x_Label = input("What is the label of the x-axis?")
y_Label = input("What is the label of y-axis?")


plt.title(title)
plt.xlabel(x_Label)
plt.ylabel(y_Label)

plt.plot(input_x, input_y)

save = input("Would you like to save this graph?")
if save == "yes" or "Yes":
    figureName = input("What would you like to name it?")
    plt.savefig(figureName)
plt.show()
