#!/usr/bin/env python3

import os
import sys

dirs = sys.argv[1:]
for dir in dirs:
    md = [os.path.join(dir, x) for x in os.listdir(dir)]
    xxx = dict(
        [
            (
                " ".join(
                    [
                        x.capitalize()
                        for x in os.path.basename(x).rsplit(".", 1)[0].split("_")
                    ]
                ),
                x,
            )
            for x in md
        ]
    )
    print("\n".join([f"*  [{x}]({y})" for x, y in xxx.items()]))
