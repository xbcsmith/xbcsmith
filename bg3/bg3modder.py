#!/usr/bin/env python3

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime

from lxml import etree

logger = logging.getLogger(__name__)


def debug_except_hook(type, value, tb):
    print("Converter Error {0}".format(type.__name__))
    print(str(type))
    import pdb
    import traceback

    traceback.print_exception(type, value, tb)
    pdb.post_mortem(tb)


def get_info(path, debug=False):
    with open(path, "r") as stream:
        info_data = json.loads(stream.read())

    mods_info = info_data.get("Mods") or info_data.get("mods")
    mod_info = mods_info[0]
    mod_name = mod_info.get("Name") or mod_info.get("modName")
    mod_uuid = mod_info.get("UUID") or mod_info.get("uuid")
    mod_version = mod_info.get("Version") or mod_info.get("version")
    mod_folder = mod_info.get("Folder") or mod_info.get("folderName")

    if mod_version is None:
        dt = datetime.now()
        created_date = mod_info.get("Created") or mod_info.get("created")
        if created_date is not None:
            try:
                dt = datetime.fromisoformat(created_date)
            except ValueError as err:
                print(err)
        ts = str(dt.timestamp()).replace(".", "")
        mod_version = f"36{ts}"
    if debug:
        logger.debug("Printing ModOrder section and Mods section for mod")
        out = f"""
                <node id="Module">
                  <attribute id="UUID" value="{mod_uuid}" type="FixedString" />
                </node>

                <node id="ModuleShortDesc">
                  <attribute id="Folder" value="{mod_folder}" type="LSWString" />
                  <attribute id="MD5" value="" type="LSString" />
                  <attribute id="Name" value="{mod_name}" type="FixedString" />
                  <attribute id="UUID" value="{mod_uuid}" type="FixedString" />
                  <attribute id="Version" value="{mod_version}" type="int64" />
                </node>
      """

        print(out)
    return mod_name, mod_uuid, mod_version, mod_folder


def create_mod_order_node(mod_uuid):
    mod_order_node = etree.Element("node", id="Module")
    attribute = etree.Element("attribute", id="UUID", value=mod_uuid, type="FixedString")
    mod_order_node.insert(1, attribute)
    return mod_order_node


def create_mods_node(mod_name, mod_uuid, mod_version, mod_folder):
    mods_node = etree.Element("node", id="ModuleShortDesc")
    attr_fldr = etree.Element("attribute", id="Folder", value=mod_folder, type="LSWString")
    attr_md5 = etree.Element("attribute", id="MD5", value="", type="LSWString")
    attr_name = etree.Element("attribute", id="Name", value=mod_name, type="FixedString")
    attr_uuid = etree.Element("attribute", id="UUID", value=mod_uuid, type="FixedString")
    attr_ver = etree.Element("attribute", id="Version", value=mod_version, type="int64")
    mods_node.insert(1, attr_fldr)
    mods_node.insert(2, attr_md5)
    mods_node.insert(3, attr_name)
    mods_node.insert(4, attr_uuid)
    mods_node.insert(5, attr_ver)
    return mods_node


def _update_modsettings(tree, mod_name, mod_uuid, mod_version, mod_folder):
    mod_order = tree.find(""".//node[@id="ModOrder"]""")
    if mod_order.find(f""".//attribute[@value="{mod_uuid}"]""") is not None:
        print(f"mod : {mod_name} uuid: {mod_uuid} already exists in ModOrder section")
        sys.exit(1)
    mods = tree.find(""".//node[@id="Mods"]""")
    if mods.find(f""".//attribute[@value="{mod_uuid}"]""") is not None:
        print(f"mod : {mod_name} uuid: {mod_uuid} already exists in Mods but is not in the ModOrder section")
        sys.exit(1)
    mod_order_children = mod_order.find(""".//children""")
    if mod_order_children is None:
        child = etree.Element("children")
        mod_order.insert(1, child)
        mod_order_children = mod_order.find(""".//children""")
    mod_order_node = create_mod_order_node(mod_uuid)
    mod_order_children.append(mod_order_node)
    mods_children = mods.find(""".//children""")
    mods_node = create_mods_node(mod_name, mod_uuid, mod_version, mod_folder)
    mods_children.append(mods_node)
    contents = etree.tostring(tree, encoding="unicode", pretty_print=True)
    print(contents)
    return tree


def write_modsettings(tree, path):
    tree.write(f"{path}.xml", xml_declaration=True, encoding="UTF-8", pretty_print=True)
    import pdb

    pdb.set_trace()


def update_modsettings(info):
    debug = info.get("debug", os.environ.get("BG3MODDER_DEBUG", False))
    level = logging.INFO
    if debug:
        sys.excepthook = debug_except_hook
        level = logging.DEBUG
    logging.basicConfig(
        stream=sys.stderr,
        level=level,
        format="%(asctime)s %(name)s:[%(levelname)s] %(message)s",
    )
    modsettngs_file = info.get("modsettings_file")
    if modsettngs_file is None:
        logger.error("path to the modsettings.lsx file is required")
        return 1
    prefix = os.path.splitext(modsettngs_file)[0]
    ext = os.path.splitext(modsettngs_file)[-1]
    ts = time.time()
    filename = f"{prefix}.{ts}{ext}"
    paths = info.get("paths", [])
    if len(paths) < 1:
        logger.error("path to at least one info.json file is required")
        return 1
    tree = etree.parse(modsettngs_file)
    for path in paths:
        mod_name, mod_uuid, mod_version, mod_folder = get_info(path)
        tree = _update_modsettings(tree, mod_name, mod_uuid, mod_version, mod_folder)
    write_modsettings(tree, filename)
    return 0


def add_modsettings(info):
    debug = info.get("debug", os.environ.get("BG3MODDER_DEBUG", False))
    level = logging.INFO
    if debug:
        sys.excepthook = debug_except_hook
        level = logging.DEBUG
    logging.basicConfig(
        stream=sys.stderr,
        level=level,
        format="%(asctime)s %(name)s:[%(levelname)s] %(message)s",
    )
    logger.error("not implemented")
    return 1


class CmdLine(object):
    def __init__(self):

        parser = argparse.ArgumentParser(
            description="BG3 Mod Tool",
            usage="""bg3modder <command> [<args>]

            bg3modder commands are:
                do          read info.json files and add the mods to the modsettings.lsx
                add         add a mod that does not have an info.json
            """,
        )

        parser.add_argument("command", help="Subcommand to run")
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            logger.error("Unrecognized command")
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def do(self):
        """
        Read info.json files and add to the modsettings.lsx
        """
        parser = argparse.ArgumentParser(description="Read info.json files and add to the modsettings.lsx\n")
        parser.add_argument(
            "--modsettings-file",
            dest="modsettings_file",
            action="store",
            default=None,
            help="Path to the modsettings.lsx file",
        )
        parser.add_argument(
            "--debug",
            dest="debug",
            action="store_true",
            default=False,
            help="Turn debug on",
        )
        parser.add_argument("paths", nargs="+", action="store", default=None, help="path to the info.json")
        args = parser.parse_args(sys.argv[2:])
        info = vars(args)
        return update_modsettings(info)

    def add(self):
        """
        Read info.json files and add to the modsettings.lsx
        """
        parser = argparse.ArgumentParser(description="Add the info to the modsettings.lsx\n")
        parser.add_argument(
            "--modsettings-file",
            dest="modsettings_file",
            action="store",
            default=None,
            help="Path to the modsettings.lsx file",
        )
        parser.add_argument(
            "--name",
            dest="mod_name",
            action="store",
            default=None,
            help="Name of the mod",
        )
        parser.add_argument(
            "--uuid",
            dest="mod_uuid",
            action="store",
            default=None,
            help="UUID of the mod",
        )
        parser.add_argument(
            "--version",
            dest="mod_version",
            action="store",
            default=None,
            help="Version of the mod (not required)",
        )
        parser.add_argument(
            "--folder",
            dest="mod_folder",
            action="store",
            default=None,
            help="Folder of the mod (usually the matches the name of the mod)",
        )
        parser.add_argument(
            "--debug",
            dest="debug",
            action="store_true",
            default=False,
            help="Turn debug on",
        )
        args = parser.parse_args(sys.argv[2:])
        info = vars(args)
        return add_modsettings(info)


def main():
    CmdLine()


if __name__ == "__main__":
    sys.exit(main())
