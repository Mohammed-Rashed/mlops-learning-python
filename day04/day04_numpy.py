import numpy as np

distances = np.array([2.5, 4.0, 7.5, 3.0, 6.0])

delivery_times = np.array([12, 18, 32, 15, 27])

print("Distances:", distances)

print("Delivery times:", delivery_times)


print("Shape:", delivery_times.shape)

print("Dimensions:", delivery_times.ndim)


average_distance = np.mean(distances)

average_time= np.mean(delivery_times)

fastest_delivery= np.min(delivery_times)

slowest_delivery= np.max(delivery_times)

time_std = np.std(delivery_times)

print("Average distance:", average_distance)
print("Average time:", average_time)
print("Fastest:", fastest_delivery)
print("Slowest:", slowest_delivery)
print("Std:", time_std)
print("Std:", round(time_std, 2))


slow_mask = delivery_times > 20

print("Mask:", slow_mask)


slow_orders = delivery_times[slow_mask]
print("Slow orders:", slow_orders)


minutes_per_km = delivery_times / distances
print("Minutes per km:",np.round(minutes_per_km, 2))



orders_matrix= np.column_stack(
    (distances,delivery_times)
)
print("Matrix shap",orders_matrix.shape)

print("first order",orders_matrix[0])

print("All delivery times:", orders_matrix[:, 1])

print("Column averages:", np.mean(orders_matrix, axis=0))


rng=np.random.default_rng(42)

random_distance = rng.uniform(
    low=1,
    high=10,
    size=5
)
print("Random distances",np.round(random_distance,2))



costs = np.array([15, 25, 30, 10, 20])

total = np.sum(costs)
maxCost= np.max(costs)
minCost = np.min(costs)
averageCost= np.mean(costs)

times = np.array([12, 35, 18, 50, 24, 42])
timeGreaterThan30 = times > 30
print("timeGreaterThan30:",timeGreaterThan30)


distances = np.array([2, 5, 8, 3, 10])
times = np.array([10, 25, 40, 18, 60])

timeForEveryKm= times/distances
ordersTimeGrtherThan5= timeForEveryKm>5
ordersGrtherThan5=distances[ordersTimeGrtherThan5]
print("timeForEveryKm: ",np.round(timeForEveryKm,2))
print(ordersTimeGrtherThan5)
print(ordersGrtherThan5)