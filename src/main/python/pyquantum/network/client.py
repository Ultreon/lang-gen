from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
import dev.ultreon.quantum.network.api.PacketDestination as __PacketDestination
__PacketDestination = __PacketDestination
import dev.ultreon.quantum.network.client.ClientPacketHandler as __ClientPacketHandler
__ClientPacketHandler = __ClientPacketHandler
import java.lang.Long as __long
import dev.ultreon.quantum.network.PacketHandler as __PacketHandler
__PacketHandler = __PacketHandler
import dev.ultreon.quantum.network.packets.Packet as __Packet
__Packet = __Packet
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.network.client.LoginClientPacketHandler as __LoginClientPacketHandler
__LoginClientPacketHandler = __LoginClientPacketHandler
try:
    from pyquantum.network import api
except ImportError:
    api = __import_once__("pyquantum.network.api")

from builtins import bool
 
class LoginClientPacketHandler(ABC, __ClientPacketHandler, ClientPacketHandler):
    """dev.ultreon.quantum.network.client.LoginClientPacketHandler"""
 
    @staticmethod
    def __wrap(java_value: __LoginClientPacketHandler) -> 'LoginClientPacketHandler':
        return LoginClientPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoginClientPacketHandler):
        """
        Dynamic initializer for LoginClientPacketHandler.
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
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'.__wrap(super(__ClientPacketHandler, self).reply(__long.valueOf(arg0)))

    @override
    @overload
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(__ClientPacketHandler, self).handleS2CReply(__long.valueOf(arg0))

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.client.ClientPacketHandler.destination()"""
        return 'api.PacketDestination'.__wrap(super(ClientPacketHandler, self).destination())

    @abstractmethod
    def context(self, ):
        """public abstract dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.network.PacketHandler.context()"""
        pass

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool.__wrap(super(__network.PacketHandler, self).shouldHandlePacket(arg0))

    @abstractmethod
    def onLoginAccepted(self, arg0: 'UUID'):
        """public abstract void dev.ultreon.quantum.network.client.LoginClientPacketHandler.onLoginAccepted(java.util.UUID)"""
        pass

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

    @override
    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool.__wrap(super(network.PacketHandler, self).isAsync())

 
 
 
# CLASS: dev.ultreon.quantum.network.client.LoginClientPacketHandler
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
import dev.ultreon.quantum.network.api.PacketDestination as __PacketDestination
__PacketDestination = __PacketDestination
import dev.ultreon.quantum.network.client.ClientPacketHandler as __ClientPacketHandler
__ClientPacketHandler = __ClientPacketHandler
import java.lang.Long as __long
import dev.ultreon.quantum.network.PacketHandler as __PacketHandler
__PacketHandler = __PacketHandler
import dev.ultreon.quantum.network.packets.Packet as __Packet
__Packet = __Packet
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.network.client.LoginClientPacketHandler as __LoginClientPacketHandler
__LoginClientPacketHandler = __LoginClientPacketHandler
try:
    from pyquantum.network import api
except ImportError:
    api = __import_once__("pyquantum.network.api")

from builtins import bool
 
class LoginClientPacketHandler(ABC, __ClientPacketHandler, ClientPacketHandler):
    """dev.ultreon.quantum.network.client.LoginClientPacketHandler"""
 
    @staticmethod
    def __wrap(java_value: __LoginClientPacketHandler) -> 'LoginClientPacketHandler':
        return LoginClientPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoginClientPacketHandler):
        """
        Dynamic initializer for LoginClientPacketHandler.
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
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'.__wrap(super(__ClientPacketHandler, self).reply(__long.valueOf(arg0)))

    @override
    @overload
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(__ClientPacketHandler, self).handleS2CReply(__long.valueOf(arg0))

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.client.ClientPacketHandler.destination()"""
        return 'api.PacketDestination'.__wrap(super(ClientPacketHandler, self).destination())

    @abstractmethod
    def context(self, ):
        """public abstract dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.network.PacketHandler.context()"""
        pass

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool.__wrap(super(__network.PacketHandler, self).shouldHandlePacket(arg0))

    @abstractmethod
    def onLoginAccepted(self, arg0: 'UUID'):
        """public abstract void dev.ultreon.quantum.network.client.LoginClientPacketHandler.onLoginAccepted(java.util.UUID)"""
        pass

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

    @override
    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool.__wrap(super(network.PacketHandler, self).isAsync())

 
 
 
# CLASS: dev.ultreon.quantum.network.client.LoginClientPacketHandler 
 
 
# CLASS: dev.ultreon.quantum.network.client.ClientPacketHandler
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.network.client.ClientPacketHandler as __ClientPacketHandler
__ClientPacketHandler = __ClientPacketHandler
import dev.ultreon.quantum.network.api.PacketDestination as __PacketDestination
__PacketDestination = __PacketDestination
import java.lang.Long as __long
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
 
class ClientPacketHandler(ABC, pyquantum.__PacketHandler, network.PacketHandler):
    """dev.ultreon.quantum.network.client.ClientPacketHandler"""
 
    @staticmethod
    def __wrap(java_value: __ClientPacketHandler) -> 'ClientPacketHandler':
        return ClientPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientPacketHandler):
        """
        Dynamic initializer for ClientPacketHandler.
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
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'.__wrap(super(__ClientPacketHandler, self).reply(__long.valueOf(arg0)))

    @overload
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(__ClientPacketHandler, self).handleS2CReply(__long.valueOf(arg0))

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.client.ClientPacketHandler.destination()"""
        return 'api.PacketDestination'.__wrap(super(ClientPacketHandler, self).destination())

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
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool.__wrap(super(network.PacketHandler, self).isAsync()) 
 
 
# CLASS: dev.ultreon.quantum.network.client.C2SReplyPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
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
import dev.ultreon.quantum.network.client.C2SReplyPacket as __C2SReplyPacket
__C2SReplyPacket = __C2SReplyPacket
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SReplyPacket(network.__Packet, packets.Packet, pyquantum.__ReplyPacket, network.ReplyPacket):
    """dev.ultreon.quantum.network.client.C2SReplyPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SReplyPacket) -> 'C2SReplyPacket':
        return C2SReplyPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SReplyPacket):
        """
        Dynamic initializer for C2SReplyPacket.
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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.client.C2SReplyPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SReplyPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'ServerPacketHandler'):
        """public void dev.ultreon.quantum.network.client.C2SReplyPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.ServerPacketHandler)"""
        super(__C2SReplyPacket, self).handle(arg0, arg1)

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
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.network.client.C2SReplyPacket(long)"""
        val = __C2SReplyPacket(__long.valueOf(arg0))
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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.client.C2SReplyPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SReplyPacket, self).toBytes(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.client.InGameClientPacketHandler
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

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

from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum import collection
except ImportError:
    collection = __import_once__("pyquantum.collection")

import dev.ultreon.quantum.network.client.InGameClientPacketHandler as __InGameClientPacketHandler
__InGameClientPacketHandler = __InGameClientPacketHandler
import dev.ultreon.quantum.network.PacketHandler as __PacketHandler
__PacketHandler = __PacketHandler
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.network.client.ClientPacketHandler as __ClientPacketHandler
__ClientPacketHandler = __ClientPacketHandler
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

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
    from pyquantum.block import entity
except ImportError:
    entity = __import_once__("pyquantum.block.entity")

try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

try:
    from pyquantum.network.packets import s2c
except ImportError:
    s2c = __import_once__("pyquantum.network.packets.s2c")

try:
    from pyquantum.world import particles
except ImportError:
    particles = __import_once__("pyquantum.world.particles")

import java.util.Map as Map
import java.util.List as List
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class InGameClientPacketHandler(ABC, __ClientPacketHandler, ClientPacketHandler):
    """dev.ultreon.quantum.network.client.InGameClientPacketHandler"""
 
    @staticmethod
    def __wrap(java_value: __InGameClientPacketHandler) -> 'InGameClientPacketHandler':
        return InGameClientPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InGameClientPacketHandler):
        """
        Dynamic initializer for InGameClientPacketHandler.
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
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'.__wrap(super(__ClientPacketHandler, self).reply(__long.valueOf(arg0)))

    @abstractmethod
    def onPlayerHurt(self, arg0: 'S2CPlayerHurtPacket'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onPlayerHurt(dev.ultreon.quantum.network.packets.s2c.S2CPlayerHurtPacket)"""
        pass

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.client.ClientPacketHandler.destination()"""
        return 'api.PacketDestination'.__wrap(super(ClientPacketHandler, self).destination())

    @abstractmethod
    def onPing(self, arg0: int, arg1: int):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onPing(long,long)"""
        pass

    @abstractmethod
    def onAddPlayer(self, arg0: 'UUID', arg1: str, arg2: 'Vec3d'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onAddPlayer(java.util.UUID,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        pass

    @abstractmethod
    def onKeepAlive(self, ):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onKeepAlive()"""
        pass

    @abstractmethod
    def isAcceptingPackets(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isAcceptingPackets()"""
        pass

    @abstractmethod
    def isDisconnected(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isDisconnected()"""
        pass

    @abstractmethod
    def onSpawnParticles(self, arg0: 'ParticleType', arg1: 'Vec3d', arg2: 'Vec3d', arg3: int):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onSpawnParticles(dev.ultreon.quantum.world.particles.ParticleType,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,int)"""
        pass

    @abstractmethod
    def onTabCompleteResult(self, arg0: 'String'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onTabCompleteResult(java.lang.String[])"""
        pass

    @abstractmethod
    def onAddEntity(self, arg0: int, arg1: 'EntityType', arg2: 'Vec3d', arg3: 'MapType'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onAddEntity(int,dev.ultreon.quantum.entity.EntityType<?>,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.ubo.types.MapType)"""
        pass

    @abstractmethod
    def onInitialPermissions(self, arg0: 'InitialPermissionsPacket'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onInitialPermissions(dev.ultreon.quantum.network.packets.InitialPermissionsPacket)"""
        pass

    @abstractmethod
    def onRespawn(self, arg0: 'Vec3d'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onRespawn(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        pass

    @override
    @overload
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(__ClientPacketHandler, self).handleS2CReply(__long.valueOf(arg0))

    @abstractmethod
    def onCloseContainerMenu(self, ):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onCloseContainerMenu()"""
        pass

    @abstractmethod
    def onPlayerHealth(self, arg0: float):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onPlayerHealth(float)"""
        pass

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool.__wrap(super(__network.PacketHandler, self).shouldHandlePacket(arg0))

    @abstractmethod
    def onPlaySound(self, arg0: 'Identifier', arg1: float):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onPlaySound(dev.ultreon.quantum.util.Identifier,float)"""
        pass

    @abstractmethod
    def onOpenContainerMenu(self, arg0: 'Identifier', arg1: 'List'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onOpenContainerMenu(dev.ultreon.quantum.util.Identifier,java.util.List<dev.ultreon.quantum.item.ItemStack>)"""
        pass

    @abstractmethod
    def onModPacket(self, arg0: 'NetworkChannel', arg1: 'ModPacket'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onModPacket(dev.ultreon.quantum.network.NetworkChannel,dev.ultreon.quantum.network.api.packet.ModPacket<?>)"""
        pass

    @abstractmethod
    def onBlockSet(self, arg0: 'BlockPos', arg1: 'BlockProperties'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onBlockSet(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        pass

    @abstractmethod
    def onPlayerSetPos(self, arg0: 'Vec3d'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onPlayerSetPos(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        pass

    @abstractmethod
    def onMenuCursorChanged(self, arg0: 'ItemStack'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onMenuCursorChanged(dev.ultreon.quantum.item.ItemStack)"""
        pass

    @abstractmethod
    def onTimeChange(self, arg0: 'PacketContext', arg1: 'Operation', arg2: int):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onTimeChange(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.packets.s2c.S2CTimePacket$Operation,int)"""
        pass

    @abstractmethod
    def onAddPermission(self, arg0: 'AddPermissionPacket'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onAddPermission(dev.ultreon.quantum.network.packets.AddPermissionPacket)"""
        pass

    @abstractmethod
    def onChatReceived(self, arg0: 'TextObject'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onChatReceived(dev.ultreon.quantum.text.TextObject)"""
        pass

    @abstractmethod
    def context(self, ):
        """public abstract dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.network.PacketHandler.context()"""
        pass

    @abstractmethod
    def onEntityPipeline(self, arg0: int, arg1: 'MapType'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onEntityPipeline(int,dev.ultreon.ubo.types.MapType)"""
        pass

    @abstractmethod
    def onChunkCancel(self, arg0: 'ChunkPos'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onChunkCancel(dev.ultreon.quantum.world.ChunkPos)"""
        pass

    @abstractmethod
    def onChunkData(self, arg0: 'ChunkPos', arg1: 'Storage', arg2: 'Storage', arg3: 'Map'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onChunkData(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.block.state.BlockProperties>,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.world.Biome>,java.util.Map<dev.ultreon.quantum.world.BlockPos, dev.ultreon.quantum.block.entity.BlockEntityType<?>>)"""
        pass

    @abstractmethod
    def onBlockEntitySet(self, arg0: 'BlockPos', arg1: 'BlockEntityType'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onBlockEntitySet(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.entity.BlockEntityType<?>)"""
        pass

    @override
    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool.__wrap(super(network.PacketHandler, self).isAsync())

    @abstractmethod
    def onPlayerPosition(self, arg0: 'PacketContext', arg1: 'UUID', arg2: 'Vec3d'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onPlayerPosition(dev.ultreon.quantum.network.PacketContext,java.util.UUID,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        pass

    @abstractmethod
    def onGamemode(self, arg0: 'GameMode'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onGamemode(dev.ultreon.quantum.util.GameMode)"""
        pass

    @abstractmethod
    def onInventoryItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onInventoryItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        pass

    @abstractmethod
    def onMenuItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onMenuItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        pass

    @abstractmethod
    def onRemovePermission(self, arg0: 'RemovePermissionPacket'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onRemovePermission(dev.ultreon.quantum.network.packets.RemovePermissionPacket)"""
        pass

    @abstractmethod
    def onDisconnect(self, arg0: str):
        """public abstract void dev.ultreon.quantum.network.PacketHandler.onDisconnect(java.lang.String)"""
        pass

    @abstractmethod
    def onRemoveEntity(self, arg0: int):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onRemoveEntity(int)"""
        pass

    @abstractmethod
    def getChannel(self, arg0: 'Identifier'):
        """public abstract dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.client.InGameClientPacketHandler.getChannel(dev.ultreon.quantum.util.Identifier)"""
        pass

    @abstractmethod
    def onAbilities(self, arg0: 'AbilitiesPacket'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onAbilities(dev.ultreon.quantum.network.packets.AbilitiesPacket)"""
        pass

    @abstractmethod
    def onRemovePlayer(self, arg0: 'UUID'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onRemovePlayer(java.util.UUID)"""
        pass

    @abstractmethod
    def onPlayerAttack(self, arg0: int, arg1: int):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onPlayerAttack(int,int)"""
        pass