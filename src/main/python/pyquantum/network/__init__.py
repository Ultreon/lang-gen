from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

import dev.ultreon.quantum.network.NetworkChannel as _NetworkChannel
_NetworkChannel = _NetworkChannel
from pyquantum_helper import override
import java.net.InetAddress as InetAddress
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.network.system.TcpNetworker as _TcpNetworker
_TcpNetworker = _TcpNetworker
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.ServerConnections as _ServerConnections
_ServerConnections = _ServerConnections
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.network.MemoryNetworker as _MemoryNetworker
_MemoryNetworker = _MemoryNetworker
import dev.ultreon.quantum.server.QuantumServer as _QuantumServer
_QuantumServer = _QuantumServer
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ServerConnections():
    """dev.ultreon.quantum.network.ServerConnections"""
 
    @staticmethod
    def _wrap(java_value: _ServerConnections) -> 'ServerConnections':
        return ServerConnections(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerConnections):
        """
        Dynamic initializer for ServerConnections.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerConnections__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerConnections__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def registerChannel(arg0: 'Identifier') -> 'NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.ServerConnections.registerChannel(dev.ultreon.quantum.util.Identifier)"""
        return NetworkChannel._wrap(_ServerConnections.registerChannel(arg0))

    @overload
    def startMemoryServer(self, arg0: 'MemoryConnection') -> 'MemoryNetworker':
        """public dev.ultreon.quantum.network.MemoryNetworker dev.ultreon.quantum.network.ServerConnections.startMemoryServer(dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        return 'MemoryNetworker'._wrap(super(_ServerConnections, self).startMemoryServer(arg0))

    @overload
    def __init__(self, arg0: 'QuantumServer'):
        """public dev.ultreon.quantum.network.ServerConnections(dev.ultreon.quantum.server.QuantumServer)"""
        val = _ServerConnections(arg0)
        self.__wrapper = val

    @overload
    def stop(self):
        """public void dev.ultreon.quantum.network.ServerConnections.stop()"""
        super(ServerConnections, self).stop()

    @overload
    def tick(self):
        """public void dev.ultreon.quantum.network.ServerConnections.tick()"""
        super(ServerConnections, self).tick()

    @overload
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.network.ServerConnections.isRunning()"""
        return bool._wrap(super(ServerConnections, self).isRunning())

    @staticmethod
    @overload
    def getChannels() -> 'Collection':
        """public static java.util.Collection<dev.ultreon.quantum.network.NetworkChannel> dev.ultreon.quantum.network.ServerConnections.getChannels()"""
        return Collection._wrap(_ServerConnections.getChannels())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.ServerConnections.toString()"""
        return str._wrap(super(ServerConnections, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getServer(self) -> 'server.QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.network.ServerConnections.getServer()"""
        return 'server.QuantumServer'._wrap(super(ServerConnections, self).getServer())

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
    def startTcpServer(self, arg0: 'InetAddress', arg1: int) -> 'system.TcpNetworker':
        """public dev.ultreon.quantum.network.system.TcpNetworker dev.ultreon.quantum.network.ServerConnections.startTcpServer(java.net.InetAddress,int) throws dev.ultreon.quantum.network.ServerHostingException"""
        return 'system.TcpNetworker'._wrap(super(_ServerConnections, self).startTcpServer(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def getChannel(arg0: 'Identifier') -> 'NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.ServerConnections.getChannel(dev.ultreon.quantum.util.Identifier)"""
        return NetworkChannel._wrap(_ServerConnections.getChannel(arg0))

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

 
 
 
# CLASS: dev.ultreon.quantum.network.ServerConnections
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

import dev.ultreon.quantum.network.NetworkChannel as _NetworkChannel
_NetworkChannel = _NetworkChannel
from pyquantum_helper import override
import java.net.InetAddress as InetAddress
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.network.system.TcpNetworker as _TcpNetworker
_TcpNetworker = _TcpNetworker
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.ServerConnections as _ServerConnections
_ServerConnections = _ServerConnections
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.network.MemoryNetworker as _MemoryNetworker
_MemoryNetworker = _MemoryNetworker
import dev.ultreon.quantum.server.QuantumServer as _QuantumServer
_QuantumServer = _QuantumServer
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ServerConnections():
    """dev.ultreon.quantum.network.ServerConnections"""
 
    @staticmethod
    def _wrap(java_value: _ServerConnections) -> 'ServerConnections':
        return ServerConnections(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerConnections):
        """
        Dynamic initializer for ServerConnections.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerConnections__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerConnections__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def registerChannel(arg0: 'Identifier') -> 'NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.ServerConnections.registerChannel(dev.ultreon.quantum.util.Identifier)"""
        return NetworkChannel._wrap(_ServerConnections.registerChannel(arg0))

    @overload
    def startMemoryServer(self, arg0: 'MemoryConnection') -> 'MemoryNetworker':
        """public dev.ultreon.quantum.network.MemoryNetworker dev.ultreon.quantum.network.ServerConnections.startMemoryServer(dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        return 'MemoryNetworker'._wrap(super(_ServerConnections, self).startMemoryServer(arg0))

    @overload
    def __init__(self, arg0: 'QuantumServer'):
        """public dev.ultreon.quantum.network.ServerConnections(dev.ultreon.quantum.server.QuantumServer)"""
        val = _ServerConnections(arg0)
        self.__wrapper = val

    @overload
    def stop(self):
        """public void dev.ultreon.quantum.network.ServerConnections.stop()"""
        super(ServerConnections, self).stop()

    @overload
    def tick(self):
        """public void dev.ultreon.quantum.network.ServerConnections.tick()"""
        super(ServerConnections, self).tick()

    @overload
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.network.ServerConnections.isRunning()"""
        return bool._wrap(super(ServerConnections, self).isRunning())

    @staticmethod
    @overload
    def getChannels() -> 'Collection':
        """public static java.util.Collection<dev.ultreon.quantum.network.NetworkChannel> dev.ultreon.quantum.network.ServerConnections.getChannels()"""
        return Collection._wrap(_ServerConnections.getChannels())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.ServerConnections.toString()"""
        return str._wrap(super(ServerConnections, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getServer(self) -> 'server.QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.network.ServerConnections.getServer()"""
        return 'server.QuantumServer'._wrap(super(ServerConnections, self).getServer())

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
    def startTcpServer(self, arg0: 'InetAddress', arg1: int) -> 'system.TcpNetworker':
        """public dev.ultreon.quantum.network.system.TcpNetworker dev.ultreon.quantum.network.ServerConnections.startTcpServer(java.net.InetAddress,int) throws dev.ultreon.quantum.network.ServerHostingException"""
        return 'system.TcpNetworker'._wrap(super(_ServerConnections, self).startTcpServer(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def getChannel(arg0: 'Identifier') -> 'NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.ServerConnections.getChannel(dev.ultreon.quantum.util.Identifier)"""
        return NetworkChannel._wrap(_ServerConnections.getChannel(arg0))

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

 
 
 
# CLASS: dev.ultreon.quantum.network.ServerConnections 
 
 
# CLASS: dev.ultreon.quantum.network.DataOverflowException
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
import dev.ultreon.quantum.network.DataOverflowException as _DataOverflowException
_DataOverflowException = _DataOverflowException
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DataOverflowException():
    """dev.ultreon.quantum.network.DataOverflowException"""
 
    @staticmethod
    def _wrap(java_value: _DataOverflowException) -> 'DataOverflowException':
        return DataOverflowException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DataOverflowException):
        """
        Dynamic initializer for DataOverflowException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DataOverflowException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DataOverflowException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

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

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int):
        """public dev.ultreon.quantum.network.DataOverflowException(java.lang.String,int,int)"""
        val = _DataOverflowException(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.network.Networker
import dev.ultreon.quantum.network.Networker as _Networker
_Networker = _Networker
from abc import abstractmethod, ABC
import java.io.Closeable as _Closeable
_Closeable = _Closeable
 
class Networker():
    """dev.ultreon.quantum.network.Networker"""
 
    @staticmethod
    def _wrap(java_value: _Networker) -> 'Networker':
        return Networker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Networker):
        """
        Dynamic initializer for Networker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Networker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Networker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def close(self, ):
        """public abstract void java.io.Closeable.close() throws java.io.IOException"""
        pass

    @abstractmethod
    def tick(self, ):
        """public abstract void dev.ultreon.quantum.network.Networker.tick()"""
        pass

    @abstractmethod
    def isRunning(self, ):
        """public abstract boolean dev.ultreon.quantum.network.Networker.isRunning()"""
        pass

    @abstractmethod
    def getConnections(self, ):
        """public abstract java.util.List<? extends dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.server.ServerPacketHandler, dev.ultreon.quantum.network.client.ClientPacketHandler>> dev.ultreon.quantum.network.Networker.getConnections()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.network.PacketIO
from pyquantum_helper import import_once as _import_once
import java.net.Socket as Socket
import java.util.UUID as UUID
import java.lang.Character as _char
import dev.ultreon.quantum.network.PacketIO as _PacketIO
_PacketIO = _PacketIO
import dev.ultreon.quantum.world.ChunkPos as _ChunkPos
_ChunkPos = _ChunkPos
import java.lang.CharSequence as _CharSequence
_CharSequence = _CharSequence
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.libs.commons.v0.vector.Vec4f as _Vec4f
_Vec4f = _Vec4f
import java.util.BitSet as BitSet
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.nio.ByteOrder as ByteOrder
import java.lang.Boolean as _boolean
import java.io.OutputStream as OutputStream
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import java.lang.CharSequence as CharSequence
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.BitSet as _BitSet
_BitSet = _BitSet
from typing import List
import java.lang.Float as _float
import java.lang.Enum as Enum
import dev.ultreon.libs.commons.v0.vector.Vec2i as _Vec2i
_Vec2i = _Vec2i
import java.lang.Enum as _Enum
_Enum = _Enum
import java.util.function.BiConsumer as BiConsumer
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.libs.commons.v0.vector.Vec2f as _Vec2f
_Vec2f = _Vec2f
try:
    from pyquantum.network import partial
except ImportError:
    partial = _import_once("pyquantum.network.partial")

import dev.ultreon.libs.commons.v0.vector.Vec4d as _Vec4d
_Vec4d = _Vec4d
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
import java.nio.channels.FileChannel as FileChannel
import java.lang.Double as _double
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
import java.nio.charset.Charset as Charset
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
try:
    from pycorelibs.commons.v0 import tuple
except ImportError:
    tuple = _import_once("pycorelibs.commons.v0.tuple")

import java.lang.String as _string
import java.nio.ByteOrder as _ByteOrder
_ByteOrder = _ByteOrder
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
from builtins import str
from pyquantum_helper import override
import dev.ultreon.libs.commons.v0.vector.Vec2d as _Vec2d
_Vec2d = _Vec2d
import dev.ultreon.libs.commons.v0.vector.Vec4i as _Vec4i
_Vec4i = _Vec4i
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
import java.nio.channels.ScatteringByteChannel as ScatteringByteChannel
import dev.ultreon.quantum.network.partial.PartialPacket as _PartialPacket
_PartialPacket = _PartialPacket
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.libs.commons.v0.vector.Vec3f as _Vec3f
_Vec3f = _Vec3f
import dev.ultreon.libs.commons.v0.tuple.Pair as _Pair
_Pair = _Pair
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import java.io.InputStream as InputStream
import java.util.function.Function as Function
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

 
class PacketIO():
    """dev.ultreon.quantum.network.PacketIO"""
 
    @staticmethod
    def _wrap(java_value: _PacketIO) -> 'PacketIO':
        return PacketIO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketIO):
        """
        Dynamic initializer for PacketIO.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketIO__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketIO__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isReadable(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.isReadable(int)"""
        return bool._wrap(super(_PacketIO, self).isReadable(_int.valueOf(arg0)))

    @overload
    def writeFloat(self, arg0: float) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeFloat(float)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeFloat(_float.valueOf(arg0)))

    @overload
    def writeBytes(self, arg0: bytes) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeBytes(byte[])"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeBytes(bytes))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.equals(java.lang.Object)"""
        return bool._wrap(super(_PacketIO, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def writeTextObject(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.network.PacketIO.writeTextObject(dev.ultreon.quantum.text.TextObject)"""
        super(_PacketIO, self).writeTextObject(arg0)

    @overload
    def writeVec2i(self, arg0: 'Vec2i'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec2i(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        super(_PacketIO, self).writeVec2i(arg0)

    @overload
    def readVec2f(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.network.PacketIO.readVec2f()"""
        return 'vector.Vec2f'._wrap(super(PacketIO, self).readVec2f())

    @overload
    def writeUbo(self, arg0: 'DataType'):
        """public void dev.ultreon.quantum.network.PacketIO.writeUbo(dev.ultreon.ubo.types.DataType<?>)"""
        super(_PacketIO, self).writeUbo(arg0)

    @overload
    def readShort(self) -> int:
        """public short dev.ultreon.quantum.network.PacketIO.readShort()"""
        return int._wrap(super(PacketIO, self).readShort())

    @overload
    def writeId(self, arg0: 'Identifier'):
        """public void dev.ultreon.quantum.network.PacketIO.writeId(dev.ultreon.quantum.util.Identifier)"""
        super(_PacketIO, self).writeId(arg0)

    @overload
    def writeBytes(self, arg0: 'InputStream', arg1: int):
        """public void dev.ultreon.quantum.network.PacketIO.writeBytes(java.io.InputStream,int)"""
        super(_PacketIO, self).writeBytes(arg0, _int.valueOf(arg1))

    @overload
    def readUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.network.PacketIO.readUuid()"""
        return 'UUID'._wrap(super(PacketIO, self).readUuid())

    @overload
    def readBytes(self, arg0: 'FileChannel', arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.readBytes(java.nio.channels.FileChannel,long,int)"""
        return int._wrap(super(_PacketIO, self).readBytes(arg0, _long.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def readChunkPos(self) -> 'world.ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.network.PacketIO.readChunkPos()"""
        return 'world.ChunkPos'._wrap(super(PacketIO, self).readChunkPos())

    @overload
    def writeList(self, arg0: 'List', arg1: 'BiConsumer') -> 'PacketIO':
        """public <T> dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeList(java.util.List<T>,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, T>)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeList(arg0, arg1))

    @overload
    def readBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.network.PacketIO.readBlockMeta()"""
        return 'state.BlockProperties'._wrap(super(PacketIO, self).readBlockMeta())

    @overload
    def validate(self, arg0: 'List') -> 'List':
        """public final java.util.List<io.netty.buffer.ByteBuf> dev.ultreon.quantum.network.PacketIO.validate(java.util.List<dev.ultreon.quantum.network.partial.PartialPacket>) throws dev.ultreon.quantum.network.PacketIntegrityException"""
        return 'List'._wrap(super(_PacketIO, self).validate(arg0))

    @overload
    def readDouble(self) -> float:
        """public double dev.ultreon.quantum.network.PacketIO.readDouble()"""
        return float._wrap(super(PacketIO, self).readDouble())

    @overload
    def writeVarInt(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeVarInt(int)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeVarInt(_int.valueOf(arg0)))

    @overload
    def readCharSequence(self, arg0: int, arg1: 'Charset') -> 'CharSequence':
        """public java.lang.CharSequence dev.ultreon.quantum.network.PacketIO.readCharSequence(int,java.nio.charset.Charset)"""
        return 'CharSequence'._wrap(super(_PacketIO, self).readCharSequence(_int.valueOf(arg0), arg1))

    @overload
    def writeMedium(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeMedium(int)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeMedium(_int.valueOf(arg0)))

    @overload
    def readBoolean(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.readBoolean()"""
        return bool._wrap(super(PacketIO, self).readBoolean())

    @overload
    def flush(self):
        """public void dev.ultreon.quantum.network.PacketIO.flush()"""
        super(PacketIO, self).flush()

    @overload
    def order(self, arg0: 'ByteOrder') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.order(java.nio.ByteOrder)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).order(arg0))

    @overload
    def hasMemoryAddress(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.hasMemoryAddress()"""
        return bool._wrap(super(PacketIO, self).hasMemoryAddress())

    @overload
    def readMediumArray(self, arg0: int) -> List[int]:
        """public int[] dev.ultreon.quantum.network.PacketIO.readMediumArray(int)"""
        return List[int]._wrap(super(_PacketIO, self).readMediumArray(_int.valueOf(arg0)))

    @overload
    def readBytes(self, arg0: bytes, arg1: int, arg2: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.readBytes(byte[],int,int)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).readBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def writePair(self, arg0: 'Pair', arg1: 'BiConsumer', arg2: 'BiConsumer') -> 'PacketIO':
        """public <F,S> dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writePair(dev.ultreon.libs.commons.v0.tuple.Pair<F, S>,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, F>,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, S>)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writePair(arg0, arg1, arg2))

    @overload
    def getVarIntSize(self, arg0: int) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.getVarIntSize(int)"""
        return int._wrap(super(_PacketIO, self).getVarIntSize(_int.valueOf(arg0)))

    @overload
    def writeUTF(self, arg0: str, arg1: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeUTF(java.lang.String,int)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeUTF(arg0, _int.valueOf(arg1)))

    @overload
    def readList(self, arg0: 'Function') -> 'List':
        """public <T> java.util.List<T> dev.ultreon.quantum.network.PacketIO.readList(java.util.function.Function<dev.ultreon.quantum.network.PacketIO, T>)"""
        return 'List'._wrap(super(_PacketIO, self).readList(arg0))

    @overload
    def writeVec4i(self, arg0: 'Vec4i'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec4i(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        super(_PacketIO, self).writeVec4i(arg0)

    @overload
    def readVec4d(self) -> 'vector.Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.quantum.network.PacketIO.readVec4d()"""
        return 'vector.Vec4d'._wrap(super(PacketIO, self).readVec4d())

    @overload
    def readShortArray(self) -> List[int]:
        """public short[] dev.ultreon.quantum.network.PacketIO.readShortArray()"""
        return List[int]._wrap(super(PacketIO, self).readShortArray())

    @overload
    def writeBoolean(self, arg0: bool) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeBoolean(boolean)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeBoolean(_boolean.valueOf(arg0)))

    @overload
    def writeUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.network.PacketIO.writeUuid(java.util.UUID)"""
        super(_PacketIO, self).writeUuid(arg0)

    @overload
    def readIntArray(self, arg0: int) -> List[int]:
        """public int[] dev.ultreon.quantum.network.PacketIO.readIntArray(int)"""
        return List[int]._wrap(super(_PacketIO, self).readIntArray(_int.valueOf(arg0)))

    @overload
    def writeMap(self, arg0: 'Map', arg1: 'BiConsumer', arg2: 'BiConsumer') -> 'PacketIO':
        """public <K,V> dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeMap(java.util.Map<K, V>,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, K>,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, V>)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeMap(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def readFloatArray(self, arg0: int) -> List[float]:
        """public float[] dev.ultreon.quantum.network.PacketIO.readFloatArray(int)"""
        return List[float]._wrap(super(_PacketIO, self).readFloatArray(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def readMap(self, arg0: 'Function', arg1: 'Function') -> 'Map':
        """public <K,V> java.util.Map<K, V> dev.ultreon.quantum.network.PacketIO.readMap(java.util.function.Function<dev.ultreon.quantum.network.PacketIO, K>,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, V>)"""
        return 'Map'._wrap(super(_PacketIO, self).readMap(arg0, arg1))

    @overload
    def writeChar(self, arg0: str) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeChar(char)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeChar(_char.valueOf(arg0)))

    @overload
    def readLongArray(self) -> List[int]:
        """public long[] dev.ultreon.quantum.network.PacketIO.readLongArray()"""
        return List[int]._wrap(super(PacketIO, self).readLongArray())

    @overload
    def capacity(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.capacity(int)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).capacity(_int.valueOf(arg0)))

    @overload
    def writeIntArray(self, arg0: 'int') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeIntArray(int[])"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeIntArray(arg0))

    @overload
    def isDirect(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.isDirect()"""
        return bool._wrap(super(PacketIO, self).isDirect())

    @overload
    def arrayOffset(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.arrayOffset()"""
        return int._wrap(super(PacketIO, self).arrayOffset())

    @overload
    def readId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.network.PacketIO.readId()"""
        return 'util.Identifier'._wrap(super(PacketIO, self).readId())

    @overload
    def toString(self, arg0: 'Charset') -> str:
        """public java.lang.String dev.ultreon.quantum.network.PacketIO.toString(java.nio.charset.Charset)"""
        return str._wrap(super(_PacketIO, self).toString(arg0))

    @overload
    def readTextObject(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.network.PacketIO.readTextObject()"""
        return 'text.TextObject'._wrap(super(PacketIO, self).readTextObject())

    @overload
    def writeBytes(self, arg0: 'FileChannel', arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.writeBytes(java.nio.channels.FileChannel,long,int)"""
        return int._wrap(super(_PacketIO, self).writeBytes(arg0, _long.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def writeDoubleArray(self, arg0: 'double') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeDoubleArray(double[])"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeDoubleArray(arg0))

    @overload
    def writeBitSet(self, arg0: 'BitSet') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeBitSet(java.util.BitSet)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeBitSet(arg0))

    @overload
    def writeDouble(self, arg0: float) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeDouble(double)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeDouble(_double.valueOf(arg0)))

    @overload
    def readableBytes(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.readableBytes()"""
        return int._wrap(super(PacketIO, self).readableBytes())

    @overload
    def readIntArray(self) -> List[int]:
        """public int[] dev.ultreon.quantum.network.PacketIO.readIntArray()"""
        return List[int]._wrap(super(PacketIO, self).readIntArray())

    @overload
    def readMap(self, arg0: 'Function', arg1: 'Function', arg2: int) -> 'Map':
        """public <K,V> java.util.Map<K, V> dev.ultreon.quantum.network.PacketIO.readMap(java.util.function.Function<dev.ultreon.quantum.network.PacketIO, K>,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, V>,int)"""
        return 'Map'._wrap(super(_PacketIO, self).readMap(arg0, arg1, _int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def unwrap(self) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.unwrap()"""
        return 'PacketIO'._wrap(super(PacketIO, self).unwrap())

    @overload
    def readEnum(self, arg0: 'Enum') -> 'Enum':
        """public <T extends java.lang.Enum<T>> T dev.ultreon.quantum.network.PacketIO.readEnum(T)"""
        return 'Enum'._wrap(super(_PacketIO, self).readEnum(arg0))

    @overload
    def readShortArray(self, arg0: int) -> List[int]:
        """public short[] dev.ultreon.quantum.network.PacketIO.readShortArray(int)"""
        return List[int]._wrap(super(_PacketIO, self).readShortArray(_int.valueOf(arg0)))

    @overload
    def readMediumArray(self) -> List[int]:
        """public int[] dev.ultreon.quantum.network.PacketIO.readMediumArray()"""
        return List[int]._wrap(super(PacketIO, self).readMediumArray())

    @overload
    def clear(self) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.clear()"""
        return 'PacketIO'._wrap(super(PacketIO, self).clear())

    @overload
    def writeVec3f(self, arg0: 'Vec3f'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec3f(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        super(_PacketIO, self).writeVec3f(arg0)

    @overload
    def writeChar(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeChar(int)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeChar(_int.valueOf(arg0)))

    @overload
    def writeVec4f(self, arg0: 'Vec4f'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec4f(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        super(_PacketIO, self).writeVec4f(arg0)

    @overload
    def writeShortArray(self, arg0: 'short') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeShortArray(short[])"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeShortArray(arg0))

    @overload
    def hasArray(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.hasArray()"""
        return bool._wrap(super(PacketIO, self).hasArray())

    @overload
    def readInt(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.readInt()"""
        return int._wrap(super(PacketIO, self).readInt())

    @overload
    def __init__(self, arg0: 'InputStream', arg1: 'OutputStream', arg2: 'List'):
        """public dev.ultreon.quantum.network.PacketIO(java.io.InputStream,java.io.OutputStream,java.util.List<dev.ultreon.quantum.network.partial.PartialPacket>) throws dev.ultreon.quantum.network.PacketIntegrityException"""
        val = _PacketIO(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def readLongArray(self, arg0: int) -> List[int]:
        """public long[] dev.ultreon.quantum.network.PacketIO.readLongArray(int)"""
        return List[int]._wrap(super(_PacketIO, self).readLongArray(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def writeBlockMeta(self, arg0: 'BlockProperties'):
        """public void dev.ultreon.quantum.network.PacketIO.writeBlockMeta(dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_PacketIO, self).writeBlockMeta(arg0)

    @overload
    def maxCapacity(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.maxCapacity()"""
        return int._wrap(super(PacketIO, self).maxCapacity())

    @overload
    def readBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.network.PacketIO.readBlockPos()"""
        return 'world.BlockPos'._wrap(super(PacketIO, self).readBlockPos())

    @overload
    def readVec4f(self) -> 'vector.Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.quantum.network.PacketIO.readVec4f()"""
        return 'vector.Vec4f'._wrap(super(PacketIO, self).readVec4f())

    @overload
    def writeBlockPos(self, arg0: 'BlockPos') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeBlockPos(dev.ultreon.quantum.world.BlockPos)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeBlockPos(arg0))

    @overload
    def asPacketBuffer(self) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.asPacketBuffer()"""
        return 'PacketIO'._wrap(super(PacketIO, self).asPacketBuffer())

    @overload
    def readString(self, arg0: int) -> str:
        """public java.lang.String dev.ultreon.quantum.network.PacketIO.readString(int)"""
        return str._wrap(super(_PacketIO, self).readString(_int.valueOf(arg0)))

    @overload
    def readVec3d(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.network.PacketIO.readVec3d()"""
        return 'vector.Vec3d'._wrap(super(PacketIO, self).readVec3d())

    @overload
    def writeInt(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeInt(int)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeInt(_int.valueOf(arg0)))

    @overload
    def writeVec2f(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec2f(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_PacketIO, self).writeVec2f(arg0)

    @overload
    def readVec3i(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.network.PacketIO.readVec3i()"""
        return 'vector.Vec3i'._wrap(super(PacketIO, self).readVec3i())

    @overload
    def readList(self, arg0: 'Function', arg1: int) -> 'List':
        """public <T> java.util.List<T> dev.ultreon.quantum.network.PacketIO.readList(java.util.function.Function<dev.ultreon.quantum.network.PacketIO, T>,int)"""
        return 'List'._wrap(super(_PacketIO, self).readList(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def readChar(self) -> str:
        """public char dev.ultreon.quantum.network.PacketIO.readChar()"""
        return str._wrap(super(PacketIO, self).readChar())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def writeByteArray(self, arg0: bytes, arg1: int):
        """public void dev.ultreon.quantum.network.PacketIO.writeByteArray(byte[],int)"""
        super(_PacketIO, self).writeByteArray(bytes, _int.valueOf(arg1))

    @overload
    def readFloatArray(self) -> List[float]:
        """public float[] dev.ultreon.quantum.network.PacketIO.readFloatArray()"""
        return List[float]._wrap(super(PacketIO, self).readFloatArray())

    @overload
    def readDoubleArray(self, arg0: int) -> List[float]:
        """public double[] dev.ultreon.quantum.network.PacketIO.readDoubleArray(int)"""
        return List[float]._wrap(super(_PacketIO, self).readDoubleArray(_int.valueOf(arg0)))

    @overload
    def writeBytes(self, arg0: bytes, arg1: int, arg2: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeBytes(byte[],int,int)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def writeVec3i(self, arg0: 'Vec3i'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec3i(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        super(_PacketIO, self).writeVec3i(arg0)

    @overload
    def array(self) -> List[int]:
        """public byte[] dev.ultreon.quantum.network.PacketIO.array()"""
        return List[int]._wrap(super(PacketIO, self).array())

    @overload
    def readLong(self) -> int:
        """public long dev.ultreon.quantum.network.PacketIO.readLong()"""
        return int._wrap(super(PacketIO, self).readLong())

    @overload
    def writeChunkPos(self, arg0: 'ChunkPos') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeChunkPos(dev.ultreon.quantum.world.ChunkPos)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeChunkPos(arg0))

    @overload
    def writeMediumArray(self, arg0: 'int') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeMediumArray(int[])"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeMediumArray(arg0))

    @overload
    def memoryAddress(self) -> int:
        """public long dev.ultreon.quantum.network.PacketIO.memoryAddress()"""
        return int._wrap(super(PacketIO, self).memoryAddress())

    @overload
    def readVarInt(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.readVarInt()"""
        return int._wrap(super(PacketIO, self).readVarInt())

    @overload
    def writeByte(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeByte(int)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeByte(_int.valueOf(arg0)))

    @overload
    def readBitSet(self) -> 'BitSet':
        """public java.util.BitSet dev.ultreon.quantum.network.PacketIO.readBitSet()"""
        return 'BitSet'._wrap(super(PacketIO, self).readBitSet())

    @overload
    def readBytes(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.readBytes(int)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).readBytes(_int.valueOf(arg0)))

    @overload
    def isReadable(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.isReadable()"""
        return bool._wrap(super(PacketIO, self).isReadable())

    @overload
    def writeItemStack(self, arg0: 'ItemStack') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeItemStack(dev.ultreon.quantum.item.ItemStack)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeItemStack(arg0))

    @overload
    def order(self) -> 'ByteOrder':
        """public java.nio.ByteOrder dev.ultreon.quantum.network.PacketIO.order()"""
        return 'ByteOrder'._wrap(super(PacketIO, self).order())

    @overload
    def capacity(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.capacity()"""
        return int._wrap(super(PacketIO, self).capacity())

    @overload
    def readUnsignedShort(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.readUnsignedShort()"""
        return int._wrap(super(PacketIO, self).readUnsignedShort())

    @overload
    def readByte(self) -> int:
        """public byte dev.ultreon.quantum.network.PacketIO.readByte()"""
        return int._wrap(super(PacketIO, self).readByte())

    @overload
    def writeVec2f(self, arg0: 'Vec2d'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec2f(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        super(_PacketIO, self).writeVec2f(arg0)

    @overload
    def isReadOnly(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.isReadOnly()"""
        return bool._wrap(super(PacketIO, self).isReadOnly())

    @overload
    def writeLongArray(self, arg0: 'long') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeLongArray(long[])"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeLongArray(arg0))

    @overload
    def readItemStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.network.PacketIO.readItemStack()"""
        return 'item.ItemStack'._wrap(super(PacketIO, self).readItemStack())

    @overload
    def __init__(self, arg0: 'Socket'):
        """public dev.ultreon.quantum.network.PacketIO(java.net.Socket) throws java.io.IOException"""
        val = _PacketIO(arg0)
        self.__wrapper = val

    @overload
    def split(self, arg0: int, arg1: int) -> List['partial.PartialPacket']:
        """public dev.ultreon.quantum.network.partial.PartialPacket[] dev.ultreon.quantum.network.PacketIO.split(int,long)"""
        return List['partial.PartialPacket']._wrap(super(_PacketIO, self).split(_int.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def readVec4i(self) -> 'vector.Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.quantum.network.PacketIO.readVec4i()"""
        return 'vector.Vec4i'._wrap(super(PacketIO, self).readVec4i())

    @overload
    def readDoubleArray(self) -> List[float]:
        """public double[] dev.ultreon.quantum.network.PacketIO.readDoubleArray()"""
        return List[float]._wrap(super(PacketIO, self).readDoubleArray())

    @overload
    def readUnsignedByte(self) -> int:
        """public short dev.ultreon.quantum.network.PacketIO.readUnsignedByte()"""
        return int._wrap(super(PacketIO, self).readUnsignedByte())

    @overload
    def readUbo(self, *arg0: 'types.DataType') -> 'types.DataType':
        """public final <T extends dev.ultreon.ubo.types.DataType<?>> T dev.ultreon.quantum.network.PacketIO.readUbo(T...)"""
        return 'types.DataType'._wrap(super(_PacketIO, self).readUbo(arg0))

    @overload
    def readVec2d(self) -> 'vector.Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.quantum.network.PacketIO.readVec2d()"""
        return 'vector.Vec2d'._wrap(super(PacketIO, self).readVec2d())

    @overload
    def writeLong(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeLong(long)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeLong(_long.valueOf(arg0)))

    @overload
    def readVec2i(self) -> 'vector.Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.network.PacketIO.readVec2i()"""
        return 'vector.Vec2i'._wrap(super(PacketIO, self).readVec2i())

    @overload
    def readMedium(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.readMedium()"""
        return int._wrap(super(PacketIO, self).readMedium())

    @overload
    def writeFloatArray(self, arg0: 'float') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeFloatArray(float[])"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeFloatArray(arg0))

    @overload
    def writeShort(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeShort(int)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).writeShort(_int.valueOf(arg0)))

    @overload
    def writeVec3d(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec3d(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_PacketIO, self).writeVec3d(arg0)

    @overload
    def readBytes(self, arg0: 'OutputStream', arg1: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.readBytes(java.io.OutputStream,int)"""
        return 'PacketIO'._wrap(super(_PacketIO, self).readBytes(arg0, _int.valueOf(arg1)))

    @overload
    def readFloat(self) -> float:
        """public float dev.ultreon.quantum.network.PacketIO.readFloat()"""
        return float._wrap(super(PacketIO, self).readFloat())

    @overload
    def readByteArray(self, arg0: int) -> List[int]:
        """public byte[] dev.ultreon.quantum.network.PacketIO.readByteArray(int)"""
        return List[int]._wrap(super(_PacketIO, self).readByteArray(_int.valueOf(arg0)))

    @overload
    def isWritable(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.isWritable()"""
        return bool._wrap(super(PacketIO, self).isWritable())

    @overload
    def readVec3f(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.network.PacketIO.readVec3f()"""
        return 'vector.Vec3f'._wrap(super(PacketIO, self).readVec3f())

    @overload
    def writeVec4d(self, arg0: 'Vec4d'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec4d(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        super(_PacketIO, self).writeVec4d(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.PacketIO.toString()"""
        return str._wrap(super(PacketIO, self).toString())

    @overload
    def isWritable(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.isWritable(int)"""
        return bool._wrap(super(_PacketIO, self).isWritable(_int.valueOf(arg0)))

    @overload
    def readPair(self, arg0: 'Function', arg1: 'Function') -> 'tuple.Pair':
        """public <F,S> dev.ultreon.libs.commons.v0.tuple.Pair<F, S> dev.ultreon.quantum.network.PacketIO.readPair(java.util.function.Function<dev.ultreon.quantum.network.PacketIO, F>,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, S>)"""
        return 'tuple.Pair'._wrap(super(_PacketIO, self).readPair(arg0, arg1))

    @overload
    def readBytes(self, arg0: bytes) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.readBytes(byte[])"""
        return 'PacketIO'._wrap(super(_PacketIO, self).readBytes(bytes))

    @overload
    def writeBytes(self, arg0: 'ScatteringByteChannel', arg1: int):
        """public void dev.ultreon.quantum.network.PacketIO.writeBytes(java.nio.channels.ScatteringByteChannel,int)"""
        super(_PacketIO, self).writeBytes(arg0, _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'InputStream', arg1: 'OutputStream'):
        """public dev.ultreon.quantum.network.PacketIO(java.io.InputStream,java.io.OutputStream)"""
        val = _PacketIO(arg0, arg1)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.PacketHandler
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.network.PacketHandler as _PacketHandler
_PacketHandler = _PacketHandler
from builtins import bool
 
class PacketHandler():
    """dev.ultreon.quantum.network.PacketHandler"""
 
    @staticmethod
    def _wrap(java_value: _PacketHandler) -> 'PacketHandler':
        return PacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketHandler):
        """
        Dynamic initializer for PacketHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool._wrap(super(_PacketHandler, self).shouldHandlePacket(arg0))

    @abstractmethod
    def context(self, ):
        """public abstract dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.network.PacketHandler.context()"""
        pass

    @abstractmethod
    def destination(self, ):
        """public abstract dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.PacketHandler.destination()"""
        pass

    @abstractmethod
    def onDisconnect(self, arg0: str):
        """public abstract void dev.ultreon.quantum.network.PacketHandler.onDisconnect(java.lang.String)"""
        pass

    @abstractmethod
    def isAcceptingPackets(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isAcceptingPackets()"""
        pass

    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool._wrap(super(PacketHandler, self).isAsync())

    @abstractmethod
    def isDisconnected(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isDisconnected()"""
        pass

    @abstractmethod
    def reply(self, arg0: int):
        """public abstract dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.PacketHandler.reply(long)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.network.PacketException
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
import dev.ultreon.quantum.network.PacketException as _PacketException
_PacketException = _PacketException
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketException():
    """dev.ultreon.quantum.network.PacketException"""
 
    @staticmethod
    def _wrap(java_value: _PacketException) -> 'PacketException':
        return PacketException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketException):
        """
        Dynamic initializer for PacketException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

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
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.network.PacketException(java.lang.Throwable)"""
        val = _PacketException(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.PacketException()"""
        val = _PacketException()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.PacketException()"""
        val = _PacketException()
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.PacketException(java.lang.String)"""
        val = _PacketException(arg0)
        self.__wrapper = val

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.network.PacketException(java.lang.String,java.lang.Throwable)"""
        val = _PacketException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.MemoryNetworker
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.network.system.MemoryConnection as _MemoryConnection
_MemoryConnection = _MemoryConnection
import java.lang.Integer as _int
import dev.ultreon.quantum.network.MemoryNetworker as _MemoryNetworker
_MemoryNetworker = _MemoryNetworker
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MemoryNetworker():
    """dev.ultreon.quantum.network.MemoryNetworker"""
 
    @staticmethod
    def _wrap(java_value: _MemoryNetworker) -> 'MemoryNetworker':
        return MemoryNetworker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MemoryNetworker):
        """
        Dynamic initializer for MemoryNetworker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MemoryNetworker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MemoryNetworker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setOtherSide(self, arg0: 'MemoryConnection'):
        """public void dev.ultreon.quantum.network.MemoryNetworker.setOtherSide(dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        super(_MemoryNetworker, self).setOtherSide(arg0)

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

    @overload
    def __init__(self, arg0: 'QuantumServer', arg1: 'MemoryConnection'):
        """public dev.ultreon.quantum.network.MemoryNetworker(dev.ultreon.quantum.server.QuantumServer,dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        val = _MemoryNetworker(arg0, arg1)
        self.__wrapper = val

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
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.network.MemoryNetworker.isRunning()"""
        return bool._wrap(super(MemoryNetworker, self).isRunning())

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
    def tick(self):
        """public void dev.ultreon.quantum.network.MemoryNetworker.tick()"""
        super(MemoryNetworker, self).tick()

    @overload
    def getOtherSide(self) -> 'system.MemoryConnection':
        """public dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.MemoryNetworker.getOtherSide()"""
        return 'system.MemoryConnection'._wrap(super(MemoryNetworker, self).getOtherSide())

    @override
    @overload
    def getConnections(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.network.system.ServerMemoryConnection> dev.ultreon.quantum.network.MemoryNetworker.getConnections()"""
        return 'List'._wrap(super(MemoryNetworker, self).getConnections())

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.MemoryNetworker.close()"""
        super(MemoryNetworker, self).close()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.PacketData
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.PacketData as _PacketData
_PacketData = _PacketData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import dev.ultreon.quantum.network.packets.Packet as _Packet
_Packet = _Packet
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketData():
    """dev.ultreon.quantum.network.PacketData"""
 
    @staticmethod
    def _wrap(java_value: _PacketData) -> 'PacketData':
        return PacketData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketData):
        """
        Dynamic initializer for PacketData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def decode(self, arg0: int, arg1: 'PacketIO') -> 'packets.Packet':
        """public dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.PacketData.decode(int,dev.ultreon.quantum.network.PacketIO)"""
        return 'packets.Packet'._wrap(super(_PacketData, self).decode(_int.valueOf(arg0), arg1))

    @overload
    def handle(self, arg0: 'Packet', arg1: 'PacketContext', arg2: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.PacketData.handle(dev.ultreon.quantum.network.packets.Packet<T>,dev.ultreon.quantum.network.PacketContext,T)"""
        super(_PacketData, self).handle(arg0, arg1, arg2)

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
    def encode(self, arg0: 'Packet', arg1: 'PacketIO'):
        """public void dev.ultreon.quantum.network.PacketData.encode(dev.ultreon.quantum.network.packets.Packet<?>,dev.ultreon.quantum.network.PacketIO)"""
        super(_PacketData, self).encode(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getId(self, arg0: 'Packet') -> int:
        """public int dev.ultreon.quantum.network.PacketData.getId(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return int._wrap(super(_PacketData, self).getId(arg0))

    @overload
    def __init__(self, arg0: 'PacketCollection'):
        """public dev.ultreon.quantum.network.PacketData(dev.ultreon.quantum.network.PacketCollection<T>)"""
        val = _PacketData(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.PacketOverflowException
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
import dev.ultreon.quantum.network.PacketOverflowException as _PacketOverflowException
_PacketOverflowException = _PacketOverflowException
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketOverflowException():
    """dev.ultreon.quantum.network.PacketOverflowException"""
 
    @staticmethod
    def _wrap(java_value: _PacketOverflowException) -> 'PacketOverflowException':
        return PacketOverflowException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketOverflowException):
        """
        Dynamic initializer for PacketOverflowException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketOverflowException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketOverflowException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

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

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int):
        """public dev.ultreon.quantum.network.PacketOverflowException(java.lang.String,int,int)"""
        val = _PacketOverflowException(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.network.ReplyPacket
import dev.ultreon.quantum.network.ReplyPacket as _ReplyPacket
_ReplyPacket = _ReplyPacket
 
class ReplyPacket():
    """dev.ultreon.quantum.network.ReplyPacket"""
 
    @staticmethod
    def _wrap(java_value: _ReplyPacket) -> 'ReplyPacket':
        return ReplyPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReplyPacket):
        """
        Dynamic initializer for ReplyPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReplyPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReplyPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__)) 
 
 
# CLASS: dev.ultreon.quantum.network.NetworkChannel
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.network.NetworkChannel as _NetworkChannel
_NetworkChannel = _NetworkChannel
import java.util.function.Function as _Function
_Function = _Function
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
try:
    from pyquantum.network.api import packet
except ImportError:
    packet = _import_once("pyquantum.network.api.packet")

import java.lang.Runnable as Runnable
import java.util.function.BiConsumer as _BiConsumer
_BiConsumer = _BiConsumer
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.function.BiConsumer as BiConsumer
import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import java.util.function.Function as Function
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class NetworkChannel():
    """dev.ultreon.quantum.network.NetworkChannel"""
 
    @staticmethod
    def _wrap(java_value: _NetworkChannel) -> 'NetworkChannel':
        return NetworkChannel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NetworkChannel):
        """
        Dynamic initializer for NetworkChannel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NetworkChannel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NetworkChannel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getChannel(arg0: 'Identifier') -> 'NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.NetworkChannel.getChannel(dev.ultreon.quantum.util.Identifier)"""
        return NetworkChannel._wrap(_NetworkChannel.getChannel(arg0))

    @overload
    def getDecoder(self, arg0: int) -> 'Function':
        """public java.util.function.Function<dev.ultreon.quantum.network.PacketIO, ? extends dev.ultreon.quantum.network.api.packet.ModPacket<?>> dev.ultreon.quantum.network.NetworkChannel.getDecoder(int)"""
        return 'Function'._wrap(super(_NetworkChannel, self).getDecoder(_int.valueOf(arg0)))

    @overload
    def getEncoder(self, arg0: 'Class') -> 'BiConsumer':
        """public java.util.function.BiConsumer<? extends dev.ultreon.quantum.network.api.packet.ModPacket<?>, dev.ultreon.quantum.network.PacketIO> dev.ultreon.quantum.network.NetworkChannel.getEncoder(java.lang.Class<? extends dev.ultreon.quantum.network.api.packet.ModPacket<?>>)"""
        return 'BiConsumer'._wrap(super(_NetworkChannel, self).getEncoder(arg0))

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

    @overload
    def sendToServer(self, arg0: 'ModPacket'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ClientEndpoint> void dev.ultreon.quantum.network.NetworkChannel.sendToServer(dev.ultreon.quantum.network.api.packet.ModPacket<T>)"""
        super(_NetworkChannel, self).sendToServer(arg0)

    @overload
    def getId(self, arg0: 'ModPacket') -> int:
        """public int dev.ultreon.quantum.network.NetworkChannel.getId(dev.ultreon.quantum.network.api.packet.ModPacket<?>)"""
        return int._wrap(super(_NetworkChannel, self).getId(arg0))

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

    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.network.NetworkChannel.id()"""
        return 'util.Identifier'._wrap(super(NetworkChannel, self).id())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def sendToPlayer(self, arg0: 'ServerPlayer', arg1: 'ModPacket'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ClientEndpoint> void dev.ultreon.quantum.network.NetworkChannel.sendToPlayer(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.network.api.packet.ModPacket<T>)"""
        super(_NetworkChannel, self).sendToPlayer(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create(arg0: 'Identifier') -> 'NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.NetworkChannel.create(dev.ultreon.quantum.util.Identifier)"""
        return NetworkChannel._wrap(_NetworkChannel.create(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setC2sConnection(self, arg0: 'IConnection'):
        """public void dev.ultreon.quantum.network.NetworkChannel.setC2sConnection(dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        super(_NetworkChannel, self).setC2sConnection(arg0)

    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.NetworkChannel.queue(java.lang.Runnable)"""
        super(_NetworkChannel, self).queue(arg0)

    @overload
    def getConsumer(self, arg0: 'Class') -> 'BiConsumer':
        """public java.util.function.BiConsumer<? extends dev.ultreon.quantum.network.api.packet.ModPacket<?>, java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>> dev.ultreon.quantum.network.NetworkChannel.getConsumer(java.lang.Class<? extends dev.ultreon.quantum.network.api.packet.ModPacket<?>>)"""
        return 'BiConsumer'._wrap(super(_NetworkChannel, self).getConsumer(arg0))

    @overload
    def register(self, arg0: 'Class', arg1: 'BiConsumer', arg2: 'Function', arg3: 'BiConsumer'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T>> void dev.ultreon.quantum.network.NetworkChannel.register(java.lang.Class<T>,java.util.function.BiConsumer<T, dev.ultreon.quantum.network.PacketIO>,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, T>,java.util.function.BiConsumer<T, java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>>)"""
        super(_NetworkChannel, self).register(arg0, arg1, arg2, arg3)

    @overload
    def sendToPlayers(self, arg0: 'List', arg1: 'ModPacket'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ClientEndpoint> void dev.ultreon.quantum.network.NetworkChannel.sendToPlayers(java.util.List<dev.ultreon.quantum.server.player.ServerPlayer>,dev.ultreon.quantum.network.api.packet.ModPacket<T>)"""
        super(_NetworkChannel, self).sendToPlayers(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.ServerHostingException
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
import dev.ultreon.quantum.network.ServerHostingException as _ServerHostingException
_ServerHostingException = _ServerHostingException
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ServerHostingException():
    """dev.ultreon.quantum.network.ServerHostingException"""
 
    @staticmethod
    def _wrap(java_value: _ServerHostingException) -> 'ServerHostingException':
        return ServerHostingException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerHostingException):
        """
        Dynamic initializer for ServerHostingException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerHostingException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerHostingException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

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

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.network.ServerHostingException(java.lang.String,java.lang.Throwable)"""
        val = _ServerHostingException(arg0, arg1)
        self.__wrapper = val

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.ServerHostingException(java.lang.String)"""
        val = _ServerHostingException(arg0)
        self.__wrapper = val

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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.network.ServerHostingException(java.lang.Throwable)"""
        val = _ServerHostingException(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.ServerHostingException()"""
        val = _ServerHostingException()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.ServerHostingException()"""
        val = _ServerHostingException()
        self.__wrapper = val

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.PacketListener
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
import java.lang.Runnable as Runnable
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import dev.ultreon.quantum.network.packets.Packet as _Packet
_Packet = _Packet
import dev.ultreon.quantum.network.PacketListener as _PacketListener
_PacketListener = _PacketListener
 
class PacketListener():
    """dev.ultreon.quantum.network.PacketListener"""
 
    @staticmethod
    def _wrap(java_value: _PacketListener) -> 'PacketListener':
        return PacketListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketListener):
        """
        Dynamic initializer for PacketListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def onSuccess(arg0: 'Runnable') -> 'PacketListener':
        """public static dev.ultreon.quantum.network.PacketListener dev.ultreon.quantum.network.PacketListener.onSuccess(java.lang.Runnable)"""
        return PacketListener._wrap(_PacketListener.onSuccess(arg0))

    @staticmethod
    @overload
    def onFailure(arg0: 'Supplier') -> 'PacketListener':
        """public static dev.ultreon.quantum.network.PacketListener dev.ultreon.quantum.network.PacketListener.onFailure(java.util.function.Supplier<dev.ultreon.quantum.network.packets.Packet<?>>)"""
        return PacketListener._wrap(_PacketListener.onFailure(arg0))

    @overload
    def onSuccess(self):
        """public default void dev.ultreon.quantum.network.PacketListener.onSuccess()"""
        super(PacketListener, self).onSuccess()

    @staticmethod
    @overload
    def onEither(arg0: 'Runnable') -> 'PacketListener':
        """public static dev.ultreon.quantum.network.PacketListener dev.ultreon.quantum.network.PacketListener.onEither(java.lang.Runnable)"""
        return PacketListener._wrap(_PacketListener.onEither(arg0))

    @overload
    def onFailure(self) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.PacketListener.onFailure()"""
        return 'packets.Packet'._wrap(super(PacketListener, self).onFailure()) 
 
 
# CLASS: dev.ultreon.quantum.network.PacketIntegrityException
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
import dev.ultreon.quantum.network.PacketIntegrityException as _PacketIntegrityException
_PacketIntegrityException = _PacketIntegrityException
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketIntegrityException():
    """dev.ultreon.quantum.network.PacketIntegrityException"""
 
    @staticmethod
    def _wrap(java_value: _PacketIntegrityException) -> 'PacketIntegrityException':
        return PacketIntegrityException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketIntegrityException):
        """
        Dynamic initializer for PacketIntegrityException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketIntegrityException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketIntegrityException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

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

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.network.PacketIntegrityException(java.lang.String,java.lang.Throwable)"""
        val = _PacketIntegrityException(arg0, arg1)
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.network.PacketIntegrityException(java.lang.Throwable)"""
        val = _PacketIntegrityException(arg0)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.PacketIntegrityException()"""
        val = _PacketIntegrityException()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.PacketIntegrityException(java.lang.String)"""
        val = _PacketIntegrityException(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.PacketIntegrityException()"""
        val = _PacketIntegrityException()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.MemoryConnectionContext
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.MemoryConnectionContext as _MemoryConnectionContext
_MemoryConnectionContext = _MemoryConnectionContext
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.network.system.MemoryConnection as _MemoryConnection
_MemoryConnection = _MemoryConnection
import java.lang.Integer as _int
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MemoryConnectionContext():
    """dev.ultreon.quantum.network.MemoryConnectionContext"""
 
    @staticmethod
    def _wrap(java_value: _MemoryConnectionContext) -> 'MemoryConnectionContext':
        return MemoryConnectionContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MemoryConnectionContext):
        """
        Dynamic initializer for MemoryConnectionContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MemoryConnectionContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MemoryConnectionContext__wrapper":
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.MemoryConnectionContext()"""
        val = _MemoryConnectionContext()
        self.__wrapper = val

    @staticmethod
    @overload
    def get() -> 'system.MemoryConnection':
        """public static dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.MemoryConnectionContext.get()"""
        return system.MemoryConnection._wrap(_MemoryConnectionContext.get())

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.MemoryConnectionContext()"""
        val = _MemoryConnectionContext()
        self.__wrapper = val

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

    @staticmethod
    @overload
    def set(arg0: 'MemoryConnection'):
        """public static void dev.ultreon.quantum.network.MemoryConnectionContext.set(dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        _MemoryConnectionContext.set(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.S2CReplyPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.S2CReplyPacket as _S2CReplyPacket
_S2CReplyPacket = _S2CReplyPacket
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CReplyPacket():
    """dev.ultreon.quantum.network.S2CReplyPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CReplyPacket) -> 'S2CReplyPacket':
        return S2CReplyPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CReplyPacket):
        """
        Dynamic initializer for S2CReplyPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CReplyPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CReplyPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.S2CReplyPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CReplyPacket, self).toBytes(arg0)

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

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.S2CReplyPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CReplyPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int):
        """public <T extends dev.ultreon.quantum.network.PacketHandler> dev.ultreon.quantum.network.S2CReplyPacket(long)"""
        val = _S2CReplyPacket(_long.valueOf(arg0))
        self.__wrapper = val

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
    def handle(self, arg0: 'PacketContext', arg1: 'ClientPacketHandler'):
        """public void dev.ultreon.quantum.network.S2CReplyPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.ClientPacketHandler)"""
        super(_S2CReplyPacket, self).handle(arg0, arg1)

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
 
 
# CLASS: dev.ultreon.quantum.network.PacketSequence
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import dev.ultreon.quantum.network.packets.Packet as _Packet
_Packet = _Packet
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.network.PacketSequence as _PacketSequence
_PacketSequence = _PacketSequence
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketSequence():
    """dev.ultreon.quantum.network.PacketSequence"""
 
    @staticmethod
    def _wrap(java_value: _PacketSequence) -> 'PacketSequence':
        return PacketSequence(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketSequence):
        """
        Dynamic initializer for PacketSequence.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketSequence__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketSequence__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int, arg1: 'Packet'):
        """public dev.ultreon.quantum.network.PacketSequence(long,dev.ultreon.quantum.network.packets.Packet<T>)"""
        val = _PacketSequence(_long.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.PacketSequence.toString()"""
        return str._wrap(super(PacketSequence, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.PacketSequence.hashCode()"""
        return int._wrap(super(PacketSequence, self).hashCode())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def packet(self) -> 'packets.Packet':
        """public dev.ultreon.quantum.network.packets.Packet<T> dev.ultreon.quantum.network.PacketSequence.packet()"""
        return 'packets.Packet'._wrap(super(PacketSequence, self).packet())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketSequence.equals(java.lang.Object)"""
        return bool._wrap(super(_PacketSequence, self).equals(arg0))

    @overload
    def sequence(self) -> int:
        """public long dev.ultreon.quantum.network.PacketSequence.sequence()"""
        return int._wrap(super(PacketSequence, self).sequence()) 
 
 
# CLASS: dev.ultreon.quantum.network.PacketCollection
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import dev.ultreon.quantum.network.PacketCollection as _PacketCollection
_PacketCollection = _PacketCollection
try:
    from pycorelibs.commons.v0 import tuple
except ImportError:
    tuple = _import_once("pycorelibs.commons.v0.tuple")

try:
    from pyquantum.network import packets
except ImportError:
    packets = _import_once("pyquantum.network.packets")

import dev.ultreon.quantum.network.packets.Packet as _Packet
_Packet = _Packet
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketCollection():
    """dev.ultreon.quantum.network.PacketCollection"""
 
    @staticmethod
    def _wrap(java_value: _PacketCollection) -> 'PacketCollection':
        return PacketCollection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketCollection):
        """
        Dynamic initializer for PacketCollection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketCollection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketCollection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.PacketCollection()"""
        val = _PacketCollection()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: 'Class', arg1: 'BiConsumer', arg2: 'Function', arg3: 'BiConsumer') -> int:
        """public int dev.ultreon.quantum.network.PacketCollection.add(java.lang.Class<? extends dev.ultreon.quantum.network.packets.Packet<?>>,java.util.function.BiConsumer<dev.ultreon.quantum.network.packets.Packet<?>, dev.ultreon.quantum.network.PacketIO>,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, dev.ultreon.quantum.network.packets.Packet<H>>,java.util.function.BiConsumer<dev.ultreon.quantum.network.packets.Packet<H>, dev.ultreon.libs.commons.v0.tuple.Pair<dev.ultreon.quantum.network.PacketContext, H>>)"""
        return int._wrap(super(_PacketCollection, self).add(arg0, arg1, arg2, arg3))

    @overload
    def getId(self, arg0: 'Packet') -> int:
        """public int dev.ultreon.quantum.network.PacketCollection.getId(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return int._wrap(super(_PacketCollection, self).getId(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def encode(self, arg0: 'Packet', arg1: 'PacketIO'):
        """public void dev.ultreon.quantum.network.PacketCollection.encode(dev.ultreon.quantum.network.packets.Packet<?>,dev.ultreon.quantum.network.PacketIO)"""
        super(_PacketCollection, self).encode(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def decode(self, arg0: int, arg1: 'PacketIO') -> 'packets.Packet':
        """public dev.ultreon.quantum.network.packets.Packet<H> dev.ultreon.quantum.network.PacketCollection.decode(int,dev.ultreon.quantum.network.PacketIO)"""
        return 'packets.Packet'._wrap(super(_PacketCollection, self).decode(_int.valueOf(arg0), arg1))

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
    def __init__(self, ):
        """public dev.ultreon.quantum.network.PacketCollection()"""
        val = _PacketCollection()
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'Packet', arg1: 'Pair'):
        """public void dev.ultreon.quantum.network.PacketCollection.handle(dev.ultreon.quantum.network.packets.Packet<H>,dev.ultreon.libs.commons.v0.tuple.Pair<dev.ultreon.quantum.network.PacketContext, H>)"""
        super(_PacketCollection, self).handle(arg0, arg1)

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.WriteOnlyBufferException
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
import dev.ultreon.quantum.network.WriteOnlyBufferException as _WriteOnlyBufferException
_WriteOnlyBufferException = _WriteOnlyBufferException
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WriteOnlyBufferException():
    """dev.ultreon.quantum.network.WriteOnlyBufferException"""
 
    @staticmethod
    def _wrap(java_value: _WriteOnlyBufferException) -> 'WriteOnlyBufferException':
        return WriteOnlyBufferException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WriteOnlyBufferException):
        """
        Dynamic initializer for WriteOnlyBufferException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WriteOnlyBufferException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WriteOnlyBufferException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

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
    def __init__(self, ):
        """public dev.ultreon.quantum.network.WriteOnlyBufferException()"""
        val = _WriteOnlyBufferException()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.WriteOnlyBufferException()"""
        val = _WriteOnlyBufferException()
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
 
 
# CLASS: dev.ultreon.quantum.network.ServerStatusException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.ServerStatusException as _ServerStatusException
_ServerStatusException = _ServerStatusException
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ServerStatusException():
    """dev.ultreon.quantum.network.ServerStatusException"""
 
    @staticmethod
    def _wrap(java_value: _ServerStatusException) -> 'ServerStatusException':
        return ServerStatusException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerStatusException):
        """
        Dynamic initializer for ServerStatusException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerStatusException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerStatusException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.network.ServerStatusException(java.lang.Throwable)"""
        val = _ServerStatusException(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.ServerStatusException()"""
        val = _ServerStatusException()
        self.__wrapper = val

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.network.ServerStatusException(java.lang.String,java.lang.Throwable)"""
        val = _ServerStatusException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.ServerStatusException()"""
        val = _ServerStatusException()
        self.__wrapper = val

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.ServerStatusException(java.lang.String)"""
        val = _ServerStatusException(arg0)
        self.__wrapper = val

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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.PacketContext
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.system.IConnection as _IConnection
_IConnection = _IConnection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.util.Env as _Env
_Env = _Env
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.server.player.ServerPlayer as _ServerPlayer
_ServerPlayer = _ServerPlayer
import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.network.PacketContext as _PacketContext
_PacketContext = _PacketContext
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketContext():
    """dev.ultreon.quantum.network.PacketContext"""
 
    @staticmethod
    def _wrap(java_value: _PacketContext) -> 'PacketContext':
        return PacketContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketContext):
        """
        Dynamic initializer for PacketContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDestination(self) -> 'util.Env':
        """public dev.ultreon.quantum.util.Env dev.ultreon.quantum.network.PacketContext.getDestination()"""
        return 'util.Env'._wrap(super(PacketContext, self).getDestination())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketContext.equals(java.lang.Object)"""
        return bool._wrap(super(_PacketContext, self).equals(arg0))

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
        """public java.lang.String dev.ultreon.quantum.network.PacketContext.toString()"""
        return str._wrap(super(PacketContext, self).toString())

    @overload
    def getPlayer(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.network.PacketContext.getPlayer()"""
        return 'player.ServerPlayer'._wrap(super(PacketContext, self).getPlayer())

    @overload
    def getConnection(self) -> 'system.IConnection':
        """public dev.ultreon.quantum.network.system.IConnection<?, ?> dev.ultreon.quantum.network.PacketContext.getConnection()"""
        return 'system.IConnection'._wrap(super(PacketContext, self).getConnection())

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
    def __init__(self, arg0: 'ServerPlayer', arg1: 'IConnection', arg2: 'Env'):
        """public dev.ultreon.quantum.network.PacketContext(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.network.system.IConnection<?, ?>,dev.ultreon.quantum.util.Env)"""
        val = _PacketContext(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.PacketContext.hashCode()"""
        return int._wrap(super(PacketContext, self).hashCode())

    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.PacketContext.queue(java.lang.Runnable)"""
        super(_PacketContext, self).queue(arg0)

    @overload
    def requirePlayer(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.network.PacketContext.requirePlayer()"""
        return 'player.ServerPlayer'._wrap(super(PacketContext, self).requirePlayer())