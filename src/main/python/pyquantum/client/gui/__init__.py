from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import dev.ultreon.quantum.client.gui.NotifyManager as _NotifyManager
_NotifyManager = _NotifyManager
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NotifyManager():
    """dev.ultreon.quantum.client.gui.NotifyManager"""
 
    @staticmethod
    def _wrap(java_value: _NotifyManager) -> 'NotifyManager':
        return NotifyManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NotifyManager):
        """
        Dynamic initializer for NotifyManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NotifyManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NotifyManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def unavailable(self, arg0: str):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.unavailable(java.lang.String)"""
        super(_NotifyManager, self).unavailable(arg0)

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.gui.NotifyManager(dev.ultreon.quantum.client.QuantumClient)"""
        val = _NotifyManager(arg0)
        self.__wrapper = val

    @overload
    def add(self, arg0: 'Notification'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(dev.ultreon.quantum.client.gui.Notification)"""
        super(_NotifyManager, self).add(arg0)

    @overload
    def addOnce(self, arg0: 'UUID', arg1: 'Notification'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.addOnce(java.util.UUID,dev.ultreon.quantum.client.gui.Notification)"""
        super(_NotifyManager, self).addOnce(arg0, arg1)

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
    def add(self, arg0: str, arg1: str):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(java.lang.String,java.lang.String)"""
        super(_NotifyManager, self).add(arg0, arg1)

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_NotifyManager, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def add(self, arg0: str, arg1: str, arg2: str):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(java.lang.String,java.lang.String,java.lang.String)"""
        super(_NotifyManager, self).add(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def add(self, arg0: 'MutableText', arg1: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText)"""
        super(_NotifyManager, self).add(arg0, arg1)

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: 'MutableText', arg1: 'MutableText', arg2: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText)"""
        super(_NotifyManager, self).add(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.NotifyManager
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import dev.ultreon.quantum.client.gui.NotifyManager as _NotifyManager
_NotifyManager = _NotifyManager
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NotifyManager():
    """dev.ultreon.quantum.client.gui.NotifyManager"""
 
    @staticmethod
    def _wrap(java_value: _NotifyManager) -> 'NotifyManager':
        return NotifyManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NotifyManager):
        """
        Dynamic initializer for NotifyManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NotifyManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NotifyManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def unavailable(self, arg0: str):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.unavailable(java.lang.String)"""
        super(_NotifyManager, self).unavailable(arg0)

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.gui.NotifyManager(dev.ultreon.quantum.client.QuantumClient)"""
        val = _NotifyManager(arg0)
        self.__wrapper = val

    @overload
    def add(self, arg0: 'Notification'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(dev.ultreon.quantum.client.gui.Notification)"""
        super(_NotifyManager, self).add(arg0)

    @overload
    def addOnce(self, arg0: 'UUID', arg1: 'Notification'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.addOnce(java.util.UUID,dev.ultreon.quantum.client.gui.Notification)"""
        super(_NotifyManager, self).addOnce(arg0, arg1)

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
    def add(self, arg0: str, arg1: str):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(java.lang.String,java.lang.String)"""
        super(_NotifyManager, self).add(arg0, arg1)

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_NotifyManager, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def add(self, arg0: str, arg1: str, arg2: str):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(java.lang.String,java.lang.String,java.lang.String)"""
        super(_NotifyManager, self).add(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def add(self, arg0: 'MutableText', arg1: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText)"""
        super(_NotifyManager, self).add(arg0, arg1)

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: 'MutableText', arg1: 'MutableText', arg2: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.NotifyManager.add(dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText)"""
        super(_NotifyManager, self).add(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.NotifyManager 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Screen
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
from abc import abstractmethod, ABC
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
 
class Screen():
    """dev.ultreon.quantum.client.gui.Screen"""
 
    @staticmethod
    def _wrap(java_value: _Screen) -> 'Screen':
        return Screen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Screen):
        """
        Dynamic initializer for Screen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Screen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Screen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_Screen, self).keyRelease(_int.valueOf(arg0)))

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool._wrap(super(_Screen, self).filesDropped(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str._wrap(super(Screen, self).getRawTitle())

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
    def getPreferredSize(self) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'Size'._wrap(super(widget.Widget, self).getPreferredSize())

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
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_widget.Widget, self).width(_int.valueOf(arg0))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool._wrap(super(_Screen, self).charType(_char.valueOf(arg0)))

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
    def title(self, arg0: 'TextObject') -> 'Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'Screen'._wrap(super(_Screen, self).title(arg0))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(widget.Widget, self).getY())

    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canClose()"""
        return bool._wrap(super(Screen, self).canClose())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_widget.Widget, self).setVisible(_boolean.valueOf(arg0))

    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool._wrap(super(Screen, self).isHoveringClickable())

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

    @overload
    def titleTranslation(self, arg0: str) -> 'Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'Screen'._wrap(super(_Screen, self).titleTranslation(arg0))

    @override
    @overload
    def getPreferredPos(self) -> 'Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'Position'._wrap(super(widget.Widget, self).getPreferredPos())

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

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

    @abstractmethod
    def build(self, arg0: 'GuiBuilder'):
        """public abstract void dev.ultreon.quantum.client.gui.Screen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        pass

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Screen, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool._wrap(super(_Screen, self).onClose(arg0))

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
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_widget.Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool._wrap(super(_Screen, self).keyPress(_int.valueOf(arg0)))

    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(_Screen, self).closeDialog(arg0)

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

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_widget.Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(_Screen, self).showDialog(arg0)

    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canCloseWithEsc()"""
        return bool._wrap(super(Screen, self).canCloseWithEsc())

    @overload
    def title(self, arg0: str) -> 'Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'Screen'._wrap(super(_Screen, self).title(arg0))

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
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_widget.Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @property
    def parentScreen(self, value: 'Screen'):
        super(_Screen).parentScreen(value)

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(_Screen, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'._wrap(super(Screen, self).getTitle())

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
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool._wrap(super(Screen, self).back())

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_widget.Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'._wrap(super(_Screen, self).add(arg0))

    @overload
    def getDialog(self) -> 'Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'Dialog'._wrap(super(Screen, self).getDialog())

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'._wrap(super(Screen, self).path())

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
    def getBounds(self) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'Bounds'._wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str._wrap(super(Screen, self).getName())

    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(_Screen, self).init(_int.valueOf(arg0), _int.valueOf(arg1))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Hud
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.Hud as _Hud
_Hud = _Hud
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Hud():
    """dev.ultreon.quantum.client.gui.Hud"""
 
    @staticmethod
    def _wrap(java_value: _Hud) -> 'Hud':
        return Hud(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Hud):
        """
        Dynamic initializer for Hud.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Hud__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Hud__wrapper":
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

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Hud.touchDown(int,int,int,int)"""
        return bool._wrap(super(_Hud, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Hud.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Hud, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Hud.touchUp(int,int,int,int)"""
        return bool._wrap(super(_Hud, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.gui.Hud(dev.ultreon.quantum.client.QuantumClient)"""
        val = _Hud(arg0)
        self.__wrapper = val

    @overload
    def isMouseOver(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Hud.isMouseOver(int,int)"""
        return bool._wrap(super(_Hud, self).isMouseOver(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.GuiBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.gui.GuiBuilder as _GuiBuilder
_GuiBuilder = _GuiBuilder
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.Screen as _Screen
_Screen = _Screen
import dev.ultreon.quantum.client.gui.widget.Widget as _Widget
_Widget = _Widget
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GuiBuilder():
    """dev.ultreon.quantum.client.gui.GuiBuilder"""
 
    @staticmethod
    def _wrap(java_value: _GuiBuilder) -> 'GuiBuilder':
        return GuiBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GuiBuilder):
        """
        Dynamic initializer for GuiBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GuiBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GuiBuilder__wrapper":
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
    def __init__(self, arg0: 'Screen'):
        """public dev.ultreon.quantum.client.gui.GuiBuilder(dev.ultreon.quantum.client.gui.Screen)"""
        val = _GuiBuilder(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.GuiBuilder.equals(java.lang.Object)"""
        return bool._wrap(super(_GuiBuilder, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.GuiBuilder.toString()"""
        return str._wrap(super(GuiBuilder, self).toString())

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

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <T extends dev.ultreon.quantum.client.gui.widget.Widget> T dev.ultreon.quantum.client.gui.GuiBuilder.add(T)"""
        return 'widget.Widget'._wrap(super(_GuiBuilder, self).add(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.GuiBuilder.hashCode()"""
        return int._wrap(super(GuiBuilder, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def screen(self) -> 'Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.GuiBuilder.screen()"""
        return 'Screen'._wrap(super(GuiBuilder, self).screen()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.GuiStateListener
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.gui.GuiStateListener as _GuiStateListener
_GuiStateListener = _GuiStateListener
 
class GuiStateListener():
    """dev.ultreon.quantum.client.gui.GuiStateListener"""
 
    @staticmethod
    def _wrap(java_value: _GuiStateListener) -> 'GuiStateListener':
        return GuiStateListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GuiStateListener):
        """
        Dynamic initializer for GuiStateListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GuiStateListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GuiStateListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Size():
    """dev.ultreon.quantum.client.gui.Size"""
 
    @staticmethod
    def _wrap(java_value: _Size) -> 'Size':
        return Size(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Size):
        """
        Dynamic initializer for Size.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Size__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Size__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.Size()"""
        val = _Size()
        self.__wrapper = val

    @override
    @overload
    def cpy(self) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.Size.cpy()"""
        return 'Size'._wrap(super(Size, self).cpy())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Size.equals(java.lang.Object)"""
        return bool._wrap(super(_Size, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.Size(int,int)"""
        val = _Size(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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
    def set(self, arg0: int, arg1: int) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.Size.set(int,int)"""
        return 'Size'._wrap(super(_Size, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Size') -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.Size.set(dev.ultreon.quantum.client.gui.Size)"""
        return 'Size'._wrap(super(_Size, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def idt(self):
        """public void dev.ultreon.quantum.client.gui.Size.idt()"""
        super(Size, self).idt()

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Size.toString()"""
        return str._wrap(super(Size, self).toString())

    @overload
    def set(self, arg0: int) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.Size.set(int)"""
        return 'Size'._wrap(super(_Size, self).set(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.Size(int)"""
        val = _Size(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.Size()"""
        val = _Size()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Size.hashCode()"""
        return int._wrap(super(Size, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.GlStateStack
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.gui.GlStateStack as _GlStateStack
_GlStateStack = _GlStateStack
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GlStateStack():
    """dev.ultreon.quantum.client.gui.GlStateStack"""
 
    @staticmethod
    def _wrap(java_value: _GlStateStack) -> 'GlStateStack':
        return GlStateStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GlStateStack):
        """
        Dynamic initializer for GlStateStack.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GlStateStack__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GlStateStack__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def end(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.end()"""
        super(GlStateStack, self).end()

    @overload
    def disableDepthTest(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.disableDepthTest()"""
        super(GlStateStack, self).disableDepthTest()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.GlStateStack()"""
        val = _GlStateStack()
        self.__wrapper = val

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
    def blendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.blendFuncSeparate(int,int,int,int)"""
        super(_GlStateStack, self).blendFuncSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def blendEquationSeparate(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.blendEquationSeparate(int,int)"""
        super(_GlStateStack, self).blendEquationSeparate(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def enableBlending(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.enableBlending()"""
        super(GlStateStack, self).enableBlending()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def blendFunc(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.blendFunc(int,int)"""
        super(_GlStateStack, self).blendFunc(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def enableDepthTest(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.enableDepthTest()"""
        super(GlStateStack, self).enableDepthTest()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.GlStateStack()"""
        val = _GlStateStack()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def push(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack.push()"""
        super(GlStateStack, self).push()

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
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Sprite$Meta
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.Sprite as _Sprite_Meta
_Meta = _Sprite_Meta.Meta
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Meta():
    """dev.ultreon.quantum.client.gui.Sprite.Meta"""
 
    @staticmethod
    def _wrap(java_value: _Meta) -> 'Meta':
        return Meta(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Meta):
        """
        Dynamic initializer for Meta.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Meta__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Meta__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.Sprite$Meta(int,int,int,int)"""
        val = _Meta(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool):
        """public dev.ultreon.quantum.client.gui.Sprite$Meta(int,int,int,int,boolean)"""
        val = _Meta(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4))
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
 
 
# CLASS: dev.ultreon.quantum.client.gui.Matrices
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.gui.Matrices as _Matrices
_Matrices = _Matrices
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Quaternion as _Quaternion
_Quaternion = _Quaternion
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Matrices():
    """dev.ultreon.quantum.client.gui.Matrices"""
 
    @staticmethod
    def _wrap(java_value: _Matrices) -> 'Matrices':
        return Matrices(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Matrices):
        """
        Dynamic initializer for Matrices.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Matrices__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Matrices__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Matrices.toString()"""
        return str._wrap(super(Matrices, self).toString())

    @overload
    def pop(self):
        """public void dev.ultreon.quantum.client.gui.Matrices.pop()"""
        super(Matrices, self).pop()

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
    def getTranslation(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.gui.Matrices.getTranslation(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Matrices, self).getTranslation(arg0))

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
    def __init__(self, arg0: 'Matrix4'):
        """public dev.ultreon.quantum.client.gui.Matrices(com.badlogic.gdx.math.Matrix4)"""
        val = _Matrices(arg0)
        self.__wrapper = val

    @overload
    def push(self):
        """public void dev.ultreon.quantum.client.gui.Matrices.push()"""
        super(Matrices, self).push()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def last(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.gui.Matrices.last()"""
        return 'math.Matrix4'._wrap(super(Matrices, self).last())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.Matrices()"""
        val = _Matrices()
        self.__wrapper = val

    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void dev.ultreon.quantum.client.gui.Matrices.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(_Matrices, self).rotate(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.Matrices()"""
        val = _Matrices()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getScale(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.gui.Matrices.getScale(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Matrices, self).getScale(arg0))

    @overload
    def isClear(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Matrices.isClear()"""
        return bool._wrap(super(Matrices, self).isClear())

    @overload
    def getRotation(self, arg0: 'Quaternion') -> 'math.Quaternion':
        """public com.badlogic.gdx.math.Quaternion dev.ultreon.quantum.client.gui.Matrices.getRotation(com.badlogic.gdx.math.Quaternion)"""
        return 'math.Quaternion'._wrap(super(_Matrices, self).getRotation(arg0))

    @overload
    def getScale(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.gui.Matrices.getScale(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Matrices, self).getScale(arg0))

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.gui.Matrices.translate(float,float,float)"""
        super(_Matrices, self).translate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTranslation(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.gui.Matrices.getTranslation(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Matrices, self).getTranslation(arg0))

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.client.gui.Matrices.translate(float,float)"""
        super(_Matrices, self).translate(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.client.gui.Matrices.translate(double,double)"""
        super(_Matrices, self).translate(_double.valueOf(arg0), _double.valueOf(arg1))

    @overload
    def scale(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.client.gui.Matrices.scale(float,float)"""
        super(_Matrices, self).scale(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Dialog
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

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
 
class Dialog():
    """dev.ultreon.quantum.client.gui.Dialog"""
 
    @staticmethod
    def _wrap(java_value: _Dialog) -> 'Dialog':
        return Dialog(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Dialog):
        """
        Dynamic initializer for Dialog.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Dialog__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Dialog__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Dialog.mouseRelease(int,int,int)"""
        return bool._wrap(super(_Dialog, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.mouseMove(int,int)"""
        super(_widget.UIContainer, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.UIContainer.getName()"""
        return str._wrap(super(widget.UIContainer, self).getName())

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
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'._wrap(super(_widget.UIContainer, self).getWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

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

    @override
    @overload
    def getPreferredSize(self) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'Size'._wrap(super(widget.Widget, self).getPreferredSize())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Dialog.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Dialog, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'._wrap(super(widget.UIContainer, self).getLayout())

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_widget.UIContainer, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.charType(char)"""
        return bool._wrap(super(_widget.UIContainer, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_widget.Widget, self).setPreferredX(_int.valueOf(arg0))

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
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Dialog.mousePress(int,int,int)"""
        return bool._wrap(super(_Dialog, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_widget.Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(widget.Widget, self).componentRegistry())

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.UIContainer.mouseWheel(int,int,double)"""
        return bool._wrap(super(_widget.UIContainer, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def bounds(self, arg0: 'Supplier') -> 'Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Dialog.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'Dialog'._wrap(super(_Dialog, self).bounds(arg0))

    @override
    @overload
    def getPreferredPos(self) -> 'Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'Position'._wrap(super(widget.Widget, self).getPreferredPos())

    @overload
    def close(self):
        """public void dev.ultreon.quantum.client.gui.Dialog.close()"""
        super(Dialog, self).close()

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Dialog.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_Dialog, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_widget.Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def position(self, arg0: 'Supplier') -> 'Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Dialog.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'Dialog'._wrap(super(_Dialog, self).position(arg0))

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

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(widget.Widget, self).getPreferredX())

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

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Dialog.keyPress(int)"""
        return bool._wrap(super(_Dialog, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def getBounds(self) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'Bounds'._wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_widget.Widget, self).setPreferredWidth(_int.valueOf(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Overlays
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client.gui import overlay
except ImportError:
    overlay = _import_once("pyquantum.client.gui.overlay")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.Overlays as _Overlays
_Overlays = _Overlays
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Overlays():
    """dev.ultreon.quantum.client.gui.Overlays"""
 
    @staticmethod
    def _wrap(java_value: _Overlays) -> 'Overlays':
        return Overlays(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Overlays):
        """
        Dynamic initializer for Overlays.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Overlays__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Overlays__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.gui.overlay.HotbarOverlay dev.ultreon.quantum.client.gui.Overlays.HOTBAR
    HOTBAR: 'overlay.HotbarOverlay' = _wrap(_overlay.HotbarOverlay.HOTBAR)

    # public static final dev.ultreon.quantum.client.gui.overlay.HealthOverlay dev.ultreon.quantum.client.gui.Overlays.HEALTH
    HEALTH: 'overlay.HealthOverlay' = _wrap(_overlay.HealthOverlay.HEALTH)

    # public static final dev.ultreon.quantum.client.gui.overlay.CrosshairOverlay dev.ultreon.quantum.client.gui.Overlays.CROSSHAIR
    CROSSHAIR: 'overlay.CrosshairOverlay' = _wrap(_overlay.CrosshairOverlay.CROSSHAIR)

    # public static final dev.ultreon.quantum.client.gui.overlay.ChatOverlay dev.ultreon.quantum.client.gui.Overlays.CHAT
    CHAT: 'overlay.ChatOverlay' = _wrap(_overlay.ChatOverlay.CHAT)

    # public static final dev.ultreon.quantum.client.gui.overlay.HungerOverlay dev.ultreon.quantum.client.gui.Overlays.HUNGER
    HUNGER: 'overlay.HungerOverlay' = _wrap(_overlay.HungerOverlay.HUNGER)

    # public static final dev.ultreon.quantum.client.gui.overlay.MemoryUsageOverlay dev.ultreon.quantum.client.gui.Overlays.MEMORY
    MEMORY: 'overlay.MemoryUsageOverlay' = _wrap(_overlay.MemoryUsageOverlay.MEMORY)


        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.client.gui.Overlays.init()"""
            _Overlays.init()

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
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.Overlays()"""
        val = _Overlays()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.Overlays()"""
        val = _Overlays()
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
 
 
# CLASS: dev.ultreon.quantum.client.gui.Notification
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.icon.Icon as _Icon
_Icon = _Icon
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pyquantum.client.gui import icon
except ImportError:
    icon = _import_once("pyquantum.client.gui.icon")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.Notification as _Notification_Builder
_Builder = _Notification_Builder.Builder
import dev.ultreon.quantum.text.MutableText as _MutableText
_MutableText = _MutableText
import dev.ultreon.quantum.client.gui.Notification as _Notification
_Notification = _Notification
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Notification():
    """dev.ultreon.quantum.client.gui.Notification"""
 
    @staticmethod
    def _wrap(java_value: _Notification) -> 'Notification':
        return Notification(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Notification):
        """
        Dynamic initializer for Notification.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Notification__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Notification__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getIcon(self) -> 'icon.Icon':
        """public dev.ultreon.quantum.client.gui.icon.Icon dev.ultreon.quantum.client.gui.Notification.getIcon()"""
        return 'icon.Icon'._wrap(super(Notification, self).getIcon())

    @overload
    def getMotion(self) -> float:
        """public float dev.ultreon.quantum.client.gui.Notification.getMotion()"""
        return float._wrap(super(Notification, self).getMotion())

    @overload
    def setSummary(self, arg0: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.Notification.setSummary(dev.ultreon.quantum.text.MutableText)"""
        super(_Notification, self).setSummary(arg0)

    @overload
    def getTitle(self) -> 'text.MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.client.gui.Notification.getTitle()"""
        return 'text.MutableText'._wrap(super(Notification, self).getTitle())

    @overload
    def close(self):
        """public void dev.ultreon.quantum.client.gui.Notification.close()"""
        super(Notification, self).close()

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
    def isFinished(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Notification.isFinished()"""
        return bool._wrap(super(Notification, self).isFinished())

    @overload
    def isSticky(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Notification.isSticky()"""
        return bool._wrap(super(Notification, self).isSticky())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setTitle(self, arg0: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.Notification.setTitle(dev.ultreon.quantum.text.MutableText)"""
        super(_Notification, self).setTitle(arg0)

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
    def getSummary(self) -> 'text.MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.client.gui.Notification.getSummary()"""
        return 'text.MutableText'._wrap(super(Notification, self).getSummary())

    @staticmethod
    @overload
    def builder(arg0: str, arg1: str) -> 'Builder':
        """public static dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification.builder(java.lang.String,java.lang.String)"""
        return Builder._wrap(_Notification.builder(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setIcon(self, arg0: 'Icon'):
        """public void dev.ultreon.quantum.client.gui.Notification.setIcon(dev.ultreon.quantum.client.gui.icon.Icon)"""
        super(_Notification, self).setIcon(arg0)

    @overload
    def set(self, arg0: 'MutableText', arg1: 'MutableText'):
        """public void dev.ultreon.quantum.client.gui.Notification.set(dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText)"""
        super(_Notification, self).set(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getSubText(self) -> 'text.MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.client.gui.Notification.getSubText()"""
        return 'text.MutableText'._wrap(super(Notification, self).getSubText())

    @staticmethod
    @overload
    def builder(arg0: 'MutableText', arg1: 'MutableText') -> 'Builder':
        """public static dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification.builder(dev.ultreon.quantum.text.MutableText,dev.ultreon.quantum.text.MutableText)"""
        return Builder._wrap(_Notification.builder(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Bounds
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.Position as _Position
_Position = _Position
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Bounds():
    """dev.ultreon.quantum.client.gui.Bounds"""
 
    @staticmethod
    def _wrap(java_value: _Bounds) -> 'Bounds':
        return Bounds(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Bounds):
        """
        Dynamic initializer for Bounds.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Bounds__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Bounds__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setSize(self, arg0: 'Size') -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setSize(dev.ultreon.quantum.client.gui.Size)"""
        return 'Bounds'._wrap(super(_Bounds, self).setSize(arg0))

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Bounds.getX()"""
        return int._wrap(super(Bounds, self).getX())

    @overload
    def setSize(self, arg0: int, arg1: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setSize(int,int)"""
        return 'Bounds'._wrap(super(_Bounds, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def setHeight(self, arg0: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setHeight(int)"""
        return 'Bounds'._wrap(super(_Bounds, self).setHeight(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setBounds(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setBounds(int,int,int,int)"""
        return 'Bounds'._wrap(super(_Bounds, self).setBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def __init__(self, arg0: 'Position', arg1: 'Size'):
        """public dev.ultreon.quantum.client.gui.Bounds(dev.ultreon.quantum.client.gui.Position,dev.ultreon.quantum.client.gui.Size)"""
        val = _Bounds(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def grow(self, arg0: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.grow(int)"""
        return 'Bounds'._wrap(super(_Bounds, self).grow(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Bounds.equals(java.lang.Object)"""
        return bool._wrap(super(_Bounds, self).equals(arg0))

    @overload
    def pos(self) -> 'Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.Bounds.pos()"""
        return 'Position'._wrap(super(Bounds, self).pos())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.Bounds(int,int,int,int)"""
        val = _Bounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @overload
    def shrink(self, arg0: int, arg1: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.shrink(int,int)"""
        return 'Bounds'._wrap(super(_Bounds, self).shrink(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Bounds.getWidth()"""
        return int._wrap(super(Bounds, self).getWidth())

    @overload
    def setBounds(self, arg0: 'Bounds') -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        return 'Bounds'._wrap(super(_Bounds, self).setBounds(arg0))

    @overload
    def shrink(self, arg0: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.shrink(int)"""
        return 'Bounds'._wrap(super(_Bounds, self).shrink(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Bounds.toString()"""
        return str._wrap(super(Bounds, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Bounds.hashCode()"""
        return int._wrap(super(Bounds, self).hashCode())

    @overload
    def setY(self, arg0: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setY(int)"""
        return 'Bounds'._wrap(super(_Bounds, self).setY(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setBounds(self, arg0: 'Position', arg1: int, arg2: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setBounds(dev.ultreon.quantum.client.gui.Position,int,int)"""
        return 'Bounds'._wrap(super(_Bounds, self).setBounds(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def contains(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Bounds.contains(int,int)"""
        return bool._wrap(super(_Bounds, self).contains(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Bounds.getHeight()"""
        return int._wrap(super(Bounds, self).getHeight())

    @overload
    def setWidth(self, arg0: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setWidth(int)"""
        return 'Bounds'._wrap(super(_Bounds, self).setWidth(_int.valueOf(arg0)))

    @override
    @overload
    def cpy(self) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.cpy()"""
        return 'Bounds'._wrap(super(Bounds, self).cpy())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.Bounds()"""
        val = _Bounds()
        self.__wrapper = val

    @overload
    def setX(self, arg0: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setX(int)"""
        return 'Bounds'._wrap(super(_Bounds, self).setX(_int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.Bounds()"""
        val = _Bounds()
        self.__wrapper = val

    @overload
    def shrink(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.shrink(int,int,int,int)"""
        return 'Bounds'._wrap(super(_Bounds, self).shrink(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def setPos(self, arg0: int, arg1: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setPos(int,int)"""
        return 'Bounds'._wrap(super(_Bounds, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def setBounds(self, arg0: int, arg1: int, arg2: 'Size') -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setBounds(int,int,dev.ultreon.quantum.client.gui.Size)"""
        return 'Bounds'._wrap(super(_Bounds, self).setBounds(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setBounds(self, arg0: 'Position', arg1: 'Size') -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setBounds(dev.ultreon.quantum.client.gui.Position,dev.ultreon.quantum.client.gui.Size)"""
        return 'Bounds'._wrap(super(_Bounds, self).setBounds(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setPos(self, arg0: 'Position') -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.setPos(dev.ultreon.quantum.client.gui.Position)"""
        return 'Bounds'._wrap(super(_Bounds, self).setPos(arg0))

    @overload
    def size(self) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.Bounds.size()"""
        return 'Size'._wrap(super(Bounds, self).size())

    @overload
    def grow(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.grow(int,int,int,int)"""
        return 'Bounds'._wrap(super(_Bounds, self).grow(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Bounds.getY()"""
        return int._wrap(super(Bounds, self).getY())

    @overload
    def grow(self, arg0: int, arg1: int) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.Bounds.grow(int,int)"""
        return 'Bounds'._wrap(super(_Bounds, self).grow(_int.valueOf(arg0), _int.valueOf(arg1))) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Fonts
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = _import_once("pyquantum.registry")

import dev.ultreon.quantum.client.gui.Fonts as _Fonts
_Fonts = _Fonts
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.registry.RegistryKey as _RegistryKey
_RegistryKey = _RegistryKey
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Fonts():
    """dev.ultreon.quantum.client.gui.Fonts"""
 
    @staticmethod
    def _wrap(java_value: _Fonts) -> 'Fonts':
        return Fonts(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Fonts):
        """
        Dynamic initializer for Fonts.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Fonts__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Fonts__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.Fonts()"""
        val = _Fonts()
        self.__wrapper = val

    @staticmethod
    @property
    def QUANTIUM_() -> RegistryKey:
        """
        Getter for the QUANTIUM property.
     
        :return: Value of QUANTIUM
        """
     
        return super(RegistryKey).QUANTIUM()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

        @staticmethod
        @overload
        def register():
            """public static void dev.ultreon.quantum.client.gui.Fonts.register()"""
            _Fonts.register()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.Fonts()"""
        val = _Fonts()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.LayoutBounds
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.LayoutBounds as _LayoutBounds
_LayoutBounds = _LayoutBounds
import java.util.function.IntSupplier as IntSupplier
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LayoutBounds():
    """dev.ultreon.quantum.client.gui.LayoutBounds"""
 
    @staticmethod
    def _wrap(java_value: _LayoutBounds) -> 'LayoutBounds':
        return LayoutBounds(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LayoutBounds):
        """
        Dynamic initializer for LayoutBounds.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LayoutBounds__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LayoutBounds__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def currentHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.LayoutBounds.currentHeight()"""
        return int._wrap(super(LayoutBounds, self).currentHeight())

    @overload
    def currentBounds(self) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.LayoutBounds.currentBounds()"""
        return 'Bounds'._wrap(super(LayoutBounds, self).currentBounds())

    @overload
    def setCurrentX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.setCurrentX(int)"""
        super(_LayoutBounds, self).setCurrentX(_int.valueOf(arg0))

    @overload
    def setCurrentWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.setCurrentWidth(int)"""
        super(_LayoutBounds, self).setCurrentWidth(_int.valueOf(arg0))

    @overload
    def setCurrentBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.setCurrentBounds(int,int,int,int)"""
        super(_LayoutBounds, self).setCurrentBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def currentWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.LayoutBounds.currentWidth()"""
        return int._wrap(super(LayoutBounds, self).currentWidth())

    @overload
    def currentX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.LayoutBounds.currentX()"""
        return int._wrap(super(LayoutBounds, self).currentX())

    @overload
    def setCurrentHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.setCurrentHeight(int)"""
        super(_LayoutBounds, self).setCurrentHeight(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.revalidate()"""
        super(LayoutBounds, self).revalidate()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setCurrentBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.setCurrentBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_LayoutBounds, self).setCurrentBounds(arg0)

    @overload
    def currentY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.LayoutBounds.currentY()"""
        return int._wrap(super(LayoutBounds, self).currentY())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'IntSupplier', arg1: 'IntSupplier', arg2: 'IntSupplier', arg3: 'IntSupplier'):
        """public dev.ultreon.quantum.client.gui.LayoutBounds(java.util.function.IntSupplier,java.util.function.IntSupplier,java.util.function.IntSupplier,java.util.function.IntSupplier)"""
        val = _LayoutBounds(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.LayoutBounds.equals(java.lang.Object)"""
        return bool._wrap(super(_LayoutBounds, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.LayoutBounds.toString()"""
        return str._wrap(super(LayoutBounds, self).toString())

    @overload
    def setCurrentY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.LayoutBounds.setCurrentY(int)"""
        super(_LayoutBounds, self).setCurrentY(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.LayoutBounds.hashCode()"""
        return int._wrap(super(LayoutBounds, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Renderer
from pyquantum_helper import import_once as _import_once
import java.lang.Double as _double
import dev.ultreon.quantum.client.gui.Renderer as _Renderer
_Renderer = _Renderer
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.client.gui.Matrices as _Matrices
_Matrices = _Matrices
import java.awt.geom.Rectangle2D as Rectangle2D
import com.badlogic.gdx.graphics.g3d.Renderable as _Renderable
_Renderable = _Renderable
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.awt.geom.Line2D as Line2D
import java.util.function.Consumer as Consumer
try:
    import pyshapedrawer
except ImportError:
    pyshapedrawer = _import_once("pyshapedrawer")

import java.lang.String as _string
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.font.Font as _Font
_Font = _Font
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
import com.badlogic.gdx.graphics.g2d.Batch as _Batch
_Batch = _Batch
from pyquantum_helper import override
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
import java.lang.Runnable as Runnable
from builtins import float
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
import java.awt.geom.Ellipse2D as Ellipse2D
import dev.ultreon.quantum.util.Color as _Color
_Color = _Color
import java.lang.Integer as _int
try:
    from pyquantum.client import font
except ImportError:
    font = _import_once("pyquantum.client.font")

try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Renderer():
    """dev.ultreon.quantum.client.gui.Renderer"""
 
    @staticmethod
    def _wrap(java_value: _Renderer) -> 'Renderer':
        return Renderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Renderer):
        """
        Dynamic initializer for Renderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Renderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Renderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'List', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def fill(self, arg0: 'Vec4i') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.fill(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Renderer'._wrap(super(_Renderer, self).fill(arg0))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: bool, arg5: float, arg6: bool, arg7: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean,float,boolean,java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4), _float.valueOf(arg5), _boolean.valueOf(arg6), arg7))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4))

    @overload
    def textMultiline(self, arg0: str, arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textMultiline(java.lang.String,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textMultiline(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'ColorCode', arg4: float, arg5: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.text.ColorCode,float,java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _float.valueOf(arg4), arg5))

    @overload
    def fill(self, arg0: 'Rectangle2D') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.fill(java.awt.geom.Rectangle2D)"""
        return 'Renderer'._wrap(super(_Renderer, self).fill(arg0))

    @overload
    def translate(self, arg0: float, arg1: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.translate(float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).translate(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4)))

    @overload
    def draw9PatchTexture(self, arg0: 'Texture', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.draw9PatchTexture(com.badlogic.gdx.graphics.Texture,int,int,int,int,int,int,int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).draw9PatchTexture(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10)))

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def drawSprite(self, arg0: 'Sprite', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.drawSprite(dev.ultreon.quantum.client.gui.Sprite,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).drawSprite(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _boolean.valueOf(arg5)))

    @overload
    def textCenter(self, arg0: 'List', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: bool, arg4: float, arg5: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,boolean,float,java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3), _float.valueOf(arg4), arg5))

    @overload
    def box(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.box(int,int,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).box(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @overload
    def renderFrame(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.renderFrame(int,int,int,int)"""
        super(_Renderer, self).renderFrame(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: bool, arg4: float, arg5: bool, arg6: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,boolean,float,boolean,java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3), _float.valueOf(arg4), _boolean.valueOf(arg5), arg6))

    @overload
    def pushScissors(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Renderer.pushScissors(int,int,int,int)"""
        return bool._wrap(super(_Renderer, self).pushScissors(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def popMatrix(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.popMatrix()"""
        return 'Renderer'._wrap(super(Renderer, self).popMatrix())

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4))

    @overload
    def drawSprite(self, arg0: 'Sprite', arg1: int, arg2: int, arg3: int, arg4: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.drawSprite(dev.ultreon.quantum.client.gui.Sprite,int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).drawSprite(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: 'List', arg1: int, arg2: int, arg3: 'ColorCode', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.text.ColorCode,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), arg7))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def textRight(self, arg0: str, arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.line(float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4))

    @overload
    def scale(self, arg0: float, arg1: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.scale(double,double)"""
        return 'Renderer'._wrap(super(_Renderer, self).scale(_double.valueOf(arg0), _double.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def blurred(self, arg0: float, arg1: float, arg2: bool, arg3: int, arg4: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(float,float,boolean,int,java.lang.Runnable)"""
        super(_Renderer, self).blurred(_float.valueOf(arg0), _float.valueOf(arg1), _boolean.valueOf(arg2), _int.valueOf(arg3), arg4)

    @overload
    def clearColor(self, arg0: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(int)"""
        return 'Renderer'._wrap(super(_Renderer, self).clearColor(_int.valueOf(arg0)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'ColorCode', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.text.ColorCode,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4)))

    @overload
    def rect3DLine(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rect3DLine(int,int,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).rect3DLine(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: 'List', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: int, arg3: int, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _boolean.valueOf(arg5)))

    @overload
    def textMultiline(self, arg0: str, arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textMultiline(java.lang.String,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textMultiline(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def getFont(self) -> 'font.Font':
        """public dev.ultreon.quantum.client.font.Font dev.ultreon.quantum.client.gui.Renderer.getFont()"""
        return 'font.Font'._wrap(super(Renderer, self).getFont())

    @overload
    def textLeft(self, arg0: str, arg1: int, arg2: int, arg3: 'ColorCode', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,int,int,dev.ultreon.quantum.text.ColorCode,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def pushMatrix(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.pushMatrix()"""
        return 'Renderer'._wrap(super(Renderer, self).pushMatrix())

    @overload
    def textCenter(self, arg0: 'List', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6)))

    @overload
    def renderPopoutFrame(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.renderPopoutFrame(int,int,int,int)"""
        super(_Renderer, self).renderPopoutFrame(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: str, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def textRight(self, arg0: 'List', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.line(float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5)))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5)))

    @overload
    def textRight(self, arg0: str, arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def textCenter(self, arg0: str, arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def clearColor(self, arg0: int, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).clearColor(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'ShapeDrawer'):
        """public dev.ultreon.quantum.client.gui.Renderer(space.earlygrey.shapedrawer.ShapeDrawer)"""
        val = _Renderer(arg0)
        self.__wrapper = val

    @overload
    def oval(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.oval(int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).oval(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def blurred(self, arg0: 'Texture'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(com.badlogic.gdx.graphics.Texture)"""
        super(_Renderer, self).blurred(arg0)

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4)))

    @overload
    def setColor(self, arg0: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).setColor(arg0))

    @overload
    def textLeft(self, arg0: 'List', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def scissorOffset(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.scissorOffset(int,int)"""
        super(_Renderer, self).scissorOffset(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def finish(self):
        """public void dev.ultreon.quantum.client.gui.Renderer.finish()"""
        super(Renderer, self).finish()

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6)))

    @overload
    def outline(self, arg0: 'Ellipse2D') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.outline(java.awt.geom.Ellipse2D)"""
        return 'Renderer'._wrap(super(_Renderer, self).outline(arg0))

    @overload
    def clearColor(self, arg0: float, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).clearColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Renderer.toString()"""
        return str._wrap(super(Renderer, self).toString())

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
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def clearColor(self, arg0: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).clearColor(arg0))

    @overload
    def getGlobalTranslation(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.gui.Renderer.getGlobalTranslation()"""
        return 'math.Vector3'._wrap(super(Renderer, self).getGlobalTranslation())

    @overload
    def blit(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def end(self):
        """public void dev.ultreon.quantum.client.gui.Renderer.end()"""
        super(Renderer, self).end()

    @overload
    def draw9Slice(self, arg0: 'Texture', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.draw9Slice(com.badlogic.gdx.graphics.Texture,int,int,int,int,int,int,int,int,int,int,int)"""
        super(_Renderer, self).draw9Slice(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11))

    @overload
    def textRight(self, arg0: 'List', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @overload
    def textCenter(self, arg0: 'List', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8)))

    @overload
    def model(self, arg0: 'Runnable') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.model(java.lang.Runnable)"""
        return 'Renderer'._wrap(super(_Renderer, self).model(arg0))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5))

    @overload
    def textLeft(self, arg0: 'List', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def clearColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).clearColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def roundRect(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.roundRect(int,int,int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).roundRect(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @overload
    def draw9PatchTexture(self, arg0: 'Identifier', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.draw9PatchTexture(dev.ultreon.quantum.util.Identifier,int,int,int,int,int,int,int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).draw9PatchTexture(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10)))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), arg11))

    @overload
    def renderFrame(self, arg0: 'Identifier', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'Color'):
        """public void dev.ultreon.quantum.client.gui.Renderer.renderFrame(dev.ultreon.quantum.util.Identifier,int,int,int,int,int,int,int,int,int,int,dev.ultreon.quantum.util.Color)"""
        super(_Renderer, self).renderFrame(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), arg11)

    @overload
    def textLeft(self, arg0: str, arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: bool, arg5: float, arg6: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean,float,java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4), _float.valueOf(arg5), arg6))

    @overload
    def getColor(self) -> 'util.Color':
        """public dev.ultreon.quantum.util.Color dev.ultreon.quantum.client.gui.Renderer.getColor()"""
        return 'util.Color'._wrap(super(Renderer, self).getColor())

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'ColorCode', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.text.ColorCode,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def actuallyEnd(self):
        """public void dev.ultreon.quantum.client.gui.Renderer.actuallyEnd()"""
        super(Renderer, self).actuallyEnd()

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: float, arg5: bool, arg6: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.util.Color,float,boolean,java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _float.valueOf(arg4), _boolean.valueOf(arg5), arg6))

    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch dev.ultreon.quantum.client.gui.Renderer.getBatch()"""
        return 'g2d.Batch'._wrap(super(Renderer, self).getBatch())

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setBlitColor(self, arg0: 'Color'):
        """public void dev.ultreon.quantum.client.gui.Renderer.setBlitColor(dev.ultreon.quantum.util.Color)"""
        super(_Renderer, self).setBlitColor(arg0)

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,float,float,float,float,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), arg11))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5)))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def pushScissors(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Renderer.pushScissors(float,float,float,float)"""
        return bool._wrap(super(_Renderer, self).pushScissors(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def blitColor(self, arg0: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blitColor(dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).blitColor(arg0))

    @overload
    def fill(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.fill(int,int,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).fill(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @overload
    def textLeft(self, arg0: 'List', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def rect(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rect(float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).rect(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def textRight(self, arg0: 'List', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def line(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.line(int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).line(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def isBlurred(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Renderer.isBlurred()"""
        return bool._wrap(super(Renderer, self).isBlurred())

    @overload
    def flush(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.flush()"""
        return 'Renderer'._wrap(super(Renderer, self).flush())

    @overload
    def textTabbed(self, arg0: str, arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textTabbed(java.lang.String,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textTabbed(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def textTabbed(self, arg0: str, arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textTabbed(java.lang.String,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textTabbed(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def blurred(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(java.lang.Runnable)"""
        super(_Renderer, self).blurred(arg0)

    @overload
    def blurred(self, arg0: bool, arg1: int, arg2: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(boolean,int,java.lang.Runnable)"""
        super(_Renderer, self).blurred(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def blurred(self, arg0: float, arg1: bool, arg2: int, arg3: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(float,boolean,int,java.lang.Runnable)"""
        super(_Renderer, self).blurred(_float.valueOf(arg0), _boolean.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def blurred(self, arg0: float, arg1: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(float,java.lang.Runnable)"""
        super(_Renderer, self).blurred(_float.valueOf(arg0), arg1)

    @overload
    def ovalLine(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.ovalLine(int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).ovalLine(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4)))

    @overload
    def clearScissors(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearScissors()"""
        return 'Renderer'._wrap(super(Renderer, self).clearScissors())

    @overload
    def textRight(self, arg0: 'TextObject', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def rectLine(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rectLine(int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).rectLine(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def outline(self, arg0: 'Rectangle2D') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.outline(java.awt.geom.Rectangle2D)"""
        return 'Renderer'._wrap(super(_Renderer, self).outline(arg0))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: int, arg3: int, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _boolean.valueOf(arg5)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def popScissors(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle dev.ultreon.quantum.client.gui.Renderer.popScissors()"""
        return 'math.Rectangle'._wrap(super(Renderer, self).popScissors())

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: int, arg3: int, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4)))

    @overload
    def blurred(self, arg0: bool, arg1: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(boolean,java.lang.Runnable)"""
        super(_Renderer, self).blurred(_boolean.valueOf(arg0), arg1)

    @overload
    def clearColor(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).clearColor(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'ColorCode', arg4: float, arg5: bool, arg6: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.text.ColorCode,float,boolean,java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _float.valueOf(arg4), _boolean.valueOf(arg5), arg6))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), arg9))

    @overload
    def oval(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.oval(float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).oval(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'ColorCode', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.text.ColorCode,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def getStrokeWidth(self) -> float:
        """public float dev.ultreon.quantum.client.gui.Renderer.getStrokeWidth()"""
        return float._wrap(super(Renderer, self).getStrokeWidth())

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def rect3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rect3D(int,int,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).rect3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'List', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def textCenter(self, arg0: str, arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: str, arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def polygon(self, arg0: 'float', arg1: 'Color', arg2: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.polygon(float[],dev.ultreon.quantum.util.Color,int)"""
        super(_Renderer, self).polygon(arg0, arg1, _int.valueOf(arg2))

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4))

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'List', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def renderFrame(self, arg0: 'Identifier', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.renderFrame(dev.ultreon.quantum.util.Identifier,int,int,int,int,int,int,int,int,int,int)"""
        super(_Renderer, self).renderFrame(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def textRight(self, arg0: 'List', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5)))

    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Renderer.getWidth()"""
        return int._wrap(super(Renderer, self).getWidth())

    @overload
    def rotate(self, arg0: float, arg1: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rotate(double,double)"""
        return 'Renderer'._wrap(super(_Renderer, self).rotate(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def setStrokeWidth(self, arg0: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setStrokeWidth(float)"""
        return 'Renderer'._wrap(super(_Renderer, self).setStrokeWidth(_float.valueOf(arg0)))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def circleLine(self, arg0: float, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.circleLine(float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).circleLine(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def external(self, arg0: 'Runnable') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.external(java.lang.Runnable)"""
        return 'Renderer'._wrap(super(_Renderer, self).external(arg0))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), arg7))

    @overload
    def __init__(self, arg0: 'ShapeDrawer', arg1: 'Matrices'):
        """public dev.ultreon.quantum.client.gui.Renderer(space.earlygrey.shapedrawer.ShapeDrawer,dev.ultreon.quantum.client.gui.Matrices)"""
        val = _Renderer(arg0, arg1)
        self.__wrapper = val

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: int, arg3: int, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4)))

    @overload
    def textMultiline(self, arg0: str, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textMultiline(java.lang.String,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textMultiline(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'ColorCode') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.text.ColorCode)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textRight(self, arg0: 'List', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def textLeft(self, arg0: str, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), arg9))

    @overload
    def textLeft(self, arg0: 'List', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'ColorCode') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.text.ColorCode)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5)))

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def textTabbed(self, arg0: str, arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textTabbed(java.lang.String,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textTabbed(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def arc(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.arc(int,int,int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).arc(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,float,java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4))

    @overload
    def textLeft(self, arg0: 'List', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def clear(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clear()"""
        return 'Renderer'._wrap(super(Renderer, self).clear())

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setColor(self, arg0: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(int)"""
        return 'Renderer'._wrap(super(_Renderer, self).setColor(_int.valueOf(arg0)))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def obtainRenderable(self) -> 'g3d.Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable dev.ultreon.quantum.client.gui.Renderer.obtainRenderable()"""
        return 'g3d.Renderable'._wrap(super(Renderer, self).obtainRenderable())

    @overload
    def setColor(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).setColor(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def font(self, arg0: 'Font') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.font(dev.ultreon.quantum.client.font.Font)"""
        return 'Renderer'._wrap(super(_Renderer, self).font(arg0))

    @overload
    def draw9Slice(self, arg0: 'Identifier', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.draw9Slice(dev.ultreon.quantum.util.Identifier,int,int,int,int,int,int,int,int,int,int,int)"""
        super(_Renderer, self).draw9Slice(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'ColorCode') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.text.ColorCode)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def rect(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rect(int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).rect(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def invertOff(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.invertOff()"""
        return 'Renderer'._wrap(super(Renderer, self).invertOff())

    @overload
    def rectLine(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.rectLine(float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).rectLine(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Renderer.getHeight()"""
        return int._wrap(super(Renderer, self).getHeight())

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: float, arg5: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.util.Color,float,java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _float.valueOf(arg4), arg5))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: int, arg3: int, arg4: 'Color', arg5: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _boolean.valueOf(arg5)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: int, arg3: int, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4)))

    @overload
    def setColor(self, arg0: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).setColor(arg0))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def fill(self, arg0: 'Line2D') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.fill(java.awt.geom.Line2D)"""
        return 'Renderer'._wrap(super(_Renderer, self).fill(arg0))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def textCenter(self, arg0: 'List', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: bool, arg5: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,float,boolean,java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4), arg5))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'ColorCode', arg4: bool, arg5: float, arg6: bool, arg7: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.text.ColorCode,boolean,float,boolean,java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4), _float.valueOf(arg5), _boolean.valueOf(arg6), arg7))

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def textRight(self, arg0: str, arg1: float, arg2: float, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def arcLine(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.arcLine(int,int,int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).arcLine(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5))

    @overload
    def textRight(self, arg0: 'List', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textCenter(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.TextObject,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4))

    @overload
    def clearColor(self, arg0: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.clearColor(java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).clearColor(arg0))

    @overload
    def getMatrices(self) -> 'Matrices':
        """public dev.ultreon.quantum.client.gui.Matrices dev.ultreon.quantum.client.gui.Renderer.getMatrices()"""
        return 'Matrices'._wrap(super(Renderer, self).getMatrices())

    @overload
    def translate(self, arg0: int, arg1: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.translate(int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).translate(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getBlitColor(self) -> 'util.Color':
        """public dev.ultreon.quantum.util.Color dev.ultreon.quantum.client.gui.Renderer.getBlitColor()"""
        return 'util.Color'._wrap(super(Renderer, self).getBlitColor())

    @overload
    def setColor(self, arg0: int, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setColor(int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).setColor(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def blit(self, arg0: 'TextureRegion', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def textRight(self, arg0: 'FormattedText', arg1: int, arg2: int, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.FormattedText,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def textCenter(self, arg0: str, arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def pushScissors(self, arg0: 'Bounds') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Renderer.pushScissors(dev.ultreon.quantum.client.gui.Bounds)"""
        return bool._wrap(super(_Renderer, self).pushScissors(arg0))

    @overload
    def unsetShader(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.unsetShader()"""
        return 'Renderer'._wrap(super(Renderer, self).unsetShader())

    @overload
    def textLeft(self, arg0: 'List', arg1: int, arg2: int, arg3: 'ColorCode') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.text.ColorCode)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def textLeft(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def textCenter(self, arg0: 'List', arg1: float, arg2: float, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def invertOn(self) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.invertOn()"""
        return 'Renderer'._wrap(super(Renderer, self).invertOn())

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def textRight(self, arg0: 'List', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def blurred(self, arg0: float, arg1: bool, arg2: 'Runnable'):
        """public void dev.ultreon.quantum.client.gui.Renderer.blurred(float,boolean,java.lang.Runnable)"""
        super(_Renderer, self).blurred(_float.valueOf(arg0), _boolean.valueOf(arg1), arg2)

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def drawRegion(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'Consumer') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.drawRegion(int,int,int,int,java.util.function.Consumer<dev.ultreon.quantum.client.gui.Renderer>)"""
        return 'Renderer'._wrap(super(_Renderer, self).drawRegion(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: float, arg3: 'ColorCode', arg4: bool, arg5: float, arg6: str) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,float,dev.ultreon.quantum.text.ColorCode,boolean,float,java.lang.String)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4), _float.valueOf(arg5), arg6))

    @overload
    def textCenter(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.lang.String,float,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4)))

    @overload
    def setShader(self, arg0: 'ShaderProgram') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        return 'Renderer'._wrap(super(_Renderer, self).setShader(arg0))

    @overload
    def textCenter(self, arg0: 'FormattedText', arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(dev.ultreon.quantum.text.FormattedText,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def textTabbed(self, arg0: str, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textTabbed(java.lang.String,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textTabbed(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def translate(self, arg0: int, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.translate(int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).translate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def blit(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10)))

    @overload
    def textLeft(self, arg0: str, arg1: float, arg2: int, arg3: int, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,float,int,int,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @overload
    def textCenter(self, arg0: 'List', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textCenter(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textCenter(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def outline(self, arg0: 'Line2D') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.outline(java.awt.geom.Line2D)"""
        return 'Renderer'._wrap(super(_Renderer, self).outline(arg0))

    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Renderer.resize(int,int)"""
        super(_Renderer, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.translate(float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).translate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def fill(self, arg0: 'Ellipse2D') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.fill(java.awt.geom.Ellipse2D)"""
        return 'Renderer'._wrap(super(_Renderer, self).fill(arg0))

    @overload
    def textLeft(self, arg0: str, arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def getTransform(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.gui.Renderer.getTransform()"""
        return 'math.Matrix4'._wrap(super(Renderer, self).getTransform())

    @overload
    def ovalLine(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.ovalLine(float,float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).ovalLine(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.circle(float,float,float)"""
        return 'Renderer'._wrap(super(_Renderer, self).circle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def textLeft(self, arg0: 'List', arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.util.List<dev.ultreon.quantum.text.FormattedText>,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def blit(self, arg0: 'Identifier', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.blit(dev.ultreon.quantum.util.Identifier,float,float,float,float,float,float,float,float,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).blit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10)))

    @overload
    def textRight(self, arg0: str, arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,float,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: int, arg2: int, arg3: 'Color', arg4: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,int,int,dev.ultreon.quantum.util.Color,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4)))

    @overload
    def textRight(self, arg0: 'TextObject', arg1: float, arg2: float, arg3: float, arg4: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(dev.ultreon.quantum.text.TextObject,float,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4))

    @overload
    def pushScissorsRaw(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Renderer.pushScissorsRaw(int,int,int,int)"""
        return bool._wrap(super(_Renderer, self).pushScissorsRaw(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def pushScissors(self, arg0: 'Rectangle') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Renderer.pushScissors(com.badlogic.gdx.math.Rectangle)"""
        return bool._wrap(super(_Renderer, self).pushScissors(arg0))

    @overload
    def resetGrid(self):
        """public void dev.ultreon.quantum.client.gui.Renderer.resetGrid()"""
        super(Renderer, self).resetGrid()

    @overload
    def textRight(self, arg0: 'List', arg1: float, arg2: float, arg3: 'Color') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def textMultiline(self, arg0: str, arg1: int, arg2: int, arg3: bool) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textMultiline(java.lang.String,int,int,boolean)"""
        return 'Renderer'._wrap(super(_Renderer, self).textMultiline(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def textLeft(self, arg0: str, arg1: int, arg2: int, arg3: 'ColorCode') -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textLeft(java.lang.String,int,int,dev.ultreon.quantum.text.ColorCode)"""
        return 'Renderer'._wrap(super(_Renderer, self).textLeft(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def textRight(self, arg0: str, arg1: int, arg2: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.textRight(java.lang.String,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).textRight(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def roundRectLine(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> 'Renderer':
        """public dev.ultreon.quantum.client.gui.Renderer dev.ultreon.quantum.client.gui.Renderer.roundRectLine(int,int,int,int,int,int)"""
        return 'Renderer'._wrap(super(_Renderer, self).roundRectLine(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Position
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.gui.Position as _Position
_Position = _Position
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Position():
    """dev.ultreon.quantum.client.gui.Position"""
 
    @staticmethod
    def _wrap(java_value: _Position) -> 'Position':
        return Position(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Position):
        """
        Dynamic initializer for Position.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Position__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Position__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.Position.set(dev.ultreon.quantum.client.gui.Position)"""
        super(_Position, self).set(arg0)

    @overload
    def idt(self):
        """public void dev.ultreon.quantum.client.gui.Position.idt()"""
        super(Position, self).idt()

    @overload
    def set(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Position.set(int,int)"""
        super(_Position, self).set(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Position.equals(java.lang.Object)"""
        return bool._wrap(super(_Position, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Position.toString()"""
        return str._wrap(super(Position, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.Position()"""
        val = _Position()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.Position(int)"""
        val = _Position(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.gui.Position(int,int)"""
        val = _Position(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def cpy(self) -> 'Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.Position.cpy()"""
        return 'Position'._wrap(super(Position, self).cpy())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.Position()"""
        val = _Position()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Position.hashCode()"""
        return int._wrap(super(Position, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Callback
import java.lang.Object as _object
import dev.ultreon.quantum.client.gui.Callback as _Callback
_Callback = _Callback
from abc import abstractmethod, ABC
 
class Callback():
    """dev.ultreon.quantum.client.gui.Callback"""
 
    @staticmethod
    def _wrap(java_value: _Callback) -> 'Callback':
        return Callback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Callback):
        """
        Dynamic initializer for Callback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Callback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Callback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def call(self, arg0: object):
        """public abstract void dev.ultreon.quantum.client.gui.Callback.call(T)"""
        pass

    @overload
    def call0(self, arg0: object):
        """public default void dev.ultreon.quantum.client.gui.Callback.call0(java.lang.Object)"""
        super(_Callback, self).call0(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.TitleWidget
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

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
import dev.ultreon.quantum.client.gui.TitleWidget as _TitleWidget
_TitleWidget = _TitleWidget
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
 
class TitleWidget():
    """dev.ultreon.quantum.client.gui.TitleWidget"""
 
    @staticmethod
    def _wrap(java_value: _TitleWidget) -> 'TitleWidget':
        return TitleWidget(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TitleWidget):
        """
        Dynamic initializer for TitleWidget.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TitleWidget__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TitleWidget__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getScreen(self) -> 'Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.TitleWidget.getScreen()"""
        return 'Screen'._wrap(super(TitleWidget, self).getScreen())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyPress(int)"""
        return bool._wrap(super(_widget.Widget, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(widget.Widget, self).isHovered())

    @overload
    def getParent(self) -> 'Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.TitleWidget.getParent()"""
        return 'Screen'._wrap(super(TitleWidget, self).getParent())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_widget.Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def position(self, arg0: 'Supplier') -> 'TitleWidget':
        """public dev.ultreon.quantum.client.gui.TitleWidget dev.ultreon.quantum.client.gui.TitleWidget.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'TitleWidget'._wrap(super(_TitleWidget, self).position(arg0))

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
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.widget.Widget.path()"""
        return 'Path'._wrap(super(widget.Widget, self).path())

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.keyRelease(int)"""
        return bool._wrap(super(_widget.Widget, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(widget.Widget, self).getPreferredHeight())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.TitleWidget.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.Widget'._wrap(super(_TitleWidget, self).bounds(arg0))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_widget.Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.TitleWidget.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_TitleWidget, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.revalidate()"""
        super(widget.Widget, self).revalidate()

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
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseWheel(int,int,double)"""
        return bool._wrap(super(_widget.Widget, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

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
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(widget.Widget, self).getX())

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

    @override
    @overload
    def getPreferredSize(self) -> 'Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'Size'._wrap(super(widget.Widget, self).getPreferredSize())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.mouseMove(int,int)"""
        super(_widget.Widget, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_widget.Widget, self).setPreferredX(_int.valueOf(arg0))

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

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_widget.Widget, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.charType(char)"""
        return bool._wrap(super(_widget.Widget, self).charType(_char.valueOf(arg0)))

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.Widget.getName()"""
        return str._wrap(super(widget.Widget, self).getName())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_widget.Widget, self).setVisible(_boolean.valueOf(arg0))

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.TitleWidget.mouseRelease(int,int,int)"""
        return bool._wrap(super(_TitleWidget, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def getPreferredPos(self) -> 'Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'Position'._wrap(super(widget.Widget, self).getPreferredPos())

    @overload
    def __init__(self, arg0: 'Screen', arg1: 'TextObject'):
        """public dev.ultreon.quantum.client.gui.TitleWidget(dev.ultreon.quantum.client.gui.Screen,dev.ultreon.quantum.text.TextObject)"""
        val = _TitleWidget(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(widget.Widget, self).getPreferredWidth())

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_widget.Widget, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_widget.Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_widget.Widget, self).withComponent(arg0, arg1, arg2)

    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.TitleWidget.getTitle()"""
        return 'text.TextObject'._wrap(super(TitleWidget, self).getTitle())

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
    def parent(self, arg0: 'Screen'):
        """public void dev.ultreon.quantum.client.gui.TitleWidget.parent(dev.ultreon.quantum.client.gui.Screen)"""
        super(_TitleWidget, self).parent(arg0)

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(widget.Widget, self).getPreferredX())

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

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.TitleWidget.mousePress(int,int,int)"""
        return bool._wrap(super(_TitleWidget, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def getBounds(self) -> 'Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'Bounds'._wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_widget.Widget, self).setPreferredWidth(_int.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.DialogBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import dev.ultreon.quantum.client.gui.DialogBuilder as _DialogBuilder
_DialogBuilder = _DialogBuilder
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DialogBuilder():
    """dev.ultreon.quantum.client.gui.DialogBuilder"""
 
    @staticmethod
    def _wrap(java_value: _DialogBuilder) -> 'DialogBuilder':
        return DialogBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DialogBuilder):
        """
        Dynamic initializer for DialogBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DialogBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DialogBuilder__wrapper":
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

    @overload
    def __init__(self, arg0: 'Screen'):
        """public dev.ultreon.quantum.client.gui.DialogBuilder(dev.ultreon.quantum.client.gui.Screen)"""
        val = _DialogBuilder(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def message(self, arg0: 'TextObject') -> 'DialogBuilder':
        """public dev.ultreon.quantum.client.gui.DialogBuilder dev.ultreon.quantum.client.gui.DialogBuilder.message(dev.ultreon.quantum.text.TextObject)"""
        return 'DialogBuilder'._wrap(super(_DialogBuilder, self).message(arg0))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def title(self, arg0: 'TextObject') -> 'DialogBuilder':
        """public dev.ultreon.quantum.client.gui.DialogBuilder dev.ultreon.quantum.client.gui.DialogBuilder.title(dev.ultreon.quantum.text.TextObject)"""
        return 'DialogBuilder'._wrap(super(_DialogBuilder, self).title(arg0))

    @overload
    def button(self, arg0: 'TextObject', arg1: 'Runnable') -> 'DialogBuilder':
        """public dev.ultreon.quantum.client.gui.DialogBuilder dev.ultreon.quantum.client.gui.DialogBuilder.button(dev.ultreon.quantum.text.TextObject,java.lang.Runnable)"""
        return 'DialogBuilder'._wrap(super(_DialogBuilder, self).button(arg0, arg1))

    @overload
    def button(self, arg0: 'TextObject', arg1: 'Callback') -> 'DialogBuilder':
        """public dev.ultreon.quantum.client.gui.DialogBuilder dev.ultreon.quantum.client.gui.DialogBuilder.button(dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.client.gui.Dialog>)"""
        return 'DialogBuilder'._wrap(super(_DialogBuilder, self).button(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Sprite
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.gui.Sprite as _Sprite
_Sprite = _Sprite
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Sprite():
    """dev.ultreon.quantum.client.gui.Sprite"""
 
    @staticmethod
    def _wrap(java_value: _Sprite) -> 'Sprite':
        return Sprite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Sprite):
        """
        Dynamic initializer for Sprite.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Sprite__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Sprite__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Sprite.getHeight()"""
        return int._wrap(super(Sprite, self).getHeight())

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
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: int, arg4: int):
        """public void dev.ultreon.quantum.client.gui.Sprite.render(dev.ultreon.quantum.client.gui.Renderer,int,int,int,int)"""
        super(_Sprite, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

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

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.client.gui.Sprite(dev.ultreon.quantum.util.Identifier)"""
        val = _Sprite(arg0)
        self.__wrapper = val

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
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.Sprite.getWidth()"""
        return int._wrap(super(Sprite, self).getWidth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Alignment
import dev.ultreon.quantum.client.gui.Alignment as _Alignment
_Alignment = _Alignment
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
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Alignment():
    """dev.ultreon.quantum.client.gui.Alignment"""
 
    @staticmethod
    def _wrap(java_value: _Alignment) -> 'Alignment':
        return Alignment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Alignment):
        """
        Dynamic initializer for Alignment.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Alignment__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Alignment__wrapper":
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
    def valueOf(arg0: str) -> 'Alignment':
        """public static dev.ultreon.quantum.client.gui.Alignment dev.ultreon.quantum.client.gui.Alignment.valueOf(java.lang.String)"""
        return Alignment._wrap(_Alignment.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['Alignment']:
        """public static dev.ultreon.quantum.client.gui.Alignment[] dev.ultreon.quantum.client.gui.Alignment.values()"""
        return List[Alignment]._wrap(_Alignment.values())

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


Alignment.CENTER = Alignment._wrap(_CENTER.CENTER)

Alignment.RIGHT = Alignment._wrap(_RIGHT.RIGHT)

Alignment.LEFT = Alignment._wrap(_LEFT.LEFT) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.Notification$Builder
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.icon.Icon as _Icon
_Icon = _Icon
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client.gui import icon
except ImportError:
    icon = _import_once("pyquantum.client.gui.icon")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.Notification as _Notification_Builder
_Builder = _Notification_Builder.Builder
try:
    from pycorelibs.datetime import v0
except ImportError:
    v0 = _import_once("pycorelibs.datetime.v0")

import dev.ultreon.quantum.client.gui.Notification as _Notification
_Notification = _Notification
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """dev.ultreon.quantum.client.gui.Notification.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @property
    def icon(self) -> Icon:
        return Icon._wrap(super(_Builder).icon())

    @overload
    def sticky(self) -> 'Builder':
        """public dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification$Builder.sticky()"""
        return 'Builder'._wrap(super(Builder, self).sticky())

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
    def icon(self, arg0: 'Icon') -> 'Builder':
        """public dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification$Builder.icon(dev.ultreon.quantum.client.gui.icon.Icon)"""
        return 'Builder'._wrap(super(_Builder, self).icon(arg0))

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

    @overload
    def build(self) -> 'Notification':
        """public dev.ultreon.quantum.client.gui.Notification dev.ultreon.quantum.client.gui.Notification$Builder.build()"""
        return 'Notification'._wrap(super(Builder, self).build())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @property
    def icon(self, value: 'icon.Icon'):
        super(_Builder).icon(value)

    @overload
    def subText(self, arg0: str) -> 'Builder':
        """public dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification$Builder.subText(java.lang.String)"""
        return 'Builder'._wrap(super(_Builder, self).subText(arg0))

    @overload
    def duration(self, arg0: 'Duration') -> 'Builder':
        """public dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification$Builder.duration(dev.ultreon.libs.datetime.v0.Duration)"""
        return 'Builder'._wrap(super(_Builder, self).duration(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def subText(self, arg0: 'MutableText') -> 'Builder':
        """public dev.ultreon.quantum.client.gui.Notification$Builder dev.ultreon.quantum.client.gui.Notification$Builder.subText(dev.ultreon.quantum.text.MutableText)"""
        return 'Builder'._wrap(super(_Builder, self).subText(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.GlStateStack$GlState
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.util.RgbColor as _RgbColor
_RgbColor = _RgbColor
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.GlStateStack as _GlStateStack_GlState
_GlState = _GlStateStack_GlState.GlState
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GlState():
    """dev.ultreon.quantum.client.gui.GlStateStack.GlState"""
 
    @staticmethod
    def _wrap(java_value: _GlState) -> 'GlState':
        return GlState(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GlState):
        """
        Dynamic initializer for GlState.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GlState__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GlState__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @property
    def blendColor(self, value: 'util.RgbColor'):
        super(_GlState).blendColor(value)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.GlStateStack$GlState()"""
        val = _GlState()
        self.__wrapper = val

    @overload
    def apply(self):
        """public void dev.ultreon.quantum.client.gui.GlStateStack$GlState.apply()"""
        super(GlState, self).apply()

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
        """public dev.ultreon.quantum.client.gui.GlStateStack$GlState()"""
        val = _GlState()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @property
    def blendColor(self) -> RgbColor:
        return RgbColor._wrap(super(_GlState).blendColor())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'GlState'):
        """public dev.ultreon.quantum.client.gui.GlStateStack$GlState(dev.ultreon.quantum.client.gui.GlStateStack$GlState)"""
        val = _GlState(arg0)
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