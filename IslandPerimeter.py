class Solution:
    """
    You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
    Determine the perimeter of the island.
    https://leetcode.com/problems/island-perimeter/description/
    """

    def __init__(self):
        """
        :return: null
        """
        self.grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

    def island_perimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            grid = self.grid

        row = len(grid)
        col = len(grid[0])
        ret_val = 0

        for idx_r in range(row):
            for idx_c in range(col):
                up = idx_r + 1
                down = idx_r - 1
                left = idx_c - 1
                right = idx_c + 1

                if grid[idx_r][idx_c] == 1:
                    val = 4
                    if up < row and grid[up][idx_c] == 1:
                        val -= 1
                    if down >= 0 and grid[down][idx_c] == 1:
                        val -= 1
                    if right < col and grid[idx_r][right] == 1:
                        val -= 1
                    if left >= 0 and grid[idx_r][left] == 1:
                        val -= 1

                    ret_val += val

        return ret_val


def main():
    """
    :rtype: int
    """
    test = Solution()
    print(test.island_perimeter([]))


if __name__ == '__main__':
    main()
