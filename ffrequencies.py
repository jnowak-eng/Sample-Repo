import math


if __name__ == "__main__":
    s_speed = 60

    # IMP 7"
    # _numRollers = 18
    # _rollerDia = 1.559
    # _cupAngle = 9.417
    # _pitchDiam = 10.157

    # 5-15/16 ISAF
    # "NumRollers": 18, "RollerDiam": 1.409, "CupAngle": 9.667, "PitchDiam": 9.189
    _numRollers = 18
    _rollerDia = 0.78
    _cupAngle = 8.833
    _pitchDiam = 5.079

    f = s_speed / 60.0
    cos_theta = math.cos(_cupAngle * 2 * math.pi / 360.0)  # Contact angle(degrees)
    inner = (
        _numRollers * f * (1.0 + _rollerDia / _pitchDiam * cos_theta) / 2.0
    )  # Inner race fault
    outer = (
        _numRollers * f * (1.0 - _rollerDia / _pitchDiam * cos_theta) / 2.0
    )  # Outer race fault
    cage = f * (1.0 - _rollerDia / _pitchDiam * cos_theta) / 2.0  # Cage fault
    rollers = (
        _pitchDiam
        * f
        * (
            1
            - (_rollerDia / _pitchDiam * cos_theta)
            * (1 - (_rollerDia / _pitchDiam * cos_theta))
        )
        / (2 * _rollerDia)
    )  # Rollers fault

    print("Inner = " + str(inner))
    print("Outer = " + str(outer))
    print("Roller = " + str(rollers))
    print("Cage = " + str(cage))
