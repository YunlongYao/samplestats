from stats import mean,std
from nose.tools import assert_equal, assert_almost_equal

def test_mean():

        assert_equal(mean([2,4]), 3)
#test_mean()

def test_float_mean():
        assert_equal(mean([1,2]),1.5)
#test_float_mean()

def test_negative_mean():
	assert_almost_equal(mean([2,-2,4]), 1.3333,places = 4)
#test_negative_mean()

def test_std1():
	obs =std([0.0,2.0])
	exp =1.0
	assert_equal(obs,exp)

# print mean([2,4
