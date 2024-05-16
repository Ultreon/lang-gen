from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import java.util.function.Predicate as Predicate
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import dev.ultreon.quantum.client.gui.widget.HorizontalList as __HorizontalList
__HorizontalList = __HorizontalList
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.function.IntSupplier as IntSupplier
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.widget.HorizontalList as __HorizontalList_Entry
__Entry = __HorizontalList_Entry.Entry
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class HorizontalList():
    """dev.ultreon.quantum.client.gui.widget.HorizontalList"""
 
    @staticmethod
    def __wrap(java_value: __HorizontalList) -> 'HorizontalList':
        return HorizontalList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HorizontalList):
        """
        Dynamic initializer for HorizontalList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'UIContainer' = __wrap(__UIContainer.ROOT)


    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'Widget') -> 'Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'Widget'.__wrap(super(__UIContainer, self).add(arg0))

    @overload
    def entry(self, arg0: 'Entry') -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.entry(T)"""
        return 'Entry'.__wrap(super(__HorizontalList, self).entry(arg0))

    @overload
    def mouseEnter(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseEnter(int,int)"""
        super(__HorizontalList, self).mouseEnter(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @overload
    def removeEntry(self, arg0: 'Entry'):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.removeEntry(T)"""
        super(__HorizontalList, self).removeEntry(arg0)

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(UIContainer, self).getWidgets())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__HorizontalList, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def removeEntryIf(self, arg0: 'Predicate'):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.removeEntryIf(java.util.function.Predicate<T>)"""
        super(__HorizontalList, self).removeEntryIf(arg0)

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def setGap(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.setGap(int)"""
        super(__HorizontalList, self).setGap(__int.valueOf(arg0))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.revalidate()"""
        super(HorizontalList, self).revalidate()

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'Widget'.__wrap(super(__UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Size'):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList(dev.ultreon.quantum.client.gui.Size)"""
        val = __HorizontalList(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getGap(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getGap()"""
        return int.__wrap(super(HorizontalList, self).getGap())

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @overload
    def itemWidth(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.itemWidth(int)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).itemWidth(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList()"""
        val = __HorizontalList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isSelectable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.isSelectable()"""
        return bool.__wrap(super(HorizontalList, self).isSelectable())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseMove(int,int)"""
        super(__HorizontalList, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__HorizontalList, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def setXOffset(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.setXOffset(int)"""
        super(__HorizontalList, self).setXOffset(__int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @overload
    def entries(self, arg0: 'Collection') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.entries(java.util.Collection<? extends T>)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).entries(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList(int)"""
        val = __HorizontalList(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @overload
    def bounds(self, arg0: 'Supplier') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).bounds(arg0))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @overload
    def callback(self, arg0: 'Callback') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.callback(dev.ultreon.quantum.client.gui.Callback<T>)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).callback(arg0))

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__HorizontalList, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def itemRenderer(self, arg0: 'ItemRenderer') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.itemRenderer(dev.ultreon.quantum.client.gui.widget.HorizontalList$ItemRenderer<T>)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).itemRenderer(arg0))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__UIContainer, self).setLayout(arg0)

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool.__wrap(super(__UIContainer, self).keyRelease(__int.valueOf(arg0)))

    @overload
    def position(self, arg0: 'Supplier') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).position(arg0))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(UIContainer, self).getLayout())

    @overload
    def scrollDelta(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.scrollDelta(int)"""
        super(__HorizontalList, self).scrollDelta(__int.valueOf(arg0))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool.__wrap(super(__UIContainer, self).charType(__char.valueOf(arg0)))

    @overload
    def getEntryAt(self, arg0: int, arg1: int) -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.getEntryAt(int,int)"""
        return 'Entry'.__wrap(super(__HorizontalList, self).getEntryAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__HorizontalList, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @overload
    def getXOffset(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getXOffset()"""
        return int.__wrap(super(HorizontalList, self).getXOffset())

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'Widget'.__wrap(super(__UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__HorizontalList, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def count(self, arg0: 'IntSupplier') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.count(java.util.function.IntSupplier)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).count(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.HorizontalList.getName()"""
        return str.__wrap(super(HorizontalList, self).getName())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__HorizontalList, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getItemWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getItemWidth()"""
        return int.__wrap(super(HorizontalList, self).getItemWidth())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mousePress(int,int,int)"""
        return bool.__wrap(super(__HorizontalList, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @overload
    def selectable(self, arg0: bool) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.selectable(boolean)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).selectable(__boolean.valueOf(arg0)))

    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getContentHeight()"""
        return int.__wrap(super(HorizontalList, self).getContentHeight())

    @overload
    def gap(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.gap(int)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).gap(__int.valueOf(arg0)))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList(int,int)"""
        val = __HorizontalList(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def xOffset(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.xOffset(int)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).xOffset(__int.valueOf(arg0)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @overload
    def mouseExit(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseExit()"""
        super(HorizontalList, self).mouseExit()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def getSelected(self) -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.getSelected()"""
        return 'Entry'.__wrap(super(HorizontalList, self).getSelected())

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.children()"""
        return 'List'.__wrap(super(HorizontalList, self).children())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyPress(int)"""
        return bool.__wrap(super(__UIContainer, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @overload
    def getItemHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getItemHeight()"""
        return int.__wrap(super(HorizontalList, self).getItemHeight())

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__UIContainer, self).remove(arg0)

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @overload
    def scroll(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.scroll(int)"""
        super(__HorizontalList, self).scroll(__int.valueOf(arg0))

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList()"""
        val = __HorizontalList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def itemHeight(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.itemHeight(int)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).itemHeight(__int.valueOf(arg0)))

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.HorizontalList
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import java.util.function.Predicate as Predicate
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import dev.ultreon.quantum.client.gui.widget.HorizontalList as __HorizontalList
__HorizontalList = __HorizontalList
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.function.IntSupplier as IntSupplier
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.widget.HorizontalList as __HorizontalList_Entry
__Entry = __HorizontalList_Entry.Entry
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class HorizontalList():
    """dev.ultreon.quantum.client.gui.widget.HorizontalList"""
 
    @staticmethod
    def __wrap(java_value: __HorizontalList) -> 'HorizontalList':
        return HorizontalList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HorizontalList):
        """
        Dynamic initializer for HorizontalList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'UIContainer' = __wrap(__UIContainer.ROOT)


    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'Widget') -> 'Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'Widget'.__wrap(super(__UIContainer, self).add(arg0))

    @overload
    def entry(self, arg0: 'Entry') -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.entry(T)"""
        return 'Entry'.__wrap(super(__HorizontalList, self).entry(arg0))

    @overload
    def mouseEnter(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseEnter(int,int)"""
        super(__HorizontalList, self).mouseEnter(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @overload
    def removeEntry(self, arg0: 'Entry'):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.removeEntry(T)"""
        super(__HorizontalList, self).removeEntry(arg0)

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(UIContainer, self).getWidgets())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__HorizontalList, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def removeEntryIf(self, arg0: 'Predicate'):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.removeEntryIf(java.util.function.Predicate<T>)"""
        super(__HorizontalList, self).removeEntryIf(arg0)

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def setGap(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.setGap(int)"""
        super(__HorizontalList, self).setGap(__int.valueOf(arg0))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.revalidate()"""
        super(HorizontalList, self).revalidate()

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'Widget'.__wrap(super(__UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Size'):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList(dev.ultreon.quantum.client.gui.Size)"""
        val = __HorizontalList(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getGap(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getGap()"""
        return int.__wrap(super(HorizontalList, self).getGap())

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @overload
    def itemWidth(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.itemWidth(int)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).itemWidth(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList()"""
        val = __HorizontalList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isSelectable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.isSelectable()"""
        return bool.__wrap(super(HorizontalList, self).isSelectable())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseMove(int,int)"""
        super(__HorizontalList, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__HorizontalList, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def setXOffset(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.setXOffset(int)"""
        super(__HorizontalList, self).setXOffset(__int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @overload
    def entries(self, arg0: 'Collection') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.entries(java.util.Collection<? extends T>)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).entries(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList(int)"""
        val = __HorizontalList(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @overload
    def bounds(self, arg0: 'Supplier') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).bounds(arg0))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @overload
    def callback(self, arg0: 'Callback') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.callback(dev.ultreon.quantum.client.gui.Callback<T>)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).callback(arg0))

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__HorizontalList, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def itemRenderer(self, arg0: 'ItemRenderer') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.itemRenderer(dev.ultreon.quantum.client.gui.widget.HorizontalList$ItemRenderer<T>)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).itemRenderer(arg0))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__UIContainer, self).setLayout(arg0)

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool.__wrap(super(__UIContainer, self).keyRelease(__int.valueOf(arg0)))

    @overload
    def position(self, arg0: 'Supplier') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).position(arg0))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(UIContainer, self).getLayout())

    @overload
    def scrollDelta(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.scrollDelta(int)"""
        super(__HorizontalList, self).scrollDelta(__int.valueOf(arg0))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool.__wrap(super(__UIContainer, self).charType(__char.valueOf(arg0)))

    @overload
    def getEntryAt(self, arg0: int, arg1: int) -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.getEntryAt(int,int)"""
        return 'Entry'.__wrap(super(__HorizontalList, self).getEntryAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__HorizontalList, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @overload
    def getXOffset(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getXOffset()"""
        return int.__wrap(super(HorizontalList, self).getXOffset())

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'Widget'.__wrap(super(__UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__HorizontalList, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def count(self, arg0: 'IntSupplier') -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.count(java.util.function.IntSupplier)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).count(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.HorizontalList.getName()"""
        return str.__wrap(super(HorizontalList, self).getName())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__HorizontalList, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getItemWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getItemWidth()"""
        return int.__wrap(super(HorizontalList, self).getItemWidth())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mousePress(int,int,int)"""
        return bool.__wrap(super(__HorizontalList, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @overload
    def selectable(self, arg0: bool) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.selectable(boolean)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).selectable(__boolean.valueOf(arg0)))

    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getContentHeight()"""
        return int.__wrap(super(HorizontalList, self).getContentHeight())

    @overload
    def gap(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.gap(int)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).gap(__int.valueOf(arg0)))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList(int,int)"""
        val = __HorizontalList(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def xOffset(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.xOffset(int)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).xOffset(__int.valueOf(arg0)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @overload
    def mouseExit(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseExit()"""
        super(HorizontalList, self).mouseExit()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def getSelected(self) -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.getSelected()"""
        return 'Entry'.__wrap(super(HorizontalList, self).getSelected())

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.children()"""
        return 'List'.__wrap(super(HorizontalList, self).children())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyPress(int)"""
        return bool.__wrap(super(__UIContainer, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @overload
    def getItemHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getItemHeight()"""
        return int.__wrap(super(HorizontalList, self).getItemHeight())

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__UIContainer, self).remove(arg0)

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @overload
    def scroll(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.scroll(int)"""
        super(__HorizontalList, self).scroll(__int.valueOf(arg0))

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList()"""
        val = __HorizontalList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def itemHeight(self, arg0: int) -> 'HorizontalList':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.itemHeight(int)"""
        return 'HorizontalList'.__wrap(super(__HorizontalList, self).itemHeight(__int.valueOf(arg0)))

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.HorizontalList 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Panel
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.gui.widget.Panel as __Panel
__Panel = __Panel
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class Panel():
    """dev.ultreon.quantum.client.gui.widget.Panel"""
 
    @staticmethod
    def __wrap(java_value: __Panel) -> 'Panel':
        return Panel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Panel):
        """
        Dynamic initializer for Panel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def position(self, arg0: 'Supplier') -> 'Panel':
        """public dev.ultreon.quantum.client.gui.widget.Panel dev.ultreon.quantum.client.gui.widget.Panel.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Panel'.__wrap(super(__Panel, self).position(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Panel.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Panel, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @staticmethod
    @overload
    def of(arg0: int, arg1: int, arg2: int, arg3: int) -> 'Panel':
        """public static dev.ultreon.quantum.client.gui.widget.Panel dev.ultreon.quantum.client.gui.widget.Panel.of(int,int,int,int)"""
        return Panel.__wrap(__Panel.of(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @staticmethod
    @overload
    def create() -> 'Panel':
        """public static dev.ultreon.quantum.client.gui.widget.Panel dev.ultreon.quantum.client.gui.widget.Panel.create()"""
        return Panel.__wrap(__Panel.create())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Panel.getName()"""
        return str.__wrap(super(Panel, self).getName())

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.widget.Panel(int,int,int,int)"""
        val = __Panel(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.Panel()"""
        val = __Panel()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.Panel()"""
        val = __Panel()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Panel':
        """public dev.ultreon.quantum.client.gui.widget.Panel dev.ultreon.quantum.client.gui.widget.Panel.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Panel'.__wrap(super(__Panel, self).bounds(arg0))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.UIContainer
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class UIContainer():
    """dev.ultreon.quantum.client.gui.widget.UIContainer"""
 
    @staticmethod
    def __wrap(java_value: __UIContainer) -> 'UIContainer':
        return UIContainer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UIContainer):
        """
        Dynamic initializer for UIContainer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'UIContainer' = __wrap(__UIContainer.ROOT)


    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool.__wrap(super(__UIContainer, self).keyRelease(__int.valueOf(arg0)))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__UIContainer, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__UIContainer, self).setLayout(arg0)

    @overload
    def add(self, arg0: 'Widget') -> 'Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'Widget'.__wrap(super(__UIContainer, self).add(arg0))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool.__wrap(super(__UIContainer, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__UIContainer, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'Widget'.__wrap(super(__UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'UIContainer'.__wrap(super(__UIContainer, self).bounds(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mousePress(int,int,int)"""
        return bool.__wrap(super(__UIContainer, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.widget.UIContainer(int,int)"""
        val = __UIContainer(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__UIContainer, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.UIContainer.getName()"""
        return str.__wrap(super(UIContainer, self).getName())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'Widget'.__wrap(super(__UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.mouseMove(int,int)"""
        super(__UIContainer, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__UIContainer, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__UIContainer, self).remove(arg0)

    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(UIContainer, self).getWidgets())

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__UIContainer, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @overload
    def position(self, arg0: 'Supplier') -> 'UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'UIContainer'.__wrap(super(__UIContainer, self).position(arg0))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(UIContainer, self).getLayout())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.revalidate()"""
        super(UIContainer, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyPress(int)"""
        return bool.__wrap(super(__UIContainer, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'.__wrap(super(UIContainer, self).children())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__UIContainer, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = __import_once__("pyquantum.client.gui.widget.components")

import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import dev.ultreon.quantum.world.TerrainNoise as __TerrainNoise
__TerrainNoise = __TerrainNoise
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel as __WorldGenTestPanel
__WorldGenTestPanel = __WorldGenTestPanel
from pyquantum_helper import override
import dev.ultreon.quantum.client.gui.widget.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.client.gui.widget.components.ColorComponent as __ColorComponent
__ColorComponent = __ColorComponent
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class WorldGenTestPanel():
    """dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel"""
 
    @staticmethod
    def __wrap(java_value: __WorldGenTestPanel) -> 'WorldGenTestPanel':
        return WorldGenTestPanel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldGenTestPanel):
        """
        Dynamic initializer for WorldGenTestPanel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def create() -> 'Rectangle':
        """public static dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.create()"""
        return Rectangle.__wrap(__Rectangle.create())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel()"""
        val = __WorldGenTestPanel()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mousePress(int,int,int)"""
        return bool.__wrap(super(__Rectangle, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def random(self):
        """public void dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.random()"""
        super(WorldGenTestPanel, self).random()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__WorldGenTestPanel, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Rectangle, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def backgroundColor(self, arg0: 'RgbColor') -> 'Rectangle':
        """public dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.backgroundColor(dev.ultreon.quantum.util.RgbColor)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).backgroundColor(arg0))

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel()"""
        val = __WorldGenTestPanel()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def backgroundColor(self) -> 'components.ColorComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.ColorComponent dev.ultreon.quantum.client.gui.widget.Rectangle.backgroundColor()"""
        return 'components.ColorComponent'.__wrap(super(Rectangle, self).backgroundColor())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def position(self, arg0: 'Supplier') -> 'Rectangle':
        """public dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).position(arg0))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Rectangle':
        """public dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).bounds(arg0))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.dispose()"""
        super(WorldGenTestPanel, self).dispose()

    @overload
    def getTerrainNoise(self) -> 'world.TerrainNoise':
        """public dev.ultreon.quantum.world.TerrainNoise dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.getTerrainNoise()"""
        return 'world.TerrainNoise'.__wrap(super(WorldGenTestPanel, self).getTerrainNoise())

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Rectangle.getName()"""
        return str.__wrap(super(Rectangle, self).getName())

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @staticmethod
    @overload
    def of(arg0: int, arg1: int, arg2: int, arg3: int) -> 'Rectangle':
        """public static dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.of(int,int,int,int)"""
        return Rectangle.__wrap(__Rectangle.of(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__WorldGenTestPanel, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.charType(char)"""
        return bool.__wrap(super(__WorldGenTestPanel, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @staticmethod
    @overload
    def create() -> 'WorldGenTestPanel':
        """public static dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel dev.ultreon.quantum.client.gui.widget.WorldGenTestPanel.create()"""
        return WorldGenTestPanel.__wrap(__WorldGenTestPanel.create())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Rectangle, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.HorizontalList$ItemRenderer
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.gui.widget.HorizontalList as __HorizontalList_ItemRenderer
__ItemRenderer = __HorizontalList_ItemRenderer.ItemRenderer
 
class ItemRenderer(ABC):
    """dev.ultreon.quantum.client.gui.widget.HorizontalList.ItemRenderer"""
 
    @staticmethod
    def __wrap(java_value: __ItemRenderer) -> 'ItemRenderer':
        return ItemRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ItemRenderer):
        """
        Dynamic initializer for ItemRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def render(self, arg0: 'Renderer', arg1: object, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool, arg7: float):
        """public abstract void dev.ultreon.quantum.client.gui.widget.HorizontalList$ItemRenderer.render(dev.ultreon.quantum.client.gui.Renderer,T,int,int,int,int,boolean,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.ScrollableContainer
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import java.util.function.Predicate as Predicate
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
from builtins import str
import dev.ultreon.quantum.util.RgbColor as __RgbColor
__RgbColor = __RgbColor
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.client.gui.widget.ScrollableContainer as __ScrollableContainer
__ScrollableContainer = __ScrollableContainer
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
import java.util.List as List
 
class ScrollableContainer():
    """dev.ultreon.quantum.client.gui.widget.ScrollableContainer"""
 
    @staticmethod
    def __wrap(java_value: __ScrollableContainer) -> 'ScrollableContainer':
        return ScrollableContainer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScrollableContainer):
        """
        Dynamic initializer for ScrollableContainer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'UIContainer' = __wrap(__UIContainer.ROOT)


    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.ScrollableContainer.getContentHeight()"""
        return int.__wrap(super(ScrollableContainer, self).getContentHeight())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool.__wrap(super(__UIContainer, self).keyRelease(__int.valueOf(arg0)))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mouseEnter(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseEnter(int,int)"""
        super(__ScrollableContainer, self).mouseEnter(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(UIContainer, self).getLayout())

    @overload
    def add(self, arg0: 'Widget') -> 'Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'Widget'.__wrap(super(__UIContainer, self).add(arg0))

    @overload
    def removeWidgetIf(self, arg0: 'Predicate'):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.removeWidgetIf(java.util.function.Predicate<dev.ultreon.quantum.client.gui.widget.Widget>)"""
        super(__ScrollableContainer, self).removeWidgetIf(arg0)

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool.__wrap(super(__UIContainer, self).charType(__char.valueOf(arg0)))

    @overload
    def position(self, arg0: 'Supplier') -> 'ScrollableContainer':
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer dev.ultreon.quantum.client.gui.widget.ScrollableContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'ScrollableContainer'.__wrap(super(__ScrollableContainer, self).position(arg0))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.ScrollableContainer.getName()"""
        return str.__wrap(super(ScrollableContainer, self).getName())

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__ScrollableContainer, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def bounds(self, arg0: 'Supplier') -> 'ScrollableContainer':
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer dev.ultreon.quantum.client.gui.widget.ScrollableContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'ScrollableContainer'.__wrap(super(__ScrollableContainer, self).bounds(arg0))

    @overload
    def backgroundColor(self, arg0: 'RgbColor') -> 'ScrollableContainer':
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer dev.ultreon.quantum.client.gui.widget.ScrollableContainer.backgroundColor(dev.ultreon.quantum.util.RgbColor)"""
        return 'ScrollableContainer'.__wrap(super(__ScrollableContainer, self).backgroundColor(arg0))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'Widget'.__wrap(super(__UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(UIContainer, self).getWidgets())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer()"""
        val = __ScrollableContainer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def backgroundColor(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.gui.widget.ScrollableContainer.backgroundColor()"""
        return 'util.RgbColor'.__wrap(super(ScrollableContainer, self).backgroundColor())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def isSelectable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.isSelectable()"""
        return bool.__wrap(super(ScrollableContainer, self).isSelectable())

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def __init__(self, arg0: 'Size'):
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer(dev.ultreon.quantum.client.gui.Size)"""
        val = __ScrollableContainer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer(int,int)"""
        val = __ScrollableContainer(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

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
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__UIContainer, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__ScrollableContainer, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__ScrollableContainer, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'.__wrap(super(UIContainer, self).children())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__ScrollableContainer, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.ScrollableContainer.getWidgetAt(int,int)"""
        return 'Widget'.__wrap(super(__ScrollableContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer()"""
        val = __ScrollableContainer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mousePress(int,int,int)"""
        return bool.__wrap(super(__ScrollableContainer, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.revalidate()"""
        super(UIContainer, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyPress(int)"""
        return bool.__wrap(super(__UIContainer, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def removeWidget(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.removeWidget(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__ScrollableContainer, self).removeWidget(arg0)

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__UIContainer, self).remove(arg0)

    @overload
    def selectable(self, arg0: bool) -> 'ScrollableContainer':
        """public dev.ultreon.quantum.client.gui.widget.ScrollableContainer dev.ultreon.quantum.client.gui.widget.ScrollableContainer.selectable(boolean)"""
        return 'ScrollableContainer'.__wrap(super(__ScrollableContainer, self).selectable(__boolean.valueOf(arg0)))

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseMove(int,int)"""
        super(__ScrollableContainer, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__UIContainer, self).setLayout(arg0)

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ScrollableContainer.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__ScrollableContainer, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.SelectionList
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import java.util.function.Predicate as Predicate
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.SelectionList as __SelectionList_Entry
__Entry = __SelectionList_Entry.Entry
import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
from builtins import object
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.gui.widget.SelectionList as __SelectionList
__SelectionList = __SelectionList
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class SelectionList():
    """dev.ultreon.quantum.client.gui.widget.SelectionList"""
 
    @staticmethod
    def __wrap(java_value: __SelectionList) -> 'SelectionList':
        return SelectionList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SelectionList):
        """
        Dynamic initializer for SelectionList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'UIContainer' = __wrap(__UIContainer.ROOT)


    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @overload
    def isSelectable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.isSelectable()"""
        return bool.__wrap(super(SelectionList, self).isSelectable())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'Widget') -> 'Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'Widget'.__wrap(super(__UIContainer, self).add(arg0))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(UIContainer, self).getWidgets())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.widget.SelectionList(int)"""
        val = __SelectionList(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def callback(self, arg0: 'Callback') -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.callback(dev.ultreon.quantum.client.gui.Callback<T>)"""
        return 'SelectionList'.__wrap(super(__SelectionList, self).callback(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def removeEntry(self, arg0: object):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.removeEntry(T)"""
        super(__SelectionList, self).removeEntry(arg0)

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def getEntryAt(self, arg0: int, arg1: int) -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T> dev.ultreon.quantum.client.gui.widget.SelectionList.getEntryAt(int,int)"""
        return 'Entry'.__wrap(super(__SelectionList, self).getEntryAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.mousePress(int,int,int)"""
        return bool.__wrap(super(__SelectionList, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'Position', arg1: 'Size'):
        """public dev.ultreon.quantum.client.gui.widget.SelectionList(dev.ultreon.quantum.client.gui.Position,dev.ultreon.quantum.client.gui.Size)"""
        val = __SelectionList(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'Widget'.__wrap(super(__UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: 'Supplier') -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'SelectionList'.__wrap(super(__SelectionList, self).position(arg0))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @overload
    def mouseExit(self):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.mouseExit()"""
        super(SelectionList, self).mouseExit()

    @overload
    def getItemHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.SelectionList.getItemHeight()"""
        return int.__wrap(super(SelectionList, self).getItemHeight())

    @overload
    def entry(self, arg0: object) -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T> dev.ultreon.quantum.client.gui.widget.SelectionList.entry(T)"""
        return 'Entry'.__wrap(super(__SelectionList, self).entry(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__SelectionList, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def itemRenderer(self, arg0: 'ItemRenderer') -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.itemRenderer(dev.ultreon.quantum.client.gui.widget.SelectionList$ItemRenderer<T>)"""
        return 'SelectionList'.__wrap(super(__SelectionList, self).itemRenderer(arg0))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @overload
    def removeEntryIf(self, arg0: 'Predicate'):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.removeEntryIf(java.util.function.Predicate<T>)"""
        super(__SelectionList, self).removeEntryIf(arg0)

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.revalidate()"""
        super(UIContainer, self).revalidate()

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__SelectionList, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def drawBackground(self, arg0: bool) -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.drawBackground(boolean)"""
        return 'SelectionList'.__wrap(super(__SelectionList, self).drawBackground(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T>> dev.ultreon.quantum.client.gui.widget.SelectionList.children()"""
        return 'List'.__wrap(super(SelectionList, self).children())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'SelectionList'.__wrap(super(__SelectionList, self).bounds(arg0))

    @overload
    def entries(self, arg0: 'Collection') -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.entries(java.util.Collection<? extends T>)"""
        return 'SelectionList'.__wrap(super(__SelectionList, self).entries(arg0))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__UIContainer, self).setLayout(arg0)

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.SelectionList()"""
        val = __SelectionList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getGap(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.SelectionList.getGap()"""
        return int.__wrap(super(SelectionList, self).getGap())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool.__wrap(super(__UIContainer, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(UIContainer, self).getLayout())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool.__wrap(super(__UIContainer, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__SelectionList, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'Widget'.__wrap(super(__UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getSelected(self) -> object:
        """public T dev.ultreon.quantum.client.gui.widget.SelectionList.getSelected()"""
        return object.__wrap(super(SelectionList, self).getSelected())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__SelectionList, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @overload
    def removeEntry(self, arg0: 'Entry') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T> dev.ultreon.quantum.client.gui.widget.SelectionList.removeEntry(dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T>)"""
        return 'Entry'.__wrap(super(__SelectionList, self).removeEntry(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__SelectionList, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.widget.SelectionList(int,int,int,int)"""
        val = __SelectionList(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.SelectionList.getName()"""
        return str.__wrap(super(SelectionList, self).getName())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.mouseMove(int,int)"""
        super(__SelectionList, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @overload
    def selectable(self, arg0: bool) -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.selectable(boolean)"""
        return 'SelectionList'.__wrap(super(__SelectionList, self).selectable(__boolean.valueOf(arg0)))

    @overload
    def isDrawBackground(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.isDrawBackground()"""
        return bool.__wrap(super(SelectionList, self).isDrawBackground())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.SelectionList()"""
        val = __SelectionList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.SelectionList.getContentHeight()"""
        return int.__wrap(super(SelectionList, self).getContentHeight())

    @overload
    def itemHeight(self, arg0: int) -> 'SelectionList':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList<T> dev.ultreon.quantum.client.gui.widget.SelectionList.itemHeight(int)"""
        return 'SelectionList'.__wrap(super(__SelectionList, self).itemHeight(__int.valueOf(arg0)))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyPress(int)"""
        return bool.__wrap(super(__UIContainer, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.SelectionList.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__SelectionList, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def mouseEnter(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList.mouseEnter(int,int)"""
        super(__SelectionList, self).mouseEnter(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__UIContainer, self).remove(arg0)

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.IconButton
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = __import_once__("pyquantum.client.gui.widget.components")

import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import dev.ultreon.quantum.client.gui.widget.Button as __Button_Type
__Type = __Button_Type.Type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
try:
    from pyquantum.client.gui import icon
except ImportError:
    icon = __import_once__("pyquantum.client.gui.icon")

import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
from builtins import bool
from builtins import str
import dev.ultreon.quantum.client.gui.widget.IconButton as __IconButton
__IconButton = __IconButton
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import dev.ultreon.quantum.client.gui.widget.Button as __Button
__Button = __Button
import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as __CallbackComponent
__CallbackComponent = __CallbackComponent
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class IconButton():
    """dev.ultreon.quantum.client.gui.widget.IconButton"""
 
    @staticmethod
    def __wrap(java_value: __IconButton) -> 'IconButton':
        return IconButton(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IconButton):
        """
        Dynamic initializer for IconButton.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.click()"""
        return bool.__wrap(super(Button, self).click())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Button, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'IconButton':
        """public dev.ultreon.quantum.client.gui.widget.IconButton dev.ultreon.quantum.client.gui.widget.IconButton.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'IconButton'.__wrap(super(__IconButton, self).bounds(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str.__wrap(super(Widget, self).getName())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def type(self, arg0: 'Type') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.type(dev.ultreon.quantum.client.gui.widget.Button$Type)"""
        return 'Button'.__wrap(super(__Button, self).type(arg0))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mousePress(int,int,int)"""
        return bool.__wrap(super(__Button, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @overload
    def callback(self, arg0: 'Callback') -> 'IconButton':
        """public dev.ultreon.quantum.client.gui.widget.IconButton dev.ultreon.quantum.client.gui.widget.IconButton.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.IconButton>)"""
        return 'IconButton'.__wrap(super(__IconButton, self).callback(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Button, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<T> dev.ultreon.quantum.client.gui.widget.Button.callback()"""
        return 'components.CallbackComponent'.__wrap(super(Button, self).callback())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.IconButton.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__IconButton, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def position(self, arg0: 'Supplier') -> 'IconButton':
        """public dev.ultreon.quantum.client.gui.widget.IconButton dev.ultreon.quantum.client.gui.widget.IconButton.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'IconButton'.__wrap(super(__IconButton, self).position(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Icon') -> 'IconButton':
        """public static dev.ultreon.quantum.client.gui.widget.IconButton dev.ultreon.quantum.client.gui.widget.IconButton.of(dev.ultreon.quantum.client.gui.icon.Icon)"""
        return IconButton.__wrap(__IconButton.of(arg0))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @override
    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.isPressed()"""
        return bool.__wrap(super(Button, self).isPressed())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button.type()"""
        return 'Type'.__wrap(super(Button, self).type())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.ChatTextEntry
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = __import_once__("pyquantum.client.gui.widget.components")

import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as __TextComponent
__TextComponent = __TextComponent
from builtins import str
from pyquantum_helper import override
import it.unimi.dsi.fastutil.chars.CharPredicate as __CharPredicate
__CharPredicate = __CharPredicate
import java.lang.Object as __object
try:
    from pyquantum.client.gui import screens
except ImportError:
    screens = __import_once__("pyquantum.client.gui.screens")

import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import dev.ultreon.quantum.client.gui.screens.ChatScreen as __ChatScreen
__ChatScreen = __ChatScreen
import dev.ultreon.quantum.client.gui.widget.TextEntry as __TextEntry
__TextEntry = __TextEntry
import it.unimi.dsi.fastutil.chars.CharPredicate as CharPredicate
import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.client.gui.widget.ChatTextEntry as __ChatTextEntry
__ChatTextEntry = __ChatTextEntry
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as __CallbackComponent
__CallbackComponent = __CallbackComponent
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class ChatTextEntry():
    """dev.ultreon.quantum.client.gui.widget.ChatTextEntry"""
 
    @staticmethod
    def __wrap(java_value: __ChatTextEntry) -> 'ChatTextEntry':
        return ChatTextEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChatTextEntry):
        """
        Dynamic initializer for ChatTextEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @override
    @overload
    def revalidateCursor(self):
        """public void dev.ultreon.quantum.client.gui.widget.TextEntry.revalidateCursor()"""
        super(TextEntry, self).revalidateCursor()

    @override
    @overload
    def getCursorIdx(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.TextEntry.getCursorIdx()"""
        return int.__wrap(super(TextEntry, self).getCursorIdx())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def setCursorIdx(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.TextEntry.setCursorIdx(int)"""
        super(__TextEntry, self).setCursorIdx(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @overload
    def __init__(self, arg0: 'ChatScreen'):
        """public dev.ultreon.quantum.client.gui.widget.ChatTextEntry(dev.ultreon.quantum.client.gui.screens.ChatScreen)"""
        val = __ChatTextEntry(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def position(self, arg0: 'Supplier') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'TextEntry'.__wrap(super(__TextEntry, self).position(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ChatTextEntry.keyPress(int)"""
        return bool.__wrap(super(__ChatTextEntry, self).keyPress(__int.valueOf(arg0)))

    @overload
    def hint(self, arg0: 'TextObject') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.hint(dev.ultreon.quantum.text.TextObject)"""
        return 'TextEntry'.__wrap(super(__TextEntry, self).hint(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def callback(self, arg0: 'Callback') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.TextEntry>)"""
        return 'TextEntry'.__wrap(super(__TextEntry, self).callback(arg0))

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.ChatTextEntry.charType(char)"""
        return bool.__wrap(super(__ChatTextEntry, self).charType(__char.valueOf(arg0)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.TextEntry.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Widget'.__wrap(super(__TextEntry, self).bounds(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def hint(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.TextEntry.hint()"""
        return 'components.TextComponent'.__wrap(super(TextEntry, self).hint())

    @overload
    def filter(self, arg0: 'CharPredicate') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.filter(it.unimi.dsi.fastutil.chars.CharPredicate)"""
        return 'TextEntry'.__wrap(super(__TextEntry, self).filter(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TextEntry.getValue()"""
        return str.__wrap(super(TextEntry, self).getValue())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def getFilter(self) -> 'CharPredicate':
        """public it.unimi.dsi.fastutil.chars.CharPredicate dev.ultreon.quantum.client.gui.widget.TextEntry.getFilter()"""
        return 'CharPredicate'.__wrap(super(TextEntry, self).getFilter())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @staticmethod
    @overload
    def of(arg0: str) -> 'TextEntry':
        """public static dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.of(java.lang.String)"""
        return TextEntry.__wrap(__TextEntry.of(arg0))

    @overload
    def onTabComplete(self, arg0: 'String'):
        """public void dev.ultreon.quantum.client.gui.widget.ChatTextEntry.onTabComplete(java.lang.String[])"""
        super(__ChatTextEntry, self).onTabComplete(arg0)

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TextEntry.getName()"""
        return str.__wrap(super(TextEntry, self).getName())

    @overload
    def value(self, arg0: str) -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.value(java.lang.String)"""
        return 'TextEntry'.__wrap(super(__TextEntry, self).value(arg0))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<dev.ultreon.quantum.client.gui.widget.TextEntry> dev.ultreon.quantum.client.gui.widget.TextEntry.callback()"""
        return 'components.CallbackComponent'.__wrap(super(TextEntry, self).callback())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @staticmethod
    @overload
    def of() -> 'TextEntry':
        """public static dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.of()"""
        return TextEntry.__wrap(__TextEntry.of())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.ChatTextEntry.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__ChatTextEntry, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getScreen(self) -> 'screens.ChatScreen':
        """public dev.ultreon.quantum.client.gui.screens.ChatScreen dev.ultreon.quantum.client.gui.widget.ChatTextEntry.getScreen()"""
        return 'screens.ChatScreen'.__wrap(super(ChatTextEntry, self).getScreen())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.ChatTextEntry.onFocusLost()"""
        super(ChatTextEntry, self).onFocusLost() 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Slider
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = __import_once__("pyquantum.client.gui.widget.components")

import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import dev.ultreon.quantum.client.gui.widget.Slider as __Slider
__Slider = __Slider
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as __TextComponent
__TextComponent = __TextComponent
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent as __RangedValueComponent
__RangedValueComponent = __RangedValueComponent
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as __CallbackComponent
__CallbackComponent = __CallbackComponent
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class Slider():
    """dev.ultreon.quantum.client.gui.widget.Slider"""
 
    @staticmethod
    def __wrap(java_value: __Slider) -> 'Slider':
        return Slider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Slider):
        """
        Dynamic initializer for Slider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def text(self, arg0: str) -> 'Slider':
        """public dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.text(java.lang.String)"""
        return 'Slider'.__wrap(super(__Slider, self).text(arg0))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def text(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.Slider.text()"""
        return 'components.TextComponent'.__wrap(super(Slider, self).text())

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def value(self, arg0: int) -> 'Slider':
        """public dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.value(int)"""
        return 'Slider'.__wrap(super(__Slider, self).value(__int.valueOf(arg0)))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str.__wrap(super(Widget, self).getName())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def callback(self, arg0: 'Callback') -> 'Slider':
        """public dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.Slider>)"""
        return 'Slider'.__wrap(super(__Slider, self).callback(arg0))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.gui.widget.Slider(int,int,int)"""
        val = __Slider(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Slider.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Slider, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def value(self) -> 'components.RangedValueComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent dev.ultreon.quantum.client.gui.widget.Slider.value()"""
        return 'components.RangedValueComponent'.__wrap(super(Slider, self).value())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @overload
    def position(self, arg0: 'Supplier') -> 'Slider':
        """public dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Slider'.__wrap(super(__Slider, self).position(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Slider':
        """public dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Slider'.__wrap(super(__Slider, self).bounds(arg0))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<dev.ultreon.quantum.client.gui.widget.Slider> dev.ultreon.quantum.client.gui.widget.Slider.callback()"""
        return 'components.CallbackComponent'.__wrap(super(Slider, self).callback())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Slider.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Slider, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Slider.mousePress(int,int,int)"""
        return bool.__wrap(super(__Slider, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @overload
    def text(self, arg0: 'TextObject') -> 'Slider':
        """public dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.text(dev.ultreon.quantum.text.TextObject)"""
        return 'Slider'.__wrap(super(__Slider, self).text(arg0))

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.widget.Slider(int,int,int,int)"""
        val = __Slider(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @staticmethod
    @overload
    def of(arg0: int, arg1: int) -> 'Slider':
        """public static dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.of(int,int)"""
        return Slider.__wrap(__Slider.of(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @staticmethod
    @overload
    def of(arg0: int, arg1: int, arg2: int) -> 'Slider':
        """public static dev.ultreon.quantum.client.gui.widget.Slider dev.ultreon.quantum.client.gui.widget.Slider.of(int,int,int)"""
        return Slider.__wrap(__Slider.of(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.TabCompletePopup
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.gui.widget.TabCompletePopup as __TabCompletePopup
__TabCompletePopup = __TabCompletePopup
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TabCompletePopup():
    """dev.ultreon.quantum.client.gui.widget.TabCompletePopup"""
 
    @staticmethod
    def __wrap(java_value: __TabCompletePopup) -> 'TabCompletePopup':
        return TabCompletePopup(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TabCompletePopup):
        """
        Dynamic initializer for TabCompletePopup.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setValues(self, arg0: 'String'):
        """public void dev.ultreon.quantum.client.gui.widget.TabCompletePopup.setValues(java.lang.String[])"""
        super(__TabCompletePopup, self).setValues(arg0)

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.widget.TabCompletePopup(int,int)"""
        val = __TabCompletePopup(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def get(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TabCompletePopup.get()"""
        return str.__wrap(super(TabCompletePopup, self).get())

    @overload
    def down(self):
        """public void dev.ultreon.quantum.client.gui.widget.TabCompletePopup.down()"""
        super(TabCompletePopup, self).down()

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.TabCompletePopup.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__TabCompletePopup, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Tab
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = __import_once__("pyquantum.client.gui.widget.components")

import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import dev.ultreon.quantum.client.gui.Screen as __Screen
__Screen = __Screen
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import dev.ultreon.quantum.client.gui.widget.Tab as __Tab
__Tab = __Tab
import dev.ultreon.quantum.client.gui.widget.Button as __Button_Type
__Type = __Button_Type.Type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.screens.tabs.TabContent as __TabContent
__TabContent = __TabContent
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import dev.ultreon.quantum.client.gui.widget.Button as __Button
__Button = __Button
import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum.client.gui.screens import tabs
except ImportError:
    tabs = __import_once__("pyquantum.client.gui.screens.tabs")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as __CallbackComponent
__CallbackComponent = __CallbackComponent
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class Tab():
    """dev.ultreon.quantum.client.gui.widget.Tab"""
 
    @staticmethod
    def __wrap(java_value: __Tab) -> 'Tab':
        return Tab(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Tab):
        """
        Dynamic initializer for Tab.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def title(self, arg0: 'TextObject') -> 'Tab':
        """public dev.ultreon.quantum.client.gui.widget.Tab dev.ultreon.quantum.client.gui.widget.Tab.title(dev.ultreon.quantum.text.TextObject)"""
        return 'Tab'.__wrap(super(__Tab, self).title(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Tab.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Tab, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def index(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Tab.index()"""
        return int.__wrap(super(Tab, self).index())

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.click()"""
        return bool.__wrap(super(Button, self).click())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Button, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str.__wrap(super(Widget, self).getName())

    @overload
    def name(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.widget.Tab.name()"""
        return 'text.TextObject'.__wrap(super(Tab, self).name())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Tab.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Tab, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def screen(self) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.widget.Tab.screen()"""
        return 'gui.Screen'.__wrap(super(Tab, self).screen())

    @overload
    def type(self, arg0: 'Type') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.type(dev.ultreon.quantum.client.gui.widget.Button$Type)"""
        return 'Button'.__wrap(super(__Button, self).type(arg0))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mousePress(int,int,int)"""
        return bool.__wrap(super(__Button, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def selected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Tab.selected()"""
        return bool.__wrap(super(Tab, self).selected())

    @overload
    def __init__(self, arg0: 'TextObject', arg1: 'TabbedUI', arg2: bool, arg3: int, arg4: 'Consumer'):
        """public dev.ultreon.quantum.client.gui.widget.Tab(dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.client.gui.screens.tabs.TabbedUI,boolean,int,java.util.function.Consumer<dev.ultreon.quantum.client.gui.screens.tabs.TabBuilder>)"""
        val = __Tab(arg0, arg1, __boolean.valueOf(arg2), __int.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def content(self) -> 'tabs.TabContent':
        """public dev.ultreon.quantum.client.gui.screens.tabs.TabContent dev.ultreon.quantum.client.gui.widget.Tab.content()"""
        return 'tabs.TabContent'.__wrap(super(Tab, self).content())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<T> dev.ultreon.quantum.client.gui.widget.Button.callback()"""
        return 'components.CallbackComponent'.__wrap(super(Button, self).callback())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def title(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.widget.Tab.title()"""
        return 'text.TextObject'.__wrap(super(Tab, self).title())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @overload
    def icon(self, arg0: 'Identifier') -> 'Tab':
        """public dev.ultreon.quantum.client.gui.widget.Tab dev.ultreon.quantum.client.gui.widget.Tab.icon(dev.ultreon.quantum.util.Identifier)"""
        return 'Tab'.__wrap(super(__Tab, self).icon(arg0))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def position(self, arg0: 'Supplier') -> 'Tab':
        """public dev.ultreon.quantum.client.gui.widget.Tab dev.ultreon.quantum.client.gui.widget.Tab.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Tab'.__wrap(super(__Tab, self).position(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def bottom(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Tab.bottom()"""
        return bool.__wrap(super(Tab, self).bottom())

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @override
    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.isPressed()"""
        return bool.__wrap(super(Button, self).isPressed())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button.type()"""
        return 'Type'.__wrap(super(Button, self).type())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def callback(self, arg0: 'Callback') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.callback(dev.ultreon.quantum.client.gui.Callback<T>)"""
        return 'Button'.__wrap(super(__Button, self).callback(arg0))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Tab.revalidate()"""
        super(Tab, self).revalidate()

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Tab':
        """public dev.ultreon.quantum.client.gui.widget.Tab dev.ultreon.quantum.client.gui.widget.Tab.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Tab'.__wrap(super(__Tab, self).bounds(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Button
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = __import_once__("pyquantum.client.gui.widget.components")

import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import dev.ultreon.quantum.client.gui.widget.Button as __Button_Type
__Type = __Button_Type.Type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import dev.ultreon.quantum.client.gui.widget.Button as __Button
__Button = __Button
import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as __CallbackComponent
__CallbackComponent = __CallbackComponent
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class Button(ABC):
    """dev.ultreon.quantum.client.gui.widget.Button"""
 
    @staticmethod
    def __wrap(java_value: __Button) -> 'Button':
        return Button(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Button):
        """
        Dynamic initializer for Button.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @abstractmethod
    def position(self, arg0: 'Supplier'):
        """public abstract dev.ultreon.quantum.client.gui.widget.Button<T> dev.ultreon.quantum.client.gui.widget.Button.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        pass

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Button, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def bounds(self, arg0: 'Supplier'):
        """public abstract dev.ultreon.quantum.client.gui.widget.Button<T> dev.ultreon.quantum.client.gui.widget.Button.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        pass

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button.type()"""
        return 'Type'.__wrap(super(Button, self).type())

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str.__wrap(super(Widget, self).getName())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.click()"""
        return bool.__wrap(super(Button, self).click())

    @overload
    def type(self, arg0: 'Type') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.type(dev.ultreon.quantum.client.gui.widget.Button$Type)"""
        return 'Button'.__wrap(super(__Button, self).type(arg0))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mousePress(int,int,int)"""
        return bool.__wrap(super(__Button, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<T> dev.ultreon.quantum.client.gui.widget.Button.callback()"""
        return 'components.CallbackComponent'.__wrap(super(Button, self).callback())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Button, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.isPressed()"""
        return bool.__wrap(super(Button, self).isPressed())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def callback(self, arg0: 'Callback') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.callback(dev.ultreon.quantum.client.gui.Callback<T>)"""
        return 'Button'.__wrap(super(__Button, self).callback(arg0))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget_RevalidateListener
__RevalidateListener = __Widget_RevalidateListener.RevalidateListener
from abc import abstractmethod, ABC
 
class RevalidateListener(ABC):
    """dev.ultreon.quantum.client.gui.widget.Widget.RevalidateListener"""
 
    @staticmethod
    def __wrap(java_value: __RevalidateListener) -> 'RevalidateListener':
        return RevalidateListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RevalidateListener):
        """
        Dynamic initializer for RevalidateListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def revalidate(self, arg0: 'Widget'):
        """public abstract void dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener.revalidate(dev.ultreon.quantum.client.gui.widget.Widget)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Button$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.gui.widget.Button as __Button_Type
__Type = __Button_Type.Type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Type():
    """dev.ultreon.quantum.client.gui.widget.Button.Type"""
 
    @staticmethod
    def __wrap(java_value: __Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Type):
        """
        Dynamic initializer for Type.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button$Type.LIGHT_EMBED
    LIGHT_EMBED: 'Type' = __wrap(__Type.LIGHT_EMBED)

    # public static final dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button$Type.DARK
    DARK: 'Type' = __wrap(__Type.DARK)

    # public static final dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button$Type.DARK_EMBED
    DARK_EMBED: 'Type' = __wrap(__Type.DARK_EMBED)

    # public static final dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button$Type.LIGHT
    LIGHT: 'Type' = __wrap(__Type.LIGHT)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static dev.ultreon.quantum.client.gui.widget.Button$Type[] dev.ultreon.quantum.client.gui.widget.Button$Type.values()"""
        return List[Type].__wrap(__Type.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button$Type.valueOf(java.lang.String)"""
        return Type.__wrap(__Type.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Widget
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class Widget(ABC):
    """dev.ultreon.quantum.client.gui.widget.Widget"""
 
    @staticmethod
    def __wrap(java_value: __Widget) -> 'Widget':
        return Widget(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Widget):
        """
        Dynamic initializer for Widget.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @abstractmethod
    def bounds(self, arg0: 'Supplier'):
        """public abstract dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.Widget.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        pass

    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str.__wrap(super(Widget, self).getName())

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @abstractmethod
    def position(self, arg0: 'Supplier'):
        """public abstract dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.Widget.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        pass

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.CycleButton
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = __import_once__("pyquantum.client.gui.widget.components")

import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import dev.ultreon.quantum.client.gui.widget.Button as __Button_Type
__Type = __Button_Type.Type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import dev.ultreon.quantum.client.gui.widget.CycleButton as __CycleButton
__CycleButton = __CycleButton
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as __TextComponent
__TextComponent = __TextComponent
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import dev.ultreon.quantum.client.gui.widget.Button as __Button
__Button = __Button
import java.nio.file.Path as Path
from builtins import object
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.client.gui.widget.components.ColorComponent as __ColorComponent
__ColorComponent = __ColorComponent
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as __CallbackComponent
__CallbackComponent = __CallbackComponent
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class CycleButton():
    """dev.ultreon.quantum.client.gui.widget.CycleButton"""
 
    @staticmethod
    def __wrap(java_value: __CycleButton) -> 'CycleButton':
        return CycleButton(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CycleButton):
        """
        Dynamic initializer for CycleButton.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @overload
    def __init__(self, arg0: int, arg1: 'MutableText'):
        """public dev.ultreon.quantum.client.gui.widget.CycleButton(int,dev.ultreon.quantum.text.MutableText)"""
        val = __CycleButton(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @overload
    def getLabel(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.widget.CycleButton.getLabel()"""
        return 'text.TextObject'.__wrap(super(CycleButton, self).getLabel())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @overload
    def textColor(self) -> 'components.ColorComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.ColorComponent dev.ultreon.quantum.client.gui.widget.CycleButton.textColor()"""
        return 'components.ColorComponent'.__wrap(super(CycleButton, self).textColor())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Button, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def labelTranslation(self, arg0: str, *arg1: object) -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.labelTranslation(java.lang.String,java.lang.Object...)"""
        return 'CycleButton'.__wrap(super(__CycleButton, self).labelTranslation(arg0, arg1))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @overload
    def getRawLabel(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.CycleButton.getRawLabel()"""
        return str.__wrap(super(CycleButton, self).getRawLabel())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'MutableText'):
        """public dev.ultreon.quantum.client.gui.widget.CycleButton(int,int,dev.ultreon.quantum.text.MutableText)"""
        val = __CycleButton(__int.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.CycleButton.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__CycleButton, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str.__wrap(super(Widget, self).getName())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.client.gui.widget.CycleButton.getValue()"""
        return object.__wrap(super(CycleButton, self).getValue())

    @overload
    def type(self, arg0: 'Type') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.type(dev.ultreon.quantum.client.gui.widget.Button$Type)"""
        return 'Button'.__wrap(super(__Button, self).type(arg0))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mousePress(int,int,int)"""
        return bool.__wrap(super(__Button, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.CycleButton.getIndex()"""
        return int.__wrap(super(CycleButton, self).getIndex())

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.CycleButton.click()"""
        return bool.__wrap(super(CycleButton, self).click())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def label(self, arg0: str) -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.label(java.lang.String)"""
        return 'CycleButton'.__wrap(super(__CycleButton, self).label(arg0))

    @overload
    def formatter(self, arg0: 'Function') -> 'CycleButton':
        """public final dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.formatter(java.util.function.Function<T, dev.ultreon.quantum.text.TextObject>)"""
        return 'CycleButton'.__wrap(super(__CycleButton, self).formatter(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def text(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.CycleButton.text()"""
        return 'components.TextComponent'.__wrap(super(CycleButton, self).text())

    @overload
    def label(self, arg0: 'TextObject') -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.label(dev.ultreon.quantum.text.TextObject)"""
        return 'CycleButton'.__wrap(super(__CycleButton, self).label(arg0))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @overload
    def value(self, arg0: object) -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.value(T)"""
        return 'CycleButton'.__wrap(super(__CycleButton, self).value(arg0))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.CycleButton.revalidate()"""
        super(CycleButton, self).revalidate()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Button, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<T> dev.ultreon.quantum.client.gui.widget.Button.callback()"""
        return 'components.CallbackComponent'.__wrap(super(Button, self).callback())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @overload
    def index(self, arg0: int) -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.index(int)"""
        return 'CycleButton'.__wrap(super(__CycleButton, self).index(__int.valueOf(arg0)))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'CycleButton'.__wrap(super(__CycleButton, self).bounds(arg0))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @overload
    def position(self, arg0: 'Supplier') -> 'CycleButton':
        """public dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'CycleButton'.__wrap(super(__CycleButton, self).position(arg0))

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @override
    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.isPressed()"""
        return bool.__wrap(super(Button, self).isPressed())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.CycleButton()"""
        val = __CycleButton()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button.type()"""
        return 'Type'.__wrap(super(Button, self).type())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.CycleButton()"""
        val = __CycleButton()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def callback(self, arg0: 'Callback') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.callback(dev.ultreon.quantum.client.gui.Callback<T>)"""
        return 'Button'.__wrap(super(__Button, self).callback(arg0))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @overload
    def values(self, *arg0: object) -> 'CycleButton':
        """public final dev.ultreon.quantum.client.gui.widget.CycleButton<T> dev.ultreon.quantum.client.gui.widget.CycleButton.values(T...)"""
        return 'CycleButton'.__wrap(super(__CycleButton, self).values(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Rectangle
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = __import_once__("pyquantum.client.gui.widget.components")

import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
from builtins import bool
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.client.gui.widget.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.client.gui.widget.components.ColorComponent as __ColorComponent
__ColorComponent = __ColorComponent
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class Rectangle():
    """dev.ultreon.quantum.client.gui.widget.Rectangle"""
 
    @staticmethod
    def __wrap(java_value: __Rectangle) -> 'Rectangle':
        return Rectangle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Rectangle):
        """
        Dynamic initializer for Rectangle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def create() -> 'Rectangle':
        """public static dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.create()"""
        return Rectangle.__wrap(__Rectangle.create())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mousePress(int,int,int)"""
        return bool.__wrap(super(__Rectangle, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Rectangle, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.Rectangle()"""
        val = __Rectangle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Rectangle, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def backgroundColor(self, arg0: 'RgbColor') -> 'Rectangle':
        """public dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.backgroundColor(dev.ultreon.quantum.util.RgbColor)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).backgroundColor(arg0))

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.Rectangle()"""
        val = __Rectangle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.widget.Rectangle(int,int,int,int)"""
        val = __Rectangle(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def position(self, arg0: 'Supplier') -> 'Rectangle':
        """public dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).position(arg0))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Rectangle':
        """public dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).bounds(arg0))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Rectangle.getName()"""
        return str.__wrap(super(Rectangle, self).getName())

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @staticmethod
    @overload
    def of(arg0: int, arg1: int, arg2: int, arg3: int) -> 'Rectangle':
        """public static dev.ultreon.quantum.client.gui.widget.Rectangle dev.ultreon.quantum.client.gui.widget.Rectangle.of(int,int,int,int)"""
        return Rectangle.__wrap(__Rectangle.of(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @overload
    def backgroundColor(self) -> 'components.ColorComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.ColorComponent dev.ultreon.quantum.client.gui.widget.Rectangle.backgroundColor()"""
        return 'components.ColorComponent'.__wrap(super(Rectangle, self).backgroundColor())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Rectangle.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Rectangle, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Rectangle.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Rectangle, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.TextButton
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = __import_once__("pyquantum.client.gui.widget.components")

import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import dev.ultreon.quantum.client.gui.widget.Button as __Button_Type
__Type = __Button_Type.Type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as __TextComponent
__TextComponent = __TextComponent
from builtins import bool
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.client.gui.widget.TextButton as __TextButton
__TextButton = __TextButton
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import dev.ultreon.quantum.client.gui.widget.Button as __Button
__Button = __Button
import java.nio.file.Path as Path
from builtins import object
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.client.gui.widget.components.ColorComponent as __ColorComponent
__ColorComponent = __ColorComponent
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as __CallbackComponent
__CallbackComponent = __CallbackComponent
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class TextButton():
    """dev.ultreon.quantum.client.gui.widget.TextButton"""
 
    @staticmethod
    def __wrap(java_value: __TextButton) -> 'TextButton':
        return TextButton(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextButton):
        """
        Dynamic initializer for TextButton.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.click()"""
        return bool.__wrap(super(Button, self).click())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Button, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.TextButton.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__TextButton, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def text(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.TextButton.text()"""
        return 'components.TextComponent'.__wrap(super(TextButton, self).text())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @staticmethod
    @overload
    def of(arg0: 'TextObject') -> 'TextButton':
        """public static dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.of(dev.ultreon.quantum.text.TextObject)"""
        return TextButton.__wrap(__TextButton.of(arg0))

    @overload
    def type(self, arg0: 'Type') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.type(dev.ultreon.quantum.client.gui.widget.Button$Type)"""
        return 'Button'.__wrap(super(__Button, self).type(arg0))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def callback(self, arg0: 'Callback') -> 'TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.TextButton>)"""
        return 'TextButton'.__wrap(super(__TextButton, self).callback(arg0))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mousePress(int,int,int)"""
        return bool.__wrap(super(__Button, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def of(arg0: str) -> 'TextButton':
        """public static dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.of(java.lang.String)"""
        return TextButton.__wrap(__TextButton.of(arg0))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def of(arg0: str, arg1: int) -> 'TextButton':
        """public static dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.of(java.lang.String,int)"""
        return TextButton.__wrap(__TextButton.of(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: 'Supplier') -> 'TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'TextButton'.__wrap(super(__TextButton, self).position(arg0))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Button, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<T> dev.ultreon.quantum.client.gui.widget.Button.callback()"""
        return 'components.CallbackComponent'.__wrap(super(Button, self).callback())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'TextButton'.__wrap(super(__TextButton, self).bounds(arg0))

    @overload
    def translation(self, arg0: str, *arg1: object) -> 'TextButton':
        """public dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.translation(java.lang.String,java.lang.Object...)"""
        return 'TextButton'.__wrap(super(__TextButton, self).translation(arg0, arg1))

    @staticmethod
    @overload
    def of(arg0: 'TextObject', arg1: int) -> 'TextButton':
        """public static dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.of(dev.ultreon.quantum.text.TextObject,int)"""
        return TextButton.__wrap(__TextButton.of(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @override
    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.isPressed()"""
        return bool.__wrap(super(Button, self).isPressed())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button.type()"""
        return 'Type'.__wrap(super(Button, self).type())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @staticmethod
    @overload
    def of(arg0: 'TextObject', arg1: int, arg2: int) -> 'TextButton':
        """public static dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.of(dev.ultreon.quantum.text.TextObject,int,int)"""
        return TextButton.__wrap(__TextButton.of(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @overload
    def textColor(self) -> 'components.ColorComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.ColorComponent dev.ultreon.quantum.client.gui.widget.TextButton.textColor()"""
        return 'components.ColorComponent'.__wrap(super(TextButton, self).textColor())

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @staticmethod
    @overload
    def of(arg0: str, arg1: int, arg2: int) -> 'TextButton':
        """public static dev.ultreon.quantum.client.gui.widget.TextButton dev.ultreon.quantum.client.gui.widget.TextButton.of(java.lang.String,int,int)"""
        return TextButton.__wrap(__TextButton.of(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.TextButton.isClickable()"""
        return bool.__wrap(super(TextButton, self).isClickable())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TextButton.getName()"""
        return str.__wrap(super(TextButton, self).getName()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.WorldCardList
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import java.util.function.Predicate as Predicate
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import dev.ultreon.quantum.client.gui.widget.WorldCardList as __WorldCardList
__WorldCardList = __WorldCardList
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.gui.widget.HorizontalList as __HorizontalList
__HorizontalList = __HorizontalList
import java.lang.Object as __Object
__Object = __Object
import java.util.function.IntSupplier as IntSupplier
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.widget.HorizontalList as __HorizontalList_Entry
__Entry = __HorizontalList_Entry.Entry
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import dev.ultreon.quantum.client.gui.widget.WorldCardList as __WorldCardList_Entry
__Entry = __WorldCardList_Entry.Entry
import java.util.List as List
from builtins import int
 
class WorldCardList():
    """dev.ultreon.quantum.client.gui.widget.WorldCardList"""
 
    @staticmethod
    def __wrap(java_value: __WorldCardList) -> 'WorldCardList':
        return WorldCardList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldCardList):
        """
        Dynamic initializer for WorldCardList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'UIContainer' = __wrap(__UIContainer.ROOT)


    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'Widget') -> 'Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'Widget'.__wrap(super(__UIContainer, self).add(arg0))

    @overload
    def position(self, arg0: 'Supplier') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'WorldCardList'.__wrap(super(__WorldCardList, self).position(arg0))

    @overload
    def worlds(self, arg0: 'List') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.worlds(java.util.List<dev.ultreon.quantum.world.WorldStorage>)"""
        return 'WorldCardList'.__wrap(super(__WorldCardList, self).worlds(arg0))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(UIContainer, self).getWidgets())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def xOffset(self, arg0: int) -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.xOffset(int)"""
        return 'WorldCardList'.__wrap(super(__WorldCardList, self).xOffset(__int.valueOf(arg0)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__HorizontalList, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def entries(self, arg0: 'Collection') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.entries(java.util.Collection<? extends dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry>)"""
        return 'WorldCardList'.__wrap(super(__WorldCardList, self).entries(arg0))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.revalidate()"""
        super(HorizontalList, self).revalidate()

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'Widget'.__wrap(super(__UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def itemHeight(self, arg0: int) -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.itemHeight(int)"""
        return 'WorldCardList'.__wrap(super(__WorldCardList, self).itemHeight(__int.valueOf(arg0)))

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseMove(int,int)"""
        super(__HorizontalList, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__HorizontalList, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def itemRenderer(self, arg0: 'ItemRenderer') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.itemRenderer(dev.ultreon.quantum.client.gui.widget.HorizontalList$ItemRenderer<dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry>)"""
        return 'WorldCardList'.__wrap(super(__WorldCardList, self).itemRenderer(arg0))

    @overload
    def selectable(self, arg0: bool) -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.selectable(boolean)"""
        return 'WorldCardList'.__wrap(super(__WorldCardList, self).selectable(__boolean.valueOf(arg0)))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def getXOffset(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getXOffset()"""
        return int.__wrap(super(HorizontalList, self).getXOffset())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @override
    @overload
    def removeEntry(self, arg0: 'Entry'):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.removeEntry(T)"""
        super(__HorizontalList, self).removeEntry(arg0)

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def callback(self, arg0: 'Callback') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry>)"""
        return 'WorldCardList'.__wrap(super(__WorldCardList, self).callback(arg0))

    @override
    @overload
    def setGap(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.setGap(int)"""
        super(__HorizontalList, self).setGap(__int.valueOf(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__HorizontalList, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__UIContainer, self).setLayout(arg0)

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getItemHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getItemHeight()"""
        return int.__wrap(super(HorizontalList, self).getItemHeight())

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool.__wrap(super(__UIContainer, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def scrollDelta(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.scrollDelta(int)"""
        super(__HorizontalList, self).scrollDelta(__int.valueOf(arg0))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(UIContainer, self).getLayout())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool.__wrap(super(__UIContainer, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def isSelectable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.isSelectable()"""
        return bool.__wrap(super(HorizontalList, self).isSelectable())

    @overload
    def getEntryAt(self, arg0: int, arg1: int) -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.getEntryAt(int,int)"""
        return 'Entry'.__wrap(super(__HorizontalList, self).getEntryAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__HorizontalList, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def entry(self, arg0: 'Entry') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry dev.ultreon.quantum.client.gui.widget.WorldCardList.entry(dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry)"""
        return 'Entry'.__wrap(super(__WorldCardList, self).entry(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'Widget'.__wrap(super(__UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__HorizontalList, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def itemWidth(self, arg0: int) -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.itemWidth(int)"""
        return 'WorldCardList'.__wrap(super(__WorldCardList, self).itemWidth(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def gap(self, arg0: int) -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.gap(int)"""
        return 'WorldCardList'.__wrap(super(__WorldCardList, self).gap(__int.valueOf(arg0)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.HorizontalList.getName()"""
        return str.__wrap(super(HorizontalList, self).getName())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def bounds(self, arg0: 'Supplier') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'WorldCardList'.__wrap(super(__WorldCardList, self).bounds(arg0))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__HorizontalList, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.HorizontalList.mousePress(int,int,int)"""
        return bool.__wrap(super(__HorizontalList, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def getContentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getContentHeight()"""
        return int.__wrap(super(HorizontalList, self).getContentHeight())

    @override
    @overload
    def removeEntryIf(self, arg0: 'Predicate'):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.removeEntryIf(java.util.function.Predicate<T>)"""
        super(__HorizontalList, self).removeEntryIf(arg0)

    @override
    @overload
    def scroll(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.scroll(int)"""
        super(__HorizontalList, self).scroll(__int.valueOf(arg0))

    @override
    @overload
    def mouseExit(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseExit()"""
        super(HorizontalList, self).mouseExit()

    @override
    @overload
    def getSelected(self) -> 'Entry':
        """public T dev.ultreon.quantum.client.gui.widget.HorizontalList.getSelected()"""
        return 'Entry'.__wrap(super(HorizontalList, self).getSelected())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @staticmethod
    @overload
    def create(arg0: 'IntSupplier') -> 'WorldCardList':
        """public static dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.create(java.util.function.IntSupplier)"""
        return WorldCardList.__wrap(__WorldCardList.create(arg0))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getItemWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getItemWidth()"""
        return int.__wrap(super(HorizontalList, self).getItemWidth())

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setXOffset(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.setXOffset(int)"""
        super(__HorizontalList, self).setXOffset(__int.valueOf(arg0))

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @override
    @overload
    def getGap(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.HorizontalList.getGap()"""
        return int.__wrap(super(HorizontalList, self).getGap())

    @override
    @overload
    def mouseEnter(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList.mouseEnter(int,int)"""
        super(__HorizontalList, self).mouseEnter(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<T> dev.ultreon.quantum.client.gui.widget.HorizontalList.children()"""
        return 'List'.__wrap(super(HorizontalList, self).children())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyPress(int)"""
        return bool.__wrap(super(__UIContainer, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__UIContainer, self).remove(arg0)

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @overload
    def count(self, arg0: 'IntSupplier') -> 'WorldCardList':
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList dev.ultreon.quantum.client.gui.widget.WorldCardList.count(java.util.function.IntSupplier)"""
        return 'WorldCardList'.__wrap(super(__WorldCardList, self).count(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.StaticWidget
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.gui.widget.StaticWidget as __StaticWidget
__StaticWidget = __StaticWidget
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class StaticWidget(ABC):
    """dev.ultreon.quantum.client.gui.widget.StaticWidget"""
 
    @staticmethod
    def __wrap(java_value: __StaticWidget) -> 'StaticWidget':
        return StaticWidget(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StaticWidget):
        """
        Dynamic initializer for StaticWidget.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public abstract void dev.ultreon.quantum.client.gui.widget.StaticWidget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.world.WorldStorage as __WorldStorage
__WorldStorage = __WorldStorage
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.widget.HorizontalList as __HorizontalList_Entry
__Entry = __HorizontalList_Entry.Entry
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import dev.ultreon.quantum.client.gui.widget.WorldCardList as __WorldCardList_Entry
__Entry = __WorldCardList_Entry.Entry
from builtins import int
 
class Entry():
    """dev.ultreon.quantum.client.gui.widget.WorldCardList.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.isPressed()"""
        return bool.__wrap(super(Entry, self).isPressed())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Entry, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Entry'.__wrap(super(__Entry, self).bounds(arg0))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.click()"""
        return bool.__wrap(super(Entry, self).click())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Entry, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def __init__(self, arg0: 'WorldCardList', arg1: 'WorldStorage'):
        """public dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry(dev.ultreon.quantum.client.gui.widget.WorldCardList,dev.ultreon.quantum.world.WorldStorage)"""
        val = __Entry(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def select(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.select(boolean)"""
        super(__Entry, self).select(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @override
    @overload
    def renderEntry(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: float):
        """public void dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.renderEntry(dev.ultreon.quantum.client.gui.Renderer,int,int,int,int,boolean,float)"""
        super(__Entry, self).renderEntry(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5), __float.valueOf(arg6))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.mouseMove(int,int)"""
        super(__Entry, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.keyPress(int)"""
        return bool.__wrap(super(__Entry, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Entry, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def getWorld(self) -> 'world.WorldStorage':
        """public dev.ultreon.quantum.world.WorldStorage dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.getWorld()"""
        return 'world.WorldStorage'.__wrap(super(Entry, self).getWorld())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @overload
    def position(self, arg0: 'Supplier') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Entry'.__wrap(super(__Entry, self).position(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.getName()"""
        return str.__wrap(super(Entry, self).getName())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.mousePress(int,int,int)"""
        return bool.__wrap(super(__Entry, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def select(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.select()"""
        super(Entry, self).select()

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: bool, arg4: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.render(dev.ultreon.quantum.client.gui.Renderer,int,int,boolean,float)"""
        super(__Entry, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.revalidate()"""
        super(Entry, self).revalidate()

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Entry, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.WorldCardList$Entry.keyRelease(int)"""
        return bool.__wrap(super(__Entry, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.widget.HorizontalList as __HorizontalList_Entry
__Entry = __HorizontalList_Entry.Entry
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class Entry(ABC):
    """dev.ultreon.quantum.client.gui.widget.HorizontalList.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Entry'.__wrap(super(__Entry, self).bounds(arg0))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @abstractmethod
    def renderEntry(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: float):
        """public abstract void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.renderEntry(dev.ultreon.quantum.client.gui.Renderer,int,int,int,int,boolean,float)"""
        pass

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def select(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.select(boolean)"""
        super(__Entry, self).select(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: bool, arg4: float):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.render(dev.ultreon.quantum.client.gui.Renderer,int,int,boolean,float)"""
        super(__Entry, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'HorizontalList'):
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry(dev.ultreon.quantum.client.gui.widget.HorizontalList<?>)"""
        val = __Entry(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @overload
    def position(self, arg0: 'Supplier') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Entry'.__wrap(super(__Entry, self).position(arg0))

    @overload
    def select(self):
        """public void dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.select()"""
        super(Entry, self).select()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.HorizontalList$Entry.getName()"""
        return str.__wrap(super(Entry, self).getName())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.TextEntry
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = __import_once__("pyquantum.client.gui.widget.components")

import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as __TextComponent
__TextComponent = __TextComponent
from builtins import bool
from builtins import str
from pyquantum_helper import override
import it.unimi.dsi.fastutil.chars.CharPredicate as __CharPredicate
__CharPredicate = __CharPredicate
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import dev.ultreon.quantum.client.gui.widget.TextEntry as __TextEntry
__TextEntry = __TextEntry
import it.unimi.dsi.fastutil.chars.CharPredicate as CharPredicate
import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as __CallbackComponent
__CallbackComponent = __CallbackComponent
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class TextEntry():
    """dev.ultreon.quantum.client.gui.widget.TextEntry"""
 
    @staticmethod
    def __wrap(java_value: __TextEntry) -> 'TextEntry':
        return TextEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextEntry):
        """
        Dynamic initializer for TextEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def revalidateCursor(self):
        """public void dev.ultreon.quantum.client.gui.widget.TextEntry.revalidateCursor()"""
        super(TextEntry, self).revalidateCursor()

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.TextEntry.charType(char)"""
        return bool.__wrap(super(__TextEntry, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @overload
    def position(self, arg0: 'Supplier') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'TextEntry'.__wrap(super(__TextEntry, self).position(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def hint(self, arg0: 'TextObject') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.hint(dev.ultreon.quantum.text.TextObject)"""
        return 'TextEntry'.__wrap(super(__TextEntry, self).hint(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def callback(self, arg0: 'Callback') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.TextEntry>)"""
        return 'TextEntry'.__wrap(super(__TextEntry, self).callback(arg0))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def setCursorIdx(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.TextEntry.setCursorIdx(int)"""
        super(__TextEntry, self).setCursorIdx(__int.valueOf(arg0))

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def getFilter(self) -> 'CharPredicate':
        """public it.unimi.dsi.fastutil.chars.CharPredicate dev.ultreon.quantum.client.gui.widget.TextEntry.getFilter()"""
        return 'CharPredicate'.__wrap(super(TextEntry, self).getFilter())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @overload
    def getValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TextEntry.getValue()"""
        return str.__wrap(super(TextEntry, self).getValue())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.TextEntry()"""
        val = __TextEntry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.TextEntry.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Widget'.__wrap(super(__TextEntry, self).bounds(arg0))

    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<dev.ultreon.quantum.client.gui.widget.TextEntry> dev.ultreon.quantum.client.gui.widget.TextEntry.callback()"""
        return 'components.CallbackComponent'.__wrap(super(TextEntry, self).callback())

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @overload
    def filter(self, arg0: 'CharPredicate') -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.filter(it.unimi.dsi.fastutil.chars.CharPredicate)"""
        return 'TextEntry'.__wrap(super(__TextEntry, self).filter(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.TextEntry.keyPress(int)"""
        return bool.__wrap(super(__TextEntry, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.widget.TextEntry(int)"""
        val = __TextEntry(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def hint(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.TextEntry.hint()"""
        return 'components.TextComponent'.__wrap(super(TextEntry, self).hint())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @staticmethod
    @overload
    def of(arg0: str) -> 'TextEntry':
        """public static dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.of(java.lang.String)"""
        return TextEntry.__wrap(__TextEntry.of(arg0))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.TextEntry()"""
        val = __TextEntry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TextEntry.getName()"""
        return str.__wrap(super(TextEntry, self).getName())

    @overload
    def value(self, arg0: str) -> 'TextEntry':
        """public dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.value(java.lang.String)"""
        return 'TextEntry'.__wrap(super(__TextEntry, self).value(arg0))

    @overload
    def getCursorIdx(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.TextEntry.getCursorIdx()"""
        return int.__wrap(super(TextEntry, self).getCursorIdx())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.TextEntry.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__TextEntry, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @staticmethod
    @overload
    def of() -> 'TextEntry':
        """public static dev.ultreon.quantum.client.gui.widget.TextEntry dev.ultreon.quantum.client.gui.widget.TextEntry.of()"""
        return TextEntry.__wrap(__TextEntry.of())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.widget.TextEntry(int,int)"""
        val = __TextEntry(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.TitleButton
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = __import_once__("pyquantum.client.gui.widget.components")

import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import dev.ultreon.quantum.client.gui.widget.Button as __Button_Type
__Type = __Button_Type.Type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import dev.ultreon.quantum.client.gui.widget.TitleButton as __TitleButton
__TitleButton = __TitleButton
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as __TextComponent
__TextComponent = __TextComponent
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import dev.ultreon.quantum.client.gui.widget.Button as __Button
__Button = __Button
import java.nio.file.Path as Path
from builtins import object
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.client.gui.widget.components.ColorComponent as __ColorComponent
__ColorComponent = __ColorComponent
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as __CallbackComponent
__CallbackComponent = __CallbackComponent
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class TitleButton():
    """dev.ultreon.quantum.client.gui.widget.TitleButton"""
 
    @staticmethod
    def __wrap(java_value: __TitleButton) -> 'TitleButton':
        return TitleButton(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TitleButton):
        """
        Dynamic initializer for TitleButton.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def of(arg0: str) -> 'TitleButton':
        """public static dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.of(java.lang.String)"""
        return TitleButton.__wrap(__TitleButton.of(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.TitleButton.isClickable()"""
        return bool.__wrap(super(TitleButton, self).isClickable())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def click(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.click()"""
        return bool.__wrap(super(Button, self).click())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Button, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def of(arg0: str, arg1: int, arg2: int) -> 'TitleButton':
        """public static dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.of(java.lang.String,int,int)"""
        return TitleButton.__wrap(__TitleButton.of(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @overload
    def getIcon(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.widget.TitleButton.getIcon()"""
        return 'util.Identifier'.__wrap(super(TitleButton, self).getIcon())

    @staticmethod
    @overload
    def of(arg0: 'TextObject') -> 'TitleButton':
        """public static dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.of(dev.ultreon.quantum.text.TextObject)"""
        return TitleButton.__wrap(__TitleButton.of(arg0))

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @staticmethod
    @overload
    def of(arg0: str, arg1: int) -> 'TitleButton':
        """public static dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.of(java.lang.String,int)"""
        return TitleButton.__wrap(__TitleButton.of(arg0, __int.valueOf(arg1)))

    @overload
    def type(self, arg0: 'Type') -> 'Button':
        """public T dev.ultreon.quantum.client.gui.widget.Button.type(dev.ultreon.quantum.client.gui.widget.Button$Type)"""
        return 'Button'.__wrap(super(__Button, self).type(arg0))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def icon(self, arg0: 'Identifier') -> 'TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.icon(dev.ultreon.quantum.util.Identifier)"""
        return 'TitleButton'.__wrap(super(__TitleButton, self).icon(arg0))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mousePress(int,int,int)"""
        return bool.__wrap(super(__Button, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def of(arg0: 'TextObject', arg1: int) -> 'TitleButton':
        """public static dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.of(dev.ultreon.quantum.text.TextObject,int)"""
        return TitleButton.__wrap(__TitleButton.of(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Button, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @overload
    def callback(self, arg0: 'Callback') -> 'TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.callback(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.widget.TitleButton>)"""
        return 'TitleButton'.__wrap(super(__TitleButton, self).callback(arg0))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @override
    @overload
    def callback(self) -> 'components.CallbackComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent<T> dev.ultreon.quantum.client.gui.widget.Button.callback()"""
        return 'components.CallbackComponent'.__wrap(super(Button, self).callback())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.TitleButton.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__TitleButton, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @overload
    def translation(self, arg0: str, *arg1: object) -> 'TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.translation(java.lang.String,java.lang.Object...)"""
        return 'TitleButton'.__wrap(super(__TitleButton, self).translation(arg0, arg1))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.TitleButton.getName()"""
        return str.__wrap(super(TitleButton, self).getName())

    @overload
    def text(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.TitleButton.text()"""
        return 'components.TextComponent'.__wrap(super(TitleButton, self).text())

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def position(self, arg0: 'Supplier') -> 'TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'TitleButton'.__wrap(super(__TitleButton, self).position(arg0))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def textColor(self) -> 'components.ColorComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.ColorComponent dev.ultreon.quantum.client.gui.widget.TitleButton.textColor()"""
        return 'components.ColorComponent'.__wrap(super(TitleButton, self).textColor())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @override
    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Button.isPressed()"""
        return bool.__wrap(super(Button, self).isPressed())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'TitleButton':
        """public dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'TitleButton'.__wrap(super(__TitleButton, self).bounds(arg0))

    @override
    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.gui.widget.Button$Type dev.ultreon.quantum.client.gui.widget.Button.type()"""
        return 'Type'.__wrap(super(Button, self).type())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @staticmethod
    @overload
    def of(arg0: 'TextObject', arg1: int, arg2: int) -> 'TitleButton':
        """public static dev.ultreon.quantum.client.gui.widget.TitleButton dev.ultreon.quantum.client.gui.widget.TitleButton.of(dev.ultreon.quantum.text.TextObject,int,int)"""
        return TitleButton.__wrap(__TitleButton.of(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.SelectionList$Entry
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.SelectionList as __SelectionList_Entry
__Entry = __SelectionList_Entry.Entry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import java.nio.file.Path as Path
from builtins import object
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class Entry():
    """dev.ultreon.quantum.client.gui.widget.SelectionList.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.getValue()"""
        return object.__wrap(super(Entry, self).getValue())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: int, arg4: bool, arg5: float):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.render(dev.ultreon.quantum.client.gui.Renderer,int,int,int,boolean,float)"""
        super(__Entry, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4), __float.valueOf(arg5))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.getName()"""
        return str.__wrap(super(Entry, self).getName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @overload
    def select(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.select(boolean)"""
        super(__Entry, self).select(__boolean.valueOf(arg0))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def select(self):
        """public void dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.select()"""
        super(Entry, self).select()

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @overload
    def position(self, arg0: 'Supplier') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T> dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Entry'.__wrap(super(__Entry, self).position(arg0))

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: object, arg1: 'SelectionList'):
        """public dev.ultreon.quantum.client.gui.widget.SelectionList$Entry(T,dev.ultreon.quantum.client.gui.widget.SelectionList<T>)"""
        val = __Entry(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Entry':
        """public dev.ultreon.quantum.client.gui.widget.SelectionList$Entry<T> dev.ultreon.quantum.client.gui.widget.SelectionList$Entry.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Entry'.__wrap(super(__Entry, self).bounds(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.SelectionList$ItemRenderer
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.gui.widget.SelectionList as __SelectionList_ItemRenderer
__ItemRenderer = __SelectionList_ItemRenderer.ItemRenderer
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class ItemRenderer(ABC):
    """dev.ultreon.quantum.client.gui.widget.SelectionList.ItemRenderer"""
 
    @staticmethod
    def __wrap(java_value: __ItemRenderer) -> 'ItemRenderer':
        return ItemRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ItemRenderer):
        """
        Dynamic initializer for ItemRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def render(self, arg0: 'Renderer', arg1: object, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: float):
        """public abstract void dev.ultreon.quantum.client.gui.widget.SelectionList$ItemRenderer.render(dev.ultreon.quantum.client.gui.Renderer,T,int,int,int,boolean,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.Label
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui.widget import components
except ImportError:
    components = __import_once__("pyquantum.client.gui.widget.components")

import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import dev.ultreon.quantum.client.gui.widget.components.ScaleComponent as __ScaleComponent
__ScaleComponent = __ScaleComponent
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as __TextComponent
__TextComponent = __TextComponent
import dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent as __AlignmentComponent
__AlignmentComponent = __AlignmentComponent
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.Label as __Label
__Label = __Label
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
from builtins import int
 
class Label():
    """dev.ultreon.quantum.client.gui.widget.Label"""
 
    @staticmethod
    def __wrap(java_value: __Label) -> 'Label':
        return Label(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Label):
        """
        Dynamic initializer for Label.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(Widget, self).componentRegistry())

    @overload
    def scale(self) -> 'components.ScaleComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.ScaleComponent dev.ultreon.quantum.client.gui.widget.Label.scale()"""
        return 'components.ScaleComponent'.__wrap(super(Label, self).scale())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(Widget, self).isEnabled())

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__Widget, self).setSize(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def alignment(self, arg0: 'Alignment') -> 'Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.alignment(dev.ultreon.quantum.client.gui.Alignment)"""
        return 'Label'.__wrap(super(__Label, self).alignment(arg0))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Label'.__wrap(super(__Label, self).bounds(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(Widget, self).path())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__Widget, self).onRevalidate(arg0)

    @overload
    def __init__(self, arg0: 'Alignment'):
        """public dev.ultreon.quantum.client.gui.widget.Label(dev.ultreon.quantum.client.gui.Alignment)"""
        val = __Label(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(Widget, self).onFocusGained()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__Widget, self).setPreferredY(__int.valueOf(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Label.getName()"""
        return str.__wrap(super(Label, self).getName())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(Widget, self).onFocusLost()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(Widget, self).getPreferredY())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.Label()"""
        val = __Label()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mousePress(int,int,int)"""
        return bool.__wrap(super(__Widget, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(Widget, self).show()

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.Label()"""
        val = __Label()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(Widget, self).isHovered())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Widget, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: 'Supplier') -> 'Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Label'.__wrap(super(__Label, self).position(arg0))

    @staticmethod
    @overload
    def of(arg0: str) -> 'Label':
        """public static dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.of(java.lang.String)"""
        return Label.__wrap(__Label.of(arg0))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(Widget, self).getX())

    @overload
    def __init__(self, arg0: 'RgbColor'):
        """public dev.ultreon.quantum.client.gui.widget.Label(dev.ultreon.quantum.util.RgbColor)"""
        val = __Label(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def alignment(self) -> 'components.AlignmentComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent dev.ultreon.quantum.client.gui.widget.Label.alignment()"""
        return 'components.AlignmentComponent'.__wrap(super(Label, self).alignment())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(Widget, self).hide()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(Widget, self).isFocused())

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(Widget, self).getPreferredWidth())

    @overload
    def scale(self, arg0: int) -> 'Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.scale(int)"""
        return 'Label'.__wrap(super(__Label, self).scale(__int.valueOf(arg0)))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(Widget, self).revalidate()

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(Widget, self).getPreferredPos())

    @staticmethod
    @overload
    def of(arg0: 'TextObject') -> 'Label':
        """public static dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.of(dev.ultreon.quantum.text.TextObject)"""
        return Label.__wrap(__Label.of(arg0))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Alignment', arg1: 'RgbColor'):
        """public dev.ultreon.quantum.client.gui.widget.Label(dev.ultreon.quantum.client.gui.Alignment,dev.ultreon.quantum.util.RgbColor)"""
        val = __Label(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__Widget, self).x(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(Widget, self).getWidth())

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(Widget, self).getPreferredSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(Widget, self).isVisible())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__Widget, self).setBounds(arg0)

    @staticmethod
    @overload
    def of() -> 'Label':
        """public static dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.of()"""
        return Label.__wrap(__Label.of())

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__Widget, self).setPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__Widget, self).onDisconnect(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(Widget, self).getHeight())

    @overload
    def textColor(self, arg0: 'Color') -> 'Label':
        """public dev.ultreon.quantum.client.gui.widget.Label dev.ultreon.quantum.client.gui.widget.Label.textColor(dev.ultreon.quantum.util.Color)"""
        return 'Label'.__wrap(super(__Label, self).textColor(arg0))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(Widget, self).getY())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(Widget, self).enable()

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(Widget, self).getPreferredHeight())

    @overload
    def text(self) -> 'components.TextComponent':
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent dev.ultreon.quantum.client.gui.widget.Label.text()"""
        return 'components.TextComponent'.__wrap(super(Label, self).text())

    @overload
    def renderBackground(self, arg0: 'Renderer', arg1: float):
        """public void dev.ultreon.quantum.client.gui.widget.Label.renderBackground(dev.ultreon.quantum.client.gui.Renderer,float)"""
        super(__Label, self).renderBackground(arg0, __float.valueOf(arg1))

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(Widget, self).getBounds())

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(Widget, self).isClickable())

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(Widget, self).disable()

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Widget, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))