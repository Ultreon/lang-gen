from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

import dev.ultreon.quantum.server.events.ServerLifecycleEvents as _ServerLifecycleEvents_ServerStopping
_ServerStopping = _ServerLifecycleEvents_ServerStopping.ServerStopping
from abc import abstractmethod, ABC
 
class ServerStopping():
    """dev.ultreon.quantum.server.events.ServerLifecycleEvents.ServerStopping"""
 
    @staticmethod
    def _wrap(java_value: _ServerStopping) -> 'ServerStopping':
        return ServerStopping(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerStopping):
        """
        Dynamic initializer for ServerStopping.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerStopping__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerStopping__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onServerStopping(self, arg0: 'QuantumServer'):
        """public abstract void dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopping.onServerStopping(dev.ultreon.quantum.server.QuantumServer)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopping
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

import dev.ultreon.quantum.server.events.ServerLifecycleEvents as _ServerLifecycleEvents_ServerStopping
_ServerStopping = _ServerLifecycleEvents_ServerStopping.ServerStopping
from abc import abstractmethod, ABC
 
class ServerStopping():
    """dev.ultreon.quantum.server.events.ServerLifecycleEvents.ServerStopping"""
 
    @staticmethod
    def _wrap(java_value: _ServerStopping) -> 'ServerStopping':
        return ServerStopping(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerStopping):
        """
        Dynamic initializer for ServerStopping.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerStopping__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerStopping__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onServerStopping(self, arg0: 'QuantumServer'):
        """public abstract void dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopping.onServerStopping(dev.ultreon.quantum.server.QuantumServer)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopping 
 
 
# CLASS: dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopped
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

import dev.ultreon.quantum.server.events.ServerLifecycleEvents as _ServerLifecycleEvents_ServerStopped
_ServerStopped = _ServerLifecycleEvents_ServerStopped.ServerStopped
from abc import abstractmethod, ABC
 
class ServerStopped():
    """dev.ultreon.quantum.server.events.ServerLifecycleEvents.ServerStopped"""
 
    @staticmethod
    def _wrap(java_value: _ServerStopped) -> 'ServerStopped':
        return ServerStopped(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerStopped):
        """
        Dynamic initializer for ServerStopped.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerStopped__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerStopped__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onServerStopped(self, arg0: 'QuantumServer'):
        """public abstract void dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopped.onServerStopped(dev.ultreon.quantum.server.QuantumServer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStarting
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

import dev.ultreon.quantum.server.events.ServerLifecycleEvents as _ServerLifecycleEvents_ServerStarting
_ServerStarting = _ServerLifecycleEvents_ServerStarting.ServerStarting
from abc import abstractmethod, ABC
 
class ServerStarting():
    """dev.ultreon.quantum.server.events.ServerLifecycleEvents.ServerStarting"""
 
    @staticmethod
    def _wrap(java_value: _ServerStarting) -> 'ServerStarting':
        return ServerStarting(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerStarting):
        """
        Dynamic initializer for ServerStarting.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerStarting__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerStarting__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onServerStarting(self, arg0: 'QuantumServer'):
        """public abstract void dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStarting.onServerStarting(dev.ultreon.quantum.server.QuantumServer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStarted
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.server.events.ServerLifecycleEvents as _ServerLifecycleEvents_ServerStarted
_ServerStarted = _ServerLifecycleEvents_ServerStarted.ServerStarted
 
class ServerStarted():
    """dev.ultreon.quantum.server.events.ServerLifecycleEvents.ServerStarted"""
 
    @staticmethod
    def _wrap(java_value: _ServerStarted) -> 'ServerStarted':
        return ServerStarted(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerStarted):
        """
        Dynamic initializer for ServerStarted.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerStarted__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerStarted__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onServerStarted(self, arg0: 'QuantumServer'):
        """public abstract void dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStarted.onServerStarted(dev.ultreon.quantum.server.QuantumServer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.server.events.ServerLifecycleEvents
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.events import api
except ImportError:
    api = _import_once("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.server.events.ServerLifecycleEvents as _ServerLifecycleEvents
_ServerLifecycleEvents = _ServerLifecycleEvents
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
 
class ServerLifecycleEvents():
    """dev.ultreon.quantum.server.events.ServerLifecycleEvents"""
 
    @staticmethod
    def _wrap(java_value: _ServerLifecycleEvents) -> 'ServerLifecycleEvents':
        return ServerLifecycleEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerLifecycleEvents):
        """
        Dynamic initializer for ServerLifecycleEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerLifecycleEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerLifecycleEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStarting> dev.ultreon.quantum.server.events.ServerLifecycleEvents.SERVER_STARTING
    SERVER_STARTING: 'api.Event' = _wrap(_api.Event.SERVER_STARTING)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopped> dev.ultreon.quantum.server.events.ServerLifecycleEvents.SERVER_STOPPED
    SERVER_STOPPED: 'api.Event' = _wrap(_api.Event.SERVER_STOPPED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStarted> dev.ultreon.quantum.server.events.ServerLifecycleEvents.SERVER_STARTED
    SERVER_STARTED: 'api.Event' = _wrap(_api.Event.SERVER_STARTED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopping> dev.ultreon.quantum.server.events.ServerLifecycleEvents.SERVER_STOPPING
    SERVER_STOPPING: 'api.Event' = _wrap(_api.Event.SERVER_STOPPING)


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
        """public dev.ultreon.quantum.server.events.ServerLifecycleEvents()"""
        val = _ServerLifecycleEvents()
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
        """public dev.ultreon.quantum.server.events.ServerLifecycleEvents()"""
        val = _ServerLifecycleEvents()
        self.__wrapper = val