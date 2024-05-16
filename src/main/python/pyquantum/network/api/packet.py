from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.api.packet.ModPacket as __ModPacket
__ModPacket = __ModPacket
from abc import abstractmethod, ABC
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ModPacket(ABC):
    """dev.ultreon.quantum.network.api.packet.ModPacket"""
 
    @staticmethod
    def __wrap(java_value: __ModPacket) -> 'ModPacket':
        return ModPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModPacket):
        """
        Dynamic initializer for ModPacket.
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
    def handlePacket(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacket.handlePacket(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool.__wrap(super(__ModPacket, self).handlePacket(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.network.api.packet.ModPacket()"""
        val = __ModPacket()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.packet.ModPacket()"""
        val = __ModPacket()
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ModPacket
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.api.packet.ModPacket as __ModPacket
__ModPacket = __ModPacket
from abc import abstractmethod, ABC
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ModPacket(ABC):
    """dev.ultreon.quantum.network.api.packet.ModPacket"""
 
    @staticmethod
    def __wrap(java_value: __ModPacket) -> 'ModPacket':
        return ModPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModPacket):
        """
        Dynamic initializer for ModPacket.
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
    def handlePacket(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacket.handlePacket(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool.__wrap(super(__ModPacket, self).handlePacket(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.network.api.packet.ModPacket()"""
        val = __ModPacket()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.packet.ModPacket()"""
        val = __ModPacket()
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ModPacket 
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ModPacketContext
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.network.api.packet.ModPacketContext as __ModPacketContext
__ModPacketContext = __ModPacketContext
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import dev.ultreon.quantum.util.Env as __Env
__Env = __Env
import dev.ultreon.quantum.network.NetworkChannel as __NetworkChannel
__NetworkChannel = __NetworkChannel
import dev.ultreon.quantum.network.system.IConnection as __IConnection
__IConnection = __IConnection
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

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
import dev.ultreon.quantum.network.PacketContext as __PacketContext
__PacketContext = __PacketContext
import java.lang.Integer as __int
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
 
class ModPacketContext():
    """dev.ultreon.quantum.network.api.packet.ModPacketContext"""
 
    @staticmethod
    def __wrap(java_value: __ModPacketContext) -> 'ModPacketContext':
        return ModPacketContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModPacketContext):
        """
        Dynamic initializer for ModPacketContext.
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
    def requirePlayer(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.network.PacketContext.requirePlayer()"""
        return 'player.ServerPlayer'.__wrap(super(network.PacketContext, self).requirePlayer())

    @override
    @overload
    def getDestination(self) -> 'util.Env':
        """public dev.ultreon.quantum.util.Env dev.ultreon.quantum.network.PacketContext.getDestination()"""
        return 'util.Env'.__wrap(super(network.PacketContext, self).getDestination())

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.PacketContext.queue(java.lang.Runnable)"""
        super(__network.PacketContext, self).queue(arg0)

    @overload
    def __init__(self, arg0: 'NetworkChannel', arg1: 'ServerPlayer', arg2: 'IConnection', arg3: 'Env'):
        """public dev.ultreon.quantum.network.api.packet.ModPacketContext(dev.ultreon.quantum.network.NetworkChannel,dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.network.system.IConnection,dev.ultreon.quantum.util.Env)"""
        val = __ModPacketContext(arg0, arg1, arg2, arg3)
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
    def getConnection(self) -> 'system.IConnection':
        """public dev.ultreon.quantum.network.system.IConnection<?, ?> dev.ultreon.quantum.network.PacketContext.getConnection()"""
        return 'system.IConnection'.__wrap(super(network.PacketContext, self).getConnection())

    @override
    @overload
    def getPlayer(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.network.PacketContext.getPlayer()"""
        return 'player.ServerPlayer'.__wrap(super(network.PacketContext, self).getPlayer())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.PacketContext.toString()"""
        return str.__wrap(super(network.PacketContext, self).toString())

    @overload
    def getChannel(self) -> 'network.NetworkChannel':
        """public dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.api.packet.ModPacketContext.getChannel()"""
        return 'network.NetworkChannel'.__wrap(super(ModPacketContext, self).getChannel())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.api.packet.ModPacketContext.equals(java.lang.Object)"""
        return bool.__wrap(super(__ModPacketContext, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.api.packet.ModPacketContext.hashCode()"""
        return int.__wrap(super(ModPacketContext, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ModPacketToServer
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.api.packet.ModPacket as __ModPacket
__ModPacket = __ModPacket
from abc import abstractmethod, ABC
import dev.ultreon.quantum.network.api.packet.ModPacketToServer as __ModPacketToServer
__ModPacketToServer = __ModPacketToServer
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ModPacketToServer(ABC):
    """dev.ultreon.quantum.network.api.packet.ModPacketToServer"""
 
    @staticmethod
    def __wrap(java_value: __ModPacketToServer) -> 'ModPacketToServer':
        return ModPacketToServer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModPacketToServer):
        """
        Dynamic initializer for ModPacketToServer.
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
    def handlePacket(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacket.handlePacket(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool.__wrap(super(__ModPacket, self).handlePacket(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.packet.ModPacketToServer()"""
        val = __ModPacketToServer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.api.packet.ModPacketToServer()"""
        val = __ModPacketToServer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def handle(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacketToServer.handle(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool.__wrap(super(__ModPacketToServer, self).handle(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ModPacketToClient
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.api.packet.ModPacket as __ModPacket
__ModPacket = __ModPacket
from abc import abstractmethod, ABC
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.network.api.packet.ModPacketToClient as __ModPacketToClient
__ModPacketToClient = __ModPacketToClient
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ModPacketToClient(ABC):
    """dev.ultreon.quantum.network.api.packet.ModPacketToClient"""
 
    @staticmethod
    def __wrap(java_value: __ModPacketToClient) -> 'ModPacketToClient':
        return ModPacketToClient(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModPacketToClient):
        """
        Dynamic initializer for ModPacketToClient.
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
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.packet.ModPacketToClient()"""
        val = __ModPacketToClient()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def handlePacket(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacket.handlePacket(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool.__wrap(super(__ModPacket, self).handlePacket(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.network.api.packet.ModPacketToClient()"""
        val = __ModPacketToClient()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def handle(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacketToClient.handle(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool.__wrap(super(__ModPacketToClient, self).handle(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ServerEndpoint
import dev.ultreon.quantum.network.api.packet.ServerEndpoint as __ServerEndpoint
__ServerEndpoint = __ServerEndpoint
 
class ServerEndpoint(ABC):
    """dev.ultreon.quantum.network.api.packet.ServerEndpoint"""
 
    @staticmethod
    def __wrap(java_value: __ServerEndpoint) -> 'ServerEndpoint':
        return ServerEndpoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerEndpoint):
        """
        Dynamic initializer for ServerEndpoint.
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
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.ClientEndpoint
import dev.ultreon.quantum.network.api.packet.ClientEndpoint as __ClientEndpoint
__ClientEndpoint = __ClientEndpoint
 
class ClientEndpoint(ABC):
    """dev.ultreon.quantum.network.api.packet.ClientEndpoint"""
 
    @staticmethod
    def __wrap(java_value: __ClientEndpoint) -> 'ClientEndpoint':
        return ClientEndpoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientEndpoint):
        """
        Dynamic initializer for ClientEndpoint.
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
 
 
# CLASS: dev.ultreon.quantum.network.api.packet.BiDirectionalModPacket
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.api.packet.ModPacket as __ModPacket
__ModPacket = __ModPacket
from abc import abstractmethod, ABC
import dev.ultreon.quantum.network.api.packet.BiDirectionalModPacket as __BiDirectionalModPacket
__BiDirectionalModPacket = __BiDirectionalModPacket
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BiDirectionalModPacket(ABC):
    """dev.ultreon.quantum.network.api.packet.BiDirectionalModPacket"""
 
    @staticmethod
    def __wrap(java_value: __BiDirectionalModPacket) -> 'BiDirectionalModPacket':
        return BiDirectionalModPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiDirectionalModPacket):
        """
        Dynamic initializer for BiDirectionalModPacket.
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
    def handle(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.BiDirectionalModPacket.handle(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool.__wrap(super(__BiDirectionalModPacket, self).handle(arg0))

    @abstractmethod
    def toBytes(self, arg0: 'PacketIO'):
        """public abstract void dev.ultreon.quantum.network.api.packet.ModPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        pass

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.api.packet.BiDirectionalModPacket()"""
        val = __BiDirectionalModPacket()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def handlePacket(self, arg0: 'Supplier') -> bool:
        """public final boolean dev.ultreon.quantum.network.api.packet.ModPacket.handlePacket(java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>)"""
        return bool.__wrap(super(__ModPacket, self).handlePacket(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.network.api.packet.BiDirectionalModPacket()"""
        val = __BiDirectionalModPacket()
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