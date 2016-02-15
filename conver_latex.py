import json
import pprint


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

with open("material_colors.json", 'r') as json_file:
    colors = json.load(json_file)

def_colors = []
for color in colors.keys():
    # print color.lower()
    tmp_color = color.replace("-", "_")
    for shade in colors[color]:
        full_color = tmp_color.lower() + "_" + shade.lower()
        # print full_color
        r, g, b = hex_to_rgb(colors[color][shade])
        # print str(hex_to_rgb(colors[color][shade]))
        if r != 0:
            if r ==255:
                r = "1"
            else:
                r = str(float(r)/255)
        else: r = str(r)

        if g != 0:
            if g==255:
                g = "1"
            else:
                g = str(float(g)/255)
        else: g = str(g)

        if b != 0:
            if b==255:
                b = "1"
            else:

                b = str(float(b)/255)
        else: b = str(b)





        # r = str(r/255) if r: else 0
        # g = str(g/255) if g: else 0
        # b = str(b/255) if g: else 0
        print r

        def_colors.append("\definecolor{" + full_color + "}{rgb}{" + r +", " + g +", " + b + "}\n")
        # print colors[color][shade]
# pprint.pprint(colors)

with open("material_colors.tex", 'w') as file:
    # for thing in def_colors:
        file.writelines(def_colors)
