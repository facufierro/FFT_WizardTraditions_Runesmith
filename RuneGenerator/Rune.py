from uuid import uuid4

class Rune:
    def __init__(self, uuid_value=None, spell_id="", name_handle=None, description_handle=None, icon=None):
        self.uuid = uuid_value if uuid_value else str(uuid4())
        self.spell_id = spell_id
        self.spell_name = spell_id.split('_')[1] if '_' in spell_id else ""
        self.name_handle = name_handle if name_handle else f'u{self.uuid.replace("-", "")}'
        self.description_handle = description_handle if description_handle else f'u{str(uuid4()).replace("-", "")}'
        self.icon = icon if icon else f'Icon_Rune_{self.spell_name}'
