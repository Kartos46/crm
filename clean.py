import os

for root, dirs, files in os.walk("."):
    if "migrations" in dirs:
        mig_path = os.path.join(root, "migrations")
        for file in os.listdir(mig_path):
            if file != "__init__.py" and (file.endswith(".py") or file.endswith(".pyc")):
                os.remove(os.path.join(mig_path, file))
                print(f"Deleted: {os.path.join(mig_path, file)}")
