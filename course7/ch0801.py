def file_type_aggregator(func_to_decorate):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
        result = func_to_decorate(doc, file_type)

        return result, counts

    return wrapper


# don't touch above this line
@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: '{doc}'. File Type: {file_type}"



run_cases = [
    (
        ("Welcome to the jungle", "txt"),
        ("Processing doc: 'Welcome to the jungle'. File Type: txt", {"txt": 1}),
    ),
    (
        ("We've got fun and games", "txt"),
        ("Processing doc: 'We've got fun and games'. File Type: txt", {"txt": 2}),
    ),
    (
        ("We've got *everything* you want honey", "md"),
        (
            "Processing doc: 'We've got *everything* you want honey'. File Type: md",
            {"txt": 2, "md": 1},
        ),
    ),
]

submit_cases = run_cases + [
    (
        ("We are the champions my friends", "docx"),
        (
            "Processing doc: 'We are the champions my friends'. File Type: docx",
            {"txt": 2, "md": 1, "docx": 1},
        ),
    ),
    (
        ("print('hello world')", "py"),
        (
            "Processing doc: 'print('hello world')'. File Type: py",
            {"txt": 2, "md": 1, "docx": 1, "py": 1},
        ),
    ),
]


def test(inputs, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    for inp in inputs:
        print(f" * {inp}")
    print(f"Expected:")
    for out in expected_output:
        print(f" * {out}")
    counts = process_doc(*inputs)
    print(f"Actual:")
    for out in counts:
        print(f" * {out}")

    if counts == expected_output:
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
