def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        # 1. 处理位置参数
        new_args = list(map(convert_md_to_txt, args))

        # 2. 处理关键字参数
        def convert_item(item):
            key, value = item
            return key, convert_md_to_txt(value)

        new_kwargs = dict(map(convert_item, kwargs.items()))

        # 3. 调用原函数
        return func(*new_args, **new_kwargs)

    return wrapper

def convert_md_to_txt_for_kw(*args):
    print(args)
    return {args[0]:args[1]}

# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)

@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""  First: {first_doc}
  Second: {second_doc}"""


@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""  Title: {title}
  Body: {body}
  Conclusion: {conclusion}"""


run_cases = [
    (
        ("# We like to play it all", "## Welcome to Tally Hall"),
        {},
        concat,
        """  First: We like to play it all
  Second: Welcome to Tally Hall""",
    ),
    (
        set(),
        {
            "title": "Why Python is Great",
            "body": "Maybe it isn't",
            "conclusion": "## That's why Python is great!",
        },
        format_as_essay,
        """  Title: Why Python is Great
  Body: Maybe it isn't
  Conclusion: That's why Python is great!""",
    ),
]

submit_cases = run_cases + [
    (
        ("# Boots' grocery list", "Salmon, gems, arcanum crystals"),
        {
            "conclusion": "## Don't forget!",
        },
        format_as_essay,
        """  Title: Boots' grocery list
  Body: Salmon, gems, arcanum crystals
  Conclusion: Don't forget!""",
    ),
]


def test(args, kwargs, func, expected_output):
    print("---------------------------------")
    print(f"Positional Arguments:")
    for arg in args:
        print(f" * {arg}")
    print(f"Keyword Arguments:")
    for key, value in kwargs.items():
        print(f" * {key}: {value}")
    print(f"Expected:")
    print(expected_output)
    try:
        result = func(*args, **kwargs)
    except Exception as error:
        result = f"Error: {error}"
    print(f"Actual:")
    print(result)
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