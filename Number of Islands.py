from typing import List

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
        """

        m = len(grid)
        n = len(grid[0])

        # STEP 1 : retrieve all land cells

        node_list = []
        visited_node = {}

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    node_list.append((i,j))
                    visited_node[(i,j)] = 0
        
        number_of_island = 0

        while len(node_list) > 0:

            node = node_list.pop()

            # STEP 2 : find a new Island
            if visited_node[node] == 0:  

                number_of_island += 1
                visited_node[node] = 1
                
                # STEP 3 : find all the cells of the island
                neighbours = self.findneighbours(grid, node)

                while len(neighbours) > 0:
                    
                    neighbour = neighbours.pop()

                    if visited_node[neighbour]==0:
                        visited_node[neighbour] = 1

                        new_n = self.findneighbours(grid, neighbour)
                        for n in range(len(new_n)):
                            if visited_node[new_n[n]]== 0:
                                neighbours.append(new_n[n])
        

        return number_of_island




    def findneighbours(self, grid, node):

        node_r,node_c = node
        neighbours = []

        if node_r > 0 and grid[node_r-1][node_c] == '1':
            neighbours.append((node_r-1, node_c))

        if node_c > 0 and grid[node_r][node_c-1] == '1':
            neighbours.append((node_r, node_c-1))

        if node_r < len(grid)-1 and grid[node_r+1][node_c] == '1':
            neighbours.append((node_r+1, node_c))

        if node_c < len(grid[0])-1 and grid[node_r][node_c+1] == '1':
            neighbours.append((node_r, node_c+1))
        
        return neighbours
    

S = Solution()
print(S.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))