import logging
from model.rune import Rune
from utils.file_manager import FileManager
from utils.paths import RUNES_JSON_DIR, SPELL_LISTS_DIR, SHOUTS_DIR


class ItemManager:

    @staticmethod
    def generate_runes():
        spells_level_1 = FileManager.get_spell_list(SPELL_LISTS_DIR, '11f331b0-e8b7-473b-9d1f-19e8e4178d7d')
        spells_level_2 = FileManager.get_spell_list(SPELL_LISTS_DIR, '80c6b070-c3a6-4864-84ca-e78626784eb4')

        runes = []
        for spell in spells_level_1:
            runes.append(Rune(spell))
        for spell in spells_level_2:
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
        # Load existing runes from JSON file
        runes = ItemManager.generate_runes()
        shouts_file = SHOUTS_DIR

        # Read existing content from shouts.txt
        try:
            with open(shouts_file, 'r') as f:
                existing_shouts = f.read()
        except FileNotFoundError:
            existing_shouts = ""

        # Split the existing content into sections based on comments
        sections = existing_shouts.split("//Runes")
        pre_runes_section = sections[0]  # Content before "//Runes"
        post_runes_section = sections[1] if len(sections) > 1 else ""  # Content after "//Runes"

        # Generate new rune shouts and collect spell_ids
        new_rune_shouts = []
        spell_ids = []
        for rune in runes:
            new_rune_shouts.append(rune.shout_string())
            spell_ids.append(rune.spell_id)

        # Concatenate spell_ids with semicolons
        concatenated_spell_ids = ";".join([f"Shout_CarveRune_{spell_id}" for spell_id in spell_ids])

        # Update the ContainerSpells line in pre_runes_section
        pre_runes_section = pre_runes_section.replace('data "ContainerSpells" "Shout_CarveRune_Banishment"', f'data "ContainerSpells" "{concatenated_spell_ids}"')

        # Combine everything
        updated_content = f"{pre_runes_section}//Runes\n{''.join(new_rune_shouts)}\n{post_runes_section}"

        # Write updated content back to file
        with open(shouts_file, 'w') as f:
            f.write(updated_content)

    @staticmethod
    def generate_root_templates():
        pass

    @staticmethod
    def generate_icons():
        pass
