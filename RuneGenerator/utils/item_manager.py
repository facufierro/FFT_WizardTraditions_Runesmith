import logging
from utils.file_manager import FileManager
from model.rune import Rune


class ItemManager:

    @staticmethod
    def generate_runes():
        spells_level_1 = FileManager.get_spell_list('D:\Projects\Mods\Baldurs Gate 3\FFT_WizardTraditions_Runesmith\RuneGenerator\SpellLists.lsx', '11f331b0-e8b7-473b-9d1f-19e8e4178d7d')
        # logging.info(f"Spells level 1: {spells_level_1[0]}")
        runes = []
        for spell in spells_level_1:
            runes.append(Rune(spell))

    @staticmethod
    def generate_objects():
        ItemManager.generate_runes()
        object_file = "D:\Projects\Mods\Baldurs Gate 3\FFT_WizardTraditions_Runesmith\Public\FFT_WizardTraditions_Runesmith\Stats\Generated\Object.txt"
        logging.info(f"Generating objects into {object_file}")
        FileManager.write_file(object_file, "Hello world")

    @staticmethod
    def generate_shouts():
        pass

    @staticmethod
    def generate_root_templates():
        pass

    @staticmethod
    def generate_icons():
        pass
