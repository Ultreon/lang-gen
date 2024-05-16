from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pycorelibs.registries import v0
except ImportError:
    v0 = _import_once("pycorelibs.registries.v0")

from abc import abstractmethod, ABC
import dev.ultreon.libs.registries.v0.event.RegistryEvents as _RegistryEvents_AutoRegister
_AutoRegister = _RegistryEvents_AutoRegister.AutoRegister
 
class AutoRegister():
    """dev.ultreon.libs.registries.v0.event.RegistryEvents.AutoRegister"""
 
    @staticmethod
    def _wrap(java_value: _AutoRegister) -> 'AutoRegister':
        return AutoRegister(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AutoRegister):
        """
        Dynamic initializer for AutoRegister.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AutoRegister__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AutoRegister__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onAutoRegister(self, arg0: 'Registry'):
        """public abstract void dev.ultreon.libs.registries.v0.event.RegistryEvents$AutoRegister.onAutoRegister(dev.ultreon.libs.registries.v0.Registry<?>)"""
        pass

 
 
 
# CLASS: dev.ultreon.libs.registries.v0.event.RegistryEvents$AutoRegister
from pyquantum_helper import import_once as _import_once
try:
    from pycorelibs.registries import v0
except ImportError:
    v0 = _import_once("pycorelibs.registries.v0")

from abc import abstractmethod, ABC
import dev.ultreon.libs.registries.v0.event.RegistryEvents as _RegistryEvents_AutoRegister
_AutoRegister = _RegistryEvents_AutoRegister.AutoRegister
 
class AutoRegister():
    """dev.ultreon.libs.registries.v0.event.RegistryEvents.AutoRegister"""
 
    @staticmethod
    def _wrap(java_value: _AutoRegister) -> 'AutoRegister':
        return AutoRegister(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AutoRegister):
        """
        Dynamic initializer for AutoRegister.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AutoRegister__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AutoRegister__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onAutoRegister(self, arg0: 'Registry'):
        """public abstract void dev.ultreon.libs.registries.v0.event.RegistryEvents$AutoRegister.onAutoRegister(dev.ultreon.libs.registries.v0.Registry<?>)"""
        pass

 
 
 
# CLASS: dev.ultreon.libs.registries.v0.event.RegistryEvents$AutoRegister 
 
 
# CLASS: dev.ultreon.libs.registries.v0.event.RegistryEvents$RegistryDump
from abc import abstractmethod, ABC
import dev.ultreon.libs.registries.v0.event.RegistryEvents as _RegistryEvents_RegistryDump
_RegistryDump = _RegistryEvents_RegistryDump.RegistryDump
 
class RegistryDump():
    """dev.ultreon.libs.registries.v0.event.RegistryEvents.RegistryDump"""
 
    @staticmethod
    def _wrap(java_value: _RegistryDump) -> 'RegistryDump':
        return RegistryDump(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RegistryDump):
        """
        Dynamic initializer for RegistryDump.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RegistryDump__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RegistryDump__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onRegistryDump(self, ):
        """public abstract void dev.ultreon.libs.registries.v0.event.RegistryEvents$RegistryDump.onRegistryDump()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.registries.v0.event.RegistryEvents
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
import dev.ultreon.libs.registries.v0.event.RegistryEvents as _RegistryEvents
_RegistryEvents = _RegistryEvents
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RegistryEvents():
    """dev.ultreon.libs.registries.v0.event.RegistryEvents"""
 
    @staticmethod
    def _wrap(java_value: _RegistryEvents) -> 'RegistryEvents':
        return RegistryEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RegistryEvents):
        """
        Dynamic initializer for RegistryEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RegistryEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RegistryEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
        """public dev.ultreon.libs.registries.v0.event.RegistryEvents()"""
        val = _RegistryEvents()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.registries.v0.event.RegistryEvents()"""
        val = _RegistryEvents()
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