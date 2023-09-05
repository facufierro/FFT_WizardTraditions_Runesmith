# main.py
from utils.file_manager import FileManager
from utils.item_manager import ItemManager
from utils.debug import setup_logger


def main():
    setup_logger()
    ItemManager.generate_objects()


if __name__ == "__main__":
    main()
