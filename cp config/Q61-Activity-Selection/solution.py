def activitySelection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    selected = []
    last_finish = None

    for s, f in activities:
        if last_finish is None or s >= last_finish:
            selected.append((s, f))
            last_finish = f

    return selected

n = int(input("Enter number of activities: "))

start = list(map(int, input("Enter start times: ").split()))
finish = list(map(int, input("Enter finish times: ").split()))

result = activitySelection(start, finish)

print("Selected activities:", result)
print("Maximum activities:", len(result))