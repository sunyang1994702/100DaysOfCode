
## accept argument from terminal

import argparse

def main(args):
    print(args)
    ## OUTPUT: Namespace(system='helloworld!')
    print(args.system)
    ## OUTPUT: helloworld!


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--system", help="System name to compute baselines")
    args = parser.parse_args()

    main(args)
    ## python demo1.py --system helloworld!