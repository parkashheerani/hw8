import pytest
import answer

class TestAnswer():
    __correct__ = 0
    __total__ = 0

    @classmethod
    def setup_class(cls):
        print("Before")
        cls.__correct__ = 0
        cls.__total__ = 0

    @classmethod
    def teardown_class(cls):
        print(f"Score:{(cls.__correct__ / cls.__total__) * 100}%")

    def test_Q1_normal_1(self):
        TestAnswer.__total__ += 1
        n = 4
        result = answer.isPowerOfFour(n)
        assert (result == True)
        TestAnswer.__correct__ += 1

    def test_Q1_normal_2(self):
        TestAnswer.__total__ += 1
        n = 16
        result = answer.isPowerOfFour(n)
        assert (result == True)
        TestAnswer.__correct__ += 1
    
    def test_Q1_normal_3(self):
        TestAnswer.__total__ += 1
        n = 1024
        result = answer.isPowerOfFour(n)
        assert (result == True)
        TestAnswer.__correct__ += 1

    def test_Q1_check_1(self):
        TestAnswer.__total__ += 1
        n = 15
        result = answer.isPowerOfFour(n)
        assert (result == False)
        TestAnswer.__correct__ += 1

    def test_Q1_check_2(self):
        TestAnswer.__total__ += 1
        n = 63
        result = answer.isPowerOfFour(n)
        assert (result == False)
        TestAnswer.__correct__ += 1

    def test_Q1_check_3(self):
        TestAnswer.__total__ += 1
        n = 1023
        result = answer.isPowerOfFour(n)
        assert (result == False)
        TestAnswer.__correct__ += 1       

    def test_Q2_normal_1(self):
        TestAnswer.__total__ += 1
        nums = [1,2,3,4]
        result = answer.runningSum(nums)
        assert (result == [1,3,6,10])
        TestAnswer.__correct__ += 1       

    def test_Q2_normal_2(self):
        TestAnswer.__total__ += 1
        nums = [1,1,1,1,1]
        result = answer.runningSum(nums)
        assert (result == [1,2,3,4,5])
        TestAnswer.__correct__ += 1   

    def test_Q2_normal_3(self):
        TestAnswer.__total__ += 1
        nums = [3,1,2,10,1]
        result = answer.runningSum(nums)
        assert (result == [3,4,6,16,17])
        TestAnswer.__correct__ += 1   

    def test_Q2_normal_4(self):
        TestAnswer.__total__ += 1
        nums = [2,6,3,2,1,3,7,5,3,6]
        result = answer.runningSum(nums)
        assert (result == [2,8,11,13,14,17,24,29,32,38])
        TestAnswer.__correct__ += 1   
    
    def test_Q3_normal_1(self):
        TestAnswer.__total__ += 1
        nums = [1,2,10,5,7]
        result = answer.canBeIncreasing(nums)
        assert (result == True)
        TestAnswer.__correct__ += 1

    def test_Q3_normal_2(self):
        TestAnswer.__total__ += 1
        nums = [1,2,3]
        result = answer.canBeIncreasing(nums)
        assert (result == True)
        TestAnswer.__correct__ += 1

    def test_Q3_normal_3(self):
        TestAnswer.__total__ += 1
        nums = [1,5,9,6,7,8,9]
        result = answer.canBeIncreasing(nums)
        assert (result == True)
        TestAnswer.__correct__ += 1

    def test_Q3_check_1(self):
        TestAnswer.__total__ += 1
        nums = [2,3,1,2]
        result = answer.canBeIncreasing(nums)
        assert (result == False)
        TestAnswer.__correct__ += 1

    def test_Q3_check_2(self):
        TestAnswer.__total__ += 1
        nums = [1,1,1]
        result = answer.canBeIncreasing(nums)
        assert (result == False)
        TestAnswer.__correct__ += 1

    def test_Q4_normal_1(self):
        TestAnswer.__total__ += 1
        n = 2
        result = answer.trailingZeroes(n)
        assert (result == 0)
        TestAnswer.__correct__ += 1    

    def test_Q4_normal_2(self):
        TestAnswer.__total__ += 1
        n = 5
        result = answer.trailingZeroes(n)
        assert (result == 1)
        TestAnswer.__correct__ += 1    

    def test_Q4_normal_3(self):
        TestAnswer.__total__ += 1
        n = 10
        result = answer.trailingZeroes(n)
        assert (result == 2)
        TestAnswer.__correct__ += 1    

    def test_Q4_normal_4(self):
        TestAnswer.__total__ += 1
        n = 15
        result = answer.trailingZeroes(n)
        assert (result == 3)
        TestAnswer.__correct__ += 1    

    def test_Q4_normal_5(self):
        TestAnswer.__total__ += 1
        n = 20
        result = answer.trailingZeroes(n)
        assert (result == 4)
        TestAnswer.__correct__ += 1    