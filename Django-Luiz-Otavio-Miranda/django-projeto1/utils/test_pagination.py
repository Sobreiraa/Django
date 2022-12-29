from unittest import TestCase
from utils.pagination import make_pagination_range

# [1] 2 3 4 5 6 7 8 9 10 ...
# 1 [2] 3 4 5 6 7 8 9 10 ...
# 4 5 6 7 [8] 9 10 11 12 ...

class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            qty_paginas=4,
            current_page=1,
        )
        self.assertEqual([1,2,3,4], pagination)

    