#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""

from LabMac.controller.controller import main as LabMac_main


def main(LabMac):
    if LabMac:
        LabMac_main()
    else:
        pass


if __name__ == "__main__":
    main(LabMac_main)
