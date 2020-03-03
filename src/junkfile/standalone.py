#!/usr/bin/env python3

import argparse
from junkfile import main


"""standalone execute junkfile

Usage:
    python standalone.py --path=/home/ivan/Documents/test --copy=True

    or

    ./standalone.py --path=/home/ivan/Documents/test --copy=True

"""

def str2bool(v):
    if isinstance(v, bool):
       return v
       
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True

    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False

    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ and "__main__":

    parser = argparse.ArgumentParser(description="=== junk files organizer ===")
    parser.add_argument("--path", help='path to organize. E.g.: /Home/Jhon/docs',  type=str)
    parser.add_argument("--copy", help='True if would like make a directory copy',  
                        type=str2bool, default=True)

    # default function
    parser.set_defaults(func=main.run) 

    # parse arguments
    args = parser.parse_args()

    # calls function 
    try:
        args.func(args.path, args.copy)
    except Exception as e:
        print(f"[Junkfile] - ERROR: {e}")


