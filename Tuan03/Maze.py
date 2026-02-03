import sys
from collections import deque

class MazeProblem:
    def __init__(self):
        # Cấu hình Mê cung 6x6
        self.rows = 6
        self.cols = 6
        self.start = (0, 0)      
        self.goal = (5, 5)

        # 1. Tường Dọc (Vertical Walls)
        # v_walls[r][c] = 1 nghĩa là có tường chắn giữa cột c và c+1
        self.v_walls = [
            [0, 1, 0, 0, 0], 
            [0, 1, 0, 0, 0], 
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0], 
            [0, 1, 0, 0, 0]  
        ]
        
        # 2. Tường Ngang (Horizontal Walls)
        # h_walls[r][c] = 1 nghĩa là có tường chắn giữa hàng r và r+1
        self.h_walls = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1], # Tường chặn ở hàng 2 xuống hàng 3 (cột 4,5)
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
    
    def get_neighbors(self, pos):
        """Lấy các vị trí lân cận hợp lệ (có kiểm tra tường chắn)"""
        r, c = pos
        neighbors = []
        
        # 1. Đi LÊN (Up) -> Check tường ngang phía trên
        if r > 0 and self.h_walls[r-1][c] == 0:
            neighbors.append((r - 1, c))
            
        # 2. Đi XUỐNG (Down) -> Check tường ngang phía dưới
        if r < self.rows - 1 and self.h_walls[r][c] == 0:
            neighbors.append((r + 1, c))
            
        # 3. Đi TRÁI (Left) -> Check tường dọc bên trái
        if c > 0 and self.v_walls[r][c-1] == 0:
            neighbors.append((r, c - 1))
            
        # 4. Đi PHẢI (Right) -> Check tường dọc bên phải
        if c < self.cols - 1 and self.v_walls[r][c] == 0:
            neighbors.append((r, c + 1))
            
        return neighbors

    def print_maze(self, path=None):
        """Hàm vẽ mê cung ra màn hình dạng text (giống hình bạn gửi)"""
        path_set = set(path) if path else set()
        
        print("\n MÊ CUNG 6x6 (Kết quả):")
        
        # 1. Vẽ cạnh trên cùng
        print("  " + "+---" * self.cols + "+")
        
        for r in range(self.rows):
            # --- In nội dung ô và tường dọc ---
            line_content = "  |" # Viền trái
            for c in range(self.cols):
                # Nội dung ô: S, E, ● (đường đi)
                symbol = "   "
                if (r, c) == self.start:
                    symbol = " S "
                elif (r, c) == self.goal:
                    symbol = " E "
                elif (r, c) in path_set:
                    symbol = " ● " # Dấu chấm
                
                line_content += symbol
                
                # Tường dọc bên phải?
                if c < self.cols - 1:
                    if self.v_walls[r][c] == 1:
                        line_content += "|" 
                    else:
                        line_content += " "
            
            line_content += "|" # Viền phải cuối cùng
            print(line_content)
            
            # --- In tường ngang bên dưới ---
            if r < self.rows - 1: 
                line_seperator = "  +"
                for c in range(self.cols):
                    if self.h_walls[r][c] == 1:
                        line_seperator += "---+" # Có tường
                    else:
                        line_seperator += "   +" # Thông nhau
                print(line_seperator)
        
        # 2. Vẽ cạnh đáy dưới cùng
        print("  " + "+---" * self.cols + "+")
        print("  Chú thích: S=Start, E=End, ●=Đường đi, |=Tường dọc, ---=Tường ngang\n")

def bfs_maze(problem):
    """Tìm đường đi ngắn nhất bằng BFS"""
    queue = deque([(problem.start, [problem.start])])
    visited = {problem.start}
    
    while queue:
        current, path = queue.popleft()
        
        if current == problem.goal:
            return path
        
        for neighbor in problem.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# --- CHẠY CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    problem = MazeProblem()
    
    bfs_path = bfs_maze(problem)

    if bfs_path:
        print(f"Tìm thấy đường đi! Độ dài: {len(bfs_path)-1} bước")
        
        # Gọi hàm in dạng chữ (như hình bạn yêu cầu)
        problem.print_maze(bfs_path)
        
        print("Chi tiết tọa độ:")
        print(" -> ".join([str(pos) for pos in bfs_path]))
    else:
        print("Không tìm thấy đường đi!")
        print(" Không tìm thấy đường đi")
    
    print("\n" + "=" * 60)
    print("Kết luận: BFS tìm ra đường đi ngắn nhất")
    print("=" * 60)
