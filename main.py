#!/usr/bin/env python3
import os
from parser import parse_arguments
from update import update

args = parse_arguments()
path = os.getcwd()

update(args, path)

cmd = f'mkdir {args.projName}'
os.system(cmd)
