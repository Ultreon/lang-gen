from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.collection.Storage as _Storage
_Storage = _Storage
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
from typing import List
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import dev.ultreon.quantum.collection.PaletteStorage as _PaletteStorage
_PaletteStorage = _PaletteStorage
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class PaletteStorage():
    """dev.ultreon.quantum.collection.PaletteStorage"""
 
    @staticmethod
    def _wrap(java_value: _PaletteStorage) -> 'PaletteStorage':
        return PaletteStorage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PaletteStorage):
        """
        Dynamic initializer for PaletteStorage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PaletteStorage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PaletteStorage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: object, arg1: int):
        """public dev.ultreon.quantum.collection.PaletteStorage(D,int)"""
        val = _PaletteStorage(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def remove(self, arg0: int):
        """public void dev.ultreon.quantum.collection.PaletteStorage.remove(int)"""
        super(_PaletteStorage, self).remove(_int.valueOf(arg0))

    @overload
    def add(self, arg0: int, arg1: object) -> int:
        """public short dev.ultreon.quantum.collection.PaletteStorage.add(int,D)"""
        return int._wrap(super(_PaletteStorage, self).add(_int.valueOf(arg0), arg1))

    @overload
    def save(self, arg0: 'MapType', arg1: 'Function') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.collection.PaletteStorage.save(dev.ultreon.ubo.types.MapType,java.util.function.Function<D, dev.ultreon.ubo.types.MapType>)"""
        return 'types.MapType'._wrap(super(_PaletteStorage, self).save(arg0, arg1))

    @overload
    def getData(self) -> 'List':
        """public java.util.List<D> dev.ultreon.quantum.collection.PaletteStorage.getData()"""
        return 'List'._wrap(super(PaletteStorage, self).getData())

    @overload
    def toDataIdx(self, arg0: int) -> int:
        """public short dev.ultreon.quantum.collection.PaletteStorage.toDataIdx(int)"""
        return int._wrap(super(_PaletteStorage, self).toDataIdx(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def dispose(self):
        """public void dev.ultreon.quantum.collection.PaletteStorage.dispose()"""
        super(PaletteStorage, self).dispose()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.collection.PaletteStorage.hashCode()"""
        return int._wrap(super(PaletteStorage, self).hashCode())

    @overload
    def set(self, arg0: int, arg1: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.PaletteStorage.set(int,D)"""
        return bool._wrap(super(_PaletteStorage, self).set(_int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.PaletteStorage.equals(java.lang.Object)"""
        return bool._wrap(super(_PaletteStorage, self).equals(arg0))

    @override
    @overload
    def load(self, arg0: 'MapType', arg1: 'Function'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.load(dev.ultreon.ubo.types.MapType,java.util.function.Function<dev.ultreon.ubo.types.MapType, D>)"""
        super(_PaletteStorage, self).load(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def read(self, arg0: 'PacketIO', arg1: 'Function'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.read(dev.ultreon.quantum.network.PacketIO,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, D>)"""
        super(_PaletteStorage, self).read(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def write(self, arg0: 'PacketIO', arg1: 'BiConsumer'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.write(dev.ultreon.quantum.network.PacketIO,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, D>)"""
        super(_PaletteStorage, self).write(arg0, arg1)

    @overload
    def direct(self, arg0: int) -> object:
        """public D dev.ultreon.quantum.collection.PaletteStorage.direct(int)"""
        return object._wrap(super(_PaletteStorage, self).direct(_int.valueOf(arg0)))

    @overload
    def map(self, arg0: object, arg1: 'Function') -> 'Storage':
        """public <R> dev.ultreon.quantum.collection.Storage<R> dev.ultreon.quantum.collection.PaletteStorage.map(R,java.util.function.Function<D, R>)"""
        return 'Storage'._wrap(super(_PaletteStorage, self).map(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: 'short', arg1: 'List'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.set(short[],java.util.List<D>)"""
        super(_PaletteStorage, self).set(arg0, arg1)

    @overload
    def getPalette(self) -> List[int]:
        """public short[] dev.ultreon.quantum.collection.PaletteStorage.getPalette()"""
        return List[int]._wrap(super(PaletteStorage, self).getPalette())

    @overload
    def get(self, arg0: int) -> object:
        """public D dev.ultreon.quantum.collection.PaletteStorage.get(int)"""
        return object._wrap(super(_PaletteStorage, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: object, arg1: 'PacketIO', arg2: 'Function'):
        """public dev.ultreon.quantum.collection.PaletteStorage(D,dev.ultreon.quantum.network.PacketIO,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, D>)"""
        val = _PaletteStorage(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: 'short', arg2: 'List'):
        """public dev.ultreon.quantum.collection.PaletteStorage(D,short[],java.util.List<D>)"""
        val = _PaletteStorage(arg0, arg1, arg2)
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.collection.PaletteStorage
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.collection.Storage as _Storage
_Storage = _Storage
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
from typing import List
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import dev.ultreon.quantum.collection.PaletteStorage as _PaletteStorage
_PaletteStorage = _PaletteStorage
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class PaletteStorage():
    """dev.ultreon.quantum.collection.PaletteStorage"""
 
    @staticmethod
    def _wrap(java_value: _PaletteStorage) -> 'PaletteStorage':
        return PaletteStorage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PaletteStorage):
        """
        Dynamic initializer for PaletteStorage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PaletteStorage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PaletteStorage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: object, arg1: int):
        """public dev.ultreon.quantum.collection.PaletteStorage(D,int)"""
        val = _PaletteStorage(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def remove(self, arg0: int):
        """public void dev.ultreon.quantum.collection.PaletteStorage.remove(int)"""
        super(_PaletteStorage, self).remove(_int.valueOf(arg0))

    @overload
    def add(self, arg0: int, arg1: object) -> int:
        """public short dev.ultreon.quantum.collection.PaletteStorage.add(int,D)"""
        return int._wrap(super(_PaletteStorage, self).add(_int.valueOf(arg0), arg1))

    @overload
    def save(self, arg0: 'MapType', arg1: 'Function') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.collection.PaletteStorage.save(dev.ultreon.ubo.types.MapType,java.util.function.Function<D, dev.ultreon.ubo.types.MapType>)"""
        return 'types.MapType'._wrap(super(_PaletteStorage, self).save(arg0, arg1))

    @overload
    def getData(self) -> 'List':
        """public java.util.List<D> dev.ultreon.quantum.collection.PaletteStorage.getData()"""
        return 'List'._wrap(super(PaletteStorage, self).getData())

    @overload
    def toDataIdx(self, arg0: int) -> int:
        """public short dev.ultreon.quantum.collection.PaletteStorage.toDataIdx(int)"""
        return int._wrap(super(_PaletteStorage, self).toDataIdx(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def dispose(self):
        """public void dev.ultreon.quantum.collection.PaletteStorage.dispose()"""
        super(PaletteStorage, self).dispose()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.collection.PaletteStorage.hashCode()"""
        return int._wrap(super(PaletteStorage, self).hashCode())

    @overload
    def set(self, arg0: int, arg1: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.PaletteStorage.set(int,D)"""
        return bool._wrap(super(_PaletteStorage, self).set(_int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.PaletteStorage.equals(java.lang.Object)"""
        return bool._wrap(super(_PaletteStorage, self).equals(arg0))

    @override
    @overload
    def load(self, arg0: 'MapType', arg1: 'Function'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.load(dev.ultreon.ubo.types.MapType,java.util.function.Function<dev.ultreon.ubo.types.MapType, D>)"""
        super(_PaletteStorage, self).load(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def read(self, arg0: 'PacketIO', arg1: 'Function'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.read(dev.ultreon.quantum.network.PacketIO,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, D>)"""
        super(_PaletteStorage, self).read(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def write(self, arg0: 'PacketIO', arg1: 'BiConsumer'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.write(dev.ultreon.quantum.network.PacketIO,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, D>)"""
        super(_PaletteStorage, self).write(arg0, arg1)

    @overload
    def direct(self, arg0: int) -> object:
        """public D dev.ultreon.quantum.collection.PaletteStorage.direct(int)"""
        return object._wrap(super(_PaletteStorage, self).direct(_int.valueOf(arg0)))

    @overload
    def map(self, arg0: object, arg1: 'Function') -> 'Storage':
        """public <R> dev.ultreon.quantum.collection.Storage<R> dev.ultreon.quantum.collection.PaletteStorage.map(R,java.util.function.Function<D, R>)"""
        return 'Storage'._wrap(super(_PaletteStorage, self).map(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: 'short', arg1: 'List'):
        """public void dev.ultreon.quantum.collection.PaletteStorage.set(short[],java.util.List<D>)"""
        super(_PaletteStorage, self).set(arg0, arg1)

    @overload
    def getPalette(self) -> List[int]:
        """public short[] dev.ultreon.quantum.collection.PaletteStorage.getPalette()"""
        return List[int]._wrap(super(PaletteStorage, self).getPalette())

    @overload
    def get(self, arg0: int) -> object:
        """public D dev.ultreon.quantum.collection.PaletteStorage.get(int)"""
        return object._wrap(super(_PaletteStorage, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: object, arg1: 'PacketIO', arg2: 'Function'):
        """public dev.ultreon.quantum.collection.PaletteStorage(D,dev.ultreon.quantum.network.PacketIO,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, D>)"""
        val = _PaletteStorage(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: 'short', arg2: 'List'):
        """public dev.ultreon.quantum.collection.PaletteStorage(D,short[],java.util.List<D>)"""
        val = _PaletteStorage(arg0, arg1, arg2)
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.collection.PaletteStorage 
 
 
# CLASS: dev.ultreon.quantum.collection.PaletteIndexException
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
import dev.ultreon.quantum.collection.PaletteIndexException as _PaletteIndexException
_PaletteIndexException = _PaletteIndexException
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
 
class PaletteIndexException():
    """dev.ultreon.quantum.collection.PaletteIndexException"""
 
    @staticmethod
    def _wrap(java_value: _PaletteIndexException) -> 'PaletteIndexException':
        return PaletteIndexException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PaletteIndexException):
        """
        Dynamic initializer for PaletteIndexException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PaletteIndexException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PaletteIndexException__wrapper":
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.collection.PaletteIndexException(java.lang.String)"""
        val = _PaletteIndexException(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.collection.PaletteIndexException()"""
        val = _PaletteIndexException()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.collection.PaletteIndexException()"""
        val = _PaletteIndexException()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.collection.PaletteIndexException(java.lang.String,java.lang.Throwable)"""
        val = _PaletteIndexException(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.collection.PaletteIndexException(java.lang.Throwable)"""
        val = _PaletteIndexException(arg0)
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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.collection.FlatStorage
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.collection.Storage as _Storage
_Storage = _Storage
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import dev.ultreon.quantum.collection.FlatStorage as _FlatStorage
_FlatStorage = _FlatStorage
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import it.unimi.dsi.fastutil.shorts.Short2ReferenceFunction as Short2ReferenceFunction
import java.util.function.Function as Function
from builtins import bool
import it.unimi.dsi.fastutil.objects.Reference2ShortFunction as Reference2ShortFunction
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
 
class FlatStorage():
    """dev.ultreon.quantum.collection.FlatStorage"""
 
    @staticmethod
    def _wrap(java_value: _FlatStorage) -> 'FlatStorage':
        return FlatStorage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FlatStorage):
        """
        Dynamic initializer for FlatStorage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FlatStorage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FlatStorage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: int, arg1: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.FlatStorage.set(int,D)"""
        return bool._wrap(super(_FlatStorage, self).set(_int.valueOf(arg0), arg1))

    @override
    @overload
    def read(self, arg0: 'PacketIO', arg1: 'Function'):
        """public void dev.ultreon.quantum.collection.FlatStorage.read(dev.ultreon.quantum.network.PacketIO,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, D>)"""
        super(_FlatStorage, self).read(arg0, arg1)

    @overload
    def __init__(self, arg0: object, arg1: 'List'):
        """public dev.ultreon.quantum.collection.FlatStorage(D,java.util.List<D>)"""
        val = _FlatStorage(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: 'short', arg2: 'Short2ReferenceFunction'):
        """public dev.ultreon.quantum.collection.FlatStorage(D,short[],it.unimi.dsi.fastutil.shorts.Short2ReferenceFunction<D>)"""
        val = _FlatStorage(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object, arg1: 'PacketIO', arg2: 'Function'):
        """public dev.ultreon.quantum.collection.FlatStorage(D,dev.ultreon.quantum.network.PacketIO,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, D>)"""
        val = _FlatStorage(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def serialize(self, arg0: 'Reference2ShortFunction') -> List[int]:
        """public short[] dev.ultreon.quantum.collection.FlatStorage.serialize(it.unimi.dsi.fastutil.objects.Reference2ShortFunction<D>)"""
        return List[int]._wrap(super(_FlatStorage, self).serialize(arg0))

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
    def save(self, arg0: 'MapType', arg1: 'Function') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.collection.FlatStorage.save(dev.ultreon.ubo.types.MapType,java.util.function.Function<D, dev.ultreon.ubo.types.MapType>)"""
        return 'types.MapType'._wrap(super(_FlatStorage, self).save(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def load(self, arg0: 'MapType', arg1: 'Function'):
        """public void dev.ultreon.quantum.collection.FlatStorage.load(dev.ultreon.ubo.types.MapType,java.util.function.Function<dev.ultreon.ubo.types.MapType, D>)"""
        super(_FlatStorage, self).load(arg0, arg1)

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
    def __init__(self, arg0: object, arg1: 'Object'):
        """public dev.ultreon.quantum.collection.FlatStorage(D,D[])"""
        val = _FlatStorage(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: object, arg1: int):
        """public dev.ultreon.quantum.collection.FlatStorage(D,int)"""
        val = _FlatStorage(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> object:
        """public D dev.ultreon.quantum.collection.FlatStorage.get(int)"""
        return object._wrap(super(_FlatStorage, self).get(_int.valueOf(arg0)))

    @overload
    def map(self, arg0: object, arg1: 'Function') -> 'Storage':
        """public <R> dev.ultreon.quantum.collection.Storage<R> dev.ultreon.quantum.collection.FlatStorage.map(R,java.util.function.Function<D, R>)"""
        return 'Storage'._wrap(super(_FlatStorage, self).map(arg0, arg1))

    @override
    @overload
    def write(self, arg0: 'PacketIO', arg1: 'BiConsumer'):
        """public void dev.ultreon.quantum.collection.FlatStorage.write(dev.ultreon.quantum.network.PacketIO,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, D>)"""
        super(_FlatStorage, self).write(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.collection.OrderedMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pycorelibs.commons.v0 import tuple
except ImportError:
    tuple = _import_once("pycorelibs.commons.v0.tuple")

import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import dev.ultreon.quantum.collection.OrderedMap as _OrderedMap
_OrderedMap = _OrderedMap
import java.util.Set as _Set
_Set = _Set
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.util.AbstractMap as _AbstractMap
_AbstractMap = _AbstractMap
from builtins import object
import dev.ultreon.libs.commons.v0.tuple.Pair as _Pair
_Pair = _Pair
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.function.BiFunction as BiFunction
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class OrderedMap():
    """dev.ultreon.quantum.collection.OrderedMap"""
 
    @staticmethod
    def _wrap(java_value: _OrderedMap) -> 'OrderedMap':
        return OrderedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OrderedMap):
        """
        Dynamic initializer for OrderedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OrderedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OrderedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def valueList(self) -> 'List':
        """public java.util.List<V> dev.ultreon.quantum.collection.OrderedMap.valueList()"""
        return 'List'._wrap(super(OrderedMap, self).valueList())

    @overload
    def get(self, arg0: object) -> object:
        """public V dev.ultreon.quantum.collection.OrderedMap.get(java.lang.Object)"""
        return object._wrap(super(_OrderedMap, self).get(arg0))

    @override
    @overload
    def clear(self):
        """public void dev.ultreon.quantum.collection.OrderedMap.clear()"""
        super(OrderedMap, self).clear()

    @overload
    def remove(self, arg0: object) -> object:
        """public V dev.ultreon.quantum.collection.OrderedMap.remove(java.lang.Object)"""
        return object._wrap(super(_OrderedMap, self).remove(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int dev.ultreon.quantum.collection.OrderedMap.indexOf(K)"""
        return int._wrap(super(_OrderedMap, self).indexOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.collection.OrderedMap()"""
        val = _OrderedMap()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def keyList(self) -> 'List':
        """public java.util.List<K> dev.ultreon.quantum.collection.OrderedMap.keyList()"""
        return 'List'._wrap(super(OrderedMap, self).keyList())

    @overload
    def indexOfValue(self, arg0: object) -> int:
        """public int dev.ultreon.quantum.collection.OrderedMap.indexOfValue(V)"""
        return int._wrap(super(_OrderedMap, self).indexOfValue(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void dev.ultreon.quantum.collection.OrderedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_OrderedMap, self).putAll(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractMap.toString()"""
        return str._wrap(super(AbstractMap, self).toString())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.OrderedMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_OrderedMap, self).containsKey(arg0))

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
    def containsValue(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.collection.OrderedMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_OrderedMap, self).containsValue(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.collection.OrderedMap()"""
        val = _OrderedMap()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMap, self).equals(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> dev.ultreon.quantum.collection.OrderedMap.entrySet()"""
        return 'Set'._wrap(super(OrderedMap, self).entrySet())

    @overload
    def removeEntry(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.collection.OrderedMap.removeEntry(int)"""
        return bool._wrap(super(_OrderedMap, self).removeEntry(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: int, arg1: object, arg2: object) -> 'tuple.Pair':
        """public dev.ultreon.libs.commons.v0.tuple.Pair<java.lang.Integer, V> dev.ultreon.quantum.collection.OrderedMap.put(int,K,V)"""
        return 'tuple.Pair'._wrap(super(_OrderedMap, self).put(_int.valueOf(arg0), arg1, arg2))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int dev.ultreon.quantum.collection.OrderedMap.size()"""
        return int._wrap(super(OrderedMap, self).size())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.quantum.collection.OrderedMap.put(K,V)"""
        return object._wrap(super(_OrderedMap, self).put(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> dev.ultreon.quantum.collection.OrderedMap.values()"""
        return 'Collection'._wrap(super(OrderedMap, self).values())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> dev.ultreon.quantum.collection.OrderedMap.keySet()"""
        return 'Set'._wrap(super(OrderedMap, self).keySet())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.quantum.collection.OrderedMap.isEmpty()"""
        return bool._wrap(super(OrderedMap, self).isEmpty())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractMap.hashCode()"""
        return int._wrap(super(AbstractMap, self).hashCode())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: dev.ultreon.quantum.collection.Storage
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.util.function.BiConsumer as BiConsumer
import dev.ultreon.quantum.collection.Storage as _Storage
_Storage = _Storage
from abc import abstractmethod, ABC
import java.util.function.Function as Function
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

 
class Storage():
    """dev.ultreon.quantum.collection.Storage"""
 
    @staticmethod
    def _wrap(java_value: _Storage) -> 'Storage':
        return Storage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Storage):
        """
        Dynamic initializer for Storage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Storage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Storage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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