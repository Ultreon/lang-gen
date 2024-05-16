from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage as _ProfilerDebugPage
_ProfilerDebugPage = _ProfilerDebugPage
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ProfilerDebugPage():
    """dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage"""
 
    @staticmethod
    def _wrap(java_value: _ProfilerDebugPage) -> 'ProfilerDebugPage':
        return ProfilerDebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ProfilerDebugPage):
        """
        Dynamic initializer for ProfilerDebugPage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ProfilerDebugPage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ProfilerDebugPage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage()"""
        val = _ProfilerDebugPage()
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
    def render(self, arg0: 'DebugPageContext'):
        """public void dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        super(_ProfilerDebugPage, self).render(arg0)

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage()"""
        val = _ProfilerDebugPage()
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


DebugPage.EMPTY = DebugPage._wrap(_EMPTY.EMPTY)

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage as _ProfilerDebugPage
_ProfilerDebugPage = _ProfilerDebugPage
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ProfilerDebugPage():
    """dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage"""
 
    @staticmethod
    def _wrap(java_value: _ProfilerDebugPage) -> 'ProfilerDebugPage':
        return ProfilerDebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ProfilerDebugPage):
        """
        Dynamic initializer for ProfilerDebugPage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ProfilerDebugPage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ProfilerDebugPage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage()"""
        val = _ProfilerDebugPage()
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
    def render(self, arg0: 'DebugPageContext'):
        """public void dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        super(_ProfilerDebugPage, self).render(arg0)

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage()"""
        val = _ProfilerDebugPage()
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


DebugPage.EMPTY = DebugPage._wrap(_EMPTY.EMPTY)

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.ProfilerDebugPage 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.DebugOverlay
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.gui.debug.DebugOverlay as _DebugOverlay
_DebugOverlay = _DebugOverlay
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
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
 
class DebugOverlay():
    """dev.ultreon.quantum.client.gui.debug.DebugOverlay"""
 
    @staticmethod
    def _wrap(java_value: _DebugOverlay) -> 'DebugOverlay':
        return DebugOverlay(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DebugOverlay):
        """
        Dynamic initializer for DebugOverlay.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DebugOverlay__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DebugOverlay__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def right(self, arg0: 'Renderer', arg1: str, arg2: object) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.right(dev.ultreon.quantum.client.gui.Renderer,java.lang.String,java.lang.Object)"""
        return 'DebugOverlay'._wrap(super(_DebugOverlay, self).right(arg0, arg1, arg2))

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay(dev.ultreon.quantum.client.QuantumClient)"""
        val = _DebugOverlay(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def updateProfiler(self):
        """public void dev.ultreon.quantum.client.gui.debug.DebugOverlay.updateProfiler()"""
        super(DebugOverlay, self).updateProfiler()

    @overload
    def entryLine(self, arg0: 'Renderer', arg1: int, arg2: str, arg3: int) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.entryLine(dev.ultreon.quantum.client.gui.Renderer,int,java.lang.String,long)"""
        return 'DebugOverlay'._wrap(super(_DebugOverlay, self).entryLine(arg0, _int.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def left(self, arg0: 'Renderer', arg1: str, arg2: object) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.left(dev.ultreon.quantum.client.gui.Renderer,java.lang.String,java.lang.Object)"""
        return 'DebugOverlay'._wrap(super(_DebugOverlay, self).left(arg0, arg1, arg2))

    @overload
    def left(self, arg0: 'Renderer', arg1: str) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.left(dev.ultreon.quantum.client.gui.Renderer,java.lang.String)"""
        return 'DebugOverlay'._wrap(super(_DebugOverlay, self).left(arg0, arg1))

    @overload
    def right(self) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.right()"""
        return 'DebugOverlay'._wrap(super(DebugOverlay, self).right())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def left(self) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.left()"""
        return 'DebugOverlay'._wrap(super(DebugOverlay, self).left())

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
    def render(self, arg0: 'Renderer'):
        """public void dev.ultreon.quantum.client.gui.debug.DebugOverlay.render(dev.ultreon.quantum.client.gui.Renderer)"""
        super(_DebugOverlay, self).render(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def entryLine(self, arg0: 'Renderer', arg1: str, arg2: str) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.entryLine(dev.ultreon.quantum.client.gui.Renderer,java.lang.String,java.lang.String)"""
        return 'DebugOverlay'._wrap(super(_DebugOverlay, self).entryLine(arg0, arg1, arg2))

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
    def right(self, arg0: 'Renderer', arg1: str) -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.right(dev.ultreon.quantum.client.gui.Renderer,java.lang.String)"""
        return 'DebugOverlay'._wrap(super(_DebugOverlay, self).right(arg0, arg1))

    @overload
    def entryLine(self, arg0: 'Renderer') -> 'DebugOverlay':
        """public dev.ultreon.quantum.client.gui.debug.DebugOverlay dev.ultreon.quantum.client.gui.debug.DebugOverlay.entryLine(dev.ultreon.quantum.client.gui.Renderer)"""
        return 'DebugOverlay'._wrap(super(_DebugOverlay, self).entryLine(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.InspectorDebugPage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.gui.debug.InspectorDebugPage as _InspectorDebugPage
_InspectorDebugPage = _InspectorDebugPage
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InspectorDebugPage():
    """dev.ultreon.quantum.client.gui.debug.InspectorDebugPage"""
 
    @staticmethod
    def _wrap(java_value: _InspectorDebugPage) -> 'InspectorDebugPage':
        return InspectorDebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InspectorDebugPage):
        """
        Dynamic initializer for InspectorDebugPage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InspectorDebugPage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InspectorDebugPage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def render(self, arg0: 'DebugPageContext'):
        """public void dev.ultreon.quantum.client.gui.debug.InspectorDebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        super(_InspectorDebugPage, self).render(arg0)

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
        """public dev.ultreon.quantum.client.gui.debug.InspectorDebugPage()"""
        val = _InspectorDebugPage()
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
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.debug.InspectorDebugPage()"""
        val = _InspectorDebugPage()
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


DebugPage.EMPTY = DebugPage._wrap(_EMPTY.EMPTY) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.SystemInfoDebugPage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.gui.debug.SystemInfoDebugPage as _SystemInfoDebugPage
_SystemInfoDebugPage = _SystemInfoDebugPage
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SystemInfoDebugPage():
    """dev.ultreon.quantum.client.gui.debug.SystemInfoDebugPage"""
 
    @staticmethod
    def _wrap(java_value: _SystemInfoDebugPage) -> 'SystemInfoDebugPage':
        return SystemInfoDebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SystemInfoDebugPage):
        """
        Dynamic initializer for SystemInfoDebugPage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SystemInfoDebugPage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SystemInfoDebugPage__wrapper":
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
        """public dev.ultreon.quantum.client.gui.debug.SystemInfoDebugPage()"""
        val = _SystemInfoDebugPage()
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

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def render(self, arg0: 'DebugPageContext'):
        """public void dev.ultreon.quantum.client.gui.debug.SystemInfoDebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        super(_SystemInfoDebugPage, self).render(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.debug.SystemInfoDebugPage()"""
        val = _SystemInfoDebugPage()
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


DebugPage.EMPTY = DebugPage._wrap(_EMPTY.EMPTY) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.DebugPage
import dev.ultreon.quantum.client.gui.debug.DebugPage as _DebugPage
_DebugPage = _DebugPage
from abc import abstractmethod, ABC
 
class DebugPage():
    """dev.ultreon.quantum.client.gui.debug.DebugPage"""
 
    @staticmethod
    def _wrap(java_value: _DebugPage) -> 'DebugPage':
        return DebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DebugPage):
        """
        Dynamic initializer for DebugPage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DebugPage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DebugPage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def render(self, arg0: 'DebugPageContext'):
        """public abstract void dev.ultreon.quantum.client.gui.debug.DebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        pass


DebugPage.EMPTY = DebugPage._wrap(_EMPTY.EMPTY) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.SimpleDebugPage
import dev.ultreon.quantum.client.gui.debug.SimpleDebugPage as _SimpleDebugPage
_SimpleDebugPage = _SimpleDebugPage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleDebugPage():
    """dev.ultreon.quantum.client.gui.debug.SimpleDebugPage"""
 
    @staticmethod
    def _wrap(java_value: _SimpleDebugPage) -> 'SimpleDebugPage':
        return SimpleDebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleDebugPage):
        """
        Dynamic initializer for SimpleDebugPage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleDebugPage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleDebugPage__wrapper":
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
        """public dev.ultreon.quantum.client.gui.debug.SimpleDebugPage()"""
        val = _SimpleDebugPage()
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
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.debug.SimpleDebugPage()"""
        val = _SimpleDebugPage()
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

    @override
    @overload
    def render(self, arg0: 'DebugPageContext'):
        """public void dev.ultreon.quantum.client.gui.debug.SimpleDebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        super(_SimpleDebugPage, self).render(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())


DebugPage.EMPTY = DebugPage._wrap(_EMPTY.EMPTY) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.debug.DebugPageContext
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.client.gui.debug.DebugPageContext as _DebugPageContext
_DebugPageContext = _DebugPageContext
from abc import abstractmethod, ABC
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
 
class DebugPageContext():
    """dev.ultreon.quantum.client.gui.debug.DebugPageContext"""
 
    @staticmethod
    def _wrap(java_value: _DebugPageContext) -> 'DebugPageContext':
        return DebugPageContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DebugPageContext):
        """
        Dynamic initializer for DebugPageContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DebugPageContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DebugPageContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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

    @overload
    def block2sectionPos(self, arg0: 'BlockPos') -> 'vector.Vec3i':
        """public default dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.client.gui.debug.DebugPageContext.block2sectionPos(dev.ultreon.quantum.world.BlockPos)"""
        return 'vector.Vec3i'._wrap(super(_DebugPageContext, self).block2sectionPos(arg0))

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
from pyquantum_helper import override
import dev.ultreon.quantum.client.gui.debug.GenericDebugPage as _GenericDebugPage
_GenericDebugPage = _GenericDebugPage
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GenericDebugPage():
    """dev.ultreon.quantum.client.gui.debug.GenericDebugPage"""
 
    @staticmethod
    def _wrap(java_value: _GenericDebugPage) -> 'GenericDebugPage':
        return GenericDebugPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GenericDebugPage):
        """
        Dynamic initializer for GenericDebugPage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GenericDebugPage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GenericDebugPage__wrapper":
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
        """public dev.ultreon.quantum.client.gui.debug.GenericDebugPage()"""
        val = _GenericDebugPage()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def render(self, arg0: 'DebugPageContext'):
        """public void dev.ultreon.quantum.client.gui.debug.GenericDebugPage.render(dev.ultreon.quantum.client.gui.debug.DebugPageContext)"""
        super(_GenericDebugPage, self).render(arg0)

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
        """public dev.ultreon.quantum.client.gui.debug.GenericDebugPage()"""
        val = _GenericDebugPage()
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


DebugPage.EMPTY = DebugPage._wrap(_EMPTY.EMPTY)