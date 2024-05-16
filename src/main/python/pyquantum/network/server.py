from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.network.server.ServerPacketHandler as __ServerPacketHandler
__ServerPacketHandler = __ServerPacketHandler
import dev.ultreon.quantum.network.api.PacketDestination as __PacketDestination
__PacketDestination = __PacketDestination
import java.lang.Long as __long
from pyquantum_helper import override
import dev.ultreon.quantum.network.PacketHandler as __PacketHandler
__PacketHandler = __PacketHandler
import dev.ultreon.quantum.network.packets.Packet as __Packet
__Packet = __Packet
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

from abc import abstractmethod, ABC
try:
    from pyquantum.network import api
except ImportError:
    api = __import_once__("pyquantum.network.api")

from builtins import bool
 
class ServerPacketHandler(ABC):
    """dev.ultreon.quantum.network.server.ServerPacketHandler"""
 
    @staticmethod
    def __wrap(java_value: __ServerPacketHandler) -> 'ServerPacketHandler':
        return ServerPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerPacketHandler):
        """
        Dynamic initializer for ServerPacketHandler.
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
 
    @overload
    def handleC2SReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.server.ServerPacketHandler.handleC2SReply(long)"""
        super(__ServerPacketHandler, self).handleC2SReply(__long.valueOf(arg0))

    @abstractmethod
    def context(self, ):
        """public abstract dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.network.PacketHandler.context()"""
        pass

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool.__wrap(super(__network.PacketHandler, self).shouldHandlePacket(arg0))

    @abstractmethod
    def onDisconnect(self, arg0: str):
        """public abstract void dev.ultreon.quantum.network.PacketHandler.onDisconnect(java.lang.String)"""
        pass

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.server.ServerPacketHandler.reply(long)"""
        return 'packets.Packet'.__wrap(super(__ServerPacketHandler, self).reply(__long.valueOf(arg0)))

    @abstractmethod
    def isAcceptingPackets(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isAcceptingPackets()"""
        pass

    @abstractmethod
    def isDisconnected(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isDisconnected()"""
        pass

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.server.ServerPacketHandler.destination()"""
        return 'api.PacketDestination'.__wrap(super(ServerPacketHandler, self).destination())

    @override
    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool.__wrap(super(network.PacketHandler, self).isAsync())

 
 
 
# CLASS: dev.ultreon.quantum.network.server.ServerPacketHandler
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.network.server.ServerPacketHandler as __ServerPacketHandler
__ServerPacketHandler = __ServerPacketHandler
import dev.ultreon.quantum.network.api.PacketDestination as __PacketDestination
__PacketDestination = __PacketDestination
import java.lang.Long as __long
from pyquantum_helper import override
import dev.ultreon.quantum.network.PacketHandler as __PacketHandler
__PacketHandler = __PacketHandler
import dev.ultreon.quantum.network.packets.Packet as __Packet
__Packet = __Packet
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

from abc import abstractmethod, ABC
try:
    from pyquantum.network import api
except ImportError:
    api = __import_once__("pyquantum.network.api")

from builtins import bool
 
class ServerPacketHandler(ABC):
    """dev.ultreon.quantum.network.server.ServerPacketHandler"""
 
    @staticmethod
    def __wrap(java_value: __ServerPacketHandler) -> 'ServerPacketHandler':
        return ServerPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerPacketHandler):
        """
        Dynamic initializer for ServerPacketHandler.
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
 
    @overload
    def handleC2SReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.server.ServerPacketHandler.handleC2SReply(long)"""
        super(__ServerPacketHandler, self).handleC2SReply(__long.valueOf(arg0))

    @abstractmethod
    def context(self, ):
        """public abstract dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.network.PacketHandler.context()"""
        pass

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool.__wrap(super(__network.PacketHandler, self).shouldHandlePacket(arg0))

    @abstractmethod
    def onDisconnect(self, arg0: str):
        """public abstract void dev.ultreon.quantum.network.PacketHandler.onDisconnect(java.lang.String)"""
        pass

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.server.ServerPacketHandler.reply(long)"""
        return 'packets.Packet'.__wrap(super(__ServerPacketHandler, self).reply(__long.valueOf(arg0)))

    @abstractmethod
    def isAcceptingPackets(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isAcceptingPackets()"""
        pass

    @abstractmethod
    def isDisconnected(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isDisconnected()"""
        pass

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.server.ServerPacketHandler.destination()"""
        return 'api.PacketDestination'.__wrap(super(ServerPacketHandler, self).destination())

    @override
    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool.__wrap(super(network.PacketHandler, self).isAsync())

 
 
 
# CLASS: dev.ultreon.quantum.network.server.ServerPacketHandler 
 
 
# CLASS: dev.ultreon.quantum.network.server.InGameServerPacketHandler
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

import java.lang.Boolean as __boolean
from builtins import type
try:
    from pyquantum.network.api import packet
except ImportError:
    packet = __import_once__("pyquantum.network.api.packet")

import dev.ultreon.quantum.network.packets.Packet as __Packet
__Packet = __Packet
import dev.ultreon.quantum.server.QuantumServer as __QuantumServer
__QuantumServer = __QuantumServer
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import dev.ultreon.quantum.network.NetworkChannel as __NetworkChannel
__NetworkChannel = __NetworkChannel
import dev.ultreon.quantum.network.server.ServerPacketHandler as __ServerPacketHandler
__ServerPacketHandler = __ServerPacketHandler
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.network.PacketHandler as __PacketHandler
__PacketHandler = __PacketHandler
import java.lang.Double as __double
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.network.server.InGameServerPacketHandler as __InGameServerPacketHandler
__InGameServerPacketHandler = __InGameServerPacketHandler
try:
    from pyquantum.network import api
except ImportError:
    api = __import_once__("pyquantum.network.api")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.network.api.PacketDestination as __PacketDestination
__PacketDestination = __PacketDestination
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

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
try:
    from pyquantum.network.packets import c2s
except ImportError:
    c2s = __import_once__("pyquantum.network.packets.c2s")

import java.lang.Integer as __int
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
 
class InGameServerPacketHandler():
    """dev.ultreon.quantum.network.server.InGameServerPacketHandler"""
 
    @staticmethod
    def __wrap(java_value: __InGameServerPacketHandler) -> 'InGameServerPacketHandler':
        return InGameServerPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InGameServerPacketHandler):
        """
        Dynamic initializer for InGameServerPacketHandler.
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
    def handleC2SReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.server.ServerPacketHandler.handleC2SReply(long)"""
        super(__ServerPacketHandler, self).handleC2SReply(__long.valueOf(arg0))

    @overload
    def onAbilities(self, arg0: 'AbilitiesPacket'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onAbilities(dev.ultreon.quantum.network.packets.AbilitiesPacket)"""
        super(__InGameServerPacketHandler, self).onAbilities(arg0)

    @overload
    def onKeepAlive(self):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onKeepAlive()"""
        super(InGameServerPacketHandler, self).onKeepAlive()

    @overload
    def onPlaceBlock(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onPlaceBlock(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__InGameServerPacketHandler, self).onPlaceBlock(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isDisconnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.server.InGameServerPacketHandler.isDisconnected()"""
        return bool.__wrap(super(InGameServerPacketHandler, self).isDisconnected())

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.server.ServerPacketHandler.reply(long)"""
        return 'packets.Packet'.__wrap(super(__ServerPacketHandler, self).reply(__long.valueOf(arg0)))

    @overload
    def onTakeItem(self, arg0: int, arg1: bool):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onTakeItem(int,boolean)"""
        super(__InGameServerPacketHandler, self).onTakeItem(__int.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def onModPacket(self, arg0: 'NetworkChannel', arg1: 'ModPacket'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onModPacket(dev.ultreon.quantum.network.NetworkChannel,dev.ultreon.quantum.network.api.packet.ModPacket<?>)"""
        super(__InGameServerPacketHandler, self).onModPacket(arg0, arg1)

    @overload
    def onRespawn(self):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onRespawn()"""
        super(InGameServerPacketHandler, self).onRespawn()

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public boolean dev.ultreon.quantum.network.server.InGameServerPacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool.__wrap(super(__InGameServerPacketHandler, self).shouldHandlePacket(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def registerChannel(arg0: 'Identifier') -> 'network.NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.server.InGameServerPacketHandler.registerChannel(dev.ultreon.quantum.util.Identifier)"""
        return network.NetworkChannel.__wrap(__InGameServerPacketHandler.registerChannel(arg0))

    @override
    @overload
    def context(self) -> 'network.PacketContext':
        """public dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.network.server.InGameServerPacketHandler.context()"""
        return 'network.PacketContext'.__wrap(super(InGameServerPacketHandler, self).context())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def onCloseContainerMenu(self):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onCloseContainerMenu()"""
        super(InGameServerPacketHandler, self).onCloseContainerMenu()

    @overload
    def getServer(self) -> 'server.QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.network.server.InGameServerPacketHandler.getServer()"""
        return 'server.QuantumServer'.__wrap(super(InGameServerPacketHandler, self).getServer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def onAttack(self, arg0: int):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onAttack(int)"""
        super(__InGameServerPacketHandler, self).onAttack(__int.valueOf(arg0))

    @overload
    def onItemUse(self, arg0: 'BlockHitResult'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onItemUse(dev.ultreon.quantum.util.BlockHitResult)"""
        super(__InGameServerPacketHandler, self).onItemUse(arg0)

    @overload
    def __init__(self, arg0: 'QuantumServer', arg1: 'ServerPlayer', arg2: 'IConnection'):
        """public dev.ultreon.quantum.network.server.InGameServerPacketHandler(dev.ultreon.quantum.server.QuantumServer,dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.network.system.IConnection)"""
        val = __InGameServerPacketHandler(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def onDisconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onDisconnect(java.lang.String)"""
        super(__InGameServerPacketHandler, self).onDisconnect(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def onOpenInventory(self):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onOpenInventory()"""
        super(InGameServerPacketHandler, self).onOpenInventory()

    @overload
    def onChunkStatus(self, arg0: 'ServerPlayer', arg1: 'ChunkPos', arg2: 'Status'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onChunkStatus(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk$Status)"""
        super(__InGameServerPacketHandler, self).onChunkStatus(arg0, arg1, arg2)

    @overload
    def onHotbarIndex(self, arg0: int):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onHotbarIndex(int)"""
        super(__InGameServerPacketHandler, self).onHotbarIndex(__int.valueOf(arg0))

    @overload
    def onCraftRecipe(self, arg0: int, arg1: 'Identifier'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onCraftRecipe(int,dev.ultreon.quantum.util.Identifier)"""
        super(__InGameServerPacketHandler, self).onCraftRecipe(__int.valueOf(arg0), arg1)

    @overload
    def onBlockBreaking(self, arg0: 'BlockPos', arg1: 'BlockStatus'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onBlockBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus)"""
        super(__InGameServerPacketHandler, self).onBlockBreaking(arg0, arg1)

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.server.InGameServerPacketHandler.destination()"""
        return 'api.PacketDestination'.__wrap(super(InGameServerPacketHandler, self).destination())

    @override
    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool.__wrap(super(network.PacketHandler, self).isAsync())

    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onPing(long)"""
        super(__InGameServerPacketHandler, self).onPing(__long.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getChannel(self, arg0: 'Identifier') -> 'network.NetworkChannel':
        """public dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.server.InGameServerPacketHandler.getChannel(dev.ultreon.quantum.util.Identifier)"""
        return 'network.NetworkChannel'.__wrap(super(__InGameServerPacketHandler, self).getChannel(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def handleOpenMenu(self, arg0: 'Identifier', arg1: 'BlockPos'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.handleOpenMenu(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.world.BlockPos)"""
        super(__InGameServerPacketHandler, self).handleOpenMenu(arg0, arg1)

    @overload
    def onDropItem(self):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onDropItem()"""
        super(InGameServerPacketHandler, self).onDropItem()

    @overload
    def onDisconnected(self, arg0: str):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onDisconnected(java.lang.String)"""
        super(__InGameServerPacketHandler, self).onDisconnected(arg0)

    @overload
    def onPlayerMove(self, arg0: 'ServerPlayer', arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onPlayerMove(dev.ultreon.quantum.server.player.ServerPlayer,double,double,double)"""
        super(__InGameServerPacketHandler, self).onPlayerMove(arg0, __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def onBlockBroken(self, arg0: 'BlockPos'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onBlockBroken(dev.ultreon.quantum.world.BlockPos)"""
        super(__InGameServerPacketHandler, self).onBlockBroken(arg0)

    @override
    @overload
    def isAcceptingPackets(self) -> bool:
        """public boolean dev.ultreon.quantum.network.server.InGameServerPacketHandler.isAcceptingPackets()"""
        return bool.__wrap(super(InGameServerPacketHandler, self).isAcceptingPackets()) 
 
 
# CLASS: dev.ultreon.quantum.network.server.LoginServerPacketHandler
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

from builtins import type
try:
    from pyquantum.network.api import packet
except ImportError:
    packet = __import_once__("pyquantum.network.api.packet")

import dev.ultreon.quantum.network.packets.Packet as __Packet
__Packet = __Packet
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import dev.ultreon.quantum.network.NetworkChannel as __NetworkChannel
__NetworkChannel = __NetworkChannel
import dev.ultreon.quantum.network.server.ServerPacketHandler as __ServerPacketHandler
__ServerPacketHandler = __ServerPacketHandler
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.network.server.LoginServerPacketHandler as __LoginServerPacketHandler
__LoginServerPacketHandler = __LoginServerPacketHandler
import java.lang.String as __string
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum.network import api
except ImportError:
    api = __import_once__("pyquantum.network.api")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import dev.ultreon.quantum.network.api.PacketDestination as __PacketDestination
__PacketDestination = __PacketDestination
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.network.PacketContext as __PacketContext
__PacketContext = __PacketContext
import java.lang.Integer as __int
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
 
class LoginServerPacketHandler():
    """dev.ultreon.quantum.network.server.LoginServerPacketHandler"""
 
    @staticmethod
    def __wrap(java_value: __LoginServerPacketHandler) -> 'LoginServerPacketHandler':
        return LoginServerPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoginServerPacketHandler):
        """
        Dynamic initializer for LoginServerPacketHandler.
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
    def handleC2SReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.server.ServerPacketHandler.handleC2SReply(long)"""
        super(__ServerPacketHandler, self).handleC2SReply(__long.valueOf(arg0))

    @overload
    def onRespawn(self):
        """public void dev.ultreon.quantum.network.server.LoginServerPacketHandler.onRespawn()"""
        super(LoginServerPacketHandler, self).onRespawn()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def onPlayerLogin(self, arg0: str):
        """public void dev.ultreon.quantum.network.server.LoginServerPacketHandler.onPlayerLogin(java.lang.String)"""
        super(__LoginServerPacketHandler, self).onPlayerLogin(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.server.LoginServerPacketHandler.onDisconnect(java.lang.String)"""
        super(__LoginServerPacketHandler, self).onDisconnect(arg0)

    @overload
    def __init__(self, arg0: 'QuantumServer', arg1: 'IConnection'):
        """public dev.ultreon.quantum.network.server.LoginServerPacketHandler(dev.ultreon.quantum.server.QuantumServer,dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.server.ServerPacketHandler, dev.ultreon.quantum.network.client.ClientPacketHandler>)"""
        val = __LoginServerPacketHandler(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.server.ServerPacketHandler.reply(long)"""
        return 'packets.Packet'.__wrap(super(__ServerPacketHandler, self).reply(__long.valueOf(arg0)))

    @override
    @overload
    def context(self) -> 'network.PacketContext':
        """public dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.network.server.LoginServerPacketHandler.context()"""
        return 'network.PacketContext'.__wrap(super(LoginServerPacketHandler, self).context())

    @override
    @overload
    def isAsync(self) -> bool:
        """public boolean dev.ultreon.quantum.network.server.LoginServerPacketHandler.isAsync()"""
        return bool.__wrap(super(LoginServerPacketHandler, self).isAsync())

    @override
    @overload
    def isAcceptingPackets(self) -> bool:
        """public boolean dev.ultreon.quantum.network.server.LoginServerPacketHandler.isAcceptingPackets()"""
        return bool.__wrap(super(LoginServerPacketHandler, self).isAcceptingPackets())

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public boolean dev.ultreon.quantum.network.server.LoginServerPacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool.__wrap(super(__LoginServerPacketHandler, self).shouldHandlePacket(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def registerChannel(arg0: 'Identifier') -> 'network.NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.server.LoginServerPacketHandler.registerChannel(dev.ultreon.quantum.util.Identifier)"""
        return network.NetworkChannel.__wrap(__LoginServerPacketHandler.registerChannel(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getChannel(self, arg0: 'Identifier') -> 'network.NetworkChannel':
        """public dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.server.LoginServerPacketHandler.getChannel(dev.ultreon.quantum.util.Identifier)"""
        return 'network.NetworkChannel'.__wrap(super(__LoginServerPacketHandler, self).getChannel(arg0))

    @overload
    def onModPacket(self, arg0: 'NetworkChannel', arg1: 'ModPacket'):
        """public void dev.ultreon.quantum.network.server.LoginServerPacketHandler.onModPacket(dev.ultreon.quantum.network.NetworkChannel,dev.ultreon.quantum.network.api.packet.ModPacket<?>)"""
        super(__LoginServerPacketHandler, self).onModPacket(arg0, arg1)

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

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.server.ServerPacketHandler.destination()"""
        return 'api.PacketDestination'.__wrap(super(ServerPacketHandler, self).destination())

    @override
    @overload
    def isDisconnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.server.LoginServerPacketHandler.isDisconnected()"""
        return bool.__wrap(super(LoginServerPacketHandler, self).isDisconnected())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))