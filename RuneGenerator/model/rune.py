from uuid import uuid4


class Rune:
    def __init__(self, spell_id, uuid=None, name_handle=None, description_handle=None, icon=None, icon_uv=None):
        self.uuid = uuid if uuid else str(uuid4())
        self.spell_id = spell_id
        self.spell_name = spell_id.split("_", 1)[1]
        self.name_handle = name_handle if name_handle else f'u{self.uuid.replace("-", "")}'
        self.description_handle = description_handle if description_handle else f'u{str(uuid4()).replace("-", "")}'
        self.icon = icon if icon else f'Icon_Rune_{self.spell_name}'
        self.icon_uv = icon_uv if icon_uv else {'u1': 0.0, 'u2': 1.0, 'v1': 0.0, 'v2': 1.0}

    def shout_string(self):
        return (
            f'new entry "Shout_CarveRune_{self.spell_name}"\n'
            'type "SpellData"\n'
            'data "SpellType" "Shout"\n'
            'using "Shout_CarveRune"\n'
            'data "SpellContainerID" "Shout_CarveRune"\n'
            f'data "SpellProperties" "SummonInInventory({self.uuid},Permanent,5,false,true,true,,,,)"\n'
            f'data "Icon" "{self.icon}"\n'
            f'data "DisplayName" "{self.name_handle};2"\n'
            f'data "Description" "{self.description_handle};2"\n'
            'data "SpellFlags" "UNUSED_D"\n')

    def object_string(self):
        return (
            f'new entry "Rune_{self.spell_name}"\n'
            'type "Object"\n'
            'using "_MagicScroll"\n'
            'data "RootTemplate" "496156bc-da32-48a6-bcb5-fd83ed533178"\n'
            'data "ValueLevel" "7"\n'
            'data "Rarity" "Rare"\n'
            'data "ObjectCategory" "MagicScroll_4;;MagicScroll_Protection_4"\n'
            'data "Priority" "1"\n')

    def icon_string(self):
        return (
            '<node id="IconUV">\n'
            f'<attribute id="MapKey" type="FixedString" value="Icon_Rune_{self.spell_name}" />\n'
            f'<attribute id="U1" type="float" value="{self.icon_uv["u1"]}" />\n'
            f'<attribute id="U2" type="float" value="{self.icon_uv["u2"]}" />\n'
            f'<attribute id="V1" type="float" value="{self.icon_uv["v1"]}" />\n'
            f'<attribute id="V2" type="float" value="{self.icon_uv["v2"]}" />\n'
            '</node>\n'
        )

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
