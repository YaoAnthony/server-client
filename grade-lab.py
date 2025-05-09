#!/usr/bin/env python3

import argparse

import ag.common.testing as testing


parser = argparse.ArgumentParser(description="Description of your program")
parser.add_argument(
    "-l", "--lab", help="The lab to grade (0, 1, 2, or 3)", required=True, type=int
)
args = vars(parser.parse_args())

print("================================================================")
if args["lab"] == 0:
    print("grading lab0")
    # import the file to load the tests
    import ag.ag0.ag0_runner as ag0_runner

    testing.run_tests()
elif args["lab"] == 1:
    print("grading lab1")
    import ag.ag1.ag1_runner as ag1_runner

    testing.run_tests()
elif args["lab"] == 2:
    print("grading lab2")
    import ag.ag2.ag2_runner as ag2_runner

    testing.run_tests()
else:
    print("invalid argument to --lab")
print("================================================================")
