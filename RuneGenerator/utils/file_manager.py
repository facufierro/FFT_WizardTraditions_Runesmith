import os
import shutil
import logging
from lxml import etree
from typing import List, Optional


class FileManager:
    @staticmethod
    def clean_folder(folder_path):
        try:
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                        logging.debug(f'Successfully deleted {file_path}')
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        logging.debug(f'Successfully deleted directory {file_path}')
                except Exception as e:
                    logging.error(f'Failed to delete {file_path}. Reason: {e}')
        except Exception as e:
            logging.error(f'Failed to clean folder. Reason: {e}')

    @staticmethod
    def find_files(mod_folder_path, target_filenames: List[str]):
        logging.info(f"Searching for target files in {mod_folder_path}")
        found_files = {}

        try:
            for root, dirs, files in os.walk(mod_folder_path):
                for filename in files:
                    if filename in target_filenames:
                        found_files[filename] = os.path.join(root, filename)

            for target in target_filenames:
                logging.debug(f"Found {target} at {found_files.get(target, 'Not Found')}")

        except Exception as e:
            logging.error(f"An error occurred while searching for target files: {e}")

        return found_files

    @staticmethod
    def get_attribute(node, attr_id, default=None) -> Optional[str]:
        try:
            # Extract the value of the attribute specified by attr_id
            result = node.xpath(f"./attribute[@id='{attr_id}']/@value")
        except Exception as e:
            logging.error(f"Error in get_attribute: {e}")
            return default
        return result[0] if result else default

    @staticmethod
    def parse_lsx(file_path):
        if not os.path.exists(file_path):
            logging.error(f"File not found: {file_path}")
            return None
        try:
            # Initialize parser and parse the XML
            parser = etree.XMLParser(remove_blank_text=True)
            tree = etree.parse(file_path, parser)
            root = tree.getroot()
            # Log successful parsing
            logging.info(f"Successfully parsed {file_path}")
            return root
        except Exception as e:
            logging.error(f"Error in parse_lsx: {e}")
            return None

    @staticmethod
    def load_nodes(lsx_file_path, node_name, attribute_list, child_handler=None):
        try:
            root = FileManager.parse_lsx(lsx_file_path)
            if root is None:
                logging.error("Failed to parse LSX file")
                return []

            nodes_data = []
            for node in root.xpath(f".//node[@id='{node_name}']"):
                node_data = {attr: FileManager.get_attribute(node, attr) for attr in attribute_list}

                if child_handler:
                    child_handler(node, node_data)

                nodes_data.append(node_data)

            return nodes_data if nodes_data else []

        except Exception as e:
            logging.error(f"An error occurred in load_from_lsx: {e}")
            return []

    @staticmethod
    def get_spells_from_spell_list(mod_folder_path):
        spell_list_file = FileManager.find_files(mod_folder_path, ["SpellList.lsx"])
        spell_list = FileManager.load_nodes(spell_list_file, "SpellList", ["Spells", "UUID"])
        wizard_spell_list = []
        for spell in spell_list:
            if spell["UUID"] == "11f331b0-e8b7-473b-9d1f-19e8e4178d7d":
                wizard_spell_list.append({"level": 1, "spells": spell["Spells"].replace(";", "").split(",")})
            if spell["UUID"] == "80c6b070-c3a6-4864-84ca-e78626784eb4":
                wizard_spell_list.append({"level": 2, "spells": spell["Spells"].replace(";", "").split(",")})
            if spell["UUID"] == "22755771-ca11-49f4-b772-13d8b8fecd93":
                wizard_spell_list.append({"level": 3, "spells": spell["Spells"].replace(";", "").split(",")})
            if spell["UUID"] == "820b1220-0385-426d-ae15-458dc8a6f5c0":
                wizard_spell_list.append({"level": 4, "spells": spell["Spells"].replace(";", "").split(",")})
            if spell["UUID"] == "f781a25e-d288-43b4-bf5d-3d8d98846687":
                wizard_spell_list.append({"level": 5, "spells": spell["Spells"].replace(";", "").split(",")})
            if spell["UUID"] == "bc917f22-7f71-4a25-9a77-7d2f91a96a65":
                wizard_spell_list.append({"level": 6, "spells": spell["Spells"].replace(";", "").split(",")})
            if spell["UUID"] == "dff7917a-0abc-4671-b68f-c03e56212549":
                wizard_spell_list.append({"level": 7, "spells": spell["Spells"].replace(";", "").split(",")})
            if spell["UUID"] == "f27a2d0a-0d6c-4c01-98a5-60081abf4807":
                wizard_spell_list.append({"level": 8, "spells": spell["Spells"].replace(";", "").split(",")})
            if spell["UUID"] == "cb123d97-8809-4d71-a0cb-0ecb66177d15":
                wizard_spell_list.append({"level": 9, "spells": spell["Spells"].replace(";", "").split(",")})
        return wizard_spell_list

    @staticmethod
    def create_file(file_path):
        # Log the file path for debugging
        logging.debug(f"Trying to create file at {file_path}")

        # Create directories if they don't exist
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
                logging.info(f"Created directory {directory}")
            except Exception as e:
                logging.error(f"Failed to create directory {directory}: {e}")
                return False

        # Create file if it doesn't exist
        if not os.path.exists(file_path):
            try:
                open(file_path, 'w').close()
                logging.info(f"Created file {file_path}")
                return True
            except Exception as e:
                logging.error(f"Failed to create file {file_path}: {e}")
                return False
        else:
            logging.info(f"File {file_path} already exists")
            return True

    @staticmethod
    def write_file(file_path, content):
        try:
            with open(file_path, 'w') as f:
                f.write(content)
            logging.info(f"Wrote content to {file_path}")
            return True
        except Exception as e:
            logging.error(f"Failed to write to file {file_path}: {e}")
            return False
