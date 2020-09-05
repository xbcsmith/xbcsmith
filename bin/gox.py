#!/usr/bin/env python

import argparse
import logging
import os
import pdb
import re
import shutil
import sys
import time
import traceback

logger = logging.getLogger(__name__)


def debug_except_hook(type, value, tb):
    print("T-Rex Hates {0}".format(type.__name__))
    print(str(type))
    traceback.print_exception(type, value, tb)
    pdb.post_mortem(tb)


docstring = "// {} {} {}\n"
docfunc = "// {} {} takes {} input and returns {}\n"

license_header = """// SPDX-FileCopyrightText: © {} {} {}
// SPDX-License-Identifier: {}

"""

__author__ = "Brett Smith"
__email__ = "<xbcsmith@gmail.com>"

def add_license(info):
    debug = info.get("debug", os.environ.get("GODOCX_DEBUG", False))
    level = logging.INFO
    if debug:
        sys.excepthook = debug_except_hook
        level = logging.DEBUG
    logging.basicConfig(stream=sys.stderr, level=level, format="%(asctime)s %(name)s:[%(levelname)s] %(message)s")
    year = time.strftime("%Y")
    author = info.get("author") or __author__
    email = info.get("email") or __email__
    license = info.get("license") or "Apache-2.0"
    paths = info.get("paths") or os.listdir()
    suffix = info.get("suffix") or ".new"
    replace = info.get("replace") or False
    gofiles = [x for x in paths if x.endswith(".go")]
    for gf in gofiles:
        lns = []
        if replace:
            logger.debug("backing up file %s to %s", gf, gf + ".bak")
            shutil.copy(gf, gf + ".bak")
        with open(gf, "r") as fh:
            lns = fh.readlines()
            test = [x for x in lns if "Copyright" in x or "SPDX" in x]
            logger.debug("TEST : {}".format(test))
            if len(test):
                logger.debug("File already has Copyright or License")
                continue
        with open(gf + suffix, "w") as new:
            lic = license_header.format(year, author, email, license)
            new.write(lic)
            for ln in lns:
                new.write(ln)
        if replace:
            logger.debug("Replacing file %s with %s", gf, gf + suffix)
            shutil.move(gf + suffix, gf)


def add_yaml(info):
    debug = info.get("debug", os.environ.get("GODOCX_DEBUG", False))
    level = logging.INFO
    if debug:
        sys.excepthook = debug_except_hook
        level = logging.DEBUG
    logging.basicConfig(stream=sys.stderr, level=level, format="%(asctime)s %(name)s:[%(levelname)s] %(message)s")
    paths = info.get("paths") or os.listdir()
    suffix = info.get("suffix") or ".new"
    replace = info.get("replace") or False
    gofiles = [x for x in paths if x.endswith(".go")]
    for gf in gofiles:
        lns = []
        if replace:
            logger.debug("backing up file %s to %s", gf, gf + ".bak")
            shutil.copy(gf, gf + ".bak")
        with open(gf, "r") as fh:
            lns = fh.readlines()
        with open(gf + suffix, "w") as new:
            for ln in lns:
                if "`json:" in ln and "yaml:" not in ln:
                    newln = ln.split("json:")[0]
                    matches = re.findall(r"json:\"(.*)\"", ln, re.MULTILINE)
                    if len(matches):
                        val = matches[-1]
                    newln += 'json:"{0}" yaml:"{0}"`\n'.format(val)
                    new.write(newln)
                else:
                    new.write(ln)
        if replace:
            logger.debug("Replacing file %s with %s", gf, gf + suffix)
            shutil.move(gf + suffix, gf)


def add_comments(info):
    debug = info.get("debug", os.environ.get("GODOCX_DEBUG", False))
    level = logging.INFO
    if debug:
        sys.excepthook = debug_except_hook
        level = logging.DEBUG
    logging.basicConfig(stream=sys.stderr, level=level, format="%(asctime)s %(name)s:[%(levelname)s] %(message)s")
    paths = info.get("paths", os.listdir())
    suffix = info.get("suffix") or ".new"
    replace = info.get("replace") or False
    gofiles = [x for x in paths if x.endswith(".go")]
    for gf in gofiles:
        lns = []
        if replace:
            logger.debug("backing up file %s to %s", gf, gf + ".bak")
            shutil.copy(gf, gf + ".bak")
        with open(gf, "r") as fh:
            lns = fh.readlines()
        with open(gf + suffix, "w") as new:
            for ln in lns:
                if ln.startswith("type "):
                    name = ln.split()[1]
                    ds = docstring.format(name, "struct for", name.lower())
                    new.write(ds)
                    new.write(ln)
                elif ln.startswith("func "):
                    length = len(ln.split("("))
                    name = ""
                    inp = ""
                    out = ""
                    if length == 4:
                        name = ln.split("(")[1].split()[-1].strip()
                        inp = ln.split("(")[2].strip()[:-1]
                        out = ln.split("(")[3].split(")")[0]
                    elif length == 3:
                        if ln.startswith("func ("):
                            name = ln.split("(")[1].split()[-1].strip()
                            inp = ln.split("(")[2].strip().split(")")[0].strip()
                            out = ln.split("(")[2].strip().split(")")[1].replace("{", "").strip()
                        else:
                            name = ln.split("(")[0].split()[-1].strip()
                            inp = ln.split("(")[1].strip()[:-1]
                            out = ln.split("(")[2].split(")")[0]
                    elif length == 2:
                        name = ln.split("(")[0].split()[-1].strip()
                        out = ln.split("(")[1].strip().replace(")", "").replace("{", "").strip()
                    else:
                        pass
                    if not len(inp):
                        inp = "no"
                    ds = docfunc.format(name, "func", inp, out)
                    logger.debug("Adding docstring : %s", ds)
                    new.write(ds)
                    new.write(ln)
                elif ln.startswith("var "):
                    name = ln.split()[1]
                    ds = docstring.format(name, "variable for", name.lower())
                    logger.debug("Adding docstring : %s", ds)
                    new.write(ds)
                    new.write(ln)
                else:
                    new.write(ln)
            if replace:
                logger.debug("Replacing file %s with %s", gf, gf + suffix)
                shutil.move(gf + suffix, gf)


def fix_comments(info):
    debug = info.get("debug", os.environ.get("GODOCX_DEBUG", False))
    level = logging.INFO
    if debug:
        sys.excepthook = debug_except_hook
        level = logging.DEBUG
    logging.basicConfig(stream=sys.stderr, level=level, format="%(asctime)s %(name)s:[%(levelname)s] %(message)s")
    paths = info.get("paths", os.listdir())
    suffix = info.get("suffix") or ".new"
    replace = info.get("replace") or False
    gofiles = [x for x in paths if x.endswith(".go")]
    for gf in gofiles:
        lns = []
        if replace:
            logger.debug("backing up file %s to %s", gf, gf + ".bak")
            shutil.copy(gf, gf + ".bak")
        with open(gf, "r") as fh:
            lns = fh.readlines()
        with open(gf + suffix, "w") as new:
            for ln in lns:
                if "//" in ln:
                    if ln[ln.index("//") + 2] != " " and ln[ln.index("//") -1] != ":":
                        ln = ln.replace("//", "// ")
                        ln = ln.replace(":// ", "://")
                new.write(ln)
            if replace:
                logger.debug("Replacing file %s with %s", gf, gf + suffix)
                shutil.move(gf + suffix, gf)


class CmdLine(object):
    def __init__(self):

        parser = argparse.ArgumentParser(
            description="Go Doc String Tool",
            usage="""gox <command> [<args>]

            gox commands are:
                do          add comments to the go file
                add         add yaml:"value" to the go file
                license     add license to the go file
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
        Read go files and add doc strings
        """
        parser = argparse.ArgumentParser(description="Read go files and add doc strings\n")
        parser.add_argument(
            "--replace",
            dest="replace",
            action="store_true",
            default=False,
            help="replace files with the new files old files stored as .bak",
        )
        parser.add_argument(
            "--suffix", dest="suffix", action="store", default=".new", help="suffix for the edited files"
        )
        parser.add_argument("--debug", dest="debug", action="store_true", default=False, help="Turn debug on")
        parser.add_argument("paths", nargs="+", action="store", default=None, help="path to the gofiles")
        args = parser.parse_args(sys.argv[2:])
        info = vars(args)
        return add_comments(info)

    def fix(self):
        """
        Read go files and add doc strings
        """
        parser = argparse.ArgumentParser(description="Read go files and fix comment strings\n")
        parser.add_argument(
            "--replace",
            dest="replace",
            action="store_true",
            default=False,
            help="replace files with the new files old files stored as .bak",
        )
        parser.add_argument(
            "--suffix", dest="suffix", action="store", default=".new", help="suffix for the edited files"
        )
        parser.add_argument("--debug", dest="debug", action="store_true", default=False, help="Turn debug on")
        parser.add_argument("paths", nargs="+", action="store", default=None, help="path to the gofiles")
        args = parser.parse_args(sys.argv[2:])
        info = vars(args)
        return fix_comments(info)

    def add(self):
        """
        Read go files and add yaml:<value> if json:<value> exists
        """
        parser = argparse.ArgumentParser(description="Read go files and add yaml:<value> if json:<value> exists\n")
        parser.add_argument(
            "--replace",
            dest="replace",
            action="store_true",
            default=False,
            help="replace files with the new files old files stored as .bak",
        )
        parser.add_argument(
            "--suffix", dest="suffix", action="store", default=".new", help="suffix for the edited files"
        )
        parser.add_argument("--debug", dest="debug", action="store_true", default=False, help="Turn debug on")
        parser.add_argument("paths", nargs="+", action="store", default=None, help="path to the gofiles")
        args = parser.parse_args(sys.argv[2:])
        info = vars(args)
        return add_yaml(info)

    def license(self):
        """
        Read go files and add copyright and license
        """
        parser = argparse.ArgumentParser(description="Read go files and add yaml:<value> if json:<value> exists\n")
        parser.add_argument("--author", dest="author", action="store", default=None, help="name of author")
        parser.add_argument("--email", dest="email", action="store", default=None, help="email of author")
        parser.add_argument("--license", dest="license", default=None, action="store", help="SPDX Identifier for the License")
        parser.add_argument(
            "--replace",
            dest="replace",
            action="store_true",
            default=False,
            help="replace files with the new files old files stored as .bak",
        )
        parser.add_argument(
            "--suffix", dest="suffix", action="store", default=".new", help="suffix for the edited files"
        )
        parser.add_argument("--debug", dest="debug", action="store_true", default=False, help="Turn debug on")
        parser.add_argument("paths", nargs="+", action="store", default=None, help="path to the gofiles")
        args = parser.parse_args(sys.argv[2:])
        info = vars(args)
        return add_license(info)


def main():
    CmdLine()


if __name__ == "__main__":
    sys.exit(CmdLine())
