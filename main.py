# main.py
import os
import subprocess
import logging
from typing import Literal


mod_name = folder_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))


class Paths():
    ROOT_DIR = os.getcwd()
    DIVINE_FILE = "D:\Apps\Modding Tools\Baldurs Gate 3\ExportTool\Tools\divine.exe"
    MOD_DIR = f"D:\Projects\Mods\Baldurs Gate 3\{mod_name}\src"
    OUTPUT_FILE = f"D:\Apps\Modding Tools\Baldurs Gate 3\BG3ModManager\{mod_name}.pak"
    ENGLISH_LOCALIZATION_DIR = os.path.join(MOD_DIR, "Localization", "English", f'{mod_name}')

    MERGED_DIR = os.path.join(MOD_DIR, "Public", f"{mod_name}", "Content", "UI", "[PAK]_UI")
    ROOT_TEMPLATES_DIR = os.path.join(MOD_DIR, "Public", f"{mod_name}", "RootTemplates")


class LSLib:
    @staticmethod
    def execute_command(command: Literal["create-package", "extract-package", "convert-resource", "convert-loca"],
                        source_path: str, destination_path: str, input_format: str = None, output_format: str = None, package_priority: int = None) -> None:
        try:
            if package_priority is None:
                package_priority = 0
            package_priority = str(package_priority)

            if input_format is None or output_format is None:
                command_string = [
                    f'{Paths.DIVINE_FILE}',
                    "-g",
                    "bg3",
                    "-a",
                    command,
                    "-c",
                    "lz4",
                    "--source",
                    source_path,
                    "--destination",
                    destination_path,
                    "--package-priority",
                    package_priority,
                    "-l",
                    "all",
                ]
            else:
                command_string = [
                    f'{Paths.DIVINE_FILE}',
                    "-g",
                    "bg3",
                    "-a",
                    command,
                    "-c",
                    "lz4",
                    "--source",
                    source_path,
                    "--destination",
                    destination_path,
                    "--input-format",
                    input_format,
                    "--output-format",
                    output_format,
                    "--package-priority",
                    package_priority,
                    "-l",
                    "all",
                ]
            # Log.debug(f"Executing lslib command: {command_string}")
            result = subprocess.run(command_string)
            if result.returncode == 0:
                return True
            else:
                return False
        except Exception as e:
            print(
                f"An error occurred while executing the lslib command. Reason: {e}")


def main():
    # print(Path.ENGLISH_LOCALIZATION_XML)
    LSLib.execute_command("convert-loca", Paths.ENGLISH_LOCALIZATION_DIR+".xml", Paths.ENGLISH_LOCALIZATION_DIR+".loca")
    LSLib.execute_command("convert-resources", Paths.MERGED_DIR, Paths.MERGED_DIR, input_format="lsx", output_format="lsf")
    LSLib.execute_command("convert-resources", Paths.ROOT_TEMPLATES_DIR, Paths.ROOT_TEMPLATES_DIR, input_format="lsx", output_format="lsf")
    LSLib.execute_command("create-package", Paths.MOD_DIR, Paths.OUTPUT_FILE, package_priority=30)


if __name__ == "__main__":
    main()
