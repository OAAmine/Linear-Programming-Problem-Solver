from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable


# Create the model
model = LpProblem(name="small-problem", sense=LpMaximize)

# Initialize the decision variables
x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)

c1cx = 2
c1cy = 1
c2cx = 4
c2cy = -5
c3cx = -1
c3cy = 2
c4cx = -1
c4cy = 5

y1 = (x*0) + 2

y1

# Add the constraints to the model
model += (c1cx * x + c1cy * y <= 20, "red_constraint")
model += (c2cx * x + c2cy * y >= -10, "blue_constraint")
model += (c3cx * x + c3cy * y >= -2, "yellow_constraint")
model += (c4cx * x + c4cy * y == 15, "green_constraint")

# Add the objective function to the model
obj_func = x + 2 * y
model += obj_func
# Add the objective function to the model
# model += x + 2 * y
# Add the objective function to the model
# model += lpSum([x, 2 * y])

# Solve the problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")
for var in model.variables():
    print(f"{var.name}: {var.value()}")
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")