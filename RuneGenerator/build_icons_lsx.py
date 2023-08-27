import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree

icons_runesmith_path = "..\\FFT_WizardTraditions_Runesmith\\Public\\FFT_WizardTraditions_Runesmith\\GUI\\Icons_Runesmith.lsx"

spells = {
    "Abjuration": ["Banishment"],
}

def initialize_file():
    root = Element("save")

    version = SubElement(root, "version")
    version.attrib["major"] = "4"
    version.attrib["minor"] = "0"
    version.attrib["revision"] = "0"
    version.attrib["build"] = "328"

    icon_region = SubElement(root, "region", id="IconUVList")
    icon_node = SubElement(icon_region, "node", id="root")
    icon_children = SubElement(icon_node, "children")

    texture_region = SubElement(root, "region", id="TextureAtlasInfo")
    texture_node = SubElement(texture_region, "node", id="root")
    texture_children = SubElement(texture_node, "children")

    # Additional TextureAtlas Information
    icon_size_node = SubElement(texture_children, "node", id="TextureAtlasIconSize")
    SubElement(icon_size_node, "attribute", id="Height", type="int32", value="64")
    SubElement(icon_size_node, "attribute", id="Width", type="int32", value="64")
    
    atlas_path_node = SubElement(texture_children, "node", id="TextureAtlasPath")
    SubElement(atlas_path_node, "attribute", id="Path", type="string", value="Assets/Textures/Icons/Icons_Runesmith.dds")
    SubElement(atlas_path_node, "attribute", id="UUID", type="FixedString", value="5a359cb4-ad61-4fa3-b8e6-1cf6191bf7f9")
    
    atlas_size_node = SubElement(texture_children, "node", id="TextureAtlasTextureSize")
    SubElement(atlas_size_node, "attribute", id="Height", type="int32", value="2048")
    SubElement(atlas_size_node, "attribute", id="Width", type="int32", value="2048")

    tree = ElementTree(root)
    tree.write(icons_runesmith_path)

def calculate_coordinates(index):
    icon_size = 64
    atlas_size = 2048
    u = (index * icon_size) / atlas_size
    v = 0
    delta = icon_size / atlas_size
    return u, u + delta, v, v + delta

def generate_icons(Runes):
    tree = ET.parse(icons_runesmith_path)
    root = tree.getroot()

    children_node = root.find(".//region[@id='IconUVList']/node[@id='root']/children")

    i = 0
    for school, rune_list in Runes.items():
        for rune in rune_list:
            u1, u2, v1, v2 = calculate_coordinates(i)
            
            new_node = SubElement(children_node, "node", id="IconUV")
            SubElement(new_node, "attribute", id="MapKey", type="FixedString", value=rune.icon)

            SubElement(new_node, "attribute", id="U1", type="float", value=str(u1))
            SubElement(new_node, "attribute", id="U2", type="float", value=str(u2))
            SubElement(new_node, "attribute", id="V1", type="float", value=str(v1))
            SubElement(new_node, "attribute", id="V2", type="float", value=str(v2))

            i += 1

    tree.write(icons_runesmith_path)

