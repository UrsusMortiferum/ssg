import os
import shutil


def establish_project_dir():
    src_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(src_dir)


def prepare_public_dir():
    project_dir = establish_project_dir()
    print("Starting preparation process of public directory...")
    public_dir = os.path.join(project_dir, "public")
    static_dir = os.path.join(project_dir, "static")
    if os.path.isdir(public_dir):
        print("Deleting public directory...")
        print("Standby...")
        print("Encountered an issue...")
        shutil.rmtree(public_dir)
        print("I'm joking, it's done.")
    print("Copying static files to public directory...")
    copy_dir_contents(static_dir, public_dir)
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
