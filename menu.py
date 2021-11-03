# -*- condig: utf-8 -*-
import os
import sys

import nuke


CGTW_ROOT = os.environ.get("CGTW_SOFT_PATH")
if CGTW_ROOT:
    CGTW_NUKE_PLUGIN = os.path.join(CGTW_ROOT, "bin\\base\\nuke_plugin")
    CGTW_BASE = os.path.join(CGTW_ROOT, "bin\\base")
    CGTW_ICON = os.path.join(CGTW_BASE, "com_icon")
    CGTW_COM_LIB = os.path.join(CGTW_BASE, "com_lib")

    for p in [CGTW_NUKE_PLUGIN, CGTW_BASE, CGTW_ICON, CGTW_COM_LIB]:
        if p not in sys.path:
            sys.path.append(p)

    nuke.pluginAddPath(CGTW_NUKE_PLUGIN.replace("\\", "/"))

    cgtw_database = os.environ.get("CGTW_DATABASE")
    if cgtw_database:
        sys.argv = []
        sys.argv.append(os.path.join(CGTW_NUKE_PLUGIN, "nuke_open_start.py"))
        sys.argv.append(cgtw_database)
        sys.argv.append(os.environ.get("CGTW_MODULE"))
        sys.argv.append(os.environ.get("CGTW_ID"))

        ##############################################################

        G_NukePlugin_Path = os.path.dirname( sys.argv[0] )
        sys.path.append( G_NukePlugin_Path )
        #20210722
        try:
            from PySide2.QtCore import *
        except:
            from PySide.QtCore import *
        os.environ['QTWEBENGINEPROCESS_PATH'] = ''
        appPath = QCoreApplication.applicationFilePath()
        os.environ['LD_LIBRARY_PATH'] = os.path.dirname(appPath)
        #20210722
        G_Base_Path = os.path.dirname( os.path.dirname( sys.argv[0] ) )

        ################################################################

        from nuke_plugin import *

        def show_cgtw_web():
            t_panel = Nuke_Panel()
            nuke.removeOnUserCreate(show_cgtw_web)

        nuke.addOnUserCreate(show_cgtw_web)