def find_longest_word(document:str, longest_word=""):
    lst = document.split(maxsplit=1)
    if len(lst) == 0:
        return longest_word
    if len(lst[0]) > len(longest_word):
        longest_word = lst[0]
    if(len(lst) > 1):
        longest_word = find_longest_word(lst[1], longest_word)
    return longest_word


run_cases = [
    ("Either that wallpaper goes, or I do.", "wallpaper"),
    (
        "Then I die happy",
        "happy",
    ),
    (
        "Et tu, Brute?",
        "Brute?",
    ),
]

submit_cases = run_cases + [
    (
        "",
        "",
    ),
    (
        " ",
        "",
    ),
    (
        "Let us cross over the river and rest under the shade of the trees",
        "cross",
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: '{input1}'")
    print(f"Expected: '{expected_output}'")
    result = find_longest_word(input1)
    print(f"Actual:   '{result}'")
    if result == expected_output:
        print("Pass")
        return True
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
