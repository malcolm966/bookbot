from __future__ import annotations

class Rectangle:
    def overlaps(self, rect:Rectangle):
        return not (
            self.get_right_x() <= rect.get_left_x() or
            self.get_left_x() >= rect.get_right_x() or
            self.get_top_y() <= rect.get_bottom_y() or
            self.get_bottom_y() >= rect.get_top_y()
        )



    # don't touch below this line

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"


run_cases = [
    (Rectangle(0, 0, 4, 4), Rectangle(3, 3, 6, 6), True),
    (Rectangle(0, 0, 4, 4), Rectangle(5, 5, 8, 8), False),
]

submit_cases = run_cases + [
    (Rectangle(0, 0, 1, 1), Rectangle(4, 4, 5, 5), False),
    (Rectangle(1, 1, 4, 4), Rectangle(2, 2, 3, 3), True),
    (Rectangle(1, 1, 2, 2), Rectangle(0, 0, 4, 4), True),
    (Rectangle(1, 1, 4, 4), Rectangle(1, 1, 4, 4), True),
    (Rectangle(0, 0, 4, 1), Rectangle(1, 2, 3, 3), False),
]


def test(rect1, rect2, expected_overlap):
    print("---------------------------------")
    print(f"Checking overlap of:")
    print(f" - {rect1}")
    print(f" - {rect2}")
    print("")
    print(f"Expected overlap: {expected_overlap}")

    result = rect1.overlaps(rect2)
    print(f"Actual overlap:   {result}")

    if result == expected_overlap:
        print("Pass")
        return True
    else:
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
