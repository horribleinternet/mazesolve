import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_small(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 32
        num_rows = 24
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_entance_exit(self):
        num_cols = 20
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m1._Maze__cells[-1][-1].has_bottom_wall)
        self.assertFalse(m1._Maze__cells[19][14].has_bottom_wall)

    def test_maze_visited_reset(self):
        num_cols = 20
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        all = False
        for col in m1._Maze__cells:
            for cell in col:
                all = all or cell.visited
        self.assertFalse(all)

if __name__ == "__main__":
    unittest.main()
