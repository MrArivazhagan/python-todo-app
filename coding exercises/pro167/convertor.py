def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


if __name__ == "__main__":
    print(convert(5, 12))
