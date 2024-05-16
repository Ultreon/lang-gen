from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
from builtins import str
import dev.ultreon.quantum.network.client.ClientPacketHandler as __ClientPacketHandler
__ClientPacketHandler = __ClientPacketHandler
from pyquantum_helper import override
import dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl as __LoginClientPacketHandlerImpl
__LoginClientPacketHandlerImpl = __LoginClientPacketHandlerImpl
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.packets.Packet as __Packet
__Packet = __Packet
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

try:
    from pyquantum.network import api
except ImportError:
    api = __import_once__("pyquantum.network.api")

import java.lang.Long as __long
import dev.ultreon.quantum.network.api.PacketDestination as __PacketDestination
__PacketDestination = __PacketDestination
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.network.PacketHandler as __PacketHandler
__PacketHandler = __PacketHandler
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
 
class LoginClientPacketHandlerImpl(network.__LoginClientPacketHandler, client.LoginClientPacketHandler):
    """dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl"""
 
    @staticmethod
    def __wrap(java_value: __LoginClientPacketHandlerImpl) -> 'LoginClientPacketHandlerImpl':
        return LoginClientPacketHandlerImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoginClientPacketHandlerImpl):
        """
        Dynamic initializer for LoginClientPacketHandlerImpl.
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
    def isDisconnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.isDisconnected()"""
        return bool.__wrap(super(LoginClientPacketHandlerImpl, self).isDisconnected())

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
    def __init__(self, arg0: 'IConnection'):
        """public dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl(dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        val = __LoginClientPacketHandlerImpl(arg0)
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
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'.__wrap(super(__client.ClientPacketHandler, self).reply(__long.valueOf(arg0)))

    @override
    @overload
    def onLoginAccepted(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.onLoginAccepted(java.util.UUID)"""
        super(__LoginClientPacketHandlerImpl, self).onLoginAccepted(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(__client.ClientPacketHandler, self).handleS2CReply(__long.valueOf(arg0))

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool.__wrap(super(__network.PacketHandler, self).shouldHandlePacket(arg0))

    @override
    @overload
    def onDisconnect(self, arg0: str):
        """public void dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.onDisconnect(java.lang.String)"""
        super(__LoginClientPacketHandlerImpl, self).onDisconnect(arg0)

    @override
    @overload
    def isAcceptingPackets(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.isAcceptingPackets()"""
        return bool.__wrap(super(LoginClientPacketHandlerImpl, self).isAcceptingPackets())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.client.ClientPacketHandler.destination()"""
        return 'api.PacketDestination'.__wrap(super(client.ClientPacketHandler, self).destination())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isAsync(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.isAsync()"""
        return bool.__wrap(super(LoginClientPacketHandlerImpl, self).isAsync())

    @override
    @overload
    def context(self) -> 'network.PacketContext':
        """public dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.context()"""
        return 'network.PacketContext'.__wrap(super(LoginClientPacketHandlerImpl, self).context())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
from builtins import str
import dev.ultreon.quantum.network.client.ClientPacketHandler as __ClientPacketHandler
__ClientPacketHandler = __ClientPacketHandler
from pyquantum_helper import override
import dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl as __LoginClientPacketHandlerImpl
__LoginClientPacketHandlerImpl = __LoginClientPacketHandlerImpl
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.packets.Packet as __Packet
__Packet = __Packet
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

try:
    from pyquantum.network import api
except ImportError:
    api = __import_once__("pyquantum.network.api")

import java.lang.Long as __long
import dev.ultreon.quantum.network.api.PacketDestination as __PacketDestination
__PacketDestination = __PacketDestination
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.network.PacketHandler as __PacketHandler
__PacketHandler = __PacketHandler
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
 
class LoginClientPacketHandlerImpl(network.__LoginClientPacketHandler, client.LoginClientPacketHandler):
    """dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl"""
 
    @staticmethod
    def __wrap(java_value: __LoginClientPacketHandlerImpl) -> 'LoginClientPacketHandlerImpl':
        return LoginClientPacketHandlerImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoginClientPacketHandlerImpl):
        """
        Dynamic initializer for LoginClientPacketHandlerImpl.
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
    def isDisconnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.isDisconnected()"""
        return bool.__wrap(super(LoginClientPacketHandlerImpl, self).isDisconnected())

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
    def __init__(self, arg0: 'IConnection'):
        """public dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl(dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        val = __LoginClientPacketHandlerImpl(arg0)
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
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'.__wrap(super(__client.ClientPacketHandler, self).reply(__long.valueOf(arg0)))

    @override
    @overload
    def onLoginAccepted(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.onLoginAccepted(java.util.UUID)"""
        super(__LoginClientPacketHandlerImpl, self).onLoginAccepted(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(__client.ClientPacketHandler, self).handleS2CReply(__long.valueOf(arg0))

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool.__wrap(super(__network.PacketHandler, self).shouldHandlePacket(arg0))

    @override
    @overload
    def onDisconnect(self, arg0: str):
        """public void dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.onDisconnect(java.lang.String)"""
        super(__LoginClientPacketHandlerImpl, self).onDisconnect(arg0)

    @override
    @overload
    def isAcceptingPackets(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.isAcceptingPackets()"""
        return bool.__wrap(super(LoginClientPacketHandlerImpl, self).isAcceptingPackets())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public default dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.client.ClientPacketHandler.destination()"""
        return 'api.PacketDestination'.__wrap(super(client.ClientPacketHandler, self).destination())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isAsync(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.isAsync()"""
        return bool.__wrap(super(LoginClientPacketHandlerImpl, self).isAsync())

    @override
    @overload
    def context(self) -> 'network.PacketContext':
        """public dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl.context()"""
        return 'network.PacketContext'.__wrap(super(LoginClientPacketHandlerImpl, self).context())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.network.LoginClientPacketHandlerImpl 
 
 
# CLASS: dev.ultreon.quantum.client.network.ClientNetwork
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
import dev.ultreon.quantum.client.network.ClientNetwork as __ClientNetwork
__ClientNetwork = __ClientNetwork
import dev.ultreon.quantum.network.api.Network as __Network
__Network = __Network
from builtins import int
 
class ClientNetwork(ABC, network.__Network, api.Network):
    """dev.ultreon.quantum.client.network.ClientNetwork"""
 
    @staticmethod
    def __wrap(java_value: __ClientNetwork) -> 'ClientNetwork':
        return ClientNetwork(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientNetwork):
        """
        Dynamic initializer for ClientNetwork.
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
    def init(self):
        """public final void dev.ultreon.quantum.network.api.Network.init()"""
        super(api.Network, self).init()

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

    @override
    @overload
    def sendToClient(self, arg0: 'ModPacket', arg1: 'ServerPlayer'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ClientEndpoint> void dev.ultreon.quantum.network.api.Network.sendToClient(dev.ultreon.quantum.network.api.packet.ModPacket<T>,dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__api.Network, self).sendToClient(arg0, arg1)

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
    def sendToServer(self, arg0: 'ModPacket'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ServerEndpoint> void dev.ultreon.quantum.client.network.ClientNetwork.sendToServer(T)"""
        super(__ClientNetwork, self).sendToServer(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def namespace(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.network.api.Network.namespace()"""
        return str.__wrap(super(api.Network, self).namespace())

    @override
    @overload
    def channelName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.network.api.Network.channelName()"""
        return str.__wrap(super(api.Network, self).channelName())

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
    def getId(self) -> 'util.Identifier':
        """public final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.network.api.Network.getId()"""
        return 'util.Identifier'.__wrap(super(api.Network, self).getId())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

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

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
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
from pyquantum_helper import override
import java.lang.Object as __object
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

import java.lang.Float as __float
try:
    from pyquantum.block import entity
except ImportError:
    entity = __import_once__("pyquantum.block.entity")

try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.network.PacketContext as __PacketContext
__PacketContext = __PacketContext
try:
    from pyquantum.network.packets import s2c
except ImportError:
    s2c = __import_once__("pyquantum.network.packets.s2c")

import java.lang.Integer as __int
try:
    from pyquantum.world import particles
except ImportError:
    particles = __import_once__("pyquantum.world.particles")

import java.util.Map as Map
import dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl as __InGameClientPacketHandlerImpl
__InGameClientPacketHandlerImpl = __InGameClientPacketHandlerImpl
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
import java.util.List as List
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class InGameClientPacketHandlerImpl(network.__InGameClientPacketHandler, client.InGameClientPacketHandler):
    """dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl"""
 
    @staticmethod
    def __wrap(java_value: __InGameClientPacketHandlerImpl) -> 'InGameClientPacketHandlerImpl':
        return InGameClientPacketHandlerImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InGameClientPacketHandlerImpl):
        """
        Dynamic initializer for InGameClientPacketHandlerImpl.
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
    def onBlockSet(self, arg0: 'BlockPos', arg1: 'BlockProperties'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onBlockSet(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__InGameClientPacketHandlerImpl, self).onBlockSet(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def onMenuItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onMenuItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        super(__InGameClientPacketHandlerImpl, self).onMenuItemChanged(__int.valueOf(arg0), arg1)

    @override
    @overload
    def onMenuCursorChanged(self, arg0: 'ItemStack'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onMenuCursorChanged(dev.ultreon.quantum.item.ItemStack)"""
        super(__InGameClientPacketHandlerImpl, self).onMenuCursorChanged(arg0)

    @override
    @overload
    def onEntityPipeline(self, arg0: int, arg1: 'MapType'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onEntityPipeline(int,dev.ultreon.ubo.types.MapType)"""
        super(__InGameClientPacketHandlerImpl, self).onEntityPipeline(__int.valueOf(arg0), arg1)

    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.getPing()"""
        return int.__wrap(super(InGameClientPacketHandlerImpl, self).getPing())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def handleS2CReply(self, arg0: int):
        """public default void dev.ultreon.quantum.network.client.ClientPacketHandler.handleS2CReply(long)"""
        super(__client.ClientPacketHandler, self).handleS2CReply(__long.valueOf(arg0))

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool.__wrap(super(__network.PacketHandler, self).shouldHandlePacket(arg0))

    @override
    @overload
    def onAbilities(self, arg0: 'AbilitiesPacket'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onAbilities(dev.ultreon.quantum.network.packets.AbilitiesPacket)"""
        super(__InGameClientPacketHandlerImpl, self).onAbilities(arg0)

    @override
    @overload
    def onPlayerSetPos(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPlayerSetPos(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__InGameClientPacketHandlerImpl, self).onPlayerSetPos(arg0)

    @override
    @overload
    def onChatReceived(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onChatReceived(dev.ultreon.quantum.text.TextObject)"""
        super(__InGameClientPacketHandlerImpl, self).onChatReceived(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def onCloseContainerMenu(self):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onCloseContainerMenu()"""
        super(InGameClientPacketHandlerImpl, self).onCloseContainerMenu()

    @override
    @overload
    def onTabCompleteResult(self, arg0: 'String'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onTabCompleteResult(java.lang.String[])"""
        super(__InGameClientPacketHandlerImpl, self).onTabCompleteResult(arg0)

    @override
    @overload
    def onSpawnParticles(self, arg0: 'ParticleType', arg1: 'Vec3d', arg2: 'Vec3d', arg3: int):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onSpawnParticles(dev.ultreon.quantum.world.particles.ParticleType,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,int)"""
        super(__InGameClientPacketHandlerImpl, self).onSpawnParticles(arg0, arg1, arg2, __int.valueOf(arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool.__wrap(super(network.PacketHandler, self).isAsync())

    @override
    @overload
    def onAddEntity(self, arg0: int, arg1: 'EntityType', arg2: 'Vec3d', arg3: 'MapType'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onAddEntity(int,dev.ultreon.quantum.entity.EntityType<?>,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.ubo.types.MapType)"""
        super(__InGameClientPacketHandlerImpl, self).onAddEntity(__int.valueOf(arg0), arg1, arg2, arg3)

    @override
    @overload
    def onAddPermission(self, arg0: 'AddPermissionPacket'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onAddPermission(dev.ultreon.quantum.network.packets.AddPermissionPacket)"""
        super(__InGameClientPacketHandlerImpl, self).onAddPermission(arg0)

    @override
    @overload
    def onInventoryItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onInventoryItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        super(__InGameClientPacketHandlerImpl, self).onInventoryItemChanged(__int.valueOf(arg0), arg1)

    @override
    @overload
    def onChunkCancel(self, arg0: 'ChunkPos'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onChunkCancel(dev.ultreon.quantum.world.ChunkPos)"""
        super(__InGameClientPacketHandlerImpl, self).onChunkCancel(arg0)

    @override
    @overload
    def onRemoveEntity(self, arg0: int):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onRemoveEntity(int)"""
        super(__InGameClientPacketHandlerImpl, self).onRemoveEntity(__int.valueOf(arg0))

    @override
    @overload
    def onPlayerHurt(self, arg0: 'S2CPlayerHurtPacket'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPlayerHurt(dev.ultreon.quantum.network.packets.s2c.S2CPlayerHurtPacket)"""
        super(__InGameClientPacketHandlerImpl, self).onPlayerHurt(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getChannel(self, arg0: 'Identifier') -> 'network.NetworkChannel':
        """public dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.getChannel(dev.ultreon.quantum.util.Identifier)"""
        return 'network.NetworkChannel'.__wrap(super(__InGameClientPacketHandlerImpl, self).getChannel(arg0))

    @overload
    def __init__(self, arg0: 'IConnection'):
        """public dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl(dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        val = __InGameClientPacketHandlerImpl(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def onChunkData(self, arg0: 'ChunkPos', arg1: 'Storage', arg2: 'Storage', arg3: 'Map'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onChunkData(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.block.state.BlockProperties>,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.world.Biome>,java.util.Map<dev.ultreon.quantum.world.BlockPos, dev.ultreon.quantum.block.entity.BlockEntityType<?>>)"""
        super(__InGameClientPacketHandlerImpl, self).onChunkData(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def destination(self) -> 'api.PacketDestination':
        """public dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.destination()"""
        return 'api.PacketDestination'.__wrap(super(InGameClientPacketHandlerImpl, self).destination())

    @override
    @overload
    def isAcceptingPackets(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.isAcceptingPackets()"""
        return bool.__wrap(super(InGameClientPacketHandlerImpl, self).isAcceptingPackets())

    @override
    @overload
    def onModPacket(self, arg0: 'NetworkChannel', arg1: 'ModPacket'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onModPacket(dev.ultreon.quantum.network.NetworkChannel,dev.ultreon.quantum.network.api.packet.ModPacket<?>)"""
        super(__InGameClientPacketHandlerImpl, self).onModPacket(arg0, arg1)

    @override
    @overload
    def onPlayerAttack(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPlayerAttack(int,int)"""
        super(__InGameClientPacketHandlerImpl, self).onPlayerAttack(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onKeepAlive(self):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onKeepAlive()"""
        super(InGameClientPacketHandlerImpl, self).onKeepAlive()

    @override
    @overload
    def onRemovePlayer(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onRemovePlayer(java.util.UUID)"""
        super(__InGameClientPacketHandlerImpl, self).onRemovePlayer(arg0)

    @override
    @overload
    def onTimeChange(self, arg0: 'PacketContext', arg1: 'Operation', arg2: int):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onTimeChange(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.packets.s2c.S2CTimePacket$Operation,int)"""
        super(__InGameClientPacketHandlerImpl, self).onTimeChange(arg0, arg1, __int.valueOf(arg2))

    @override
    @overload
    def onBlockEntitySet(self, arg0: 'BlockPos', arg1: 'BlockEntityType'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onBlockEntitySet(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.entity.BlockEntityType<?>)"""
        super(__InGameClientPacketHandlerImpl, self).onBlockEntitySet(arg0, arg1)

    @overload
    def reply(self, arg0: int) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.client.ClientPacketHandler.reply(long)"""
        return 'packets.Packet'.__wrap(super(__client.ClientPacketHandler, self).reply(__long.valueOf(arg0)))

    @override
    @overload
    def onPlayerPosition(self, arg0: 'PacketContext', arg1: 'UUID', arg2: 'Vec3d'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPlayerPosition(dev.ultreon.quantum.network.PacketContext,java.util.UUID,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__InGameClientPacketHandlerImpl, self).onPlayerPosition(arg0, arg1, arg2)

    @override
    @overload
    def onDisconnect(self, arg0: str):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onDisconnect(java.lang.String)"""
        super(__InGameClientPacketHandlerImpl, self).onDisconnect(arg0)

    @override
    @overload
    def onPing(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPing(long,long)"""
        super(__InGameClientPacketHandlerImpl, self).onPing(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def onPlaySound(self, arg0: 'Identifier', arg1: float):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPlaySound(dev.ultreon.quantum.util.Identifier,float)"""
        super(__InGameClientPacketHandlerImpl, self).onPlaySound(arg0, __float.valueOf(arg1))

    @override
    @overload
    def context(self) -> 'network.PacketContext':
        """public dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.context()"""
        return 'network.PacketContext'.__wrap(super(InGameClientPacketHandlerImpl, self).context())

    @override
    @overload
    def onRemovePermission(self, arg0: 'RemovePermissionPacket'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onRemovePermission(dev.ultreon.quantum.network.packets.RemovePermissionPacket)"""
        super(__InGameClientPacketHandlerImpl, self).onRemovePermission(arg0)

    @staticmethod
    @overload
    def byteArrayToHexString(arg0: bytes) -> str:
        """public static java.lang.String dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.byteArrayToHexString(byte[])"""
        return str.__wrap(__InGameClientPacketHandlerImpl.byteArrayToHexString(bytes))

    @override
    @overload
    def onPlayerHealth(self, arg0: float):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onPlayerHealth(float)"""
        super(__InGameClientPacketHandlerImpl, self).onPlayerHealth(__float.valueOf(arg0))

    @override
    @overload
    def onGamemode(self, arg0: 'GameMode'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onGamemode(dev.ultreon.quantum.util.GameMode)"""
        super(__InGameClientPacketHandlerImpl, self).onGamemode(arg0)

    @override
    @overload
    def onRespawn(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onRespawn(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__InGameClientPacketHandlerImpl, self).onRespawn(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def onOpenContainerMenu(self, arg0: 'Identifier', arg1: 'List'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onOpenContainerMenu(dev.ultreon.quantum.util.Identifier,java.util.List<dev.ultreon.quantum.item.ItemStack>)"""
        super(__InGameClientPacketHandlerImpl, self).onOpenContainerMenu(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isDisconnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.isDisconnected()"""
        return bool.__wrap(super(InGameClientPacketHandlerImpl, self).isDisconnected())

    @overload
    def registerChannel(self, arg0: 'Identifier') -> 'network.NetworkChannel':
        """public dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.registerChannel(dev.ultreon.quantum.util.Identifier)"""
        return 'network.NetworkChannel'.__wrap(super(__InGameClientPacketHandlerImpl, self).registerChannel(arg0))

    @override
    @overload
    def onInitialPermissions(self, arg0: 'InitialPermissionsPacket'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onInitialPermissions(dev.ultreon.quantum.network.packets.InitialPermissionsPacket)"""
        super(__InGameClientPacketHandlerImpl, self).onInitialPermissions(arg0)

    @override
    @overload
    def onAddPlayer(self, arg0: 'UUID', arg1: str, arg2: 'Vec3d'):
        """public void dev.ultreon.quantum.client.network.InGameClientPacketHandlerImpl.onAddPlayer(java.util.UUID,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__InGameClientPacketHandlerImpl, self).onAddPlayer(arg0, arg1, arg2)