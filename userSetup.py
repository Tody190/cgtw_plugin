# -*- coding: utf-8 -*-
# author:yangtao
# time: 2021/11/01
"""
替换 CGTW 原先添加工具架的方式
"""

import os
import sys


def add_menu_and_show():
    """
    添加菜单, 并显示插件窗口
    :return:
    """
    # 将工具添加到菜单
    MainMayaWindow = pm.language.melGlobals['gMainWindow']
    cgtw_mina_menu = pm.menu("cgtw_tools", label=u"CGTW", parent=MainMayaWindow, tearOff=True)
    pm.menuItem("cgtw_show",
                label=u"加载",
                command="from maya_plugin import*;win = show()",
                parent=cgtw_mina_menu)


def show_tools():
    # 显示工具
    try:
        from maya_plugin import *
        win = show()
    except:
        pass


if __name__ == "__main__":
    # 获取 CGTW 需要加载的环境
    CGTW_ROOT = os.environ.get("CGTW_SOFT_PATH")
    if CGTW_ROOT:
        import pymel.core as pm
        import maya.utils as mu
        
        CGTW_MAYA_PLUGIN = os.path.join(CGTW_ROOT, "bin\\base\\maya_plugin")  # cgtw maya 脚本根路径
        CGTW_BASE = os.path.join(CGTW_ROOT, "bin\\base")  # cgtw 脚本库
        CGTW_ICON = os.path.join(CGTW_BASE, "com_icon")  # cgtw 通用图标
        CGTW_COM_LIB = os.path.join(CGTW_BASE, "com_lib")  # 通用库

        CGTW_MAYA_OPEN_START = os.path.join(CGTW_MAYA_PLUGIN, "maya_open_start.mel")  # cgtw 在工具架上添加tool的脚本

        # 将路径添加到当前环境
        for p in [CGTW_MAYA_PLUGIN, CGTW_BASE, CGTW_ICON, CGTW_COM_LIB]:
            if p not in sys.path:
                sys.path.append(p)

        # 将参数添加到 sys.argv
        # cgtw 原先设计是使用
        # maya.exe -script maya_open_start.mel *
        # 我们虽然不使用这种方式, 但是我们需要在 sys.argv 添加对应的指令
        # 因为 CGTW maya 脚本使用这种方式获取他们需要的参数
        sys.argv.append("-script")
        sys.argv.append(CGTW_MAYA_OPEN_START)
        cgtw_database = os.environ.get("CGTW_DATABASE")
        if cgtw_database:
            sys.argv = []
            sys.argv.append(cgtw_database)
            sys.argv.append(os.environ.get("CGTW_MODULE"))
            sys.argv.append(os.environ.get("CGTW_ID"))

            # 加载菜单
            #mu.executeDeferred(add_menu_and_show)
            # 显示工具
            mu.executeDeferred(show_tools)
    else:
        print(u"No environment: CGTW_SOFT_PATH")