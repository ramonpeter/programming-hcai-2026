"""Run p1.py to p4.py, each on a fresh t.txt, and show what is left in the file."""
import subprocess
import sys


def reset():
    with open("t.txt", "w") as f:
        f.write("a\nb\n")


for name in ["p1.py", "p2.py", "p3.py", "p4.py"]:
    reset()
    result = subprocess.run([sys.executable, name], capture_output=True, text=True)
    with open("t.txt") as f:
        contents = f.read()
    error = result.stderr.strip().split("\n")[-1] if result.stderr else ""
    print(f"{name}  {contents!r}  {error}")

reset()
subprocess.run([sys.executable, "p1.py"])
with open("t.txt") as f:
    print(len(f.read()))          # 6
with open("t.txt") as f:
    print(f.readlines())          # ['a\n', 'b\n', 'c\n']
reset()
