from __future__ import annotations
from overload import overload


 
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

from abc import abstractmethod, ABC
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
 
class TabbedUI():
    """dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI"""
 
    @staticmethod
    def _wrap(java_value: _TabbedUI) -> 'TabbedUI':
        return TabbedUI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TabbedUI):
        """
        Dynamic initializer for TabbedUI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TabbedUI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TabbedUI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(_gui.Screen, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseWheel(int,int,double)"""
        return bool._wrap(super(_TabbedUI, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

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

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_TabbedUI, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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

    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getContentHeight()"""
        return int._wrap(super(TabbedUI, self).getContentHeight())

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

    @overload
    def getTab(self) -> 'widget.Tab':
        """public final dev.ultreon.quantum.client.gui.widget.Tab dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getTab()"""
        return 'widget.Tab'._wrap(super(TabbedUI, self).getTab())

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
    def setSelected(self, arg0: int):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setSelected(int)"""
        super(_TabbedUI, self).setSelected(_int.valueOf(arg0))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.revalidate()"""
        super(TabbedUI, self).revalidate()

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_TabbedUI, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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

    @abstractmethod
    def build(self, arg0: 'TabbedUIBuilder'):
        """public abstract void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.build(dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI$TabbedUIBuilder)"""
        pass

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

    @overload
    def getTabX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getTabX()"""
        return int._wrap(super(TabbedUI, self).getTabX())

    @overload
    def getContentWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getContentWidth()"""
        return int._wrap(super(TabbedUI, self).getContentWidth())

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
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_TabbedUI, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_widget.Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @overload
    def isBottomSelected(self) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.isBottomSelected()"""
        return bool._wrap(super(TabbedUI, self).isBottomSelected())

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

    @overload
    def getSelected(self) -> int:
        """public final int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getSelected()"""
        return int._wrap(super(TabbedUI, self).getSelected())

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(_Screen).parentScreen(value)

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
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setSelected(self, arg0: 'Tab'):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setSelected(dev.ultreon.quantum.client.gui.widget.Tab)"""
        super(_TabbedUI, self).setSelected(arg0)

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

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mousePress(int,int,int)"""
        return bool._wrap(super(_TabbedUI, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(_gui.Screen, self).showDialog(arg0)

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
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_TabbedUI, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def getContentX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getContentX()"""
        return int._wrap(super(TabbedUI, self).getContentX())

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

    @overload
    def setSelected(self, arg0: 'TextObject'):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setSelected(dev.ultreon.quantum.text.TextObject)"""
        super(_TabbedUI, self).setSelected(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_widget.Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @overload
    def setTabs(self, arg0: 'List'):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setTabs(java.util.List<dev.ultreon.quantum.client.gui.widget.Tab>)"""
        super(_TabbedUI, self).setTabs(arg0)

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

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseMove(int,int)"""
        super(_TabbedUI, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).title(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool._wrap(super(_gui.Screen, self).keyPress(_int.valueOf(arg0)))

    @overload
    def getContentY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getContentY()"""
        return int._wrap(super(TabbedUI, self).getContentY())

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

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseRelease(int,int,int)"""
        return bool._wrap(super(_TabbedUI, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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

    @overload
    def setSelected(self, arg0: str):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setSelected(java.lang.String)"""
        super(_TabbedUI, self).setSelected(arg0)

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_TabbedUI, self).build(arg0)

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_widget.Widget, self).setPreferredY(_int.valueOf(arg0))

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
    def getTabs(self) -> 'List':
        """public final java.util.List<dev.ultreon.quantum.client.gui.widget.Tab> dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getTabs()"""
        return 'List'._wrap(super(TabbedUI, self).getTabs())

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT)

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI
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

from abc import abstractmethod, ABC
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
 
class TabbedUI():
    """dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI"""
 
    @staticmethod
    def _wrap(java_value: _TabbedUI) -> 'TabbedUI':
        return TabbedUI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TabbedUI):
        """
        Dynamic initializer for TabbedUI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TabbedUI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TabbedUI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(_gui.Screen, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseWheel(int,int,double)"""
        return bool._wrap(super(_TabbedUI, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

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

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_TabbedUI, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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

    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getContentHeight()"""
        return int._wrap(super(TabbedUI, self).getContentHeight())

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

    @overload
    def getTab(self) -> 'widget.Tab':
        """public final dev.ultreon.quantum.client.gui.widget.Tab dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getTab()"""
        return 'widget.Tab'._wrap(super(TabbedUI, self).getTab())

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
    def setSelected(self, arg0: int):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setSelected(int)"""
        super(_TabbedUI, self).setSelected(_int.valueOf(arg0))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.revalidate()"""
        super(TabbedUI, self).revalidate()

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_TabbedUI, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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

    @abstractmethod
    def build(self, arg0: 'TabbedUIBuilder'):
        """public abstract void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.build(dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI$TabbedUIBuilder)"""
        pass

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

    @overload
    def getTabX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getTabX()"""
        return int._wrap(super(TabbedUI, self).getTabX())

    @overload
    def getContentWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getContentWidth()"""
        return int._wrap(super(TabbedUI, self).getContentWidth())

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
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_TabbedUI, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_widget.Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @overload
    def isBottomSelected(self) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.isBottomSelected()"""
        return bool._wrap(super(TabbedUI, self).isBottomSelected())

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

    @overload
    def getSelected(self) -> int:
        """public final int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getSelected()"""
        return int._wrap(super(TabbedUI, self).getSelected())

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(_Screen).parentScreen(value)

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
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setSelected(self, arg0: 'Tab'):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setSelected(dev.ultreon.quantum.client.gui.widget.Tab)"""
        super(_TabbedUI, self).setSelected(arg0)

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

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mousePress(int,int,int)"""
        return bool._wrap(super(_TabbedUI, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(_gui.Screen, self).showDialog(arg0)

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
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_TabbedUI, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def getContentX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getContentX()"""
        return int._wrap(super(TabbedUI, self).getContentX())

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

    @overload
    def setSelected(self, arg0: 'TextObject'):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setSelected(dev.ultreon.quantum.text.TextObject)"""
        super(_TabbedUI, self).setSelected(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_widget.Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @overload
    def setTabs(self, arg0: 'List'):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setTabs(java.util.List<dev.ultreon.quantum.client.gui.widget.Tab>)"""
        super(_TabbedUI, self).setTabs(arg0)

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

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseMove(int,int)"""
        super(_TabbedUI, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).title(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool._wrap(super(_gui.Screen, self).keyPress(_int.valueOf(arg0)))

    @overload
    def getContentY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getContentY()"""
        return int._wrap(super(TabbedUI, self).getContentY())

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

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.mouseRelease(int,int,int)"""
        return bool._wrap(super(_TabbedUI, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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

    @overload
    def setSelected(self, arg0: str):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.setSelected(java.lang.String)"""
        super(_TabbedUI, self).setSelected(arg0)

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public final void dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_TabbedUI, self).build(arg0)

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_widget.Widget, self).setPreferredY(_int.valueOf(arg0))

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
    def getTabs(self) -> 'List':
        """public final java.util.List<dev.ultreon.quantum.client.gui.widget.Tab> dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.getTabs()"""
        return 'List'._wrap(super(TabbedUI, self).getTabs())

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT)

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder as _TabBuilder
_TabBuilder = _TabBuilder
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import dev.ultreon.quantum.client.gui.screens.tabs.TabContent as _TabContent
_TabContent = _TabContent
import java.lang.String as _String
_String = _String
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI as _TabbedUI
_TabbedUI = _TabbedUI
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.widget.Widget as _Widget
_Widget = _Widget
from builtins import bool
import dev.ultreon.quantum.client.QuantumClient as _QuantumClient
_QuantumClient = _QuantumClient
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TabBuilder():
    """dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder"""
 
    @staticmethod
    def _wrap(java_value: _TabBuilder) -> 'TabBuilder':
        return TabBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TabBuilder):
        """
        Dynamic initializer for TabBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TabBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TabBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addWithPos(self, arg0: 'Widget', arg1: 'Supplier') -> 'widget.Widget':
        """public <T extends dev.ultreon.quantum.client.gui.widget.Widget> T dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder.addWithPos(T,java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.Widget'._wrap(super(_TabBuilder, self).addWithPos(arg0, arg1))

    @overload
    def title(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder.title()"""
        return 'text.TextObject'._wrap(super(TabBuilder, self).title())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def screen(self) -> 'TabbedUI':
        """public dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder.screen()"""
        return 'TabbedUI'._wrap(super(TabBuilder, self).screen())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <T extends dev.ultreon.quantum.client.gui.widget.Widget> T dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder.add(T)"""
        return 'widget.Widget'._wrap(super(_TabBuilder, self).add(arg0))

    @overload
    def client(self) -> 'client.QuantumClient':
        """public dev.ultreon.quantum.client.QuantumClient dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder.client()"""
        return 'client.QuantumClient'._wrap(super(TabBuilder, self).client())

    @overload
    def content(self) -> 'TabContent':
        """public dev.ultreon.quantum.client.gui.screens.tabs.TabContent dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder.content()"""
        return 'TabContent'._wrap(super(TabBuilder, self).content())

    @overload
    def tabContent(self) -> 'TabContent':
        """public dev.ultreon.quantum.client.gui.screens.tabs.TabContent dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder.tabContent()"""
        return 'TabContent'._wrap(super(TabBuilder, self).tabContent())

    @overload
    def add(self, arg0: 'TextObject', arg1: 'Widget') -> 'widget.Widget':
        """public <T extends dev.ultreon.quantum.client.gui.widget.Widget> T dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder.add(dev.ultreon.quantum.text.TextObject,T)"""
        return 'widget.Widget'._wrap(super(_TabBuilder, self).add(arg0, arg1))

    @overload
    def __init__(self, arg0: 'TabContent'):
        """public dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder(dev.ultreon.quantum.client.gui.screens.tabs.TabContent)"""
        val = _TabBuilder(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder.equals(java.lang.Object)"""
        return bool._wrap(super(_TabBuilder, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder.hashCode()"""
        return int._wrap(super(TabBuilder, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder.toString()"""
        return str._wrap(super(TabBuilder, self).toString())

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

    @overload
    def addWithBounds(self, arg0: 'Widget', arg1: 'Supplier') -> 'widget.Widget':
        """public <T extends dev.ultreon.quantum.client.gui.widget.Widget> T dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder.addWithBounds(T,java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.Widget'._wrap(super(_TabBuilder, self).addWithBounds(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI$TabbedUIBuilder
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI as _TabbedUI_TabbedUIBuilder
_TabbedUIBuilder = _TabbedUI_TabbedUIBuilder.TabbedUIBuilder
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.gui.GuiBuilder as _GuiBuilder
_GuiBuilder = _GuiBuilder
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI as _TabbedUI
_TabbedUI = _TabbedUI
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.widget.Widget as _Widget
_Widget = _Widget
import dev.ultreon.quantum.client.gui.widget.Tab as _Tab
_Tab = _Tab
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TabbedUIBuilder():
    """dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI.TabbedUIBuilder"""
 
    @staticmethod
    def _wrap(java_value: _TabbedUIBuilder) -> 'TabbedUIBuilder':
        return TabbedUIBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TabbedUIBuilder):
        """
        Dynamic initializer for TabbedUIBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TabbedUIBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TabbedUIBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.GuiBuilder.hashCode()"""
        return int._wrap(super(gui.GuiBuilder, self).hashCode())

    @overload
    def add(self, arg0: 'TextObject', arg1: bool, arg2: int, arg3: 'UIContainer') -> 'widget.Tab':
        """public dev.ultreon.quantum.client.gui.widget.Tab dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI$TabbedUIBuilder.add(dev.ultreon.quantum.text.TextObject,boolean,int,dev.ultreon.quantum.client.gui.widget.UIContainer<?>)"""
        return 'widget.Tab'._wrap(super(_TabbedUIBuilder, self).add(arg0, _boolean.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def contentBounds(self, arg0: 'Supplier') -> 'TabbedUIBuilder':
        """public dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI$TabbedUIBuilder dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI$TabbedUIBuilder.contentBounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'TabbedUIBuilder'._wrap(super(_TabbedUIBuilder, self).contentBounds(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.GuiBuilder.equals(java.lang.Object)"""
        return bool._wrap(super(_gui.GuiBuilder, self).equals(arg0))

    @overload
    def add(self, arg0: 'TextObject', arg1: bool, arg2: int, arg3: 'Consumer') -> 'widget.Tab':
        """public dev.ultreon.quantum.client.gui.widget.Tab dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI$TabbedUIBuilder.add(dev.ultreon.quantum.text.TextObject,boolean,int,java.util.function.Consumer<dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder>)"""
        return 'widget.Tab'._wrap(super(_TabbedUIBuilder, self).add(arg0, _boolean.valueOf(arg1), _int.valueOf(arg2), arg3))

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def screen(self) -> 'TabbedUI':
        """public dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI$TabbedUIBuilder.screen()"""
        return 'TabbedUI'._wrap(super(TabbedUIBuilder, self).screen())

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

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <T extends dev.ultreon.quantum.client.gui.widget.Widget> T dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI$TabbedUIBuilder.add(T)"""
        return 'widget.Widget'._wrap(super(_TabbedUIBuilder, self).add(arg0))

    @overload
    def __init__(self, arg0: 'GuiBuilder', arg1: 'TabbedUI'):
        """public dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI$TabbedUIBuilder(dev.ultreon.quantum.client.gui.GuiBuilder,dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI)"""
        val = _TabbedUIBuilder(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.GuiBuilder.toString()"""
        return str._wrap(super(gui.GuiBuilder, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.tabs.TabContent
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Predicate as Predicate
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
import dev.ultreon.quantum.client.gui.screens.tabs.TabContent as _TabContent
_TabContent = _TabContent
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.util.RgbColor as _RgbColor
_RgbColor = _RgbColor
import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI as _TabbedUI
_TabbedUI = _TabbedUI
import java.nio.file.Path as _Path
_Path = _Path
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.gui.widget.layout.Layout as _Layout
_Layout = _Layout
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

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = _import_once("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.widget.ScrollableContainer as _ScrollableContainer
_ScrollableContainer = _ScrollableContainer
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
 
class TabContent():
    """dev.ultreon.quantum.client.gui.screens.tabs.TabContent"""
 
    @staticmethod
    def _wrap(java_value: _TabContent) -> 'TabContent':
        return TabContent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TabContent):
        """
        Dynamic initializer for TabContent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TabContent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TabContent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.ScrollableContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_widget.ScrollableContainer, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(widget.Widget, self).isHovered())

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'TabbedUI', arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'TextObject'):
        """public dev.ultreon.quantum.client.gui.screens.tabs.TabContent(dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI,int,int,int,int,dev.ultreon.quantum.text.TextObject)"""
        val = _TabContent(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5)
        self.__wrapper = val

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseMove(int,int)"""
        super(_widget.ScrollableContainer, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_widget.Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

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

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.ScrollableContainer':
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer dev.ultreon.quantum.client.gui.widget.ScrollableContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.ScrollableContainer'._wrap(super(_widget.ScrollableContainer, self).bounds(arg0))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_widget.Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(widget.Widget, self).path())

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

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyPress(int)"""
        return bool._wrap(super(_widget.UIContainer, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(widget.Widget, self).getPreferredHeight())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_widget.Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

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

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'widget.Widget'._wrap(super(_widget.UIContainer, self).add(arg0))

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
    def title(self, arg0: 'TextObject') -> 'TabContent':
        """public dev.ultreon.quantum.client.gui.screens.tabs.TabContent dev.ultreon.quantum.client.gui.screens.tabs.TabContent.title(dev.ultreon.quantum.text.TextObject)"""
        return 'TabContent'._wrap(super(_TabContent, self).title(arg0))

    @overload
    def title(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.screens.tabs.TabContent.title()"""
        return 'text.TextObject'._wrap(super(TabContent, self).title())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_widget.ScrollableContainer, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_widget.Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_widget.Widget, self).setPos(arg0)

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'._wrap(super(_widget.UIContainer, self).getWidgetsAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(widget.Widget, self).getX())

    @override
    @overload
    def isSelectable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.isSelectable()"""
        return bool._wrap(super(widget.ScrollableContainer, self).isSelectable())

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool._wrap(super(_widget.UIContainer, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_widget.Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.ScrollableContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'._wrap(super(_widget.ScrollableContainer, self).getWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'._wrap(super(widget.UIContainer, self).getLayout())

    @override
    @overload
    def removeWidgetIf(self, arg0: 'Predicate'):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.removeWidgetIf(java.util.function.Predicate<dev.ultreon.quantum.client.gui.widget.Widget>)"""
        super(_widget.ScrollableContainer, self).removeWidgetIf(arg0)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseRelease(int,int,int)"""
        return bool._wrap(super(_widget.ScrollableContainer, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool._wrap(super(_widget.UIContainer, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_widget.Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mousePress(int,int,int)"""
        return bool._wrap(super(_widget.ScrollableContainer, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.ScrollableContainer.getName()"""
        return str._wrap(super(widget.ScrollableContainer, self).getName())

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
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_widget.UIContainer, self).remove(arg0)

    @override
    @overload
    def removeWidget(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.removeWidget(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_widget.ScrollableContainer, self).removeWidget(arg0)

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.screens.tabs.TabContent.revalidate()"""
        super(TabContent, self).revalidate()

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_widget.Widget, self).setVisible(_boolean.valueOf(arg0))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseWheel(int,int,double)"""
        return bool._wrap(super(_widget.ScrollableContainer, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def backgroundColor(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.gui.widget.ScrollableContainer.backgroundColor()"""
        return 'util.RgbColor'._wrap(super(widget.ScrollableContainer, self).backgroundColor())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @override
    @overload
    def mouseEnter(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseEnter(int,int)"""
        super(_widget.ScrollableContainer, self).mouseEnter(_int.valueOf(arg0), _int.valueOf(arg1))

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

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.ScrollableContainer':
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer dev.ultreon.quantum.client.gui.widget.ScrollableContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.ScrollableContainer'._wrap(super(_widget.ScrollableContainer, self).position(arg0))

    @overload
    def selectable(self, arg0: bool) -> 'widget.ScrollableContainer':
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer dev.ultreon.quantum.client.gui.widget.ScrollableContainer.selectable(boolean)"""
        return 'widget.ScrollableContainer'._wrap(super(_widget.ScrollableContainer, self).selectable(_boolean.valueOf(arg0)))

    @overload
    def backgroundColor(self, arg0: 'RgbColor') -> 'widget.ScrollableContainer':
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer dev.ultreon.quantum.client.gui.widget.ScrollableContainer.backgroundColor(dev.ultreon.quantum.util.RgbColor)"""
        return 'widget.ScrollableContainer'._wrap(super(_widget.ScrollableContainer, self).backgroundColor(arg0))

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
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_widget.Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def mouseExit(self):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseExit()"""
        super(widget.ScrollableContainer, self).mouseExit()

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.ScrollableContainer.getContentHeight()"""
        return int._wrap(super(widget.ScrollableContainer, self).getContentHeight())

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_widget.UIContainer, self).renderChild(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'._wrap(super(_widget.UIContainer, self).getExactWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

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

    @overload
    def parent(self) -> 'TabbedUI':
        """public dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI dev.ultreon.quantum.client.gui.screens.tabs.TabContent.parent()"""
        return 'TabbedUI'._wrap(super(TabContent, self).parent())

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
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'._wrap(super(component.GameComponentHolder, self).components())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool._wrap(_Widget.isPosWithin(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_widget.Widget, self).height(_int.valueOf(arg0))

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
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(widget.Widget, self).getWidth())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_widget.Widget, self).setPreferredY(_int.valueOf(arg0))

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
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(widget.Widget, self).getPreferredSize())

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_widget.Widget, self).setPreferredWidth(_int.valueOf(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT)