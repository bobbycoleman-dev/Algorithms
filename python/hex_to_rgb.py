hex = "#FF9933"


def hex_string_to_RGB(hex):
    hex = hex[1:]
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i : i + 2], 16)
        rgb.append(decimal)

    return {"r": rgb[0], "g": rgb[1], "b": rgb[2]}


print(hex_string_to_RGB(hex))
