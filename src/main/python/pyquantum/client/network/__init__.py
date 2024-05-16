from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl as _LoginClientPacketHandlerImpl
_LoginClientPacketHandlerImpl = _LoginClientPacketHandlerImpl
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import dev.ultreon.quantum.network.packets.Packet as _Packet
_Packet = _Packet
import java.lang.String as _String
_String = _String
try:
    from pyquantum.network import api
except ImportError:
    api = _import_once("pyquantum.network.api")

import java.lang.String as _string
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.api.PacketDestination as _PacketDestination
_PacketDestination = _PacketDestination
import dev.ultreon.quantum.network.client.ClientPacketHandler as _ClientPacketHandler
_ClientPacketHandler = _ClientPacketHandler
import dev.ultreon.quantum.network.PacketContext as _PacketContext
_PacketContext = _PacketContext
from builtins import bool
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
 
class LoginClientPacketHandlerImpl():
    """dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl"""
 
    @staticmethod
    def _wrap(java_value: _LoginClientPacketHandlerImpl) -> 'LoginClientPacketHandlerImpl':
        return LoginClientPacketHandlerImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoginClientPacketHandlerImpl):
        """
        Dynamic initializer for LoginClientPacketHandlerImpl.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoginClientPacketHandlerImpl__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoginClientPacketHandlerImpl__wrapper":
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
    def isDisconnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.isDisconnected()"""
        return bool._wrap(super(LoginClientPacketHandlerImpl, self).isDisconnected())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def context(self) -> 'network.PacketContext':
        """public dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.context()"""
        return 'network.PacketContext'._wrap(super(LoginClientPacketHandlerImpl, self).context())

    @override
    @overload
    def onLoginAccepted(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.onLoginAccepted(java.util.UUID)"""
        super(_LoginClientPacketHandlerImpl, self).onLoginAccepted(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isAsync(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.isAsync()"""
        return bool._wrap(super(LoginClientPacketHandlerImpl, self).isAsync())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def onDisconnect(self, arg0: str):
        """public void dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.onDisconnect(java.lang.String)"""
        super(_LoginClientPacketHandlerImpl, self).onDisconnect(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool._wrap(super(_network.PacketHandler, self).shouldHandlePacket(arg0))

    @override
    @overload
    def isAcceptingPackets(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.isAcceptingPackets()"""
        return bool._wrap(super(LoginClientPacketHandlerImpl, self).isAcceptingPackets())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.client.ClientPacketHandler.destination()"""
        return 'api.PacketDestination'._wrap(super(client.ClientPacketHandler, self).destination())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'._wrap(super(_client.ClientPacketHandler, self).reply(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'IConnection'):
        """public dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl(dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        val = _LoginClientPacketHandlerImpl(arg0)
        self.__wrapper = val

    @override
    @overload
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(_client.ClientPacketHandler, self).handleS2CReply(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl as _LoginClientPacketHandlerImpl
_LoginClientPacketHandlerImpl = _LoginClientPacketHandlerImpl
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import dev.ultreon.quantum.network.packets.Packet as _Packet
_Packet = _Packet
import java.lang.String as _String
_String = _String
try:
    from pyquantum.network import api
except ImportError:
    api = _import_once("pyquantum.network.api")

import java.lang.String as _string
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.api.PacketDestination as _PacketDestination
_PacketDestination = _PacketDestination
import dev.ultreon.quantum.network.client.ClientPacketHandler as _ClientPacketHandler
_ClientPacketHandler = _ClientPacketHandler
import dev.ultreon.quantum.network.PacketContext as _PacketContext
_PacketContext = _PacketContext
from builtins import bool
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
 
class LoginClientPacketHandlerImpl():
    """dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl"""
 
    @staticmethod
    def _wrap(java_value: _LoginClientPacketHandlerImpl) -> 'LoginClientPacketHandlerImpl':
        return LoginClientPacketHandlerImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoginClientPacketHandlerImpl):
        """
        Dynamic initializer for LoginClientPacketHandlerImpl.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoginClientPacketHandlerImpl__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoginClientPacketHandlerImpl__wrapper":
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
    def isDisconnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.isDisconnected()"""
        return bool._wrap(super(LoginClientPacketHandlerImpl, self).isDisconnected())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def context(self) -> 'network.PacketContext':
        """public dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.context()"""
        return 'network.PacketContext'._wrap(super(LoginClientPacketHandlerImpl, self).context())

    @override
    @overload
    def onLoginAccepted(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.onLoginAccepted(java.util.UUID)"""
        super(_LoginClientPacketHandlerImpl, self).onLoginAccepted(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isAsync(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.isAsync()"""
        return bool._wrap(super(LoginClientPacketHandlerImpl, self).isAsync())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def onDisconnect(self, arg0: str):
        """public void dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.onDisconnect(java.lang.String)"""
        super(_LoginClientPacketHandlerImpl, self).onDisconnect(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool._wrap(super(_network.PacketHandler, self).shouldHandlePacket(arg0))

    @override
    @overload
    def isAcceptingPackets(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.isAcceptingPackets()"""
        return bool._wrap(super(LoginClientPacketHandlerImpl, self).isAcceptingPackets())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.client.ClientPacketHandler.destination()"""
        return 'api.PacketDestination'._wrap(super(client.ClientPacketHandler, self).destination())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'._wrap(super(_client.ClientPacketHandler, self).reply(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'IConnection'):
        """public dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl(dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        val = _LoginClientPacketHandlerImpl(arg0)
        self.__wrapper = val

    @override
    @overload
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(_client.ClientPacketHandler, self).handleS2CReply(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl 
 
 
# CLASS: dev.ultreon.quantum.client.network.ClientNetwork
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.network.api.Network as _Network
_Network = _Network
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

import dev.ultreon.quantum.client.network.ClientNetwork as _ClientNetwork
_ClientNetwork = _ClientNetwork
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientNetwork():
    """dev.ultreon.quantum.client.network.ClientNetwork"""
 
    @staticmethod
    def _wrap(java_value: _ClientNetwork) -> 'ClientNetwork':
        return ClientNetwork(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientNetwork):
        """
        Dynamic initializer for ClientNetwork.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientNetwork__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientNetwork__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def init(self):
        """public final void dev.ultreon.quantum.network.api.Network.init()"""
        super(api.Network, self).init()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def namespace(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.network.api.Network.namespace()"""
        return str._wrap(super(api.Network, self).namespace())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.network.api.Network.getId()"""
        return 'util.Identifier'._wrap(super(api.Network, self).getId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def sendToServer(self, arg0: 'ModPacket'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ServerEndpoint> void dev.ultreon.quantum.client.network.ClientNetwork.sendToServer(T)"""
        super(_ClientNetwork, self).sendToServer(arg0)

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
    def channelName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.network.api.Network.channelName()"""
        return str._wrap(super(api.Network, self).channelName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def sendToClient(self, arg0: 'ModPacket', arg1: 'ServerPlayer'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ClientEndpoint> void dev.ultreon.quantum.network.api.Network.sendToClient(dev.ultreon.quantum.network.api.packet.ModPacket<T>,dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_api.Network, self).sendToClient(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
import dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl as _InGameClientPacketHandlerImpl
_InGameClientPacketHandlerImpl = _InGameClientPacketHandlerImpl
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

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

import java.lang.String as _string
import dev.ultreon.quantum.network.client.ClientPacketHandler as _ClientPacketHandler
_ClientPacketHandler = _ClientPacketHandler
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
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

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

import java.lang.Float as _float
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

try:
    from pyquantum.block import entity
except ImportError:
    entity = _import_once("pyquantum.block.entity")

import java.lang.Integer as _int
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
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InGameClientPacketHandlerImpl():
    """dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl"""
 
    @staticmethod
    def _wrap(java_value: _InGameClientPacketHandlerImpl) -> 'InGameClientPacketHandlerImpl':
        return InGameClientPacketHandlerImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InGameClientPacketHandlerImpl):
        """
        Dynamic initializer for InGameClientPacketHandlerImpl.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InGameClientPacketHandlerImpl__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InGameClientPacketHandlerImpl__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def onInitialPermissions(self, arg0: 'InitialPermissionsPacket'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onInitialPermissions(dev.ultreon.quantum.network.packets.InitialPermissionsPacket)"""
        super(_InGameClientPacketHandlerImpl, self).onInitialPermissions(arg0)

    @override
    @overload
    def onChatReceived(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onChatReceived(dev.ultreon.quantum.text.TextObject)"""
        super(_InGameClientPacketHandlerImpl, self).onChatReceived(arg0)

    @override
    @overload
    def onInventoryItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onInventoryItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        super(_InGameClientPacketHandlerImpl, self).onInventoryItemChanged(_int.valueOf(arg0), arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def onRemovePlayer(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onRemovePlayer(java.util.UUID)"""
        super(_InGameClientPacketHandlerImpl, self).onRemovePlayer(arg0)

    @override
    @overload
    def onPlaySound(self, arg0: 'Identifier', arg1: float):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPlaySound(dev.ultreon.quantum.util.Identifier,float)"""
        super(_InGameClientPacketHandlerImpl, self).onPlaySound(arg0, _float.valueOf(arg1))

    @override
    @overload
    def onOpenContainerMenu(self, arg0: 'Identifier', arg1: 'List'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onOpenContainerMenu(dev.ultreon.quantum.util.Identifier,java.util.List<dev.ultreon.quantum.item.ItemStack>)"""
        super(_InGameClientPacketHandlerImpl, self).onOpenContainerMenu(arg0, arg1)

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
    def onRemovePermission(self, arg0: 'RemovePermissionPacket'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onRemovePermission(dev.ultreon.quantum.network.packets.RemovePermissionPacket)"""
        super(_InGameClientPacketHandlerImpl, self).onRemovePermission(arg0)

    @override
    @overload
    def onAddPermission(self, arg0: 'AddPermissionPacket'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onAddPermission(dev.ultreon.quantum.network.packets.AddPermissionPacket)"""
        super(_InGameClientPacketHandlerImpl, self).onAddPermission(arg0)

    @override
    @overload
    def onTimeChange(self, arg0: 'PacketContext', arg1: 'Operation', arg2: int):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onTimeChange(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.packets.s2c.S2CTimePacket$Operation,int)"""
        super(_InGameClientPacketHandlerImpl, self).onTimeChange(arg0, arg1, _int.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def onCloseContainerMenu(self):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onCloseContainerMenu()"""
        super(InGameClientPacketHandlerImpl, self).onCloseContainerMenu()

    @override
    @overload
    def onRemoveEntity(self, arg0: int):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onRemoveEntity(int)"""
        super(_InGameClientPacketHandlerImpl, self).onRemoveEntity(_int.valueOf(arg0))

    @override
    @overload
    def onPing(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPing(long,long)"""
        super(_InGameClientPacketHandlerImpl, self).onPing(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def registerChannel(self, arg0: 'Identifier') -> 'network.NetworkChannel':
        """public dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.registerChannel(dev.ultreon.quantum.util.Identifier)"""
        return 'network.NetworkChannel'._wrap(super(_InGameClientPacketHandlerImpl, self).registerChannel(arg0))

    @override
    @overload
    def onRespawn(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onRespawn(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_InGameClientPacketHandlerImpl, self).onRespawn(arg0)

    @override
    @overload
    def onPlayerSetPos(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPlayerSetPos(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_InGameClientPacketHandlerImpl, self).onPlayerSetPos(arg0)

    @override
    @overload
    def onDisconnect(self, arg0: str):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onDisconnect(java.lang.String)"""
        super(_InGameClientPacketHandlerImpl, self).onDisconnect(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def onPlayerHurt(self, arg0: 'S2CPlayerHurtPacket'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPlayerHurt(dev.ultreon.quantum.network.packets.s2c.S2CPlayerHurtPacket)"""
        super(_InGameClientPacketHandlerImpl, self).onPlayerHurt(arg0)

    @override
    @overload
    def onAbilities(self, arg0: 'AbilitiesPacket'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onAbilities(dev.ultreon.quantum.network.packets.AbilitiesPacket)"""
        super(_InGameClientPacketHandlerImpl, self).onAbilities(arg0)

    @override
    @overload
    def isAcceptingPackets(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.isAcceptingPackets()"""
        return bool._wrap(super(InGameClientPacketHandlerImpl, self).isAcceptingPackets())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'._wrap(super(_client.ClientPacketHandler, self).reply(_long.valueOf(arg0)))

    @override
    @overload
    def onModPacket(self, arg0: 'NetworkChannel', arg1: 'ModPacket'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onModPacket(dev.ultreon.quantum.network.NetworkChannel,dev.ultreon.quantum.network.api.packet.ModPacket<?>)"""
        super(_InGameClientPacketHandlerImpl, self).onModPacket(arg0, arg1)

    @overload
    def __init__(self, arg0: 'IConnection'):
        """public dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl(dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        val = _InGameClientPacketHandlerImpl(arg0)
        self.__wrapper = val

    @override
    @overload
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(_client.ClientPacketHandler, self).handleS2CReply(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def onAddEntity(self, arg0: int, arg1: 'EntityType', arg2: 'Vec3d', arg3: 'MapType'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onAddEntity(int,dev.ultreon.quantum.entity.EntityType<?>,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.ubo.types.MapType)"""
        super(_InGameClientPacketHandlerImpl, self).onAddEntity(_int.valueOf(arg0), arg1, arg2, arg3)

    @staticmethod
    @overload
    def byteArrayToHexString(arg0: bytes) -> str:
        """public static java.lang.String dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.byteArrayToHexString(byte[])"""
        return str._wrap(_InGameClientPacketHandlerImpl.byteArrayToHexString(bytes))

    @override
    @overload
    def onBlockSet(self, arg0: 'BlockPos', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onBlockSet(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_InGameClientPacketHandlerImpl, self).onBlockSet(arg0, arg1)

    @override
    @overload
    def onKeepAlive(self):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onKeepAlive()"""
        super(InGameClientPacketHandlerImpl, self).onKeepAlive()

    @override
    @overload
    def isDisconnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.isDisconnected()"""
        return bool._wrap(super(InGameClientPacketHandlerImpl, self).isDisconnected())

    @override
    @overload
    def onMenuItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onMenuItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        super(_InGameClientPacketHandlerImpl, self).onMenuItemChanged(_int.valueOf(arg0), arg1)

    @overload
    def getChannel(self, arg0: 'Identifier') -> 'network.NetworkChannel':
        """public dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.getChannel(dev.ultreon.quantum.util.Identifier)"""
        return 'network.NetworkChannel'._wrap(super(_InGameClientPacketHandlerImpl, self).getChannel(arg0))

    @override
    @overload
    def onBlockEntitySet(self, arg0: 'BlockPos', arg1: 'BlockEntityType'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onBlockEntitySet(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.entity.BlockEntityType<?>)"""
        super(_InGameClientPacketHandlerImpl, self).onBlockEntitySet(arg0, arg1)

    @override
    @overload
    def onGamemode(self, arg0: 'GameMode'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onGamemode(dev.ultreon.quantum.util.GameMode)"""
        super(_InGameClientPacketHandlerImpl, self).onGamemode(arg0)

    @override
    @overload
    def onPlayerHealth(self, arg0: float):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPlayerHealth(float)"""
        super(_InGameClientPacketHandlerImpl, self).onPlayerHealth(_float.valueOf(arg0))

    @override
    @overload
    def onSpawnParticles(self, arg0: 'ParticleType', arg1: 'Vec3d', arg2: 'Vec3d', arg3: int):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onSpawnParticles(dev.ultreon.quantum.world.particles.ParticleType,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,int)"""
        super(_InGameClientPacketHandlerImpl, self).onSpawnParticles(arg0, arg1, arg2, _int.valueOf(arg3))

    @override
    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool._wrap(super(network.PacketHandler, self).isAsync())

    @override
    @overload
    def onPlayerAttack(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPlayerAttack(int,int)"""
        super(_InGameClientPacketHandlerImpl, self).onPlayerAttack(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onTabCompleteResult(self, arg0: 'String'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onTabCompleteResult(java.lang.String[])"""
        super(_InGameClientPacketHandlerImpl, self).onTabCompleteResult(arg0)

    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.getPing()"""
        return int._wrap(super(InGameClientPacketHandlerImpl, self).getPing())

    @override
    @overload
    def onMenuCursorChanged(self, arg0: 'ItemStack'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onMenuCursorChanged(dev.ultreon.quantum.item.ItemStack)"""
        super(_InGameClientPacketHandlerImpl, self).onMenuCursorChanged(arg0)

    @override
    @overload
    def onChunkData(self, arg0: 'ChunkPos', arg1: 'Storage', arg2: 'Storage', arg3: 'Map'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onChunkData(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.block.state.BlockProperties>,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.world.Biome>,java.util.Map<dev.ultreon.quantum.world.BlockPos, dev.ultreon.quantum.block.entity.BlockEntityType<?>>)"""
        super(_InGameClientPacketHandlerImpl, self).onChunkData(arg0, arg1, arg2, arg3)

    @override
    @overload
    def onChunkCancel(self, arg0: 'ChunkPos'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onChunkCancel(dev.ultreon.quantum.world.ChunkPos)"""
        super(_InGameClientPacketHandlerImpl, self).onChunkCancel(arg0)

    @override
    @overload
    def onAddPlayer(self, arg0: 'UUID', arg1: str, arg2: 'Vec3d'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onAddPlayer(java.util.UUID,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_InGameClientPacketHandlerImpl, self).onAddPlayer(arg0, arg1, arg2)

    @override
    @overload
    def onEntityPipeline(self, arg0: int, arg1: 'MapType'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onEntityPipeline(int,dev.ultreon.ubo.types.MapType)"""
        super(_InGameClientPacketHandlerImpl, self).onEntityPipeline(_int.valueOf(arg0), arg1)

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool._wrap(super(_network.PacketHandler, self).shouldHandlePacket(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def onPlayerPosition(self, arg0: 'PacketContext', arg1: 'UUID', arg2: 'Vec3d'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPlayerPosition(dev.ultreon.quantum.network.PacketContext,java.util.UUID,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_InGameClientPacketHandlerImpl, self).onPlayerPosition(arg0, arg1, arg2)

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.destination()"""
        return 'api.PacketDestination'._wrap(super(InGameClientPacketHandlerImpl, self).destination())

    @override
    @overload
    def context(self) -> 'network.PacketContext':
        """public dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.context()"""
        return 'network.PacketContext'._wrap(super(InGameClientPacketHandlerImpl, self).context())