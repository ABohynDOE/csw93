import numpy as np
import pytest

from csw93 import *

# Global variables for all tests
run_sizes = [16, 32, 32, 64, 64]
design_indices = ["8-4.6", "8-3.5", "14-9.2", "12-6.2", "17-11.6"]


def test_design():
    """Function produces the correct design matrix"""
    ref_matrix = np.array(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 0, 0],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0],
        ]
    )
    comp_matrix = get_design(16, "5-1.1")
    assert (comp_matrix == ref_matrix).all()


def test_wlp():
    """Function produces the correct WLP"""
    wlps = [
        [7, 7, 0, 0, 1, 0],
        [1, 2, 3, 1, 0],
        [5, 55, 45, 96, 106],
        [8, 20, 14, 8],
        [105, 35, 280, 168],
    ]
    computed_wlps = [get_wlp(x, design_indices[i]) for i, x in enumerate(run_sizes)]
    assert all([x == wlps[i] for i, x in enumerate(computed_wlps)])


def test_cfi():
    """Function produces the correct cfi"""
    cfi = (7, 13, 3, 27, 31)
    commputed_cfi = [get_cfi(x, design_indices[i]) for i, x in enumerate(run_sizes)]
    assert all([x == cfi[i] for i, x in enumerate(commputed_cfi)])


class TestDesign:
    def test_run_size(self):
        with pytest.raises(ValueError):
            get_design(15, "8-4.1")

    def test_index(self):
        assert get_design(16, "8-3.1") is None


class TestWLP:
    def test_run_size(self):
        with pytest.raises(ValueError):
            get_wlp(15, "8-4.1")

    def test_index(self):
        assert get_wlp(16, "8-3.1") is None


class TestCfi:
    def test_run_size(self):
        with pytest.raises(ValueError):
            get_cfi(15, "8-4.1")

    def test_index(self):
        assert get_cfi(16, "8-3.1") is None


class TestCIG:
    def test_dot_content(self):
        d = clear_interaction_graph(32, "8-3.4", render=False)
        reference_dotfile = 'digraph name {\n\toverlap=false\n\t1 -> 8 [arrowhead=none]\n\t2 -> 8 [arrowhead=none]\n\t3 -> 8 [arrowhead=none]\n\t4 -> 8 [arrowhead=none]\n\t5 -> 8 [arrowhead=none]\n\t6 -> 8 [arrowhead=none]\n\t7 -> 8 [arrowhead=none]\n\t1 -> 2 [arrowhead=none color=transparent]\n\t2 -> 3 [arrowhead=none color=transparent]\n\t3 -> 4 [arrowhead=none color=transparent]\n\t4 -> 5 [arrowhead=none color=transparent]\n\t5 -> 6 [arrowhead=none color=transparent]\n\t6 -> 7 [arrowhead=none color=transparent]\n\t7 -> 8 [arrowhead=none color=transparent]\n\t8 -> 1 [arrowhead=none color=transparent]\n}\n'
        assert d.source == reference_dotfile


class TestGen:
    def test_num2word(self):
        assert num2word(7) == 'abc'

    def test_error_num2word(self):
        with pytest.raises(ValueError):
            num2word(0)
            num2word('11')

    def test_word2num(self):
        assert word2num('abd') == 11

    def test_error_word2num(self):
        with pytest.raises(ValueError):
            word2num('Abcd')
            word2num('aer@')
