from __future__ import annotations
from overload import overload


 
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
import dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage as __ProfilerDebugPage
__ProfilerDebugPage = __ProfilerDebugPage
from builtins import bool
from builtins import int
 
class ProfilerDebugPage(__DebugPage, DebugPage):
    """dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage"""
 
    @staticmethod
    def __wrap(java_value: __ProfilerDebugPage) -> 'ProfilerDebugPage':
        return ProfilerDebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ProfilerDebugPage):
        """
        Dynamic initializer for ProfilerDebugPage.
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
 
    # public static final dev.ultreon.quantum.client.gui.debug.DebugPage dev.ultreon.quantum.client.gui.debug.DebugPage.EMPTY
    EMPTY: 'DebugPage' = __wrap(__DebugPage.EMPTY)


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

    @override
    @overload
    def render(self, arg0: 'DebugPageContext'):
        """public void dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        super(__ProfilerDebugPage, self).render(arg0)

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
        """public dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage()"""
        val = __ProfilerDebugPage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage()"""
        val = __ProfilerDebugPage()
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

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage
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
import dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage as __ProfilerDebugPage
__ProfilerDebugPage = __ProfilerDebugPage
from builtins import bool
from builtins import int
 
class ProfilerDebugPage(__DebugPage, DebugPage):
    """dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage"""
 
    @staticmethod
    def __wrap(java_value: __ProfilerDebugPage) -> 'ProfilerDebugPage':
        return ProfilerDebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ProfilerDebugPage):
        """
        Dynamic initializer for ProfilerDebugPage.
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
 
    # public static final dev.ultreon.quantum.client.gui.debug.DebugPage dev.ultreon.quantum.client.gui.debug.DebugPage.EMPTY
    EMPTY: 'DebugPage' = __wrap(__DebugPage.EMPTY)


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

    @override
    @overload
    def render(self, arg0: 'DebugPageContext'):
        """public void dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        super(__ProfilerDebugPage, self).render(arg0)

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
        """public dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage()"""
        val = __ProfilerDebugPage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage()"""
        val = __ProfilerDebugPage()
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

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.DebugOverlay
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
import dev.ultreon.quantum.client.gui.debug.DebugOverlay as __DebugOverlay
__DebugOverlay = __DebugOverlay
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
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
 
class DebugOverlay():
    """dev.ultreon.quantum.client.gui.debug.DebugOverlay"""
 
    @staticmethod
    def __wrap(java_value: __DebugOverlay) -> 'DebugOverlay':
        return DebugOverlay(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DebugOverlay):
        """
        Dynamic initializer for DebugOverlay.
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
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay(dev.ultreon.quantum.client.QuantumClient)"""
        val = __DebugOverlay(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def updateProfiler(self):
        """public void dev.ultreon.quantum.client.gui.debug.DebugOverlay.updateProfiler()"""
        super(DebugOverlay, self).updateProfiler()

    @overload
    def entryLine(self, arg0: 'Renderer') -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.entryLine(dev.ultreon.quantum.client.gui.Renderer)"""
        return 'DebugOverlay'.__wrap(super(__DebugOverlay, self).entryLine(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def render(self, arg0: 'Renderer'):
        """public void dev.ultreon.quantum.client.gui.debug.DebugOverlay.render(dev.ultreon.quantum.client.gui.Renderer)"""
        super(__DebugOverlay, self).render(arg0)

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
    def left(self) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.left()"""
        return 'DebugOverlay'.__wrap(super(DebugOverlay, self).left())

    @overload
    def nextPage(self):
        """public void dev.ultreon.quantum.client.gui.debug.DebugOverlay.nextPage()"""
        super(DebugOverlay, self).nextPage()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def entryLine(self, arg0: 'Renderer', arg1: int, arg2: str, arg3: int) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.entryLine(dev.ultreon.quantum.client.gui.Renderer,int,java.lang.String,long)"""
        return 'DebugOverlay'.__wrap(super(__DebugOverlay, self).entryLine(arg0, __int.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @overload
    def left(self, arg0: 'Renderer', arg1: str, arg2: object) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.left(dev.ultreon.quantum.client.gui.Renderer,java.lang.String,java.lang.Object)"""
        return 'DebugOverlay'.__wrap(super(__DebugOverlay, self).left(arg0, arg1, arg2))

    @overload
    def left(self, arg0: 'Renderer', arg1: str) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.left(dev.ultreon.quantum.client.gui.Renderer,java.lang.String)"""
        return 'DebugOverlay'.__wrap(super(__DebugOverlay, self).left(arg0, arg1))

    @overload
    def entryLine(self, arg0: 'Renderer', arg1: str, arg2: str) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.entryLine(dev.ultreon.quantum.client.gui.Renderer,java.lang.String,java.lang.String)"""
        return 'DebugOverlay'.__wrap(super(__DebugOverlay, self).entryLine(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def right(self, arg0: 'Renderer', arg1: str) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.right(dev.ultreon.quantum.client.gui.Renderer,java.lang.String)"""
        return 'DebugOverlay'.__wrap(super(__DebugOverlay, self).right(arg0, arg1))

    @overload
    def right(self) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.right()"""
        return 'DebugOverlay'.__wrap(super(DebugOverlay, self).right())

    @overload
    def prevPage(self):
        """public void dev.ultreon.quantum.client.gui.debug.DebugOverlay.prevPage()"""
        super(DebugOverlay, self).prevPage()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def right(self, arg0: 'Renderer', arg1: str, arg2: object) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.right(dev.ultreon.quantum.client.gui.Renderer,java.lang.String,java.lang.Object)"""
        return 'DebugOverlay'.__wrap(super(__DebugOverlay, self).right(arg0, arg1, arg2)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.InspectorDebugPage
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
import dev.ultreon.quantum.client.gui.debug.InspectorDebugPage as __InspectorDebugPage
__InspectorDebugPage = __InspectorDebugPage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InspectorDebugPage(__DebugPage, DebugPage):
    """dev.ultreon.quantum.client.gui.debug.InspectorDebugPage"""
 
    @staticmethod
    def __wrap(java_value: __InspectorDebugPage) -> 'InspectorDebugPage':
        return InspectorDebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InspectorDebugPage):
        """
        Dynamic initializer for InspectorDebugPage.
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
 
    # public static final dev.ultreon.quantum.client.gui.debug.DebugPage dev.ultreon.quantum.client.gui.debug.DebugPage.EMPTY
    EMPTY: 'DebugPage' = __wrap(__DebugPage.EMPTY)


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
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.debug.InspectorDebugPage()"""
        val = __InspectorDebugPage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.debug.InspectorDebugPage()"""
        val = __InspectorDebugPage()
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

    @override
    @overload
    def render(self, arg0: 'DebugPageContext'):
        """public void dev.ultreon.quantum.client.gui.debug.InspectorDebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        super(__InspectorDebugPage, self).render(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.SystemInfoDebugPage
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.client.gui.debug.SystemInfoDebugPage as __SystemInfoDebugPage
__SystemInfoDebugPage = __SystemInfoDebugPage
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SystemInfoDebugPage(__DebugPage, DebugPage):
    """dev.ultreon.quantum.client.gui.debug.SystemInfoDebugPage"""
 
    @staticmethod
    def __wrap(java_value: __SystemInfoDebugPage) -> 'SystemInfoDebugPage':
        return SystemInfoDebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SystemInfoDebugPage):
        """
        Dynamic initializer for SystemInfoDebugPage.
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
 
    # public static final dev.ultreon.quantum.client.gui.debug.DebugPage dev.ultreon.quantum.client.gui.debug.DebugPage.EMPTY
    EMPTY: 'DebugPage' = __wrap(__DebugPage.EMPTY)


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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def render(self, arg0: 'DebugPageContext'):
        """public void dev.ultreon.quantum.client.gui.debug.SystemInfoDebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        super(__SystemInfoDebugPage, self).render(arg0)

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
        """public dev.ultreon.quantum.client.gui.debug.SystemInfoDebugPage()"""
        val = __SystemInfoDebugPage()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.debug.SystemInfoDebugPage()"""
        val = __SystemInfoDebugPage()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.DebugPage
import dev.ultreon.quantum.client.gui.debug.DebugPage as __DebugPage
__DebugPage = __DebugPage
from abc import abstractmethod, ABC
 
class DebugPage(ABC):
    """dev.ultreon.quantum.client.gui.debug.DebugPage"""
 
    @staticmethod
    def __wrap(java_value: __DebugPage) -> 'DebugPage':
        return DebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DebugPage):
        """
        Dynamic initializer for DebugPage.
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
 
    # public static final dev.ultreon.quantum.client.gui.debug.DebugPage dev.ultreon.quantum.client.gui.debug.DebugPage.EMPTY
    EMPTY: 'DebugPage' = __wrap(__DebugPage.EMPTY)


    @abstractmethod
    def render(self, arg0: 'DebugPageContext'):
        """public abstract void dev.ultreon.quantum.client.gui.debug.DebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.SimpleDebugPage
from builtins import str
import java.lang.Long as __long
import dev.ultreon.quantum.client.gui.debug.SimpleDebugPage as __SimpleDebugPage
__SimpleDebugPage = __SimpleDebugPage
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
 
class SimpleDebugPage(__DebugPage, DebugPage):
    """dev.ultreon.quantum.client.gui.debug.SimpleDebugPage"""
 
    @staticmethod
    def __wrap(java_value: __SimpleDebugPage) -> 'SimpleDebugPage':
        return SimpleDebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleDebugPage):
        """
        Dynamic initializer for SimpleDebugPage.
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
 
    # public static final dev.ultreon.quantum.client.gui.debug.DebugPage dev.ultreon.quantum.client.gui.debug.DebugPage.EMPTY
    EMPTY: 'DebugPage' = __wrap(__DebugPage.EMPTY)


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
        """public dev.ultreon.quantum.client.gui.debug.SimpleDebugPage()"""
        val = __SimpleDebugPage()
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
    def render(self, arg0: 'DebugPageContext'):
        """public void dev.ultreon.quantum.client.gui.debug.SimpleDebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        super(__SimpleDebugPage, self).render(arg0)

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.debug.SimpleDebugPage()"""
        val = __SimpleDebugPage()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.DebugPageContext
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
from abc import abstractmethod, ABC
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.client.gui.debug.DebugPageContext as __DebugPageContext
__DebugPageContext = __DebugPageContext
 
class DebugPageContext(ABC):
    """dev.ultreon.quantum.client.gui.debug.DebugPageContext"""
 
    @staticmethod
    def __wrap(java_value: __DebugPageContext) -> 'DebugPageContext':
        return DebugPageContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DebugPageContext):
        """
        Dynamic initializer for DebugPageContext.
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
    def right(self, arg0: str):
        """public abstract dev.ultreon.quantum.client.gui.debug.DebugPageContext dev.ultreon.quantum.client.gui.debug.DebugPageContext.right(java.lang.String)"""
        pass

    @abstractmethod
    def entryLine(self, arg0: 'TextObject'):
        """public abstract dev.ultreon.quantum.client.gui.debug.DebugPageContext dev.ultreon.quantum.client.gui.debug.DebugPageContext.entryLine(dev.ultreon.quantum.text.TextObject)"""
        pass

    @overload
    def block2sectionPos(self, arg0: 'BlockPos') -> 'vector.Vec3i':
        """public default dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.client.gui.debug.DebugPageContext.block2sectionPos(dev.ultreon.quantum.world.BlockPos)"""
        return 'vector.Vec3i'.__wrap(super(__DebugPageContext, self).block2sectionPos(arg0))

    @abstractmethod
    def entryLine(self, ):
        """public abstract dev.ultreon.quantum.client.gui.debug.DebugPageContext dev.ultreon.quantum.client.gui.debug.DebugPageContext.entryLine()"""
        pass

    @abstractmethod
    def client(self, ):
        """public abstract dev.ultreon.quantum.client.QuantumClient dev.ultreon.quantum.client.gui.debug.DebugPageContext.client()"""
        pass

    @abstractmethod
    def right(self, ):
        """public abstract dev.ultreon.quantum.client.gui.debug.DebugPageContext dev.ultreon.quantum.client.gui.debug.DebugPageContext.right()"""
        pass

    @abstractmethod
    def entryLine(self, arg0: int, arg1: str, arg2: int):
        """public abstract dev.ultreon.quantum.client.gui.debug.DebugPageContext dev.ultreon.quantum.client.gui.debug.DebugPageContext.entryLine(int,java.lang.String,long)"""
        pass

    @abstractmethod
    def left(self, arg0: str, arg1: object):
        """public abstract dev.ultreon.quantum.client.gui.debug.DebugPageContext dev.ultreon.quantum.client.gui.debug.DebugPageContext.left(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def entryLine(self, arg0: int, arg1: str):
        """public abstract dev.ultreon.quantum.client.gui.debug.DebugPageContext dev.ultreon.quantum.client.gui.debug.DebugPageContext.entryLine(int,java.lang.String)"""
        pass

    @abstractmethod
    def entryLine(self, arg0: str, arg1: str):
        """public abstract dev.ultreon.quantum.client.gui.debug.DebugPageContext dev.ultreon.quantum.client.gui.debug.DebugPageContext.entryLine(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def left(self, arg0: str):
        """public abstract dev.ultreon.quantum.client.gui.debug.DebugPageContext dev.ultreon.quantum.client.gui.debug.DebugPageContext.left(java.lang.String)"""
        pass

    @abstractmethod
    def left(self, ):
        """public abstract dev.ultreon.quantum.client.gui.debug.DebugPageContext dev.ultreon.quantum.client.gui.debug.DebugPageContext.left()"""
        pass

    @abstractmethod
    def right(self, arg0: str, arg1: object):
        """public abstract dev.ultreon.quantum.client.gui.debug.DebugPageContext dev.ultreon.quantum.client.gui.debug.DebugPageContext.right(java.lang.String,java.lang.Object)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.GenericDebugPage
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
import dev.ultreon.quantum.client.gui.debug.GenericDebugPage as __GenericDebugPage
__GenericDebugPage = __GenericDebugPage
from builtins import bool
from builtins import int
 
class GenericDebugPage(__DebugPage, DebugPage):
    """dev.ultreon.quantum.client.gui.debug.GenericDebugPage"""
 
    @staticmethod
    def __wrap(java_value: __GenericDebugPage) -> 'GenericDebugPage':
        return GenericDebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GenericDebugPage):
        """
        Dynamic initializer for GenericDebugPage.
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
 
    # public static final dev.ultreon.quantum.client.gui.debug.DebugPage dev.ultreon.quantum.client.gui.debug.DebugPage.EMPTY
    EMPTY: 'DebugPage' = __wrap(__DebugPage.EMPTY)


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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.debug.GenericDebugPage()"""
        val = __GenericDebugPage()
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
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.debug.GenericDebugPage()"""
        val = __GenericDebugPage()
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

    @override
    @overload
    def render(self, arg0: 'DebugPageContext'):
        """public void dev.ultreon.quantum.client.gui.debug.GenericDebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        super(__GenericDebugPage, self).render(arg0)