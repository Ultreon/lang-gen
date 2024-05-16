from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.api.NetworkManager as _NetworkManager
_NetworkManager = _NetworkManager
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NetworkManager():
    """dev.ultreon.quantum.network.api.NetworkManager"""
 
    @staticmethod
    def _wrap(java_value: _NetworkManager) -> 'NetworkManager':
        return NetworkManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NetworkManager):
        """
        Dynamic initializer for NetworkManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NetworkManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NetworkManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.network.api.NetworkManager.init()"""
            _NetworkManager.init()

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

    @staticmethod
    @overload
    def registerNetwork(arg0: 'Network'):
        """public static void dev.ultreon.quantum.network.api.NetworkManager.registerNetwork(dev.ultreon.quantum.network.api.Network)"""
        _NetworkManager.registerNetwork(arg0)

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
        """public dev.ultreon.quantum.network.api.NetworkManager()"""
        val = _NetworkManager()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.NetworkManager()"""
        val = _NetworkManager()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.network.api.NetworkManager
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.api.NetworkManager as _NetworkManager
_NetworkManager = _NetworkManager
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NetworkManager():
    """dev.ultreon.quantum.network.api.NetworkManager"""
 
    @staticmethod
    def _wrap(java_value: _NetworkManager) -> 'NetworkManager':
        return NetworkManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NetworkManager):
        """
        Dynamic initializer for NetworkManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NetworkManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NetworkManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.network.api.NetworkManager.init()"""
            _NetworkManager.init()

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

    @staticmethod
    @overload
    def registerNetwork(arg0: 'Network'):
        """public static void dev.ultreon.quantum.network.api.NetworkManager.registerNetwork(dev.ultreon.quantum.network.api.Network)"""
        _NetworkManager.registerNetwork(arg0)

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
        """public dev.ultreon.quantum.network.api.NetworkManager()"""
        val = _NetworkManager()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.NetworkManager()"""
        val = _NetworkManager()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.network.api.NetworkManager 
 
 
# CLASS: dev.ultreon.quantum.network.api.NetworkContext
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.system.IConnection as _IConnection
_IConnection = _IConnection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.api.NetworkContext as _NetworkContext
_NetworkContext = _NetworkContext
import dev.ultreon.quantum.network.PacketIO as _PacketIO
_PacketIO = _PacketIO
import java.lang.Runnable as Runnable
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.server.player.ServerPlayer as _ServerPlayer
_ServerPlayer = _ServerPlayer
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.network.api.PacketDestination as _PacketDestination
_PacketDestination = _PacketDestination
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NetworkContext():
    """dev.ultreon.quantum.network.api.NetworkContext"""
 
    @staticmethod
    def _wrap(java_value: _NetworkContext) -> 'NetworkContext':
        return NetworkContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NetworkContext):
        """
        Dynamic initializer for NetworkContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NetworkContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NetworkContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def enqueueWork(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.api.NetworkContext.enqueueWork(java.lang.Runnable)"""
        super(_NetworkContext, self).enqueueWork(arg0)

    @overload
    def connection(self) -> 'system.IConnection':
        """public dev.ultreon.quantum.network.system.IConnection dev.ultreon.quantum.network.api.NetworkContext.connection()"""
        return 'system.IConnection'._wrap(super(NetworkContext, self).connection())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.api.NetworkContext.equals(java.lang.Object)"""
        return bool._wrap(super(_NetworkContext, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.api.NetworkContext.hashCode()"""
        return int._wrap(super(NetworkContext, self).hashCode())

    @overload
    def direction(self) -> 'PacketDestination':
        """public dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.api.NetworkContext.direction()"""
        return 'PacketDestination'._wrap(super(NetworkContext, self).direction())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'PacketIO', arg1: 'PacketDestination', arg2: 'IConnection', arg3: 'ServerPlayer'):
        """public dev.ultreon.quantum.network.api.NetworkContext(dev.ultreon.quantum.network.PacketIO,dev.ultreon.quantum.network.api.PacketDestination,dev.ultreon.quantum.network.system.IConnection,dev.ultreon.quantum.server.player.ServerPlayer)"""
        val = _NetworkContext(arg0, arg1, arg2, arg3)
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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.api.NetworkContext.toString()"""
        return str._wrap(super(NetworkContext, self).toString())

    @overload
    def buffer(self) -> 'network.PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.api.NetworkContext.buffer()"""
        return 'network.PacketIO'._wrap(super(NetworkContext, self).buffer())

    @overload
    def sender(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.network.api.NetworkContext.sender()"""
        return 'player.ServerPlayer'._wrap(super(NetworkContext, self).sender())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.network.api.PacketDestination
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.util.Env as _Env
_Env = _Env
from typing import List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import dev.ultreon.quantum.network.api.PacketDestination as _PacketDestination
_PacketDestination = _PacketDestination
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketDestination():
    """dev.ultreon.quantum.network.api.PacketDestination"""
 
    @staticmethod
    def _wrap(java_value: _PacketDestination) -> 'PacketDestination':
        return PacketDestination(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketDestination):
        """
        Dynamic initializer for PacketDestination.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketDestination__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketDestination__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'PacketDestination':
        """public static dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.api.PacketDestination.valueOf(java.lang.String)"""
        return PacketDestination._wrap(_PacketDestination.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getSourceEnv(self) -> 'util.Env':
        """public dev.ultreon.quantum.util.Env dev.ultreon.quantum.network.api.PacketDestination.getSourceEnv()"""
        return 'util.Env'._wrap(super(PacketDestination, self).getSourceEnv())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def opposite(self) -> 'PacketDestination':
        """public dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.api.PacketDestination.opposite()"""
        return 'PacketDestination'._wrap(super(PacketDestination, self).opposite())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @overload
    def getDestinationEnv(self) -> 'util.Env':
        """public dev.ultreon.quantum.util.Env dev.ultreon.quantum.network.api.PacketDestination.getDestinationEnv()"""
        return 'util.Env'._wrap(super(PacketDestination, self).getDestinationEnv())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def values() -> List['PacketDestination']:
        """public static dev.ultreon.quantum.network.api.PacketDestination[] dev.ultreon.quantum.network.api.PacketDestination.values()"""
        return List[PacketDestination]._wrap(_PacketDestination.values())


PacketDestination.SERVER = PacketDestination._wrap(_SERVER.SERVER)

PacketDestination.CLIENT = PacketDestination._wrap(_CLIENT.CLIENT) 
 
 
# CLASS: dev.ultreon.quantum.network.api.PacketRegisterContext
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network.api import packet
except ImportError:
    packet = _import_once("pyquantum.network.api.packet")

import dev.ultreon.quantum.network.api.PacketRegisterContext as _PacketRegisterContext
_PacketRegisterContext = _PacketRegisterContext
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketRegisterContext():
    """dev.ultreon.quantum.network.api.PacketRegisterContext"""
 
    @staticmethod
    def _wrap(java_value: _PacketRegisterContext) -> 'PacketRegisterContext':
        return PacketRegisterContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketRegisterContext):
        """
        Dynamic initializer for PacketRegisterContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketRegisterContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketRegisterContext__wrapper":
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
    def register(self, arg0: 'Function', *arg1: 'packet.ModPacket') -> int:
        """public final <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T>> int dev.ultreon.quantum.network.api.PacketRegisterContext.register(java.util.function.Function<dev.ultreon.quantum.network.PacketIO, T>,T...)"""
        return int._wrap(super(_PacketRegisterContext, self).register(arg0, arg1))

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
 
 
# CLASS: dev.ultreon.quantum.network.api.Network
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.network.api.Network as _Network
_Network = _Network
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network.api import packet
except ImportError:
    packet = _import_once("pyquantum.network.api.packet")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Network():
    """dev.ultreon.quantum.network.api.Network"""
 
    @staticmethod
    def _wrap(java_value: _Network) -> 'Network':
        return Network(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Network):
        """
        Dynamic initializer for Network.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Network__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Network__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def channelName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.network.api.Network.channelName()"""
        return str._wrap(super(Network, self).channelName())

    @overload
    def getId(self) -> 'util.Identifier':
        """public final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.network.api.Network.getId()"""
        return 'util.Identifier'._wrap(super(Network, self).getId())

    @overload
    def sendToServer(self, arg0: 'ModPacket'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ServerEndpoint> void dev.ultreon.quantum.network.api.Network.sendToServer(T)"""
        super(_Network, self).sendToServer(arg0)

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def init(self):
        """public final void dev.ultreon.quantum.network.api.Network.init()"""
        super(Network, self).init()

    @overload
    def namespace(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.network.api.Network.namespace()"""
        return str._wrap(super(Network, self).namespace())

    @overload
    def sendToClient(self, arg0: 'ModPacket', arg1: 'ServerPlayer'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ClientEndpoint> void dev.ultreon.quantum.network.api.Network.sendToClient(dev.ultreon.quantum.network.api.packet.ModPacket<T>,dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_Network, self).sendToClient(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())