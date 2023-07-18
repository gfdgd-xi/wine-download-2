#!/usr/bin/env python3
import os
for i in os.listdir("."):
    if i[-3:] == ".7z":
        os.system(f"cp -rv '{i}' '{i}.html'")