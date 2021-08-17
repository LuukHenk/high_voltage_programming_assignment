#!/usr/bin/env python3
"""
    Title:          Python programming test, main script
    Description:    Runs the analyses processing script that processes 'analyses' subsection of
                    .ams measurement files

    Author:         Luuk Perdaems
    Emails:         Luukperdaems@hotmail.com
    Websites:       https://github.com/LuukHenk
"""

### Import functions {{{

import sys
from lib import analyses_processing

### }}}



### Run main function {{{

analyses_processing.main()
sys.exit()

### }}}
