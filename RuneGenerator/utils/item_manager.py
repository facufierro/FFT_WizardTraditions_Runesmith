import logging
from utils.file_manager import FileManager
from model.rune import Rune


class ItemManager:

    @staticmethod
    def generate_runes():
        spells_level_1 = FileManager.get_spell_list('D:\Projects\Mods\Baldurs Gate 3\FFT_WizardTraditions_Runesmith\RuneGenerator\SpellLists.lsx', '11f331b0-e8b7-473b-9d1f-19e8e4178d7d')
        runes = []
        for spell in spells_level_1:
            runes.append(Rune(spell))
        return runes

    @staticmethod
    def generate_objects():
        runes = ItemManager.generate_runes()
        object_file = "D:\Projects\Mods\Baldurs Gate 3\FFT_WizardTraditions_Runesmith\Public\FFT_WizardTraditions_Runesmith\Stats\Generated\Object.txt"

        for rune in runes:
            if rune == runes[0]:
                FileManager.write_file(object_file, rune.object_string(), 'w')
            FileManager.write_file(object_file, rune.object_string(), 'a')

    @staticmethod
    def generate_shouts():
        # add shouts to shouts.txt without overwriting existing shouts but overwriting existing runes
        runes = FileManager.load_object_from_json(Rune, 'D:\Projects\Mods\Baldurs Gate 3\FFT_WizardTraditions_Runesmith\RuneGenerator\runes.json')

    @staticmethod
    def generate_root_templates():
        pass

    @staticmethod
    def generate_icons():
        pass
