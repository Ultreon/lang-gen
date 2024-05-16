from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

import dev.ultreon.quantum.server.events.ServerLifecycleEvents as __ServerLifecycleEvents_ServerStopping
__ServerStopping = __ServerLifecycleEvents_ServerStopping.ServerStopping
from abc import abstractmethod, ABC
 
class ServerStopping(ABC):
    """dev.ultreon.quantum.server.events.ServerLifecycleEvents.ServerStopping"""
 
    @staticmethod
    def __wrap(java_value: __ServerStopping) -> 'ServerStopping':
        return ServerStopping(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerStopping):
        """
        Dynamic initializer for ServerStopping.
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
    def onServerStopping(self, arg0: 'QuantumServer'):
        """public abstract void dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopping.onServerStopping(dev.ultreon.quantum.server.QuantumServer)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopping
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

import dev.ultreon.quantum.server.events.ServerLifecycleEvents as __ServerLifecycleEvents_ServerStopping
__ServerStopping = __ServerLifecycleEvents_ServerStopping.ServerStopping
from abc import abstractmethod, ABC
 
class ServerStopping(ABC):
    """dev.ultreon.quantum.server.events.ServerLifecycleEvents.ServerStopping"""
 
    @staticmethod
    def __wrap(java_value: __ServerStopping) -> 'ServerStopping':
        return ServerStopping(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerStopping):
        """
        Dynamic initializer for ServerStopping.
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
    def onServerStopping(self, arg0: 'QuantumServer'):
        """public abstract void dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopping.onServerStopping(dev.ultreon.quantum.server.QuantumServer)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopping 
 
 
# CLASS: dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopped
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

import dev.ultreon.quantum.server.events.ServerLifecycleEvents as __ServerLifecycleEvents_ServerStopped
__ServerStopped = __ServerLifecycleEvents_ServerStopped.ServerStopped
from abc import abstractmethod, ABC
 
class ServerStopped(ABC):
    """dev.ultreon.quantum.server.events.ServerLifecycleEvents.ServerStopped"""
 
    @staticmethod
    def __wrap(java_value: __ServerStopped) -> 'ServerStopped':
        return ServerStopped(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerStopped):
        """
        Dynamic initializer for ServerStopped.
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
    def onServerStopped(self, arg0: 'QuantumServer'):
        """public abstract void dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopped.onServerStopped(dev.ultreon.quantum.server.QuantumServer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStarting
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.server.events.ServerLifecycleEvents as __ServerLifecycleEvents_ServerStarting
__ServerStarting = __ServerLifecycleEvents_ServerStarting.ServerStarting
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

from abc import abstractmethod, ABC
 
class ServerStarting(ABC):
    """dev.ultreon.quantum.server.events.ServerLifecycleEvents.ServerStarting"""
 
    @staticmethod
    def __wrap(java_value: __ServerStarting) -> 'ServerStarting':
        return ServerStarting(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerStarting):
        """
        Dynamic initializer for ServerStarting.
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
    def onServerStarting(self, arg0: 'QuantumServer'):
        """public abstract void dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStarting.onServerStarting(dev.ultreon.quantum.server.QuantumServer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStarted
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

import dev.ultreon.quantum.server.events.ServerLifecycleEvents as __ServerLifecycleEvents_ServerStarted
__ServerStarted = __ServerLifecycleEvents_ServerStarted.ServerStarted
from abc import abstractmethod, ABC
 
class ServerStarted(ABC):
    """dev.ultreon.quantum.server.events.ServerLifecycleEvents.ServerStarted"""
 
    @staticmethod
    def __wrap(java_value: __ServerStarted) -> 'ServerStarted':
        return ServerStarted(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerStarted):
        """
        Dynamic initializer for ServerStarted.
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
    def onServerStarted(self, arg0: 'QuantumServer'):
        """public abstract void dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStarted.onServerStarted(dev.ultreon.quantum.server.QuantumServer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.server.events.ServerLifecycleEvents
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.server.events.ServerLifecycleEvents as __ServerLifecycleEvents
__ServerLifecycleEvents = __ServerLifecycleEvents
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
 
class ServerLifecycleEvents():
    """dev.ultreon.quantum.server.events.ServerLifecycleEvents"""
 
    @staticmethod
    def __wrap(java_value: __ServerLifecycleEvents) -> 'ServerLifecycleEvents':
        return ServerLifecycleEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerLifecycleEvents):
        """
        Dynamic initializer for ServerLifecycleEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStarting> dev.ultreon.quantum.server.events.ServerLifecycleEvents.SERVER_STARTING
    SERVER_STARTING: 'api.Event' = __wrap(__api.Event.SERVER_STARTING)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopped> dev.ultreon.quantum.server.events.ServerLifecycleEvents.SERVER_STOPPED
    SERVER_STOPPED: 'api.Event' = __wrap(__api.Event.SERVER_STOPPED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStopping> dev.ultreon.quantum.server.events.ServerLifecycleEvents.SERVER_STOPPING
    SERVER_STOPPING: 'api.Event' = __wrap(__api.Event.SERVER_STOPPING)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.server.events.ServerLifecycleEvents$ServerStarted> dev.ultreon.quantum.server.events.ServerLifecycleEvents.SERVER_STARTED
    SERVER_STARTED: 'api.Event' = __wrap(__api.Event.SERVER_STARTED)


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
        """public dev.ultreon.quantum.server.events.ServerLifecycleEvents()"""
        val = __ServerLifecycleEvents()
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
        """public dev.ultreon.quantum.server.events.ServerLifecycleEvents()"""
        val = __ServerLifecycleEvents()
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