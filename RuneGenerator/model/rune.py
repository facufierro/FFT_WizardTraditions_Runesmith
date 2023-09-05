from uuid import uuid4


class Rune:
    def __init__(self, spell_id, uuid_value=None, name_handle=None, description_handle=None, icon=None):
        self.uuid = uuid_value if uuid_value else str(uuid4())
        self.spell_id = spell_id
        self.spell_name = spell_id
        self.name_handle = name_handle if name_handle else f'u{self.uuid.replace("-", "")}'
        self.description_handle = description_handle if description_handle else f'u{str(uuid4()).replace("-", "")}'
        self.icon = icon if icon else f'Icon_Rune_{self.spell_name}'

    def shout_string(self):
        return (
            f'new entry "Shout_CarveRune_{self.spell_name}"\n'
            'type "SpellData"\n'
            'data "SpellType" "Shout"\n'
            'using "Shout_CarveRune"\n'
            'data "SpellContainerID" "Shout_CarveRune"\n'
            'data "SpellProperties" "SummonInInventory(496156bc-da32-48a6-bcb5-fd83ed533178,Permanent,5,false,true,true,,,,)"\n'
            'data "Icon" "Icon_Rune_Banishment"\n'
            'data "DisplayName" "h89f0b838g285fg4e72g8ce4gaf1e8ec5ac2c;2"\n'
            'data "Description" "h277c9a64g8300g419egbda7g62763b24ba72;2"\n'
            'data "SpellFlags" "UNUSED_D"\n')

    def object_string(self):
        return ("")

    def icon_string(self):
        return ("")

    def root_template_pack(self):
        return ("")

    def root_template_string(self):
        return (
            f'<?xml version="1.0" encoding="utf-8"?>'
            f'<save>'
            f'<version major="4" minor="0" revision="9" build="309" />'
            f'<region id="Templates">'
            f'<node id="Templates">'
            f'<children>'
            f'<node id="GameObjects">'
            f'<attribute id="MapKey" type="FixedString" value="{self.uuid}" />'
            f'<attribute id="Name" type="LSString" value="Rune_{self.spell_name}" />'
            f'<attribute id="DisplayName" type="TranslatedString" handle="{self.name_handle}" version="1" />'
            f'<attribute id="Icon" type="FixedString" value="Icon_Rune_{self.spell_name}" />'
            f'<attribute id="LevelName" type="FixedString" value="" />'
            f'<attribute id="Type" type="FixedString" value="item" />'
            f'<attribute id="ParentTemplateId" type="FixedString" value="4ffd5c4b-4c56-4f05-a228-a33754bb1806" />'
            f'<attribute id="VisualTemplate" type="FixedString" value="916f78a4-779b-3e43-28eb-eefc26d9683d" />'
            f'<attribute id="PhysicsTemplate" type="FixedString" value="94a7c400-b2df-c54c-1675-1937920b7714" />'
            f'<attribute id="Stats" type="FixedString" value="OBJ_Scroll_{self.spell_name}" />'
            f'<children>'
            f'<node id="OnUsePeaceActions">'
            f'<children>'
            f'<node id="Action">'
            f'<attribute id="ActionType" type="int32" value="12" />'
            f'<children>'
            f'<node id="Attributes">'
            f'<attribute id="Animation" type="FixedString" value="" />'
            f'<attribute id="Conditions" type="LSString" value="CanUseSpellScroll(&quot;{self.spell_id}&quot;)" />'
            f'<attribute id="SkillID" type="FixedString" value="{self.spell_id}" />'
            f'<attribute id="Consume" type="bool" value="True" />'
            f'<attribute id="ClassId" type="guid" value="a865965f-501b-46e9-aa9e-4877c0e8094d" />'
            f'</node>'
            f'</children>'
            f'</node>'
            f'<node id="Action">'
            f'<attribute id="ActionType" type="int32" value="33" />'
            f'<children>'
            f'<node id="Attributes">'
            f'<attribute id="Animation" type="FixedString" value="" />'
            f'<attribute id="Conditions" type="LSString" value="" />'
            f'<attribute id="SpellId" type="FixedString" value="{self.spell_id}" />'
            f'<attribute id="Consume" type="bool" value="True" />'
            f'</node>'
            f'</children>'
            f'</node>'
            f'</children>'
            f'</node>'
            f'</children>'
            f'</node>'
            f'</children>'
            f'</node>'
            f'</region>'
            f'</save>'
        )
