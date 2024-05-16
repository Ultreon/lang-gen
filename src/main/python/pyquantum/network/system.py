from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import stage
except ImportError:
    stage = __import_once__("pyquantum.network.stage")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.PacketData as __PacketData
__PacketData = __PacketData
import java.lang.Runnable as Runnable
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import dev.ultreon.quantum.network.system.MemoryConnection as __MemoryConnection
__MemoryConnection = __MemoryConnection
import dev.ultreon.quantum.network.system.IConnection as __IConnection
__IConnection = __IConnection
import java.util.concurrent.Executor as Executor
from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MemoryConnection(ABC, __IConnection, IConnection):
    """dev.ultreon.quantum.network.system.MemoryConnection"""
 
    @staticmethod
    def __wrap(java_value: __MemoryConnection) -> 'MemoryConnection':
        return MemoryConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MemoryConnection):
        """
        Dynamic initializer for MemoryConnection.
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
        return bool.__wrap(super(IConnection, self).isConnecting())

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isCompressed()"""
        return bool.__wrap(super(MemoryConnection, self).isCompressed())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.start()"""
        super(MemoryConnection, self).start()

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.onPing(long)"""
        super(__MemoryConnection, self).onPing(__long.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__MemoryConnection, self).send(arg0)

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(__MemoryConnection, self).send(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def on3rdPartyDisconnect(self, arg0: str):
        """public abstract dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.network.system.MemoryConnection.on3rdPartyDisconnect(java.lang.String)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'MemoryConnection', arg1: 'Executor'):
        """public dev.ultreon.quantum.network.system.MemoryConnection(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>,java.util.concurrent.Executor)"""
        val = __MemoryConnection(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.MemoryConnection.getPing()"""
        return int.__wrap(super(MemoryConnection, self).getPing())

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(__MemoryConnection, self).moveTo(arg0, arg1)

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isMemoryConnection()"""
        return bool.__wrap(super(MemoryConnection, self).isMemoryConnection())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(__IConnection, self).disconnect(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.queue(java.lang.Runnable)"""
        super(__MemoryConnection, self).queue(arg0)

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.disconnect(java.lang.String)"""
        super(__MemoryConnection, self).disconnect(arg0)

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__MemoryConnection, self).setPlayer(arg0)

    @overload
    def setHandler(self, arg0: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setHandler(OurHandler)"""
        super(__MemoryConnection, self).setHandler(arg0)

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
    def setOtherSide(self, arg0: 'MemoryConnection'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setOtherSide(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>)"""
        super(__MemoryConnection, self).setOtherSide(arg0)

    @override
    @overload
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setReadOnly()"""
        super(MemoryConnection, self).setReadOnly()

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isConnected()"""
        return bool.__wrap(super(MemoryConnection, self).isConnected())

    @override
    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(IConnection, self).tick()

    @overload
    def getTheirPacketData(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<TheirHandler> dev.ultreon.quantum.network.system.MemoryConnection.getTheirPacketData()"""
        return 'network.PacketData'.__wrap(super(MemoryConnection, self).getTheirPacketData())

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.close()"""
        super(MemoryConnection, self).close()

    @staticmethod
    @overload
    def getRx() -> int:
        """public static int dev.ultreon.quantum.network.system.MemoryConnection.getRx()"""
        return int.__wrap(__MemoryConnection.getRx())

 
 
 
# CLASS: dev.ultreon.quantum.network.system.MemoryConnection
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import stage
except ImportError:
    stage = __import_once__("pyquantum.network.stage")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.PacketData as __PacketData
__PacketData = __PacketData
import java.lang.Runnable as Runnable
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import dev.ultreon.quantum.network.system.MemoryConnection as __MemoryConnection
__MemoryConnection = __MemoryConnection
import dev.ultreon.quantum.network.system.IConnection as __IConnection
__IConnection = __IConnection
import java.util.concurrent.Executor as Executor
from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MemoryConnection(ABC, __IConnection, IConnection):
    """dev.ultreon.quantum.network.system.MemoryConnection"""
 
    @staticmethod
    def __wrap(java_value: __MemoryConnection) -> 'MemoryConnection':
        return MemoryConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MemoryConnection):
        """
        Dynamic initializer for MemoryConnection.
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
        return bool.__wrap(super(IConnection, self).isConnecting())

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isCompressed()"""
        return bool.__wrap(super(MemoryConnection, self).isCompressed())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.start()"""
        super(MemoryConnection, self).start()

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.onPing(long)"""
        super(__MemoryConnection, self).onPing(__long.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__MemoryConnection, self).send(arg0)

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(__MemoryConnection, self).send(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def on3rdPartyDisconnect(self, arg0: str):
        """public abstract dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.network.system.MemoryConnection.on3rdPartyDisconnect(java.lang.String)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'MemoryConnection', arg1: 'Executor'):
        """public dev.ultreon.quantum.network.system.MemoryConnection(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>,java.util.concurrent.Executor)"""
        val = __MemoryConnection(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.MemoryConnection.getPing()"""
        return int.__wrap(super(MemoryConnection, self).getPing())

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(__MemoryConnection, self).moveTo(arg0, arg1)

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isMemoryConnection()"""
        return bool.__wrap(super(MemoryConnection, self).isMemoryConnection())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(__IConnection, self).disconnect(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.queue(java.lang.Runnable)"""
        super(__MemoryConnection, self).queue(arg0)

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.disconnect(java.lang.String)"""
        super(__MemoryConnection, self).disconnect(arg0)

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__MemoryConnection, self).setPlayer(arg0)

    @overload
    def setHandler(self, arg0: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setHandler(OurHandler)"""
        super(__MemoryConnection, self).setHandler(arg0)

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
    def setOtherSide(self, arg0: 'MemoryConnection'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setOtherSide(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>)"""
        super(__MemoryConnection, self).setOtherSide(arg0)

    @override
    @overload
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setReadOnly()"""
        super(MemoryConnection, self).setReadOnly()

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isConnected()"""
        return bool.__wrap(super(MemoryConnection, self).isConnected())

    @override
    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(IConnection, self).tick()

    @overload
    def getTheirPacketData(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<TheirHandler> dev.ultreon.quantum.network.system.MemoryConnection.getTheirPacketData()"""
        return 'network.PacketData'.__wrap(super(MemoryConnection, self).getTheirPacketData())

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.close()"""
        super(MemoryConnection, self).close()

    @staticmethod
    @overload
    def getRx() -> int:
        """public static int dev.ultreon.quantum.network.system.MemoryConnection.getRx()"""
        return int.__wrap(__MemoryConnection.getRx())

 
 
 
# CLASS: dev.ultreon.quantum.network.system.MemoryConnection 
 
 
# CLASS: dev.ultreon.quantum.network.system.ServerMemoryConnection
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

from builtins import type
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

import dev.ultreon.quantum.network.system.ServerMemoryConnection as __ServerMemoryConnection
__ServerMemoryConnection = __ServerMemoryConnection
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
 
class ServerMemoryConnection(__MemoryConnection, MemoryConnection):
    """dev.ultreon.quantum.network.system.ServerMemoryConnection"""
 
    @staticmethod
    def __wrap(java_value: __ServerMemoryConnection) -> 'ServerMemoryConnection':
        return ServerMemoryConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerMemoryConnection):
        """
        Dynamic initializer for ServerMemoryConnection.
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
        return bool.__wrap(super(IConnection, self).isConnecting())

    @override
    @overload
    def setHandler(self, arg0: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setHandler(OurHandler)"""
        super(__MemoryConnection, self).setHandler(arg0)

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isCompressed()"""
        return bool.__wrap(super(MemoryConnection, self).isCompressed())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.start()"""
        super(MemoryConnection, self).start()

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.onPing(long)"""
        super(__MemoryConnection, self).onPing(__long.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__MemoryConnection, self).send(arg0)

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(__MemoryConnection, self).send(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.ServerMemoryConnection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__ServerMemoryConnection, self).setPlayer(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.MemoryConnection.getPing()"""
        return int.__wrap(super(MemoryConnection, self).getPing())

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(__MemoryConnection, self).moveTo(arg0, arg1)

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isMemoryConnection()"""
        return bool.__wrap(super(MemoryConnection, self).isMemoryConnection())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(__IConnection, self).disconnect(arg0)

    @override
    @overload
    def setOtherSide(self, arg0: 'MemoryConnection'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setOtherSide(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>)"""
        super(__MemoryConnection, self).setOtherSide(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.queue(java.lang.Runnable)"""
        super(__MemoryConnection, self).queue(arg0)

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.disconnect(java.lang.String)"""
        super(__MemoryConnection, self).disconnect(arg0)

    @overload
    def on3rdPartyDisconnect(self, arg0: str) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.network.system.ServerMemoryConnection.on3rdPartyDisconnect(java.lang.String)"""
        return 'util.Result'.__wrap(super(__ServerMemoryConnection, self).on3rdPartyDisconnect(arg0))

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
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setReadOnly()"""
        super(MemoryConnection, self).setReadOnly()

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isConnected()"""
        return bool.__wrap(super(MemoryConnection, self).isConnected())

    @override
    @overload
    def getTheirPacketData(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<TheirHandler> dev.ultreon.quantum.network.system.MemoryConnection.getTheirPacketData()"""
        return 'network.PacketData'.__wrap(super(MemoryConnection, self).getTheirPacketData())

    @override
    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(IConnection, self).tick()

    @overload
    def __init__(self, arg0: 'MemoryConnection', arg1: 'QuantumServer'):
        """public dev.ultreon.quantum.network.system.ServerMemoryConnection(dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>,dev.ultreon.quantum.server.QuantumServer)"""
        val = __ServerMemoryConnection(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.close()"""
        super(MemoryConnection, self).close()

    @staticmethod
    @overload
    def getRx() -> int:
        """public static int dev.ultreon.quantum.network.system.MemoryConnection.getRx()"""
        return int.__wrap(__MemoryConnection.getRx()) 
 
 
# CLASS: dev.ultreon.quantum.network.system.TcpNetworker
from pyquantum_helper import import_once as __import_once__
import java.net.Socket as Socket
from builtins import str
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

from pyquantum_helper import override
import java.lang.Object as __object
import java.net.InetAddress as InetAddress
from builtins import type
import dev.ultreon.quantum.network.system.TcpNetworker as __TcpNetworker
__TcpNetworker = __TcpNetworker
import java.net.Socket as __Socket
__Socket = __Socket
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class TcpNetworker(__ConnectionReceiver, ConnectionReceiver, pyquantum.__Networker, network.Networker):
    """dev.ultreon.quantum.network.system.TcpNetworker"""
 
    @staticmethod
    def __wrap(java_value: __TcpNetworker) -> 'TcpNetworker':
        return TcpNetworker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TcpNetworker):
        """
        Dynamic initializer for TcpNetworker.
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
    def tick(self):
        """public void dev.ultreon.quantum.network.system.TcpNetworker.tick()"""
        super(TcpNetworker, self).tick()

    @overload
    def join(self):
        """public void dev.ultreon.quantum.network.system.TcpNetworker.join() throws java.lang.InterruptedException"""
        super(TcpNetworker, self).join()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'QuantumServer', arg1: 'InetAddress', arg2: int):
        """public dev.ultreon.quantum.network.system.TcpNetworker(dev.ultreon.quantum.server.QuantumServer,java.net.InetAddress,int) throws java.io.IOException"""
        val = __TcpNetworker(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def accept(self) -> 'Socket':
        """public java.net.Socket dev.ultreon.quantum.network.system.TcpNetworker.accept() throws java.io.IOException"""
        return 'Socket'.__wrap(super(TcpNetworker, self).accept())

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

    @override
    @overload
    def getConnections(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.network.system.ServerTcpConnection> dev.ultreon.quantum.network.system.TcpNetworker.getConnections()"""
        return 'List'.__wrap(super(TcpNetworker, self).getConnections())

    @override
    @overload
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.TcpNetworker.isRunning()"""
        return bool.__wrap(super(TcpNetworker, self).isRunning())

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
    def close(self):
        """public void dev.ultreon.quantum.network.system.TcpNetworker.close() throws java.io.IOException"""
        super(TcpNetworker, self).close()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.system.IConnection
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

try:
    from pyquantum.network import stage
except ImportError:
    stage = __import_once__("pyquantum.network.stage")

import java.io.Closeable as __Closeable
__Closeable = __Closeable
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Runnable as Runnable
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import dev.ultreon.quantum.network.system.IConnection as __IConnection
__IConnection = __IConnection
from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

from builtins import bool
 
class IConnection(ABC, __Closeable, Closeable):
    """dev.ultreon.quantum.network.system.IConnection"""
 
    @staticmethod
    def __wrap(java_value: __IConnection) -> 'IConnection':
        return IConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IConnection):
        """
        Dynamic initializer for IConnection.
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


    @abstractmethod
    def on3rdPartyDisconnect(self, arg0: str):
        """public abstract dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.network.system.IConnection.on3rdPartyDisconnect(java.lang.String)"""
        pass

    @abstractmethod
    def queue(self, arg0: 'Runnable'):
        """public abstract void dev.ultreon.quantum.network.system.IConnection.queue(java.lang.Runnable)"""
        pass

    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool.__wrap(super(IConnection, self).isConnecting())

    @overload
    def send(self, arg0: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__IConnection, self).send(arg0)

    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(__IConnection, self).disconnect(arg0)

    @abstractmethod
    def onPing(self, arg0: int):
        """public abstract void dev.ultreon.quantum.network.system.IConnection.onPing(long)"""
        pass

    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(IConnection, self).tick()

    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__IConnection, self).initiate(arg0, arg1)

    @abstractmethod
    def setReadOnly(self, ):
        """public abstract void dev.ultreon.quantum.network.system.IConnection.setReadOnly()"""
        pass

    @abstractmethod
    def isCompressed(self, ):
        """public abstract boolean dev.ultreon.quantum.network.system.IConnection.isCompressed()"""
        pass

    @abstractmethod
    def close(self, ):
        """public abstract void java.io.Closeable.close() throws java.io.IOException"""
        pass

    @abstractmethod
    def disconnect(self, arg0: str):
        """public abstract void dev.ultreon.quantum.network.system.IConnection.disconnect(java.lang.String)"""
        pass

    @abstractmethod
    def isConnected(self, ):
        """public abstract boolean dev.ultreon.quantum.network.system.IConnection.isConnected()"""
        pass

    @abstractmethod
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public abstract void dev.ultreon.quantum.network.system.IConnection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        pass

    @abstractmethod
    def isMemoryConnection(self, ):
        """public abstract boolean dev.ultreon.quantum.network.system.IConnection.isMemoryConnection()"""
        pass

    @abstractmethod
    def getPing(self, ):
        """public abstract long dev.ultreon.quantum.network.system.IConnection.getPing()"""
        pass

    @abstractmethod
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public abstract void dev.ultreon.quantum.network.system.IConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        pass

    @abstractmethod
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public abstract void dev.ultreon.quantum.network.system.IConnection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        pass

    @abstractmethod
    def start(self, ):
        """public abstract void dev.ultreon.quantum.network.system.IConnection.start()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.network.system.ServerTcpConnection
from pyquantum_helper import import_once as __import_once__
import java.net.Socket as Socket
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

import java.lang.Boolean as __boolean
from builtins import type
import dev.ultreon.quantum.server.QuantumServer as __QuantumServer
__QuantumServer = __QuantumServer
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

import java.net.Socket as __Socket
__Socket = __Socket
import dev.ultreon.quantum.server.player.ServerPlayer as __ServerPlayer
__ServerPlayer = __ServerPlayer
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
import dev.ultreon.quantum.network.system.ServerTcpConnection as __ServerTcpConnection
__ServerTcpConnection = __ServerTcpConnection
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
 
class ServerTcpConnection(__Connection, Connection):
    """dev.ultreon.quantum.network.system.ServerTcpConnection"""
 
    @staticmethod
    def __wrap(java_value: __ServerTcpConnection) -> 'ServerTcpConnection':
        return ServerTcpConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerTcpConnection):
        """
        Dynamic initializer for ServerTcpConnection.
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
        return bool.__wrap(super(IConnection, self).isConnecting())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.system.ServerTcpConnection.onPing(long)"""
        super(__ServerTcpConnection, self).onPing(__long.valueOf(arg0))

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.network.system.Connection.start()"""
        super(Connection, self).start()

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.Connection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(__Connection, self).send(arg0, arg1)

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.Connection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__Connection, self).send(arg0)

    @overload
    def __init__(self, arg0: 'Socket', arg1: 'QuantumServer'):
        """public dev.ultreon.quantum.network.system.ServerTcpConnection(java.net.Socket,dev.ultreon.quantum.server.QuantumServer)"""
        val = __ServerTcpConnection(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isCompressed()"""
        return bool.__wrap(super(Connection, self).isCompressed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.Connection.close() throws java.io.IOException"""
        super(Connection, self).close()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.Connection.getPing()"""
        return int.__wrap(super(Connection, self).getPing())

    @overload
    def getServer(self) -> 'server.QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.network.system.ServerTcpConnection.getServer()"""
        return 'server.QuantumServer'.__wrap(super(ServerTcpConnection, self).getServer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(__IConnection, self).disconnect(arg0)

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.Connection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(__Connection, self).moveTo(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isConnected()"""
        return bool.__wrap(super(Connection, self).isConnected())

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.ServerTcpConnection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__ServerTcpConnection, self).setPlayer(arg0)

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isMemoryConnection()"""
        return bool.__wrap(super(Connection, self).isMemoryConnection())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def isReadOnly(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isReadOnly()"""
        return bool.__wrap(super(Connection, self).isReadOnly())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getSocket(self) -> 'Socket':
        """public java.net.Socket dev.ultreon.quantum.network.system.Connection.getSocket()"""
        return 'Socket'.__wrap(super(Connection, self).getSocket())

    @overload
    def on3rdPartyDisconnect(self, arg0: str) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.network.system.ServerTcpConnection.on3rdPartyDisconnect(java.lang.String)"""
        return 'util.Result'.__wrap(super(__ServerTcpConnection, self).on3rdPartyDisconnect(arg0))

    @overload
    def getPlayer(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.network.system.ServerTcpConnection.getPlayer()"""
        return 'player.ServerPlayer'.__wrap(super(ServerTcpConnection, self).getPlayer())

    @override
    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(IConnection, self).tick()

    @override
    @overload
    def setCompressed(self, arg0: bool):
        """public void dev.ultreon.quantum.network.system.Connection.setCompressed(boolean)"""
        super(__Connection, self).setCompressed(__boolean.valueOf(arg0))

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.Connection.queue(java.lang.Runnable)"""
        super(__Connection, self).queue(arg0)

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.Connection.setReadOnly()"""
        super(Connection, self).setReadOnly()

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.Connection.disconnect(java.lang.String)"""
        super(__Connection, self).disconnect(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.network.system.Connection
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

from abc import abstractmethod, ABC
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
import dev.ultreon.quantum.network.system.Connection as __Connection
__Connection = __Connection
import java.lang.Runnable as Runnable
try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

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
 
class Connection(ABC, __IConnection, IConnection, __Closeable, Closeable):
    """dev.ultreon.quantum.network.system.Connection"""
 
    @staticmethod
    def __wrap(java_value: __Connection) -> 'Connection':
        return Connection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Connection):
        """
        Dynamic initializer for Connection.
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

    @abstractmethod
    def on3rdPartyDisconnect(self, arg0: str):
        """public abstract dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.network.system.IConnection.on3rdPartyDisconnect(java.lang.String)"""
        pass

    @override
    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool.__wrap(super(IConnection, self).isConnecting())

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.Connection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__Connection, self).setPlayer(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSocket(self) -> 'Socket':
        """public java.net.Socket dev.ultreon.quantum.network.system.Connection.getSocket()"""
        return 'Socket'.__wrap(super(Connection, self).getSocket())

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.network.system.Connection.start()"""
        super(Connection, self).start()

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.Connection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(__Connection, self).send(arg0, arg1)

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.Connection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__Connection, self).send(arg0)

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isCompressed()"""
        return bool.__wrap(super(Connection, self).isCompressed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.Connection.close() throws java.io.IOException"""
        super(Connection, self).close()

    @overload
    def setCompressed(self, arg0: bool):
        """public void dev.ultreon.quantum.network.system.Connection.setCompressed(boolean)"""
        super(__Connection, self).setCompressed(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.Connection.getPing()"""
        return int.__wrap(super(Connection, self).getPing())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(__IConnection, self).disconnect(arg0)

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.Connection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(__Connection, self).moveTo(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isReadOnly(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isReadOnly()"""
        return bool.__wrap(super(Connection, self).isReadOnly())

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isConnected()"""
        return bool.__wrap(super(Connection, self).isConnected())

    @abstractmethod
    def onPing(self, arg0: int):
        """public abstract void dev.ultreon.quantum.network.system.IConnection.onPing(long)"""
        pass

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isMemoryConnection()"""
        return bool.__wrap(super(Connection, self).isMemoryConnection())

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
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(IConnection, self).tick()

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.Connection.queue(java.lang.Runnable)"""
        super(__Connection, self).queue(arg0)

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(__IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.Connection.setReadOnly()"""
        super(Connection, self).setReadOnly()

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.Connection.disconnect(java.lang.String)"""
        super(__Connection, self).disconnect(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.network.system.ConnectionReceiver
import java.io.Closeable as __Closeable
__Closeable = __Closeable
import dev.ultreon.quantum.network.system.ConnectionReceiver as __ConnectionReceiver
__ConnectionReceiver = __ConnectionReceiver
from abc import abstractmethod, ABC
 
class ConnectionReceiver(ABC, __Closeable, Closeable):
    """dev.ultreon.quantum.network.system.ConnectionReceiver"""
 
    @staticmethod
    def __wrap(java_value: __ConnectionReceiver) -> 'ConnectionReceiver':
        return ConnectionReceiver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConnectionReceiver):
        """
        Dynamic initializer for ConnectionReceiver.
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
 
    @abstractmethod
    def close(self, ):
        """public abstract void java.io.Closeable.close() throws java.io.IOException"""
        pass

    @abstractmethod
    def accept(self, ):
        """public abstract java.net.Socket dev.ultreon.quantum.network.system.ConnectionReceiver.accept() throws java.io.IOException"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.network.system.ReadOnlyConnectionException
from builtins import str
import dev.ultreon.quantum.network.system.ReadOnlyConnectionException as __ReadOnlyConnectionException
__ReadOnlyConnectionException = __ReadOnlyConnectionException
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ReadOnlyConnectionException(__RuntimeException, RuntimeException):
    """dev.ultreon.quantum.network.system.ReadOnlyConnectionException"""
 
    @staticmethod
    def __wrap(java_value: __ReadOnlyConnectionException) -> 'ReadOnlyConnectionException':
        return ReadOnlyConnectionException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReadOnlyConnectionException):
        """
        Dynamic initializer for ReadOnlyConnectionException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.system.ReadOnlyConnectionException()"""
        val = __ReadOnlyConnectionException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.system.ReadOnlyConnectionException()"""
        val = __ReadOnlyConnectionException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.system.ReadOnlyConnectionException(java.lang.String)"""
        val = __ReadOnlyConnectionException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val