# Request the input
mass = float(input("Enter the object's mass: ")) 
velocity = float(input("Enter the object's velocity: "))  

# Compute the results
momentum = mass * velocity
kinetic = (1/2) * mass * velocity * velocity

# Display the results

print("The object's momentum is", momentum)
print("The object's kinetic energy is", kinetic)
