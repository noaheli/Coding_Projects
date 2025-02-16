import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    ### This file is for familiarizing myself with the basic functions, runtimes, and syntax of the datastructures of python ###
    return


@app.cell
def __():
    ### LIST ###
    ### Insert or Delete from beginning or end O(1)
    ### Insert or Delete in middle O(n)
    ### Search O(n) [O(log n) if sorted]

    l = [1, 2, 3, 4]

    l.append(5)
    print(f"l after popping {l.pop()}: {l}")
    l.insert(1, 3)
    print(f"l after inserting 1 at index 3: {l}")
    print(f"remove value 2: {l.remove(2)}")
    print(f"reverse! {l.reverse()}")
    print(f"resort! {l.sort()}")
    return (l,)


@app.cell
def __():
    ### TUPLE ###
    ### Ordered, immutable sequence. Use for keys or multiple return values from fuctions
    ### Access is O(1)
    t = (1, 2, 3)
    x, y, z = t
    print(x, y, z)
    return t, x, y, z


@app.cell
def __():
    ### SET
    ### Unordered, all unique elements
    ### Fast lookups and set operations
    ### Add/Remove O(1), Search O(1)

    s = {1, 2, 3}
    s.add(4)
    print(s)
    s.remove(1)
    print(s)
    s.discard(10)
    print(s)
    s = s.union({5, 6})
    print(s)
    s = s.intersection({2, 4, 6})
    print(s)
    return (s,)


@app.cell
def __():
    ### DICTIONARY WOO
    ### Key value pairs, basically a map. Fast insert, deletion, and lookup
    ### Access: O(1), Insert/Delete O(1)

    d = {'a': 1, 'b': 2}
    d['c'] = 3
    print(d)
    d.pop('b')
    print(d)
    for key in d.keys():
        print(key)
    for value in d.values():
        print(value)
    for item in d.items():
        print(item)
    #zip fun
    for pair in zip(d.keys(), d.values()):
        n, m = pair
        print(f"{n}: {m}")
    return d, item, key, m, n, pair, value


@app.cell
def __():
    ### QUEUES
    ### Double ended queue. scrape from the top or bottom
    ### append / pop from both ends, O(1)
    from collections import deque
    q = deque([1, 2, 3])
    print(q)
    q.append(4)
    print(q)
    q.appendleft(0)
    print(q)
    print(f"popping {q.pop()}...")
    print(q)
    print(f"popping left {q.popleft()}...")
    print(q)
    return deque, q


@app.cell
def __():
    ### HEAPS
    ### Min-heap by default, can simulate max heap using negation
    ### insert: O(log n), delete: O(log n), Peek min: O(1)
    import heapq
    h = [3, 1, 4, 1, 5]
    heapq.heapify(h)
    print(h)
    heapq.heappush(h, 2)
    print(h)
    heapq.heappop(h)
    print(h)
    return h, heapq


if __name__ == "__main__":
    app.run()
