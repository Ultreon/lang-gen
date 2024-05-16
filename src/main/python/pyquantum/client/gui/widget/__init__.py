from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.widget.HorizontalList as _HorizontalList
_HorizontalList = _HorizontalList
import java.util.function.Supplier as Supplier
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
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
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
import dev.ultreon.quantum.client.gui.widget.HorizontalList as _HorizontalList_Entry
_Entry = _HorizontalList_Entry.Entry
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
import dev.ultreon.quantum.client.gui.widget.Widget as _Widget
_Widget = _Widget
import dev.ultreon.quantum.client.gui.Position as _Position
_Position = _Position
import java.util.function.IntSupplier as IntSupplier
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
 
class HorizontalList():
    """dev.ultreon.quantum.client.gui.widget.HorizontalList"""
 
    @staticmethod
    def _wrap(java_value: _HorizontalList) -> 'HorizontalList':
        return HorizontalList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HorizontalList):
        """
        Dynamic initializer for HorizontalList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HorizontalList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HorizontalList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def mouseEnter(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseEnter(int,int)"""
        super(_HorizontalList, self).mouseEnter(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getGap(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getGap()"""
        return int._wrap(super(HorizontalList, self).getGap())

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool._wrap(super(_UIContainer, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @overload
    def entries(self, arg0: 'Collection') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.entries(java.util.Collection<? extends T>)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).entries(arg0))

    @overload
    def entry(self, arg0: 'Entry') -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.entry(T)"""
        return 'Entry'._wrap(super(_HorizontalList, self).entry(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def itemHeight(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.itemHeight(int)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).itemHeight(_int.valueOf(arg0)))

    @overload
    def removeEntry(self, arg0: 'Entry'):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.removeEntry(T)"""
        super(_HorizontalList, self).removeEntry(arg0)

    @overload
    def setXOffset(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.setXOffset(int)"""
        super(_HorizontalList, self).setXOffset(_int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @overload
    def position(self, arg0: 'Supplier') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).position(arg0))

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_HorizontalList, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @overload
    def getSelected(self) -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.getSelected()"""
        return 'Entry'._wrap(super(HorizontalList, self).getSelected())

    @overload
    def scroll(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.scroll(int)"""
        super(_HorizontalList, self).scroll(_int.valueOf(arg0))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def isSelectable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.isSelectable()"""
        return bool._wrap(super(HorizontalList, self).isSelectable())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList()"""
        val = _HorizontalList()
        self.__wrapper = val

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.revalidate()"""
        super(HorizontalList, self).revalidate()

    @overload
    def itemRenderer(self, arg0: 'ItemRenderer') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.itemRenderer(dev.ultreon.quantum.client.gui.widget.HorizontalList$ItemRenderer<T>)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).itemRenderer(arg0))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mousePress(int,int,int)"""
        return bool._wrap(super(_HorizontalList, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList()"""
        val = _HorizontalList()
        self.__wrapper = val

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_HorizontalList, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.children()"""
        return 'List'._wrap(super(HorizontalList, self).children())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getContentHeight()"""
        return int._wrap(super(HorizontalList, self).getContentHeight())

    @overload
    def __init__(self, arg0: 'Size'):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList(dev.ultreon.quantum.client.gui.Size)"""
        val = _HorizontalList(arg0)
        self.__wrapper = val

    @overload
    def selectable(self, arg0: bool) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.selectable(boolean)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).selectable(_boolean.valueOf(arg0)))

    @overload
    def scrollDelta(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.scrollDelta(int)"""
        super(_HorizontalList, self).scrollDelta(_int.valueOf(arg0))

    @overload
    def itemWidth(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.itemWidth(int)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).itemWidth(_int.valueOf(arg0)))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @overload
    def gap(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.gap(int)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).gap(_int.valueOf(arg0)))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool._wrap(super(_UIContainer, self).charType(_char.valueOf(arg0)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseWheel(int,int,double)"""
        return bool._wrap(super(_HorizontalList, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def xOffset(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.xOffset(int)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).xOffset(_int.valueOf(arg0)))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'Widget'._wrap(super(_UIContainer, self).getExactWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'Widget'._wrap(super(_UIContainer, self).getWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(_UIContainer, self).setLayout(arg0)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseRelease(int,int,int)"""
        return bool._wrap(super(_HorizontalList, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseMove(int,int)"""
        super(_HorizontalList, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_UIContainer, self).renderChild(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setGap(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.setGap(int)"""
        super(_HorizontalList, self).setGap(_int.valueOf(arg0))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).bounds(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @overload
    def getItemHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getItemHeight()"""
        return int._wrap(super(HorizontalList, self).getItemHeight())

    @overload
    def callback(self, arg0: 'Callback') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.callback(dev.ultreon.quantum.client.gui.Callback<T>)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).callback(arg0))

    @overload
    def getEntryAt(self, arg0: int, arg1: int) -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.getEntryAt(int,int)"""
        return 'Entry'._wrap(super(_HorizontalList, self).getEntryAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList(int,int)"""
        val = _HorizontalList(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.HorizontalList.getName()"""
        return str._wrap(super(HorizontalList, self).getName())

    @overload
    def count(self, arg0: 'IntSupplier') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.count(java.util.function.IntSupplier)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).count(arg0))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'._wrap(super(UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_UIContainer, self).remove(arg0)

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList(int)"""
        val = _HorizontalList(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @overload
    def removeEntryIf(self, arg0: 'Predicate'):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.removeEntryIf(java.util.function.Predicate<T>)"""
        super(_HorizontalList, self).removeEntryIf(arg0)

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(UIContainer, self).getWidgets())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_HorizontalList, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def mouseExit(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseExit()"""
        super(HorizontalList, self).mouseExit()

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @overload
    def getXOffset(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getXOffset()"""
        return int._wrap(super(HorizontalList, self).getXOffset())

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'._wrap(super(_UIContainer, self).getWidgetsAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_HorizontalList, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def add(self, arg0: 'Widget') -> 'Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'Widget'._wrap(super(_UIContainer, self).add(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyPress(int)"""
        return bool._wrap(super(_UIContainer, self).keyPress(_int.valueOf(arg0)))

    @overload
    def getItemWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getItemWidth()"""
        return int._wrap(super(HorizontalList, self).getItemWidth())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())


UIContainer.ROOT = UIContainer._wrap(_ROOT.ROOT)

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.HorizontalList
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.widget.HorizontalList as _HorizontalList
_HorizontalList = _HorizontalList
import java.util.function.Supplier as Supplier
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
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
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
import dev.ultreon.quantum.client.gui.widget.HorizontalList as _HorizontalList_Entry
_Entry = _HorizontalList_Entry.Entry
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
import dev.ultreon.quantum.client.gui.widget.Widget as _Widget
_Widget = _Widget
import dev.ultreon.quantum.client.gui.Position as _Position
_Position = _Position
import java.util.function.IntSupplier as IntSupplier
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
 
class HorizontalList():
    """dev.ultreon.quantum.client.gui.widget.HorizontalList"""
 
    @staticmethod
    def _wrap(java_value: _HorizontalList) -> 'HorizontalList':
        return HorizontalList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HorizontalList):
        """
        Dynamic initializer for HorizontalList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HorizontalList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HorizontalList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def mouseEnter(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseEnter(int,int)"""
        super(_HorizontalList, self).mouseEnter(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getGap(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getGap()"""
        return int._wrap(super(HorizontalList, self).getGap())

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool._wrap(super(_UIContainer, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @overload
    def entries(self, arg0: 'Collection') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.entries(java.util.Collection<? extends T>)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).entries(arg0))

    @overload
    def entry(self, arg0: 'Entry') -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.entry(T)"""
        return 'Entry'._wrap(super(_HorizontalList, self).entry(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def itemHeight(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.itemHeight(int)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).itemHeight(_int.valueOf(arg0)))

    @overload
    def removeEntry(self, arg0: 'Entry'):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.removeEntry(T)"""
        super(_HorizontalList, self).removeEntry(arg0)

    @overload
    def setXOffset(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.setXOffset(int)"""
        super(_HorizontalList, self).setXOffset(_int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @overload
    def position(self, arg0: 'Supplier') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).position(arg0))

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_HorizontalList, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @overload
    def getSelected(self) -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.getSelected()"""
        return 'Entry'._wrap(super(HorizontalList, self).getSelected())

    @overload
    def scroll(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.scroll(int)"""
        super(_HorizontalList, self).scroll(_int.valueOf(arg0))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def isSelectable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.isSelectable()"""
        return bool._wrap(super(HorizontalList, self).isSelectable())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList()"""
        val = _HorizontalList()
        self.__wrapper = val

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.revalidate()"""
        super(HorizontalList, self).revalidate()

    @overload
    def itemRenderer(self, arg0: 'ItemRenderer') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.itemRenderer(dev.ultreon.quantum.client.gui.widget.HorizontalList$ItemRenderer<T>)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).itemRenderer(arg0))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mousePress(int,int,int)"""
        return bool._wrap(super(_HorizontalList, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList()"""
        val = _HorizontalList()
        self.__wrapper = val

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_HorizontalList, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.children()"""
        return 'List'._wrap(super(HorizontalList, self).children())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getContentHeight()"""
        return int._wrap(super(HorizontalList, self).getContentHeight())

    @overload
    def __init__(self, arg0: 'Size'):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList(dev.ultreon.quantum.client.gui.Size)"""
        val = _HorizontalList(arg0)
        self.__wrapper = val

    @overload
    def selectable(self, arg0: bool) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.selectable(boolean)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).selectable(_boolean.valueOf(arg0)))

    @overload
    def scrollDelta(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.scrollDelta(int)"""
        super(_HorizontalList, self).scrollDelta(_int.valueOf(arg0))

    @overload
    def itemWidth(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.itemWidth(int)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).itemWidth(_int.valueOf(arg0)))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @overload
    def gap(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.gap(int)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).gap(_int.valueOf(arg0)))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool._wrap(super(_UIContainer, self).charType(_char.valueOf(arg0)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseWheel(int,int,double)"""
        return bool._wrap(super(_HorizontalList, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def xOffset(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.xOffset(int)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).xOffset(_int.valueOf(arg0)))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'Widget'._wrap(super(_UIContainer, self).getExactWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'Widget'._wrap(super(_UIContainer, self).getWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(_UIContainer, self).setLayout(arg0)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseRelease(int,int,int)"""
        return bool._wrap(super(_HorizontalList, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseMove(int,int)"""
        super(_HorizontalList, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_UIContainer, self).renderChild(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setGap(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.setGap(int)"""
        super(_HorizontalList, self).setGap(_int.valueOf(arg0))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).bounds(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @overload
    def getItemHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getItemHeight()"""
        return int._wrap(super(HorizontalList, self).getItemHeight())

    @overload
    def callback(self, arg0: 'Callback') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.callback(dev.ultreon.quantum.client.gui.Callback<T>)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).callback(arg0))

    @overload
    def getEntryAt(self, arg0: int, arg1: int) -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.getEntryAt(int,int)"""
        return 'Entry'._wrap(super(_HorizontalList, self).getEntryAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList(int,int)"""
        val = _HorizontalList(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.HorizontalList.getName()"""
        return str._wrap(super(HorizontalList, self).getName())

    @overload
    def count(self, arg0: 'IntSupplier') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.count(java.util.function.IntSupplier)"""
        return 'HorizontalList'._wrap(super(_HorizontalList, self).count(arg0))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'._wrap(super(UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_UIContainer, self).remove(arg0)

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList(int)"""
        val = _HorizontalList(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @overload
    def removeEntryIf(self, arg0: 'Predicate'):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.removeEntryIf(java.util.function.Predicate<T>)"""
        super(_HorizontalList, self).removeEntryIf(arg0)

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(UIContainer, self).getWidgets())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_HorizontalList, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def mouseExit(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseExit()"""
        super(HorizontalList, self).mouseExit()

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @overload
    def getXOffset(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getXOffset()"""
        return int._wrap(super(HorizontalList, self).getXOffset())

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'._wrap(super(_UIContainer, self).getWidgetsAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_HorizontalList, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def add(self, arg0: 'Widget') -> 'Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'Widget'._wrap(super(_UIContainer, self).add(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyPress(int)"""
        return bool._wrap(super(_UIContainer, self).keyPress(_int.valueOf(arg0)))

    @overload
    def getItemWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getItemWidth()"""
        return int._wrap(super(HorizontalList, self).getItemWidth())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())


UIContainer.ROOT = UIContainer._wrap(_ROOT.ROOT)

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.HorizontalList 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Panel
from pyquantum_helper import import_once as _import_once
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
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
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
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
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
import dev.ultreon.quantum.client.gui.widget.Panel as _Panel
_Panel = _Panel
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Panel():
    """dev.ultreon.quantum.client.gui.widget.Panel"""
 
    @staticmethod
    def _wrap(java_value: _Panel) -> 'Panel':
        return Panel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Panel):
        """
        Dynamic initializer for Panel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Panel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Panel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.widget.Panel(int,int,int,int)"""
        val = _Panel(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Panel.getName()"""
        return str._wrap(super(Panel, self).getName())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def create() -> 'Panel':
        """public static dev.ultreon.quantum.client.gui.widget.Panel dev.ultreon.quantum.client.gui.widget.Panel.create()"""
        return Panel._wrap(_Panel.create())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Panel':
        """public dev.ultreon.quantum.client.gui.widget.Panel dev.ultreon.quantum.client.gui.widget.Panel.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Panel'._wrap(super(_Panel, self).bounds(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @overload
    def position(self, arg0: 'Supplier') -> 'Panel':
        """public dev.ultreon.quantum.client.gui.widget.Panel dev.ultreon.quantum.client.gui.widget.Panel.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Panel'._wrap(super(_Panel, self).position(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool._wrap(super(_Widget, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.Panel()"""
        val = _Panel()
        self.__wrapper = val

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Panel.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Panel, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.Panel()"""
        val = _Panel()
        self.__wrapper = val

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def of(arg0: int, arg1: int, arg2: int, arg3: int) -> 'Panel':
        """public static dev.ultreon.quantum.client.gui.widget.Panel dev.ultreon.quantum.client.gui.widget.Panel.of(int,int,int,int)"""
        return Panel._wrap(_Panel.of(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.UIContainer
from pyquantum_helper import import_once as _import_once
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
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
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
 
class UIContainer():
    """dev.ultreon.quantum.client.gui.widget.UIContainer"""
 
    @staticmethod
    def _wrap(java_value: _UIContainer) -> 'UIContainer':
        return UIContainer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UIContainer):
        """
        Dynamic initializer for UIContainer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UIContainer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UIContainer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool._wrap(super(_UIContainer, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'._wrap(super(UIContainer, self).getLayout())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.widget.UIContainer(int,int)"""
        val = _UIContainer(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'._wrap(super(UIContainer, self).children())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_UIContainer, self).renderChild(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'UIContainer'._wrap(super(_UIContainer, self).bounds(arg0))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_UIContainer, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_UIContainer, self).remove(arg0)

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def position(self, arg0: 'Supplier') -> 'UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'UIContainer'._wrap(super(_UIContainer, self).position(arg0))

    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(UIContainer, self).getWidgets())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool._wrap(super(_UIContainer, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_UIContainer, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(_UIContainer, self).setLayout(arg0)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.UIContainer.getName()"""
        return str._wrap(super(UIContainer, self).getName())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.revalidate()"""
        super(UIContainer, self).revalidate()

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'._wrap(super(_UIContainer, self).getWidgetsAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

    @overload
    def add(self, arg0: 'Widget') -> 'Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'Widget'._wrap(super(_UIContainer, self).add(arg0))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'Widget'._wrap(super(_UIContainer, self).getExactWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyPress(int)"""
        return bool._wrap(super(_UIContainer, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.mouseMove(int,int)"""
        super(_UIContainer, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mouseRelease(int,int,int)"""
        return bool._wrap(super(_UIContainer, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'Widget'._wrap(super(_UIContainer, self).getWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mouseWheel(int,int,double)"""
        return bool._wrap(super(_UIContainer, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_UIContainer, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mousePress(int,int,int)"""
        return bool._wrap(super(_UIContainer, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))


UIContainer.ROOT = UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = _import_once("pyquantum.client.gui.widget.components")

import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
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
import java.nio.file.Path as Path
import dev.ultreon.quantum.client.gui.widget.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel as _WorldGenTestPanel
_WorldGenTestPanel = _WorldGenTestPanel
import dev.ultreon.quantum.client.gui.widget.components.ColorComponent as _ColorComponent
_ColorComponent = _ColorComponent
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
import dev.ultreon.quantum.world.TerrainNoise as _TerrainNoise
_TerrainNoise = _TerrainNoise
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldGenTestPanel():
    """dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel"""
 
    @staticmethod
    def _wrap(java_value: _WorldGenTestPanel) -> 'WorldGenTestPanel':
        return WorldGenTestPanel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldGenTestPanel):
        """
        Dynamic initializer for WorldGenTestPanel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldGenTestPanel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldGenTestPanel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Rectangle':
        """public dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).bounds(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel()"""
        val = _WorldGenTestPanel()
        self.__wrapper = val

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def random(self):
        """public void dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.random()"""
        super(WorldGenTestPanel, self).random()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Rectangle.getName()"""
        return str._wrap(super(Rectangle, self).getName())

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def backgroundColor(self, arg0: 'RgbColor') -> 'Rectangle':
        """public dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.backgroundColor(dev.ultreon.quantum.util.RgbColor)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).backgroundColor(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def backgroundColor(self) -> 'components.ColorComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.ColorComponent dev.ultreon.quantum.client.gui.widget.Rectangle.backgroundColor()"""
        return 'components.ColorComponent'._wrap(super(Rectangle, self).backgroundColor())

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @overload
    def getTerrainNoise(self) -> 'world.TerrainNoise':
        """public dev.ultreon.quantum.world.TerrainNoise dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.getTerrainNoise()"""
        return 'world.TerrainNoise'._wrap(super(WorldGenTestPanel, self).getTerrainNoise())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @overload
    def position(self, arg0: 'Supplier') -> 'Rectangle':
        """public dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).position(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mousePress(int,int,int)"""
        return bool._wrap(super(_Rectangle, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.mouseWheel(int,int,double)"""
        return bool._wrap(super(_WorldGenTestPanel, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @staticmethod
    @overload
    def of(arg0: int, arg1: int, arg2: int, arg3: int) -> 'Rectangle':
        """public static dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.of(int,int,int,int)"""
        return Rectangle._wrap(_Rectangle.of(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.charType(char)"""
        return bool._wrap(super(_WorldGenTestPanel, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @staticmethod
    @overload
    def create() -> 'WorldGenTestPanel':
        """public static dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.create()"""
        return WorldGenTestPanel._wrap(_WorldGenTestPanel.create())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Rectangle, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.dispose()"""
        super(WorldGenTestPanel, self).dispose()

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_WorldGenTestPanel, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel()"""
        val = _WorldGenTestPanel()
        self.__wrapper = val

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @staticmethod
    @overload
    def create() -> 'Rectangle':
        """public static dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.create()"""
        return Rectangle._wrap(_Rectangle.create())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Rectangle, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.HorizontalList$ItemRenderer
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.widget.HorizontalList as _HorizontalList_ItemRenderer
_ItemRenderer = _HorizontalList_ItemRenderer.ItemRenderer
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class ItemRenderer():
    """dev.ultreon.quantum.client.gui.widget.HorizontalList.ItemRenderer"""
 
    @staticmethod
    def _wrap(java_value: _ItemRenderer) -> 'ItemRenderer':
        return ItemRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemRenderer):
        """
        Dynamic initializer for ItemRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def render(self, arg0: 'Renderer', arg1: object, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool, arg7: float):
        """public abstract void dev.ultreon.quantum.client.gui.widget.HorizontalList$ItemRenderer.render(dev.ultreon.quantum.client.gui.Renderer,T,int,int,int,int,boolean,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.ScrollableContainer
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
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
import java.util.Collection as Collection
import dev.ultreon.quantum.util.RgbColor as _RgbColor
_RgbColor = _RgbColor
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
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
 
class ScrollableContainer():
    """dev.ultreon.quantum.client.gui.widget.ScrollableContainer"""
 
    @staticmethod
    def _wrap(java_value: _ScrollableContainer) -> 'ScrollableContainer':
        return ScrollableContainer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScrollableContainer):
        """
        Dynamic initializer for ScrollableContainer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScrollableContainer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScrollableContainer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.ScrollableContainer.getWidgetAt(int,int)"""
        return 'Widget'._wrap(super(_ScrollableContainer, self).getWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool._wrap(super(_UIContainer, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @overload
    def backgroundColor(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.gui.widget.ScrollableContainer.backgroundColor()"""
        return 'util.RgbColor'._wrap(super(ScrollableContainer, self).backgroundColor())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mousePress(int,int,int)"""
        return bool._wrap(super(_ScrollableContainer, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def removeWidgetIf(self, arg0: 'Predicate'):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.removeWidgetIf(java.util.function.Predicate<dev.ultreon.quantum.client.gui.widget.Widget>)"""
        super(_ScrollableContainer, self).removeWidgetIf(arg0)

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_UIContainer, self).renderChild(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_ScrollableContainer, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseMove(int,int)"""
        super(_ScrollableContainer, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_ScrollableContainer, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def isSelectable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.isSelectable()"""
        return bool._wrap(super(ScrollableContainer, self).isSelectable())

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def backgroundColor(self, arg0: 'RgbColor') -> 'ScrollableContainer':
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer dev.ultreon.quantum.client.gui.widget.ScrollableContainer.backgroundColor(dev.ultreon.quantum.util.RgbColor)"""
        return 'ScrollableContainer'._wrap(super(_ScrollableContainer, self).backgroundColor(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer()"""
        val = _ScrollableContainer()
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.ScrollableContainer.getName()"""
        return str._wrap(super(ScrollableContainer, self).getName())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Size'):
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer(dev.ultreon.quantum.client.gui.Size)"""
        val = _ScrollableContainer(arg0)
        self.__wrapper = val

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def mouseExit(self):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseExit()"""
        super(ScrollableContainer, self).mouseExit()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'._wrap(super(UIContainer, self).children())

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'._wrap(super(UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_ScrollableContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_UIContainer, self).remove(arg0)

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_UIContainer, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(UIContainer, self).getWidgets())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer()"""
        val = _ScrollableContainer()
        self.__wrapper = val

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @overload
    def mouseEnter(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseEnter(int,int)"""
        super(_ScrollableContainer, self).mouseEnter(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'ScrollableContainer':
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer dev.ultreon.quantum.client.gui.widget.ScrollableContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'ScrollableContainer'._wrap(super(_ScrollableContainer, self).bounds(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.ScrollableContainer.getContentHeight()"""
        return int._wrap(super(ScrollableContainer, self).getContentHeight())

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseWheel(int,int,double)"""
        return bool._wrap(super(_ScrollableContainer, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool._wrap(super(_UIContainer, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def selectable(self, arg0: bool) -> 'ScrollableContainer':
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer dev.ultreon.quantum.client.gui.widget.ScrollableContainer.selectable(boolean)"""
        return 'ScrollableContainer'._wrap(super(_ScrollableContainer, self).selectable(_boolean.valueOf(arg0)))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseRelease(int,int,int)"""
        return bool._wrap(super(_ScrollableContainer, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.revalidate()"""
        super(UIContainer, self).revalidate()

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'._wrap(super(_UIContainer, self).getWidgetsAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer(int,int)"""
        val = _ScrollableContainer(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def add(self, arg0: 'Widget') -> 'Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'Widget'._wrap(super(_UIContainer, self).add(arg0))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'Widget'._wrap(super(_UIContainer, self).getExactWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyPress(int)"""
        return bool._wrap(super(_UIContainer, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(_UIContainer, self).setLayout(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())

    @overload
    def position(self, arg0: 'Supplier') -> 'ScrollableContainer':
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer dev.ultreon.quantum.client.gui.widget.ScrollableContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'ScrollableContainer'._wrap(super(_ScrollableContainer, self).position(arg0))

    @overload
    def removeWidget(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.removeWidget(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_ScrollableContainer, self).removeWidget(arg0)


UIContainer.ROOT = UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.SelectionList
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
import java.util.function.Predicate as Predicate
import dev.ultreon.quantum.client.gui.widget.SelectionList as _SelectionList_Entry
_Entry = _SelectionList_Entry.Entry
import java.lang.Double as _double
import java.lang.Character as _char
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
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
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
from builtins import object
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
 
class SelectionList():
    """dev.ultreon.quantum.client.gui.widget.SelectionList"""
 
    @staticmethod
    def _wrap(java_value: _SelectionList) -> 'SelectionList':
        return SelectionList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SelectionList):
        """
        Dynamic initializer for SelectionList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SelectionList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SelectionList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool._wrap(super(_UIContainer, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T>> dev.ultreon.quantum.client.gui.widget.SelectionList.children()"""
        return 'List'._wrap(super(SelectionList, self).children())

    @overload
    def entries(self, arg0: 'Collection') -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.entries(java.util.Collection<? extends T>)"""
        return 'SelectionList'._wrap(super(_SelectionList, self).entries(arg0))

    @overload
    def isSelectable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.isSelectable()"""
        return bool._wrap(super(SelectionList, self).isSelectable())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @overload
    def __init__(self, arg0: 'Position', arg1: 'Size'):
        """public dev.ultreon.quantum.client.gui.widget.SelectionList(dev.ultreon.quantum.client.gui.Position,dev.ultreon.quantum.client.gui.Size)"""
        val = _SelectionList(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def removeEntryIf(self, arg0: 'Predicate'):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.removeEntryIf(java.util.function.Predicate<T>)"""
        super(_SelectionList, self).removeEntryIf(arg0)

    @overload
    def getEntryAt(self, arg0: int, arg1: int) -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T> dev.ultreon.quantum.client.gui.widget.SelectionList.getEntryAt(int,int)"""
        return 'Entry'._wrap(super(_SelectionList, self).getEntryAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @overload
    def itemHeight(self, arg0: int) -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.itemHeight(int)"""
        return 'SelectionList'._wrap(super(_SelectionList, self).itemHeight(_int.valueOf(arg0)))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.SelectionList()"""
        val = _SelectionList()
        self.__wrapper = val

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def removeEntry(self, arg0: 'Entry') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T> dev.ultreon.quantum.client.gui.widget.SelectionList.removeEntry(dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T>)"""
        return 'Entry'._wrap(super(_SelectionList, self).removeEntry(arg0))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_SelectionList, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.mousePress(int,int,int)"""
        return bool._wrap(super(_SelectionList, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @overload
    def mouseExit(self):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.mouseExit()"""
        super(SelectionList, self).mouseExit()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def isDrawBackground(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.isDrawBackground()"""
        return bool._wrap(super(SelectionList, self).isDrawBackground())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool._wrap(super(_UIContainer, self).charType(_char.valueOf(arg0)))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.mouseRelease(int,int,int)"""
        return bool._wrap(super(_SelectionList, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.widget.SelectionList(int)"""
        val = _SelectionList(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.revalidate()"""
        super(UIContainer, self).revalidate()

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_SelectionList, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.mouseWheel(int,int,double)"""
        return bool._wrap(super(_SelectionList, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def getItemHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.SelectionList.getItemHeight()"""
        return int._wrap(super(SelectionList, self).getItemHeight())

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'Widget'._wrap(super(_UIContainer, self).getExactWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.mouseMove(int,int)"""
        super(_SelectionList, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'Widget'._wrap(super(_UIContainer, self).getWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(_UIContainer, self).setLayout(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @overload
    def getGap(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.SelectionList.getGap()"""
        return int._wrap(super(SelectionList, self).getGap())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def itemRenderer(self, arg0: 'ItemRenderer') -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.itemRenderer(dev.ultreon.quantum.client.gui.widget.SelectionList$ItemRenderer<T>)"""
        return 'SelectionList'._wrap(super(_SelectionList, self).itemRenderer(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_UIContainer, self).renderChild(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_SelectionList, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def selectable(self, arg0: bool) -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.selectable(boolean)"""
        return 'SelectionList'._wrap(super(_SelectionList, self).selectable(_boolean.valueOf(arg0)))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_SelectionList, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def getSelected(self) -> object:
        """public T dev.ultreon.quantum.client.gui.widget.SelectionList.getSelected()"""
        return object._wrap(super(SelectionList, self).getSelected())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.widget.SelectionList(int,int,int,int)"""
        val = _SelectionList(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @overload
    def bounds(self, arg0: 'Supplier') -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'SelectionList'._wrap(super(_SelectionList, self).bounds(arg0))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'._wrap(super(UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @overload
    def position(self, arg0: 'Supplier') -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'SelectionList'._wrap(super(_SelectionList, self).position(arg0))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_UIContainer, self).remove(arg0)

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(UIContainer, self).getWidgets())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.SelectionList.getName()"""
        return str._wrap(super(SelectionList, self).getName())

    @overload
    def mouseEnter(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.mouseEnter(int,int)"""
        super(_SelectionList, self).mouseEnter(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @overload
    def removeEntry(self, arg0: object):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.removeEntry(T)"""
        super(_SelectionList, self).removeEntry(arg0)

    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.SelectionList.getContentHeight()"""
        return int._wrap(super(SelectionList, self).getContentHeight())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @overload
    def entry(self, arg0: object) -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T> dev.ultreon.quantum.client.gui.widget.SelectionList.entry(T)"""
        return 'Entry'._wrap(super(_SelectionList, self).entry(arg0))

    @overload
    def drawBackground(self, arg0: bool) -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.drawBackground(boolean)"""
        return 'SelectionList'._wrap(super(_SelectionList, self).drawBackground(_boolean.valueOf(arg0)))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'._wrap(super(_UIContainer, self).getWidgetsAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

    @overload
    def add(self, arg0: 'Widget') -> 'Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'Widget'._wrap(super(_UIContainer, self).add(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyPress(int)"""
        return bool._wrap(super(_UIContainer, self).keyPress(_int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.SelectionList()"""
        val = _SelectionList()
        self.__wrapper = val

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())

    @overload
    def callback(self, arg0: 'Callback') -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.callback(dev.ultreon.quantum.client.gui.Callback<T>)"""
        return 'SelectionList'._wrap(super(_SelectionList, self).callback(arg0))


UIContainer.ROOT = UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.IconButton
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = _import_once("pyquantum.client.gui.widget.components")

import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import java.util.Collection as Collection
try:
    from pyquantum.client.gui import icon
except ImportError:
    icon = _import_once("pyquantum.client.gui.icon")

import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
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
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.Button as _Button
_Button = _Button
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as _CallbackComponent
_CallbackComponent = _CallbackComponent
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
import dev.ultreon.quantum.client.gui.widget.Button as _Button_Type
_Type = _Button_Type.Type
import dev.ultreon.quantum.client.gui.widget.IconButton as _IconButton
_IconButton = _IconButton
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IconButton():
    """dev.ultreon.quantum.client.gui.widget.IconButton"""
 
    @staticmethod
    def _wrap(java_value: _IconButton) -> 'IconButton':
        return IconButton(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IconButton):
        """
        Dynamic initializer for IconButton.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IconButton__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IconButton__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button.type()"""
        return 'Type'._wrap(super(Button, self).type())

    @overload
    def callback(self, arg0: 'Callback') -> 'IconButton':
        """public dev.ultreon.quantum.client.gui.widget.IconButton dev.ultreon.quantum.client.gui.widget.IconButton.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.IconButton>)"""
        return 'IconButton'._wrap(super(_IconButton, self).callback(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.isPressed()"""
        return bool._wrap(super(Button, self).isPressed())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def position(self, arg0: 'Supplier') -> 'IconButton':
        """public dev.ultreon.quantum.client.gui.widget.IconButton dev.ultreon.quantum.client.gui.widget.IconButton.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'IconButton'._wrap(super(_IconButton, self).position(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @overload
    def bounds(self, arg0: 'Supplier') -> 'IconButton':
        """public dev.ultreon.quantum.client.gui.widget.IconButton dev.ultreon.quantum.client.gui.widget.IconButton.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'IconButton'._wrap(super(_IconButton, self).bounds(arg0))

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<T> dev.ultreon.quantum.client.gui.widget.Button.callback()"""
        return 'components.CallbackComponent'._wrap(super(Button, self).callback())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Button, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str._wrap(super(Widget, self).getName())

    @override
    @overload
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.click()"""
        return bool._wrap(super(Button, self).click())

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @overload
    def type(self, arg0: 'Type') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.type(dev.ultreon.quantum.client.gui.widget.Button$Type)"""
        return 'Button'._wrap(super(_Button, self).type(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mousePress(int,int,int)"""
        return bool._wrap(super(_Button, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def of(arg0: 'Icon') -> 'IconButton':
        """public static dev.ultreon.quantum.client.gui.widget.IconButton dev.ultreon.quantum.client.gui.widget.IconButton.of(dev.ultreon.quantum.client.gui.icon.Icon)"""
        return IconButton._wrap(_IconButton.of(arg0))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Button, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.IconButton.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_IconButton, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.ChatTextEntry
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = _import_once("pyquantum.client.gui.widget.components")

import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as _TextComponent
_TextComponent = _TextComponent
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import it.unimi.dsi.fastutil.chars.CharPredicate as _CharPredicate
_CharPredicate = _CharPredicate
import dev.ultreon.quantum.client.gui.widget.ChatTextEntry as _ChatTextEntry
_ChatTextEntry = _ChatTextEntry
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.gui.screens.ChatScreen as _ChatScreen
_ChatScreen = _ChatScreen
import dev.ultreon.quantum.client.gui.widget.TextEntry as _TextEntry
_TextEntry = _TextEntry
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
    from pyquantum.client.gui import screens
except ImportError:
    screens = _import_once("pyquantum.client.gui.screens")

import it.unimi.dsi.fastutil.chars.CharPredicate as CharPredicate
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as _CallbackComponent
_CallbackComponent = _CallbackComponent
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
import java.lang.Class as _Class
_Class = _Class
 
class ChatTextEntry():
    """dev.ultreon.quantum.client.gui.widget.ChatTextEntry"""
 
    @staticmethod
    def _wrap(java_value: _ChatTextEntry) -> 'ChatTextEntry':
        return ChatTextEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChatTextEntry):
        """
        Dynamic initializer for ChatTextEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChatTextEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChatTextEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def position(self, arg0: 'Supplier') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'TextEntry'._wrap(super(_TextEntry, self).position(arg0))

    @override
    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<dev.ultreon.quantum.client.gui.widget.TextEntry> dev.ultreon.quantum.client.gui.widget.TextEntry.callback()"""
        return 'components.CallbackComponent'._wrap(super(TextEntry, self).callback())

    @override
    @overload
    def revalidateCursor(self):
        """public void dev.ultreon.quantum.client.gui.widget.TextEntry.revalidateCursor()"""
        super(TextEntry, self).revalidateCursor()

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @staticmethod
    @overload
    def of(arg0: str) -> 'TextEntry':
        """public static dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.of(java.lang.String)"""
        return TextEntry._wrap(_TextEntry.of(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def getFilter(self) -> 'CharPredicate':
        """public it.unimi.dsi.fastutil.chars.CharPredicate dev.ultreon.quantum.client.gui.widget.TextEntry.getFilter()"""
        return 'CharPredicate'._wrap(super(TextEntry, self).getFilter())

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @overload
    def getScreen(self) -> 'screens.ChatScreen':
        """public dev.ultreon.quantum.client.gui.screens.ChatScreen dev.ultreon.quantum.client.gui.widget.ChatTextEntry.getScreen()"""
        return 'screens.ChatScreen'._wrap(super(ChatTextEntry, self).getScreen())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.ChatTextEntry.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_ChatTextEntry, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def value(self, arg0: str) -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.value(java.lang.String)"""
        return 'TextEntry'._wrap(super(_TextEntry, self).value(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @overload
    def __init__(self, arg0: 'ChatScreen'):
        """public dev.ultreon.quantum.client.gui.widget.ChatTextEntry(dev.ultreon.quantum.client.gui.screens.ChatScreen)"""
        val = _ChatTextEntry(arg0)
        self.__wrapper = val

    @overload
    def callback(self, arg0: 'Callback') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.TextEntry>)"""
        return 'TextEntry'._wrap(super(_TextEntry, self).callback(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ChatTextEntry.keyPress(int)"""
        return bool._wrap(super(_ChatTextEntry, self).keyPress(_int.valueOf(arg0)))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.TextEntry.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Widget'._wrap(super(_TextEntry, self).bounds(arg0))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ChatTextEntry.charType(char)"""
        return bool._wrap(super(_ChatTextEntry, self).charType(_char.valueOf(arg0)))

    @overload
    def onTabComplete(self, arg0: 'String'):
        """public void dev.ultreon.quantum.client.gui.widget.ChatTextEntry.onTabComplete(java.lang.String[])"""
        super(_ChatTextEntry, self).onTabComplete(arg0)

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def hint(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.TextEntry.hint()"""
        return 'components.TextComponent'._wrap(super(TextEntry, self).hint())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @staticmethod
    @overload
    def of() -> 'TextEntry':
        """public static dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.of()"""
        return TextEntry._wrap(_TextEntry.of())

    @override
    @overload
    def getCursorIdx(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.TextEntry.getCursorIdx()"""
        return int._wrap(super(TextEntry, self).getCursorIdx())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool._wrap(super(_Widget, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def filter(self, arg0: 'CharPredicate') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.filter(it.unimi.dsi.fastutil.chars.CharPredicate)"""
        return 'TextEntry'._wrap(super(_TextEntry, self).filter(arg0))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @override
    @overload
    def setCursorIdx(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.TextEntry.setCursorIdx(int)"""
        super(_TextEntry, self).setCursorIdx(_int.valueOf(arg0))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def hint(self, arg0: 'TextObject') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.hint(dev.ultreon.quantum.text.TextObject)"""
        return 'TextEntry'._wrap(super(_TextEntry, self).hint(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TextEntry.getName()"""
        return str._wrap(super(TextEntry, self).getName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.ChatTextEntry.onFocusLost()"""
        super(ChatTextEntry, self).onFocusLost()

    @override
    @overload
    def getValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TextEntry.getValue()"""
        return str._wrap(super(TextEntry, self).getValue())

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Slider
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = _import_once("pyquantum.client.gui.widget.components")

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
import dev.ultreon.quantum.client.gui.widget.Slider as _Slider
_Slider = _Slider
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as _TextComponent
_TextComponent = _TextComponent
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
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
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent as _RangedValueComponent
_RangedValueComponent = _RangedValueComponent
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as _CallbackComponent
_CallbackComponent = _CallbackComponent
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
import java.lang.Class as _Class
_Class = _Class
 
class Slider():
    """dev.ultreon.quantum.client.gui.widget.Slider"""
 
    @staticmethod
    def _wrap(java_value: _Slider) -> 'Slider':
        return Slider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Slider):
        """
        Dynamic initializer for Slider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Slider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Slider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Slider.mousePress(int,int,int)"""
        return bool._wrap(super(_Slider, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<dev.ultreon.quantum.client.gui.widget.Slider> dev.ultreon.quantum.client.gui.widget.Slider.callback()"""
        return 'components.CallbackComponent'._wrap(super(Slider, self).callback())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Slider.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Slider, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Slider':
        """public dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Slider'._wrap(super(_Slider, self).bounds(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def text(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.Slider.text()"""
        return 'components.TextComponent'._wrap(super(Slider, self).text())

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.gui.widget.Slider(int,int,int)"""
        val = _Slider(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @overload
    def position(self, arg0: 'Supplier') -> 'Slider':
        """public dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Slider'._wrap(super(_Slider, self).position(arg0))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Slider.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Slider, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.widget.Slider(int,int,int,int)"""
        val = _Slider(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @overload
    def value(self) -> 'components.RangedValueComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent dev.ultreon.quantum.client.gui.widget.Slider.value()"""
        return 'components.RangedValueComponent'._wrap(super(Slider, self).value())

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @overload
    def callback(self, arg0: 'Callback') -> 'Slider':
        """public dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.Slider>)"""
        return 'Slider'._wrap(super(_Slider, self).callback(arg0))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @overload
    def value(self, arg0: int) -> 'Slider':
        """public dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.value(int)"""
        return 'Slider'._wrap(super(_Slider, self).value(_int.valueOf(arg0)))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def text(self, arg0: str) -> 'Slider':
        """public dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.text(java.lang.String)"""
        return 'Slider'._wrap(super(_Slider, self).text(arg0))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str._wrap(super(Widget, self).getName())

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @overload
    def text(self, arg0: 'TextObject') -> 'Slider':
        """public dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.text(dev.ultreon.quantum.text.TextObject)"""
        return 'Slider'._wrap(super(_Slider, self).text(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @staticmethod
    @overload
    def of(arg0: int, arg1: int) -> 'Slider':
        """public static dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.of(int,int)"""
        return Slider._wrap(_Slider.of(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def of(arg0: int, arg1: int, arg2: int) -> 'Slider':
        """public static dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.of(int,int,int)"""
        return Slider._wrap(_Slider.of(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.TabCompletePopup
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import dev.ultreon.quantum.client.gui.widget.TabCompletePopup as _TabCompletePopup
_TabCompletePopup = _TabCompletePopup
import java.lang.Integer as _int
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TabCompletePopup():
    """dev.ultreon.quantum.client.gui.widget.TabCompletePopup"""
 
    @staticmethod
    def _wrap(java_value: _TabCompletePopup) -> 'TabCompletePopup':
        return TabCompletePopup(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TabCompletePopup):
        """
        Dynamic initializer for TabCompletePopup.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TabCompletePopup__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TabCompletePopup__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.TabCompletePopup.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_TabCompletePopup, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def up(self):
        """public void dev.ultreon.quantum.client.gui.widget.TabCompletePopup.up()"""
        super(TabCompletePopup, self).up()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setValues(self, arg0: 'String'):
        """public void dev.ultreon.quantum.client.gui.widget.TabCompletePopup.setValues(java.lang.String[])"""
        super(_TabCompletePopup, self).setValues(arg0)

    @overload
    def down(self):
        """public void dev.ultreon.quantum.client.gui.widget.TabCompletePopup.down()"""
        super(TabCompletePopup, self).down()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.widget.TabCompletePopup(int,int)"""
        val = _TabCompletePopup(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def get(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TabCompletePopup.get()"""
        return str._wrap(super(TabCompletePopup, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Tab
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = _import_once("pyquantum.client.gui.widget.components")

import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.screens.tabs.TabContent as _TabContent
_TabContent = _TabContent
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.gui.Screen as _Screen
_Screen = _Screen
try:
    from pyquantum import component
except ImportError:
    component = _import_once("pyquantum.component")

import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
import dev.ultreon.quantum.client.gui.widget.Tab as _Tab
_Tab = _Tab
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.Button as _Button
_Button = _Button
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as _CallbackComponent
_CallbackComponent = _CallbackComponent
try:
    from pyquantum.client.gui.screens import tabs
except ImportError:
    tabs = _import_once("pyquantum.client.gui.screens.tabs")

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
import dev.ultreon.quantum.client.gui.widget.Button as _Button_Type
_Type = _Button_Type.Type
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Tab():
    """dev.ultreon.quantum.client.gui.widget.Tab"""
 
    @staticmethod
    def _wrap(java_value: _Tab) -> 'Tab':
        return Tab(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Tab):
        """
        Dynamic initializer for Tab.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Tab__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Tab__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def bottom(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Tab.bottom()"""
        return bool._wrap(super(Tab, self).bottom())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button.type()"""
        return 'Type'._wrap(super(Button, self).type())

    @overload
    def selected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Tab.selected()"""
        return bool._wrap(super(Tab, self).selected())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.isPressed()"""
        return bool._wrap(super(Button, self).isPressed())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Tab':
        """public dev.ultreon.quantum.client.gui.widget.Tab dev.ultreon.quantum.client.gui.widget.Tab.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Tab'._wrap(super(_Tab, self).bounds(arg0))

    @overload
    def callback(self, arg0: 'Callback') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.callback(dev.ultreon.quantum.client.gui.Callback<T>)"""
        return 'Button'._wrap(super(_Button, self).callback(arg0))

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Tab.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Tab, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def title(self, arg0: 'TextObject') -> 'Tab':
        """public dev.ultreon.quantum.client.gui.widget.Tab dev.ultreon.quantum.client.gui.widget.Tab.title(dev.ultreon.quantum.text.TextObject)"""
        return 'Tab'._wrap(super(_Tab, self).title(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @overload
    def position(self, arg0: 'Supplier') -> 'Tab':
        """public dev.ultreon.quantum.client.gui.widget.Tab dev.ultreon.quantum.client.gui.widget.Tab.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Tab'._wrap(super(_Tab, self).position(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def __init__(self, arg0: 'TextObject', arg1: 'TabbedUI', arg2: bool, arg3: int, arg4: 'Consumer'):
        """public dev.ultreon.quantum.client.gui.widget.Tab(dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI,boolean,int,java.util.function.Consumer<dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder>)"""
        val = _Tab(arg0, arg1, _boolean.valueOf(arg2), _int.valueOf(arg3), arg4)
        self.__wrapper = val

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @overload
    def icon(self, arg0: 'Identifier') -> 'Tab':
        """public dev.ultreon.quantum.client.gui.widget.Tab dev.ultreon.quantum.client.gui.widget.Tab.icon(dev.ultreon.quantum.util.Identifier)"""
        return 'Tab'._wrap(super(_Tab, self).icon(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def index(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Tab.index()"""
        return int._wrap(super(Tab, self).index())

    @overload
    def title(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.widget.Tab.title()"""
        return 'text.TextObject'._wrap(super(Tab, self).title())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Tab.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Tab, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<T> dev.ultreon.quantum.client.gui.widget.Button.callback()"""
        return 'components.CallbackComponent'._wrap(super(Button, self).callback())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Button, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @overload
    def content(self) -> 'tabs.TabContent':
        """public dev.ultreon.quantum.client.gui.screens.tabs.TabContent dev.ultreon.quantum.client.gui.widget.Tab.content()"""
        return 'tabs.TabContent'._wrap(super(Tab, self).content())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str._wrap(super(Widget, self).getName())

    @overload
    def name(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.widget.Tab.name()"""
        return 'text.TextObject'._wrap(super(Tab, self).name())

    @override
    @overload
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.click()"""
        return bool._wrap(super(Button, self).click())

    @overload
    def screen(self) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.widget.Tab.screen()"""
        return 'gui.Screen'._wrap(super(Tab, self).screen())

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @overload
    def type(self, arg0: 'Type') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.type(dev.ultreon.quantum.client.gui.widget.Button$Type)"""
        return 'Button'._wrap(super(_Button, self).type(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mousePress(int,int,int)"""
        return bool._wrap(super(_Button, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Tab.revalidate()"""
        super(Tab, self).revalidate()

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Button
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = _import_once("pyquantum.client.gui.widget.components")

import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
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
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.Button as _Button
_Button = _Button
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as _CallbackComponent
_CallbackComponent = _CallbackComponent
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
import dev.ultreon.quantum.client.gui.widget.Button as _Button_Type
_Type = _Button_Type.Type
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Button():
    """dev.ultreon.quantum.client.gui.widget.Button"""
 
    @staticmethod
    def _wrap(java_value: _Button) -> 'Button':
        return Button(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Button):
        """
        Dynamic initializer for Button.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Button__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Button__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def position(self, arg0: 'Supplier'):
        """public abstract dev.ultreon.quantum.client.gui.widget.Button<T> dev.ultreon.quantum.client.gui.widget.Button.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        pass

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.isPressed()"""
        return bool._wrap(super(Button, self).isPressed())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @overload
    def callback(self, arg0: 'Callback') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.callback(dev.ultreon.quantum.client.gui.Callback<T>)"""
        return 'Button'._wrap(super(_Button, self).callback(arg0))

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.click()"""
        return bool._wrap(super(Button, self).click())

    @abstractmethod
    def bounds(self, arg0: 'Supplier'):
        """public abstract dev.ultreon.quantum.client.gui.widget.Button<T> dev.ultreon.quantum.client.gui.widget.Button.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        pass

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<T> dev.ultreon.quantum.client.gui.widget.Button.callback()"""
        return 'components.CallbackComponent'._wrap(super(Button, self).callback())

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Button, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str._wrap(super(Widget, self).getName())

    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button.type()"""
        return 'Type'._wrap(super(Button, self).type())

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @overload
    def type(self, arg0: 'Type') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.type(dev.ultreon.quantum.client.gui.widget.Button$Type)"""
        return 'Button'._wrap(super(_Button, self).type(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mousePress(int,int,int)"""
        return bool._wrap(super(_Button, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Button, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener
import dev.ultreon.quantum.client.gui.widget.Widget as _Widget_RevalidateListener
_RevalidateListener = _Widget_RevalidateListener.RevalidateListener
from abc import abstractmethod, ABC
 
class RevalidateListener():
    """dev.ultreon.quantum.client.gui.widget.Widget.RevalidateListener"""
 
    @staticmethod
    def _wrap(java_value: _RevalidateListener) -> 'RevalidateListener':
        return RevalidateListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RevalidateListener):
        """
        Dynamic initializer for RevalidateListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RevalidateListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RevalidateListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def revalidate(self, arg0: 'Widget'):
        """public abstract void dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener.revalidate(dev.ultreon.quantum.client.gui.widget.Widget)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Button$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import dev.ultreon.quantum.client.gui.widget.Button as _Button_Type
_Type = _Button_Type.Type
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Type():
    """dev.ultreon.quantum.client.gui.widget.Button.Type"""
 
    @staticmethod
    def _wrap(java_value: _Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Type):
        """
        Dynamic initializer for Type.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Type__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Type__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static dev.ultreon.quantum.client.gui.widget.Button$Type[] dev.ultreon.quantum.client.gui.widget.Button$Type.values()"""
        return List[Type]._wrap(_Type.values())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


Type.DARK = Type._wrap(_DARK.DARK)

Type.DARK_EMBED = Type._wrap(_DARK_EMBED.DARK_EMBED)

Type.LIGHT = Type._wrap(_LIGHT.LIGHT)

Type.LIGHT_EMBED = Type._wrap(_LIGHT_EMBED.LIGHT_EMBED) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Widget
from pyquantum_helper import import_once as _import_once
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
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
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
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
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
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Widget():
    """dev.ultreon.quantum.client.gui.widget.Widget"""
 
    @staticmethod
    def _wrap(java_value: _Widget) -> 'Widget':
        return Widget(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Widget):
        """
        Dynamic initializer for Widget.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Widget__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Widget__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @abstractmethod
    def bounds(self, arg0: 'Supplier'):
        """public abstract dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.Widget.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str._wrap(super(Widget, self).getName())

    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool._wrap(super(_Widget, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @abstractmethod
    def position(self, arg0: 'Supplier'):
        """public abstract dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.Widget.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        pass

    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.CycleButton
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = _import_once("pyquantum.client.gui.widget.components")

import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as _TextComponent
_TextComponent = _TextComponent
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
import dev.ultreon.quantum.client.gui.widget.CycleButton as _CycleButton
_CycleButton = _CycleButton
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.file.Path as Path
from builtins import object
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.components.ColorComponent as _ColorComponent
_ColorComponent = _ColorComponent
import dev.ultreon.quantum.client.gui.widget.Button as _Button
_Button = _Button
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as _CallbackComponent
_CallbackComponent = _CallbackComponent
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
import dev.ultreon.quantum.client.gui.widget.Button as _Button_Type
_Type = _Button_Type.Type
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import java.util.function.Function as Function
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CycleButton():
    """dev.ultreon.quantum.client.gui.widget.CycleButton"""
 
    @staticmethod
    def _wrap(java_value: _CycleButton) -> 'CycleButton':
        return CycleButton(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CycleButton):
        """
        Dynamic initializer for CycleButton.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CycleButton__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CycleButton__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button.type()"""
        return 'Type'._wrap(super(Button, self).type())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.isPressed()"""
        return bool._wrap(super(Button, self).isPressed())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @overload
    def callback(self, arg0: 'Callback') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.callback(dev.ultreon.quantum.client.gui.Callback<T>)"""
        return 'Button'._wrap(super(_Button, self).callback(arg0))

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.client.gui.widget.CycleButton.getValue()"""
        return object._wrap(super(CycleButton, self).getValue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def bounds(self, arg0: 'Supplier') -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'CycleButton'._wrap(super(_CycleButton, self).bounds(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.CycleButton.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_CycleButton, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @overload
    def text(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.CycleButton.text()"""
        return 'components.TextComponent'._wrap(super(CycleButton, self).text())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @overload
    def formatter(self, arg0: 'Function') -> 'CycleButton':
        """public final dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.formatter(java.util.function.Function<T, dev.ultreon.quantum.text.TextObject>)"""
        return 'CycleButton'._wrap(super(_CycleButton, self).formatter(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def labelTranslation(self, arg0: str, *arg1: object) -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.labelTranslation(java.lang.String,java.lang.Object...)"""
        return 'CycleButton'._wrap(super(_CycleButton, self).labelTranslation(arg0, arg1))

    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.CycleButton.getIndex()"""
        return int._wrap(super(CycleButton, self).getIndex())

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<T> dev.ultreon.quantum.client.gui.widget.Button.callback()"""
        return 'components.CallbackComponent'._wrap(super(Button, self).callback())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Button, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.CycleButton()"""
        val = _CycleButton()
        self.__wrapper = val

    @overload
    def label(self, arg0: str) -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.label(java.lang.String)"""
        return 'CycleButton'._wrap(super(_CycleButton, self).label(arg0))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.CycleButton()"""
        val = _CycleButton()
        self.__wrapper = val

    @overload
    def label(self, arg0: 'TextObject') -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.label(dev.ultreon.quantum.text.TextObject)"""
        return 'CycleButton'._wrap(super(_CycleButton, self).label(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @overload
    def values(self, *arg0: object) -> 'CycleButton':
        """public final dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.values(T...)"""
        return 'CycleButton'._wrap(super(_CycleButton, self).values(arg0))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.CycleButton.revalidate()"""
        super(CycleButton, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def getLabel(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.widget.CycleButton.getLabel()"""
        return 'text.TextObject'._wrap(super(CycleButton, self).getLabel())

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str._wrap(super(Widget, self).getName())

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @overload
    def type(self, arg0: 'Type') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.type(dev.ultreon.quantum.client.gui.widget.Button$Type)"""
        return 'Button'._wrap(super(_Button, self).type(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: 'MutableText'):
        """public dev.ultreon.quantum.client.gui.widget.CycleButton(int,dev.ultreon.quantum.text.MutableText)"""
        val = _CycleButton(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mousePress(int,int,int)"""
        return bool._wrap(super(_Button, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.CycleButton.click()"""
        return bool._wrap(super(CycleButton, self).click())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

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

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'MutableText'):
        """public dev.ultreon.quantum.client.gui.widget.CycleButton(int,int,dev.ultreon.quantum.text.MutableText)"""
        val = _CycleButton(_int.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @overload
    def position(self, arg0: 'Supplier') -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'CycleButton'._wrap(super(_CycleButton, self).position(arg0))

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def textColor(self) -> 'components.ColorComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.ColorComponent dev.ultreon.quantum.client.gui.widget.CycleButton.textColor()"""
        return 'components.ColorComponent'._wrap(super(CycleButton, self).textColor())

    @overload
    def index(self, arg0: int) -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.index(int)"""
        return 'CycleButton'._wrap(super(_CycleButton, self).index(_int.valueOf(arg0)))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Button, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def value(self, arg0: object) -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.value(T)"""
        return 'CycleButton'._wrap(super(_CycleButton, self).value(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())

    @overload
    def getRawLabel(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.CycleButton.getRawLabel()"""
        return str._wrap(super(CycleButton, self).getRawLabel()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Rectangle
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = _import_once("pyquantum.client.gui.widget.components")

import java.lang.Double as _double
import java.lang.Character as _char
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
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
import java.nio.file.Path as Path
import dev.ultreon.quantum.client.gui.widget.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.components.ColorComponent as _ColorComponent
_ColorComponent = _ColorComponent
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
import java.lang.Class as _Class
_Class = _Class
 
class Rectangle():
    """dev.ultreon.quantum.client.gui.widget.Rectangle"""
 
    @staticmethod
    def _wrap(java_value: _Rectangle) -> 'Rectangle':
        return Rectangle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Rectangle):
        """
        Dynamic initializer for Rectangle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Rectangle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Rectangle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Rectangle':
        """public dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).bounds(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Rectangle.getName()"""
        return str._wrap(super(Rectangle, self).getName())

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def backgroundColor(self, arg0: 'RgbColor') -> 'Rectangle':
        """public dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.backgroundColor(dev.ultreon.quantum.util.RgbColor)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).backgroundColor(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.widget.Rectangle(int,int,int,int)"""
        val = _Rectangle(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.Rectangle()"""
        val = _Rectangle()
        self.__wrapper = val

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.Rectangle()"""
        val = _Rectangle()
        self.__wrapper = val

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Rectangle, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @overload
    def position(self, arg0: 'Supplier') -> 'Rectangle':
        """public dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).position(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mousePress(int,int,int)"""
        return bool._wrap(super(_Rectangle, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @staticmethod
    @overload
    def of(arg0: int, arg1: int, arg2: int, arg3: int) -> 'Rectangle':
        """public static dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.of(int,int,int,int)"""
        return Rectangle._wrap(_Rectangle.of(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Rectangle, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Rectangle.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Rectangle, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

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

    @overload
    def backgroundColor(self) -> 'components.ColorComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.ColorComponent dev.ultreon.quantum.client.gui.widget.Rectangle.backgroundColor()"""
        return 'components.ColorComponent'._wrap(super(Rectangle, self).backgroundColor())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @staticmethod
    @overload
    def create() -> 'Rectangle':
        """public static dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.create()"""
        return Rectangle._wrap(_Rectangle.create())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Rectangle, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.TextButton
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = _import_once("pyquantum.client.gui.widget.components")

import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as _TextComponent
_TextComponent = _TextComponent
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
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
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.client.gui.widget.components.ColorComponent as _ColorComponent
_ColorComponent = _ColorComponent
import dev.ultreon.quantum.client.gui.widget.Button as _Button
_Button = _Button
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as _CallbackComponent
_CallbackComponent = _CallbackComponent
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
import dev.ultreon.quantum.client.gui.widget.Button as _Button_Type
_Type = _Button_Type.Type
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextButton():
    """dev.ultreon.quantum.client.gui.widget.TextButton"""
 
    @staticmethod
    def _wrap(java_value: _TextButton) -> 'TextButton':
        return TextButton(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextButton):
        """
        Dynamic initializer for TextButton.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextButton__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextButton__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button.type()"""
        return 'Type'._wrap(super(Button, self).type())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.isPressed()"""
        return bool._wrap(super(Button, self).isPressed())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def of(arg0: 'TextObject') -> 'TextButton':
        """public static dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.of(dev.ultreon.quantum.text.TextObject)"""
        return TextButton._wrap(_TextButton.of(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @staticmethod
    @overload
    def of(arg0: str) -> 'TextButton':
        """public static dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.of(java.lang.String)"""
        return TextButton._wrap(_TextButton.of(arg0))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def of(arg0: 'TextObject', arg1: int, arg2: int) -> 'TextButton':
        """public static dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.of(dev.ultreon.quantum.text.TextObject,int,int)"""
        return TextButton._wrap(_TextButton.of(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'TextButton'._wrap(super(_TextButton, self).bounds(arg0))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def position(self, arg0: 'Supplier') -> 'TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'TextButton'._wrap(super(_TextButton, self).position(arg0))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.TextButton.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_TextButton, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @overload
    def textColor(self) -> 'components.ColorComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.ColorComponent dev.ultreon.quantum.client.gui.widget.TextButton.textColor()"""
        return 'components.ColorComponent'._wrap(super(TextButton, self).textColor())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def text(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.TextButton.text()"""
        return 'components.TextComponent'._wrap(super(TextButton, self).text())

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<T> dev.ultreon.quantum.client.gui.widget.Button.callback()"""
        return 'components.CallbackComponent'._wrap(super(Button, self).callback())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TextButton.getName()"""
        return str._wrap(super(TextButton, self).getName())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def of(arg0: 'TextObject', arg1: int) -> 'TextButton':
        """public static dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.of(dev.ultreon.quantum.text.TextObject,int)"""
        return TextButton._wrap(_TextButton.of(arg0, _int.valueOf(arg1)))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Button, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.TextButton.isClickable()"""
        return bool._wrap(super(TextButton, self).isClickable())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @overload
    def translation(self, arg0: str, *arg1: object) -> 'TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.translation(java.lang.String,java.lang.Object...)"""
        return 'TextButton'._wrap(super(_TextButton, self).translation(arg0, arg1))

    @override
    @overload
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.click()"""
        return bool._wrap(super(Button, self).click())

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @overload
    def type(self, arg0: 'Type') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.type(dev.ultreon.quantum.client.gui.widget.Button$Type)"""
        return 'Button'._wrap(super(_Button, self).type(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mousePress(int,int,int)"""
        return bool._wrap(super(_Button, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Button, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def of(arg0: str, arg1: int) -> 'TextButton':
        """public static dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.of(java.lang.String,int)"""
        return TextButton._wrap(_TextButton.of(arg0, _int.valueOf(arg1)))

    @overload
    def callback(self, arg0: 'Callback') -> 'TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.TextButton>)"""
        return 'TextButton'._wrap(super(_TextButton, self).callback(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @staticmethod
    @overload
    def of(arg0: str, arg1: int, arg2: int) -> 'TextButton':
        """public static dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.of(java.lang.String,int,int)"""
        return TextButton._wrap(_TextButton.of(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.WorldCardList
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.widget.WorldCardList as _WorldCardList_Entry
_Entry = _WorldCardList_Entry.Entry
import dev.ultreon.quantum.client.gui.widget.HorizontalList as _HorizontalList
_HorizontalList = _HorizontalList
import java.util.function.Predicate as Predicate
import dev.ultreon.quantum.client.gui.widget.WorldCardList as _WorldCardList
_WorldCardList = _WorldCardList
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
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
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
import dev.ultreon.quantum.client.gui.widget.HorizontalList as _HorizontalList_Entry
_Entry = _HorizontalList_Entry.Entry
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
import dev.ultreon.quantum.client.gui.widget.Widget as _Widget
_Widget = _Widget
import dev.ultreon.quantum.client.gui.Position as _Position
_Position = _Position
import java.util.function.IntSupplier as IntSupplier
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
 
class WorldCardList():
    """dev.ultreon.quantum.client.gui.widget.WorldCardList"""
 
    @staticmethod
    def _wrap(java_value: _WorldCardList) -> 'WorldCardList':
        return WorldCardList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldCardList):
        """
        Dynamic initializer for WorldCardList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldCardList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldCardList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool._wrap(super(_UIContainer, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def scroll(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.scroll(int)"""
        super(_HorizontalList, self).scroll(_int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @staticmethod
    @overload
    def create(arg0: 'IntSupplier') -> 'WorldCardList':
        """public static dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.create(java.util.function.IntSupplier)"""
        return WorldCardList._wrap(_WorldCardList.create(arg0))

    @override
    @overload
    def getGap(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getGap()"""
        return int._wrap(super(HorizontalList, self).getGap())

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_HorizontalList, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getContentHeight()"""
        return int._wrap(super(HorizontalList, self).getContentHeight())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.revalidate()"""
        super(HorizontalList, self).revalidate()

    @override
    @overload
    def getXOffset(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getXOffset()"""
        return int._wrap(super(HorizontalList, self).getXOffset())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mousePress(int,int,int)"""
        return bool._wrap(super(_HorizontalList, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def isSelectable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.isSelectable()"""
        return bool._wrap(super(HorizontalList, self).isSelectable())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_HorizontalList, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @overload
    def count(self, arg0: 'IntSupplier') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.count(java.util.function.IntSupplier)"""
        return 'WorldCardList'._wrap(super(_WorldCardList, self).count(arg0))

    @overload
    def worlds(self, arg0: 'List') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.worlds(java.util.List<dev.ultreon.quantum.world.WorldStorage>)"""
        return 'WorldCardList'._wrap(super(_WorldCardList, self).worlds(arg0))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.children()"""
        return 'List'._wrap(super(HorizontalList, self).children())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def removeEntry(self, arg0: 'Entry'):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.removeEntry(T)"""
        super(_HorizontalList, self).removeEntry(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def mouseEnter(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseEnter(int,int)"""
        super(_HorizontalList, self).mouseEnter(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getItemWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getItemWidth()"""
        return int._wrap(super(HorizontalList, self).getItemWidth())

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @override
    @overload
    def setXOffset(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.setXOffset(int)"""
        super(_HorizontalList, self).setXOffset(_int.valueOf(arg0))

    @override
    @overload
    def getSelected(self) -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.getSelected()"""
        return 'Entry'._wrap(super(HorizontalList, self).getSelected())

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @overload
    def itemRenderer(self, arg0: 'ItemRenderer') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.itemRenderer(dev.ultreon.quantum.client.gui.widget.HorizontalList$ItemRenderer<dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry>)"""
        return 'WorldCardList'._wrap(super(_WorldCardList, self).itemRenderer(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool._wrap(super(_UIContainer, self).charType(_char.valueOf(arg0)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseWheel(int,int,double)"""
        return bool._wrap(super(_HorizontalList, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def xOffset(self, arg0: int) -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.xOffset(int)"""
        return 'WorldCardList'._wrap(super(_WorldCardList, self).xOffset(_int.valueOf(arg0)))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def gap(self, arg0: int) -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.gap(int)"""
        return 'WorldCardList'._wrap(super(_WorldCardList, self).gap(_int.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'._wrap(super(component.GameComponentHolder, self).components())

    @overload
    def entries(self, arg0: 'Collection') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.entries(java.util.Collection<? extends dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry>)"""
        return 'WorldCardList'._wrap(super(_WorldCardList, self).entries(arg0))

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool._wrap(_Widget.isPosWithin(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @overload
    def position(self, arg0: 'Supplier') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'WorldCardList'._wrap(super(_WorldCardList, self).position(arg0))

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'Widget'._wrap(super(_UIContainer, self).getExactWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def removeEntryIf(self, arg0: 'Predicate'):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.removeEntryIf(java.util.function.Predicate<T>)"""
        super(_HorizontalList, self).removeEntryIf(arg0)

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'Widget'._wrap(super(_UIContainer, self).getWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(_UIContainer, self).setLayout(arg0)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseRelease(int,int,int)"""
        return bool._wrap(super(_HorizontalList, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setGap(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.setGap(int)"""
        super(_HorizontalList, self).setGap(_int.valueOf(arg0))

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseMove(int,int)"""
        super(_HorizontalList, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @overload
    def callback(self, arg0: 'Callback') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry>)"""
        return 'WorldCardList'._wrap(super(_WorldCardList, self).callback(arg0))

    @overload
    def selectable(self, arg0: bool) -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.selectable(boolean)"""
        return 'WorldCardList'._wrap(super(_WorldCardList, self).selectable(_boolean.valueOf(arg0)))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_UIContainer, self).renderChild(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @overload
    def entry(self, arg0: 'Entry') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry dev.ultreon.quantum.client.gui.widget.WorldCardList.entry(dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry)"""
        return 'Entry'._wrap(super(_WorldCardList, self).entry(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @overload
    def itemHeight(self, arg0: int) -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.itemHeight(int)"""
        return 'WorldCardList'._wrap(super(_WorldCardList, self).itemHeight(_int.valueOf(arg0)))

    @overload
    def getEntryAt(self, arg0: int, arg1: int) -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.getEntryAt(int,int)"""
        return 'Entry'._wrap(super(_HorizontalList, self).getEntryAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def itemWidth(self, arg0: int) -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.itemWidth(int)"""
        return 'WorldCardList'._wrap(super(_WorldCardList, self).itemWidth(_int.valueOf(arg0)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.HorizontalList.getName()"""
        return str._wrap(super(HorizontalList, self).getName())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'WorldCardList'._wrap(super(_WorldCardList, self).bounds(arg0))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'._wrap(super(UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def scrollDelta(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.scrollDelta(int)"""
        super(_HorizontalList, self).scrollDelta(_int.valueOf(arg0))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_UIContainer, self).remove(arg0)

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def mouseExit(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseExit()"""
        super(HorizontalList, self).mouseExit()

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(UIContainer, self).getWidgets())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_HorizontalList, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'._wrap(super(_UIContainer, self).getWidgetsAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_HorizontalList, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def add(self, arg0: 'Widget') -> 'Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'Widget'._wrap(super(_UIContainer, self).add(arg0))

    @override
    @overload
    def getItemHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getItemHeight()"""
        return int._wrap(super(HorizontalList, self).getItemHeight())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyPress(int)"""
        return bool._wrap(super(_UIContainer, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())


UIContainer.ROOT = UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.StaticWidget
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.widget.StaticWidget as _StaticWidget
_StaticWidget = _StaticWidget
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class StaticWidget():
    """dev.ultreon.quantum.client.gui.widget.StaticWidget"""
 
    @staticmethod
    def _wrap(java_value: _StaticWidget) -> 'StaticWidget':
        return StaticWidget(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StaticWidget):
        """
        Dynamic initializer for StaticWidget.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StaticWidget__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StaticWidget__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public abstract void dev.ultreon.quantum.client.gui.widget.StaticWidget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.widget.WorldCardList as _WorldCardList_Entry
_Entry = _WorldCardList_Entry.Entry
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
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
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
import dev.ultreon.quantum.client.gui.widget.HorizontalList as _HorizontalList_Entry
_Entry = _HorizontalList_Entry.Entry
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
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
import java.lang.Class as _Class
_Class = _Class
 
class Entry():
    """dev.ultreon.quantum.client.gui.widget.WorldCardList.Entry"""
 
    @staticmethod
    def _wrap(java_value: _Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Entry):
        """
        Dynamic initializer for Entry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Entry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Entry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @overload
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.click()"""
        return bool._wrap(super(Entry, self).click())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: bool, arg4: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.render(dev.ultreon.quantum.client.gui.Renderer,int,int,boolean,float)"""
        super(_Entry, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Entry, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def position(self, arg0: 'Supplier') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Entry'._wrap(super(_Entry, self).position(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.keyPress(int)"""
        return bool._wrap(super(_Entry, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.isPressed()"""
        return bool._wrap(super(Entry, self).isPressed())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @override
    @overload
    def select(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.select(boolean)"""
        super(_Entry, self).select(_boolean.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @overload
    def __init__(self, arg0: 'WorldCardList', arg1: 'WorldStorage'):
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry(dev.ultreon.quantum.client.gui.widget.WorldCardList,dev.ultreon.quantum.world.WorldStorage)"""
        val = _Entry(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Entry, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.keyRelease(int)"""
        return bool._wrap(super(_Entry, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def renderEntry(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: float):
        """public void dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.renderEntry(dev.ultreon.quantum.client.gui.Renderer,int,int,int,int,boolean,float)"""
        super(_Entry, self).renderEntry(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5), _float.valueOf(arg6))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Entry, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.mousePress(int,int,int)"""
        return bool._wrap(super(_Entry, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Entry'._wrap(super(_Entry, self).bounds(arg0))

    @override
    @overload
    def select(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.select()"""
        super(Entry, self).select()

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.revalidate()"""
        super(Entry, self).revalidate()

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'._wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.getName()"""
        return str._wrap(super(Entry, self).getName())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool._wrap(_Widget.isPosWithin(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Entry, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.mouseMove(int,int)"""
        super(_Entry, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getWorld(self) -> 'world.WorldStorage':
        """public dev.ultreon.quantum.world.WorldStorage dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.getWorld()"""
        return 'world.WorldStorage'._wrap(super(Entry, self).getWorld())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry
from pyquantum_helper import import_once as _import_once
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
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
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
import dev.ultreon.quantum.client.gui.widget.HorizontalList as _HorizontalList_Entry
_Entry = _HorizontalList_Entry.Entry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
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
import java.lang.Class as _Class
_Class = _Class
 
class Entry():
    """dev.ultreon.quantum.client.gui.widget.HorizontalList.Entry"""
 
    @staticmethod
    def _wrap(java_value: _Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Entry):
        """
        Dynamic initializer for Entry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Entry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Entry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @abstractmethod
    def renderEntry(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: float):
        """public abstract void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.renderEntry(dev.ultreon.quantum.client.gui.Renderer,int,int,int,int,boolean,float)"""
        pass

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def position(self, arg0: 'Supplier') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Entry'._wrap(super(_Entry, self).position(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def select(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.select(boolean)"""
        super(_Entry, self).select(_boolean.valueOf(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: bool, arg4: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.render(dev.ultreon.quantum.client.gui.Renderer,int,int,boolean,float)"""
        super(_Entry, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @overload
    def select(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.select()"""
        super(Entry, self).select()

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool._wrap(super(_Widget, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Entry'._wrap(super(_Entry, self).bounds(arg0))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'._wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.getName()"""
        return str._wrap(super(Entry, self).getName())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool._wrap(_Widget.isPosWithin(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())

    @overload
    def __init__(self, arg0: 'HorizontalList'):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry(dev.ultreon.quantum.client.gui.widget.HorizontalList<?>)"""
        val = _Entry(arg0)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.TextEntry
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = _import_once("pyquantum.client.gui.widget.components")

import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as _TextComponent
_TextComponent = _TextComponent
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import it.unimi.dsi.fastutil.chars.CharPredicate as _CharPredicate
_CharPredicate = _CharPredicate
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.gui.widget.TextEntry as _TextEntry
_TextEntry = _TextEntry
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
import it.unimi.dsi.fastutil.chars.CharPredicate as CharPredicate
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as _CallbackComponent
_CallbackComponent = _CallbackComponent
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
import java.lang.Class as _Class
_Class = _Class
 
class TextEntry():
    """dev.ultreon.quantum.client.gui.widget.TextEntry"""
 
    @staticmethod
    def _wrap(java_value: _TextEntry) -> 'TextEntry':
        return TextEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextEntry):
        """
        Dynamic initializer for TextEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def position(self, arg0: 'Supplier') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'TextEntry'._wrap(super(_TextEntry, self).position(arg0))

    @overload
    def revalidateCursor(self):
        """public void dev.ultreon.quantum.client.gui.widget.TextEntry.revalidateCursor()"""
        super(TextEntry, self).revalidateCursor()

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @staticmethod
    @overload
    def of(arg0: str) -> 'TextEntry':
        """public static dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.of(java.lang.String)"""
        return TextEntry._wrap(_TextEntry.of(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.widget.TextEntry(int)"""
        val = _TextEntry(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.TextEntry()"""
        val = _TextEntry()
        self.__wrapper = val

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TextEntry.getValue()"""
        return str._wrap(super(TextEntry, self).getValue())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.widget.TextEntry(int,int)"""
        val = _TextEntry(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.TextEntry.keyPress(int)"""
        return bool._wrap(super(_TextEntry, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def value(self, arg0: str) -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.value(java.lang.String)"""
        return 'TextEntry'._wrap(super(_TextEntry, self).value(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @overload
    def callback(self, arg0: 'Callback') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.TextEntry>)"""
        return 'TextEntry'._wrap(super(_TextEntry, self).callback(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.TextEntry.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Widget'._wrap(super(_TextEntry, self).bounds(arg0))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @overload
    def setCursorIdx(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.TextEntry.setCursorIdx(int)"""
        super(_TextEntry, self).setCursorIdx(_int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.TextEntry()"""
        val = _TextEntry()
        self.__wrapper = val

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @staticmethod
    @overload
    def of() -> 'TextEntry':
        """public static dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.of()"""
        return TextEntry._wrap(_TextEntry.of())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.TextEntry.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_TextEntry, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool._wrap(super(_Widget, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def filter(self, arg0: 'CharPredicate') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.filter(it.unimi.dsi.fastutil.chars.CharPredicate)"""
        return 'TextEntry'._wrap(super(_TextEntry, self).filter(arg0))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def hint(self, arg0: 'TextObject') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.hint(dev.ultreon.quantum.text.TextObject)"""
        return 'TextEntry'._wrap(super(_TextEntry, self).hint(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TextEntry.getName()"""
        return str._wrap(super(TextEntry, self).getName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getCursorIdx(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.TextEntry.getCursorIdx()"""
        return int._wrap(super(TextEntry, self).getCursorIdx())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.TextEntry.charType(char)"""
        return bool._wrap(super(_TextEntry, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def hint(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.TextEntry.hint()"""
        return 'components.TextComponent'._wrap(super(TextEntry, self).hint())

    @overload
    def getFilter(self) -> 'CharPredicate':
        """public it.unimi.dsi.fastutil.chars.CharPredicate dev.ultreon.quantum.client.gui.widget.TextEntry.getFilter()"""
        return 'CharPredicate'._wrap(super(TextEntry, self).getFilter())

    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<dev.ultreon.quantum.client.gui.widget.TextEntry> dev.ultreon.quantum.client.gui.widget.TextEntry.callback()"""
        return 'components.CallbackComponent'._wrap(super(TextEntry, self).callback())

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.TitleButton
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = _import_once("pyquantum.client.gui.widget.components")

import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as _TextComponent
_TextComponent = _TextComponent
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
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
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.client.gui.widget.components.ColorComponent as _ColorComponent
_ColorComponent = _ColorComponent
import dev.ultreon.quantum.client.gui.widget.Button as _Button
_Button = _Button
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as _CallbackComponent
_CallbackComponent = _CallbackComponent
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
import dev.ultreon.quantum.client.gui.widget.Button as _Button_Type
_Type = _Button_Type.Type
import dev.ultreon.quantum.client.gui.widget.TitleButton as _TitleButton
_TitleButton = _TitleButton
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TitleButton():
    """dev.ultreon.quantum.client.gui.widget.TitleButton"""
 
    @staticmethod
    def _wrap(java_value: _TitleButton) -> 'TitleButton':
        return TitleButton(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TitleButton):
        """
        Dynamic initializer for TitleButton.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TitleButton__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TitleButton__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button.type()"""
        return 'Type'._wrap(super(Button, self).type())

    @overload
    def callback(self, arg0: 'Callback') -> 'TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.TitleButton>)"""
        return 'TitleButton'._wrap(super(_TitleButton, self).callback(arg0))

    @overload
    def icon(self, arg0: 'Identifier') -> 'TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.icon(dev.ultreon.quantum.util.Identifier)"""
        return 'TitleButton'._wrap(super(_TitleButton, self).icon(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.isPressed()"""
        return bool._wrap(super(Button, self).isPressed())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @staticmethod
    @overload
    def of(arg0: str, arg1: int, arg2: int) -> 'TitleButton':
        """public static dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.of(java.lang.String,int,int)"""
        return TitleButton._wrap(_TitleButton.of(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def translation(self, arg0: str, *arg1: object) -> 'TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.translation(java.lang.String,java.lang.Object...)"""
        return 'TitleButton'._wrap(super(_TitleButton, self).translation(arg0, arg1))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def of(arg0: 'TextObject', arg1: int) -> 'TitleButton':
        """public static dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.of(dev.ultreon.quantum.text.TextObject,int)"""
        return TitleButton._wrap(_TitleButton.of(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @staticmethod
    @overload
    def of(arg0: str, arg1: int) -> 'TitleButton':
        """public static dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.of(java.lang.String,int)"""
        return TitleButton._wrap(_TitleButton.of(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @staticmethod
    @overload
    def of(arg0: 'TextObject', arg1: int, arg2: int) -> 'TitleButton':
        """public static dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.of(dev.ultreon.quantum.text.TextObject,int,int)"""
        return TitleButton._wrap(_TitleButton.of(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TitleButton.getName()"""
        return str._wrap(super(TitleButton, self).getName())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<T> dev.ultreon.quantum.client.gui.widget.Button.callback()"""
        return 'components.CallbackComponent'._wrap(super(Button, self).callback())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'TitleButton'._wrap(super(_TitleButton, self).bounds(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Button, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @overload
    def text(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.TitleButton.text()"""
        return 'components.TextComponent'._wrap(super(TitleButton, self).text())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.TitleButton.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_TitleButton, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.TitleButton.isClickable()"""
        return bool._wrap(super(TitleButton, self).isClickable())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @staticmethod
    @overload
    def of(arg0: 'TextObject') -> 'TitleButton':
        """public static dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.of(dev.ultreon.quantum.text.TextObject)"""
        return TitleButton._wrap(_TitleButton.of(arg0))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getIcon(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.widget.TitleButton.getIcon()"""
        return 'util.Identifier'._wrap(super(TitleButton, self).getIcon())

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @override
    @overload
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.click()"""
        return bool._wrap(super(Button, self).click())

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @overload
    def type(self, arg0: 'Type') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.type(dev.ultreon.quantum.client.gui.widget.Button$Type)"""
        return 'Button'._wrap(super(_Button, self).type(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mousePress(int,int,int)"""
        return bool._wrap(super(_Button, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'._wrap(super(component.GameComponentHolder, self).components())

    @overload
    def position(self, arg0: 'Supplier') -> 'TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'TitleButton'._wrap(super(_TitleButton, self).position(arg0))

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool._wrap(_Widget.isPosWithin(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def textColor(self) -> 'components.ColorComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.ColorComponent dev.ultreon.quantum.client.gui.widget.TitleButton.textColor()"""
        return 'components.ColorComponent'._wrap(super(TitleButton, self).textColor())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Button, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @staticmethod
    @overload
    def of(arg0: str) -> 'TitleButton':
        """public static dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.of(java.lang.String)"""
        return TitleButton._wrap(_TitleButton.of(arg0))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.SelectionList$Entry
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.widget.SelectionList as _SelectionList_Entry
_Entry = _SelectionList_Entry.Entry
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
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
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
from builtins import object
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
import java.lang.Class as _Class
_Class = _Class
 
class Entry():
    """dev.ultreon.quantum.client.gui.widget.SelectionList.Entry"""
 
    @staticmethod
    def _wrap(java_value: _Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Entry):
        """
        Dynamic initializer for Entry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Entry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Entry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

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
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @overload
    def select(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.select(boolean)"""
        super(_Entry, self).select(_boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool._wrap(super(_Widget, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @overload
    def __init__(self, arg0: object, arg1: 'SelectionList'):
        """public dev.ultreon.quantum.client.gui.widget.SelectionList$Entry(T,dev.ultreon.quantum.client.gui.widget.SelectionList<T>)"""
        val = _Entry(arg0, arg1)
        self.__wrapper = val

    @overload
    def select(self):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.select()"""
        super(Entry, self).select()

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: int, arg4: bool, arg5: float):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.render(dev.ultreon.quantum.client.gui.Renderer,int,int,int,boolean,float)"""
        super(_Entry, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T> dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Entry'._wrap(super(_Entry, self).bounds(arg0))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.getName()"""
        return str._wrap(super(Entry, self).getName())

    @overload
    def position(self, arg0: 'Supplier') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T> dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Entry'._wrap(super(_Entry, self).position(arg0))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.getValue()"""
        return object._wrap(super(Entry, self).getValue()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.SelectionList$ItemRenderer
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.gui.widget.SelectionList as _SelectionList_ItemRenderer
_ItemRenderer = _SelectionList_ItemRenderer.ItemRenderer
 
class ItemRenderer():
    """dev.ultreon.quantum.client.gui.widget.SelectionList.ItemRenderer"""
 
    @staticmethod
    def _wrap(java_value: _ItemRenderer) -> 'ItemRenderer':
        return ItemRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemRenderer):
        """
        Dynamic initializer for ItemRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def render(self, arg0: 'Renderer', arg1: object, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: float):
        """public abstract void dev.ultreon.quantum.client.gui.widget.SelectionList$ItemRenderer.render(dev.ultreon.quantum.client.gui.Renderer,T,int,int,int,boolean,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Label
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = _import_once("pyquantum.client.gui.widget.components")

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
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as _TextComponent
_TextComponent = _TextComponent
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.client.gui.widget.components.ScaleComponent as _ScaleComponent
_ScaleComponent = _ScaleComponent
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
import dev.ultreon.quantum.client.gui.widget.Label as _Label
_Label = _Label
import java.lang.Boolean as _boolean
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

import dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent as _AlignmentComponent
_AlignmentComponent = _AlignmentComponent
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
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
import java.lang.Class as _Class
_Class = _Class
 
class Label():
    """dev.ultreon.quantum.client.gui.widget.Label"""
 
    @staticmethod
    def _wrap(java_value: _Label) -> 'Label':
        return Label(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Label):
        """
        Dynamic initializer for Label.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Label__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Label__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_Widget, self).onDisconnect(arg0)

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(Widget, self).getHeight())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(Widget, self).path())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(Widget, self).isVisible())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_Widget, self).setPreferredX(_int.valueOf(arg0))

    @staticmethod
    @overload
    def of(arg0: str) -> 'Label':
        """public static dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.of(java.lang.String)"""
        return Label._wrap(_Label.of(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.Label()"""
        val = _Label()
        self.__wrapper = val

    @overload
    def text(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.Label.text()"""
        return 'components.TextComponent'._wrap(super(Label, self).text())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(Widget, self).isHovered())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Label.getName()"""
        return str._wrap(super(Label, self).getName())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.Label()"""
        val = _Label()
        self.__wrapper = val

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(Widget, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def __init__(self, arg0: 'Alignment'):
        """public dev.ultreon.quantum.client.gui.widget.Label(dev.ultreon.quantum.client.gui.Alignment)"""
        val = _Label(arg0)
        self.__wrapper = val

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_Widget, self).setSize(arg0)

    @overload
    def scale(self) -> 'components.ScaleComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.ScaleComponent dev.ultreon.quantum.client.gui.widget.Label.scale()"""
        return 'components.ScaleComponent'._wrap(super(Label, self).scale())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(Widget, self).componentRegistry())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def scale(self, arg0: int) -> 'Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.scale(int)"""
        return 'Label'._wrap(super(_Label, self).scale(_int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(Widget, self).getY())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_Widget, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_Widget, self).keyRelease(_int.valueOf(arg0)))

    @overload
    def alignment(self) -> 'components.AlignmentComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent dev.ultreon.quantum.client.gui.widget.Label.alignment()"""
        return 'components.AlignmentComponent'._wrap(super(Label, self).alignment())

    @overload
    def renderBackground(self, arg0: 'Renderer', arg1: float):
        """public void dev.ultreon.quantum.client.gui.widget.Label.renderBackground(dev.ultreon.quantum.client.gui.Renderer,float)"""
        super(_Label, self).renderBackground(arg0, _float.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(Widget, self).getPreferredY())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Label'._wrap(super(_Label, self).bounds(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(Widget, self).getPreferredHeight())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_Widget, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @overload
    def __init__(self, arg0: 'Alignment', arg1: 'RgbColor'):
        """public dev.ultreon.quantum.client.gui.widget.Label(dev.ultreon.quantum.client.gui.Alignment,dev.ultreon.quantum.util.RgbColor)"""
        val = _Label(arg0, arg1)
        self.__wrapper = val

    @overload
    def position(self, arg0: 'Supplier') -> 'Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Label'._wrap(super(_Label, self).position(arg0))

    @overload
    def __init__(self, arg0: 'RgbColor'):
        """public dev.ultreon.quantum.client.gui.widget.Label(dev.ultreon.quantum.util.RgbColor)"""
        val = _Label(arg0)
        self.__wrapper = val

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_Widget, self).setPos(arg0)

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(Widget, self).getX())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Widget, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool._wrap(super(_Widget, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(Widget, self).isFocused())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Widget, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(Widget, self).isClickable())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_Widget, self).withComponent(arg0, arg1, arg2)

    @staticmethod
    @overload
    def of() -> 'Label':
        """public static dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.of()"""
        return Label._wrap(_Label.of())

    @overload
    def alignment(self, arg0: 'Alignment') -> 'Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.alignment(dev.ultreon.quantum.client.gui.Alignment)"""
        return 'Label'._wrap(super(_Label, self).alignment(arg0))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_Widget, self).onRevalidate(arg0)

    @overload
    def textColor(self, arg0: 'Color') -> 'Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.textColor(dev.ultreon.quantum.util.Color)"""
        return 'Label'._wrap(super(_Label, self).textColor(arg0))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_Widget, self).height(_int.valueOf(arg0))

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
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(Widget, self).getBounds())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_Widget, self).setBounds(arg0)

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def of(arg0: 'TextObject') -> 'Label':
        """public static dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.of(dev.ultreon.quantum.text.TextObject)"""
        return Label._wrap(_Label.of(arg0))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(Widget, self).getPreferredPos())