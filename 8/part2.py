def euclidean_distance_squared(junction_box1: tuple[int, int, int], junction_box2: tuple[int, int, int]) -> int:
    x1, y1, z1 = junction_box1
    x2, y2, z2 = junction_box2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

junction_boxes = []
for line in open(0).read().strip().splitlines():
    junction_boxes.append(tuple(map(int, line.split(','))))

distances = []
for i, junction_box1 in enumerate(junction_boxes[:-1]):
    for junction_box2 in junction_boxes[i + 1:]:
        distance = euclidean_distance_squared(junction_box1, junction_box2)
        distances.append((junction_box1, junction_box2, distance))

sorted_distances = list(filter(lambda tup: tup[2] != 0, sorted(distances, key=lambda tup: tup[2])))

circuits = {}
circuit_id = 1
for distance in sorted_distances:
    p1, p2, d = sorted_distances.pop(0)
    if p1 not in circuits and p2 not in circuits:
        # create new circuit
        circuits[p1] = circuit_id
        circuits[p2] = circuit_id
        circuit_id += 1
    elif p1 in circuits and p2 not in circuits:
        # adjoin to circuit
        answer = p1[0] * p2[0]
        circuits[p2] = circuits[p1]
    elif p1 not in circuits and p2 in circuits:
        # adjoin to circuit
        answer = p1[0] * p2[0]
        circuits[p1] = circuits[p2]
    elif p1 in circuits and p2 in circuits and circuits[p1] == circuits[p2]:
        # do nothing, already part of same circuit
        continue
    elif p1 in circuits and p2 in circuits and circuits[p1] != circuits[p2]:
        # coalesce two circuits
        answer = p1[0] * p2[0]
        dominant_id = min(circuits[p1], circuits[p2])
        overwrite_id = max(circuits[p1], circuits[p2])
        for point in circuits:
            if circuits[point] == overwrite_id:
                circuits[point] = dominant_id
    else:
        assert False

print(answer)
