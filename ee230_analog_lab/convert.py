# convert 230 labwork for report

def convert(string, filename):

    def include_line(line):
        if not line.strip():
            return False
        line = line.strip()
        if line.startswith("**"):
            # ** comments to be included
            return True
        if line.startswith("*"):
            return False
        return True

    assert string.startswith("19D070052 Sheel Shah"), print(
        "%s's heading does not include roll/name" % filename
    )
    with open("report_related/"+filename, "w") as f:
        for line in string.strip().split("\n"):
            if include_line(line):
                f.write(line + "\n")

if __name__ == '__main__':
    labnum = input("Enter lab prefix: ")
    part = 'a'
    while True:
        try:
            filename = "solution_" + labnum + part + ".cir"
            with open(filename) as f:
                convert(f.read(), filename)
        except:
            break
        part = chr(ord(part)+1)