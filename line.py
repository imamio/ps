import sys

if len(sys.argv) <= 1:
    print("panic: got no arguments")
    exit(1)

content = sys.argv[1]
parts = content.split(",")

lines = [p.strip() + "\n" for p in parts if len(p.strip()) > 0]

sys.stdout.writelines(lines)

