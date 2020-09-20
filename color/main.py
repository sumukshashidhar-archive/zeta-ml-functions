from colorthief import ColorThief
import sys

color = ''


def dominant_color(image_path):
    color_thief = ColorThief(image_path)
    color = color_thief.get_color(quality=1)


if __name__ == "__main__":
    dominant_color(sys.argv[1])
