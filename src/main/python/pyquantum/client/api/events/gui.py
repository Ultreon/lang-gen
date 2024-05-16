from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents_MouseDrag
_MouseDrag = _ScreenEvents_MouseDrag.MouseDrag
from abc import abstractmethod, ABC
 
class MouseDrag():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseDrag"""
 
    @staticmethod
    def _wrap(java_value: _MouseDrag) -> 'MouseDrag':
        return MouseDrag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MouseDrag):
        """
        Dynamic initializer for MouseDrag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MouseDrag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MouseDrag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onMouseDragScreen(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseDrag.onMouseDragScreen(int,int,int,int,int)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseDrag
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents_MouseDrag
_MouseDrag = _ScreenEvents_MouseDrag.MouseDrag
from abc import abstractmethod, ABC
 
class MouseDrag():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseDrag"""
 
    @staticmethod
    def _wrap(java_value: _MouseDrag) -> 'MouseDrag':
        return MouseDrag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MouseDrag):
        """
        Dynamic initializer for MouseDrag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MouseDrag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MouseDrag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onMouseDragScreen(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseDrag.onMouseDragScreen(int,int,int,int,int)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseDrag 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseClick
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents_MouseClick
_MouseClick = _ScreenEvents_MouseClick.MouseClick
from abc import abstractmethod, ABC
 
class MouseClick():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseClick"""
 
    @staticmethod
    def _wrap(java_value: _MouseClick) -> 'MouseClick':
        return MouseClick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MouseClick):
        """
        Dynamic initializer for MouseClick.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MouseClick__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MouseClick__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onMouseClickScreen(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseClick.onMouseClickScreen(int,int,int,int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.WidgetEvents$WidgetRemoved
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import dev.ultreon.quantum.client.api.events.gui.WidgetEvents as _WidgetEvents_WidgetRemoved
_WidgetRemoved = _WidgetEvents_WidgetRemoved.WidgetRemoved
from abc import abstractmethod, ABC
 
class WidgetRemoved():
    """dev.ultreon.quantum.client.api.events.gui.WidgetEvents.WidgetRemoved"""
 
    @staticmethod
    def _wrap(java_value: _WidgetRemoved) -> 'WidgetRemoved':
        return WidgetRemoved(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WidgetRemoved):
        """
        Dynamic initializer for WidgetRemoved.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WidgetRemoved__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WidgetRemoved__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onWidgetRemoved(self, arg0: 'UIContainer', arg1: 'Widget'):
        """public abstract void dev.ultreon.quantum.client.api.events.gui.WidgetEvents$WidgetRemoved.onWidgetRemoved(dev.ultreon.quantum.client.gui.widget.UIContainer<?>,dev.ultreon.quantum.client.gui.widget.Widget)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.WidgetEvents
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.events import api
except ImportError:
    api = _import_once("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.api.events.gui.WidgetEvents as _WidgetEvents
_WidgetEvents = _WidgetEvents
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WidgetEvents():
    """dev.ultreon.quantum.client.api.events.gui.WidgetEvents"""
 
    @staticmethod
    def _wrap(java_value: _WidgetEvents) -> 'WidgetEvents':
        return WidgetEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WidgetEvents):
        """
        Dynamic initializer for WidgetEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WidgetEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WidgetEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.WidgetEvents$WidgetAdded> dev.ultreon.quantum.client.api.events.gui.WidgetEvents.WIDGET_ADDED
    WIDGET_ADDED: 'api.Event' = _wrap(_api.Event.WIDGET_ADDED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.WidgetEvents$WidgetRemoved> dev.ultreon.quantum.client.api.events.gui.WidgetEvents.WIDGET_REMOVED
    WIDGET_REMOVED: 'api.Event' = _wrap(_api.Event.WIDGET_REMOVED)


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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.gui.WidgetEvents()"""
        val = _WidgetEvents()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.gui.WidgetEvents()"""
        val = _WidgetEvents()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseEnter
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents_MouseEnter
_MouseEnter = _ScreenEvents_MouseEnter.MouseEnter
from abc import abstractmethod, ABC
 
class MouseEnter():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseEnter"""
 
    @staticmethod
    def _wrap(java_value: _MouseEnter) -> 'MouseEnter':
        return MouseEnter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MouseEnter):
        """
        Dynamic initializer for MouseEnter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MouseEnter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MouseEnter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onMouseEnterScreen(self, arg0: int, arg1: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseEnter.onMouseEnterScreen(int,int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MousePress
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents_MousePress
_MousePress = _ScreenEvents_MousePress.MousePress
from abc import abstractmethod, ABC
 
class MousePress():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MousePress"""
 
    @staticmethod
    def _wrap(java_value: _MousePress) -> 'MousePress':
        return MousePress(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MousePress):
        """
        Dynamic initializer for MousePress.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MousePress__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MousePress__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onMousePressScreen(self, arg0: int, arg1: int, arg2: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MousePress.onMousePressScreen(int,int,int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.events import api
except ImportError:
    api = _import_once("pyquantum.events.api")

from builtins import str
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents
_ScreenEvents = _ScreenEvents
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ScreenEvents():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents"""
 
    @staticmethod
    def _wrap(java_value: _ScreenEvents) -> 'ScreenEvents':
        return ScreenEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScreenEvents):
        """
        Dynamic initializer for ScreenEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScreenEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScreenEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseRelease> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_RELEASE
    MOUSE_RELEASE: 'api.Event' = _wrap(_api.Event.MOUSE_RELEASE)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseClick> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_CLICK
    MOUSE_CLICK: 'api.Event' = _wrap(_api.Event.MOUSE_CLICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MousePress> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_PRESS
    MOUSE_PRESS: 'api.Event' = _wrap(_api.Event.MOUSE_PRESS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$KeyRelease> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.KEY_RELEASE
    KEY_RELEASE: 'api.Event' = _wrap(_api.Event.KEY_RELEASE)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$Close> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.CLOSE
    CLOSE: 'api.Event' = _wrap(_api.Event.CLOSE)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$Open> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.OPEN
    OPEN: 'api.Event' = _wrap(_api.Event.OPEN)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseDrag> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_DRAG
    MOUSE_DRAG: 'api.Event' = _wrap(_api.Event.MOUSE_DRAG)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseEnter> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_ENTER
    MOUSE_ENTER: 'api.Event' = _wrap(_api.Event.MOUSE_ENTER)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseExit> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_EXIT
    MOUSE_EXIT: 'api.Event' = _wrap(_api.Event.MOUSE_EXIT)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$KeyPress> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.KEY_PRESS
    KEY_PRESS: 'api.Event' = _wrap(_api.Event.KEY_PRESS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$CharType> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.CHAR_TYPE
    CHAR_TYPE: 'api.Event' = _wrap(_api.Event.CHAR_TYPE)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseWheel> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_WHEEL
    MOUSE_WHEEL: 'api.Event' = _wrap(_api.Event.MOUSE_WHEEL)


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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.gui.ScreenEvents()"""
        val = _ScreenEvents()
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
        """public dev.ultreon.quantum.client.api.events.gui.ScreenEvents()"""
        val = _ScreenEvents()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$KeyRelease
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents_KeyRelease
_KeyRelease = _ScreenEvents_KeyRelease.KeyRelease
from abc import abstractmethod, ABC
 
class KeyRelease():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.KeyRelease"""
 
    @staticmethod
    def _wrap(java_value: _KeyRelease) -> 'KeyRelease':
        return KeyRelease(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KeyRelease):
        """
        Dynamic initializer for KeyRelease.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KeyRelease__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KeyRelease__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onKeyReleaseScreen(self, arg0: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$KeyRelease.onKeyReleaseScreen(int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$Open
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents_Open
_Open = _ScreenEvents_Open.Open
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class Open():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.Open"""
 
    @staticmethod
    def _wrap(java_value: _Open) -> 'Open':
        return Open(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Open):
        """
        Dynamic initializer for Open.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Open__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Open__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onOpenScreen(self, arg0: 'Screen'):
        """public abstract dev.ultreon.quantum.events.api.ValueEventResult<dev.ultreon.quantum.client.gui.Screen> dev.ultreon.quantum.client.api.events.gui.ScreenEvents$Open.onOpenScreen(dev.ultreon.quantum.client.gui.Screen)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$KeyPress
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents_KeyPress
_KeyPress = _ScreenEvents_KeyPress.KeyPress
from abc import abstractmethod, ABC
 
class KeyPress():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.KeyPress"""
 
    @staticmethod
    def _wrap(java_value: _KeyPress) -> 'KeyPress':
        return KeyPress(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KeyPress):
        """
        Dynamic initializer for KeyPress.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KeyPress__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KeyPress__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onKeyPressScreen(self, arg0: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$KeyPress.onKeyPressScreen(int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$Close
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents_Close
_Close = _ScreenEvents_Close.Close
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class Close():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.Close"""
 
    @staticmethod
    def _wrap(java_value: _Close) -> 'Close':
        return Close(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Close):
        """
        Dynamic initializer for Close.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Close__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Close__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onCloseScreen(self, arg0: 'Screen'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$Close.onCloseScreen(dev.ultreon.quantum.client.gui.Screen)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$CharType
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents_CharType
_CharType = _ScreenEvents_CharType.CharType
from abc import abstractmethod, ABC
 
class CharType():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.CharType"""
 
    @staticmethod
    def _wrap(java_value: _CharType) -> 'CharType':
        return CharType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharType):
        """
        Dynamic initializer for CharType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onCharTypeScreen(self, arg0: str):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$CharType.onCharTypeScreen(char)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseExit
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents_MouseExit
_MouseExit = _ScreenEvents_MouseExit.MouseExit
from abc import abstractmethod, ABC
 
class MouseExit():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseExit"""
 
    @staticmethod
    def _wrap(java_value: _MouseExit) -> 'MouseExit':
        return MouseExit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MouseExit):
        """
        Dynamic initializer for MouseExit.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MouseExit__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MouseExit__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onMouseExitScreen(self, ):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseExit.onMouseExitScreen()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseWheel
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents_MouseWheel
_MouseWheel = _ScreenEvents_MouseWheel.MouseWheel
from abc import abstractmethod, ABC
 
class MouseWheel():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseWheel"""
 
    @staticmethod
    def _wrap(java_value: _MouseWheel) -> 'MouseWheel':
        return MouseWheel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MouseWheel):
        """
        Dynamic initializer for MouseWheel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MouseWheel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MouseWheel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onMouseWheelScreen(self, arg0: int, arg1: int, arg2: float):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseWheel.onMouseWheelScreen(int,int,double)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseRelease
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as _ScreenEvents_MouseRelease
_MouseRelease = _ScreenEvents_MouseRelease.MouseRelease
from abc import abstractmethod, ABC
 
class MouseRelease():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseRelease"""
 
    @staticmethod
    def _wrap(java_value: _MouseRelease) -> 'MouseRelease':
        return MouseRelease(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MouseRelease):
        """
        Dynamic initializer for MouseRelease.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MouseRelease__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MouseRelease__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onMouseReleaseScreen(self, arg0: int, arg1: int, arg2: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseRelease.onMouseReleaseScreen(int,int,int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.WidgetEvents$WidgetAdded
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import dev.ultreon.quantum.client.api.events.gui.WidgetEvents as _WidgetEvents_WidgetAdded
_WidgetAdded = _WidgetEvents_WidgetAdded.WidgetAdded
from abc import abstractmethod, ABC
 
class WidgetAdded():
    """dev.ultreon.quantum.client.api.events.gui.WidgetEvents.WidgetAdded"""
 
    @staticmethod
    def _wrap(java_value: _WidgetAdded) -> 'WidgetAdded':
        return WidgetAdded(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WidgetAdded):
        """
        Dynamic initializer for WidgetAdded.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WidgetAdded__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WidgetAdded__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onWidgetAdded(self, arg0: 'UIContainer', arg1: 'Widget'):
        """public abstract void dev.ultreon.quantum.client.api.events.gui.WidgetEvents$WidgetAdded.onWidgetAdded(dev.ultreon.quantum.client.gui.widget.UIContainer<?>,dev.ultreon.quantum.client.gui.widget.Widget)"""
        pass