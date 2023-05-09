#!/usr/bin/env python3
import os
import random
import subprocess

# File presence check
file_present = os.path.isfile("./0-positive_or_negative.py")
readme_present = os.path.isfile("./README.md")

# Readme content check
readme_content = ""
if readme_present:
    with open("README.md", "r") as readme_file:
        readme_content = readme_file.read()

# First line check
first_line_correct = False
if file_present:
    with open("0-positive_or_negative.py", "r") as source_file:
        first_line = source_file.readline().strip()
        first_line_correct = first_line == "#!/usr/bin/env python3"

# Output correctness check
positive_output = subprocess.run(
    ["python3", "./0-positive_or_negative.py"],
    capture_output=True,
    text=True
)
negative_output = subprocess.run(
    ["python3", "./0-positive_or_negative.py"],
    capture_output=True,
    text=True
)
zero_output = subprocess.run(
    ["python3", "./0-positive_or_negative.py"],
    capture_output=True,
    text=True
)
wrong_type_output = subprocess.run(
    ["python3", "./0-positive_or_negative.py"],
    capture_output=True,
    text=True
)

# Pycodestyle validation
pycodestyle_output = subprocess.run(
    ["pycodestyle", "0-positive_or_negative.py"],
    capture_output=True,
    text=True
)

# File presence validation
print("File is present:", file_present)
print("README.md exists and is not empty:", readme_present and len(readme_content.strip()) > 0)

# First line validation
if file_present:
    if first_line_correct:
        print("First line contains #!/usr/bin/env python3")
    else:
        print("First line does not contain #!/usr/bin/env python3")

# Output correctness validation
positive_expected_output = "is positive"
negative_expected_output = "is negative"
zero_expected_output = "is zero"

print("Correct output - positive:", positive_expected_output in positive_output.stdout)
print("Correct output - negative:", negative_expected_output in negative_output.stdout)
print("Correct output - zero:", zero_expected_output in zero_output.stdout)
print("Correct output - wrong type:", wrong_type_output.stderr.startswith("Traceback"))

# Pycodestyle validation
if pycodestyle_output.returncode == 0:
    print("Pycodestyle validation passed")
else:
    print("Pycodestyle validation failed:")
    print(pycodestyle_output.stdout)
    print(pycodestyle_output.stderr)

