import heapq # dùng để làm thuật toán A* nhanh hơn 
name = r"D:\Python\classroom\SGU26k1_csttnt\Tuan02\lesson4\input_puzzle.txt"
# đọc file
with open(name,"r") as f:
     lines = f.readlines()
# băm dữ liệu ra thành [[],[],[]]
data=[list(map(int,line.split()))for line in lines]
# chia dữ liệu đã bấm thành start và goal
start=data[:3]
goal=data[3:]
# tìm ô trống 
def find_zero(board):
     for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                return i,j

def neighbors(board):
    x,y=find_zero(board)
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    res=[]
    for dx,dy in dirs:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            new_board=[row[:] for row in board]
            new_board[x][y],new_board[nx][ny]=new_board[nx][ny],new_board[x][y]
            res.append(new_board)
    return res

def board_to_key(board):
    return tuple(map(tuple,board))

def calc_h(board,goal):
    pos={}
    for i in range(3):
        for j in range(3):
            pos[goal[i][j]]=(i,j)
    h=0
    for i in range(3):
        for j in range(3):
            v=board[i][j]
            if v!=0:
                gi,gj=pos[v]
                h+=abs(i-gi)+abs(j-gj)
    return h

def a_star(start,goal):
    open_list=[]
    visited=set()
    counter=0

    h0=calc_h(start,goal)
    start_state={
        "board":start,
        "g":0,
        "h":h0,
        "f":h0,
        "parent":None
    }

    heapq.heappush(open_list,(start_state["f"],counter,start_state))

    while open_list:
        _, _, cur= heapq.heappop(open_list)
        key=board_to_key(cur["board"])
        if key in visited:
            continue
        visited.add(key)

        if cur["board"]==goal:
            return cur
        
        for nb in neighbors(cur["board"]):
            k=board_to_key(nb)
            if k in visited:
                continue
            g=cur["g"]+1
            h=calc_h(nb,goal)

            state={
                "board":nb,
                "g":g,
                "h":h,
                "f":g+h,
                "parent":cur
            }

            counter+=1
            heapq.heappush(open_list,(state["f"],counter,state))
    return None

def print_path(state):
    path=[]
    while state:
        path.append(state["board"])
        state=state["parent"]
    path.reverse()

    for step,b in enumerate(path):
        print(f"Step {step}")
        for row in b:
            print(row)
        print()

res=a_star(start,goal)
if res:
    print_path(res)
else:
    print("khong loi giai")