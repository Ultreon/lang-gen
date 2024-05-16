from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import stage
except ImportError:
    stage = _import_once("pyquantum.network.stage")

import dev.ultreon.quantum.network.PacketData as _PacketData
_PacketData = _PacketData
import dev.ultreon.quantum.network.system.IConnection as _IConnection
_IConnection = _IConnection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import java.util.concurrent.Executor as Executor
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.network.system.MemoryConnection as _MemoryConnection
_MemoryConnection = _MemoryConnection
try:
    from pyquantum import log
except ImportError:
    log = _import_once("pyquantum.log")

import java.lang.String as _string
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MemoryConnection():
    """dev.ultreon.quantum.network.system.MemoryConnection"""
 
    @staticmethod
    def _wrap(java_value: _MemoryConnection) -> 'MemoryConnection':
        return MemoryConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MemoryConnection):
        """
        Dynamic initializer for MemoryConnection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MemoryConnection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MemoryConnection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.network.system.IConnection.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.MemoryConnection.getPing()"""
        return int._wrap(super(MemoryConnection, self).getPing())

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.disconnect(java.lang.String)"""
        super(_MemoryConnection, self).disconnect(arg0)

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
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isConnected()"""
        return bool._wrap(super(MemoryConnection, self).isConnected())

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_MemoryConnection, self).setPlayer(arg0)

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_MemoryConnection, self).send(arg0)

    @overload
    def setOtherSide(self, arg0: 'MemoryConnection'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setOtherSide(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>)"""
        super(_MemoryConnection, self).setOtherSide(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isMemoryConnection()"""
        return bool._wrap(super(MemoryConnection, self).isMemoryConnection())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool._wrap(super(IConnection, self).isConnecting())

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(_MemoryConnection, self).moveTo(arg0, arg1)

    @abstractmethod
    def on3rdPartyDisconnect(self, arg0: str):
        """public abstract dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.network.system.MemoryConnection.on3rdPartyDisconnect(java.lang.String)"""
        pass

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isCompressed()"""
        return bool._wrap(super(MemoryConnection, self).isCompressed())

    @overload
    def getTheirPacketData(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<TheirHandler> dev.ultreon.quantum.network.system.MemoryConnection.getTheirPacketData()"""
        return 'network.PacketData'._wrap(super(MemoryConnection, self).getTheirPacketData())

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.queue(java.lang.Runnable)"""
        super(_MemoryConnection, self).queue(arg0)

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(_IConnection, self).disconnect(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(_MemoryConnection, self).send(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'MemoryConnection', arg1: 'Executor'):
        """public dev.ultreon.quantum.network.system.MemoryConnection(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>,java.util.concurrent.Executor)"""
        val = _MemoryConnection(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setReadOnly()"""
        super(MemoryConnection, self).setReadOnly()

    @overload
    def setHandler(self, arg0: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setHandler(OurHandler)"""
        super(_MemoryConnection, self).setHandler(arg0)

    @override
    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(IConnection, self).tick()

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.onPing(long)"""
        super(_MemoryConnection, self).onPing(_long.valueOf(arg0))

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
    def close(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.close()"""
        super(MemoryConnection, self).close()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.network.system.MemoryConnection
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import stage
except ImportError:
    stage = _import_once("pyquantum.network.stage")

import dev.ultreon.quantum.network.PacketData as _PacketData
_PacketData = _PacketData
import dev.ultreon.quantum.network.system.IConnection as _IConnection
_IConnection = _IConnection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import java.util.concurrent.Executor as Executor
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.network.system.MemoryConnection as _MemoryConnection
_MemoryConnection = _MemoryConnection
try:
    from pyquantum import log
except ImportError:
    log = _import_once("pyquantum.log")

import java.lang.String as _string
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MemoryConnection():
    """dev.ultreon.quantum.network.system.MemoryConnection"""
 
    @staticmethod
    def _wrap(java_value: _MemoryConnection) -> 'MemoryConnection':
        return MemoryConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MemoryConnection):
        """
        Dynamic initializer for MemoryConnection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MemoryConnection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MemoryConnection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.network.system.IConnection.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.MemoryConnection.getPing()"""
        return int._wrap(super(MemoryConnection, self).getPing())

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.disconnect(java.lang.String)"""
        super(_MemoryConnection, self).disconnect(arg0)

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
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isConnected()"""
        return bool._wrap(super(MemoryConnection, self).isConnected())

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_MemoryConnection, self).setPlayer(arg0)

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_MemoryConnection, self).send(arg0)

    @overload
    def setOtherSide(self, arg0: 'MemoryConnection'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setOtherSide(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>)"""
        super(_MemoryConnection, self).setOtherSide(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isMemoryConnection()"""
        return bool._wrap(super(MemoryConnection, self).isMemoryConnection())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool._wrap(super(IConnection, self).isConnecting())

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(_MemoryConnection, self).moveTo(arg0, arg1)

    @abstractmethod
    def on3rdPartyDisconnect(self, arg0: str):
        """public abstract dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.network.system.MemoryConnection.on3rdPartyDisconnect(java.lang.String)"""
        pass

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isCompressed()"""
        return bool._wrap(super(MemoryConnection, self).isCompressed())

    @overload
    def getTheirPacketData(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<TheirHandler> dev.ultreon.quantum.network.system.MemoryConnection.getTheirPacketData()"""
        return 'network.PacketData'._wrap(super(MemoryConnection, self).getTheirPacketData())

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.queue(java.lang.Runnable)"""
        super(_MemoryConnection, self).queue(arg0)

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(_IConnection, self).disconnect(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(_MemoryConnection, self).send(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'MemoryConnection', arg1: 'Executor'):
        """public dev.ultreon.quantum.network.system.MemoryConnection(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>,java.util.concurrent.Executor)"""
        val = _MemoryConnection(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setReadOnly()"""
        super(MemoryConnection, self).setReadOnly()

    @overload
    def setHandler(self, arg0: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setHandler(OurHandler)"""
        super(_MemoryConnection, self).setHandler(arg0)

    @override
    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(IConnection, self).tick()

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.onPing(long)"""
        super(_MemoryConnection, self).onPing(_long.valueOf(arg0))

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
    def close(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.close()"""
        super(MemoryConnection, self).close()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.network.system.MemoryConnection 
 
 
# CLASS: dev.ultreon.quantum.network.system.ServerMemoryConnection
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.PacketData as _PacketData
_PacketData = _PacketData
import dev.ultreon.quantum.network.system.IConnection as _IConnection
_IConnection = _IConnection
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.network.system.ServerMemoryConnection as _ServerMemoryConnection
_ServerMemoryConnection = _ServerMemoryConnection
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
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ServerMemoryConnection():
    """dev.ultreon.quantum.network.system.ServerMemoryConnection"""
 
    @staticmethod
    def _wrap(java_value: _ServerMemoryConnection) -> 'ServerMemoryConnection':
        return ServerMemoryConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerMemoryConnection):
        """
        Dynamic initializer for ServerMemoryConnection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerMemoryConnection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerMemoryConnection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.network.system.IConnection.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.MemoryConnection.getPing()"""
        return int._wrap(super(MemoryConnection, self).getPing())

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.disconnect(java.lang.String)"""
        super(_MemoryConnection, self).disconnect(arg0)

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
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isConnected()"""
        return bool._wrap(super(MemoryConnection, self).isConnected())

    @override
    @overload
    def setHandler(self, arg0: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setHandler(OurHandler)"""
        super(_MemoryConnection, self).setHandler(arg0)

    @override
    @overload
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_MemoryConnection, self).send(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isMemoryConnection()"""
        return bool._wrap(super(MemoryConnection, self).isMemoryConnection())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool._wrap(super(IConnection, self).isConnecting())

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(_MemoryConnection, self).moveTo(arg0, arg1)

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.ServerMemoryConnection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_ServerMemoryConnection, self).setPlayer(arg0)

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.MemoryConnection.isCompressed()"""
        return bool._wrap(super(MemoryConnection, self).isCompressed())

    @overload
    def __init__(self, arg0: 'MemoryConnection', arg1: 'QuantumServer'):
        """public dev.ultreon.quantum.network.system.ServerMemoryConnection(dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>,dev.ultreon.quantum.server.QuantumServer)"""
        val = _ServerMemoryConnection(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.queue(java.lang.Runnable)"""
        super(_MemoryConnection, self).queue(arg0)

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(_IConnection, self).disconnect(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getTheirPacketData(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<TheirHandler> dev.ultreon.quantum.network.system.MemoryConnection.getTheirPacketData()"""
        return 'network.PacketData'._wrap(super(MemoryConnection, self).getTheirPacketData())

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(_MemoryConnection, self).send(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def on3rdPartyDisconnect(self, arg0: str) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.network.system.ServerMemoryConnection.on3rdPartyDisconnect(java.lang.String)"""
        return 'util.Result'._wrap(super(_ServerMemoryConnection, self).on3rdPartyDisconnect(arg0))

    @override
    @overload
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setReadOnly()"""
        super(MemoryConnection, self).setReadOnly()

    @override
    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(IConnection, self).tick()

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.onPing(long)"""
        super(_MemoryConnection, self).onPing(_long.valueOf(arg0))

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
    def close(self):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.close()"""
        super(MemoryConnection, self).close()

    @override
    @overload
    def setOtherSide(self, arg0: 'MemoryConnection'):
        """public void dev.ultreon.quantum.network.system.MemoryConnection.setOtherSide(dev.ultreon.quantum.network.system.MemoryConnection<TheirHandler, OurHandler>)"""
        super(_MemoryConnection, self).setOtherSide(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.system.TcpNetworker
from pyquantum_helper import import_once as _import_once
import java.net.Socket as Socket
from builtins import str
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.net.InetAddress as InetAddress
import dev.ultreon.quantum.network.system.TcpNetworker as _TcpNetworker
_TcpNetworker = _TcpNetworker
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Integer as _int
import java.net.Socket as _Socket
_Socket = _Socket
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TcpNetworker():
    """dev.ultreon.quantum.network.system.TcpNetworker"""
 
    @staticmethod
    def _wrap(java_value: _TcpNetworker) -> 'TcpNetworker':
        return TcpNetworker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TcpNetworker):
        """
        Dynamic initializer for TcpNetworker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TcpNetworker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TcpNetworker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def tick(self):
        """public void dev.ultreon.quantum.network.system.TcpNetworker.tick()"""
        super(TcpNetworker, self).tick()

    @override
    @overload
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.TcpNetworker.isRunning()"""
        return bool._wrap(super(TcpNetworker, self).isRunning())

    @overload
    def join(self):
        """public void dev.ultreon.quantum.network.system.TcpNetworker.join() throws java.lang.InterruptedException"""
        super(TcpNetworker, self).join()

    @overload
    def __init__(self, arg0: 'QuantumServer', arg1: 'InetAddress', arg2: int):
        """public dev.ultreon.quantum.network.system.TcpNetworker(dev.ultreon.quantum.server.QuantumServer,java.net.InetAddress,int) throws java.io.IOException"""
        val = _TcpNetworker(arg0, arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def accept(self) -> 'Socket':
        """public java.net.Socket dev.ultreon.quantum.network.system.TcpNetworker.accept() throws java.io.IOException"""
        return 'Socket'._wrap(super(TcpNetworker, self).accept())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getConnections(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.network.system.ServerTcpConnection> dev.ultreon.quantum.network.system.TcpNetworker.getConnections()"""
        return 'List'._wrap(super(TcpNetworker, self).getConnections())

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.TcpNetworker.close() throws java.io.IOException"""
        super(TcpNetworker, self).close()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.system.IConnection
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.system.IConnection as _IConnection
_IConnection = _IConnection
try:
    from pyquantum import log
except ImportError:
    log = _import_once("pyquantum.log")

try:
    from pyquantum.network import stage
except ImportError:
    stage = _import_once("pyquantum.network.stage")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import java.lang.Runnable as Runnable
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

from builtins import bool
import java.io.Closeable as _Closeable
_Closeable = _Closeable
 
class IConnection():
    """dev.ultreon.quantum.network.system.IConnection"""
 
    @staticmethod
    def _wrap(java_value: _IConnection) -> 'IConnection':
        return IConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IConnection):
        """
        Dynamic initializer for IConnection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IConnection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IConnection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.network.system.IConnection.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @abstractmethod
    def on3rdPartyDisconnect(self, arg0: str):
        """public abstract dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.network.system.IConnection.on3rdPartyDisconnect(java.lang.String)"""
        pass

    @abstractmethod
    def queue(self, arg0: 'Runnable'):
        """public abstract void dev.ultreon.quantum.network.system.IConnection.queue(java.lang.Runnable)"""
        pass

    @abstractmethod
    def onPing(self, arg0: int):
        """public abstract void dev.ultreon.quantum.network.system.IConnection.onPing(long)"""
        pass

    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_IConnection, self).initiate(arg0, arg1)

    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(IConnection, self).tick()

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

    @overload
    def send(self, arg0: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_IConnection, self).send(arg0)

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

    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool._wrap(super(IConnection, self).isConnecting())

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

    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(_IConnection, self).disconnect(arg0) 
 
 
# CLASS: dev.ultreon.quantum.network.system.ServerTcpConnection
from pyquantum_helper import import_once as _import_once
import java.net.Socket as Socket
import dev.ultreon.quantum.network.system.IConnection as _IConnection
_IConnection = _IConnection
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
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
import dev.ultreon.quantum.server.player.ServerPlayer as _ServerPlayer
_ServerPlayer = _ServerPlayer
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

import dev.ultreon.quantum.server.QuantumServer as _QuantumServer
_QuantumServer = _QuantumServer
import java.lang.Long as _long
import dev.ultreon.quantum.network.system.ServerTcpConnection as _ServerTcpConnection
_ServerTcpConnection = _ServerTcpConnection
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ServerTcpConnection():
    """dev.ultreon.quantum.network.system.ServerTcpConnection"""
 
    @staticmethod
    def _wrap(java_value: _ServerTcpConnection) -> 'ServerTcpConnection':
        return ServerTcpConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerTcpConnection):
        """
        Dynamic initializer for ServerTcpConnection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerTcpConnection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerTcpConnection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.network.system.IConnection.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isMemoryConnection()"""
        return bool._wrap(super(Connection, self).isMemoryConnection())

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isCompressed()"""
        return bool._wrap(super(Connection, self).isCompressed())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setCompressed(self, arg0: bool):
        """public void dev.ultreon.quantum.network.system.Connection.setCompressed(boolean)"""
        super(_Connection, self).setCompressed(_boolean.valueOf(arg0))

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.network.system.Connection.start()"""
        super(Connection, self).start()

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.Connection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(_Connection, self).moveTo(arg0, arg1)

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.Connection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(_Connection, self).send(arg0, arg1)

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
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.Connection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_Connection, self).send(arg0)

    @override
    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool._wrap(super(IConnection, self).isConnecting())

    @overload
    def getServer(self) -> 'server.QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.network.system.ServerTcpConnection.getServer()"""
        return 'server.QuantumServer'._wrap(super(ServerTcpConnection, self).getServer())

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.Connection.close() throws java.io.IOException"""
        super(Connection, self).close()

    @staticmethod
    @overload
    def handleReply(arg0: int):
        """public static void dev.ultreon.quantum.network.system.Connection.handleReply(long)"""
        _Connection.handleReply(_long.valueOf(arg0))

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.Connection.queue(java.lang.Runnable)"""
        super(_Connection, self).queue(arg0)

    @overload
    def __init__(self, arg0: 'Socket', arg1: 'QuantumServer'):
        """public dev.ultreon.quantum.network.system.ServerTcpConnection(java.net.Socket,dev.ultreon.quantum.server.QuantumServer)"""
        val = _ServerTcpConnection(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isConnected()"""
        return bool._wrap(super(Connection, self).isConnected())

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(_IConnection, self).disconnect(arg0)

    @override
    @overload
    def onPing(self, arg0: int):
        """public void dev.ultreon.quantum.network.system.ServerTcpConnection.onPing(long)"""
        super(_ServerTcpConnection, self).onPing(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.Connection.getPing()"""
        return int._wrap(super(Connection, self).getPing())

    @overload
    def on3rdPartyDisconnect(self, arg0: str) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.network.system.ServerTcpConnection.on3rdPartyDisconnect(java.lang.String)"""
        return 'util.Result'._wrap(super(_ServerTcpConnection, self).on3rdPartyDisconnect(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.Connection.disconnect(java.lang.String)"""
        super(_Connection, self).disconnect(arg0)

    @overload
    def getPlayer(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.network.system.ServerTcpConnection.getPlayer()"""
        return 'player.ServerPlayer'._wrap(super(ServerTcpConnection, self).getPlayer())

    @override
    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(IConnection, self).tick()

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isReadOnly(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isReadOnly()"""
        return bool._wrap(super(Connection, self).isReadOnly())

    @override
    @overload
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.Connection.setReadOnly()"""
        super(Connection, self).setReadOnly()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getSocket(self) -> 'Socket':
        """public java.net.Socket dev.ultreon.quantum.network.system.Connection.getSocket()"""
        return 'Socket'._wrap(super(Connection, self).getSocket())

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.ServerTcpConnection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_ServerTcpConnection, self).setPlayer(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.system.Connection
from pyquantum_helper import import_once as _import_once
import java.net.Socket as Socket
import dev.ultreon.quantum.network.system.IConnection as _IConnection
_IConnection = _IConnection
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

from abc import abstractmethod, ABC
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
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Connection():
    """dev.ultreon.quantum.network.system.Connection"""
 
    @staticmethod
    def _wrap(java_value: _Connection) -> 'Connection':
        return Connection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Connection):
        """
        Dynamic initializer for Connection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Connection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Connection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.network.system.IConnection.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @abstractmethod
    def on3rdPartyDisconnect(self, arg0: str):
        """public abstract dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.network.system.IConnection.on3rdPartyDisconnect(java.lang.String)"""
        pass

    @override
    @overload
    def isMemoryConnection(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isMemoryConnection()"""
        return bool._wrap(super(Connection, self).isMemoryConnection())

    @override
    @overload
    def isCompressed(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isCompressed()"""
        return bool._wrap(super(Connection, self).isCompressed())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.network.system.Connection.start()"""
        super(Connection, self).start()

    @override
    @overload
    def moveTo(self, arg0: 'PacketStage', arg1: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.system.Connection.moveTo(dev.ultreon.quantum.network.stage.PacketStage,OurHandler)"""
        super(_Connection, self).moveTo(arg0, arg1)

    @override
    @overload
    def send(self, arg0: 'Packet', arg1: 'PacketListener'):
        """public void dev.ultreon.quantum.network.system.Connection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>,dev.ultreon.quantum.network.PacketListener)"""
        super(_Connection, self).send(arg0, arg1)

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
    def send(self, arg0: 'Packet'):
        """public void dev.ultreon.quantum.network.system.Connection.send(dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_Connection, self).send(arg0)

    @override
    @overload
    def isConnecting(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.system.IConnection.isConnecting()"""
        return bool._wrap(super(IConnection, self).isConnecting())

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.system.Connection.close() throws java.io.IOException"""
        super(Connection, self).close()

    @staticmethod
    @overload
    def handleReply(arg0: int):
        """public static void dev.ultreon.quantum.network.system.Connection.handleReply(long)"""
        _Connection.handleReply(_long.valueOf(arg0))

    @override
    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.system.Connection.queue(java.lang.Runnable)"""
        super(_Connection, self).queue(arg0)

    @overload
    def isReadOnly(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isReadOnly()"""
        return bool._wrap(super(Connection, self).isReadOnly())

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.network.system.Connection.isConnected()"""
        return bool._wrap(super(Connection, self).isConnected())

    @override
    @overload
    def disconnect(self, arg0: 'TextObject'):
        """public default void dev.ultreon.quantum.network.system.IConnection.disconnect(dev.ultreon.quantum.text.TextObject)"""
        super(_IConnection, self).disconnect(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getPing(self) -> int:
        """public long dev.ultreon.quantum.network.system.Connection.getPing()"""
        return int._wrap(super(Connection, self).getPing())

    @overload
    def setCompressed(self, arg0: bool):
        """public void dev.ultreon.quantum.network.system.Connection.setCompressed(boolean)"""
        super(_Connection, self).setCompressed(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def onPing(self, arg0: int):
        """public abstract void dev.ultreon.quantum.network.system.IConnection.onPing(long)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def disconnect(self, arg0: str):
        """public void dev.ultreon.quantum.network.system.Connection.disconnect(java.lang.String)"""
        super(_Connection, self).disconnect(arg0)

    @override
    @overload
    def setPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.network.system.Connection.setPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_Connection, self).setPlayer(arg0)

    @override
    @overload
    def tick(self):
        """public default void dev.ultreon.quantum.network.system.IConnection.tick()"""
        super(IConnection, self).tick()

    @override
    @overload
    def initiate(self, arg0: 'PacketHandler', arg1: 'Packet'):
        """public default void dev.ultreon.quantum.network.system.IConnection.initiate(OurHandler,dev.ultreon.quantum.network.packets.Packet<? extends TheirHandler>)"""
        super(_IConnection, self).initiate(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getSocket(self) -> 'Socket':
        """public java.net.Socket dev.ultreon.quantum.network.system.Connection.getSocket()"""
        return 'Socket'._wrap(super(Connection, self).getSocket())

    @override
    @overload
    def setReadOnly(self):
        """public void dev.ultreon.quantum.network.system.Connection.setReadOnly()"""
        super(Connection, self).setReadOnly()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.system.ConnectionReceiver
import dev.ultreon.quantum.network.system.ConnectionReceiver as _ConnectionReceiver
_ConnectionReceiver = _ConnectionReceiver
from abc import abstractmethod, ABC
import java.io.Closeable as _Closeable
_Closeable = _Closeable
 
class ConnectionReceiver():
    """dev.ultreon.quantum.network.system.ConnectionReceiver"""
 
    @staticmethod
    def _wrap(java_value: _ConnectionReceiver) -> 'ConnectionReceiver':
        return ConnectionReceiver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConnectionReceiver):
        """
        Dynamic initializer for ConnectionReceiver.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConnectionReceiver__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConnectionReceiver__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import dev.ultreon.quantum.network.system.ReadOnlyConnectionException as _ReadOnlyConnectionException
_ReadOnlyConnectionException = _ReadOnlyConnectionException
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReadOnlyConnectionException():
    """dev.ultreon.quantum.network.system.ReadOnlyConnectionException"""
 
    @staticmethod
    def _wrap(java_value: _ReadOnlyConnectionException) -> 'ReadOnlyConnectionException':
        return ReadOnlyConnectionException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReadOnlyConnectionException):
        """
        Dynamic initializer for ReadOnlyConnectionException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReadOnlyConnectionException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReadOnlyConnectionException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.system.ReadOnlyConnectionException()"""
        val = _ReadOnlyConnectionException()
        self.__wrapper = val

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.system.ReadOnlyConnectionException()"""
        val = _ReadOnlyConnectionException()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.system.ReadOnlyConnectionException(java.lang.String)"""
        val = _ReadOnlyConnectionException(arg0)
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())