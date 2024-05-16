from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.registry.event.RegistryEvents as _RegistryEvents_RegistryDump
_RegistryDump = _RegistryEvents_RegistryDump.RegistryDump
from abc import abstractmethod, ABC
 
class RegistryDump():
    """dev.ultreon.quantum.registry.event.RegistryEvents.RegistryDump"""
 
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
        """public abstract void dev.ultreon.quantum.registry.event.RegistryEvents$RegistryDump.onRegistryDump()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.registry.event.RegistryEvents$RegistryDump
import dev.ultreon.quantum.registry.event.RegistryEvents as _RegistryEvents_RegistryDump
_RegistryDump = _RegistryEvents_RegistryDump.RegistryDump
from abc import abstractmethod, ABC
 
class RegistryDump():
    """dev.ultreon.quantum.registry.event.RegistryEvents.RegistryDump"""
 
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
        """public abstract void dev.ultreon.quantum.registry.event.RegistryEvents$RegistryDump.onRegistryDump()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.registry.event.RegistryEvents$RegistryDump 
 
 
# CLASS: dev.ultreon.quantum.registry.event.RegistryEvents
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
import dev.ultreon.quantum.registry.event.RegistryEvents as _RegistryEvents
_RegistryEvents = _RegistryEvents
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RegistryEvents():
    """dev.ultreon.quantum.registry.event.RegistryEvents"""
 
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.registry.event.RegistryEvents$RegistryCreation> dev.ultreon.quantum.registry.event.RegistryEvents.REGISTRY_CREATION
    REGISTRY_CREATION: 'api.Event' = _wrap(_api.Event.REGISTRY_CREATION)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.registry.event.RegistryEvents$AutoRegister> dev.ultreon.quantum.registry.event.RegistryEvents.AUTO_REGISTER
    AUTO_REGISTER: 'api.Event' = _wrap(_api.Event.AUTO_REGISTER)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.registry.event.RegistryEvents$RegistryDump> dev.ultreon.quantum.registry.event.RegistryEvents.REGISTRY_DUMP
    REGISTRY_DUMP: 'api.Event' = _wrap(_api.Event.REGISTRY_DUMP)


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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.registry.event.RegistryEvents()"""
        val = _RegistryEvents()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.registry.event.RegistryEvents()"""
        val = _RegistryEvents()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.registry.event.RegistryEvents$AutoRegister
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import registry
except ImportError:
    registry = _import_once("pyquantum.registry")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.registry.event.RegistryEvents as _RegistryEvents_AutoRegister
_AutoRegister = _RegistryEvents_AutoRegister.AutoRegister
 
class AutoRegister():
    """dev.ultreon.quantum.registry.event.RegistryEvents.AutoRegister"""
 
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
    def onAutoRegister(self, arg0: str, arg1: 'Registry'):
        """public abstract void dev.ultreon.quantum.registry.event.RegistryEvents$AutoRegister.onAutoRegister(java.lang.String,dev.ultreon.quantum.registry.Registry<?>)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.registry.event.RegistryEvents$RegistryCreation
import dev.ultreon.quantum.registry.event.RegistryEvents as _RegistryEvents_RegistryCreation
_RegistryCreation = _RegistryEvents_RegistryCreation.RegistryCreation
from abc import abstractmethod, ABC
 
class RegistryCreation():
    """dev.ultreon.quantum.registry.event.RegistryEvents.RegistryCreation"""
 
    @staticmethod
    def _wrap(java_value: _RegistryCreation) -> 'RegistryCreation':
        return RegistryCreation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RegistryCreation):
        """
        Dynamic initializer for RegistryCreation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RegistryCreation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RegistryCreation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onRegistryCreation(self, ):
        """public abstract void dev.ultreon.quantum.registry.event.RegistryEvents$RegistryCreation.onRegistryCreation()"""
        pass