from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pycorelibs.registries import v0
except ImportError:
    v0 = __import_once__("pycorelibs.registries.v0")

import dev.ultreon.libs.registries.v0.event.RegistryEvents as __RegistryEvents_AutoRegister
__AutoRegister = __RegistryEvents_AutoRegister.AutoRegister
from abc import abstractmethod, ABC
 
class AutoRegister(ABC):
    """dev.ultreon.libs.registries.v0.event.RegistryEvents.AutoRegister"""
 
    @staticmethod
    def __wrap(java_value: __AutoRegister) -> 'AutoRegister':
        return AutoRegister(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AutoRegister):
        """
        Dynamic initializer for AutoRegister.
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
    def onAutoRegister(self, arg0: 'Registry'):
        """public abstract void dev.ultreon.libs.registries.v0.event.RegistryEvents$AutoRegister.onAutoRegister(dev.ultreon.libs.registries.v0.Registry<?>)"""
        pass

 
 
 
# CLASS: dev.ultreon.libs.registries.v0.event.RegistryEvents$AutoRegister
from pyquantum_helper import import_once as __import_once__
try:
    from pycorelibs.registries import v0
except ImportError:
    v0 = __import_once__("pycorelibs.registries.v0")

import dev.ultreon.libs.registries.v0.event.RegistryEvents as __RegistryEvents_AutoRegister
__AutoRegister = __RegistryEvents_AutoRegister.AutoRegister
from abc import abstractmethod, ABC
 
class AutoRegister(ABC):
    """dev.ultreon.libs.registries.v0.event.RegistryEvents.AutoRegister"""
 
    @staticmethod
    def __wrap(java_value: __AutoRegister) -> 'AutoRegister':
        return AutoRegister(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AutoRegister):
        """
        Dynamic initializer for AutoRegister.
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
    def onAutoRegister(self, arg0: 'Registry'):
        """public abstract void dev.ultreon.libs.registries.v0.event.RegistryEvents$AutoRegister.onAutoRegister(dev.ultreon.libs.registries.v0.Registry<?>)"""
        pass

 
 
 
# CLASS: dev.ultreon.libs.registries.v0.event.RegistryEvents$AutoRegister 
 
 
# CLASS: dev.ultreon.libs.registries.v0.event.RegistryEvents$RegistryDump
import dev.ultreon.libs.registries.v0.event.RegistryEvents as __RegistryEvents_RegistryDump
__RegistryDump = __RegistryEvents_RegistryDump.RegistryDump
from abc import abstractmethod, ABC
 
class RegistryDump(ABC):
    """dev.ultreon.libs.registries.v0.event.RegistryEvents.RegistryDump"""
 
    @staticmethod
    def __wrap(java_value: __RegistryDump) -> 'RegistryDump':
        return RegistryDump(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegistryDump):
        """
        Dynamic initializer for RegistryDump.
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
    def onRegistryDump(self, ):
        """public abstract void dev.ultreon.libs.registries.v0.event.RegistryEvents$RegistryDump.onRegistryDump()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.registries.v0.event.RegistryEvents
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
import dev.ultreon.libs.registries.v0.event.RegistryEvents as __RegistryEvents
__RegistryEvents = __RegistryEvents
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RegistryEvents():
    """dev.ultreon.libs.registries.v0.event.RegistryEvents"""
 
    @staticmethod
    def __wrap(java_value: __RegistryEvents) -> 'RegistryEvents':
        return RegistryEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegistryEvents):
        """
        Dynamic initializer for RegistryEvents.
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
    def __init__(self, ):
        """public dev.ultreon.libs.registries.v0.event.RegistryEvents()"""
        val = __RegistryEvents()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.libs.registries.v0.event.RegistryEvents()"""
        val = __RegistryEvents()
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))