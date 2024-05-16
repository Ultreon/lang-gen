from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.client.gui.screens.settings.VideoSettingsUI as _VideoSettingsUI
_VideoSettingsUI = _VideoSettingsUI
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client.gui.screens import tabs
except ImportError:
    tabs = _import_once("pyquantum.client.gui.screens.tabs")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VideoSettingsUI():
    """dev.ultreon.quantum.client.gui.screens.settings.VideoSettingsUI"""
 
    @staticmethod
    def _wrap(java_value: _VideoSettingsUI) -> 'VideoSettingsUI':
        return VideoSettingsUI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VideoSettingsUI):
        """
        Dynamic initializer for VideoSettingsUI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VideoSettingsUI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VideoSettingsUI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def build(self, arg0: 'TabBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.settings.VideoSettingsUI.build(dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder)"""
        super(_VideoSettingsUI, self).build(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.settings.VideoSettingsUI()"""
        val = _VideoSettingsUI()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.settings.VideoSettingsUI()"""
        val = _VideoSettingsUI()
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.settings.VideoSettingsUI
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.client.gui.screens.settings.VideoSettingsUI as _VideoSettingsUI
_VideoSettingsUI = _VideoSettingsUI
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client.gui.screens import tabs
except ImportError:
    tabs = _import_once("pyquantum.client.gui.screens.tabs")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VideoSettingsUI():
    """dev.ultreon.quantum.client.gui.screens.settings.VideoSettingsUI"""
 
    @staticmethod
    def _wrap(java_value: _VideoSettingsUI) -> 'VideoSettingsUI':
        return VideoSettingsUI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VideoSettingsUI):
        """
        Dynamic initializer for VideoSettingsUI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VideoSettingsUI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VideoSettingsUI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def build(self, arg0: 'TabBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.settings.VideoSettingsUI.build(dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder)"""
        super(_VideoSettingsUI, self).build(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.settings.VideoSettingsUI()"""
        val = _VideoSettingsUI()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.settings.VideoSettingsUI()"""
        val = _VideoSettingsUI()
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.settings.VideoSettingsUI 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.settings.AccessibilitySettingsUI
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client.gui.screens import tabs
except ImportError:
    tabs = _import_once("pyquantum.client.gui.screens.tabs")

import dev.ultreon.quantum.client.gui.screens.settings.AccessibilitySettingsUI as _AccessibilitySettingsUI
_AccessibilitySettingsUI = _AccessibilitySettingsUI
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AccessibilitySettingsUI():
    """dev.ultreon.quantum.client.gui.screens.settings.AccessibilitySettingsUI"""
 
    @staticmethod
    def _wrap(java_value: _AccessibilitySettingsUI) -> 'AccessibilitySettingsUI':
        return AccessibilitySettingsUI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AccessibilitySettingsUI):
        """
        Dynamic initializer for AccessibilitySettingsUI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AccessibilitySettingsUI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AccessibilitySettingsUI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.settings.AccessibilitySettingsUI()"""
        val = _AccessibilitySettingsUI()
        self.__wrapper = val

    @overload
    def build(self, arg0: 'TabBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.settings.AccessibilitySettingsUI.build(dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder)"""
        super(_AccessibilitySettingsUI, self).build(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.settings.AccessibilitySettingsUI()"""
        val = _AccessibilitySettingsUI()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.settings.PrivacySettingsUI
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client.gui.screens import tabs
except ImportError:
    tabs = _import_once("pyquantum.client.gui.screens.tabs")

import dev.ultreon.quantum.client.gui.screens.settings.PrivacySettingsUI as _PrivacySettingsUI
_PrivacySettingsUI = _PrivacySettingsUI
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PrivacySettingsUI():
    """dev.ultreon.quantum.client.gui.screens.settings.PrivacySettingsUI"""
 
    @staticmethod
    def _wrap(java_value: _PrivacySettingsUI) -> 'PrivacySettingsUI':
        return PrivacySettingsUI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PrivacySettingsUI):
        """
        Dynamic initializer for PrivacySettingsUI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PrivacySettingsUI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PrivacySettingsUI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def build(self, arg0: 'TabBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.settings.PrivacySettingsUI.build(dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder)"""
        super(_PrivacySettingsUI, self).build(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.settings.PrivacySettingsUI()"""
        val = _PrivacySettingsUI()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.settings.PrivacySettingsUI()"""
        val = _PrivacySettingsUI()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.settings.SettingsScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Double as _double
import java.lang.Character as _char
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.UIContainer as _UIContainer
_UIContainer = _UIContainer
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI as _TabbedUI
_TabbedUI = _TabbedUI
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.gui.widget.layout.Layout as _Layout
_Layout = _Layout
import dev.ultreon.quantum.client.gui.Screen as _Screen
_Screen = _Screen
try:
    from pyquantum import component
except ImportError:
    component = _import_once("pyquantum.component")

import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.widget.Tab as _Tab
_Tab = _Tab
from builtins import bool
import dev.ultreon.quantum.client.gui.screens.settings.SettingsScreen as _SettingsScreen
_SettingsScreen = _SettingsScreen
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = _import_once("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.client.gui.Dialog as _Dialog
_Dialog = _Dialog
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum.client.gui.screens import tabs
except ImportError:
    tabs = _import_once("pyquantum.client.gui.screens.tabs")

import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.widget.Widget as _Widget
_Widget = _Widget
import dev.ultreon.quantum.client.gui.Position as _Position
_Position = _Position
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class SettingsScreen():
    """dev.ultreon.quantum.client.gui.screens.settings.SettingsScreen"""
 
    @staticmethod
    def _wrap(java_value: _SettingsScreen) -> 'SettingsScreen':
        return SettingsScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SettingsScreen):
        """
        Dynamic initializer for SettingsScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SettingsScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SettingsScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(_gui.Screen, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getContentHeight()"""
        return int._wrap(super(tabs.TabbedUI, self).getContentHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseWheel(int,int,double)"""
        return bool._wrap(super(_tabs.TabbedUI, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def setSelected(self, arg0: str):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setSelected(java.lang.String)"""
        super(_tabs.TabbedUI, self).setSelected(arg0)

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @override
    @overload
    def getTab(self) -> 'widget.Tab':
        """public final dev.ultreon.quantum.client.gui.widget.Tab dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getTab()"""
        return 'widget.Tab'._wrap(super(tabs.TabbedUI, self).getTab())

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'._wrap(super(gui.Screen, self).getTitle())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_widget.Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_widget.Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSelected(self, arg0: int):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setSelected(int)"""
        super(_tabs.TabbedUI, self).setSelected(_int.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.settings.SettingsScreen()"""
        val = _SettingsScreen()
        self.__wrapper = val

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_widget.Widget, self).setPos(arg0)

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'._wrap(super(_widget.UIContainer, self).getWidgetsAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(widget.Widget, self).getX())

    @overload
    def title(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).title(arg0))

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getContentWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getContentWidth()"""
        return int._wrap(super(tabs.TabbedUI, self).getContentWidth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.revalidate()"""
        super(tabs.TabbedUI, self).revalidate()

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_widget.Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(widget.Widget, self).isFocused())

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_widget.Widget, self).onRevalidate(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(widget.Widget, self).isEnabled())

    @override
    @overload
    def getDialog(self) -> 'gui.Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'gui.Dialog'._wrap(super(gui.Screen, self).getDialog())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_widget.Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(_gui.Screen, self).closeDialog(arg0)

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseRelease(int,int,int)"""
        return bool._wrap(super(_tabs.TabbedUI, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseMove(int,int)"""
        super(_tabs.TabbedUI, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'._wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str._wrap(super(gui.Screen, self).getRawTitle())

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool._wrap(super(_gui.Screen, self).onClose(arg0))

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_widget.UIContainer, self).renderChild(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_widget.Widget, self).setSize(arg0)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isBottomSelected(self) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.isBottomSelected()"""
        return bool._wrap(super(tabs.TabbedUI, self).isBottomSelected())

    @override
    @overload
    def setSelected(self, arg0: 'TextObject'):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setSelected(dev.ultreon.quantum.text.TextObject)"""
        super(_tabs.TabbedUI, self).setSelected(arg0)

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'._wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str._wrap(super(gui.Screen, self).getName())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool._wrap(_Widget.isPosWithin(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @override
    @overload
    def getTabX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getTabX()"""
        return int._wrap(super(tabs.TabbedUI, self).getTabX())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.settings.SettingsScreen()"""
        val = _SettingsScreen()
        self.__wrapper = val

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_widget.Widget, self).height(_int.valueOf(arg0))

    @override
    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool._wrap(super(gui.Screen, self).back())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_widget.Widget, self).setEnabled(_boolean.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(widget.Widget, self).isClickable())

    @override
    @overload
    def getContentX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getContentX()"""
        return int._wrap(super(tabs.TabbedUI, self).getContentX())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(widget.Widget, self).getWidth())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_widget.Widget, self).setBounds(arg0)

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_widget.Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canCloseWithEsc()"""
        return bool._wrap(super(gui.Screen, self).canCloseWithEsc())

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(widget.Widget, self).isHovered())

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(_Screen).parentScreen(value)

    @override
    @overload
    def setTabs(self, arg0: 'List'):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setTabs(java.util.List<dev.ultreon.quantum.client.gui.widget.Tab>)"""
        super(_tabs.TabbedUI, self).setTabs(arg0)

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'._wrap(super(gui.Screen, self).path())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_widget.Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def setSelected(self, arg0: 'Tab'):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setSelected(dev.ultreon.quantum.client.gui.widget.Tab)"""
        super(_tabs.TabbedUI, self).setSelected(arg0)

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_widget.Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(_widget.UIContainer, self).setLayout(arg0)

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(_Screen).directHovered(value)

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(widget.Widget, self).getPreferredHeight())

    @override
    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(_gui.Screen, self).init(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_widget.Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_tabs.TabbedUI, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(_gui.Screen, self).showDialog(arg0)

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mousePress(int,int,int)"""
        return bool._wrap(super(_tabs.TabbedUI, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'._wrap(super(_widget.UIContainer, self).getWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @property
    def focused(self, value: 'widget.Widget'):
        super(_Screen).focused(value)

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool._wrap(super(gui.Screen, self).isHoveringClickable())

    @override
    @overload
    def getTabs(self) -> 'List':
        """public final java.util.List<dev.ultreon.quantum.client.gui.widget.Tab> dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getTabs()"""
        return 'List'._wrap(super(tabs.TabbedUI, self).getTabs())

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'._wrap(super(_widget.UIContainer, self).position(arg0))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_widget.Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_widget.Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'._wrap(super(widget.UIContainer, self).getLayout())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'._wrap(super(_widget.UIContainer, self).bounds(arg0))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_widget.Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).title(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool._wrap(super(_gui.Screen, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_widget.UIContainer, self).remove(arg0)

    @property
    def focused(self) -> Widget:
        return Widget._wrap(super(_Screen).focused())

    @property
    def directHovered(self) -> Widget:
        return Widget._wrap(super(_Screen).directHovered())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_widget.Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(widget.Widget, self).componentRegistry())

    @override
    @overload
    def getSelected(self) -> int:
        """public final int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getSelected()"""
        return int._wrap(super(tabs.TabbedUI, self).getSelected())

    @override
    @overload
    def getContentY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getContentY()"""
        return int._wrap(super(tabs.TabbedUI, self).getContentY())

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_tabs.TabbedUI, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'._wrap(super(_gui.Screen, self).add(arg0))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_widget.Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool._wrap(super(_gui.Screen, self).filesDropped(arg0))

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_tabs.TabbedUI, self).build(arg0)

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool._wrap(super(_gui.Screen, self).charType(_char.valueOf(arg0)))

    @property
    def parentScreen(self) -> Screen:
        return Screen._wrap(super(_Screen).parentScreen())

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'._wrap(super(_widget.UIContainer, self).getExactWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_tabs.TabbedUI, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def build(self, arg0: 'TabbedUIBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.settings.SettingsScreen.build(dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI$TabbedUIBuilder)"""
        super(_SettingsScreen, self).build(arg0)

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_widget.Widget, self).setPreferredY(_int.valueOf(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_tabs.TabbedUI, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(widget.Widget, self).getPreferredSize())

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canClose()"""
        return bool._wrap(super(gui.Screen, self).canClose())

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.settings.PersonalSettingsUI
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client.gui.screens import tabs
except ImportError:
    tabs = _import_once("pyquantum.client.gui.screens.tabs")

import java.lang.Integer as _int
from builtins import bool
import dev.ultreon.quantum.client.gui.screens.settings.PersonalSettingsUI as _PersonalSettingsUI
_PersonalSettingsUI = _PersonalSettingsUI
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PersonalSettingsUI():
    """dev.ultreon.quantum.client.gui.screens.settings.PersonalSettingsUI"""
 
    @staticmethod
    def _wrap(java_value: _PersonalSettingsUI) -> 'PersonalSettingsUI':
        return PersonalSettingsUI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PersonalSettingsUI):
        """
        Dynamic initializer for PersonalSettingsUI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PersonalSettingsUI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PersonalSettingsUI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.settings.PersonalSettingsUI()"""
        val = _PersonalSettingsUI()
        self.__wrapper = val

    @overload
    def build(self, arg0: 'TabBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.settings.PersonalSettingsUI.build(dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder)"""
        super(_PersonalSettingsUI, self).build(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.settings.PersonalSettingsUI()"""
        val = _PersonalSettingsUI()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())