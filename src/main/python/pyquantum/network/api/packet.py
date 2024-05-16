from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.api.packet.ModPacket as _ModPacket
_ModPacket = _ModPacket
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModPacket():
    """dev.ultreon.quantum.network.api.packet.ModPacket"""
 
    @staticmethod
    def _wrap(java_value: _ModPacket) -> 'ModPacket':
        return ModPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModPacket):
        """
        Dynamic initializer for ModPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handlePacket(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacket.handlePacket(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool._wrap(super(_ModPacket, self).handlePacket(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def toBytes(self, arg0: 'PacketIO'):
        """public abstract void dev.ultreon.quantum.network.api.packet.ModPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.api.packet.ModPacket()"""
        val = _ModPacket()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.packet.ModPacket()"""
        val = _ModPacket()
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

 
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ModPacket
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.api.packet.ModPacket as _ModPacket
_ModPacket = _ModPacket
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModPacket():
    """dev.ultreon.quantum.network.api.packet.ModPacket"""
 
    @staticmethod
    def _wrap(java_value: _ModPacket) -> 'ModPacket':
        return ModPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModPacket):
        """
        Dynamic initializer for ModPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handlePacket(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacket.handlePacket(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool._wrap(super(_ModPacket, self).handlePacket(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def toBytes(self, arg0: 'PacketIO'):
        """public abstract void dev.ultreon.quantum.network.api.packet.ModPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.api.packet.ModPacket()"""
        val = _ModPacket()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.packet.ModPacket()"""
        val = _ModPacket()
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

 
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ModPacket 
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ModPacketContext
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.system.IConnection as _IConnection
_IConnection = _IConnection
from builtins import str
import dev.ultreon.quantum.network.NetworkChannel as _NetworkChannel
_NetworkChannel = _NetworkChannel
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.util.Env as _Env
_Env = _Env
import dev.ultreon.quantum.network.api.packet.ModPacketContext as _ModPacketContext
_ModPacketContext = _ModPacketContext
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

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

from builtins import bool
import dev.ultreon.quantum.network.PacketContext as _PacketContext
_PacketContext = _PacketContext
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModPacketContext():
    """dev.ultreon.quantum.network.api.packet.ModPacketContext"""
 
    @staticmethod
    def _wrap(java_value: _ModPacketContext) -> 'ModPacketContext':
        return ModPacketContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModPacketContext):
        """
        Dynamic initializer for ModPacketContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModPacketContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModPacketContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def requirePlayer(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.network.PacketContext.requirePlayer()"""
        return 'player.ServerPlayer'._wrap(super(network.PacketContext, self).requirePlayer())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getPlayer(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.network.PacketContext.getPlayer()"""
        return 'player.ServerPlayer'._wrap(super(network.PacketContext, self).getPlayer())

    @override
    @overload
    def getConnection(self) -> 'system.IConnection':
        """public dev.ultreon.quantum.network.system.IConnection<?, ?> dev.ultreon.quantum.network.PacketContext.getConnection()"""
        return 'system.IConnection'._wrap(super(network.PacketContext, self).getConnection())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.PacketContext.toString()"""
        return str._wrap(super(network.PacketContext, self).toString())

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.PacketContext.queue(java.lang.Runnable)"""
        super(_network.PacketContext, self).queue(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.api.packet.ModPacketContext.hashCode()"""
        return int._wrap(super(ModPacketContext, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getChannel(self) -> 'network.NetworkChannel':
        """public dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.api.packet.ModPacketContext.getChannel()"""
        return 'network.NetworkChannel'._wrap(super(ModPacketContext, self).getChannel())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.api.packet.ModPacketContext.equals(java.lang.Object)"""
        return bool._wrap(super(_ModPacketContext, self).equals(arg0))

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

    @override
    @overload
    def getDestination(self) -> 'util.Env':
        """public dev.ultreon.quantum.util.Env dev.ultreon.quantum.network.PacketContext.getDestination()"""
        return 'util.Env'._wrap(super(network.PacketContext, self).getDestination())

    @overload
    def __init__(self, arg0: 'NetworkChannel', arg1: 'ServerPlayer', arg2: 'IConnection', arg3: 'Env'):
        """public dev.ultreon.quantum.network.api.packet.ModPacketContext(dev.ultreon.quantum.network.NetworkChannel,dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.network.system.IConnection,dev.ultreon.quantum.util.Env)"""
        val = _ModPacketContext(arg0, arg1, arg2, arg3)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ModPacketToServer
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.api.packet.ModPacketToServer as _ModPacketToServer
_ModPacketToServer = _ModPacketToServer
import dev.ultreon.quantum.network.api.packet.ModPacket as _ModPacket
_ModPacket = _ModPacket
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModPacketToServer():
    """dev.ultreon.quantum.network.api.packet.ModPacketToServer"""
 
    @staticmethod
    def _wrap(java_value: _ModPacketToServer) -> 'ModPacketToServer':
        return ModPacketToServer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModPacketToServer):
        """
        Dynamic initializer for ModPacketToServer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModPacketToServer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModPacketToServer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handlePacket(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacket.handlePacket(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool._wrap(super(_ModPacket, self).handlePacket(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.api.packet.ModPacketToServer()"""
        val = _ModPacketToServer()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def toBytes(self, arg0: 'PacketIO'):
        """public abstract void dev.ultreon.quantum.network.api.packet.ModPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        pass

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.packet.ModPacketToServer()"""
        val = _ModPacketToServer()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def handle(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacketToServer.handle(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool._wrap(super(_ModPacketToServer, self).handle(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ModPacketToClient
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.api.packet.ModPacket as _ModPacket
_ModPacket = _ModPacket
import dev.ultreon.quantum.network.api.packet.ModPacketToClient as _ModPacketToClient
_ModPacketToClient = _ModPacketToClient
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModPacketToClient():
    """dev.ultreon.quantum.network.api.packet.ModPacketToClient"""
 
    @staticmethod
    def _wrap(java_value: _ModPacketToClient) -> 'ModPacketToClient':
        return ModPacketToClient(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModPacketToClient):
        """
        Dynamic initializer for ModPacketToClient.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModPacketToClient__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModPacketToClient__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handlePacket(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacket.handlePacket(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool._wrap(super(_ModPacket, self).handlePacket(arg0))

    @overload
    def handle(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacketToClient.handle(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool._wrap(super(_ModPacketToClient, self).handle(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def toBytes(self, arg0: 'PacketIO'):
        """public abstract void dev.ultreon.quantum.network.api.packet.ModPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        pass

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.api.packet.ModPacketToClient()"""
        val = _ModPacketToClient()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.packet.ModPacketToClient()"""
        val = _ModPacketToClient()
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
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ServerEndpoint
import dev.ultreon.quantum.network.api.packet.ServerEndpoint as _ServerEndpoint
_ServerEndpoint = _ServerEndpoint
 
class ServerEndpoint():
    """dev.ultreon.quantum.network.api.packet.ServerEndpoint"""
 
    @staticmethod
    def _wrap(java_value: _ServerEndpoint) -> 'ServerEndpoint':
        return ServerEndpoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerEndpoint):
        """
        Dynamic initializer for ServerEndpoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerEndpoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerEndpoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__)) 
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ClientEndpoint
import dev.ultreon.quantum.network.api.packet.ClientEndpoint as _ClientEndpoint
_ClientEndpoint = _ClientEndpoint
 
class ClientEndpoint():
    """dev.ultreon.quantum.network.api.packet.ClientEndpoint"""
 
    @staticmethod
    def _wrap(java_value: _ClientEndpoint) -> 'ClientEndpoint':
        return ClientEndpoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientEndpoint):
        """
        Dynamic initializer for ClientEndpoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientEndpoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientEndpoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__)) 
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.BiDirectionalModPacket
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.api.packet.ModPacket as _ModPacket
_ModPacket = _ModPacket
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.api.packet.BiDirectionalModPacket as _BiDirectionalModPacket
_BiDirectionalModPacket = _BiDirectionalModPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BiDirectionalModPacket():
    """dev.ultreon.quantum.network.api.packet.BiDirectionalModPacket"""
 
    @staticmethod
    def _wrap(java_value: _BiDirectionalModPacket) -> 'BiDirectionalModPacket':
        return BiDirectionalModPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BiDirectionalModPacket):
        """
        Dynamic initializer for BiDirectionalModPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BiDirectionalModPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BiDirectionalModPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handlePacket(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacket.handlePacket(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool._wrap(super(_ModPacket, self).handlePacket(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.packet.BiDirectionalModPacket()"""
        val = _BiDirectionalModPacket()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def toBytes(self, arg0: 'PacketIO'):
        """public abstract void dev.ultreon.quantum.network.api.packet.ModPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        pass

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
    def __init__(self):
        """public dev.ultreon.quantum.network.api.packet.BiDirectionalModPacket()"""
        val = _BiDirectionalModPacket()
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.BiDirectionalModPacket.handle(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool._wrap(super(_BiDirectionalModPacket, self).handle(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())