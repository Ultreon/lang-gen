from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import dev.ultreon.quantum.network.system.MemoryConnection as __MemoryConnection
__MemoryConnection = __MemoryConnection
import dev.ultreon.quantum.network.system.IConnection as __IConnection
__IConnection = __IConnection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.client.network.system.ClientMemoryConnection as __ClientMemoryConnection
__ClientMemoryConnection = __ClientMemoryConnection
from builtins import bool
try:
    from pyquantum.network import stage
except ImportError:
    stage = __import_once__("pyquantum.network.stage")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.util.Result as __Result
__Result = __Result
import dev.ultreon.quantum.network.PacketData as __PacketData
__PacketData = __PacketData
import java.lang.Runnable as Runnable
try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
 
class ClientMemoryConnection():
    """dev.ultreon.quantum.client.network.system.ClientMemoryConnection"""
 
    @staticmethod
    def __wrap(java_value: __ClientMemoryConnection) -> 'ClientMemoryConnection':
        return ClientMemoryConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientMemoryConnection):
        """
        Dynamic initializer for ClientMemoryConnection.
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
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.network.system.IConnection.LOGGER
    LOGGER: 'log.Logger' = __wrap(__log.Logger.LOGGER)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool.__wrap(super(system.IConnection, self).isConnecting())

    @override
    @overload
    def setHandler(self, arg0: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setHandler(OurHandler)"""
        super(__system.MemoryConnection, self).setHandler(arg0)

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isMemoryConnection()"""
        return bool.__wrap(super(system.MemoryConnection, self).isMemoryConnection())

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.start()"""
        super(system.MemoryConnection, self).start()

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.network.system.ClientMemoryConnection(dev.ultreon.quantum.client.QuantumClient)"""
        val = __ClientMemoryConnection(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.onPing(long)"""
        super(__system.MemoryConnection, self).onPing(__long.valueOf(arg0))

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isCompressed()"""
        return bool.__wrap(super(system.MemoryConnection, self).isCompressed())

    @override
    @overload
    def getTheirPacketData(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<TheirHandler> dev.ultreon.quantum.network.system.MemoryConnection.getTheirPacketData()"""
        return 'network.PacketData'.__wrap(super(system.MemoryConnection, self).getTheirPacketData())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.MemoryConnection.getPing()"""
        return int.__wrap(super(system.MemoryConnection, self).getPing())

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(__system.MemoryConnection, self).send(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(__system.MemoryConnection, self).moveTo(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.queue(java.lang.Runnable)"""
        super(__system.MemoryConnection, self).queue(arg0)

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.close()"""
        super(system.MemoryConnection, self).close()

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(__system.IConnection, self).disconnect(arg0)

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__system.MemoryConnection, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isConnected()"""
        return bool.__wrap(super(system.MemoryConnection, self).isConnected())

    @override
    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(system.IConnection, self).tick()

    @override
    @overload
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setReadOnly()"""
        super(system.MemoryConnection, self).setReadOnly()

    @override
    @overload
    def setOtherSide(self, arg0: 'MemoryConnection'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setOtherSide(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>)"""
        super(__system.MemoryConnection, self).setOtherSide(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__system.IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.disconnect(java.lang.String)"""
        super(__system.MemoryConnection, self).disconnect(arg0)

    @staticmethod
    @overload
    def getRx() -> int:
        """public static int dev.ultreon.quantum.network.system.MemoryConnection.getRx()"""
        return int.__wrap(__MemoryConnection.getRx())

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__system.MemoryConnection, self).setPlayer(arg0)

    @overload
    def on3rdPartyDisconnect(self, arg0: str) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.client.network.system.ClientMemoryConnection.on3rdPartyDisconnect(java.lang.String)"""
        return 'util.Result'.__wrap(super(__ClientMemoryConnection, self).on3rdPartyDisconnect(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.network.system.ClientMemoryConnection
from pyquantum_helper import import_once as __import_once__
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import dev.ultreon.quantum.network.system.MemoryConnection as __MemoryConnection
__MemoryConnection = __MemoryConnection
import dev.ultreon.quantum.network.system.IConnection as __IConnection
__IConnection = __IConnection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.client.network.system.ClientMemoryConnection as __ClientMemoryConnection
__ClientMemoryConnection = __ClientMemoryConnection
from builtins import bool
try:
    from pyquantum.network import stage
except ImportError:
    stage = __import_once__("pyquantum.network.stage")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.util.Result as __Result
__Result = __Result
import dev.ultreon.quantum.network.PacketData as __PacketData
__PacketData = __PacketData
import java.lang.Runnable as Runnable
try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
 
class ClientMemoryConnection():
    """dev.ultreon.quantum.client.network.system.ClientMemoryConnection"""
 
    @staticmethod
    def __wrap(java_value: __ClientMemoryConnection) -> 'ClientMemoryConnection':
        return ClientMemoryConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientMemoryConnection):
        """
        Dynamic initializer for ClientMemoryConnection.
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
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.network.system.IConnection.LOGGER
    LOGGER: 'log.Logger' = __wrap(__log.Logger.LOGGER)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool.__wrap(super(system.IConnection, self).isConnecting())

    @override
    @overload
    def setHandler(self, arg0: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setHandler(OurHandler)"""
        super(__system.MemoryConnection, self).setHandler(arg0)

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isMemoryConnection()"""
        return bool.__wrap(super(system.MemoryConnection, self).isMemoryConnection())

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.start()"""
        super(system.MemoryConnection, self).start()

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.network.system.ClientMemoryConnection(dev.ultreon.quantum.client.QuantumClient)"""
        val = __ClientMemoryConnection(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.onPing(long)"""
        super(__system.MemoryConnection, self).onPing(__long.valueOf(arg0))

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isCompressed()"""
        return bool.__wrap(super(system.MemoryConnection, self).isCompressed())

    @override
    @overload
    def getTheirPacketData(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<TheirHandler> dev.ultreon.quantum.network.system.MemoryConnection.getTheirPacketData()"""
        return 'network.PacketData'.__wrap(super(system.MemoryConnection, self).getTheirPacketData())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.MemoryConnection.getPing()"""
        return int.__wrap(super(system.MemoryConnection, self).getPing())

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(__system.MemoryConnection, self).send(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(__system.MemoryConnection, self).moveTo(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.queue(java.lang.Runnable)"""
        super(__system.MemoryConnection, self).queue(arg0)

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.close()"""
        super(system.MemoryConnection, self).close()

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(__system.IConnection, self).disconnect(arg0)

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__system.MemoryConnection, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isConnected()"""
        return bool.__wrap(super(system.MemoryConnection, self).isConnected())

    @override
    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(system.IConnection, self).tick()

    @override
    @overload
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setReadOnly()"""
        super(system.MemoryConnection, self).setReadOnly()

    @override
    @overload
    def setOtherSide(self, arg0: 'MemoryConnection'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setOtherSide(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>)"""
        super(__system.MemoryConnection, self).setOtherSide(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__system.IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.disconnect(java.lang.String)"""
        super(__system.MemoryConnection, self).disconnect(arg0)

    @staticmethod
    @overload
    def getRx() -> int:
        """public static int dev.ultreon.quantum.network.system.MemoryConnection.getRx()"""
        return int.__wrap(__MemoryConnection.getRx())

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__system.MemoryConnection, self).setPlayer(arg0)

    @overload
    def on3rdPartyDisconnect(self, arg0: str) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.client.network.system.ClientMemoryConnection.on3rdPartyDisconnect(java.lang.String)"""
        return 'util.Result'.__wrap(super(__ClientMemoryConnection, self).on3rdPartyDisconnect(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.network.system.ClientMemoryConnection 
 
 
# CLASS: dev.ultreon.quantum.client.network.system.ClientTcpConnection
from pyquantum_helper import import_once as __import_once__
import java.net.Socket as Socket
import java.lang.Boolean as __boolean
from builtins import type
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import dev.ultreon.quantum.network.system.IConnection as __IConnection
__IConnection = __IConnection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.client.network.system.ClientTcpConnection as __ClientTcpConnection
__ClientTcpConnection = __ClientTcpConnection
import java.net.Socket as __Socket
__Socket = __Socket
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
from builtins import bool
try:
    from pyquantum.network import stage
except ImportError:
    stage = __import_once__("pyquantum.network.stage")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.util.Result as __Result
__Result = __Result
import dev.ultreon.quantum.network.system.Connection as __Connection
__Connection = __Connection
import java.lang.Runnable as Runnable
try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
 
class ClientTcpConnection():
    """dev.ultreon.quantum.client.network.system.ClientTcpConnection"""
 
    @staticmethod
    def __wrap(java_value: __ClientTcpConnection) -> 'ClientTcpConnection':
        return ClientTcpConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientTcpConnection):
        """
        Dynamic initializer for ClientTcpConnection.
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
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.network.system.IConnection.LOGGER
    LOGGER: 'log.Logger' = __wrap(__log.Logger.LOGGER)


    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.Connection.close() throws java.io.IOException"""
        super(system.Connection, self).close()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool.__wrap(super(system.IConnection, self).isConnecting())

    @staticmethod
    @overload
    def connectToServer(arg0: str, arg1: int) -> 'util.Result':
        """public static dev.ultreon.quantum.util.Result<dev.ultreon.quantum.client.network.system.ClientTcpConnection> dev.ultreon.quantum.client.network.system.ClientTcpConnection.connectToServer(java.lang.String,int)"""
        return util.Result.__wrap(__ClientTcpConnection.connectToServer(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def isReadOnly(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isReadOnly()"""
        return bool.__wrap(super(system.Connection, self).isReadOnly())

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isMemoryConnection()"""
        return bool.__wrap(super(system.Connection, self).isMemoryConnection())

    @overload
    def on3rdPartyDisconnect(self, arg0: str) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.client.network.system.ClientTcpConnection.on3rdPartyDisconnect(java.lang.String)"""
        return 'util.Result'.__wrap(super(__ClientTcpConnection, self).on3rdPartyDisconnect(arg0))

    @override
    @overload
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.Connection.setReadOnly()"""
        super(system.Connection, self).setReadOnly()

    @override
    @overload
    def setCompressed(self, arg0: bool):
        """public void dev.ultreon.quantum.network.system.Connection.setCompressed(boolean)"""
        super(__system.Connection, self).setCompressed(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getSocket(self) -> 'Socket':
        """public java.net.Socket dev.ultreon.quantum.network.system.Connection.getSocket()"""
        return 'Socket'.__wrap(super(system.Connection, self).getSocket())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def connectToLocalServer() -> 'util.Result':
        """public static dev.ultreon.quantum.util.Result<dev.ultreon.quantum.client.network.system.ClientMemoryConnection> dev.ultreon.quantum.client.network.system.ClientTcpConnection.connectToLocalServer()"""
        return util.Result.__wrap(__ClientTcpConnection.connectToLocalServer())

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(__system.IConnection, self).disconnect(arg0)

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.Connection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__system.Connection, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.client.network.system.ClientTcpConnection.onPing(long)"""
        super(__ClientTcpConnection, self).onPing(__long.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.Connection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(__system.Connection, self).send(arg0, arg1)

    @override
    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(system.IConnection, self).tick()

    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.Connection.getPing()"""
        return int.__wrap(super(system.Connection, self).getPing())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__system.IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.network.system.Connection.start()"""
        super(system.Connection, self).start()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.Connection.queue(java.lang.Runnable)"""
        super(__system.Connection, self).queue(arg0)

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.Connection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(__system.Connection, self).moveTo(arg0, arg1)

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.Connection.disconnect(java.lang.String)"""
        super(__system.Connection, self).disconnect(arg0)

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isConnected()"""
        return bool.__wrap(super(system.Connection, self).isConnected())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def handleReply(arg0: int):
        """public static void dev.ultreon.quantum.network.system.Connection.handleReply(long)"""
        __Connection.handleReply(__long.valueOf(arg0))

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.Connection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__system.Connection, self).setPlayer(arg0)

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isCompressed()"""
        return bool.__wrap(super(system.Connection, self).isCompressed())