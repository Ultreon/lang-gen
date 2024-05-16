from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.gui.NotifyManager as __NotifyManager
__NotifyManager = __NotifyManager
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NotifyManager():
    """dev.ultreon.quantum.client.gui.NotifyManager"""
 
    @staticmethod
    def __wrap(java_value: __NotifyManager) -> 'NotifyManager':
        return NotifyManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NotifyManager):
        """
        Dynamic initializer for NotifyManager.
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

    @overload
    def add(self, arg0: str, arg1: str):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(java.lang.String,java.lang.String)"""
        super(__NotifyManager, self).add(arg0, arg1)

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__NotifyManager, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def add(self, arg0: str, arg1: str, arg2: str):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(java.lang.String,java.lang.String,java.lang.String)"""
        super(__NotifyManager, self).add(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'MutableText', arg1: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText)"""
        super(__NotifyManager, self).add(arg0, arg1)

    @overload
    def unavailable(self, arg0: str):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.unavailable(java.lang.String)"""
        super(__NotifyManager, self).unavailable(arg0)

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
    def add(self, arg0: 'MutableText', arg1: 'MutableText', arg2: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText)"""
        super(__NotifyManager, self).add(arg0, arg1, arg2)

    @overload
    def add(self, arg0: 'Notification'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(dev.ultreon.quantum.client.gui.Notification)"""
        super(__NotifyManager, self).add(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addOnce(self, arg0: 'UUID', arg1: 'Notification'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.addOnce(java.util.UUID,dev.ultreon.quantum.client.gui.Notification)"""
        super(__NotifyManager, self).addOnce(arg0, arg1)

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.gui.NotifyManager(dev.ultreon.quantum.client.QuantumClient)"""
        val = __NotifyManager(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.NotifyManager
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.gui.NotifyManager as __NotifyManager
__NotifyManager = __NotifyManager
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NotifyManager():
    """dev.ultreon.quantum.client.gui.NotifyManager"""
 
    @staticmethod
    def __wrap(java_value: __NotifyManager) -> 'NotifyManager':
        return NotifyManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NotifyManager):
        """
        Dynamic initializer for NotifyManager.
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

    @overload
    def add(self, arg0: str, arg1: str):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(java.lang.String,java.lang.String)"""
        super(__NotifyManager, self).add(arg0, arg1)

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__NotifyManager, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def add(self, arg0: str, arg1: str, arg2: str):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(java.lang.String,java.lang.String,java.lang.String)"""
        super(__NotifyManager, self).add(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'MutableText', arg1: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText)"""
        super(__NotifyManager, self).add(arg0, arg1)

    @overload
    def unavailable(self, arg0: str):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.unavailable(java.lang.String)"""
        super(__NotifyManager, self).unavailable(arg0)

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
    def add(self, arg0: 'MutableText', arg1: 'MutableText', arg2: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText)"""
        super(__NotifyManager, self).add(arg0, arg1, arg2)

    @overload
    def add(self, arg0: 'Notification'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(dev.ultreon.quantum.client.gui.Notification)"""
        super(__NotifyManager, self).add(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addOnce(self, arg0: 'UUID', arg1: 'Notification'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.addOnce(java.util.UUID,dev.ultreon.quantum.client.gui.Notification)"""
        super(__NotifyManager, self).addOnce(arg0, arg1)

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.gui.NotifyManager(dev.ultreon.quantum.client.QuantumClient)"""
        val = __NotifyManager(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.NotifyManager 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Screen
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import dev.ultreon.quantum.client.gui.Screen as __Screen
__Screen = __Screen
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.gui.Dialog as __Dialog
__Dialog = __Dialog
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
 
class Screen(ABC):
    """dev.ultreon.quantum.client.gui.Screen"""
 
    @staticmethod
    def __wrap(java_value: __Screen) -> 'Screen':
        return Screen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Screen):
        """
        Dynamic initializer for Screen.
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
    ROOT: 'widget.UIContainer' = __wrap(__widget.UIContainer.ROOT)


    @property
    def directHovered(self) -> Widget:
        return Widget.__wrap(super(__Screen).directHovered())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(widget.Widget, self).isClickable())

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'.__wrap(super(__Screen, self).add(arg0))

    @property
    def parentScreen(self, value: 'Screen'):
        super(__Screen).parentScreen(value)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Screen, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

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
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(__Screen, self).closeDialog(arg0)

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__widget.Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__widget.Widget, self).setBounds(arg0)

    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str.__wrap(super(Screen, self).getRawTitle())

    @overload
    def title(self, arg0: 'TextObject') -> 'Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'Screen'.__wrap(super(__Screen, self).title(arg0))

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__widget.Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__widget.Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(widget.UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(widget.Widget, self).getPreferredHeight())

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__widget.Widget, self).setEnabled(__boolean.valueOf(arg0))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Screen, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getBounds(self) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'Bounds'.__wrap(super(widget.Widget, self).getBounds())

    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(Screen, self).onClosed()

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
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str.__wrap(super(Screen, self).getName())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(Screen, self).revalidate()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(widget.Widget, self).getPreferredX())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Screen, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool.__wrap(super(__Screen, self).keyRelease(__int.valueOf(arg0)))

    @overload
    def title(self, arg0: str) -> 'Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'Screen'.__wrap(super(__Screen, self).title(arg0))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool.__wrap(super(__Screen, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @property
    def focused(self, value: 'widget.Widget'):
        super(__Screen).focused(value)

    @override
    @overload
    def getPreferredPos(self) -> 'Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'Position'.__wrap(super(widget.Widget, self).getPreferredPos())

    @abstractmethod
    def build(self, arg0: 'GuiBuilder'):
        """public abstract void dev.ultreon.quantum.client.gui.Screen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        pass

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__Screen, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(widget.Widget, self).componentRegistry())

    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(__Screen, self).init(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(widget.Widget, self).getX())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__widget.Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canCloseWithEsc()"""
        return bool.__wrap(super(Screen, self).canCloseWithEsc())

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__widget.Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool.__wrap(super(__Screen, self).filesDropped(arg0))

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__widget.Widget, self).y(__int.valueOf(arg0))

    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(__Screen, self).showDialog(arg0)

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__Screen, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).remove(arg0)

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__widget.Widget, self).height(__int.valueOf(arg0))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool.__wrap(super(__Screen, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getDialog(self) -> 'Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'Dialog'.__wrap(super(Screen, self).getDialog())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(widget.Widget, self).isEnabled())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__widget.Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(widget.Widget, self).isFocused())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__widget.Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__widget.UIContainer, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__widget.Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'.__wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__widget.Widget, self).setPos(arg0)

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__widget.UIContainer, self).setLayout(arg0)

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__widget.Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool.__wrap(super(__Screen, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool.__wrap(super(__Screen, self).onClose(arg0))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Screen, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__widget.Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).position(arg0))

    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canClose()"""
        return bool.__wrap(super(Screen, self).canClose())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).bounds(arg0))

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(__Screen, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(widget.Widget, self).isHovered())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__widget.Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__widget.Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(__Screen).directHovered(value)

    @overload
    def titleTranslation(self, arg0: str) -> 'Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'Screen'.__wrap(super(__Screen, self).titleTranslation(arg0))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(widget.Widget, self).isVisible())

    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool.__wrap(super(Screen, self).back())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'.__wrap(super(Screen, self).path())

    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool.__wrap(super(Screen, self).isHoveringClickable())

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__widget.Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__widget.Widget, self).onRevalidate(arg0)

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(__Screen, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__widget.UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @property
    def focused(self) -> Widget:
        return Widget.__wrap(super(__Screen).focused())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(widget.Widget, self).getWidth())

    @property
    def parentScreen(self) -> Screen:
        return Screen.__wrap(super(__Screen).parentScreen())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'.__wrap(super(Screen, self).getTitle())

    @override
    @overload
    def getPreferredSize(self) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'Size'.__wrap(super(widget.Widget, self).getPreferredSize())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__widget.Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__widget.Widget, self).setSize(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Hud
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.gui.Hud as __Hud
__Hud = __Hud
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Hud():
    """dev.ultreon.quantum.client.gui.Hud"""
 
    @staticmethod
    def __wrap(java_value: __Hud) -> 'Hud':
        return Hud(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Hud):
        """
        Dynamic initializer for Hud.
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
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Hud.touchUp(int,int,int,int)"""
        return bool.__wrap(super(__Hud, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.gui.Hud(dev.ultreon.quantum.client.QuantumClient)"""
        val = __Hud(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Hud.touchDown(int,int,int,int)"""
        return bool.__wrap(super(__Hud, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

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
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Hud.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Hud, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isMouseOver(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Hud.isMouseOver(int,int)"""
        return bool.__wrap(super(__Hud, self).isMouseOver(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.GuiBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

import dev.ultreon.quantum.client.gui.Screen as __Screen
__Screen = __Screen
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
import dev.ultreon.quantum.client.gui.GuiBuilder as __GuiBuilder
__GuiBuilder = __GuiBuilder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GuiBuilder():
    """dev.ultreon.quantum.client.gui.GuiBuilder"""
 
    @staticmethod
    def __wrap(java_value: __GuiBuilder) -> 'GuiBuilder':
        return GuiBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GuiBuilder):
        """
        Dynamic initializer for GuiBuilder.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.GuiBuilder.hashCode()"""
        return int.__wrap(super(GuiBuilder, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.GuiBuilder.equals(java.lang.Object)"""
        return bool.__wrap(super(__GuiBuilder, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.GuiBuilder.toString()"""
        return str.__wrap(super(GuiBuilder, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <T extends dev.ultreon.quantum.client.gui.widget.Widget> T dev.ultreon.quantum.client.gui.GuiBuilder.add(T)"""
        return 'widget.Widget'.__wrap(super(__GuiBuilder, self).add(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def screen(self) -> 'Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.GuiBuilder.screen()"""
        return 'Screen'.__wrap(super(GuiBuilder, self).screen())

    @overload
    def __init__(self, arg0: 'Screen'):
        """public dev.ultreon.quantum.client.gui.GuiBuilder(dev.ultreon.quantum.client.gui.Screen)"""
        val = __GuiBuilder(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.gui.GuiStateListener
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.gui.GuiStateListener as __GuiStateListener
__GuiStateListener = __GuiStateListener
 
class GuiStateListener(ABC):
    """dev.ultreon.quantum.client.gui.GuiStateListener"""
 
    @staticmethod
    def __wrap(java_value: __GuiStateListener) -> 'GuiStateListener':
        return GuiStateListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GuiStateListener):
        """
        Dynamic initializer for GuiStateListener.
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
    def destroy(self, ):
        """public abstract void dev.ultreon.quantum.client.gui.GuiStateListener.destroy()"""
        pass

    @abstractmethod
    def isValid(self, ):
        """public abstract boolean dev.ultreon.quantum.client.gui.GuiStateListener.isValid()"""
        pass

    @abstractmethod
    def make(self, ):
        """public abstract void dev.ultreon.quantum.client.gui.GuiStateListener.make()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Size
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Size():
    """dev.ultreon.quantum.client.gui.Size"""
 
    @staticmethod
    def __wrap(java_value: __Size) -> 'Size':
        return Size(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Size):
        """
        Dynamic initializer for Size.
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
    def set(self, arg0: int) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.Size.set(int)"""
        return 'Size'.__wrap(super(__Size, self).set(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Size.equals(java.lang.Object)"""
        return bool.__wrap(super(__Size, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.Size()"""
        val = __Size()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.Size(int)"""
        val = __Size(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Size') -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.Size.set(dev.ultreon.quantum.client.gui.Size)"""
        return 'Size'.__wrap(super(__Size, self).set(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.Size()"""
        val = __Size()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Size.toString()"""
        return str.__wrap(super(Size, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Size.hashCode()"""
        return int.__wrap(super(Size, self).hashCode())

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

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.Size(int,int)"""
        val = __Size(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def idt(self):
        """public void dev.ultreon.quantum.client.gui.Size.idt()"""
        super(Size, self).idt()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: int, arg1: int) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.Size.set(int,int)"""
        return 'Size'.__wrap(super(__Size, self).set(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def cpy(self) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.Size.cpy()"""
        return 'Size'.__wrap(super(Size, self).cpy())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.client.gui.GlStateStack
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.client.gui.GlStateStack as __GlStateStack
__GlStateStack = __GlStateStack
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GlStateStack():
    """dev.ultreon.quantum.client.gui.GlStateStack"""
 
    @staticmethod
    def __wrap(java_value: __GlStateStack) -> 'GlStateStack':
        return GlStateStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GlStateStack):
        """
        Dynamic initializer for GlStateStack.
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

    @overload
    def end(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.end()"""
        super(GlStateStack, self).end()

    @overload
    def disableDepthTest(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.disableDepthTest()"""
        super(GlStateStack, self).disableDepthTest()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.GlStateStack()"""
        val = __GlStateStack()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def enableBlending(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.enableBlending()"""
        super(GlStateStack, self).enableBlending()

    @overload
    def blendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.blendFuncSeparate(int,int,int,int)"""
        super(__GlStateStack, self).blendFuncSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.GlStateStack()"""
        val = __GlStateStack()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def blendFunc(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.blendFunc(int,int)"""
        super(__GlStateStack, self).blendFunc(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def enableDepthTest(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.enableDepthTest()"""
        super(GlStateStack, self).enableDepthTest()

    @overload
    def push(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.push()"""
        super(GlStateStack, self).push()

    @overload
    def blendEquationSeparate(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.blendEquationSeparate(int,int)"""
        super(__GlStateStack, self).blendEquationSeparate(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def disableBlending(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.disableBlending()"""
        super(GlStateStack, self).disableBlending()

    @overload
    def begin(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.begin()"""
        super(GlStateStack, self).begin()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Sprite$Meta
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import dev.ultreon.quantum.client.gui.Sprite as __Sprite_Meta
__Meta = __Sprite_Meta.Meta
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Meta():
    """dev.ultreon.quantum.client.gui.Sprite.Meta"""
 
    @staticmethod
    def __wrap(java_value: __Meta) -> 'Meta':
        return Meta(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Meta):
        """
        Dynamic initializer for Meta.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool):
        """public dev.ultreon.quantum.client.gui.Sprite$Meta(int,int,int,int,boolean)"""
        val = __Meta(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.Sprite$Meta(int,int,int,int)"""
        val = __Meta(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Matrices
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.math.Quaternion as __Quaternion
__Quaternion = __Quaternion
import dev.ultreon.quantum.client.gui.Matrices as __Matrices
__Matrices = __Matrices
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Matrices():
    """dev.ultreon.quantum.client.gui.Matrices"""
 
    @staticmethod
    def __wrap(java_value: __Matrices) -> 'Matrices':
        return Matrices(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Matrices):
        """
        Dynamic initializer for Matrices.
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
    def scale(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.client.gui.Matrices.scale(float,float)"""
        super(__Matrices, self).scale(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def pop(self):
        """public void dev.ultreon.quantum.client.gui.Matrices.pop()"""
        super(Matrices, self).pop()

    @overload
    def getRotation(self, arg0: 'Quaternion') -> 'math.Quaternion':
        """public com.badlogic.gdx.math.Quaternion dev.ultreon.quantum.client.gui.Matrices.getRotation(com.badlogic.gdx.math.Quaternion)"""
        return 'math.Quaternion'.__wrap(super(__Matrices, self).getRotation(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def reset(self):
        """public void dev.ultreon.quantum.client.gui.Matrices.reset()"""
        super(Matrices, self).reset()

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.client.gui.Matrices.translate(double,double)"""
        super(__Matrices, self).translate(__double.valueOf(arg0), __double.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def push(self):
        """public void dev.ultreon.quantum.client.gui.Matrices.push()"""
        super(Matrices, self).push()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def isClear(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Matrices.isClear()"""
        return bool.__wrap(super(Matrices, self).isClear())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Matrices.toString()"""
        return str.__wrap(super(Matrices, self).toString())

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.client.gui.Matrices.translate(float,float)"""
        super(__Matrices, self).translate(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.Matrices()"""
        val = __Matrices()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Matrix4'):
        """public dev.ultreon.quantum.client.gui.Matrices(com.badlogic.gdx.math.Matrix4)"""
        val = __Matrices(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.gui.Matrices.translate(float,float,float)"""
        super(__Matrices, self).translate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def getScale(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.gui.Matrices.getScale(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Matrices, self).getScale(arg0))

    @overload
    def last(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.gui.Matrices.last()"""
        return 'math.Matrix4'.__wrap(super(Matrices, self).last())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void dev.ultreon.quantum.client.gui.Matrices.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(__Matrices, self).rotate(arg0)

    @overload
    def getTranslation(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.gui.Matrices.getTranslation(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Matrices, self).getTranslation(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTranslation(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.gui.Matrices.getTranslation(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Matrices, self).getTranslation(arg0))

    @overload
    def getScale(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.gui.Matrices.getScale(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Matrices, self).getScale(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.Matrices()"""
        val = __Matrices()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Dialog
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

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
import dev.ultreon.quantum.client.gui.Dialog as __Dialog
__Dialog = __Dialog
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

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
 
class Dialog():
    """dev.ultreon.quantum.client.gui.Dialog"""
 
    @staticmethod
    def __wrap(java_value: __Dialog) -> 'Dialog':
        return Dialog(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Dialog):
        """
        Dynamic initializer for Dialog.
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
    ROOT: 'widget.UIContainer' = __wrap(__widget.UIContainer.ROOT)


    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(widget.Widget, self).isEnabled())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Dialog.keyPress(int)"""
        return bool.__wrap(super(__Dialog, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(widget.Widget, self).isClickable())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__widget.Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(widget.Widget, self).isFocused())

    @overload
    def position(self, arg0: 'Supplier') -> 'Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Dialog.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Dialog'.__wrap(super(__Dialog, self).position(arg0))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__widget.UIContainer, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__widget.Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Dialog.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Dialog, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__widget.UIContainer, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__widget.Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__widget.Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__widget.Widget, self).setBounds(arg0)

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'.__wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__widget.Widget, self).setPos(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__widget.Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__widget.UIContainer, self).setLayout(arg0)

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__widget.Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__widget.Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(widget.UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(widget.Widget, self).getPreferredHeight())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Dialog.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__Dialog, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__widget.Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Dialog.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Dialog'.__wrap(super(__Dialog, self).bounds(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__widget.Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Dialog.mousePress(int,int,int)"""
        return bool.__wrap(super(__Dialog, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getBounds(self) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'Bounds'.__wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Dialog.revalidate()"""
        super(Dialog, self).revalidate()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.UIContainer.getName()"""
        return str.__wrap(super(widget.UIContainer, self).getName())

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__widget.UIContainer, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool.__wrap(super(__widget.UIContainer, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Dialog.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__Dialog, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

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
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(widget.Widget, self).isHovered())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__widget.Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__widget.Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.keyRelease(int)"""
        return bool.__wrap(super(__widget.UIContainer, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(widget.Widget, self).path())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(widget.Widget, self).isVisible())

    @overload
    def close(self):
        """public void dev.ultreon.quantum.client.gui.Dialog.close()"""
        super(Dialog, self).close()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.mouseMove(int,int)"""
        super(__widget.UIContainer, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getPreferredPos(self) -> 'Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'Position'.__wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__widget.Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__widget.Widget, self).onRevalidate(arg0)

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__widget.UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.widget.UIContainer.add(C)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).add(arg0))

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(widget.Widget, self).getWidth())

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__widget.UIContainer, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(widget.Widget, self).componentRegistry())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(widget.Widget, self).getX())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__widget.Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__widget.Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def getPreferredSize(self) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'Size'.__wrap(super(widget.Widget, self).getPreferredSize())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__widget.Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).remove(arg0)

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__widget.Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__widget.Widget, self).setSize(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Overlays
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.gui.Overlays as __Overlays
__Overlays = __Overlays
try:
    from pyquantum.client.gui import overlay
except ImportError:
    overlay = __import_once__("pyquantum.client.gui.overlay")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Overlays():
    """dev.ultreon.quantum.client.gui.Overlays"""
 
    @staticmethod
    def __wrap(java_value: __Overlays) -> 'Overlays':
        return Overlays(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Overlays):
        """
        Dynamic initializer for Overlays.
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
 
    # public static final dev.ultreon.quantum.client.gui.overlay.ChatOverlay dev.ultreon.quantum.client.gui.Overlays.CHAT
    CHAT: 'overlay.ChatOverlay' = __wrap(__overlay.ChatOverlay.CHAT)

    # public static final dev.ultreon.quantum.client.gui.overlay.HealthOverlay dev.ultreon.quantum.client.gui.Overlays.HEALTH
    HEALTH: 'overlay.HealthOverlay' = __wrap(__overlay.HealthOverlay.HEALTH)

    # public static final dev.ultreon.quantum.client.gui.overlay.MemoryUsageOverlay dev.ultreon.quantum.client.gui.Overlays.MEMORY
    MEMORY: 'overlay.MemoryUsageOverlay' = __wrap(__overlay.MemoryUsageOverlay.MEMORY)

    # public static final dev.ultreon.quantum.client.gui.overlay.CrosshairOverlay dev.ultreon.quantum.client.gui.Overlays.CROSSHAIR
    CROSSHAIR: 'overlay.CrosshairOverlay' = __wrap(__overlay.CrosshairOverlay.CROSSHAIR)

    # public static final dev.ultreon.quantum.client.gui.overlay.HotbarOverlay dev.ultreon.quantum.client.gui.Overlays.HOTBAR
    HOTBAR: 'overlay.HotbarOverlay' = __wrap(__overlay.HotbarOverlay.HOTBAR)

    # public static final dev.ultreon.quantum.client.gui.overlay.HungerOverlay dev.ultreon.quantum.client.gui.Overlays.HUNGER
    HUNGER: 'overlay.HungerOverlay' = __wrap(__overlay.HungerOverlay.HUNGER)


    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.Overlays()"""
        val = __Overlays()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.Overlays()"""
        val = __Overlays()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.client.gui.Overlays.init()"""
            __Overlays.init()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Notification
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.gui.icon.Icon as __Icon
__Icon = __Icon
import dev.ultreon.quantum.text.MutableText as __MutableText
__MutableText = __MutableText
from builtins import str
import dev.ultreon.quantum.client.gui.Notification as __Notification
__Notification = __Notification
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pyquantum.client.gui import icon
except ImportError:
    icon = __import_once__("pyquantum.client.gui.icon")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.client.gui.Notification as __Notification_Builder
__Builder = __Notification_Builder.Builder
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Notification():
    """dev.ultreon.quantum.client.gui.Notification"""
 
    @staticmethod
    def __wrap(java_value: __Notification) -> 'Notification':
        return Notification(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Notification):
        """
        Dynamic initializer for Notification.
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
    def getMotion(self) -> float:
        """public float dev.ultreon.quantum.client.gui.Notification.getMotion()"""
        return float.__wrap(super(Notification, self).getMotion())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getIcon(self) -> 'icon.Icon':
        """public dev.ultreon.quantum.client.gui.icon.Icon dev.ultreon.quantum.client.gui.Notification.getIcon()"""
        return 'icon.Icon'.__wrap(super(Notification, self).getIcon())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getTitle(self) -> 'text.MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.client.gui.Notification.getTitle()"""
        return 'text.MutableText'.__wrap(super(Notification, self).getTitle())

    @overload
    def close(self):
        """public void dev.ultreon.quantum.client.gui.Notification.close()"""
        super(Notification, self).close()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setSummary(self, arg0: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.Notification.setSummary(dev.ultreon.quantum.text.MutableText)"""
        super(__Notification, self).setSummary(arg0)

    @staticmethod
    @overload
    def builder(arg0: str, arg1: str) -> 'Builder':
        """public static dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification.builder(java.lang.String,java.lang.String)"""
        return Builder.__wrap(__Notification.builder(arg0, arg1))

    @overload
    def isSticky(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Notification.isSticky()"""
        return bool.__wrap(super(Notification, self).isSticky())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isFinished(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Notification.isFinished()"""
        return bool.__wrap(super(Notification, self).isFinished())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def builder(arg0: 'MutableText', arg1: 'MutableText') -> 'Builder':
        """public static dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification.builder(dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText)"""
        return Builder.__wrap(__Notification.builder(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setIcon(self, arg0: 'Icon'):
        """public void dev.ultreon.quantum.client.gui.Notification.setIcon(dev.ultreon.quantum.client.gui.icon.Icon)"""
        super(__Notification, self).setIcon(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setTitle(self, arg0: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.Notification.setTitle(dev.ultreon.quantum.text.MutableText)"""
        super(__Notification, self).setTitle(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getSummary(self) -> 'text.MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.client.gui.Notification.getSummary()"""
        return 'text.MutableText'.__wrap(super(Notification, self).getSummary())

    @overload
    def getSubText(self) -> 'text.MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.client.gui.Notification.getSubText()"""
        return 'text.MutableText'.__wrap(super(Notification, self).getSubText())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def set(self, arg0: 'MutableText', arg1: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.Notification.set(dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText)"""
        super(__Notification, self).set(arg0, arg1) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Bounds
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
from builtins import bool
from builtins import int
 
class Bounds():
    """dev.ultreon.quantum.client.gui.Bounds"""
 
    @staticmethod
    def __wrap(java_value: __Bounds) -> 'Bounds':
        return Bounds(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Bounds):
        """
        Dynamic initializer for Bounds.
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

    @overload
    def grow(self, arg0: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.grow(int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).grow(__int.valueOf(arg0)))

    @overload
    def shrink(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.shrink(int,int,int,int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).shrink(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Bounds.getY()"""
        return int.__wrap(super(Bounds, self).getY())

    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Bounds.getWidth()"""
        return int.__wrap(super(Bounds, self).getWidth())

    @overload
    def setBounds(self, arg0: int, arg1: int, arg2: 'Size') -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setBounds(int,int,dev.ultreon.quantum.client.gui.Size)"""
        return 'Bounds'.__wrap(super(__Bounds, self).setBounds(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @overload
    def grow(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.grow(int,int,int,int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).grow(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def setBounds(self, arg0: 'Bounds') -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        return 'Bounds'.__wrap(super(__Bounds, self).setBounds(arg0))

    @overload
    def setBounds(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setBounds(int,int,int,int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).setBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def setBounds(self, arg0: 'Position', arg1: int, arg2: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setBounds(dev.ultreon.quantum.client.gui.Position,int,int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).setBounds(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.Bounds()"""
        val = __Bounds()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setWidth(self, arg0: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setWidth(int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).setWidth(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.Bounds(int,int,int,int)"""
        val = __Bounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setSize(self, arg0: 'Size') -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setSize(dev.ultreon.quantum.client.gui.Size)"""
        return 'Bounds'.__wrap(super(__Bounds, self).setSize(arg0))

    @override
    @overload
    def cpy(self) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.cpy()"""
        return 'Bounds'.__wrap(super(Bounds, self).cpy())

    @overload
    def setX(self, arg0: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setX(int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).setX(__int.valueOf(arg0)))

    @overload
    def setPos(self, arg0: int, arg1: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setPos(int,int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def shrink(self, arg0: int, arg1: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.shrink(int,int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).shrink(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Bounds.toString()"""
        return str.__wrap(super(Bounds, self).toString())

    @overload
    def setPos(self, arg0: 'Position') -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setPos(dev.ultreon.quantum.client.gui.Position)"""
        return 'Bounds'.__wrap(super(__Bounds, self).setPos(arg0))

    @overload
    def size(self) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.Bounds.size()"""
        return 'Size'.__wrap(super(Bounds, self).size())

    @overload
    def shrink(self, arg0: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.shrink(int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).shrink(__int.valueOf(arg0)))

    @overload
    def setSize(self, arg0: int, arg1: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setSize(int,int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def setBounds(self, arg0: 'Position', arg1: 'Size') -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setBounds(dev.ultreon.quantum.client.gui.Position,dev.ultreon.quantum.client.gui.Size)"""
        return 'Bounds'.__wrap(super(__Bounds, self).setBounds(arg0, arg1))

    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Bounds.getHeight()"""
        return int.__wrap(super(Bounds, self).getHeight())

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Bounds.getX()"""
        return int.__wrap(super(Bounds, self).getX())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.Bounds()"""
        val = __Bounds()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Bounds.equals(java.lang.Object)"""
        return bool.__wrap(super(__Bounds, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Bounds.hashCode()"""
        return int.__wrap(super(Bounds, self).hashCode())

    @overload
    def setY(self, arg0: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setY(int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).setY(__int.valueOf(arg0)))

    @overload
    def setHeight(self, arg0: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setHeight(int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).setHeight(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def grow(self, arg0: int, arg1: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.grow(int,int)"""
        return 'Bounds'.__wrap(super(__Bounds, self).grow(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def pos(self) -> 'Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.Bounds.pos()"""
        return 'Position'.__wrap(super(Bounds, self).pos())

    @overload
    def __init__(self, arg0: 'Position', arg1: 'Size'):
        """public dev.ultreon.quantum.client.gui.Bounds(dev.ultreon.quantum.client.gui.Position,dev.ultreon.quantum.client.gui.Size)"""
        val = __Bounds(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def contains(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Bounds.contains(int,int)"""
        return bool.__wrap(super(__Bounds, self).contains(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Fonts
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.gui.Fonts as __Fonts
__Fonts = __Fonts
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = __import_once__("pyquantum.registry")

import dev.ultreon.quantum.registry.RegistryKey as __RegistryKey
__RegistryKey = __RegistryKey
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Fonts():
    """dev.ultreon.quantum.client.gui.Fonts"""
 
    @staticmethod
    def __wrap(java_value: __Fonts) -> 'Fonts':
        return Fonts(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Fonts):
        """
        Dynamic initializer for Fonts.
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

    @staticmethod
    @property
    def QUANTIUM_() -> RegistryKey:
        """
        Getter for the QUANTIUM property.
     
        :return: Value of QUANTIUM
        """
     
        return super(RegistryKey).QUANTIUM()

        @staticmethod
        @overload
        def register():
            """public static void dev.ultreon.quantum.client.gui.Fonts.register()"""
            __Fonts.register()

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.Fonts()"""
        val = __Fonts()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @property
    def QUANTIUM_(value: 'registry.RegistryKey'):
        """
        Setter for the QUANTIUM property.
     
        :param value: Value to set for the QUANTIUM property.
        """
     
        super('registry.RegistryKey').QUANTIUM(value)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.Fonts()"""
        val = __Fonts()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.LayoutBounds
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.gui.LayoutBounds as __LayoutBounds
__LayoutBounds = __LayoutBounds
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.function.IntSupplier as IntSupplier
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
from builtins import int
 
class LayoutBounds():
    """dev.ultreon.quantum.client.gui.LayoutBounds"""
 
    @staticmethod
    def __wrap(java_value: __LayoutBounds) -> 'LayoutBounds':
        return LayoutBounds(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LayoutBounds):
        """
        Dynamic initializer for LayoutBounds.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.LayoutBounds.hashCode()"""
        return int.__wrap(super(LayoutBounds, self).hashCode())

    @overload
    def setCurrentBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.setCurrentBounds(int,int,int,int)"""
        super(__LayoutBounds, self).setCurrentBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def currentY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.LayoutBounds.currentY()"""
        return int.__wrap(super(LayoutBounds, self).currentY())

    @overload
    def currentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.LayoutBounds.currentHeight()"""
        return int.__wrap(super(LayoutBounds, self).currentHeight())

    @overload
    def setCurrentHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.setCurrentHeight(int)"""
        super(__LayoutBounds, self).setCurrentHeight(__int.valueOf(arg0))

    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.revalidate()"""
        super(LayoutBounds, self).revalidate()

    @overload
    def __init__(self, arg0: 'IntSupplier', arg1: 'IntSupplier', arg2: 'IntSupplier', arg3: 'IntSupplier'):
        """public dev.ultreon.quantum.client.gui.LayoutBounds(java.util.function.IntSupplier,java.util.function.IntSupplier,java.util.function.IntSupplier,java.util.function.IntSupplier)"""
        val = __LayoutBounds(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setCurrentX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.setCurrentX(int)"""
        super(__LayoutBounds, self).setCurrentX(__int.valueOf(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.LayoutBounds.equals(java.lang.Object)"""
        return bool.__wrap(super(__LayoutBounds, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def currentWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.LayoutBounds.currentWidth()"""
        return int.__wrap(super(LayoutBounds, self).currentWidth())

    @overload
    def setCurrentWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.setCurrentWidth(int)"""
        super(__LayoutBounds, self).setCurrentWidth(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def currentX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.LayoutBounds.currentX()"""
        return int.__wrap(super(LayoutBounds, self).currentX())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.LayoutBounds.toString()"""
        return str.__wrap(super(LayoutBounds, self).toString())

    @overload
    def currentBounds(self) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.LayoutBounds.currentBounds()"""
        return 'Bounds'.__wrap(super(LayoutBounds, self).currentBounds())

    @overload
    def setCurrentY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.setCurrentY(int)"""
        super(__LayoutBounds, self).setCurrentY(__int.valueOf(arg0))

    @overload
    def setCurrentBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.setCurrentBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__LayoutBounds, self).setCurrentBounds(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Renderer
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
import dev.ultreon.quantum.client.font.Font as __Font
__Font = __Font
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import java.awt.geom.Rectangle2D as Rectangle2D
import dev.ultreon.quantum.client.gui.Matrices as __Matrices
__Matrices = __Matrices
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.awt.geom.Line2D as Line2D
import com.badlogic.gdx.graphics.g3d.Renderable as __Renderable
__Renderable = __Renderable
import java.util.function.Consumer as Consumer
try:
    import pyshapedrawer
except ImportError:
    pyshapedrawer = __import_once__("pyshapedrawer")

import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import com.badlogic.gdx.graphics.g2d.Batch as __Batch
__Batch = __Batch
import java.lang.Double as __double
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import java.lang.Runnable as Runnable
from builtins import float
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.awt.geom.Ellipse2D as Ellipse2D
import dev.ultreon.quantum.util.Color as __Color
__Color = __Color
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.gui.Renderer as __Renderer
__Renderer = __Renderer
try:
    from pyquantum.client import font
except ImportError:
    font = __import_once__("pyquantum.client.font")

try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import java.util.List as List
from builtins import int
 
class Renderer():
    """dev.ultreon.quantum.client.gui.Renderer"""
 
    @staticmethod
    def __wrap(java_value: __Renderer) -> 'Renderer':
        return Renderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Renderer):
        """
        Dynamic initializer for Renderer.
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
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: bool, arg4: float, arg5: bool, arg6: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,boolean,float,boolean,java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3), __float.valueOf(arg4), __boolean.valueOf(arg5), arg6))

    @overload
    def drawSprite(self, arg0: 'Sprite', arg1: int, arg2: int, arg3: int, arg4: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.drawSprite(dev.ultreon.quantum.client.gui.Sprite,int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).drawSprite(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def rectLine(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rectLine(float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).rectLine(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def renderFrame(self, arg0: 'Identifier', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'Color'):
        """public void dev.ultreon.quantum.client.gui.Renderer.renderFrame(dev.ultreon.quantum.util.Identifier,int,int,int,int,int,int,int,int,int,int,dev.ultreon.quantum.util.Color)"""
        super(__Renderer, self).renderFrame(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), arg11)

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4)))

    @overload
    def blit(self, arg0: 'TextureRegion', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4))

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.circle(float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).circle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def textLeft(self, arg0: 'List', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def ovalLine(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.ovalLine(float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).ovalLine(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def popScissors(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle dev.ultreon.quantum.client.gui.Renderer.popScissors()"""
        return 'math.Rectangle'.__wrap(super(Renderer, self).popScissors())

    @overload
    def textTabbed(self, arg0: str, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textTabbed(java.lang.String,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textTabbed(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def setStrokeWidth(self, arg0: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setStrokeWidth(float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).setStrokeWidth(__float.valueOf(arg0)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def rotate(self, arg0: float, arg1: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rotate(double,double)"""
        return 'Renderer'.__wrap(super(__Renderer, self).rotate(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: int, arg3: int, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: 'List', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def setShader(self, arg0: 'ShaderProgram') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        return 'Renderer'.__wrap(super(__Renderer, self).setShader(arg0))

    @overload
    def outline(self, arg0: 'Rectangle2D') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.outline(java.awt.geom.Rectangle2D)"""
        return 'Renderer'.__wrap(super(__Renderer, self).outline(arg0))

    @overload
    def renderPopoutFrame(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.renderPopoutFrame(int,int,int,int)"""
        super(__Renderer, self).renderPopoutFrame(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def draw9PatchTexture(self, arg0: 'Identifier', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.draw9PatchTexture(dev.ultreon.quantum.util.Identifier,int,int,int,int,int,int,int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).draw9PatchTexture(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def translate(self, arg0: int, arg1: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.translate(int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).translate(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def textCenter(self, arg0: 'List', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'List', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'ColorCode', arg4: bool, arg5: float, arg6: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.text.ColorCode,boolean,float,java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4), __float.valueOf(arg5), arg6))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), arg7))

    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch dev.ultreon.quantum.client.gui.Renderer.getBatch()"""
        return 'g2d.Batch'.__wrap(super(Renderer, self).getBatch())

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textRight(self, arg0: 'List', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.line(float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4))

    @overload
    def rect(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rect(float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).rect(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def getGlobalTranslation(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.gui.Renderer.getGlobalTranslation()"""
        return 'math.Vector3'.__wrap(super(Renderer, self).getGlobalTranslation())

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def blitColor(self, arg0: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blitColor(dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blitColor(arg0))

    @overload
    def oval(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.oval(float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).oval(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: bool, arg5: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,float,boolean,java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4), arg5))

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'ColorCode') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.text.ColorCode)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def getColor(self) -> 'util.Color':
        """public dev.ultreon.quantum.util.Color dev.ultreon.quantum.client.gui.Renderer.getColor()"""
        return 'util.Color'.__wrap(super(Renderer, self).getColor())

    @overload
    def rectLine(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rectLine(int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).rectLine(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def clearColor(self, arg0: float, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).clearColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def blurred(self, arg0: bool, arg1: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(boolean,java.lang.Runnable)"""
        super(__Renderer, self).blurred(__boolean.valueOf(arg0), arg1)

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def textMultiline(self, arg0: str, arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textMultiline(java.lang.String,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textMultiline(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def translate(self, arg0: int, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.translate(int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).translate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def textMultiline(self, arg0: str, arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textMultiline(java.lang.String,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textMultiline(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def renderFrame(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.renderFrame(int,int,int,int)"""
        super(__Renderer, self).renderFrame(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def pushMatrix(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.pushMatrix()"""
        return 'Renderer'.__wrap(super(Renderer, self).pushMatrix())

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def getTransform(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.gui.Renderer.getTransform()"""
        return 'math.Matrix4'.__wrap(super(Renderer, self).getTransform())

    @overload
    def textRight(self, arg0: 'List', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def roundRect(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.roundRect(int,int,int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).roundRect(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: int, arg3: int, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: bool, arg4: float, arg5: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,boolean,float,java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3), __float.valueOf(arg4), arg5))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def pushScissors(self, arg0: 'Rectangle') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Renderer.pushScissors(com.badlogic.gdx.math.Rectangle)"""
        return bool.__wrap(super(__Renderer, self).pushScissors(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4)))

    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Renderer.getWidth()"""
        return int.__wrap(super(Renderer, self).getWidth())

    @overload
    def textCenter(self, arg0: str, arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def finish(self):
        """public void dev.ultreon.quantum.client.gui.Renderer.finish()"""
        super(Renderer, self).finish()

    @overload
    def clearColor(self, arg0: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).clearColor(arg0))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'ColorCode', arg4: float, arg5: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.text.ColorCode,float,java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __float.valueOf(arg4), arg5))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4))

    @overload
    def begin(self):
        """public void dev.ultreon.quantum.client.gui.Renderer.begin()"""
        super(Renderer, self).begin()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.gui.Renderer.dispose()"""
        super(Renderer, self).dispose()

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), arg9))

    @overload
    def external(self, arg0: 'Runnable') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.external(java.lang.Runnable)"""
        return 'Renderer'.__wrap(super(__Renderer, self).external(arg0))

    @overload
    def textMultiline(self, arg0: str, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textMultiline(java.lang.String,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textMultiline(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def end(self):
        """public void dev.ultreon.quantum.client.gui.Renderer.end()"""
        super(Renderer, self).end()

    @overload
    def drawRegion(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'Consumer') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.drawRegion(int,int,int,int,java.util.function.Consumer<dev.ultreon.quantum.client.gui.Renderer>)"""
        return 'Renderer'.__wrap(super(__Renderer, self).drawRegion(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @overload
    def textRight(self, arg0: str, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'ColorCode', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.text.ColorCode,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def roundRectLine(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.roundRectLine(int,int,int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).roundRectLine(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,float,float,float,float,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10)))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def textTabbed(self, arg0: str, arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textTabbed(java.lang.String,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textTabbed(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def isBlurred(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Renderer.isBlurred()"""
        return bool.__wrap(super(Renderer, self).isBlurred())

    @overload
    def getStrokeWidth(self) -> float:
        """public float dev.ultreon.quantum.client.gui.Renderer.getStrokeWidth()"""
        return float.__wrap(super(Renderer, self).getStrokeWidth())

    @overload
    def font(self, arg0: 'Font') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.font(dev.ultreon.quantum.client.font.Font)"""
        return 'Renderer'.__wrap(super(__Renderer, self).font(arg0))

    @overload
    def blurred(self, arg0: float, arg1: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(float,java.lang.Runnable)"""
        super(__Renderer, self).blurred(__float.valueOf(arg0), arg1)

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def blit(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'List', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def clearColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).clearColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5)))

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: bool, arg5: float, arg6: bool, arg7: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean,float,boolean,java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4), __float.valueOf(arg5), __boolean.valueOf(arg6), arg7))

    @overload
    def actuallyEnd(self):
        """public void dev.ultreon.quantum.client.gui.Renderer.actuallyEnd()"""
        super(Renderer, self).actuallyEnd()

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def drawSprite(self, arg0: 'Sprite', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.drawSprite(dev.ultreon.quantum.client.gui.Sprite,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).drawSprite(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), arg11))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __boolean.valueOf(arg5)))

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def textCenter(self, arg0: str, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def blurred(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(java.lang.Runnable)"""
        super(__Renderer, self).blurred(arg0)

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.resize(int,int)"""
        super(__Renderer, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def obtainRenderable(self) -> 'g3d.Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable dev.ultreon.quantum.client.gui.Renderer.obtainRenderable()"""
        return 'g3d.Renderable'.__wrap(super(Renderer, self).obtainRenderable())

    @overload
    def textCenter(self, arg0: 'List', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def textCenter(self, arg0: 'List', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'ColorCode', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.text.ColorCode,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: int, arg3: int, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __boolean.valueOf(arg5)))

    @overload
    def textCenter(self, arg0: 'List', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def __init__(self, arg0: 'ShapeDrawer', arg1: 'Matrices'):
        """public dev.ultreon.quantum.client.gui.Renderer(space.earlygrey.shapedrawer.ShapeDrawer,dev.ultreon.quantum.client.gui.Matrices)"""
        val = __Renderer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def scale(self, arg0: float, arg1: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.scale(double,double)"""
        return 'Renderer'.__wrap(super(__Renderer, self).scale(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5)))

    @overload
    def textRight(self, arg0: 'List', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def pushScissors(self, arg0: 'Bounds') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Renderer.pushScissors(dev.ultreon.quantum.client.gui.Bounds)"""
        return bool.__wrap(super(__Renderer, self).pushScissors(arg0))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def renderFrame(self, arg0: 'Identifier', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.renderFrame(dev.ultreon.quantum.util.Identifier,int,int,int,int,int,int,int,int,int,int)"""
        super(__Renderer, self).renderFrame(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def setBlitColor(self, arg0: 'Color'):
        """public void dev.ultreon.quantum.client.gui.Renderer.setBlitColor(dev.ultreon.quantum.util.Color)"""
        super(__Renderer, self).setBlitColor(arg0)

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: str, arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def box(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.box(int,int,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).box(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @overload
    def draw9Slice(self, arg0: 'Identifier', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.draw9Slice(dev.ultreon.quantum.util.Identifier,int,int,int,int,int,int,int,int,int,int,int)"""
        super(__Renderer, self).draw9Slice(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11))

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def blurred(self, arg0: 'Texture'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(com.badlogic.gdx.graphics.Texture)"""
        super(__Renderer, self).blurred(arg0)

    @overload
    def textRight(self, arg0: str, arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textMultiline(self, arg0: str, arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textMultiline(java.lang.String,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textMultiline(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4)))

    @overload
    def setColor(self, arg0: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).setColor(__int.valueOf(arg0)))

    @overload
    def rect3DLine(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rect3DLine(int,int,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).rect3DLine(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4)))

    @overload
    def fill(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.fill(int,int,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).fill(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @overload
    def pushScissors(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Renderer.pushScissors(float,float,float,float)"""
        return bool.__wrap(super(__Renderer, self).pushScissors(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: 'List', arg1: int, arg2: int, arg3: 'ColorCode') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.text.ColorCode)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), arg9))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5)))

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,float,float,float,float,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), arg11))

    @overload
    def textLeft(self, arg0: 'List', arg1: int, arg2: int, arg3: 'ColorCode', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.text.ColorCode,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textRight(self, arg0: str, arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def fill(self, arg0: 'Vec4i') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.fill(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Renderer'.__wrap(super(__Renderer, self).fill(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Renderer.toString()"""
        return str.__wrap(super(Renderer, self).toString())

    @overload
    def textLeft(self, arg0: 'List', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def pushScissorsRaw(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Renderer.pushScissorsRaw(int,int,int,int)"""
        return bool.__wrap(super(__Renderer, self).pushScissorsRaw(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: 'List', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def scissorOffset(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.scissorOffset(int,int)"""
        super(__Renderer, self).scissorOffset(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def textCenter(self, arg0: str, arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def textLeft(self, arg0: str, arg1: int, arg2: int, arg3: 'ColorCode', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,int,int,dev.ultreon.quantum.text.ColorCode,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @overload
    def textRight(self, arg0: 'List', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def textRight(self, arg0: str, arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def fill(self, arg0: 'Ellipse2D') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.fill(java.awt.geom.Ellipse2D)"""
        return 'Renderer'.__wrap(super(__Renderer, self).fill(arg0))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setColor(self, arg0: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).setColor(arg0))

    @overload
    def textRight(self, arg0: 'List', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: str, arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def blurred(self, arg0: bool, arg1: int, arg2: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(boolean,int,java.lang.Runnable)"""
        super(__Renderer, self).blurred(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def clearColor(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).clearColor(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: int, arg3: int, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __boolean.valueOf(arg5)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'List', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,float,java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4))

    @overload
    def ovalLine(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.ovalLine(int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).ovalLine(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'ColorCode', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.text.ColorCode,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def pushScissors(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Renderer.pushScissors(int,int,int,int)"""
        return bool.__wrap(super(__Renderer, self).pushScissors(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def invertOff(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.invertOff()"""
        return 'Renderer'.__wrap(super(Renderer, self).invertOff())

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def popMatrix(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.popMatrix()"""
        return 'Renderer'.__wrap(super(Renderer, self).popMatrix())

    @overload
    def getFont(self) -> 'font.Font':
        """public dev.ultreon.quantum.client.font.Font dev.ultreon.quantum.client.gui.Renderer.getFont()"""
        return 'font.Font'.__wrap(super(Renderer, self).getFont())

    @overload
    def invertOn(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.invertOn()"""
        return 'Renderer'.__wrap(super(Renderer, self).invertOn())

    @overload
    def clearColor(self, arg0: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).clearColor(arg0))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: bool, arg5: float, arg6: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean,float,java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4), __float.valueOf(arg5), arg6))

    @overload
    def fill(self, arg0: 'Rectangle2D') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.fill(java.awt.geom.Rectangle2D)"""
        return 'Renderer'.__wrap(super(__Renderer, self).fill(arg0))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: float, arg5: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.util.Color,float,java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __float.valueOf(arg4), arg5))

    @overload
    def blurred(self, arg0: float, arg1: bool, arg2: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(float,boolean,java.lang.Runnable)"""
        super(__Renderer, self).blurred(__float.valueOf(arg0), __boolean.valueOf(arg1), arg2)

    @overload
    def setColor(self, arg0: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).setColor(arg0))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def draw9PatchTexture(self, arg0: 'Texture', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.draw9PatchTexture(com.badlogic.gdx.graphics.Texture,int,int,int,int,int,int,int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).draw9PatchTexture(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10)))

    @overload
    def draw9Slice(self, arg0: 'Texture', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.draw9Slice(com.badlogic.gdx.graphics.Texture,int,int,int,int,int,int,int,int,int,int,int)"""
        super(__Renderer, self).draw9Slice(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: float, arg5: bool, arg6: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.util.Color,float,boolean,java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __float.valueOf(arg4), __boolean.valueOf(arg5), arg6))

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8)))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __boolean.valueOf(arg5)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'ColorCode') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.text.ColorCode)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def oval(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.oval(int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).oval(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def textRight(self, arg0: 'List', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def rect3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rect3D(int,int,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).rect3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4)))

    @overload
    def rect(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rect(int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).rect(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.line(float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5)))

    @overload
    def textLeft(self, arg0: 'List', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'ColorCode', arg4: float, arg5: bool, arg6: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.text.ColorCode,float,boolean,java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __float.valueOf(arg4), __boolean.valueOf(arg5), arg6))

    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Renderer.getHeight()"""
        return int.__wrap(super(Renderer, self).getHeight())

    @overload
    def textCenter(self, arg0: 'List', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def circleLine(self, arg0: float, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.circleLine(float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).circleLine(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def polygon(self, arg0: 'float', arg1: 'Color', arg2: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.polygon(float[],dev.ultreon.quantum.util.Color,int)"""
        super(__Renderer, self).polygon(arg0, arg1, __int.valueOf(arg2))

    @overload
    def clear(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clear()"""
        return 'Renderer'.__wrap(super(Renderer, self).clear())

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'List', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textRight(self, arg0: 'List', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textTabbed(self, arg0: str, arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textTabbed(java.lang.String,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textTabbed(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: str, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def clearScissors(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearScissors()"""
        return 'Renderer'.__wrap(super(Renderer, self).clearScissors())

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), arg7))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def blurred(self, arg0: float, arg1: float, arg2: bool, arg3: int, arg4: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(float,float,boolean,int,java.lang.Runnable)"""
        super(__Renderer, self).blurred(__float.valueOf(arg0), __float.valueOf(arg1), __boolean.valueOf(arg2), __int.valueOf(arg3), arg4)

    @overload
    def getMatrices(self) -> 'Matrices':
        """public dev.ultreon.quantum.client.gui.Matrices dev.ultreon.quantum.client.gui.Renderer.getMatrices()"""
        return 'Matrices'.__wrap(super(Renderer, self).getMatrices())

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @overload
    def translate(self, arg0: float, arg1: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.translate(float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).translate(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def arcLine(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.arcLine(int,int,int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).arcLine(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6)))

    @overload
    def setColor(self, arg0: int, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).setColor(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def clearColor(self, arg0: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).clearColor(__int.valueOf(arg0)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def line(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.line(int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).line(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def setColor(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).setColor(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.translate(float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).translate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'ColorCode', arg4: bool, arg5: float, arg6: bool, arg7: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.text.ColorCode,boolean,float,boolean,java.lang.String)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4), __float.valueOf(arg5), __boolean.valueOf(arg6), arg7))

    @overload
    def textLeft(self, arg0: 'List', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: int, arg3: int, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: str, arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def getBlitColor(self) -> 'util.Color':
        """public dev.ultreon.quantum.util.Color dev.ultreon.quantum.client.gui.Renderer.getBlitColor()"""
        return 'util.Color'.__wrap(super(Renderer, self).getBlitColor())

    @overload
    def textLeft(self, arg0: str, arg1: int, arg2: int, arg3: 'ColorCode') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,int,int,dev.ultreon.quantum.text.ColorCode)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def unsetShader(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.unsetShader()"""
        return 'Renderer'.__wrap(super(Renderer, self).unsetShader())

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: int, arg3: int, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @overload
    def clearColor(self, arg0: int, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).clearColor(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def flush(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.flush()"""
        return 'Renderer'.__wrap(super(Renderer, self).flush())

    @overload
    def arc(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.arc(int,int,int,int,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).arc(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @overload
    def model(self, arg0: 'Runnable') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.model(java.lang.Runnable)"""
        return 'Renderer'.__wrap(super(__Renderer, self).model(arg0))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def textTabbed(self, arg0: str, arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textTabbed(java.lang.String,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textTabbed(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def textLeft(self, arg0: str, arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'ColorCode') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.text.ColorCode)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def outline(self, arg0: 'Ellipse2D') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.outline(java.awt.geom.Ellipse2D)"""
        return 'Renderer'.__wrap(super(__Renderer, self).outline(arg0))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4))

    @overload
    def textRight(self, arg0: 'List', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,float)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textRight(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: 'List', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textCenter(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def blurred(self, arg0: float, arg1: bool, arg2: int, arg3: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(float,boolean,int,java.lang.Runnable)"""
        super(__Renderer, self).blurred(__float.valueOf(arg0), __boolean.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def outline(self, arg0: 'Line2D') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.outline(java.awt.geom.Line2D)"""
        return 'Renderer'.__wrap(super(__Renderer, self).outline(arg0))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,int,int,boolean)"""
        return 'Renderer'.__wrap(super(__Renderer, self).textLeft(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def resetGrid(self):
        """public void dev.ultreon.quantum.client.gui.Renderer.resetGrid()"""
        super(Renderer, self).resetGrid()

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,int,int)"""
        return 'Renderer'.__wrap(super(__Renderer, self).blit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10)))

    @overload
    def fill(self, arg0: 'Line2D') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.fill(java.awt.geom.Line2D)"""
        return 'Renderer'.__wrap(super(__Renderer, self).fill(arg0))

    @overload
    def __init__(self, arg0: 'ShapeDrawer'):
        """public dev.ultreon.quantum.client.gui.Renderer(space.earlygrey.shapedrawer.ShapeDrawer)"""
        val = __Renderer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Position
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Position():
    """dev.ultreon.quantum.client.gui.Position"""
 
    @staticmethod
    def __wrap(java_value: __Position) -> 'Position':
        return Position(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Position):
        """
        Dynamic initializer for Position.
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

    @overload
    def idt(self):
        """public void dev.ultreon.quantum.client.gui.Position.idt()"""
        super(Position, self).idt()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Position.equals(java.lang.Object)"""
        return bool.__wrap(super(__Position, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.Position(int,int)"""
        val = __Position(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.Position.set(dev.ultreon.quantum.client.gui.Position)"""
        super(__Position, self).set(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Position.toString()"""
        return str.__wrap(super(Position, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Position.hashCode()"""
        return int.__wrap(super(Position, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.Position()"""
        val = __Position()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def set(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Position.set(int,int)"""
        super(__Position, self).set(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def cpy(self) -> 'Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.Position.cpy()"""
        return 'Position'.__wrap(super(Position, self).cpy())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.Position(int)"""
        val = __Position(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.Position()"""
        val = __Position()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Callback
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.Callback as __Callback
__Callback = __Callback
from abc import abstractmethod, ABC
 
class Callback(ABC):
    """dev.ultreon.quantum.client.gui.Callback"""
 
    @staticmethod
    def __wrap(java_value: __Callback) -> 'Callback':
        return Callback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Callback):
        """
        Dynamic initializer for Callback.
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
    def call0(self, arg0: object):
        """public default void dev.ultreon.quantum.client.gui.Callback.call0(java.lang.Object)"""
        super(__Callback, self).call0(arg0)

    @abstractmethod
    def call(self, arg0: object):
        """public abstract void dev.ultreon.quantum.client.gui.Callback.call(T)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.TitleWidget
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import dev.ultreon.quantum.client.gui.Screen as __Screen
__Screen = __Screen
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
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

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

import dev.ultreon.quantum.client.gui.TitleWidget as __TitleWidget
__TitleWidget = __TitleWidget
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
 
class TitleWidget():
    """dev.ultreon.quantum.client.gui.TitleWidget"""
 
    @staticmethod
    def __wrap(java_value: __TitleWidget) -> 'TitleWidget':
        return TitleWidget(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TitleWidget):
        """
        Dynamic initializer for TitleWidget.
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
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(widget.Widget, self).isEnabled())

    @overload
    def __init__(self, arg0: 'Screen', arg1: 'TextObject'):
        """public dev.ultreon.quantum.client.gui.TitleWidget(dev.ultreon.quantum.client.gui.Screen,dev.ultreon.quantum.text.TextObject)"""
        val = __TitleWidget(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str.__wrap(super(widget.Widget, self).getName())

    @overload
    def getScreen(self) -> 'Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.TitleWidget.getScreen()"""
        return 'Screen'.__wrap(super(TitleWidget, self).getScreen())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(widget.Widget, self).isClickable())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.TitleWidget.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.Widget'.__wrap(super(__TitleWidget, self).bounds(arg0))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__widget.Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(widget.Widget, self).isFocused())

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool.__wrap(super(__widget.Widget, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__widget.Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def position(self, arg0: 'Supplier') -> 'TitleWidget':
        """public dev.ultreon.quantum.client.gui.TitleWidget dev.ultreon.quantum.client.gui.TitleWidget.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'TitleWidget'.__wrap(super(__TitleWidget, self).position(arg0))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__widget.Widget, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__widget.Widget, self).onDisconnect(arg0)

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool.__wrap(super(__widget.Widget, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.TitleWidget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__TitleWidget, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__widget.Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__widget.Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__widget.Widget, self).setBounds(arg0)

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(widget.Widget, self).revalidate()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__widget.Widget, self).setPos(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__widget.Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__widget.Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__widget.Widget, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__widget.Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(widget.Widget, self).getPreferredHeight())

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.TitleWidget.mousePress(int,int,int)"""
        return bool.__wrap(super(__TitleWidget, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__widget.Widget, self).setEnabled(__boolean.valueOf(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__widget.Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def getBounds(self) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'Bounds'.__wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool.__wrap(super(__widget.Widget, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.TitleWidget.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__TitleWidget, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

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
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(widget.Widget, self).isHovered())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__widget.Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(widget.Widget, self).getPreferredWidth())

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__widget.Widget, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__widget.Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'.__wrap(super(widget.Widget, self).path())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getPreferredPos(self) -> 'Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'Position'.__wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__widget.Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(__widget.Widget, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__widget.Widget, self).onRevalidate(arg0)

    @overload
    def getParent(self) -> 'Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.TitleWidget.getParent()"""
        return 'Screen'.__wrap(super(TitleWidget, self).getParent())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(widget.Widget, self).getWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(widget.Widget, self).componentRegistry())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(widget.Widget, self).getX())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__widget.Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def parent(self, arg0: 'Screen'):
        """public void dev.ultreon.quantum.client.gui.TitleWidget.parent(dev.ultreon.quantum.client.gui.Screen)"""
        super(__TitleWidget, self).parent(arg0)

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__widget.Widget, self).y(__int.valueOf(arg0))

    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.TitleWidget.getTitle()"""
        return 'text.TextObject'.__wrap(super(TitleWidget, self).getTitle())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__widget.Widget, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def getPreferredSize(self) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'Size'.__wrap(super(widget.Widget, self).getPreferredSize())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__widget.Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__widget.Widget, self).height(__int.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__widget.Widget, self).setSize(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.DialogBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import dev.ultreon.quantum.client.gui.DialogBuilder as __DialogBuilder
__DialogBuilder = __DialogBuilder
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DialogBuilder():
    """dev.ultreon.quantum.client.gui.DialogBuilder"""
 
    @staticmethod
    def __wrap(java_value: __DialogBuilder) -> 'DialogBuilder':
        return DialogBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DialogBuilder):
        """
        Dynamic initializer for DialogBuilder.
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
    def button(self, arg0: 'TextObject', arg1: 'Runnable') -> 'DialogBuilder':
        """public dev.ultreon.quantum.client.gui.DialogBuilder dev.ultreon.quantum.client.gui.DialogBuilder.button(dev.ultreon.quantum.text.TextObject,java.lang.Runnable)"""
        return 'DialogBuilder'.__wrap(super(__DialogBuilder, self).button(arg0, arg1))

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

    @overload
    def message(self, arg0: 'TextObject') -> 'DialogBuilder':
        """public dev.ultreon.quantum.client.gui.DialogBuilder dev.ultreon.quantum.client.gui.DialogBuilder.message(dev.ultreon.quantum.text.TextObject)"""
        return 'DialogBuilder'.__wrap(super(__DialogBuilder, self).message(arg0))

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
    def title(self, arg0: 'TextObject') -> 'DialogBuilder':
        """public dev.ultreon.quantum.client.gui.DialogBuilder dev.ultreon.quantum.client.gui.DialogBuilder.title(dev.ultreon.quantum.text.TextObject)"""
        return 'DialogBuilder'.__wrap(super(__DialogBuilder, self).title(arg0))

    @overload
    def __init__(self, arg0: 'Screen'):
        """public dev.ultreon.quantum.client.gui.DialogBuilder(dev.ultreon.quantum.client.gui.Screen)"""
        val = __DialogBuilder(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def button(self, arg0: 'TextObject', arg1: 'Callback') -> 'DialogBuilder':
        """public dev.ultreon.quantum.client.gui.DialogBuilder dev.ultreon.quantum.client.gui.DialogBuilder.button(dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.Dialog>)"""
        return 'DialogBuilder'.__wrap(super(__DialogBuilder, self).button(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Sprite
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import dev.ultreon.quantum.client.gui.Sprite as __Sprite
__Sprite = __Sprite
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Sprite():
    """dev.ultreon.quantum.client.gui.Sprite"""
 
    @staticmethod
    def __wrap(java_value: __Sprite) -> 'Sprite':
        return Sprite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Sprite):
        """
        Dynamic initializer for Sprite.
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
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Sprite.getWidth()"""
        return int.__wrap(super(Sprite, self).getWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Sprite.getHeight()"""
        return int.__wrap(super(Sprite, self).getHeight())

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
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: int, arg4: int):
        """public void dev.ultreon.quantum.client.gui.Sprite.render(dev.ultreon.quantum.client.gui.Renderer,int,int,int,int)"""
        super(__Sprite, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.client.gui.Sprite(dev.ultreon.quantum.util.Identifier)"""
        val = __Sprite(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Alignment
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
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
import dev.ultreon.quantum.client.gui.Alignment as __Alignment
__Alignment = __Alignment
from builtins import int
 
class Alignment():
    """dev.ultreon.quantum.client.gui.Alignment"""
 
    @staticmethod
    def __wrap(java_value: __Alignment) -> 'Alignment':
        return Alignment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Alignment):
        """
        Dynamic initializer for Alignment.
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
 
    # public static final dev.ultreon.quantum.client.gui.Alignment dev.ultreon.quantum.client.gui.Alignment.CENTER
    CENTER: 'Alignment' = __wrap(__Alignment.CENTER)

    # public static final dev.ultreon.quantum.client.gui.Alignment dev.ultreon.quantum.client.gui.Alignment.LEFT
    LEFT: 'Alignment' = __wrap(__Alignment.LEFT)

    # public static final dev.ultreon.quantum.client.gui.Alignment dev.ultreon.quantum.client.gui.Alignment.RIGHT
    RIGHT: 'Alignment' = __wrap(__Alignment.RIGHT)


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
    def values() -> List['Alignment']:
        """public static dev.ultreon.quantum.client.gui.Alignment[] dev.ultreon.quantum.client.gui.Alignment.values()"""
        return List[Alignment].__wrap(__Alignment.values())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Alignment':
        """public static dev.ultreon.quantum.client.gui.Alignment dev.ultreon.quantum.client.gui.Alignment.valueOf(java.lang.String)"""
        return Alignment.__wrap(__Alignment.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Notification$Builder
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.gui.icon.Icon as __Icon
__Icon = __Icon
from builtins import str
import dev.ultreon.quantum.client.gui.Notification as __Notification
__Notification = __Notification
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.gui import icon
except ImportError:
    icon = __import_once__("pyquantum.client.gui.icon")

try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.client.gui.Notification as __Notification_Builder
__Builder = __Notification_Builder.Builder
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from pycorelibs.datetime import v0
except ImportError:
    v0 = __import_once__("pycorelibs.datetime.v0")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Builder():
    """dev.ultreon.quantum.client.gui.Notification.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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

    @overload
    def duration(self, arg0: 'Duration') -> 'Builder':
        """public dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification$Builder.duration(dev.ultreon.libs.datetime.v0.Duration)"""
        return 'Builder'.__wrap(super(__Builder, self).duration(arg0))

    @property
    def icon(self) -> Icon:
        return Icon.__wrap(super(__Builder).icon())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @property
    def icon(self, value: 'icon.Icon'):
        super(__Builder).icon(value)

    @overload
    def build(self) -> 'Notification':
        """public dev.ultreon.quantum.client.gui.Notification dev.ultreon.quantum.client.gui.Notification$Builder.build()"""
        return 'Notification'.__wrap(super(Builder, self).build())

    @overload
    def sticky(self) -> 'Builder':
        """public dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification$Builder.sticky()"""
        return 'Builder'.__wrap(super(Builder, self).sticky())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def subText(self, arg0: str) -> 'Builder':
        """public dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification$Builder.subText(java.lang.String)"""
        return 'Builder'.__wrap(super(__Builder, self).subText(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def icon(self, arg0: 'Icon') -> 'Builder':
        """public dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification$Builder.icon(dev.ultreon.quantum.client.gui.icon.Icon)"""
        return 'Builder'.__wrap(super(__Builder, self).icon(arg0))

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
    def subText(self, arg0: 'MutableText') -> 'Builder':
        """public dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification$Builder.subText(dev.ultreon.quantum.text.MutableText)"""
        return 'Builder'.__wrap(super(__Builder, self).subText(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.GlStateStack$GlState
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.util.RgbColor as __RgbColor
__RgbColor = __RgbColor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.gui.GlStateStack as __GlStateStack_GlState
__GlState = __GlStateStack_GlState.GlState
from builtins import int
 
class GlState():
    """dev.ultreon.quantum.client.gui.GlStateStack.GlState"""
 
    @staticmethod
    def __wrap(java_value: __GlState) -> 'GlState':
        return GlState(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GlState):
        """
        Dynamic initializer for GlState.
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
    def apply(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack$GlState.apply()"""
        super(GlState, self).apply()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @property
    def blendColor(self) -> RgbColor:
        return RgbColor.__wrap(super(__GlState).blendColor())

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.GlStateStack$GlState()"""
        val = __GlState()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.GlStateStack$GlState()"""
        val = __GlState()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'GlState'):
        """public dev.ultreon.quantum.client.gui.GlStateStack$GlState(dev.ultreon.quantum.client.gui.GlStateStack$GlState)"""
        val = __GlState(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @property
    def blendColor(self, value: 'util.RgbColor'):
        super(__GlState).blendColor(value)