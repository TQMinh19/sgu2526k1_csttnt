# Bài 1: Xác định các yêu tố của bài toán tìm kiếm
# Bài toán: Tìm đường đi từ đỉnh A đến đỉnh D trên đồ thị

from collections import deque, defaultdict

# ===== ĐỊNH NGHĨA BÀI TOÁN =====
class SearchProblem:
    def __init__(self):
        # Đồ thị được biểu diễn bằng danh sách cạnh 
        self.graph = {
            'A': ['B', 'C', 'F'],
            'B': ['A', 'C', 'E', 'F'],
            'C': ['A', 'B', 'D', 'F'],
            'D': ['C', 'F'],
            'E': ['B', 'D', 'F'],
            'F': ['A', 'C', 'E']
        }
        
        # ===== CÁC YÊU TỐ CỦA BÀI TOÁN TÌM KIẾM =====
        self.initial_state = 'A'      # 1. Trạng thái ban đầu
        self.goal_state = 'D'         # 2. Trạng thái đích
        self.search_space = set(self.graph.keys())  # 3. Không gian tìm kiếm
        
    def get_operators(self, state):
        """4. Các hành động/toán tử: Trả về danh sách đỉnh kề từ state"""
        return self.graph.get(state, [])
    
    def is_goal(self, state):
        """Kiểm tra đó có phải trạng thái đích không"""
        return state == self.goal_state
    
    def print_problem_elements(self):
        """In ra các yêu tố của bài toán tìm kiếm"""
        print("=" * 60)
        print("CÁC YÊU TỐ CỦA BÀI TOÁN TÌM KIẾM")
        print("=" * 60)
        print(f"1. Trạng thái ban đầu (Initial State): {self.initial_state}")
        print(f"2. Trạng thái đích (Goal State): {self.goal_state}")
        print(f"3. Không gian tìm kiếm (Search Space): {sorted(self.search_space)}")
        print(f"4. Các hành động/Toán tử (Operators):")
        for state in sorted(self.search_space):
            neighbors = self.get_operators(state)
            print(f"   {state} → {neighbors}")
        print("5. Chi phí: Mỗi cạnh có chi phí = 1")
        print("=" * 60)

# ===== THUẬT TOÁN TÌM KIẾM BFS =====
def bfs_search(problem):
    """Tìm kiếm theo chiều rộng (Breadth-First Search)"""
    queue = deque([(problem.initial_state, [problem.initial_state])])
    visited = {problem.initial_state}
    
    while queue:
        current_state, path = queue.popleft()
        
        if problem.is_goal(current_state):
            return path
        
        for next_state in problem.get_operators(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    
    return None  # Không tìm thấy đường đi

# ===== THUẬT TOÁN TÌM KIẾM DFS =====
def dfs_search(problem):
    """Tìm kiếm theo chiều sâu (Depth-First Search)"""
    stack = [(problem.initial_state, [problem.initial_state])]
    visited = {problem.initial_state}
    
    while stack:
        current_state, path = stack.pop()
        
        if problem.is_goal(current_state):
            return path
        
        for next_state in problem.get_operators(current_state):
            if next_state not in visited:
                visited.add(next_state)
                stack.append((next_state, path + [next_state]))
    
    return None  # Không tìm thấy đường đi

# ===== MAIN =====
if __name__ == "__main__":
    # Tạo bài toán
    problem = SearchProblem()
    
    # In các yêu tố của bài toán
    problem.print_problem_elements()
    
    print("\n" + "=" * 60)
    print("KẾT QUẢ TÌM KIẾM")
    print("=" * 60)
    
    # Tìm kiếm BFS
    bfs_path = bfs_search(problem)
    if bfs_path:
        print(f"\n BFS: Đường đi từ {problem.initial_state} → {problem.goal_state}")
        print(f"  Đường đi: {' → '.join(bfs_path)}")
        print(f"  Chiều dài: {len(bfs_path) - 1} bước")
    else:
        print(f"\n BFS: Không tìm thấy đường đi")
    
    # Tìm kiếm DFS
    dfs_path = dfs_search(problem)
    if dfs_path:
        print(f"\n DFS: Đường đi từ {problem.initial_state} → {problem.goal_state}")
        print(f"  Đường đi: {' → '.join(dfs_path)}")
        print(f"  Chiều dài: {len(dfs_path) - 1} bước")
    else:
        print(f"\n DFS: Không tìm thấy đường đi")
    
    print("=" * 60)
