# -*- coding: utf-8 -*-
"""Paragate builtin task suite"""

from __future__ import print_function

import os, shutil

from microapp import App

class Init(App):
    """task initialization"""

    _name_ = "init"
    _version_ = "0.1.0"

    def __init__(self, parent):
        self.add_argument("path", nargs="*", help="path to be initialized")

        self.gitpath = shutil.which("git")

    def perform(self, args):

        if args.path:
            paths = [os.path.abspath(p["_"]) for p in args.path]

        else:
            paths = [os.getcwd()]

        for path in paths:
            if self.gitpath:
                import pdb; pdb.set_trace()
                self.run_command(args=["shell", "git", "init"], cwd=path)

            # TODO: what to do
            import pdb; pdb.set_trace()


suite = [Init]
