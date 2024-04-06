import os

import web


class Parser:
    def __init__(self):
        self.mode = "normal"
        self.text = ""

    def go(self, pyfile):
        for line in open(pyfile):
            if self.mode == "in def":
                self.text += " " + line.strip()
                if line.strip().endswith(":"):
                    if self.definition(self.text):
                        self.text = ""
                        self.mode = "in func"
                    else:
                        self.text = ""
                        self.mode = "normal"

            elif self.mode == "in func":
                if '"""' in line:
                    self.text += line.strip().strip('"')
                    self.mode = "in doc"
                    if line.count('"""') == 2:
                        self.mode = "normal"
                        self.docstring(self.text)
                        self.text = ""
                else:
                    self.mode = "normal"
