
def change_bullet_style(document:str):
    return '\n'.join(list(map(convert_line,document.split('\n'))))


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line




run_cases = [
    (
        "* Alai\n- Dink Meeker\n",
        "* Alai\n* Dink Meeker\n",
    ),
    (
        "* Ender Wiggin\n- Petra Arkanian\n* Bean\n",
        "* Ender Wiggin\n* Petra Arkanian\n* Bean\n",
    ),
]

submit_cases = run_cases + [
    (
        "- Bonzo Madrid\n- Stilson\n- The Formics\n- Peter Wiggin\n- Valentine Wiggin\n- Colonel Graff\n",
        "* Bonzo Madrid\n* Stilson\n* The Formics\n* Peter Wiggin\n* Valentine Wiggin\n* Colonel Graff\n",
    ),
]


def test(input_document, expected_output):
    print("---------------------------------")
    print("Input document:")
    print(input_document)
    print("Expected output:")
    print(expected_output)
    result = change_bullet_style(input_document)
    print("Actual output:")
    print(result)
    if result == expected_output:
        print("Pass")
        return True
    if expected_output.endswith("\n") and not result.endswith("\n"):
        print("Fail")
        print("Reason: expected newline at the end of the output")
        return False
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