from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.PacketData as _PacketData
_PacketData = _PacketData
import dev.ultreon.quantum.network.system.IConnection as _IConnection
_IConnection = _IConnection
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import dev.ultreon.quantum.client.network.system.ClientMemoryConnection as _ClientMemoryConnection
_ClientMemoryConnection = _ClientMemoryConnection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _string
from builtins import bool
try:
    from pyquantum.network import stage
except ImportError:
    stage = _import_once("pyquantum.network.stage")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Runnable as Runnable
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.network.system.MemoryConnection as _MemoryConnection
_MemoryConnection = _MemoryConnection
try:
    from pyquantum import log
except ImportError:
    log = _import_once("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import dev.ultreon.quantum.util.Result as _Result
_Result = _Result
import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import java.lang.Long as _long
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientMemoryConnection():
    """dev.ultreon.quantum.client.network.system.ClientMemoryConnection"""
 
    @staticmethod
    def _wrap(java_value: _ClientMemoryConnection) -> 'ClientMemoryConnection':
        return ClientMemoryConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientMemoryConnection):
        """
        Dynamic initializer for ClientMemoryConnection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientMemoryConnection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientMemoryConnection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.network.system.IConnection.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.network.system.ClientMemoryConnection(dev.ultreon.quantum.client.QuantumClient)"""
        val = _ClientMemoryConnection(arg0)
        self.__wrapper = val

    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.MemoryConnection.getPing()"""
        return int._wrap(super(system.MemoryConnection, self).getPing())

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.start()"""
        super(system.MemoryConnection, self).start()

    @override
    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool._wrap(super(system.IConnection, self).isConnecting())

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(_system.IConnection, self).disconnect(arg0)

    @override
    @overload
    def setOtherSide(self, arg0: 'MemoryConnection'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setOtherSide(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>)"""
        super(_system.MemoryConnection, self).setOtherSide(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isCompressed()"""
        return bool._wrap(super(system.MemoryConnection, self).isCompressed())

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
    def on3rdPartyDisconnect(self, arg0: str) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.client.network.system.ClientMemoryConnection.on3rdPartyDisconnect(java.lang.String)"""
        return 'util.Result'._wrap(super(_ClientMemoryConnection, self).on3rdPartyDisconnect(arg0))

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.onPing(long)"""
        super(_system.MemoryConnection, self).onPing(_long.valueOf(arg0))

    @override
    @overload
    def setHandler(self, arg0: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setHandler(OurHandler)"""
        super(_system.MemoryConnection, self).setHandler(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.close()"""
        super(system.MemoryConnection, self).close()

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isConnected()"""
        return bool._wrap(super(system.MemoryConnection, self).isConnected())

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.disconnect(java.lang.String)"""
        super(_system.MemoryConnection, self).disconnect(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(_system.MemoryConnection, self).send(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getTheirPacketData(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<TheirHandler> dev.ultreon.quantum.network.system.MemoryConnection.getTheirPacketData()"""
        return 'network.PacketData'._wrap(super(system.MemoryConnection, self).getTheirPacketData())

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(_system.MemoryConnection, self).moveTo(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_system.MemoryConnection, self).send(arg0)

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.queue(java.lang.Runnable)"""
        super(_system.MemoryConnection, self).queue(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getRx() -> int:
        """public static int dev.ultreon.quantum.network.system.MemoryConnection.getRx()"""
        return int._wrap(_MemoryConnection.getRx())

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isMemoryConnection()"""
        return bool._wrap(super(system.MemoryConnection, self).isMemoryConnection())

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_system.IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_system.MemoryConnection, self).setPlayer(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.network.system.ClientMemoryConnection
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.PacketData as _PacketData
_PacketData = _PacketData
import dev.ultreon.quantum.network.system.IConnection as _IConnection
_IConnection = _IConnection
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import dev.ultreon.quantum.client.network.system.ClientMemoryConnection as _ClientMemoryConnection
_ClientMemoryConnection = _ClientMemoryConnection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _string
from builtins import bool
try:
    from pyquantum.network import stage
except ImportError:
    stage = _import_once("pyquantum.network.stage")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Runnable as Runnable
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.network.system.MemoryConnection as _MemoryConnection
_MemoryConnection = _MemoryConnection
try:
    from pyquantum import log
except ImportError:
    log = _import_once("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import dev.ultreon.quantum.util.Result as _Result
_Result = _Result
import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import java.lang.Long as _long
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientMemoryConnection():
    """dev.ultreon.quantum.client.network.system.ClientMemoryConnection"""
 
    @staticmethod
    def _wrap(java_value: _ClientMemoryConnection) -> 'ClientMemoryConnection':
        return ClientMemoryConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientMemoryConnection):
        """
        Dynamic initializer for ClientMemoryConnection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientMemoryConnection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientMemoryConnection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.network.system.IConnection.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.network.system.ClientMemoryConnection(dev.ultreon.quantum.client.QuantumClient)"""
        val = _ClientMemoryConnection(arg0)
        self.__wrapper = val

    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.MemoryConnection.getPing()"""
        return int._wrap(super(system.MemoryConnection, self).getPing())

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.start()"""
        super(system.MemoryConnection, self).start()

    @override
    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool._wrap(super(system.IConnection, self).isConnecting())

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(_system.IConnection, self).disconnect(arg0)

    @override
    @overload
    def setOtherSide(self, arg0: 'MemoryConnection'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setOtherSide(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>)"""
        super(_system.MemoryConnection, self).setOtherSide(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isCompressed()"""
        return bool._wrap(super(system.MemoryConnection, self).isCompressed())

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
    def on3rdPartyDisconnect(self, arg0: str) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.client.network.system.ClientMemoryConnection.on3rdPartyDisconnect(java.lang.String)"""
        return 'util.Result'._wrap(super(_ClientMemoryConnection, self).on3rdPartyDisconnect(arg0))

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.onPing(long)"""
        super(_system.MemoryConnection, self).onPing(_long.valueOf(arg0))

    @override
    @overload
    def setHandler(self, arg0: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setHandler(OurHandler)"""
        super(_system.MemoryConnection, self).setHandler(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.close()"""
        super(system.MemoryConnection, self).close()

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isConnected()"""
        return bool._wrap(super(system.MemoryConnection, self).isConnected())

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.disconnect(java.lang.String)"""
        super(_system.MemoryConnection, self).disconnect(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(_system.MemoryConnection, self).send(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getTheirPacketData(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<TheirHandler> dev.ultreon.quantum.network.system.MemoryConnection.getTheirPacketData()"""
        return 'network.PacketData'._wrap(super(system.MemoryConnection, self).getTheirPacketData())

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(_system.MemoryConnection, self).moveTo(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_system.MemoryConnection, self).send(arg0)

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.queue(java.lang.Runnable)"""
        super(_system.MemoryConnection, self).queue(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getRx() -> int:
        """public static int dev.ultreon.quantum.network.system.MemoryConnection.getRx()"""
        return int._wrap(_MemoryConnection.getRx())

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isMemoryConnection()"""
        return bool._wrap(super(system.MemoryConnection, self).isMemoryConnection())

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_system.IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_system.MemoryConnection, self).setPlayer(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.network.system.ClientMemoryConnection 
 
 
# CLASS: dev.ultreon.quantum.client.network.system.ClientTcpConnection
from pyquantum_helper import import_once as _import_once
import java.net.Socket as Socket
import dev.ultreon.quantum.network.system.IConnection as _IConnection
_IConnection = _IConnection
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.client.network.system.ClientTcpConnection as _ClientTcpConnection
_ClientTcpConnection = _ClientTcpConnection
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.network.system.Connection as _Connection
_Connection = _Connection
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.net.Socket as _Socket
_Socket = _Socket
from builtins import bool
try:
    from pyquantum.network import stage
except ImportError:
    stage = _import_once("pyquantum.network.stage")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Runnable as Runnable
import java.lang.String as _String
_String = _String
try:
    from pyquantum import log
except ImportError:
    log = _import_once("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import dev.ultreon.quantum.util.Result as _Result
_Result = _Result
import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientTcpConnection():
    """dev.ultreon.quantum.client.network.system.ClientTcpConnection"""
 
    @staticmethod
    def _wrap(java_value: _ClientTcpConnection) -> 'ClientTcpConnection':
        return ClientTcpConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientTcpConnection):
        """
        Dynamic initializer for ClientTcpConnection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientTcpConnection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientTcpConnection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.network.system.IConnection.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.Connection.close() throws java.io.IOException"""
        super(system.Connection, self).close()

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isCompressed()"""
        return bool._wrap(super(system.Connection, self).isCompressed())

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.Connection.queue(java.lang.Runnable)"""
        super(_system.Connection, self).queue(arg0)

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.client.network.system.ClientTcpConnection.onPing(long)"""
        super(_ClientTcpConnection, self).onPing(_long.valueOf(arg0))

    @staticmethod
    @overload
    def connectToServer(arg0: str, arg1: int) -> 'util.Result':
        """public static dev.ultreon.quantum.util.Result<dev.ultreon.quantum.client.network.system.ClientTcpConnection> dev.ultreon.quantum.client.network.system.ClientTcpConnection.connectToServer(java.lang.String,int)"""
        return util.Result._wrap(_ClientTcpConnection.connectToServer(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool._wrap(super(system.IConnection, self).isConnecting())

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(_system.IConnection, self).disconnect(arg0)

    @override
    @overload
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.Connection.setReadOnly()"""
        super(system.Connection, self).setReadOnly()

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isConnected()"""
        return bool._wrap(super(system.Connection, self).isConnected())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.Connection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(_system.Connection, self).moveTo(arg0, arg1)

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

    @staticmethod
    @overload
    def handleReply(arg0: int):
        """public static void dev.ultreon.quantum.network.system.Connection.handleReply(long)"""
        _Connection.handleReply(_long.valueOf(arg0))

    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.Connection.getPing()"""
        return int._wrap(super(system.Connection, self).getPing())

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isMemoryConnection()"""
        return bool._wrap(super(system.Connection, self).isMemoryConnection())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.Connection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_system.Connection, self).send(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def on3rdPartyDisconnect(self, arg0: str) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.client.network.system.ClientTcpConnection.on3rdPartyDisconnect(java.lang.String)"""
        return 'util.Result'._wrap(super(_ClientTcpConnection, self).on3rdPartyDisconnect(arg0))

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.Connection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_system.Connection, self).setPlayer(arg0)

    @override
    @overload
    def setCompressed(self, arg0: bool):
        """public void dev.ultreon.quantum.network.system.Connection.setCompressed(boolean)"""
        super(_system.Connection, self).setCompressed(_boolean.valueOf(arg0))

    @override
    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(system.IConnection, self).tick()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.Connection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(_system.Connection, self).send(arg0, arg1)

    @override
    @overload
    def getSocket(self) -> 'Socket':
        """public java.net.Socket dev.ultreon.quantum.network.system.Connection.getSocket()"""
        return 'Socket'._wrap(super(system.Connection, self).getSocket())

    @override
    @overload
    def isReadOnly(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isReadOnly()"""
        return bool._wrap(super(system.Connection, self).isReadOnly())

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.network.system.Connection.start()"""
        super(system.Connection, self).start()

    @staticmethod
    @overload
    def connectToLocalServer() -> 'util.Result':
        """public static dev.ultreon.quantum.util.Result<dev.ultreon.quantum.client.network.system.ClientMemoryConnection> dev.ultreon.quantum.client.network.system.ClientTcpConnection.connectToLocalServer()"""
        return util.Result._wrap(_ClientTcpConnection.connectToLocalServer())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.Connection.disconnect(java.lang.String)"""
        super(_system.Connection, self).disconnect(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_system.IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())