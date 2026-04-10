import os
import shutil


def establish_project_dir():
    src_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(src_dir)


def prepare_dst_dir(dst_dir):
    project_dir = establish_project_dir()
    print(f"Starting preparation process of {dst_dir} directory...")
    dst_dir = os.path.join(project_dir, dst_dir)
    static_dir = os.path.join(project_dir, "static")
    if os.path.isdir(dst_dir):
        print(f"Deleting {dst_dir} directory...")
        shutil.rmtree(dst_dir)
    print(f"Copying static files to {dst_dir} directory...")
    copy_dir_contents(static_dir, dst_dir)
    print("Preparation has been completed.")


def copy_dir_contents(src_dir, dest_dir):
    if not os.path.isdir(src_dir):
        raise ValueError("not a dir")
    os.mkdir(dest_dir)
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        if os.path.isdir(item_path):
            copy_dir_contents(item_path, os.path.join(dest_dir, item))
            continue
        shutil.copy(item_path, dest_dir)
