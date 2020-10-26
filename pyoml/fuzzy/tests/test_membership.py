from pyoml.fuzzy.membership import TriMF

def test_trimf_set_abc_params():
    # Test getting/setting the parameters of the Triangular MF
    mf = TriMF(2,1,0)
    assert mf.get_params() == (0,1,2)