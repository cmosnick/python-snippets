import arcpy


def main():
    argument = arcpy.GetParameterAsText(0)
    print argument


if __name__ == '__main__':
    main()
