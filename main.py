#!/usr/bin/env python3
import os
from parser import parse_arguments
from update import update

args = parse_arguments()
path = os.getcwd()

update(args, path)

cmd = f"mkdir {args.projName}"
os.system(cmd)

if "competitive-programming" in args.categoryName:
    os.system(
        f"cp /home/anandh/Documents/Projects/Python/mk-project/data/snippet.cpp test/solution1.cpp")
