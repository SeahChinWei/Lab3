import ET0735_Lab2.BMI as BMI


def test_bmi_normal_weight():
    height=1.7
    weight=60
    test=0

    result =BMI.calculate_bmi(weight,height)

    assert (result == test)

def test_bmi_over_weight():
    height=1.7
    weight=100
    test=1

    result =BMI.calculate_bmi(weight,height)

    assert (result == test)

def test_bmi_under_weight():
    height = 1.7
    weight = 10
    test = -1

    result = BMI.calculate_bmi(weight, height)

    assert (result == test)

