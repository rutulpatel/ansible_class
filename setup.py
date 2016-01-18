import sys, getopt

print "echo starting the script"

def main(argv):
    try:
        for i in sys.argv:
            print i
    except getopt.GetoptError:
        print "error here"

if __name__ == "__main__":
    main(sys.argv[1:])
