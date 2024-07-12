from pathlib import Path
import shutil


def input_error(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print (str(e))
    return inner

@input_error
def copy_files(working_dir, destination_dir = "dist" )-> None:
    destination_dir = Path(destination_dir)
    working_dir = Path(working_dir)
    
    if working_dir.is_file() and working_dir.suffix:

        new_dir = destination_dir / working_dir.suffix.strip(".")
        new_dir.mkdir(parents=True, exist_ok=True)
        new_file_path = new_dir /  working_dir.name
        print(new_file_path)
        shutil.copy(working_dir, new_file_path)

    if working_dir.is_dir():
        for child in working_dir.iterdir():
            copy_files(child, destination_dir = "dist")


if __name__ == "__main__":
    working_dir = input("Enter working directory: ")
    if Path(working_dir).is_dir():
        destination_dir = input("Enter destination directory: ")
        copy_files(working_dir, destination_dir)
    else:
        print ( "Working directory does not exist")