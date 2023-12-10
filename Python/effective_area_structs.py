def get_points_from_input():
    points = []
    try:
        num_points = int(input("Enter the number of points: "))
        for i in range(num_points):
            x = float(input("Enter z-coordinate for point {}: ".format(i + 1)))
            y = float(input("Enter y-coordinate for point {}: ".format(i + 1)))
            area = float(input("Enter area for point {}: ".format(i + 1)))
            points.append([x, y, area])
        return points
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return None

points = get_points_from_input()

sum_weighted_z = 0
sum_weighted_y = 0
total_area = 0

for i in range(len(points)):
    z = points[i][0]
    y = points[i][1]
    area = points[i][2]

    sum_weighted_z += z * area
    sum_weighted_y += y * area
    total_area += area

# Calculate the centroid
centroid_z = sum_weighted_z / total_area
centroid_y = sum_weighted_y / total_area

points_shifted = [point[:] for point in points]
for i in range(len(points_shifted)):
    points_shifted[i][0] -= centroid_z
    points_shifted[i][1] -= centroid_y

# Display the centroid coordinates
print('Centroid Coordinates (z,y): ({:.2f}, {:.2f})'.format(centroid_z, centroid_y))

print('Shifted Points:')
print('Z,Y,A')
for point in points_shifted:
    print(point)

# I am very dyslexic
shifted_points = [point[:] for point in points_shifted]
Iy = 0
Iz = 0
Iyz = 0

for i in range(len(shifted_points)):
    z = shifted_points[i][0]
    y = shifted_points[i][1]
    area = shifted_points[i][2]

    Iy += area * z**2
    Iz += area * y**2
    Iyz += area * z * y

print('Iy = {:.4f} in^4'.format(Iy))
print('Iz = {:.4f} in^4'.format(Iz))
print('Iyz = {:.4f} in^4'.format(Iyz))


My = float(input("Enter My: "))
Mz = float(input("Enter Mz: "))

sigmafirst = (Iy*Mz + Iyz*My)/(Iy*Iz - Iyz**2)
sigmasecond = (Iyz*Mz + Iz*My)/(Iy*Iz - Iyz**2)

print('STRESS EQUATION')
print('(({:.4g} * {:.4g} + {:.4g} * {:.4g}) * (-y_bar) + ({:.4g} * {:.4g} + {:.4g} * {:.4g}) * z_bar) / ({:.4g} * {:.4g} - {:.4g}^2)'.format(Iy, Mz, Iyz, My, Iyz, Mz, Iz, My, Iy, Iz, Iyz))

print('sigma=-({:.2f})y+({:.2f})z'.format(sigmafirst, sigmasecond))

print( '(-) is comp, + ten')

sigmatable = [0] * len(shifted_points)

for i in range(len(shifted_points)):
    sigmatable[i] =  sigmafirst*-shifted_points[i][1] + sigmasecond*shifted_points[i][0]

for value in sigmatable:
    print('sigmax = {:.4g}'.format(value))

Vy = float(input("Enter Vy: "))
Vz = float(input("Enter Vz: "))  

print('SHEAR FLOW')
print('(({:.4g} * {:.4g} - {:.4g} * {:.4g}) * (y_bar*A) + (-{:.4g} * {:.4g} + {:.4g} * {:.4g}) * (z_bar*A) / ({:.4g} * {:.4g} - {:.4g}^2)'.format(Iy, Vy, Iyz, Vz, Iyz, Vy, Iz, Vz, Iy, Iz, Iyz))

qfirst = (Iy*Vy - Iyz*Vz)/(Iy*Iz - Iyz**2)
qsecond = (-Iyz*Vy + Iz*Vz)/(Iy*Iz - Iyz**2)
print('q_o - qin = (({:.2f})y+({:.2f})z)A'.format(qfirst, qsecond))

qtable = [0] * len(shifted_points)
for i in range(len(shifted_points)):
    qtable[i] =  (qfirst*shifted_points[i][1] + qsecond*shifted_points[i][0])*shifted_points[i][2]

for valueq in qtable:
    print('qout - qin = {:.4g}'.format(valueq))

print('KEEPING Vs')
vyfirst = Iy/(Iy*Iz - Iyz**2)
vysecond = -Iyz/(Iy*Iz - Iyz**2)
vzfirst = -Iyz/(Iy*Iz - Iyz**2)
vzsecond = Iz/(Iy*Iz - Iyz**2)

print('qout-qin = A*([{:.4g}y + {:.4g}z]Vy + [{:.4g}y + {:.4g}z]Vz)'.format(vyfirst,vysecond,vzfirst,vzsecond))

qvtable = [0] * len(shifted_points)

for i in range(len(shifted_points)):
    vycoef =  (vyfirst*shifted_points[i][1] + vysecond*shifted_points[i][0])*shifted_points[i][2]
    vzcoef =  (vzfirst*shifted_points[i][1] + vzsecond*shifted_points[i][0])*shifted_points[i][2]
    print('qout-qin ={:.4g}Vy + {:.4g}Vz'.format(vycoef,vzcoef))



