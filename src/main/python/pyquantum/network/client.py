from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
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
import dev.ultreon.quantum.network.client.ClientPacketHandler as _ClientPacketHandler
_ClientPacketHandler = _ClientPacketHandler
try:
    from pyquantum.network import api
except ImportError:
    api = _import_once("pyquantum.network.api")

import dev.ultreon.quantum.network.PacketHandler as _PacketHandler
_PacketHandler = _PacketHandler
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.network.client.LoginClientPacketHandler as _LoginClientPacketHandler
_LoginClientPacketHandler = _LoginClientPacketHandler
 
class LoginClientPacketHandler():
    """dev.ultreon.quantum.network.client.LoginClientPacketHandler"""
 
    @staticmethod
    def _wrap(java_value: _LoginClientPacketHandler) -> 'LoginClientPacketHandler':
        return LoginClientPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoginClientPacketHandler):
        """
        Dynamic initializer for LoginClientPacketHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoginClientPacketHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoginClientPacketHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.client.ClientPacketHandler.destination()"""
        return 'api.PacketDestination'._wrap(super(ClientPacketHandler, self).destination())

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

    @override
    @overload
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(_ClientPacketHandler, self).handleS2CReply(_long.valueOf(arg0))

    @abstractmethod
    def onLoginAccepted(self, arg0: 'UUID'):
        """public abstract void dev.ultreon.quantum.network.client.LoginClientPacketHandler.onLoginAccepted(java.util.UUID)"""
        pass

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'._wrap(super(_ClientPacketHandler, self).reply(_long.valueOf(arg0)))

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

 
 
 
# CLASS: dev.ultreon.quantum.network.client.LoginClientPacketHandler
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
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
import dev.ultreon.quantum.network.client.ClientPacketHandler as _ClientPacketHandler
_ClientPacketHandler = _ClientPacketHandler
try:
    from pyquantum.network import api
except ImportError:
    api = _import_once("pyquantum.network.api")

import dev.ultreon.quantum.network.PacketHandler as _PacketHandler
_PacketHandler = _PacketHandler
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.network.client.LoginClientPacketHandler as _LoginClientPacketHandler
_LoginClientPacketHandler = _LoginClientPacketHandler
 
class LoginClientPacketHandler():
    """dev.ultreon.quantum.network.client.LoginClientPacketHandler"""
 
    @staticmethod
    def _wrap(java_value: _LoginClientPacketHandler) -> 'LoginClientPacketHandler':
        return LoginClientPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoginClientPacketHandler):
        """
        Dynamic initializer for LoginClientPacketHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoginClientPacketHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoginClientPacketHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.client.ClientPacketHandler.destination()"""
        return 'api.PacketDestination'._wrap(super(ClientPacketHandler, self).destination())

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

    @override
    @overload
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(_ClientPacketHandler, self).handleS2CReply(_long.valueOf(arg0))

    @abstractmethod
    def onLoginAccepted(self, arg0: 'UUID'):
        """public abstract void dev.ultreon.quantum.network.client.LoginClientPacketHandler.onLoginAccepted(java.util.UUID)"""
        pass

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'._wrap(super(_ClientPacketHandler, self).reply(_long.valueOf(arg0)))

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

 
 
 
# CLASS: dev.ultreon.quantum.network.client.LoginClientPacketHandler 
 
 
# CLASS: dev.ultreon.quantum.network.client.ClientPacketHandler
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import dev.ultreon.quantum.network.api.PacketDestination as _PacketDestination
_PacketDestination = _PacketDestination
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import dev.ultreon.quantum.network.packets.Packet as _Packet
_Packet = _Packet
import dev.ultreon.quantum.network.client.ClientPacketHandler as _ClientPacketHandler
_ClientPacketHandler = _ClientPacketHandler
from abc import abstractmethod, ABC
try:
    from pyquantum.network import api
except ImportError:
    api = _import_once("pyquantum.network.api")

import dev.ultreon.quantum.network.PacketHandler as _PacketHandler
_PacketHandler = _PacketHandler
from builtins import bool
import java.lang.Long as _long
 
class ClientPacketHandler():
    """dev.ultreon.quantum.network.client.ClientPacketHandler"""
 
    @staticmethod
    def _wrap(java_value: _ClientPacketHandler) -> 'ClientPacketHandler':
        return ClientPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientPacketHandler):
        """
        Dynamic initializer for ClientPacketHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientPacketHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientPacketHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.client.ClientPacketHandler.destination()"""
        return 'api.PacketDestination'._wrap(super(ClientPacketHandler, self).destination())

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
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(_ClientPacketHandler, self).handleS2CReply(_long.valueOf(arg0))

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'._wrap(super(_ClientPacketHandler, self).reply(_long.valueOf(arg0)))

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
 
 
# CLASS: dev.ultreon.quantum.network.client.C2SReplyPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.client.C2SReplyPacket as _C2SReplyPacket
_C2SReplyPacket = _C2SReplyPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class C2SReplyPacket():
    """dev.ultreon.quantum.network.client.C2SReplyPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SReplyPacket) -> 'C2SReplyPacket':
        return C2SReplyPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SReplyPacket):
        """
        Dynamic initializer for C2SReplyPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SReplyPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SReplyPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.network.client.C2SReplyPacket(long)"""
        val = _C2SReplyPacket(_long.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.client.C2SReplyPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SReplyPacket, self).toBytes(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.client.C2SReplyPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SReplyPacket(arg0)
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

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'ServerPacketHandler'):
        """public void dev.ultreon.quantum.network.client.C2SReplyPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.ServerPacketHandler)"""
        super(_C2SReplyPacket, self).handle(arg0, arg1)

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
 
 
# CLASS: dev.ultreon.quantum.network.client.InGameClientPacketHandler
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

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
from abc import abstractmethod, ABC
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pyquantum import collection
except ImportError:
    collection = _import_once("pyquantum.collection")

import dev.ultreon.quantum.network.client.ClientPacketHandler as _ClientPacketHandler
_ClientPacketHandler = _ClientPacketHandler
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.network.client.InGameClientPacketHandler as _InGameClientPacketHandler
_InGameClientPacketHandler = _InGameClientPacketHandler
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

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

try:
    from pyquantum.block import entity
except ImportError:
    entity = _import_once("pyquantum.block.entity")

try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.network.api.PacketDestination as _PacketDestination
_PacketDestination = _PacketDestination
try:
    from pyquantum.network.packets import s2c
except ImportError:
    s2c = _import_once("pyquantum.network.packets.s2c")

try:
    from pyquantum.world import particles
except ImportError:
    particles = _import_once("pyquantum.world.particles")

import java.util.Map as Map
import dev.ultreon.quantum.network.PacketHandler as _PacketHandler
_PacketHandler = _PacketHandler
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.util.List as List
 
class InGameClientPacketHandler():
    """dev.ultreon.quantum.network.client.InGameClientPacketHandler"""
 
    @staticmethod
    def _wrap(java_value: _InGameClientPacketHandler) -> 'InGameClientPacketHandler':
        return InGameClientPacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InGameClientPacketHandler):
        """
        Dynamic initializer for InGameClientPacketHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InGameClientPacketHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InGameClientPacketHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onPlayerHurt(self, arg0: 'S2CPlayerHurtPacket'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onPlayerHurt(dev.ultreon.quantum.network.packets.s2c.S2CPlayerHurtPacket)"""
        pass

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.client.ClientPacketHandler.destination()"""
        return 'api.PacketDestination'._wrap(super(ClientPacketHandler, self).destination())

    @override
    @overload
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(_ClientPacketHandler, self).handleS2CReply(_long.valueOf(arg0))

    @abstractmethod
    def onPing(self, arg0: int, arg1: int):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onPing(long,long)"""
        pass

    @abstractmethod
    def onKeepAlive(self, ):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onKeepAlive()"""
        pass

    @abstractmethod
    def onAddPlayer(self, arg0: 'UUID', arg1: str, arg2: 'Vec3d'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onAddPlayer(java.util.UUID,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
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
    def onAddEntity(self, arg0: int, arg1: 'EntityType', arg2: 'Vec3d', arg3: 'MapType'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onAddEntity(int,dev.ultreon.quantum.entity.EntityType<?>,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.ubo.types.MapType)"""
        pass

    @abstractmethod
    def onTabCompleteResult(self, arg0: 'String'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onTabCompleteResult(java.lang.String[])"""
        pass

    @abstractmethod
    def onInitialPermissions(self, arg0: 'InitialPermissionsPacket'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onInitialPermissions(dev.ultreon.quantum.network.packets.InitialPermissionsPacket)"""
        pass

    @abstractmethod
    def onRespawn(self, arg0: 'Vec3d'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onRespawn(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        pass

    @abstractmethod
    def onCloseContainerMenu(self, ):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onCloseContainerMenu()"""
        pass

    @abstractmethod
    def onPlayerHealth(self, arg0: float):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onPlayerHealth(float)"""
        pass

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'._wrap(super(_ClientPacketHandler, self).reply(_long.valueOf(arg0)))

    @abstractmethod
    def onPlaySound(self, arg0: 'Identifier', arg1: float):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onPlaySound(dev.ultreon.quantum.util.Identifier,float)"""
        pass

    @abstractmethod
    def onModPacket(self, arg0: 'NetworkChannel', arg1: 'ModPacket'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onModPacket(dev.ultreon.quantum.network.NetworkChannel,dev.ultreon.quantum.network.api.packet.ModPacket<?>)"""
        pass

    @abstractmethod
    def onOpenContainerMenu(self, arg0: 'Identifier', arg1: 'List'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onOpenContainerMenu(dev.ultreon.quantum.util.Identifier,java.util.List<dev.ultreon.quantum.item.ItemStack>)"""
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

    @override
    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool._wrap(super(network.PacketHandler, self).isAsync())

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
    def onRemovePermission(self, arg0: 'RemovePermissionPacket'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onRemovePermission(dev.ultreon.quantum.network.packets.RemovePermissionPacket)"""
        pass

    @abstractmethod
    def onMenuItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public abstract void dev.ultreon.quantum.network.client.InGameClientPacketHandler.onMenuItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        pass

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool._wrap(super(_network.PacketHandler, self).shouldHandlePacket(arg0))

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