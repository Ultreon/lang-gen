from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.network.api.NetworkManager as __NetworkManager
__NetworkManager = __NetworkManager
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NetworkManager():
    """dev.ultreon.quantum.network.api.NetworkManager"""
 
    @staticmethod
    def __wrap(java_value: __NetworkManager) -> 'NetworkManager':
        return NetworkManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NetworkManager):
        """
        Dynamic initializer for NetworkManager.
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

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.network.api.NetworkManager.init()"""
            __NetworkManager.init()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def registerNetwork(arg0: 'Network'):
        """public static void dev.ultreon.quantum.network.api.NetworkManager.registerNetwork(dev.ultreon.quantum.network.api.Network)"""
        __NetworkManager.registerNetwork(arg0)

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.api.NetworkManager()"""
        val = __NetworkManager()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.NetworkManager()"""
        val = __NetworkManager()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.network.api.NetworkManager
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.network.api.NetworkManager as __NetworkManager
__NetworkManager = __NetworkManager
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NetworkManager():
    """dev.ultreon.quantum.network.api.NetworkManager"""
 
    @staticmethod
    def __wrap(java_value: __NetworkManager) -> 'NetworkManager':
        return NetworkManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NetworkManager):
        """
        Dynamic initializer for NetworkManager.
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

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.network.api.NetworkManager.init()"""
            __NetworkManager.init()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def registerNetwork(arg0: 'Network'):
        """public static void dev.ultreon.quantum.network.api.NetworkManager.registerNetwork(dev.ultreon.quantum.network.api.Network)"""
        __NetworkManager.registerNetwork(arg0)

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.api.NetworkManager()"""
        val = __NetworkManager()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.NetworkManager()"""
        val = __NetworkManager()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.network.api.NetworkManager 
 
 
# CLASS: dev.ultreon.quantum.network.api.NetworkContext
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.network.api.NetworkContext as __NetworkContext
__NetworkContext = __NetworkContext
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import dev.ultreon.quantum.network.system.IConnection as __IConnection
__IConnection = __IConnection
import dev.ultreon.quantum.network.api.PacketDestination as __PacketDestination
__PacketDestination = __PacketDestination
import dev.ultreon.quantum.server.player.ServerPlayer as __ServerPlayer
__ServerPlayer = __ServerPlayer
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.network.PacketIO as __PacketIO
__PacketIO = __PacketIO
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
 
class NetworkContext():
    """dev.ultreon.quantum.network.api.NetworkContext"""
 
    @staticmethod
    def __wrap(java_value: __NetworkContext) -> 'NetworkContext':
        return NetworkContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NetworkContext):
        """
        Dynamic initializer for NetworkContext.
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

    @overload
    def buffer(self) -> 'network.PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.api.NetworkContext.buffer()"""
        return 'network.PacketIO'.__wrap(super(NetworkContext, self).buffer())

    @overload
    def __init__(self, arg0: 'PacketIO', arg1: 'PacketDestination', arg2: 'IConnection', arg3: 'ServerPlayer'):
        """public dev.ultreon.quantum.network.api.NetworkContext(dev.ultreon.quantum.network.PacketIO,dev.ultreon.quantum.network.api.PacketDestination,dev.ultreon.quantum.network.system.IConnection,dev.ultreon.quantum.server.player.ServerPlayer)"""
        val = __NetworkContext(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def connection(self) -> 'system.IConnection':
        """public dev.ultreon.quantum.network.system.IConnection dev.ultreon.quantum.network.api.NetworkContext.connection()"""
        return 'system.IConnection'.__wrap(super(NetworkContext, self).connection())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def direction(self) -> 'PacketDestination':
        """public dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.api.NetworkContext.direction()"""
        return 'PacketDestination'.__wrap(super(NetworkContext, self).direction())

    @overload
    def enqueueWork(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.api.NetworkContext.enqueueWork(java.lang.Runnable)"""
        super(__NetworkContext, self).enqueueWork(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.api.NetworkContext.hashCode()"""
        return int.__wrap(super(NetworkContext, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.api.NetworkContext.equals(java.lang.Object)"""
        return bool.__wrap(super(__NetworkContext, self).equals(arg0))

    @overload
    def sender(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.network.api.NetworkContext.sender()"""
        return 'player.ServerPlayer'.__wrap(super(NetworkContext, self).sender())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.api.NetworkContext.toString()"""
        return str.__wrap(super(NetworkContext, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.network.api.PacketDestination
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.util.Env as __Env
__Env = __Env
from typing import List
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Enum as Enum
import dev.ultreon.quantum.network.api.PacketDestination as __PacketDestination
__PacketDestination = __PacketDestination
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class PacketDestination(__Enum, Enum):
    """dev.ultreon.quantum.network.api.PacketDestination"""
 
    @staticmethod
    def __wrap(java_value: __PacketDestination) -> 'PacketDestination':
        return PacketDestination(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketDestination):
        """
        Dynamic initializer for PacketDestination.
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
 
    # public static final dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.api.PacketDestination.SERVER
    SERVER: 'PacketDestination' = __wrap(__PacketDestination.SERVER)

    # public static final dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.api.PacketDestination.CLIENT
    CLIENT: 'PacketDestination' = __wrap(__PacketDestination.CLIENT)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def opposite(self) -> 'PacketDestination':
        """public dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.api.PacketDestination.opposite()"""
        return 'PacketDestination'.__wrap(super(PacketDestination, self).opposite())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def values() -> List['PacketDestination']:
        """public static dev.ultreon.quantum.network.api.PacketDestination[] dev.ultreon.quantum.network.api.PacketDestination.values()"""
        return List[PacketDestination].__wrap(__PacketDestination.values())

    @overload
    def getSourceEnv(self) -> 'util.Env':
        """public dev.ultreon.quantum.util.Env dev.ultreon.quantum.network.api.PacketDestination.getSourceEnv()"""
        return 'util.Env'.__wrap(super(PacketDestination, self).getSourceEnv())

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'PacketDestination':
        """public static dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.api.PacketDestination.valueOf(java.lang.String)"""
        return PacketDestination.__wrap(__PacketDestination.valueOf(arg0))

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @overload
    def getDestinationEnv(self) -> 'util.Env':
        """public dev.ultreon.quantum.util.Env dev.ultreon.quantum.network.api.PacketDestination.getDestinationEnv()"""
        return 'util.Env'.__wrap(super(PacketDestination, self).getDestinationEnv())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.network.api.PacketRegisterContext
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.network.api import packet
except ImportError:
    packet = __import_once__("pyquantum.network.api.packet")

import dev.ultreon.quantum.network.api.PacketRegisterContext as __PacketRegisterContext
__PacketRegisterContext = __PacketRegisterContext
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.function.Function as Function
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PacketRegisterContext():
    """dev.ultreon.quantum.network.api.PacketRegisterContext"""
 
    @staticmethod
    def __wrap(java_value: __PacketRegisterContext) -> 'PacketRegisterContext':
        return PacketRegisterContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketRegisterContext):
        """
        Dynamic initializer for PacketRegisterContext.
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
    def register(self, arg0: 'Function', *arg1: 'packet.ModPacket') -> int:
        """public final <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T>> int dev.ultreon.quantum.network.api.PacketRegisterContext.register(java.util.function.Function<dev.ultreon.quantum.network.PacketIO, T>,T...)"""
        return int.__wrap(super(__PacketRegisterContext, self).register(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.api.Network
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.network.api import packet
except ImportError:
    packet = __import_once__("pyquantum.network.api.packet")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.network.api.Network as __Network
__Network = __Network
from builtins import int
 
class Network(ABC):
    """dev.ultreon.quantum.network.api.Network"""
 
    @staticmethod
    def __wrap(java_value: __Network) -> 'Network':
        return Network(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Network):
        """
        Dynamic initializer for Network.
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

    @overload
    def channelName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.network.api.Network.channelName()"""
        return str.__wrap(super(Network, self).channelName())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def sendToClient(self, arg0: 'ModPacket', arg1: 'ServerPlayer'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ClientEndpoint> void dev.ultreon.quantum.network.api.Network.sendToClient(dev.ultreon.quantum.network.api.packet.ModPacket<T>,dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__Network, self).sendToClient(arg0, arg1)

    @overload
    def sendToServer(self, arg0: 'ModPacket'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ServerEndpoint> void dev.ultreon.quantum.network.api.Network.sendToServer(T)"""
        super(__Network, self).sendToServer(arg0)

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getId(self) -> 'util.Identifier':
        """public final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.network.api.Network.getId()"""
        return 'util.Identifier'.__wrap(super(Network, self).getId())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def namespace(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.network.api.Network.namespace()"""
        return str.__wrap(super(Network, self).namespace())

    @overload
    def init(self):
        """public final void dev.ultreon.quantum.network.api.Network.init()"""
        super(Network, self).init()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))