# messy_app/utils/file_utils.py
def read_file(path):
    # Broad except + pass
    try:
        with open(path, "r") as f:
            return f.read()
    except:
        pass
    return ""

def write_file(path, content):
    try:
        with open(path, "w") as f:
            f.write(content)
    except:
        pass
