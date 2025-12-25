def count_nested_levels(nested_documents, target_document_id, level=1):
    # 当前层没有子节点
    if not nested_documents:
        return -1

    for key, children in nested_documents.items():
        # 当前层命中
        if key == target_document_id:
            return level

        # 向下递归
        found_level = count_nested_levels(children, target_document_id, level + 1)

        # 如果在子树中找到了，向上传播
        if found_level != -1:
            return found_level

    # 当前层及所有子树都没找到
    return -1




run_cases = [
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 2, 2),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 9, 4),
]

submit_cases = run_cases + [
    ({}, 1, -1),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 5, 4),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 20, -1),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Input tree: {input1}")
    print(f"Input document id: {input2}")
    print(f"Expected: {expected_output}")
    result = count_nested_levels(input1, input2)
    print(f"Actual:   {result}")
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
