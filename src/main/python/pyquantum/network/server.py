from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.server.ServerPacketHandler as _ServerPacketHandler
_ServerPacketHandler = _ServerPacketHandler
from pyquantum_helper import override
import dev.ultreon.quantum.network.api.PacketDestination as _PacketDestination
_PacketDestination = _PacketDestination
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import dev.ultreon.quantum.network.packets.Packet as _Packet
_Packet = _Packet
from abc import abstractmethod, ABC
try:
    from pyquantum.network import api
except ImportError:
    api = _import_once("pyquantum.network.api")

import dev.ultreon.quantum.network.PacketHandler as _PacketHandler
_PacketHandler = _PacketHandler
from builtins import bool
import java.lang.Long as _long
 
class ServerPacketHandler():
    """dev.ultreon.quantum.network.server.ServerPacketHandler"""
 
    @staticmethod
    def _wrap(java_value: _ServerPacketHandler) -> 'ServerPacketHandler':
        return ServerPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerPacketHandler):
        """
        Dynamic initializer for ServerPacketHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerPacketHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerPacketHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handleC2SReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.server.ServerPacketHandler.handleC2SReply(long)"""
        super(_ServerPacketHandler, self).handleC2SReply(_long.valueOf(arg0))

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.server.ServerPacketHandler.destination()"""
        return 'api.PacketDestination'._wrap(super(ServerPacketHandler, self).destination())

    @abstractmethod
    def context(self, ):
        """public abstract dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.network.PacketHandler.context()"""
        pass

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool._wrap(super(_network.PacketHandler, self).shouldHandlePacket(arg0))

    @override
    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool._wrap(super(network.PacketHandler, self).isAsync())

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.server.ServerPacketHandler.reply(long)"""
        return 'packets.Packet'._wrap(super(_ServerPacketHandler, self).reply(_long.valueOf(arg0)))

    @abstractmethod
    def onDisconnect(self, arg0: str):
        """public abstract void dev.ultreon.quantum.network.PacketHandler.onDisconnect(java.lang.String)"""
        pass

    @abstractmethod
    def isAcceptingPackets(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isAcceptingPackets()"""
        pass

    @abstractmethod
    def isDisconnected(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isDisconnected()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.network.server.ServerPacketHandler
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.server.ServerPacketHandler as _ServerPacketHandler
_ServerPacketHandler = _ServerPacketHandler
from pyquantum_helper import override
import dev.ultreon.quantum.network.api.PacketDestination as _PacketDestination
_PacketDestination = _PacketDestination
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import dev.ultreon.quantum.network.packets.Packet as _Packet
_Packet = _Packet
from abc import abstractmethod, ABC
try:
    from pyquantum.network import api
except ImportError:
    api = _import_once("pyquantum.network.api")

import dev.ultreon.quantum.network.PacketHandler as _PacketHandler
_PacketHandler = _PacketHandler
from builtins import bool
import java.lang.Long as _long
 
class ServerPacketHandler():
    """dev.ultreon.quantum.network.server.ServerPacketHandler"""
 
    @staticmethod
    def _wrap(java_value: _ServerPacketHandler) -> 'ServerPacketHandler':
        return ServerPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerPacketHandler):
        """
        Dynamic initializer for ServerPacketHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerPacketHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerPacketHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handleC2SReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.server.ServerPacketHandler.handleC2SReply(long)"""
        super(_ServerPacketHandler, self).handleC2SReply(_long.valueOf(arg0))

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.server.ServerPacketHandler.destination()"""
        return 'api.PacketDestination'._wrap(super(ServerPacketHandler, self).destination())

    @abstractmethod
    def context(self, ):
        """public abstract dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.network.PacketHandler.context()"""
        pass

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool._wrap(super(_network.PacketHandler, self).shouldHandlePacket(arg0))

    @override
    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool._wrap(super(network.PacketHandler, self).isAsync())

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.server.ServerPacketHandler.reply(long)"""
        return 'packets.Packet'._wrap(super(_ServerPacketHandler, self).reply(_long.valueOf(arg0)))

    @abstractmethod
    def onDisconnect(self, arg0: str):
        """public abstract void dev.ultreon.quantum.network.PacketHandler.onDisconnect(java.lang.String)"""
        pass

    @abstractmethod
    def isAcceptingPackets(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isAcceptingPackets()"""
        pass

    @abstractmethod
    def isDisconnected(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isDisconnected()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.network.server.ServerPacketHandler 
 
 
# CLASS: dev.ultreon.quantum.network.server.InGameServerPacketHandler
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum.network.api import packet
except ImportError:
    packet = _import_once("pyquantum.network.api.packet")

try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import dev.ultreon.quantum.network.packets.Packet as _Packet
_Packet = _Packet
import dev.ultreon.quantum.network.server.InGameServerPacketHandler as _InGameServerPacketHandler
_InGameServerPacketHandler = _InGameServerPacketHandler
import java.lang.String as _string
import dev.ultreon.quantum.network.server.ServerPacketHandler as _ServerPacketHandler
_ServerPacketHandler = _ServerPacketHandler
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.network.PacketContext as _PacketContext
_PacketContext = _PacketContext
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.network.NetworkChannel as _NetworkChannel
_NetworkChannel = _NetworkChannel
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
try:
    from pyquantum.network import api
except ImportError:
    api = _import_once("pyquantum.network.api")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.network.api.PacketDestination as _PacketDestination
_PacketDestination = _PacketDestination
try:
    from pyquantum.network.packets import c2s
except ImportError:
    c2s = _import_once("pyquantum.network.packets.c2s")

import dev.ultreon.quantum.server.QuantumServer as _QuantumServer
_QuantumServer = _QuantumServer
import dev.ultreon.quantum.network.PacketHandler as _PacketHandler
_PacketHandler = _PacketHandler
import java.lang.Long as _long
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InGameServerPacketHandler():
    """dev.ultreon.quantum.network.server.InGameServerPacketHandler"""
 
    @staticmethod
    def _wrap(java_value: _InGameServerPacketHandler) -> 'InGameServerPacketHandler':
        return InGameServerPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InGameServerPacketHandler):
        """
        Dynamic initializer for InGameServerPacketHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InGameServerPacketHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InGameServerPacketHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def onBlockBreaking(self, arg0: 'BlockPos', arg1: 'BlockStatus'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onBlockBreaking(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus)"""
        super(_InGameServerPacketHandler, self).onBlockBreaking(arg0, arg1)

    @overload
    def onPlaceBlock(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onPlaceBlock(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_InGameServerPacketHandler, self).onPlaceBlock(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def onDisconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onDisconnect(java.lang.String)"""
        super(_InGameServerPacketHandler, self).onDisconnect(arg0)

    @overload
    def onKeepAlive(self):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onKeepAlive()"""
        super(InGameServerPacketHandler, self).onKeepAlive()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getServer(self) -> 'server.QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.network.server.InGameServerPacketHandler.getServer()"""
        return 'server.QuantumServer'._wrap(super(InGameServerPacketHandler, self).getServer())

    @overload
    def onAttack(self, arg0: int):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onAttack(int)"""
        super(_InGameServerPacketHandler, self).onAttack(_int.valueOf(arg0))

    @overload
    def handleOpenMenu(self, arg0: 'Identifier', arg1: 'BlockPos'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.handleOpenMenu(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.world.BlockPos)"""
        super(_InGameServerPacketHandler, self).handleOpenMenu(arg0, arg1)

    @override
    @overload
    def handleC2SReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.server.ServerPacketHandler.handleC2SReply(long)"""
        super(_ServerPacketHandler, self).handleC2SReply(_long.valueOf(arg0))

    @overload
    def onRespawn(self):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onRespawn()"""
        super(InGameServerPacketHandler, self).onRespawn()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getChannel(self, arg0: 'Identifier') -> 'network.NetworkChannel':
        """public dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.server.InGameServerPacketHandler.getChannel(dev.ultreon.quantum.util.Identifier)"""
        return 'network.NetworkChannel'._wrap(super(_InGameServerPacketHandler, self).getChannel(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def onItemUse(self, arg0: 'BlockHitResult'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onItemUse(dev.ultreon.quantum.util.BlockHitResult)"""
        super(_InGameServerPacketHandler, self).onItemUse(arg0)

    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onPing(long)"""
        super(_InGameServerPacketHandler, self).onPing(_long.valueOf(arg0))

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.server.ServerPacketHandler.reply(long)"""
        return 'packets.Packet'._wrap(super(_ServerPacketHandler, self).reply(_long.valueOf(arg0)))

    @overload
    def onHotbarIndex(self, arg0: int):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onHotbarIndex(int)"""
        super(_InGameServerPacketHandler, self).onHotbarIndex(_int.valueOf(arg0))

    @overload
    def onDisconnected(self, arg0: str):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onDisconnected(java.lang.String)"""
        super(_InGameServerPacketHandler, self).onDisconnected(arg0)

    @overload
    def onCloseContainerMenu(self):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onCloseContainerMenu()"""
        super(InGameServerPacketHandler, self).onCloseContainerMenu()

    @overload
    def __init__(self, arg0: 'QuantumServer', arg1: 'ServerPlayer', arg2: 'IConnection'):
        """public dev.ultreon.quantum.network.server.InGameServerPacketHandler(dev.ultreon.quantum.server.QuantumServer,dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.network.system.IConnection)"""
        val = _InGameServerPacketHandler(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def onAbilities(self, arg0: 'AbilitiesPacket'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onAbilities(dev.ultreon.quantum.network.packets.AbilitiesPacket)"""
        super(_InGameServerPacketHandler, self).onAbilities(arg0)

    @override
    @overload
    def isAcceptingPackets(self) -> bool:
        """public boolean dev.ultreon.quantum.network.server.InGameServerPacketHandler.isAcceptingPackets()"""
        return bool._wrap(super(InGameServerPacketHandler, self).isAcceptingPackets())

    @overload
    def onPlayerMove(self, arg0: 'ServerPlayer', arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onPlayerMove(dev.ultreon.quantum.server.player.ServerPlayer,double,double,double)"""
        super(_InGameServerPacketHandler, self).onPlayerMove(arg0, _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3))

    @override
    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool._wrap(super(network.PacketHandler, self).isAsync())

    @overload
    def onOpenInventory(self):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onOpenInventory()"""
        super(InGameServerPacketHandler, self).onOpenInventory()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isDisconnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.server.InGameServerPacketHandler.isDisconnected()"""
        return bool._wrap(super(InGameServerPacketHandler, self).isDisconnected())

    @staticmethod
    @overload
    def registerChannel(arg0: 'Identifier') -> 'network.NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.server.InGameServerPacketHandler.registerChannel(dev.ultreon.quantum.util.Identifier)"""
        return network.NetworkChannel._wrap(_InGameServerPacketHandler.registerChannel(arg0))

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.server.InGameServerPacketHandler.destination()"""
        return 'api.PacketDestination'._wrap(super(InGameServerPacketHandler, self).destination())

    @overload
    def onTakeItem(self, arg0: int, arg1: bool):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onTakeItem(int,boolean)"""
        super(_InGameServerPacketHandler, self).onTakeItem(_int.valueOf(arg0), _boolean.valueOf(arg1))

    @overload
    def onCraftRecipe(self, arg0: int, arg1: 'Identifier'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onCraftRecipe(int,dev.ultreon.quantum.util.Identifier)"""
        super(_InGameServerPacketHandler, self).onCraftRecipe(_int.valueOf(arg0), arg1)

    @overload
    def onModPacket(self, arg0: 'NetworkChannel', arg1: 'ModPacket'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onModPacket(dev.ultreon.quantum.network.NetworkChannel,dev.ultreon.quantum.network.api.packet.ModPacket<?>)"""
        super(_InGameServerPacketHandler, self).onModPacket(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public boolean dev.ultreon.quantum.network.server.InGameServerPacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool._wrap(super(_InGameServerPacketHandler, self).shouldHandlePacket(arg0))

    @overload
    def onDropItem(self):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onDropItem()"""
        super(InGameServerPacketHandler, self).onDropItem()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def onChunkStatus(self, arg0: 'ServerPlayer', arg1: 'ChunkPos', arg2: 'Status'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onChunkStatus(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk$Status)"""
        super(_InGameServerPacketHandler, self).onChunkStatus(arg0, arg1, arg2)

    @override
    @overload
    def context(self) -> 'network.PacketContext':
        """public dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.network.server.InGameServerPacketHandler.context()"""
        return 'network.PacketContext'._wrap(super(InGameServerPacketHandler, self).context())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def onBlockBroken(self, arg0: 'BlockPos'):
        """public void dev.ultreon.quantum.network.server.InGameServerPacketHandler.onBlockBroken(dev.ultreon.quantum.world.BlockPos)"""
        super(_InGameServerPacketHandler, self).onBlockBroken(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.server.LoginServerPacketHandler
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum.network.api import packet
except ImportError:
    packet = _import_once("pyquantum.network.api.packet")

try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import dev.ultreon.quantum.network.packets.Packet as _Packet
_Packet = _Packet
import dev.ultreon.quantum.network.server.LoginServerPacketHandler as _LoginServerPacketHandler
_LoginServerPacketHandler = _LoginServerPacketHandler
import java.lang.String as _string
import dev.ultreon.quantum.network.server.ServerPacketHandler as _ServerPacketHandler
_ServerPacketHandler = _ServerPacketHandler
import dev.ultreon.quantum.network.PacketContext as _PacketContext
_PacketContext = _PacketContext
from builtins import bool
from builtins import str
import dev.ultreon.quantum.network.NetworkChannel as _NetworkChannel
_NetworkChannel = _NetworkChannel
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
try:
    from pyquantum.network import api
except ImportError:
    api = _import_once("pyquantum.network.api")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.api.PacketDestination as _PacketDestination
_PacketDestination = _PacketDestination
import java.lang.Long as _long
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LoginServerPacketHandler():
    """dev.ultreon.quantum.network.server.LoginServerPacketHandler"""
 
    @staticmethod
    def _wrap(java_value: _LoginServerPacketHandler) -> 'LoginServerPacketHandler':
        return LoginServerPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoginServerPacketHandler):
        """
        Dynamic initializer for LoginServerPacketHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoginServerPacketHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoginServerPacketHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def registerChannel(arg0: 'Identifier') -> 'network.NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.server.LoginServerPacketHandler.registerChannel(dev.ultreon.quantum.util.Identifier)"""
        return network.NetworkChannel._wrap(_LoginServerPacketHandler.registerChannel(arg0))

    @override
    @overload
    def isAcceptingPackets(self) -> bool:
        """public boolean dev.ultreon.quantum.network.server.LoginServerPacketHandler.isAcceptingPackets()"""
        return bool._wrap(super(LoginServerPacketHandler, self).isAcceptingPackets())

    @overload
    def onRespawn(self):
        """public void dev.ultreon.quantum.network.server.LoginServerPacketHandler.onRespawn()"""
        super(LoginServerPacketHandler, self).onRespawn()

    @override
    @overload
    def onDisconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.server.LoginServerPacketHandler.onDisconnect(java.lang.String)"""
        super(_LoginServerPacketHandler, self).onDisconnect(arg0)

    @overload
    def __init__(self, arg0: 'QuantumServer', arg1: 'IConnection'):
        """public dev.ultreon.quantum.network.server.LoginServerPacketHandler(dev.ultreon.quantum.server.QuantumServer,dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.server.ServerPacketHandler, dev.ultreon.quantum.network.client.ClientPacketHandler>)"""
        val = _LoginServerPacketHandler(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def context(self) -> 'network.PacketContext':
        """public dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.network.server.LoginServerPacketHandler.context()"""
        return 'network.PacketContext'._wrap(super(LoginServerPacketHandler, self).context())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public boolean dev.ultreon.quantum.network.server.LoginServerPacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool._wrap(super(_LoginServerPacketHandler, self).shouldHandlePacket(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def handleC2SReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.server.ServerPacketHandler.handleC2SReply(long)"""
        super(_ServerPacketHandler, self).handleC2SReply(_long.valueOf(arg0))

    @overload
    def getChannel(self, arg0: 'Identifier') -> 'network.NetworkChannel':
        """public dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.server.LoginServerPacketHandler.getChannel(dev.ultreon.quantum.util.Identifier)"""
        return 'network.NetworkChannel'._wrap(super(_LoginServerPacketHandler, self).getChannel(arg0))

    @override
    @overload
    def isDisconnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.server.LoginServerPacketHandler.isDisconnected()"""
        return bool._wrap(super(LoginServerPacketHandler, self).isDisconnected())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.server.ServerPacketHandler.destination()"""
        return 'api.PacketDestination'._wrap(super(ServerPacketHandler, self).destination())

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

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.server.ServerPacketHandler.reply(long)"""
        return 'packets.Packet'._wrap(super(_ServerPacketHandler, self).reply(_long.valueOf(arg0)))

    @overload
    def onModPacket(self, arg0: 'NetworkChannel', arg1: 'ModPacket'):
        """public void dev.ultreon.quantum.network.server.LoginServerPacketHandler.onModPacket(dev.ultreon.quantum.network.NetworkChannel,dev.ultreon.quantum.network.api.packet.ModPacket<?>)"""
        super(_LoginServerPacketHandler, self).onModPacket(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isAsync(self) -> bool:
        """public boolean dev.ultreon.quantum.network.server.LoginServerPacketHandler.isAsync()"""
        return bool._wrap(super(LoginServerPacketHandler, self).isAsync())

    @overload
    def onPlayerLogin(self, arg0: str):
        """public void dev.ultreon.quantum.network.server.LoginServerPacketHandler.onPlayerLogin(java.lang.String)"""
        super(_LoginServerPacketHandler, self).onPlayerLogin(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())