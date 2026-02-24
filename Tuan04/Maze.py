import heapq
import math
name = r"D:\Python\classroom\SGU26k1_csttnt\Tuan02\lesson4\input_maze.txt"
# Đọc dữ liệu từ file input_maze.txt
with open(name, 'r') as f:
    lines = f.readlines()

# Đọc kích thước mảng
n, m = map(int, lines[0].split())

# Đọc tường dọc
wall_v = []
for i in range(n):
    wall_v.append(list(map(int, lines[1 + i].split())))

# Đọc tường ngang
wall_h = []
for i in range(n - 1):
    wall_h.append(list(map(int, lines[1 + n + i].split())))

# Đọc điểm bắt đầu và kết thúc
start = tuple(map(int, lines[1 + n + (n - 1)].split()))
goal = tuple(map(int, lines[2 + n + (n - 1)].split()))

def h_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def h_euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def h_chebyshev(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def A_star(start,goal,n,m,wall_v,wall_h):
    OPEN=[]
    heapq.heappush(OPEN,(0,start))

    parent={start:None}
    g={start:0}
    order=[] #để animate
    CLOSED=set()
    while OPEN:
        _,(x,y)=heapq.heappop(OPEN)
        if (x,y) in CLOSED:
            continue
        CLOSED.add((x,y))
        order.append((x,y))

        if (x, y) == goal:
            break
    
     # right
        if y < m-1 and wall_v[x][y] == 0:
            nxt = (x, y+1)
            cost = g[(x, y)] + 1
            if nxt not in g or cost < g[nxt]:
                g[nxt] = cost
                parent[nxt] = (x, y)
                f = cost + h_manhattan(nxt, goal)
                heapq.heappush(OPEN, (f, nxt))

        # left
        if y > 0 and wall_v[x][y-1] == 0:
            nxt = (x, y-1)
            cost = g[(x, y)] + 1
            if nxt not in g or cost < g[nxt]:
                g[nxt] = cost
                parent[nxt] = (x, y)
                f = cost + h_manhattan(nxt, goal)
                heapq.heappush(OPEN, (f, nxt))

        # up
        if x > 0 and wall_h[x-1][y] == 0:
            nxt = (x-1, y)
            cost = g[(x, y)] + 1
            if nxt not in g or cost < g[nxt]:
                g[nxt] = cost
                parent[nxt] = (x, y)
                f = cost + h_manhattan(nxt, goal)
                heapq.heappush(OPEN, (f, nxt))

        # down
        if x < n-1 and wall_h[x][y] == 0:
            nxt = (x+1, y)
            cost = g[(x, y)] + 1
            if nxt not in g or cost < g[nxt]:
                g[nxt] = cost
                parent[nxt] = (x, y)
                f = cost + h_manhattan(nxt, goal)
                heapq.heappush(OPEN, (f, nxt))
    return parent,order

def find(parent,goal):
    if goal not in parent:
        return []
    path=[]
    cur=goal
    while cur is not None:
        path.append(cur)
        cur=parent[cur]
    path.reverse()
    return path

parent,order=A_star(start,goal,n,m,wall_v,wall_h)
path=find(parent,goal)

print("Đường đi:")
print(path)

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

'''def ve_me_cung_o(n, m, wall_v, wall_h, path=None, start=None, goal=None):
    fig, ax = plt.subplots(figsize=(6,6))

    # vẽ lưới ô
    for x in range(n+1):
        ax.plot([0, m], [x, x], color="black", linewidth=1)
    for y in range(m+1):
        ax.plot([y, y], [0, n], color="black", linewidth=1)

    # vẽ tường dọc
    for x in range(n):
        for y in range(m-1):
            if wall_v[x][y] == 1:
                ax.plot([y+1, y+1], [n-x-1, n-x], color="black", linewidth=3)

    # vẽ tường ngang
    for x in range(n-1):
        for y in range(m):
            if wall_h[x][y] == 1:
                ax.plot([y, y+1], [n-x-1, n-x-1], color="black", linewidth=3)

    # vẽ đường đi của kiến (GIỮA Ô)
    if path:
        xs = [p[1] + 0.5 for p in path]
        ys = [n - p[0] - 0.5 for p in path]
        ax.plot(xs, ys, color="red", linewidth=3)

    # start & goal
    if start:
        ax.scatter(start[1]+0.5, n-start[0]-0.5, color="green", s=200)
    if goal:
        ax.scatter(goal[1]+0.5, n-goal[0]-0.5, color="blue", s=200)

    ax.set_aspect("equal")
    ax.axis("off")
    plt.title("Mê cung kiến đi")
    plt.show()  '''
def animate_maze(n, m, wall_v, wall_h, order, path, start, goal):
    fig, ax = plt.subplots(figsize=(6,6))
    path_x = [p[1] + 0.5 for p in path]
    path_y = [n - p[0] - 0.5 for p in path]

    # vẽ lưới
    for x in range(n+1):
        ax.plot([0, m], [x, x], color="black")
    for y in range(m+1):
        ax.plot([y, y], [0, n], color="black")
    
    # vẽ tường
    for x in range(n):
        for y in range(m-1):
            if wall_v[x][y]:
                ax.plot([y+1, y+1], [n-x-1, n-x], color="black", linewidth=3)

    for x in range(n-1):
        for y in range(m):
            if wall_h[x][y]:
                ax.plot([y, y+1], [n-x-1, n-x-1], color="black", linewidth=3)

    ant, = ax.plot([], [], 'o', color="orange", markersize=12)
    visited_plot, = ax.plot([], [], color="orange", linewidth=2, alpha=0.6)
    final_path, = ax.plot([], [], color="red", linewidth=3)

    ax.scatter(start[1]+0.5, n-start[0]-0.5, color="green", s=200)
    ax.scatter(goal[1]+0.5, n-goal[0]-0.5, color="blue", s=200)

    ax.set_aspect("equal")
    ax.axis("off")

    xs, ys = [], []

    def update(i):
        # ===== GIAI ĐOẠN 1: BFS =====
        if i < len(order):
            x, y = order[i]
            cx, cy = y + 0.5, n - x - 0.5
            xs.append(cx)
            ys.append(cy)

            ant.set_data([cx], [cy])
            visited_plot.set_data(xs, ys)

        # ===== GIAI ĐOẠN 2: ĐI THEO PATH =====
        else:
            j = i - len(order)   # index trong path
            if j < len(path):
                ant.set_data([path_x[j]], [path_y[j]])
                final_path.set_data(path_x[:j+1], path_y[:j+1])

        return ant, visited_plot, final_path


    total_frames = len(order) + len(path)

    ani = FuncAnimation(
    fig,
    update,
    frames=total_frames,
    interval=300,
    repeat=False
    )


    return ani
ani=animate_maze(n, m, wall_v, wall_h, order, path, start, goal)
plt.show()