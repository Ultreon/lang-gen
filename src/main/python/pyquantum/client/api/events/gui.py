from __future__ import annotations
from overload import overload


 
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents_MouseDrag
__MouseDrag = __ScreenEvents_MouseDrag.MouseDrag
 
class MouseDrag(ABC):
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseDrag"""
 
    @staticmethod
    def __wrap(java_value: __MouseDrag) -> 'MouseDrag':
        return MouseDrag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MouseDrag):
        """
        Dynamic initializer for MouseDrag.
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
    def onMouseDragScreen(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseDrag.onMouseDragScreen(int,int,int,int,int)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseDrag
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents_MouseDrag
__MouseDrag = __ScreenEvents_MouseDrag.MouseDrag
 
class MouseDrag(ABC):
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseDrag"""
 
    @staticmethod
    def __wrap(java_value: __MouseDrag) -> 'MouseDrag':
        return MouseDrag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MouseDrag):
        """
        Dynamic initializer for MouseDrag.
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
    def onMouseDragScreen(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseDrag.onMouseDragScreen(int,int,int,int,int)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseDrag 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseClick
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents_MouseClick
__MouseClick = __ScreenEvents_MouseClick.MouseClick
from abc import abstractmethod, ABC
 
class MouseClick(ABC):
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseClick"""
 
    @staticmethod
    def __wrap(java_value: __MouseClick) -> 'MouseClick':
        return MouseClick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MouseClick):
        """
        Dynamic initializer for MouseClick.
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
    def onMouseClickScreen(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseClick.onMouseClickScreen(int,int,int,int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.WidgetEvents$WidgetRemoved
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.api.events.gui.WidgetEvents as __WidgetEvents_WidgetRemoved
__WidgetRemoved = __WidgetEvents_WidgetRemoved.WidgetRemoved
 
class WidgetRemoved(ABC):
    """dev.ultreon.quantum.client.api.events.gui.WidgetEvents.WidgetRemoved"""
 
    @staticmethod
    def __wrap(java_value: __WidgetRemoved) -> 'WidgetRemoved':
        return WidgetRemoved(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WidgetRemoved):
        """
        Dynamic initializer for WidgetRemoved.
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
    def onWidgetRemoved(self, arg0: 'UIContainer', arg1: 'Widget'):
        """public abstract void dev.ultreon.quantum.client.api.events.gui.WidgetEvents$WidgetRemoved.onWidgetRemoved(dev.ultreon.quantum.client.gui.widget.UIContainer<?>,dev.ultreon.quantum.client.gui.widget.Widget)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.WidgetEvents
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.api.events.gui.WidgetEvents as __WidgetEvents
__WidgetEvents = __WidgetEvents
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
 
class WidgetEvents():
    """dev.ultreon.quantum.client.api.events.gui.WidgetEvents"""
 
    @staticmethod
    def __wrap(java_value: __WidgetEvents) -> 'WidgetEvents':
        return WidgetEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WidgetEvents):
        """
        Dynamic initializer for WidgetEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.WidgetEvents$WidgetRemoved> dev.ultreon.quantum.client.api.events.gui.WidgetEvents.WIDGET_REMOVED
    WIDGET_REMOVED: 'api.Event' = __wrap(__api.Event.WIDGET_REMOVED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.WidgetEvents$WidgetAdded> dev.ultreon.quantum.client.api.events.gui.WidgetEvents.WIDGET_ADDED
    WIDGET_ADDED: 'api.Event' = __wrap(__api.Event.WIDGET_ADDED)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.gui.WidgetEvents()"""
        val = __WidgetEvents()
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
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.gui.WidgetEvents()"""
        val = __WidgetEvents()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseEnter
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents_MouseEnter
__MouseEnter = __ScreenEvents_MouseEnter.MouseEnter
from abc import abstractmethod, ABC
 
class MouseEnter(ABC):
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseEnter"""
 
    @staticmethod
    def __wrap(java_value: __MouseEnter) -> 'MouseEnter':
        return MouseEnter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MouseEnter):
        """
        Dynamic initializer for MouseEnter.
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
    def onMouseEnterScreen(self, arg0: int, arg1: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseEnter.onMouseEnterScreen(int,int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MousePress
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents_MousePress
__MousePress = __ScreenEvents_MousePress.MousePress
from abc import abstractmethod, ABC
 
class MousePress(ABC):
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MousePress"""
 
    @staticmethod
    def __wrap(java_value: __MousePress) -> 'MousePress':
        return MousePress(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MousePress):
        """
        Dynamic initializer for MousePress.
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
    def onMousePressScreen(self, arg0: int, arg1: int, arg2: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MousePress.onMousePressScreen(int,int,int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents
__ScreenEvents = __ScreenEvents
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ScreenEvents():
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents"""
 
    @staticmethod
    def __wrap(java_value: __ScreenEvents) -> 'ScreenEvents':
        return ScreenEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScreenEvents):
        """
        Dynamic initializer for ScreenEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$Close> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.CLOSE
    CLOSE: 'api.Event' = __wrap(__api.Event.CLOSE)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$KeyPress> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.KEY_PRESS
    KEY_PRESS: 'api.Event' = __wrap(__api.Event.KEY_PRESS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseClick> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_CLICK
    MOUSE_CLICK: 'api.Event' = __wrap(__api.Event.MOUSE_CLICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MousePress> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_PRESS
    MOUSE_PRESS: 'api.Event' = __wrap(__api.Event.MOUSE_PRESS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$Open> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.OPEN
    OPEN: 'api.Event' = __wrap(__api.Event.OPEN)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseRelease> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_RELEASE
    MOUSE_RELEASE: 'api.Event' = __wrap(__api.Event.MOUSE_RELEASE)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseExit> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_EXIT
    MOUSE_EXIT: 'api.Event' = __wrap(__api.Event.MOUSE_EXIT)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseWheel> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_WHEEL
    MOUSE_WHEEL: 'api.Event' = __wrap(__api.Event.MOUSE_WHEEL)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseDrag> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_DRAG
    MOUSE_DRAG: 'api.Event' = __wrap(__api.Event.MOUSE_DRAG)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseEnter> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MOUSE_ENTER
    MOUSE_ENTER: 'api.Event' = __wrap(__api.Event.MOUSE_ENTER)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$KeyRelease> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.KEY_RELEASE
    KEY_RELEASE: 'api.Event' = __wrap(__api.Event.KEY_RELEASE)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.gui.ScreenEvents$CharType> dev.ultreon.quantum.client.api.events.gui.ScreenEvents.CHAR_TYPE
    CHAR_TYPE: 'api.Event' = __wrap(__api.Event.CHAR_TYPE)


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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.gui.ScreenEvents()"""
        val = __ScreenEvents()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.gui.ScreenEvents()"""
        val = __ScreenEvents()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$KeyRelease
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents_KeyRelease
__KeyRelease = __ScreenEvents_KeyRelease.KeyRelease
 
class KeyRelease(ABC):
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.KeyRelease"""
 
    @staticmethod
    def __wrap(java_value: __KeyRelease) -> 'KeyRelease':
        return KeyRelease(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeyRelease):
        """
        Dynamic initializer for KeyRelease.
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
    def onKeyReleaseScreen(self, arg0: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$KeyRelease.onKeyReleaseScreen(int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$Open
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents_Open
__Open = __ScreenEvents_Open.Open
from abc import abstractmethod, ABC
 
class Open(ABC):
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.Open"""
 
    @staticmethod
    def __wrap(java_value: __Open) -> 'Open':
        return Open(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Open):
        """
        Dynamic initializer for Open.
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
    def onOpenScreen(self, arg0: 'Screen'):
        """public abstract dev.ultreon.quantum.events.api.ValueEventResult<dev.ultreon.quantum.client.gui.Screen> dev.ultreon.quantum.client.api.events.gui.ScreenEvents$Open.onOpenScreen(dev.ultreon.quantum.client.gui.Screen)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$KeyPress
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents_KeyPress
__KeyPress = __ScreenEvents_KeyPress.KeyPress
from abc import abstractmethod, ABC
 
class KeyPress(ABC):
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.KeyPress"""
 
    @staticmethod
    def __wrap(java_value: __KeyPress) -> 'KeyPress':
        return KeyPress(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeyPress):
        """
        Dynamic initializer for KeyPress.
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
    def onKeyPressScreen(self, arg0: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$KeyPress.onKeyPressScreen(int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$Close
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents_Close
__Close = __ScreenEvents_Close.Close
 
class Close(ABC):
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.Close"""
 
    @staticmethod
    def __wrap(java_value: __Close) -> 'Close':
        return Close(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Close):
        """
        Dynamic initializer for Close.
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
    def onCloseScreen(self, arg0: 'Screen'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$Close.onCloseScreen(dev.ultreon.quantum.client.gui.Screen)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$CharType
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents_CharType
__CharType = __ScreenEvents_CharType.CharType
from abc import abstractmethod, ABC
 
class CharType(ABC):
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.CharType"""
 
    @staticmethod
    def __wrap(java_value: __CharType) -> 'CharType':
        return CharType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharType):
        """
        Dynamic initializer for CharType.
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
    def onCharTypeScreen(self, arg0: str):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$CharType.onCharTypeScreen(char)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseExit
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents_MouseExit
__MouseExit = __ScreenEvents_MouseExit.MouseExit
from abc import abstractmethod, ABC
 
class MouseExit(ABC):
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseExit"""
 
    @staticmethod
    def __wrap(java_value: __MouseExit) -> 'MouseExit':
        return MouseExit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MouseExit):
        """
        Dynamic initializer for MouseExit.
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
    def onMouseExitScreen(self, ):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseExit.onMouseExitScreen()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseWheel
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents_MouseWheel
__MouseWheel = __ScreenEvents_MouseWheel.MouseWheel
 
class MouseWheel(ABC):
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseWheel"""
 
    @staticmethod
    def __wrap(java_value: __MouseWheel) -> 'MouseWheel':
        return MouseWheel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MouseWheel):
        """
        Dynamic initializer for MouseWheel.
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
    def onMouseWheelScreen(self, arg0: int, arg1: int, arg2: float):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseWheel.onMouseWheelScreen(int,int,double)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseRelease
import dev.ultreon.quantum.client.api.events.gui.ScreenEvents as __ScreenEvents_MouseRelease
__MouseRelease = __ScreenEvents_MouseRelease.MouseRelease
from abc import abstractmethod, ABC
 
class MouseRelease(ABC):
    """dev.ultreon.quantum.client.api.events.gui.ScreenEvents.MouseRelease"""
 
    @staticmethod
    def __wrap(java_value: __MouseRelease) -> 'MouseRelease':
        return MouseRelease(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MouseRelease):
        """
        Dynamic initializer for MouseRelease.
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
    def onMouseReleaseScreen(self, arg0: int, arg1: int, arg2: int):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.gui.ScreenEvents$MouseRelease.onMouseReleaseScreen(int,int,int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.gui.WidgetEvents$WidgetAdded
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

import dev.ultreon.quantum.client.api.events.gui.WidgetEvents as __WidgetEvents_WidgetAdded
__WidgetAdded = __WidgetEvents_WidgetAdded.WidgetAdded
from abc import abstractmethod, ABC
 
class WidgetAdded(ABC):
    """dev.ultreon.quantum.client.api.events.gui.WidgetEvents.WidgetAdded"""
 
    @staticmethod
    def __wrap(java_value: __WidgetAdded) -> 'WidgetAdded':
        return WidgetAdded(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WidgetAdded):
        """
        Dynamic initializer for WidgetAdded.
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
    def onWidgetAdded(self, arg0: 'UIContainer', arg1: 'Widget'):
        """public abstract void dev.ultreon.quantum.client.api.events.gui.WidgetEvents$WidgetAdded.onWidgetAdded(dev.ultreon.quantum.client.gui.widget.UIContainer<?>,dev.ultreon.quantum.client.gui.widget.Widget)"""
        pass