# main.py
import os
import subprocess
import logging
from typing import Literal
from enum import Enum


class Path():
    ROOT_DIR = os.getcwd()
    DIVINE_FILE = os.path.join(ROOT_DIR, "export_tool", "divine.exe")
    MOD_DIR = "D:\Projects\Mods\Baldurs Gate 3\FFT_WizardTraditions_Runesmith\src"
    OUTPUT_FILE = "D:\Apps\Modding Tools\Baldurs Gate 3\BG3ModManager\FFT_WizardTraditions_Runesmith.pak"
    ENGLISH_LOCALIZATION_DIR = os.path.join(MOD_DIR, "Localization", "English", 'FFT_WizardTraditions_Runesmith')

    MERGED_DIR = os.path.join(MOD_DIR, "Public", "FFT_WizardTraditions_Runesmith", "Content", "UI", "[PAK]_UI")
    ROOT_TEMPLATES_DIR = os.path.join(MOD_DIR, "Public", "FFT_WizardTraditions_Runesmith", "RootTemplates")


class LSLib:
    @staticmethod
    def execute_command(command: Literal["create-package", "list-package", "extract-single-file", "extract-package", "extract-packages", "convert-model", "convert-models", "convert-resource", "convert-resources", "convert-loca"], source: str, destination: str):
        try:
            str = [
                Path.DIVINE_FILE,
                "-g",
                "bg3",
                "-a",
                command,
                "-c",
                "lz4",
                "--source",
                source,
                "--destination",
                destination,
                "--input-format",
                "lsx",
                "--output-format",
                "lsf",
                "-l",
                "info",
            ]
            subprocess.run(str, check=True)
        except Exception as e:
            logging.error(
                f"An error occurred while executing the lslib command. Reason: {e}")


def main():
    # print(Path.ENGLISH_LOCALIZATION_XML)
    LSLib.execute_command("convert-loca", Path.ENGLISH_LOCALIZATION_DIR+".xml", Path.ENGLISH_LOCALIZATION_DIR+".loca")
    LSLib.execute_command("convert-resources", Path.MERGED_DIR, Path.MERGED_DIR)
    LSLib.execute_command("convert-resources", Path.ROOT_TEMPLATES_DIR, Path.ROOT_TEMPLATES_DIR)
    LSLib.execute_command("create-package", Path.MOD_DIR, Path.OUTPUT_FILE)


if __name__ == "__main__":
    main()
