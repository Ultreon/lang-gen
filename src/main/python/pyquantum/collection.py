from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.collection.PaletteStorage as __PaletteStorage
__PaletteStorage = __PaletteStorage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import dev.ultreon.quantum.collection.Storage as __Storage
__Storage = __Storage
from builtins import object
from typing import List
import java.util.List as __List
__List = __List
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

import java.util.List as List
 
class PaletteStorage(pyquantum.__ServerDisposable, server.ServerDisposable, __Storage, Storage):
    """dev.ultreon.quantum.collection.PaletteStorage"""
 
    @staticmethod
    def __wrap(java_value: __PaletteStorage) -> 'PaletteStorage':
        return PaletteStorage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PaletteStorage):
        """
        Dynamic initializer for PaletteStorage.
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
    def __init__(self, arg0: object, arg1: int):
        """public dev.ultreon.quantum.collection.PaletteStorage(D,int)"""
        val = __PaletteStorage(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.PaletteStorage.set(int,D)"""
        return bool.__wrap(super(__PaletteStorage, self).set(__int.valueOf(arg0), arg1))

    @overload
    def direct(self, arg0: int) -> object:
        """public D dev.ultreon.quantum.collection.PaletteStorage.direct(int)"""
        return object.__wrap(super(__PaletteStorage, self).direct(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'short', arg1: 'List'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.set(short[],java.util.List<D>)"""
        super(__PaletteStorage, self).set(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def map(self, arg0: object, arg1: 'Function') -> 'Storage':
        """public <R> dev.ultreon.quantum.collection.Storage<R> dev.ultreon.quantum.collection.PaletteStorage.map(R,java.util.function.Function<D, R>)"""
        return 'Storage'.__wrap(super(__PaletteStorage, self).map(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.collection.PaletteStorage.dispose()"""
        super(PaletteStorage, self).dispose()

    @overload
    def remove(self, arg0: int):
        """public void dev.ultreon.quantum.collection.PaletteStorage.remove(int)"""
        super(__PaletteStorage, self).remove(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: object, arg1: 'short', arg2: 'List'):
        """public dev.ultreon.quantum.collection.PaletteStorage(D,short[],java.util.List<D>)"""
        val = __PaletteStorage(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'MapType', arg1: 'Function'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.load(dev.ultreon.ubo.types.MapType,java.util.function.Function<dev.ultreon.ubo.types.MapType, D>)"""
        super(__PaletteStorage, self).load(arg0, arg1)

    @overload
    def getPalette(self) -> List[int]:
        """public short[] dev.ultreon.quantum.collection.PaletteStorage.getPalette()"""
        return List[int].__wrap(super(PaletteStorage, self).getPalette())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.PaletteStorage.equals(java.lang.Object)"""
        return bool.__wrap(super(__PaletteStorage, self).equals(arg0))

    @override
    @overload
    def write(self, arg0: 'PacketIO', arg1: 'BiConsumer'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.write(dev.ultreon.quantum.network.PacketIO,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, D>)"""
        super(__PaletteStorage, self).write(arg0, arg1)

    @overload
    def save(self, arg0: 'MapType', arg1: 'Function') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.collection.PaletteStorage.save(dev.ultreon.ubo.types.MapType,java.util.function.Function<D, dev.ultreon.ubo.types.MapType>)"""
        return 'types.MapType'.__wrap(super(__PaletteStorage, self).save(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: object, arg1: 'PacketIO', arg2: 'Function'):
        """public dev.ultreon.quantum.collection.PaletteStorage(D,dev.ultreon.quantum.network.PacketIO,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, D>)"""
        val = __PaletteStorage(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def add(self, arg0: int, arg1: object) -> int:
        """public short dev.ultreon.quantum.collection.PaletteStorage.add(int,D)"""
        return int.__wrap(super(__PaletteStorage, self).add(__int.valueOf(arg0), arg1))

    @overload
    def toDataIdx(self, arg0: int) -> int:
        """public short dev.ultreon.quantum.collection.PaletteStorage.toDataIdx(int)"""
        return int.__wrap(super(__PaletteStorage, self).toDataIdx(__int.valueOf(arg0)))

    @override
    @overload
    def read(self, arg0: 'PacketIO', arg1: 'Function'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.read(dev.ultreon.quantum.network.PacketIO,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, D>)"""
        super(__PaletteStorage, self).read(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.collection.PaletteStorage.hashCode()"""
        return int.__wrap(super(PaletteStorage, self).hashCode())

    @overload
    def getData(self) -> 'List':
        """public java.util.List<D> dev.ultreon.quantum.collection.PaletteStorage.getData()"""
        return 'List'.__wrap(super(PaletteStorage, self).getData())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: int) -> object:
        """public D dev.ultreon.quantum.collection.PaletteStorage.get(int)"""
        return object.__wrap(super(__PaletteStorage, self).get(__int.valueOf(arg0)))

 
 
 
# CLASS: dev.ultreon.quantum.collection.PaletteStorage
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.collection.PaletteStorage as __PaletteStorage
__PaletteStorage = __PaletteStorage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import dev.ultreon.quantum.collection.Storage as __Storage
__Storage = __Storage
from builtins import object
from typing import List
import java.util.List as __List
__List = __List
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

import java.util.List as List
 
class PaletteStorage(pyquantum.__ServerDisposable, server.ServerDisposable, __Storage, Storage):
    """dev.ultreon.quantum.collection.PaletteStorage"""
 
    @staticmethod
    def __wrap(java_value: __PaletteStorage) -> 'PaletteStorage':
        return PaletteStorage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PaletteStorage):
        """
        Dynamic initializer for PaletteStorage.
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
    def __init__(self, arg0: object, arg1: int):
        """public dev.ultreon.quantum.collection.PaletteStorage(D,int)"""
        val = __PaletteStorage(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.PaletteStorage.set(int,D)"""
        return bool.__wrap(super(__PaletteStorage, self).set(__int.valueOf(arg0), arg1))

    @overload
    def direct(self, arg0: int) -> object:
        """public D dev.ultreon.quantum.collection.PaletteStorage.direct(int)"""
        return object.__wrap(super(__PaletteStorage, self).direct(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'short', arg1: 'List'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.set(short[],java.util.List<D>)"""
        super(__PaletteStorage, self).set(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def map(self, arg0: object, arg1: 'Function') -> 'Storage':
        """public <R> dev.ultreon.quantum.collection.Storage<R> dev.ultreon.quantum.collection.PaletteStorage.map(R,java.util.function.Function<D, R>)"""
        return 'Storage'.__wrap(super(__PaletteStorage, self).map(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.collection.PaletteStorage.dispose()"""
        super(PaletteStorage, self).dispose()

    @overload
    def remove(self, arg0: int):
        """public void dev.ultreon.quantum.collection.PaletteStorage.remove(int)"""
        super(__PaletteStorage, self).remove(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: object, arg1: 'short', arg2: 'List'):
        """public dev.ultreon.quantum.collection.PaletteStorage(D,short[],java.util.List<D>)"""
        val = __PaletteStorage(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'MapType', arg1: 'Function'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.load(dev.ultreon.ubo.types.MapType,java.util.function.Function<dev.ultreon.ubo.types.MapType, D>)"""
        super(__PaletteStorage, self).load(arg0, arg1)

    @overload
    def getPalette(self) -> List[int]:
        """public short[] dev.ultreon.quantum.collection.PaletteStorage.getPalette()"""
        return List[int].__wrap(super(PaletteStorage, self).getPalette())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.PaletteStorage.equals(java.lang.Object)"""
        return bool.__wrap(super(__PaletteStorage, self).equals(arg0))

    @override
    @overload
    def write(self, arg0: 'PacketIO', arg1: 'BiConsumer'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.write(dev.ultreon.quantum.network.PacketIO,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, D>)"""
        super(__PaletteStorage, self).write(arg0, arg1)

    @overload
    def save(self, arg0: 'MapType', arg1: 'Function') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.collection.PaletteStorage.save(dev.ultreon.ubo.types.MapType,java.util.function.Function<D, dev.ultreon.ubo.types.MapType>)"""
        return 'types.MapType'.__wrap(super(__PaletteStorage, self).save(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: object, arg1: 'PacketIO', arg2: 'Function'):
        """public dev.ultreon.quantum.collection.PaletteStorage(D,dev.ultreon.quantum.network.PacketIO,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, D>)"""
        val = __PaletteStorage(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def add(self, arg0: int, arg1: object) -> int:
        """public short dev.ultreon.quantum.collection.PaletteStorage.add(int,D)"""
        return int.__wrap(super(__PaletteStorage, self).add(__int.valueOf(arg0), arg1))

    @overload
    def toDataIdx(self, arg0: int) -> int:
        """public short dev.ultreon.quantum.collection.PaletteStorage.toDataIdx(int)"""
        return int.__wrap(super(__PaletteStorage, self).toDataIdx(__int.valueOf(arg0)))

    @override
    @overload
    def read(self, arg0: 'PacketIO', arg1: 'Function'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.read(dev.ultreon.quantum.network.PacketIO,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, D>)"""
        super(__PaletteStorage, self).read(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.collection.PaletteStorage.hashCode()"""
        return int.__wrap(super(PaletteStorage, self).hashCode())

    @overload
    def getData(self) -> 'List':
        """public java.util.List<D> dev.ultreon.quantum.collection.PaletteStorage.getData()"""
        return 'List'.__wrap(super(PaletteStorage, self).getData())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: int) -> object:
        """public D dev.ultreon.quantum.collection.PaletteStorage.get(int)"""
        return object.__wrap(super(__PaletteStorage, self).get(__int.valueOf(arg0)))

 
 
 
# CLASS: dev.ultreon.quantum.collection.PaletteStorage 
 
 
# CLASS: dev.ultreon.quantum.collection.PaletteIndexException
from builtins import str
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
import dev.ultreon.quantum.collection.PaletteIndexException as __PaletteIndexException
__PaletteIndexException = __PaletteIndexException
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PaletteIndexException(__RuntimeException, RuntimeException):
    """dev.ultreon.quantum.collection.PaletteIndexException"""
 
    @staticmethod
    def __wrap(java_value: __PaletteIndexException) -> 'PaletteIndexException':
        return PaletteIndexException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PaletteIndexException):
        """
        Dynamic initializer for PaletteIndexException.
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
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

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

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.collection.PaletteIndexException(java.lang.String,java.lang.Throwable)"""
        val = __PaletteIndexException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.collection.PaletteIndexException()"""
        val = __PaletteIndexException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.collection.PaletteIndexException(java.lang.String)"""
        val = __PaletteIndexException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.collection.PaletteIndexException()"""
        val = __PaletteIndexException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.collection.PaletteIndexException(java.lang.Throwable)"""
        val = __PaletteIndexException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.collection.FlatStorage
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import dev.ultreon.quantum.collection.Storage as __Storage
__Storage = __Storage
from builtins import object
from typing import List
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.collection.FlatStorage as __FlatStorage
__FlatStorage = __FlatStorage
import java.lang.Object as __Object
__Object = __Object
import it.unimi.dsi.fastutil.shorts.Short2ReferenceFunction as Short2ReferenceFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import it.unimi.dsi.fastutil.objects.Reference2ShortFunction as Reference2ShortFunction
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import java.util.List as List
 
class FlatStorage(__Storage, Storage):
    """dev.ultreon.quantum.collection.FlatStorage"""
 
    @staticmethod
    def __wrap(java_value: __FlatStorage) -> 'FlatStorage':
        return FlatStorage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FlatStorage):
        """
        Dynamic initializer for FlatStorage.
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
    def map(self, arg0: object, arg1: 'Function') -> 'Storage':
        """public <R> dev.ultreon.quantum.collection.Storage<R> dev.ultreon.quantum.collection.FlatStorage.map(R,java.util.function.Function<D, R>)"""
        return 'Storage'.__wrap(super(__FlatStorage, self).map(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: object, arg1: 'short', arg2: 'Short2ReferenceFunction'):
        """public dev.ultreon.quantum.collection.FlatStorage(D,short[],it.unimi.dsi.fastutil.shorts.Short2ReferenceFunction<D>)"""
        val = __FlatStorage(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> object:
        """public D dev.ultreon.quantum.collection.FlatStorage.get(int)"""
        return object.__wrap(super(__FlatStorage, self).get(__int.valueOf(arg0)))

    @overload
    def serialize(self, arg0: 'Reference2ShortFunction') -> List[int]:
        """public short[] dev.ultreon.quantum.collection.FlatStorage.serialize(it.unimi.dsi.fastutil.objects.Reference2ShortFunction<D>)"""
        return List[int].__wrap(super(__FlatStorage, self).serialize(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: object, arg1: 'List'):
        """public dev.ultreon.quantum.collection.FlatStorage(D,java.util.List<D>)"""
        val = __FlatStorage(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def save(self, arg0: 'MapType', arg1: 'Function') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.collection.FlatStorage.save(dev.ultreon.ubo.types.MapType,java.util.function.Function<D, dev.ultreon.ubo.types.MapType>)"""
        return 'types.MapType'.__wrap(super(__FlatStorage, self).save(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def read(self, arg0: 'PacketIO', arg1: 'Function'):
        """public void dev.ultreon.quantum.collection.FlatStorage.read(dev.ultreon.quantum.network.PacketIO,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, D>)"""
        super(__FlatStorage, self).read(arg0, arg1)

    @overload
    def set(self, arg0: int, arg1: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.FlatStorage.set(int,D)"""
        return bool.__wrap(super(__FlatStorage, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def load(self, arg0: 'MapType', arg1: 'Function'):
        """public void dev.ultreon.quantum.collection.FlatStorage.load(dev.ultreon.ubo.types.MapType,java.util.function.Function<dev.ultreon.ubo.types.MapType, D>)"""
        super(__FlatStorage, self).load(arg0, arg1)

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
    def __init__(self, arg0: object, arg1: int):
        """public dev.ultreon.quantum.collection.FlatStorage(D,int)"""
        val = __FlatStorage(arg0, __int.valueOf(arg1))
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

    @overload
    def __init__(self, arg0: object, arg1: 'Object'):
        """public dev.ultreon.quantum.collection.FlatStorage(D,D[])"""
        val = __FlatStorage(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: object, arg1: 'PacketIO', arg2: 'Function'):
        """public dev.ultreon.quantum.collection.FlatStorage(D,dev.ultreon.quantum.network.PacketIO,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, D>)"""
        val = __FlatStorage(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'PacketIO', arg1: 'BiConsumer'):
        """public void dev.ultreon.quantum.collection.FlatStorage.write(dev.ultreon.quantum.network.PacketIO,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, D>)"""
        super(__FlatStorage, self).write(arg0, arg1) 
 
 
# CLASS: dev.ultreon.quantum.collection.OrderedMap
from pyquantum_helper import import_once as __import_once__
import java.util.AbstractMap as __AbstractMap
__AbstractMap = __AbstractMap
from builtins import type
try:
    from pycorelibs.commons.v0 import tuple
except ImportError:
    tuple = __import_once__("pycorelibs.commons.v0.tuple")

import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.collection.OrderedMap as __OrderedMap
__OrderedMap = __OrderedMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import dev.ultreon.libs.commons.v0.tuple.Pair as __Pair
__Pair = __Pair
import java.util.Set as Set
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
import java.util.List as List
 
class OrderedMap(__AbstractMap, AbstractMap):
    """dev.ultreon.quantum.collection.OrderedMap"""
 
    @staticmethod
    def __wrap(java_value: __OrderedMap) -> 'OrderedMap':
        return OrderedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrderedMap):
        """
        Dynamic initializer for OrderedMap.
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
    def keySet(self) -> 'Set':
        """public java.util.Set<K> dev.ultreon.quantum.collection.OrderedMap.keySet()"""
        return 'Set'.__wrap(super(OrderedMap, self).keySet())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void dev.ultreon.quantum.collection.OrderedMap.clear()"""
        super(OrderedMap, self).clear()

    @override
    @overload
    def size(self) -> int:
        """public int dev.ultreon.quantum.collection.OrderedMap.size()"""
        return int.__wrap(super(OrderedMap, self).size())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractMap.toString()"""
        return str.__wrap(super(AbstractMap, self).toString())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.quantum.collection.OrderedMap.put(K,V)"""
        return object.__wrap(super(__OrderedMap, self).put(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMap, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def keyList(self) -> 'List':
        """public java.util.List<K> dev.ultreon.quantum.collection.OrderedMap.keyList()"""
        return 'List'.__wrap(super(OrderedMap, self).keyList())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractMap.hashCode()"""
        return int.__wrap(super(AbstractMap, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int dev.ultreon.quantum.collection.OrderedMap.indexOf(K)"""
        return int.__wrap(super(__OrderedMap, self).indexOf(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V dev.ultreon.quantum.collection.OrderedMap.get(java.lang.Object)"""
        return object.__wrap(super(__OrderedMap, self).get(arg0))

    @overload
    def put(self, arg0: int, arg1: object, arg2: object) -> 'tuple.Pair':
        """public dev.ultreon.libs.commons.v0.tuple.Pair<java.lang.Integer, V> dev.ultreon.quantum.collection.OrderedMap.put(int,K,V)"""
        return 'tuple.Pair'.__wrap(super(__OrderedMap, self).put(__int.valueOf(arg0), arg1, arg2))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V dev.ultreon.quantum.collection.OrderedMap.remove(java.lang.Object)"""
        return object.__wrap(super(__OrderedMap, self).remove(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void dev.ultreon.quantum.collection.OrderedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__OrderedMap, self).putAll(arg0)

    @overload
    def removeEntry(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.collection.OrderedMap.removeEntry(int)"""
        return bool.__wrap(super(__OrderedMap, self).removeEntry(__int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.collection.OrderedMap()"""
        val = __OrderedMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def indexOfValue(self, arg0: object) -> int:
        """public int dev.ultreon.quantum.collection.OrderedMap.indexOfValue(V)"""
        return int.__wrap(super(__OrderedMap, self).indexOfValue(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.collection.OrderedMap()"""
        val = __OrderedMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.OrderedMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__OrderedMap, self).containsValue(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.quantum.collection.OrderedMap.isEmpty()"""
        return bool.__wrap(super(OrderedMap, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.OrderedMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__OrderedMap, self).containsKey(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> dev.ultreon.quantum.collection.OrderedMap.values()"""
        return 'Collection'.__wrap(super(OrderedMap, self).values())

    @overload
    def valueList(self) -> 'List':
        """public java.util.List<V> dev.ultreon.quantum.collection.OrderedMap.valueList()"""
        return 'List'.__wrap(super(OrderedMap, self).valueList())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> dev.ultreon.quantum.collection.OrderedMap.entrySet()"""
        return 'Set'.__wrap(super(OrderedMap, self).entrySet()) 
 
 
# CLASS: dev.ultreon.quantum.collection.Storage
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.util.function.BiConsumer as BiConsumer
import dev.ultreon.quantum.collection.Storage as __Storage
__Storage = __Storage
from abc import abstractmethod, ABC
import java.util.function.Function as Function
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class Storage(ABC):
    """dev.ultreon.quantum.collection.Storage"""
 
    @staticmethod
    def __wrap(java_value: __Storage) -> 'Storage':
        return Storage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Storage):
        """
        Dynamic initializer for Storage.
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
    def get(self, arg0: int):
        """public abstract D dev.ultreon.quantum.collection.Storage.get(int)"""
        pass

    @abstractmethod
    def save(self, arg0: 'MapType', arg1: 'Function'):
        """public abstract dev.ultreon.ubo.types.MapType dev.ultreon.quantum.collection.Storage.save(dev.ultreon.ubo.types.MapType,java.util.function.Function<D, dev.ultreon.ubo.types.MapType>)"""
        pass

    @abstractmethod
    def set(self, arg0: int, arg1: object):
        """public abstract boolean dev.ultreon.quantum.collection.Storage.set(int,D)"""
        pass

    @abstractmethod
    def map(self, arg0: object, arg1: 'Function'):
        """public abstract <R> dev.ultreon.quantum.collection.Storage<R> dev.ultreon.quantum.collection.Storage.map(R,java.util.function.Function<D, R>)"""
        pass

    @abstractmethod
    def read(self, arg0: 'PacketIO', arg1: 'Function'):
        """public abstract void dev.ultreon.quantum.collection.Storage.read(dev.ultreon.quantum.network.PacketIO,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, D>)"""
        pass

    @abstractmethod
    def load(self, arg0: 'MapType', arg1: 'Function'):
        """public abstract void dev.ultreon.quantum.collection.Storage.load(dev.ultreon.ubo.types.MapType,java.util.function.Function<dev.ultreon.ubo.types.MapType, D>)"""
        pass

    @abstractmethod
    def write(self, arg0: 'PacketIO', arg1: 'BiConsumer'):
        """public abstract void dev.ultreon.quantum.collection.Storage.write(dev.ultreon.quantum.network.PacketIO,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, D>)"""
        pass