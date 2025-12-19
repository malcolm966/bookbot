def get_median_font_size(font_sizes:list):
    if not font_sizes:
        return None

    sorted_sizes = sorted(font_sizes)
    middle_index = (len(sorted_sizes) - 1) // 2

    return sorted_sizes[middle_index]