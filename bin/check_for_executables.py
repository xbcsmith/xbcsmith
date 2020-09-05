#!/usr/bin/env python3

"""Check that executable text files have a shebang."""
import argparse
import os
import pdb as debugger
import shlex
import subprocess
import sys
import traceback
from typing import Any, List, Optional, Sequence, Set

EXECUTABLE_VALUES = frozenset(("1", "3", "5", "7"))


def debug_except_hook(type, value, tb):
    print("Komatsu Hates %s" % type.__name__)
    print(str(type))
    traceback.print_exception(type, value, tb)
    debugger.post_mortem(tb)


sys.excepthook = debug_except_hook


class CalledProcessError(RuntimeError):
    # CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    def __init__(self, cmd, retcode, returncode, stdout, stderr):
        self.cmd = cmd
        self.retcode = retcode
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

    def msg(self):
        stderr = self.stderr
        return f"ERROR : {stderr}"


def added_files() -> Set[str]:
    cmd = ("git", "diff", "--staged", "--name-only", "--diff-filter=A")
    return set(cmd_output(*cmd).splitlines())


def cmd_output(*cmd: str, retcode: Optional[int] = 0, **kwargs: Any) -> str:
    kwargs.setdefault("stdout", subprocess.PIPE)
    kwargs.setdefault("stderr", subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


def zsplit(s: str) -> List[str]:
    s = s.strip("\0")
    if s:
        return s.split("\0")
    else:
        return []


def check_executables(paths: List[str]) -> int:
    ok = False
    try:
        ok = cmd_output("git", "rev-parse", "--is-inside-work-tree")
        if ok.startswith("true"): ok = True
    except CalledProcessError as err:
        print(err.msg())
    if ok:
        return _check_git_filemodes(paths)
    return _check_filemodes(paths)


def _check_git_filemodes(paths: Sequence[str]) -> int:
    outs = cmd_output("git", "ls-files", "-z", "--stage", "--", *paths)
    seen: Set[str] = set()
    for out in zsplit(outs):
        metadata, path = out.split("\t")
        tagmode = metadata.split(" ", 1)[0]
        is_executable = any(b in EXECUTABLE_VALUES for b in tagmode[-3:])
        has_shebang = _check_has_shebang(path)
        if is_executable and not has_shebang:
            _message(path)
            seen.add(path)
    _message_fix(seen)
    return int(bool(seen))


def _check_filemodes(paths: List[str]) -> int:
    print(f"checking filemodes...{paths}")
    seen: Set[str] = set()
    for path in paths:
        if not _check_has_shebang(path) and os.access(path, os.X_OK):
            _message(path)
            seen.add(path)
    _message_fix(seen)
    return int(bool(seen))


def _check_has_shebang(path: str) -> int:
    with open(path, "rb") as f:
        first_bytes = f.read(2)
    return first_bytes == b"#!"


def _message(path: str) -> None:
    print(
        f"{path}: marked executable but has no (or invalid) shebang!\n"
        f"  If it isn't supposed to be executable, try: "
        f"`chmod -x {shlex.quote(path)}`\n"
        f"  If it is supposed to be executable, double-check its shebang.",
        file=sys.stderr,
    )


def _message_fix(pathlist: List[str]) -> None:
    for path in pathlist:
        print(f"chmod -x {shlex.quote(path)}")


def _exclude(path: str) -> bool:
    excludes = [".git", ".tox", ".config", ".local"]
    for exclude in excludes:
        if exclude in path.split(os.sep):
            return True
    return False


def get_files(path: str):
    filepaths = []
    filenames = cmd_output("find", path, "-type", "f", "-print")
    print(f"find {path} -type f -print")
    for path in filenames.split("\n"):
        if path:
            if os.path.isfile(path):
                if not _exclude(path):
                    filepaths.append(path)
    return filepaths


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args(argv)
    filepaths = []
    paths = args.paths
    if len(paths) == 0:
        paths = [ os.getcwd() ]
    for path in paths:
        if path == ".":
            path = os.getcwd()
        filepaths.extend(get_files(path))
    return check_executables(filepaths)


if __name__ == "__main__":
    exit(main())
