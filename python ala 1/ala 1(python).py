print("Hostel Visitor")

visitors = []

for i in range(3):
    name = input("Enter visitor name: ")
    visitors.append(name)

print("Visitors:", visitors)

if len(visitors) > 0:
    print("Logged")
else:
    print("No Visitors")

for i in range(2):
    print("Done")

print("End")