import os
import re
import sys
import argparse
heading_count = {"heading_count": 0, "subheading":
    {"sub1": 0, "sub2": 0, "sub3": 0}, "Content_Counter": 0}


def helper():
    """
    Description: This module is used to create a helper for end user that
    if he/she passed some wrong file then get a proper error message
    Return: Parser object
    """
    parse_obj = argparse.ArgumentParser("Description= Help and Support"
                                        " for data parsing")
    parse_obj.add_argument("-f", "--filename", nargs=1,
                           help="Please pass the correct filename", default=False)
    return parse_obj


def text_parser(file):
    """
    Description: This parser work with any text file and create a
    proper formatted file.
    Return None
    """
    single_dot_checker = False
    double_dot_checker = False
    triple_dot_checker = False
    with open("{}".format(file)) as fd:
        while True:
            count_star = 0
            count_dot = 0
            checker = True
            data_write = open("output", "a+")
            try:
                data = [next(fd) for i in range(1)][0]
            except StopIteration:
                break
            for space in data:
                if re.match(r"^\s*$", data):
                    checker = False
                elif space == ".":
                    count_dot += 1
                    checker = True
                elif space == "*":
                    count_star += 1
                    checker = True
                else:
                    checker = True
                    break
            data = data.strip("^*")
            data = data.strip("^.")
            if count_star == 1 and checker:
                heading_count["heading_count"] += 1
                data_write.write("{} {}".format(heading_count["heading_count"], data))
                heading_count["subheading"] = {"sub1": 0, "sub2": 0, "sub3": 0}
            elif count_star == 2 and checker:
                heading_count["subheading"]["sub1"] += 1
                data_write.write(("{}.{} {}".
                                  format(heading_count["heading_count"],
                                         heading_count["subheading"]["sub1"],
                                         data)))
            elif count_star == 3 and checker:
                heading_count["subheading"]["sub2"] += 1
                data_write.write(("{}.{}.{} {}".format(
                    heading_count["heading_count"],
                    heading_count["subheading"]["sub1"],
                    heading_count["subheading"]["sub2"], data)))
            elif count_star == 4 and checker:
                heading_count["subheading"]["sub2"] += 1
                data_write.write(("{}.{}.{} {}".format(
                    heading_count["heading_count"],
                    heading_count["subheading"]["sub1"],
                    heading_count["subheading"]["sub2"], data)))
            elif count_star == 5 and checker:
                heading_count["subheading"]["sub3"] += 1
                data_write.write(("{}.{}.{}.{} {}".format(
                    heading_count["heading_count"],
                    heading_count["subheading"]["sub1"],
                    heading_count["subheading"]["sub2"],
                    heading_count["subheading"]["sub3"], data)))
            elif count_star == 6 and checker:
                heading_count["subheading"]["sub4"] += 1
                data_write.write(("{}.{}.{}.{} {}".format(
                    heading_count["heading_count"],
                    heading_count["subheading"]["sub1"],
                    heading_count["subheading"]["sub2"],
                    heading_count["subheading"]["sub3"],
                    heading_count["subheading"]["sub4"], data)))
            elif count_star == 7 and checker:
                heading_count["subheading"]["sub2"] += 1
                data_write.write(("{}.{}.{}.{}.{} {}".format(
                    heading_count["subheading"]["sub1"],
                    heading_count["subheading"]["sub2"],
                    heading_count["subheading"]["sub3"],
                    heading_count["subheading"]["sub4"],
                    heading_count["subheading"]["sub5"], data)))
            elif count_star == 8 and checker:
                heading_count["subheading"]["sub2"] += 1
                data_write.write(("{}.{}.{}.{}.{}.{} {}".format(
                    heading_count["subheading"]["sub1"],
                    heading_count["subheading"]["sub2"],
                    heading_count["subheading"]["sub3"],
                    heading_count["subheading"]["sub4"],
                    heading_count["subheading"]["sub5"],
                    heading_count["subheading"]["sub6"], data)))
            if count_dot == 1 and heading_count["heading_count"]>0:
                if single_dot_checker:
                    data_write.write(" - {}".format(data))
                    single_dot_checker = False
                else:
                    data_write.write(" + {}".format(data))
                    single_dot_checker = True

            if count_dot == 2 and heading_count["heading_count"]>0:
                if double_dot_checker:
                    data_write.write("  + {}".format(data))
                    double_dot_checker = False
                else:
                    data_write.write("   - {}".format(data))
                    double_dot_checker = True

            if count_dot == 3 and heading_count["heading_count"]>0:
                if triple_dot_checker:
                    data_write.write("    + {}".format(data))
                    triple_dot_checker = False
                else:
                    data_write.write("    - {}".format(data))
                    triple_dot_checker = True
            data_write.close()


if __name__ == '__main__':
    data = sys.argv[1]
    parser = helper()
    parser_obj = parser.parse_args()
    if parser_obj.filename[0]:
        if os.path.isfile(parser_obj.filename[0]):
            text_parser(parser_obj.filename[0])
        else:
            print("Provided file does not Exist")

