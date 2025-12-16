class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if self.__num_arrows < num:
            raise Exception('not enough arrows')
        self.__num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target:Human):
        super().use_arrows(1)
        super().use_arrows(1)
        super().use_arrows(1)
        return f'{target.get_name()} was shot by 3 crossbow bolts'




run_cases = [
    ("Will", 1, "Darren", 4, None, 1),
    ("Elena", 5, "Connor", 3, None, 0),
]

submit_cases = run_cases + [
    ("Jake", 0, "Victor", 3, None, 0),
    ("Ryan", 2, "Emma", 1, "not enough arrows", None),
    ("Zoe", 10, "Lucas", 8, None, 5),
]


def test(
    archer_name,
    archer_arrows,
    crossbowman_name,
    crossbowman_bolts,
    expected_exception,
    expected_remaining_bolts,
):
    print("---------------------------------")
    print(f"Archer: {archer_name}, Arrows: {archer_arrows}")
    archer = Archer(archer_name, archer_arrows)
    print(f"Crossbowman: {crossbowman_name}, Arrows: {crossbowman_bolts}")
    print("")
    crossbowman = Crossbowman(crossbowman_name, crossbowman_bolts)
    try:
        expected_str = f"{archer_name} was shot by 3 crossbow bolts"
        actual_str = crossbowman.triple_shot(archer)
        if expected_exception:
            print(
                f"Expected exception '{expected_exception}', but no exception occurred"
            )
            return False
        print(f"Expected triple_shot message: {expected_str}")
        print(f"Actual triple_shot message:   {actual_str}")
        if actual_str != expected_str:
            return False

        print(f"Expected remaining bolts: {expected_remaining_bolts}")
        print(f"Actual remaining bolts:   {crossbowman.get_num_arrows()}")
        if crossbowman.get_num_arrows() != expected_remaining_bolts:
            return False
        return True
    except Exception as e:
        if str(e) == expected_exception:
            print(f"Expected exception: {expected_exception}")
            print(f"Actual exception:   {e}")
            return True
        else:
            print(f"Unexpected exception: {e}")
            return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
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