from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
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
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
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

import dev.ultreon.quantum.world.WorldStorage as _WorldStorage
_WorldStorage = _WorldStorage
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import dev.ultreon.quantum.client.gui.screens.WorldEditScreen as _WorldEditScreen
_WorldEditScreen = _WorldEditScreen
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
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldEditScreen():
    """dev.ultreon.quantum.client.gui.screens.WorldEditScreen"""
 
    @staticmethod
    def _wrap(java_value: _WorldEditScreen) -> 'WorldEditScreen':
        return WorldEditScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldEditScreen):
        """
        Dynamic initializer for WorldEditScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldEditScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldEditScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def getWorld(self) -> 'world.WorldStorage':
        """public dev.ultreon.quantum.world.WorldStorage dev.ultreon.quantum.client.gui.screens.WorldEditScreen.getWorld()"""
        return 'world.WorldStorage'._wrap(super(WorldEditScreen, self).getWorld())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(widget.Widget, self).getWidth())

    @overload
    def __init__(self, arg0: 'WorldStorage'):
        """public dev.ultreon.quantum.client.gui.screens.WorldEditScreen(dev.ultreon.quantum.world.WorldStorage)"""
        val = _WorldEditScreen(arg0)
        self.__wrapper = val

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
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.WorldEditScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_WorldEditScreen, self).build(arg0)

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
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(widget.Widget, self).isHovered())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.WorldEditScreen.canCloseWithEsc()"""
        return bool._wrap(super(WorldEditScreen, self).canCloseWithEsc())

    @property
    def focused(self, value: 'widget.Widget'):
        super(_Screen).focused(value)

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool._wrap(super(gui.Screen, self).isHoveringClickable())

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT)

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.WorldEditScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
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
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
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

import dev.ultreon.quantum.world.WorldStorage as _WorldStorage
_WorldStorage = _WorldStorage
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import dev.ultreon.quantum.client.gui.screens.WorldEditScreen as _WorldEditScreen
_WorldEditScreen = _WorldEditScreen
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
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldEditScreen():
    """dev.ultreon.quantum.client.gui.screens.WorldEditScreen"""
 
    @staticmethod
    def _wrap(java_value: _WorldEditScreen) -> 'WorldEditScreen':
        return WorldEditScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldEditScreen):
        """
        Dynamic initializer for WorldEditScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldEditScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldEditScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def getWorld(self) -> 'world.WorldStorage':
        """public dev.ultreon.quantum.world.WorldStorage dev.ultreon.quantum.client.gui.screens.WorldEditScreen.getWorld()"""
        return 'world.WorldStorage'._wrap(super(WorldEditScreen, self).getWorld())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(widget.Widget, self).getWidth())

    @overload
    def __init__(self, arg0: 'WorldStorage'):
        """public dev.ultreon.quantum.client.gui.screens.WorldEditScreen(dev.ultreon.quantum.world.WorldStorage)"""
        val = _WorldEditScreen(arg0)
        self.__wrapper = val

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
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.WorldEditScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_WorldEditScreen, self).build(arg0)

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
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(widget.Widget, self).isHovered())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.WorldEditScreen.canCloseWithEsc()"""
        return bool._wrap(super(WorldEditScreen, self).canCloseWithEsc())

    @property
    def focused(self, value: 'widget.Widget'):
        super(_Screen).focused(value)

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool._wrap(super(gui.Screen, self).isHoveringClickable())

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT)

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.WorldEditScreen 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.MessageScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
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
import dev.ultreon.quantum.client.gui.screens.MessageScreen as _MessageScreen
_MessageScreen = _MessageScreen
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
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MessageScreen():
    """dev.ultreon.quantum.client.gui.screens.MessageScreen"""
 
    @staticmethod
    def _wrap(java_value: _MessageScreen) -> 'MessageScreen':
        return MessageScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessageScreen):
        """
        Dynamic initializer for MessageScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessageScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessageScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'TextObject'):
        """public dev.ultreon.quantum.client.gui.screens.MessageScreen(dev.ultreon.quantum.text.TextObject)"""
        val = _MessageScreen(arg0)
        self.__wrapper = val

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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

    @overload
    def message(self, arg0: str) -> 'MessageScreen':
        """public dev.ultreon.quantum.client.gui.screens.MessageScreen dev.ultreon.quantum.client.gui.screens.MessageScreen.message(java.lang.String)"""
        return 'MessageScreen'._wrap(super(_MessageScreen, self).message(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @overload
    def renderBackground(self, arg0: 'Renderer'):
        """public void dev.ultreon.quantum.client.gui.screens.MessageScreen.renderBackground(dev.ultreon.quantum.client.gui.Renderer)"""
        super(_MessageScreen, self).renderBackground(arg0)

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

    @overload
    def message(self, arg0: 'TextObject') -> 'MessageScreen':
        """public dev.ultreon.quantum.client.gui.screens.MessageScreen dev.ultreon.quantum.client.gui.screens.MessageScreen.message(dev.ultreon.quantum.text.TextObject)"""
        return 'MessageScreen'._wrap(super(_MessageScreen, self).message(arg0))

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

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.MessageScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_MessageScreen, self).build(arg0)

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
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.MessageScreen.canClose()"""
        return bool._wrap(super(MessageScreen, self).canClose())

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

    @overload
    def __init__(self, arg0: 'TranslationText', arg1: str):
        """public dev.ultreon.quantum.client.gui.screens.MessageScreen(dev.ultreon.quantum.text.TranslationText,java.lang.String)"""
        val = _MessageScreen(arg0, arg1)
        self.__wrapper = val

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.MultiplayerScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.gui.screens.MultiplayerScreen as _MultiplayerScreen
_MultiplayerScreen = _MultiplayerScreen
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
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
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
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MultiplayerScreen():
    """dev.ultreon.quantum.client.gui.screens.MultiplayerScreen"""
 
    @staticmethod
    def _wrap(java_value: _MultiplayerScreen) -> 'MultiplayerScreen':
        return MultiplayerScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiplayerScreen):
        """
        Dynamic initializer for MultiplayerScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiplayerScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiplayerScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def __init__(self, arg0: 'Screen'):
        """public dev.ultreon.quantum.client.gui.screens.MultiplayerScreen(dev.ultreon.quantum.client.gui.Screen)"""
        val = _MultiplayerScreen(arg0)
        self.__wrapper = val

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.MultiplayerScreen()"""
        val = _MultiplayerScreen()
        self.__wrapper = val

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
        """public void dev.ultreon.quantum.client.gui.screens.MultiplayerScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_MultiplayerScreen, self).build(arg0)

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.MultiplayerScreen()"""
        val = _MultiplayerScreen()
        self.__wrapper = val

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
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.ModImportFailedScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.UIContainer as _UIContainer
_UIContainer = _UIContainer
import dev.ultreon.quantum.client.gui.screens.ModImportFailedScreen as _ModImportFailedScreen
_ModImportFailedScreen = _ModImportFailedScreen
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
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
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModImportFailedScreen():
    """dev.ultreon.quantum.client.gui.screens.ModImportFailedScreen"""
 
    @staticmethod
    def _wrap(java_value: _ModImportFailedScreen) -> 'ModImportFailedScreen':
        return ModImportFailedScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModImportFailedScreen):
        """
        Dynamic initializer for ModImportFailedScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModImportFailedScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModImportFailedScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.ModImportFailedScreen()"""
        val = _ModImportFailedScreen()
        self.__wrapper = val

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
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.ModImportFailedScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_ModImportFailedScreen, self).build(arg0)

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_widget.Widget, self).setPreferredY(_int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.ModImportFailedScreen()"""
        val = _ModImportFailedScreen()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.DisconnectedScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
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
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
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

import dev.ultreon.quantum.client.gui.screens.DisconnectedScreen as _DisconnectedScreen
_DisconnectedScreen = _DisconnectedScreen
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
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DisconnectedScreen():
    """dev.ultreon.quantum.client.gui.screens.DisconnectedScreen"""
 
    @staticmethod
    def _wrap(java_value: _DisconnectedScreen) -> 'DisconnectedScreen':
        return DisconnectedScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DisconnectedScreen):
        """
        Dynamic initializer for DisconnectedScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DisconnectedScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DisconnectedScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.DisconnectedScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_DisconnectedScreen, self).build(arg0)

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @overload
    def __init__(self, arg0: str, arg1: bool):
        """public dev.ultreon.quantum.client.gui.screens.DisconnectedScreen(java.lang.String,boolean)"""
        val = _DisconnectedScreen(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

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

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.DisconnectedScreen.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_DisconnectedScreen, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.RestartConfirmScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
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
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import dev.ultreon.quantum.client.gui.screens.RestartConfirmScreen as _RestartConfirmScreen
_RestartConfirmScreen = _RestartConfirmScreen
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
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RestartConfirmScreen():
    """dev.ultreon.quantum.client.gui.screens.RestartConfirmScreen"""
 
    @staticmethod
    def _wrap(java_value: _RestartConfirmScreen) -> 'RestartConfirmScreen':
        return RestartConfirmScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RestartConfirmScreen):
        """
        Dynamic initializer for RestartConfirmScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RestartConfirmScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RestartConfirmScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.RestartConfirmScreen()"""
        val = _RestartConfirmScreen()
        self.__wrapper = val

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
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.RestartConfirmScreen()"""
        val = _RestartConfirmScreen()
        self.__wrapper = val

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.RestartConfirmScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_RestartConfirmScreen, self).build(arg0)

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.LanguageScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.client.gui.widget.SelectionList as _SelectionList
_SelectionList = _SelectionList
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.UIContainer as _UIContainer
_UIContainer = _UIContainer
import dev.ultreon.quantum.client.gui.screens.LanguageScreen as _LanguageScreen
_LanguageScreen = _LanguageScreen
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
import dev.ultreon.quantum.client.gui.widget.Label as _Label
_Label = _Label
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

import dev.ultreon.quantum.client.gui.widget.TextButton as _TextButton
_TextButton = _TextButton
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
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LanguageScreen():
    """dev.ultreon.quantum.client.gui.screens.LanguageScreen"""
 
    @staticmethod
    def _wrap(java_value: _LanguageScreen) -> 'LanguageScreen':
        return LanguageScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LanguageScreen):
        """
        Dynamic initializer for LanguageScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LanguageScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LanguageScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.LanguageScreen()"""
        val = _LanguageScreen()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.LanguageScreen()"""
        val = _LanguageScreen()
        self.__wrapper = val

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
    def getTitleLabel(self) -> 'widget.Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.screens.LanguageScreen.getTitleLabel()"""
        return 'widget.Label'._wrap(super(LanguageScreen, self).getTitleLabel())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.LanguageScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_LanguageScreen, self).build(arg0)

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

    @overload
    def getBackButton(self) -> 'widget.TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.screens.LanguageScreen.getBackButton()"""
        return 'widget.TextButton'._wrap(super(LanguageScreen, self).getBackButton())

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def getList(self) -> 'widget.SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<java.util.Locale> dev.ultreon.quantum.client.gui.screens.LanguageScreen.getList()"""
        return 'widget.SelectionList'._wrap(super(LanguageScreen, self).getList())

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
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.WorldCreationScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
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
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.gui.widget.TextEntry as _TextEntry
_TextEntry = _TextEntry
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

import dev.ultreon.quantum.client.gui.widget.TextButton as _TextButton
_TextButton = _TextButton
from builtins import bool
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.client.gui.screens.WorldCreationScreen as _WorldCreationScreen
_WorldCreationScreen = _WorldCreationScreen
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
import dev.ultreon.quantum.client.gui.widget.IconButton as _IconButton
_IconButton = _IconButton
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldCreationScreen():
    """dev.ultreon.quantum.client.gui.screens.WorldCreationScreen"""
 
    @staticmethod
    def _wrap(java_value: _WorldCreationScreen) -> 'WorldCreationScreen':
        return WorldCreationScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldCreationScreen):
        """
        Dynamic initializer for WorldCreationScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldCreationScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldCreationScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getCreateButton(self) -> 'widget.TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.screens.WorldCreationScreen.getCreateButton()"""
        return 'widget.TextButton'._wrap(super(WorldCreationScreen, self).getCreateButton())

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @overload
    def getReloadButton(self) -> 'widget.IconButton':
        """public dev.ultreon.quantum.client.gui.widget.IconButton dev.ultreon.quantum.client.gui.screens.WorldCreationScreen.getReloadButton()"""
        return 'widget.IconButton'._wrap(super(WorldCreationScreen, self).getReloadButton())

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str._wrap(super(gui.Screen, self).getRawTitle())

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool._wrap(super(_gui.Screen, self).onClose(arg0))

    @overload
    def getWorldName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.screens.WorldCreationScreen.getWorldName()"""
        return str._wrap(super(WorldCreationScreen, self).getWorldName())

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.WorldCreationScreen()"""
        val = _WorldCreationScreen()
        self.__wrapper = val

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

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.WorldCreationScreen()"""
        val = _WorldCreationScreen()
        self.__wrapper = val

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool._wrap(super(gui.Screen, self).isHoveringClickable())

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'._wrap(super(_gui.Screen, self).add(arg0))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_widget.Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getWorldNameEntry(self) -> 'widget.TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.screens.WorldCreationScreen.getWorldNameEntry()"""
        return 'widget.TextEntry'._wrap(super(WorldCreationScreen, self).getWorldNameEntry())

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

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.WorldCreationScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_WorldCreationScreen, self).build(arg0)

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
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.WorldLoadScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.UIContainer as _UIContainer
_UIContainer = _UIContainer
import dev.ultreon.quantum.client.gui.screens.WorldLoadScreen as _WorldLoadScreen
_WorldLoadScreen = _WorldLoadScreen
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
import dev.ultreon.quantum.client.gui.widget.Label as _Label
_Label = _Label
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

from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

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
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
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
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldLoadScreen():
    """dev.ultreon.quantum.client.gui.screens.WorldLoadScreen"""
 
    @staticmethod
    def _wrap(java_value: _WorldLoadScreen) -> 'WorldLoadScreen':
        return WorldLoadScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldLoadScreen):
        """
        Dynamic initializer for WorldLoadScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldLoadScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldLoadScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.gui.screens.WorldLoadScreen.PROGRESS_BG
    PROGRESS_BG: 'util.RgbColor' = _wrap(_util.RgbColor.PROGRESS_BG)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.gui.screens.WorldLoadScreen.PROGRESS_FG
    PROGRESS_FG: 'util.RgbColor' = _wrap(_util.RgbColor.PROGRESS_FG)


    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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

    @overload
    def setCloseScreen(self, arg0: 'DeathScreen'):
        """public void dev.ultreon.quantum.client.gui.screens.WorldLoadScreen.setCloseScreen(dev.ultreon.quantum.client.gui.screens.DeathScreen)"""
        super(_WorldLoadScreen, self).setCloseScreen(arg0)

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
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @overload
    def __init__(self, arg0: 'WorldStorage'):
        """public dev.ultreon.quantum.client.gui.screens.WorldLoadScreen(dev.ultreon.quantum.world.WorldStorage)"""
        val = _WorldLoadScreen(arg0)
        self.__wrapper = val

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

    @overload
    def getTitleLabel(self) -> 'widget.Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.screens.WorldLoadScreen.getTitleLabel()"""
        return 'widget.Label'._wrap(super(WorldLoadScreen, self).getTitleLabel())

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(widget.Widget, self).isHovered())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(_Screen).parentScreen(value)

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'._wrap(super(gui.Screen, self).path())

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.WorldLoadScreen.canCloseWithEsc()"""
        return bool._wrap(super(WorldLoadScreen, self).canCloseWithEsc())

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

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.WorldLoadScreen.canClose()"""
        return bool._wrap(super(WorldLoadScreen, self).canClose())

    @overload
    def getDescriptionLabel(self) -> 'widget.Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.screens.WorldLoadScreen.getDescriptionLabel()"""
        return 'widget.Label'._wrap(super(WorldLoadScreen, self).getDescriptionLabel())

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

    @overload
    def run(self):
        """public void dev.ultreon.quantum.client.gui.screens.WorldLoadScreen.run()"""
        super(WorldLoadScreen, self).run()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.WorldLoadScreen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool._wrap(super(_WorldLoadScreen, self).onClose(arg0))

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
        """public void dev.ultreon.quantum.client.gui.screens.WorldLoadScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_WorldLoadScreen, self).build(arg0)

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

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))

    @overload
    def done(self):
        """public void dev.ultreon.quantum.client.gui.screens.WorldLoadScreen.done()"""
        super(WorldLoadScreen, self).done()


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.TitleScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
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
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
import dev.ultreon.quantum.client.gui.widget.Label as _Label
_Label = _Label
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

from builtins import bool
import dev.ultreon.quantum.client.gui.screens.TitleScreen as _TitleScreen
_TitleScreen = _TitleScreen
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
import dev.ultreon.quantum.client.gui.widget.TitleButton as _TitleButton
_TitleButton = _TitleButton
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TitleScreen():
    """dev.ultreon.quantum.client.gui.screens.TitleScreen"""
 
    @staticmethod
    def _wrap(java_value: _TitleScreen) -> 'TitleScreen':
        return TitleScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TitleScreen):
        """
        Dynamic initializer for TitleScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TitleScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TitleScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.TitleScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_TitleScreen, self).build(arg0)

    @overload
    def getModListButton(self) -> 'widget.TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.screens.TitleScreen.getModListButton()"""
        return 'widget.TitleButton'._wrap(super(TitleScreen, self).getModListButton())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.TitleScreen()"""
        val = _TitleScreen()
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
    def getSingleplayerButton(self) -> 'widget.TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.screens.TitleScreen.getSingleplayerButton()"""
        return 'widget.TitleButton'._wrap(super(TitleScreen, self).getSingleplayerButton())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.TitleScreen.canClose()"""
        return bool._wrap(super(TitleScreen, self).canClose())

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @overload
    def getTitleLabel(self) -> 'widget.Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.screens.TitleScreen.getTitleLabel()"""
        return 'widget.Label'._wrap(super(TitleScreen, self).getTitleLabel())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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

    @overload
    def getQuitButton(self) -> 'widget.TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.screens.TitleScreen.getQuitButton()"""
        return 'widget.TitleButton'._wrap(super(TitleScreen, self).getQuitButton())

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

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.TitleScreen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool._wrap(super(_TitleScreen, self).onClose(arg0))

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
    def getWorldGenTestButton(self) -> 'widget.TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.screens.TitleScreen.getWorldGenTestButton()"""
        return 'widget.TitleButton'._wrap(super(TitleScreen, self).getWorldGenTestButton())

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

    @overload
    def getMultiplayerButton(self) -> 'widget.TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.screens.TitleScreen.getMultiplayerButton()"""
        return 'widget.TitleButton'._wrap(super(TitleScreen, self).getMultiplayerButton())

    @property
    def directHovered(self) -> Widget:
        return Widget._wrap(super(_Screen).directHovered())

    @overload
    def getOptionsButton(self) -> 'widget.TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.screens.TitleScreen.getOptionsButton()"""
        return 'widget.TitleButton'._wrap(super(TitleScreen, self).getOptionsButton())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.TitleScreen()"""
        val = _TitleScreen()
        self.__wrapper = val

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

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.WorldDeleteConfirmScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
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
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
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

import dev.ultreon.quantum.world.WorldStorage as _WorldStorage
_WorldStorage = _WorldStorage
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import dev.ultreon.quantum.client.gui.screens.WorldDeleteConfirmScreen as _WorldDeleteConfirmScreen
_WorldDeleteConfirmScreen = _WorldDeleteConfirmScreen
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
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldDeleteConfirmScreen():
    """dev.ultreon.quantum.client.gui.screens.WorldDeleteConfirmScreen"""
 
    @staticmethod
    def _wrap(java_value: _WorldDeleteConfirmScreen) -> 'WorldDeleteConfirmScreen':
        return WorldDeleteConfirmScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldDeleteConfirmScreen):
        """
        Dynamic initializer for WorldDeleteConfirmScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldDeleteConfirmScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldDeleteConfirmScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.WorldDeleteConfirmScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_WorldDeleteConfirmScreen, self).build(arg0)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @overload
    def getStorage(self) -> 'world.WorldStorage':
        """public dev.ultreon.quantum.world.WorldStorage dev.ultreon.quantum.client.gui.screens.WorldDeleteConfirmScreen.getStorage()"""
        return 'world.WorldStorage'._wrap(super(WorldDeleteConfirmScreen, self).getStorage())

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

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))

    @overload
    def __init__(self, arg0: 'WorldStorage'):
        """public dev.ultreon.quantum.client.gui.screens.WorldDeleteConfirmScreen(dev.ultreon.quantum.world.WorldStorage)"""
        val = _WorldDeleteConfirmScreen(arg0)
        self.__wrapper = val


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.ModListScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.client.gui.widget.SelectionList as _SelectionList
_SelectionList = _SelectionList
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
import dev.ultreon.quantum.client.gui.screens.ModListScreen as _ModListScreen
_ModListScreen = _ModListScreen
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
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

import dev.ultreon.quantum.client.gui.widget.TextButton as _TextButton
_TextButton = _TextButton
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
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModListScreen():
    """dev.ultreon.quantum.client.gui.screens.ModListScreen"""
 
    @staticmethod
    def _wrap(java_value: _ModListScreen) -> 'ModListScreen':
        return ModListScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModListScreen):
        """
        Dynamic initializer for ModListScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModListScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModListScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def __init__(self, arg0: 'Screen'):
        """public dev.ultreon.quantum.client.gui.screens.ModListScreen(dev.ultreon.quantum.client.gui.Screen)"""
        val = _ModListScreen(arg0)
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
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @overload
    def getConfigButton(self) -> 'widget.TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.screens.ModListScreen.getConfigButton()"""
        return 'widget.TextButton'._wrap(super(ModListScreen, self).getConfigButton())

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
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.ModListScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_ModListScreen, self).build(arg0)

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
    def getList(self) -> 'widget.SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<dev.ultreon.quantum.Mod> dev.ultreon.quantum.client.gui.screens.ModListScreen.getList()"""
        return 'widget.SelectionList'._wrap(super(ModListScreen, self).getList())

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def getBackButton(self) -> 'widget.TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.screens.ModListScreen.getBackButton()"""
        return 'widget.TextButton'._wrap(super(ModListScreen, self).getBackButton())

    @overload
    def onBack(self, arg0: 'TextButton'):
        """public void dev.ultreon.quantum.client.gui.screens.ModListScreen.onBack(dev.ultreon.quantum.client.gui.widget.TextButton)"""
        super(_ModListScreen, self).onBack(arg0)

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_widget.Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.ModListScreen.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_ModListScreen, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.PauseScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.UIContainer as _UIContainer
_UIContainer = _UIContainer
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.nio.file.Path as _Path
_Path = _Path
import dev.ultreon.quantum.client.gui.widget.Label as _Label
_Label = _Label
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
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
import java.util.Collection as _Collection
_Collection = _Collection
import dev.ultreon.quantum.client.gui.widget.Widget as _Widget
_Widget = _Widget
import dev.ultreon.quantum.client.Screenshot as _Screenshot
_Screenshot = _Screenshot
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import dev.ultreon.quantum.client.gui.Screen as _Screen
_Screen = _Screen
import dev.ultreon.quantum.client.gui.screens.PauseScreen as _PauseScreen
_PauseScreen = _PauseScreen
import dev.ultreon.quantum.client.gui.widget.TextButton as _TextButton
_TextButton = _TextButton
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = _import_once("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.client.gui.Dialog as _Dialog
_Dialog = _Dialog
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.Position as _Position
_Position = _Position
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.widget.Panel as _Panel
_Panel = _Panel
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
 
class PauseScreen():
    """dev.ultreon.quantum.client.gui.screens.PauseScreen"""
 
    @staticmethod
    def _wrap(java_value: _PauseScreen) -> 'PauseScreen':
        return PauseScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PauseScreen):
        """
        Dynamic initializer for PauseScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PauseScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PauseScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.PauseScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_PauseScreen, self).build(arg0)

    @overload
    def getOptionsButton(self) -> 'widget.TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.screens.PauseScreen.getOptionsButton()"""
        return 'widget.TextButton'._wrap(super(PauseScreen, self).getOptionsButton())

    @overload
    def getGamePausedLabel(self) -> 'widget.Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.screens.PauseScreen.getGamePausedLabel()"""
        return 'widget.Label'._wrap(super(PauseScreen, self).getGamePausedLabel())

    @overload
    def getPanel(self) -> 'widget.Panel':
        """public dev.ultreon.quantum.client.gui.widget.Panel dev.ultreon.quantum.client.gui.screens.PauseScreen.getPanel()"""
        return 'widget.Panel'._wrap(super(PauseScreen, self).getPanel())

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

    @overload
    def getExitWorldButton(self) -> 'widget.TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.screens.PauseScreen.getExitWorldButton()"""
        return 'widget.TextButton'._wrap(super(PauseScreen, self).getExitWorldButton())

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
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.PauseScreen.canCloseWithEsc()"""
        return bool._wrap(super(PauseScreen, self).canCloseWithEsc())

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_widget.Widget, self).setBounds(arg0)

    @overload
    def getScreenshot(self) -> 'client.Screenshot':
        """public dev.ultreon.quantum.client.Screenshot dev.ultreon.quantum.client.gui.screens.PauseScreen.getScreenshot()"""
        return 'client.Screenshot'._wrap(super(PauseScreen, self).getScreenshot())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(widget.Widget, self).getHeight())

    @overload
    def setScreenshot(self, arg0: 'Screenshot'):
        """public void dev.ultreon.quantum.client.gui.screens.PauseScreen.setScreenshot(dev.ultreon.quantum.client.Screenshot)"""
        super(_PauseScreen, self).setScreenshot(arg0)

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_widget.Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(widget.Widget, self).isHovered())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.PauseScreen()"""
        val = _PauseScreen()
        self.__wrapper = val

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_widget.Widget, self).setPreferredY(_int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.PauseScreen()"""
        val = _PauseScreen()
        self.__wrapper = val

    @overload
    def getBackToGameButton(self) -> 'widget.TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.screens.PauseScreen.getBackToGameButton()"""
        return 'widget.TextButton'._wrap(super(PauseScreen, self).getBackToGameButton())

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
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.ChatScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
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

import dev.ultreon.quantum.client.gui.widget.ChatTextEntry as _ChatTextEntry
_ChatTextEntry = _ChatTextEntry
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.gui.screens.ChatScreen as _ChatScreen
_ChatScreen = _ChatScreen
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

from builtins import bool
from builtins import str
import it.unimi.dsi.fastutil.longs.LongList as _LongList
_LongList = _LongList
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
import it.unimi.dsi.fastutil.longs.LongList as LongList
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ChatScreen():
    """dev.ultreon.quantum.client.gui.screens.ChatScreen"""
 
    @staticmethod
    def _wrap(java_value: _ChatScreen) -> 'ChatScreen':
        return ChatScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChatScreen):
        """
        Dynamic initializer for ChatScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChatScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChatScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.ChatScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_ChatScreen, self).build(arg0)

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.ChatScreen.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_ChatScreen, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.gui.screens.ChatScreen(java.lang.String)"""
        val = _ChatScreen(arg0)
        self.__wrapper = val

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

    @overload
    def send(self):
        """public void dev.ultreon.quantum.client.gui.screens.ChatScreen.send()"""
        super(ChatScreen, self).send()

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_widget.Widget, self).setVisible(_boolean.valueOf(arg0))

    @staticmethod
    @overload
    def getMessageTimestamps() -> 'LongList':
        """public static it.unimi.dsi.fastutil.longs.LongList dev.ultreon.quantum.client.gui.screens.ChatScreen.getMessageTimestamps()"""
        return LongList._wrap(_ChatScreen.getMessageTimestamps())

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
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.screens.ChatScreen()"""
        val = _ChatScreen()
        self.__wrapper = val

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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

    @staticmethod
    @overload
    def addMessage(arg0: 'TextObject'):
        """public static void dev.ultreon.quantum.client.gui.screens.ChatScreen.addMessage(dev.ultreon.quantum.text.TextObject)"""
        _ChatScreen.addMessage(arg0)

    @overload
    def getEntry(self) -> 'widget.ChatTextEntry':
        """public dev.ultreon.quantum.client.gui.widget.ChatTextEntry dev.ultreon.quantum.client.gui.screens.ChatScreen.getEntry()"""
        return 'widget.ChatTextEntry'._wrap(super(ChatScreen, self).getEntry())

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
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'._wrap(super(gui.Screen, self).path())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_widget.Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def getMessages() -> 'List':
        """public static java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.client.gui.screens.ChatScreen.getMessages()"""
        return List._wrap(_ChatScreen.getMessages())

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

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(_gui.Screen, self).showDialog(arg0)

    @overload
    def onTabComplete(self, arg0: 'String'):
        """public void dev.ultreon.quantum.client.gui.screens.ChatScreen.onTabComplete(java.lang.String[])"""
        super(_ChatScreen, self).onTabComplete(arg0)

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.screens.ChatScreen()"""
        val = _ChatScreen()
        self.__wrapper = val

    @property
    def focused(self) -> Widget:
        return Widget._wrap(super(_Screen).focused())

    @property
    def directHovered(self) -> Widget:
        return Widget._wrap(super(_Screen).directHovered())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.DeathScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
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
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
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

import dev.ultreon.quantum.client.gui.widget.TextButton as _TextButton
_TextButton = _TextButton
from builtins import bool
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.client.gui.screens.DeathScreen as _DeathScreen
_DeathScreen = _DeathScreen
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
try:
    from pyquantum.entity import damagesource
except ImportError:
    damagesource = _import_once("pyquantum.entity.damagesource")

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
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DeathScreen():
    """dev.ultreon.quantum.client.gui.screens.DeathScreen"""
 
    @staticmethod
    def _wrap(java_value: _DeathScreen) -> 'DeathScreen':
        return DeathScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DeathScreen):
        """
        Dynamic initializer for DeathScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DeathScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DeathScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def __init__(self, arg0: 'DamageSource'):
        """public dev.ultreon.quantum.client.gui.screens.DeathScreen(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        val = _DeathScreen(arg0)
        self.__wrapper = val

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.DeathScreen.canCloseWithEsc()"""
        return bool._wrap(super(DeathScreen, self).canCloseWithEsc())

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def getRespawnButton(self) -> 'widget.TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.screens.DeathScreen.getRespawnButton()"""
        return 'widget.TextButton'._wrap(super(DeathScreen, self).getRespawnButton())

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
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(widget.Widget, self).isHovered())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.DeathScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_DeathScreen, self).build(arg0)

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

    @overload
    def getExitWorldButton(self) -> 'widget.TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.screens.DeathScreen.getExitWorldButton()"""
        return 'widget.TextButton'._wrap(super(DeathScreen, self).getExitWorldButton())

    @overload
    def renderBackground(self, arg0: 'Renderer'):
        """public void dev.ultreon.quantum.client.gui.screens.DeathScreen.renderBackground(dev.ultreon.quantum.client.gui.Renderer)"""
        super(_DeathScreen, self).renderBackground(arg0)

    @property
    def directHovered(self) -> Widget:
        return Widget._wrap(super(_Screen).directHovered())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.WorldGenTestScreen
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.screens.WorldGenTestScreen as _WorldGenTestScreen
_WorldGenTestScreen = _WorldGenTestScreen
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
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
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
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
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldGenTestScreen():
    """dev.ultreon.quantum.client.gui.screens.WorldGenTestScreen"""
 
    @staticmethod
    def _wrap(java_value: _WorldGenTestScreen) -> 'WorldGenTestScreen':
        return WorldGenTestScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldGenTestScreen):
        """
        Dynamic initializer for WorldGenTestScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldGenTestScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldGenTestScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

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
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.gui.screens.WorldGenTestScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_WorldGenTestScreen, self).build(arg0)

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

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.WorldGenTestScreen.keyRelease(int)"""
        return bool._wrap(super(_WorldGenTestScreen, self).keyRelease(_int.valueOf(arg0)))

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT)