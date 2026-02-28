import importlib
import sys

def main():
    q = int(sys.stdin.readline().strip())
    for _ in range(q):
        module_path, attribute = sys.stdin.readline().strip().split()
        try:
            module = importlib.import_module(module_path)
        except ModuleNotFoundError:
            print("MODULE_NOT_FOUND")
            continue

        if not hasattr(module, attribute):
            print("ATTRIBUTE_NOT_FOUND")
            continue

        attr = getattr(module, attribute)
        if callable(attr):
            print("CALLABLE")
        else:
            print("VALUE")

if __name__ == "__main__":
    main()