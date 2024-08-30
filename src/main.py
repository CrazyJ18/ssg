import os, shutil


def copy_dir(src, dst):
    if os.path.exists(dst) == False:
        os.mkdir(dst)
    for entry in os.listdir(dst):
        entry_path = os.path.join(dst, entry)
        if os.path.isfile(entry_path):
            os.remove(entry_path)
        else:
            shutil.rmtree(entry_path)
    for entry in os.listdir(src):
        entry_path = os.path.join(src, entry)
        if os.path.isfile(entry_path):
            print(f"{entry_path} copied to {shutil.copy(entry_path, dst)}")
        else:
            copy_dir(entry_path, os.path.join(dst, entry))
    return

def main():
    copy_dir("static", "public")

main()