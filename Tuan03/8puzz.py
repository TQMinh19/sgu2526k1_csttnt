from collections import deque
from typing import List, Tuple, Set

class EightPuzzle:
    def __init__(self, initial_state: List[int], goal_state: List[int]):
        """
        Khởi tạo bài toán 8-Puzzle
        initial_state: trạng thái ban đầu (0 đại diện cho ô trống)
        goal_state: trạng thái đích
        """
        self.initial_state = tuple(initial_state)
        self.goal_state = tuple(goal_state)
        self.moves = []
        
    def get_neighbors(self, state: Tuple) -> List[Tuple]:
        """Tìm tất cả các trạng thái có thể đạt được từ trạng thái hiện tại"""
        state_list = list(state)
        empty_pos = state_list.index(0)  # Tìm vị trí ô trống
        neighbors = []
        row, col = empty_pos // 3, empty_pos % 3
        
        # Các hướng di chuyển: xuống, lên, trái, phải
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_pos = new_row * 3 + new_col
                new_state = state_list.copy()
                new_state[empty_pos], new_state[new_pos] = new_state[new_pos], new_state[empty_pos]
                neighbors.append(tuple(new_state))
        
        return neighbors
    
    def solve_bfs(self) -> Tuple[bool, List[Tuple]]:
        """
        Giải bài toán bằng thuật toán BFS
        Trả về (thành công hay không, danh sách các bước giải)
        """
        if self.initial_state == self.goal_state:
            return True, [self.initial_state]
        
        queue = deque([(self.initial_state, [self.initial_state])])
        visited = {self.initial_state}
        
        while queue:
            current_state, path = queue.popleft()
            
            for next_state in self.get_neighbors(current_state):
                if next_state == self.goal_state:
                    return True, path + [next_state]
                
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, path + [next_state]))
        
        return False, []
    
    def print_state(self, state: Tuple):
        """In ra một trạng thái dưới dạng bảng 3x3"""
        for i in range(3):
            row = []
            for j in range(3):
                val = state[i * 3 + j]
                row.append(str(val) if val != 0 else '0')
            print(' '.join(f'{x:2}' for x in row))
        print()
    
    def display_solution(self):
        success, path = self.solve_bfs()
        
        if success:
            print(" Tìm được lời giải!")
            print(f"Số bước: {len(path) - 1}\n")
            
            for i, state in enumerate(path):
                print(f"Bước {i}:")
                self.print_state(state)
            
            return len(path) - 1
        else:
            print(" Không thể tìm được lời giải!")
            return -1


# Bài toán từ hình ảnh
if __name__ == "__main__":
    # Trạng thái ban đầu: 4 8 1 / 6 3 _ / 2 7 5
    initial = [4, 8, 1, 6, 3, 0, 2, 7, 5]
    
    # Trạng thái đích: 1 2 3 / 4 5 6 / 7 8 _
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    puzzle = EightPuzzle(initial, goal)
    
    print("=" * 30)
    print("GIẢI BÀI 8-PUZZLE")
    print("=" * 30)
    print("\nTrạng thái ban đầu:")
    puzzle.print_state(tuple(initial))
    
    print("Trạng thái đích:")
    puzzle.print_state(tuple(goal))
    
    print("Quá trình giải:")
    print("-" * 30)
    steps = puzzle.display_solution()
