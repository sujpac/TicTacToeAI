import sys
import engine

if __name__ == '__main__':
    p1_name = sys.argv[1]
    p2_name = sys.argv[2]

    engine.play(p1_name, p2_name)
