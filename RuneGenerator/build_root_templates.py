import os

# Assuming Rune class is defined in Rune.py and you are running from the same directory
from Rune import Rune

root_templates_path = "Public\\FFT_WizardTraditions_Runesmith\\RootTemplates\\"

# Create directory if it doesn't exist
if not os.path.exists(root_templates_path):
    os.makedirs(root_templates_path)

def generate_root_templates(Runes):
    xml_template = '''<?xml version="1.0" encoding="utf-8"?>
<save>
    <version major="4" minor="0" revision="9" build="309" />
    <region id="Templates">
        <node id="Templates">
            <children>
                <node id="GameObjects">
                    <attribute id="MapKey" type="FixedString" value="{uuid}" />
                    <attribute id="Name" type="LSString" value="Rune_{spell_name}" />
                    <attribute id="DisplayName" type="TranslatedString" handle="{name_handle}" version="1" />
                    <attribute id="Icon" type="FixedString" value="Icon_Rune_{spell_name}" />
                    <attribute id="LevelName" type="FixedString" value="" />
                    <attribute id="Type" type="FixedString" value="item" />
					<attribute id="ParentTemplateId" type="FixedString" value="4ffd5c4b-4c56-4f05-a228-a33754bb1806" />
					<attribute id="VisualTemplate" type="FixedString" value="916f78a4-779b-3e43-28eb-eefc26d9683d" />
					<attribute id="PhysicsTemplate" type="FixedString" value="94a7c400-b2df-c54c-1675-1937920b7714" />
					<attribute id="Stats" type="FixedString" value="OBJ_Scroll_{spell_name}" />
                    <children>
                        <node id="OnUsePeaceActions">
                            <children>
                                <node id="Action">
                                    <attribute id="ActionType" type="int32" value="12" />
                                    <children>
                                        <node id="Attributes">
                                            <attribute id="Animation" type="FixedString" value="" />
                                            <attribute id="Conditions" type="LSString" value="CanUseSpellScroll(&quot;{spell_id}&quot;)" />
                                            <attribute id="SkillID" type="FixedString" value="{spell_id}" />
                                            <attribute id="Consume" type="bool" value="True" />
                                            <attribute id="ClassId" type="guid" value="a865965f-501b-46e9-aa9e-4877c0e8094d" />
                                        </node>
                                    </children>
                                </node>
                                <node id="Action">
									<attribute id="ActionType" type="int32" value="33" />
									<children>
										<node id="Attributes">
											<attribute id="Animation" type="FixedString" value="" />
											<attribute id="Conditions" type="LSString" value="" />
											<attribute id="SpellId" type="FixedString" value="{spell_id}" />
											<attribute id="Consume" type="bool" value="True" />
										</node>
									</children>
								</node>
                            </children>
                        </node>
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>'''

    for school, rune_list in Runes.items():
        for rune in rune_list:
            file_name = f"rune_{rune.spell_name}.lsx"
            file_path = os.path.join(root_templates_path, file_name)

            # Clear file contents if file already exists
            if os.path.exists(file_path):
                open(file_path, 'w').close()

            # Populate the XML template and write to file
            with open(file_path, 'w') as f:
                populated_xml = xml_template.format(
                    uuid=rune.uuid,
                    spell_name=rune.spell_name,
                    name_handle=rune.name_handle,
                    spell_id=rune.spell_id
                )
                f.write(populated_xml)
