class TestExamples:
    def test_math(self):
        a = 5
        b = 5
        expected_res = 10
        assert a + b == expected_res, f"a + b !={expected_res}"

    def test_math_1(self):
        a = 5
        b = 5
        expected_res = 25
        assert a * b == expected_res, f"a * b !={expected_res}"