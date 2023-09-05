from build_icons_lsx import initialize_file, generate_icons
from build_root_templates import generate_root_templates  # Import the function
from model.rune import Rune  # Notice the dot before Rune


Runes = {
    "Abjuration": [
        Rune(spell_id="Projectile_Banishment"),
        Rune(spell_id="Target_DispelMagic"),
    ],
    # Add more Runes here
}

initialize_file()
generate_icons(Runes)
generate_root_templates(Runes)  # Call the function
