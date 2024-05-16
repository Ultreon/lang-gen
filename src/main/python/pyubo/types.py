from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

import java.lang.Float as Float
import dev.ultreon.ubo.types.FloatType as __FloatType
__FloatType = __FloatType
from builtins import object
import java.io.DataInput as DataInput
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FloatType(__DataType, DataType):
    """dev.ultreon.ubo.types.FloatType"""
 
    @staticmethod
    def __wrap(java_value: __FloatType) -> 'FloatType':
        return FloatType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatType):
        """
        Dynamic initializer for FloatType.
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
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.FloatType.writeUso()"""
        return str.__wrap(super(FloatType, self).writeUso())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'FloatType':
        """public static dev.ultreon.ubo.types.FloatType dev.ultreon.ubo.types.FloatType.read(java.io.DataInput) throws java.io.IOException"""
        return FloatType.__wrap(__FloatType.read(arg0))

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

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

    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.ubo.types.FloatType(float)"""
        val = __FloatType(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.FloatType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__FloatType, self).write(arg0)

    @overload
    def setValue(self, arg0: 'Float'):
        """public void dev.ultreon.ubo.types.FloatType.setValue(java.lang.Float)"""
        super(__FloatType, self).setValue(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.FloatType.equals(java.lang.Object)"""
        return bool.__wrap(super(__FloatType, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.FloatType.id()"""
        return int.__wrap(super(FloatType, self).id())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.FloatType.toString()"""
        return str.__wrap(super(FloatType, self).toString())

    @override
    @overload
    def getValue(self) -> 'Float':
        """public java.lang.Float dev.ultreon.ubo.types.FloatType.getValue()"""
        return __transform(super(FloatType, self).getValue()).'Float'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.FloatType.hashCode()"""
        return int.__wrap(super(FloatType, self).hashCode())

    @override
    @overload
    def copy(self) -> 'FloatType':
        """public dev.ultreon.ubo.types.FloatType dev.ultreon.ubo.types.FloatType.copy()"""
        return 'FloatType'.__wrap(super(FloatType, self).copy())

 
 
 
# CLASS: dev.ultreon.ubo.types.FloatType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

import java.lang.Float as Float
import dev.ultreon.ubo.types.FloatType as __FloatType
__FloatType = __FloatType
from builtins import object
import java.io.DataInput as DataInput
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FloatType(__DataType, DataType):
    """dev.ultreon.ubo.types.FloatType"""
 
    @staticmethod
    def __wrap(java_value: __FloatType) -> 'FloatType':
        return FloatType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatType):
        """
        Dynamic initializer for FloatType.
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
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.FloatType.writeUso()"""
        return str.__wrap(super(FloatType, self).writeUso())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'FloatType':
        """public static dev.ultreon.ubo.types.FloatType dev.ultreon.ubo.types.FloatType.read(java.io.DataInput) throws java.io.IOException"""
        return FloatType.__wrap(__FloatType.read(arg0))

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

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

    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.ubo.types.FloatType(float)"""
        val = __FloatType(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.FloatType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__FloatType, self).write(arg0)

    @overload
    def setValue(self, arg0: 'Float'):
        """public void dev.ultreon.ubo.types.FloatType.setValue(java.lang.Float)"""
        super(__FloatType, self).setValue(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.FloatType.equals(java.lang.Object)"""
        return bool.__wrap(super(__FloatType, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.FloatType.id()"""
        return int.__wrap(super(FloatType, self).id())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.FloatType.toString()"""
        return str.__wrap(super(FloatType, self).toString())

    @override
    @overload
    def getValue(self) -> 'Float':
        """public java.lang.Float dev.ultreon.ubo.types.FloatType.getValue()"""
        return __transform(super(FloatType, self).getValue()).'Float'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.FloatType.hashCode()"""
        return int.__wrap(super(FloatType, self).hashCode())

    @override
    @overload
    def copy(self) -> 'FloatType':
        """public dev.ultreon.ubo.types.FloatType dev.ultreon.ubo.types.FloatType.copy()"""
        return 'FloatType'.__wrap(super(FloatType, self).copy())

 
 
 
# CLASS: dev.ultreon.ubo.types.FloatType 
 
 
# CLASS: dev.ultreon.ubo.types.MapType
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
import java.lang.Character as __char
from pyquantum_helper import transform as __transform
import java.lang.Boolean as __boolean
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.BitSet as BitSet
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
import java.lang.Double as __double
from builtins import bool
import java.util.BitSet as __BitSet
__BitSet = __BitSet
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import float
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.ListType as __ListType
__ListType = __ListType
from typing import List
import java.lang.Long as __long
import java.util.Set as Set
import java.math.BigInteger as BigInteger
import java.lang.Float as __float
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.Object as __Object
__Object = __Object
import java.math.BigDecimal as BigDecimal
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class MapType(__DataType, DataType):
    """dev.ultreon.ubo.types.MapType"""
 
    @staticmethod
    def __wrap(java_value: __MapType) -> 'MapType':
        return MapType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapType):
        """
        Dynamic initializer for MapType.
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
    def __init__(self, ):
        """public dev.ultreon.ubo.types.MapType()"""
        val = __MapType()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMap(self, arg0: str, arg1: 'MapType') -> 'MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.ubo.types.MapType.getMap(java.lang.String,dev.ultreon.ubo.types.MapType)"""
        return 'MapType'.__wrap(super(__MapType, self).getMap(arg0, arg1))

    @overload
    def putBigDec(self, arg0: str, arg1: 'BigDecimal'):
        """public void dev.ultreon.ubo.types.MapType.putBigDec(java.lang.String,java.math.BigDecimal)"""
        super(__MapType, self).putBigDec(arg0, arg1)

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.MapType.id()"""
        return int.__wrap(super(MapType, self).id())

    @overload
    def getShort(self, arg0: str) -> int:
        """public short dev.ultreon.ubo.types.MapType.getShort(java.lang.String)"""
        return int.__wrap(super(__MapType, self).getShort(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getCharArray(self, arg0: str) -> List[str]:
        """public char[] dev.ultreon.ubo.types.MapType.getCharArray(java.lang.String)"""
        return List[str].__wrap(super(__MapType, self).getCharArray(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.ubo.types.MapType()"""
        val = __MapType()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getDouble(self, arg0: str, arg1: float) -> float:
        """public double dev.ultreon.ubo.types.MapType.getDouble(java.lang.String,double)"""
        return float.__wrap(super(__MapType, self).getDouble(arg0, __double.valueOf(arg1)))

    @overload
    def getShortArray(self, arg0: str) -> List[int]:
        """public short[] dev.ultreon.ubo.types.MapType.getShortArray(java.lang.String)"""
        return List[int].__wrap(super(__MapType, self).getShortArray(arg0))

    @overload
    def putByte(self, arg0: str, arg1: int):
        """public void dev.ultreon.ubo.types.MapType.putByte(java.lang.String,byte)"""
        super(__MapType, self).putByte(arg0, __byte.valueOf(arg1))

    @overload
    def getByteArray(self, arg0: str, arg1: bytes) -> List[int]:
        """public byte[] dev.ultreon.ubo.types.MapType.getByteArray(java.lang.String,byte[])"""
        return List[int].__wrap(super(__MapType, self).getByteArray(arg0, bytes))

    @overload
    def getBoolean(self, arg0: str) -> bool:
        """public boolean dev.ultreon.ubo.types.MapType.getBoolean(java.lang.String)"""
        return bool.__wrap(super(__MapType, self).getBoolean(arg0))

    @overload
    def getFloatArray(self, arg0: str) -> List[float]:
        """public float[] dev.ultreon.ubo.types.MapType.getFloatArray(java.lang.String)"""
        return List[float].__wrap(super(__MapType, self).getFloatArray(arg0))

    @overload
    def getIntArray(self, arg0: str, arg1: 'int') -> List[int]:
        """public int[] dev.ultreon.ubo.types.MapType.getIntArray(java.lang.String,int[])"""
        return List[int].__wrap(super(__MapType, self).getIntArray(arg0, arg1))

    @overload
    def getDoubleArray(self, arg0: str) -> List[float]:
        """public double[] dev.ultreon.ubo.types.MapType.getDoubleArray(java.lang.String)"""
        return List[float].__wrap(super(__MapType, self).getDoubleArray(arg0))

    @overload
    def getDoubleArray(self, arg0: str, arg1: 'double') -> List[float]:
        """public double[] dev.ultreon.ubo.types.MapType.getDoubleArray(java.lang.String,double[])"""
        return List[float].__wrap(super(__MapType, self).getDoubleArray(arg0, arg1))

    @overload
    def putShort(self, arg0: str, arg1: int):
        """public void dev.ultreon.ubo.types.MapType.putShort(java.lang.String,int)"""
        super(__MapType, self).putShort(arg0, __int.valueOf(arg1))

    @overload
    def putDoubleArray(self, arg0: str, arg1: 'double'):
        """public void dev.ultreon.ubo.types.MapType.putDoubleArray(java.lang.String,double[])"""
        super(__MapType, self).putDoubleArray(arg0, arg1)

    @overload
    def getBigInt(self, arg0: str, arg1: 'BigInteger') -> 'BigInteger':
        """public java.math.BigInteger dev.ultreon.ubo.types.MapType.getBigInt(java.lang.String,java.math.BigInteger)"""
        return __transform(super(__MapType, self).getBigInt(arg0, arg1)).'BigInteger'Value()

    @overload
    def putIntArray(self, arg0: str, arg1: 'int'):
        """public void dev.ultreon.ubo.types.MapType.putIntArray(java.lang.String,int[])"""
        super(__MapType, self).putIntArray(arg0, arg1)

    @overload
    def getBigDec(self, arg0: str, arg1: 'BigDecimal') -> 'BigDecimal':
        """public java.math.BigDecimal dev.ultreon.ubo.types.MapType.getBigDec(java.lang.String,java.math.BigDecimal)"""
        return __transform(super(__MapType, self).getBigDec(arg0, arg1)).'BigDecimal'Value()

    @overload
    def getBigDec(self, arg0: str) -> 'BigDecimal':
        """public java.math.BigDecimal dev.ultreon.ubo.types.MapType.getBigDec(java.lang.String)"""
        return __transform(super(__MapType, self).getBigDec(arg0)).'BigDecimal'Value()

    @overload
    def pop(self, arg0: str) -> 'DataType':
        """public dev.ultreon.ubo.types.DataType<?> dev.ultreon.ubo.types.MapType.pop(java.lang.String)"""
        return 'DataType'.__wrap(super(__MapType, self).pop(arg0))

    @overload
    def putByteArray(self, arg0: str, arg1: bytes):
        """public void dev.ultreon.ubo.types.MapType.putByteArray(java.lang.String,byte[])"""
        super(__MapType, self).putByteArray(arg0, bytes)

    @overload
    def getByteArray(self, arg0: str) -> List[int]:
        """public byte[] dev.ultreon.ubo.types.MapType.getByteArray(java.lang.String)"""
        return List[int].__wrap(super(__MapType, self).getByteArray(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def putFloat(self, arg0: str, arg1: float):
        """public void dev.ultreon.ubo.types.MapType.putFloat(java.lang.String,float)"""
        super(__MapType, self).putFloat(arg0, __float.valueOf(arg1))

    @overload
    def putLongArray(self, arg0: str, arg1: 'long'):
        """public void dev.ultreon.ubo.types.MapType.putLongArray(java.lang.String,long[])"""
        super(__MapType, self).putLongArray(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def putBoolean(self, arg0: str, arg1: bool):
        """public void dev.ultreon.ubo.types.MapType.putBoolean(java.lang.String,boolean)"""
        super(__MapType, self).putBoolean(arg0, __boolean.valueOf(arg1))

    @overload
    def putBigInt(self, arg0: str, arg1: 'BigInteger'):
        """public void dev.ultreon.ubo.types.MapType.putBigInt(java.lang.String,java.math.BigInteger)"""
        super(__MapType, self).putBigInt(arg0, arg1)

    @overload
    def putUUID(self, arg0: str, arg1: 'UUID'):
        """public void dev.ultreon.ubo.types.MapType.putUUID(java.lang.String,java.util.UUID)"""
        super(__MapType, self).putUUID(arg0, arg1)

    @overload
    def putChar(self, arg0: str, arg1: str):
        """public void dev.ultreon.ubo.types.MapType.putChar(java.lang.String,char)"""
        super(__MapType, self).putChar(arg0, __char.valueOf(arg1))

    @overload
    def putShort(self, arg0: str, arg1: int):
        """public void dev.ultreon.ubo.types.MapType.putShort(java.lang.String,short)"""
        super(__MapType, self).putShort(arg0, __short.valueOf(arg1))

    @overload
    def putDouble(self, arg0: str, arg1: float):
        """public void dev.ultreon.ubo.types.MapType.putDouble(java.lang.String,double)"""
        super(__MapType, self).putDouble(arg0, __double.valueOf(arg1))

    @overload
    def keys(self) -> 'Set':
        """public java.util.Set<java.lang.String> dev.ultreon.ubo.types.MapType.keys()"""
        return 'Set'.__wrap(super(MapType, self).keys())

    @overload
    def __init__(self, arg0: 'Map'):
        """public dev.ultreon.ubo.types.MapType(java.util.Map<java.lang.String, dev.ultreon.ubo.types.DataType<?>>)"""
        val = __MapType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getLong(self, arg0: str) -> int:
        """public long dev.ultreon.ubo.types.MapType.getLong(java.lang.String)"""
        return int.__wrap(super(__MapType, self).getLong(arg0))

    @overload
    def getBigInt(self, arg0: str) -> 'BigInteger':
        """public java.math.BigInteger dev.ultreon.ubo.types.MapType.getBigInt(java.lang.String)"""
        return __transform(super(__MapType, self).getBigInt(arg0)).'BigInteger'Value()

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'MapType':
        """public static dev.ultreon.ubo.types.MapType dev.ultreon.ubo.types.MapType.read(java.io.DataInput) throws java.io.IOException"""
        return MapType.__wrap(__MapType.read(arg0))

    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.ubo.types.MapType.isEmpty()"""
        return bool.__wrap(super(MapType, self).isEmpty())

    @overload
    def getMap(self, arg0: str) -> 'MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.ubo.types.MapType.getMap(java.lang.String)"""
        return 'MapType'.__wrap(super(__MapType, self).getMap(arg0))

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.MapType.size()"""
        return int.__wrap(super(MapType, self).size())

    @overload
    def getCharArray(self, arg0: str, arg1: 'char') -> List[str]:
        """public char[] dev.ultreon.ubo.types.MapType.getCharArray(java.lang.String,char[])"""
        return List[str].__wrap(super(__MapType, self).getCharArray(arg0, arg1))

    @overload
    def getShortArray(self, arg0: str, arg1: 'short') -> List[int]:
        """public short[] dev.ultreon.ubo.types.MapType.getShortArray(java.lang.String,short[])"""
        return List[int].__wrap(super(__MapType, self).getShortArray(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getLong(self, arg0: str, arg1: int) -> int:
        """public long dev.ultreon.ubo.types.MapType.getLong(java.lang.String,long)"""
        return int.__wrap(super(__MapType, self).getLong(arg0, __long.valueOf(arg1)))

    @overload
    def putLong(self, arg0: str, arg1: int):
        """public void dev.ultreon.ubo.types.MapType.putLong(java.lang.String,long)"""
        super(__MapType, self).putLong(arg0, __long.valueOf(arg1))

    @overload
    def contains(self, arg0: str, *arg1: 'DataType') -> bool:
        """public final <T extends dev.ultreon.ubo.types.DataType<?>> boolean dev.ultreon.ubo.types.MapType.contains(java.lang.String,T...)"""
        return bool.__wrap(super(__MapType, self).contains(arg0, arg1))

    @overload
    def getByte(self, arg0: str) -> int:
        """public byte dev.ultreon.ubo.types.MapType.getByte(java.lang.String)"""
        return int.__wrap(super(__MapType, self).getByte(arg0))

    @overload
    def contains(self, arg0: str, arg1: int) -> bool:
        """public boolean dev.ultreon.ubo.types.MapType.contains(java.lang.String,int)"""
        return bool.__wrap(super(__MapType, self).contains(arg0, __int.valueOf(arg1)))

    @overload
    def getUUID(self, arg0: str, arg1: 'UUID') -> 'UUID':
        """public java.util.UUID dev.ultreon.ubo.types.MapType.getUUID(java.lang.String,java.util.UUID)"""
        return 'UUID'.__wrap(super(__MapType, self).getUUID(arg0, arg1))

    @overload
    def put(self, arg0: str, arg1: 'DataType'):
        """public void dev.ultreon.ubo.types.MapType.put(java.lang.String,dev.ultreon.ubo.types.DataType<?>)"""
        super(__MapType, self).put(arg0, arg1)

    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.types.MapType.values()"""
        return 'Collection'.__wrap(super(MapType, self).values())

    @overload
    def getIntArray(self, arg0: str) -> List[int]:
        """public int[] dev.ultreon.ubo.types.MapType.getIntArray(java.lang.String)"""
        return List[int].__wrap(super(__MapType, self).getIntArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.MapType.toString()"""
        return str.__wrap(super(MapType, self).toString())

    @overload
    def getInt(self, arg0: str) -> int:
        """public int dev.ultreon.ubo.types.MapType.getInt(java.lang.String)"""
        return int.__wrap(super(__MapType, self).getInt(arg0))

    @overload
    def getFloat(self, arg0: str) -> float:
        """public float dev.ultreon.ubo.types.MapType.getFloat(java.lang.String)"""
        return float.__wrap(super(__MapType, self).getFloat(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.MapType.hashCode()"""
        return int.__wrap(super(MapType, self).hashCode())

    @overload
    def getString(self, arg0: str) -> str:
        """public java.lang.String dev.ultreon.ubo.types.MapType.getString(java.lang.String)"""
        return str.__wrap(super(__MapType, self).getString(arg0))

    @overload
    def remove(self, arg0: str) -> bool:
        """public boolean dev.ultreon.ubo.types.MapType.remove(java.lang.String)"""
        return bool.__wrap(super(__MapType, self).remove(arg0))

    @overload
    def getShort(self, arg0: str, arg1: int) -> int:
        """public short dev.ultreon.ubo.types.MapType.getShort(java.lang.String,short)"""
        return int.__wrap(super(__MapType, self).getShort(arg0, __short.valueOf(arg1)))

    @overload
    def setValue(self, arg0: 'Map'):
        """public void dev.ultreon.ubo.types.MapType.setValue(java.util.Map<java.lang.String, dev.ultreon.ubo.types.DataType<?>>)"""
        super(__MapType, self).setValue(arg0)

    @overload
    def getUUID(self, arg0: str) -> 'UUID':
        """public java.util.UUID dev.ultreon.ubo.types.MapType.getUUID(java.lang.String)"""
        return 'UUID'.__wrap(super(__MapType, self).getUUID(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def putString(self, arg0: str, arg1: str):
        """public void dev.ultreon.ubo.types.MapType.putString(java.lang.String,java.lang.String)"""
        super(__MapType, self).putString(arg0, arg1)

    @overload
    def putBitSet(self, arg0: str, arg1: 'BitSet'):
        """public void dev.ultreon.ubo.types.MapType.putBitSet(java.lang.String,java.util.BitSet)"""
        super(__MapType, self).putBitSet(arg0, arg1)

    @overload
    def getChar(self, arg0: str) -> str:
        """public char dev.ultreon.ubo.types.MapType.getChar(java.lang.String)"""
        return str.__wrap(super(__MapType, self).getChar(arg0))

    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<java.lang.String, dev.ultreon.ubo.types.DataType<?>>> dev.ultreon.ubo.types.MapType.entries()"""
        return 'Set'.__wrap(super(MapType, self).entries())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @overload
    def getFloatArray(self, arg0: str, arg1: 'float') -> List[float]:
        """public float[] dev.ultreon.ubo.types.MapType.getFloatArray(java.lang.String,float[])"""
        return List[float].__wrap(super(__MapType, self).getFloatArray(arg0, arg1))

    @overload
    def getBitSet(self, arg0: str) -> 'BitSet':
        """public java.util.BitSet dev.ultreon.ubo.types.MapType.getBitSet(java.lang.String)"""
        return 'BitSet'.__wrap(super(__MapType, self).getBitSet(arg0))

    @overload
    def putByte(self, arg0: str, arg1: int):
        """public void dev.ultreon.ubo.types.MapType.putByte(java.lang.String,int)"""
        super(__MapType, self).putByte(arg0, __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.MapType.equals(java.lang.Object)"""
        return bool.__wrap(super(__MapType, self).equals(arg0))

    @overload
    def getChar(self, arg0: str, arg1: str) -> str:
        """public char dev.ultreon.ubo.types.MapType.getChar(java.lang.String,char)"""
        return str.__wrap(super(__MapType, self).getChar(arg0, __char.valueOf(arg1)))

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.MapType.writeUso()"""
        return str.__wrap(super(MapType, self).writeUso())

    @overload
    def getList(self, arg0: str, *arg1: 'DataType') -> 'ListType':
        """public final <T extends dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.types.ListType<T> dev.ultreon.ubo.types.MapType.getList(java.lang.String,T...)"""
        return 'ListType'.__wrap(super(__MapType, self).getList(arg0, arg1))

    @overload
    def getLongArray(self, arg0: str) -> List[int]:
        """public long[] dev.ultreon.ubo.types.MapType.getLongArray(java.lang.String)"""
        return List[int].__wrap(super(__MapType, self).getLongArray(arg0))

    @overload
    def getBitSet(self, arg0: str, arg1: 'BitSet') -> 'BitSet':
        """public java.util.BitSet dev.ultreon.ubo.types.MapType.getBitSet(java.lang.String,java.util.BitSet)"""
        return 'BitSet'.__wrap(super(__MapType, self).getBitSet(arg0, arg1))

    @overload
    def getLongArray(self, arg0: str, arg1: 'long') -> List[int]:
        """public long[] dev.ultreon.ubo.types.MapType.getLongArray(java.lang.String,long[])"""
        return List[int].__wrap(super(__MapType, self).getLongArray(arg0, arg1))

    @overload
    def putCharArray(self, arg0: str, arg1: 'char'):
        """public void dev.ultreon.ubo.types.MapType.putCharArray(java.lang.String,char[])"""
        super(__MapType, self).putCharArray(arg0, arg1)

    @overload
    def getByte(self, arg0: str, arg1: int) -> int:
        """public byte dev.ultreon.ubo.types.MapType.getByte(java.lang.String,byte)"""
        return int.__wrap(super(__MapType, self).getByte(arg0, __byte.valueOf(arg1)))

    @override
    @overload
    def copy(self) -> 'MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.ubo.types.MapType.copy()"""
        return 'MapType'.__wrap(super(MapType, self).copy())

    @overload
    def __init__(self, arg0: str, arg1: 'DataType'):
        """public dev.ultreon.ubo.types.MapType(java.lang.String,dev.ultreon.ubo.types.DataType<?>)"""
        val = __MapType(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getInt(self, arg0: str, arg1: int) -> int:
        """public int dev.ultreon.ubo.types.MapType.getInt(java.lang.String,int)"""
        return int.__wrap(super(__MapType, self).getInt(arg0, __int.valueOf(arg1)))

    @overload
    def get(self, arg0: str) -> 'DataType':
        """public dev.ultreon.ubo.types.DataType<?> dev.ultreon.ubo.types.MapType.get(java.lang.String)"""
        return 'DataType'.__wrap(super(__MapType, self).get(arg0))

    @overload
    def getString(self, arg0: str, arg1: str) -> str:
        """public java.lang.String dev.ultreon.ubo.types.MapType.getString(java.lang.String,java.lang.String)"""
        return str.__wrap(super(__MapType, self).getString(arg0, arg1))

    @overload
    def clear(self):
        """public void dev.ultreon.ubo.types.MapType.clear()"""
        super(MapType, self).clear()

    @overload
    def getBoolean(self, arg0: str, arg1: bool) -> bool:
        """public boolean dev.ultreon.ubo.types.MapType.getBoolean(java.lang.String,boolean)"""
        return bool.__wrap(super(__MapType, self).getBoolean(arg0, __boolean.valueOf(arg1)))

    @overload
    def getList(self, arg0: str, arg1: 'ListType') -> 'ListType':
        """public <T extends dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.types.ListType<T> dev.ultreon.ubo.types.MapType.getList(java.lang.String,dev.ultreon.ubo.types.ListType<T>)"""
        return 'ListType'.__wrap(super(__MapType, self).getList(arg0, arg1))

    @overload
    def putBitSet(self, arg0: str, arg1: bytes):
        """public void dev.ultreon.ubo.types.MapType.putBitSet(java.lang.String,byte[])"""
        super(__MapType, self).putBitSet(arg0, bytes)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getDouble(self, arg0: str) -> float:
        """public double dev.ultreon.ubo.types.MapType.getDouble(java.lang.String)"""
        return float.__wrap(super(__MapType, self).getDouble(arg0))

    @overload
    def getFloat(self, arg0: str, arg1: float) -> float:
        """public float dev.ultreon.ubo.types.MapType.getFloat(java.lang.String,float)"""
        return float.__wrap(super(__MapType, self).getFloat(arg0, __float.valueOf(arg1)))

    @overload
    def putShortArray(self, arg0: str, arg1: 'short'):
        """public void dev.ultreon.ubo.types.MapType.putShortArray(java.lang.String,short[])"""
        super(__MapType, self).putShortArray(arg0, arg1)

    @overload
    def putInt(self, arg0: str, arg1: int):
        """public void dev.ultreon.ubo.types.MapType.putInt(java.lang.String,int)"""
        super(__MapType, self).putInt(arg0, __int.valueOf(arg1))

    @overload
    def putFloatArray(self, arg0: str, arg1: 'float'):
        """public void dev.ultreon.ubo.types.MapType.putFloatArray(java.lang.String,float[])"""
        super(__MapType, self).putFloatArray(arg0, arg1)

    @override
    @overload
    def getValue(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.types.MapType.getValue()"""
        return 'Map'.__wrap(super(MapType, self).getValue())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.MapType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__MapType, self).write(arg0) 
 
 
# CLASS: dev.ultreon.ubo.types.DoubleType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

import dev.ultreon.ubo.types.DoubleType as __DoubleType
__DoubleType = __DoubleType
from builtins import object
import java.io.DataInput as DataInput
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
import java.lang.Double as Double
from builtins import int
 
class DoubleType(__DataType, DataType):
    """dev.ultreon.ubo.types.DoubleType"""
 
    @staticmethod
    def __wrap(java_value: __DoubleType) -> 'DoubleType':
        return DoubleType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DoubleType):
        """
        Dynamic initializer for DoubleType.
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
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.DoubleType.writeUso()"""
        return str.__wrap(super(DoubleType, self).writeUso())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @override
    @overload
    def getValue(self) -> 'Double':
        """public java.lang.Double dev.ultreon.ubo.types.DoubleType.getValue()"""
        return __transform(super(DoubleType, self).getValue()).'Double'Value()

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

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'DoubleType':
        """public static dev.ultreon.ubo.types.DoubleType dev.ultreon.ubo.types.DoubleType.read(java.io.DataInput) throws java.io.IOException"""
        return DoubleType.__wrap(__DoubleType.read(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.DoubleType.hashCode()"""
        return int.__wrap(super(DoubleType, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.DoubleType.equals(java.lang.Object)"""
        return bool.__wrap(super(__DoubleType, self).equals(arg0))

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.DoubleType.id()"""
        return int.__wrap(super(DoubleType, self).id())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.DoubleType.toString()"""
        return str.__wrap(super(DoubleType, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.ubo.types.DoubleType(double)"""
        val = __DoubleType(__double.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.DoubleType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__DoubleType, self).write(arg0)

    @overload
    def setValue(self, arg0: 'Double'):
        """public void dev.ultreon.ubo.types.DoubleType.setValue(java.lang.Double)"""
        super(__DoubleType, self).setValue(arg0)

    @override
    @overload
    def copy(self) -> 'DoubleType':
        """public dev.ultreon.ubo.types.DoubleType dev.ultreon.ubo.types.DoubleType.copy()"""
        return 'DoubleType'.__wrap(super(DoubleType, self).copy()) 
 
 
# CLASS: dev.ultreon.ubo.types.BigIntType
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.BigIntType as __BigIntType
__BigIntType = __BigIntType
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
import java.math.BigInteger as BigInteger
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BigIntType(__DataType, DataType):
    """dev.ultreon.ubo.types.BigIntType"""
 
    @staticmethod
    def __wrap(java_value: __BigIntType) -> 'BigIntType':
        return BigIntType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BigIntType):
        """
        Dynamic initializer for BigIntType.
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
    def copy(self) -> 'BigIntType':
        """public dev.ultreon.ubo.types.BigIntType dev.ultreon.ubo.types.BigIntType.copy()"""
        return 'BigIntType'.__wrap(super(BigIntType, self).copy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.BigIntType.equals(java.lang.Object)"""
        return bool.__wrap(super(__BigIntType, self).equals(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.BigIntType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__BigIntType, self).write(arg0)

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.BigIntType.id()"""
        return int.__wrap(super(BigIntType, self).id())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BigIntType.toString()"""
        return str.__wrap(super(BigIntType, self).toString())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'BigIntType':
        """public static dev.ultreon.ubo.types.BigIntType dev.ultreon.ubo.types.BigIntType.read(java.io.DataInput) throws java.io.IOException"""
        return BigIntType.__wrap(__BigIntType.read(arg0))

    @overload
    def setValue(self, arg0: 'BigInteger'):
        """public void dev.ultreon.ubo.types.BigIntType.setValue(java.math.BigInteger)"""
        super(__BigIntType, self).setValue(arg0)

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
    def __init__(self, arg0: 'BigInteger'):
        """public dev.ultreon.ubo.types.BigIntType(java.math.BigInteger)"""
        val = __BigIntType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.ubo.types.BigIntType(java.lang.String)"""
        val = __BigIntType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getValue(self) -> 'BigInteger':
        """public java.math.BigInteger dev.ultreon.ubo.types.BigIntType.getValue()"""
        return __transform(super(BigIntType, self).getValue()).'BigInteger'Value()

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BigIntType.writeUso()"""
        return str.__wrap(super(BigIntType, self).writeUso())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.BigIntType.hashCode()"""
        return int.__wrap(super(BigIntType, self).hashCode()) 
 
 
# CLASS: dev.ultreon.ubo.types.LongType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Long as Long
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.LongType as __LongType
__LongType = __LongType
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LongType(__DataType, DataType):
    """dev.ultreon.ubo.types.LongType"""
 
    @staticmethod
    def __wrap(java_value: __LongType) -> 'LongType':
        return LongType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongType):
        """
        Dynamic initializer for LongType.
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
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.LongType.writeUso()"""
        return str.__wrap(super(LongType, self).writeUso())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.LongType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__LongType, self).write(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.LongType.hashCode()"""
        return int.__wrap(super(LongType, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def copy(self) -> 'LongType':
        """public dev.ultreon.ubo.types.LongType dev.ultreon.ubo.types.LongType.copy()"""
        return 'LongType'.__wrap(super(LongType, self).copy())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setValue(self, arg0: 'Long'):
        """public void dev.ultreon.ubo.types.LongType.setValue(java.lang.Long)"""
        super(__LongType, self).setValue(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.LongType.equals(java.lang.Object)"""
        return bool.__wrap(super(__LongType, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.LongType.toString()"""
        return str.__wrap(super(LongType, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.LongType(long)"""
        val = __LongType(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getValue(self) -> 'Long':
        """public java.lang.Long dev.ultreon.ubo.types.LongType.getValue()"""
        return __transform(super(LongType, self).getValue()).'Long'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'LongType':
        """public static dev.ultreon.ubo.types.LongType dev.ultreon.ubo.types.LongType.read(java.io.DataInput) throws java.io.IOException"""
        return LongType.__wrap(__LongType.read(arg0))

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.LongType.id()"""
        return int.__wrap(super(LongType, self).id()) 
 
 
# CLASS: dev.ultreon.ubo.types.DoubleArrayType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DoubleArrayType as __DoubleArrayType
__DoubleArrayType = __DoubleArrayType
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DoubleArrayType(__DataType, DataType):
    """dev.ultreon.ubo.types.DoubleArrayType"""
 
    @staticmethod
    def __wrap(java_value: __DoubleArrayType) -> 'DoubleArrayType':
        return DoubleArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DoubleArrayType):
        """
        Dynamic initializer for DoubleArrayType.
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
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.DoubleArrayType.id()"""
        return int.__wrap(super(DoubleArrayType, self).id())

    @overload
    def setValue(self, arg0: 'double'):
        """public void dev.ultreon.ubo.types.DoubleArrayType.setValue(double[])"""
        super(__DoubleArrayType, self).setValue(arg0)

    @override
    @overload
    def getValue(self) -> List[float]:
        """public double[] dev.ultreon.ubo.types.DoubleArrayType.getValue()"""
        return List[float].__wrap(super(DoubleArrayType, self).getValue())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @overload
    def __init__(self, arg0: 'double'):
        """public dev.ultreon.ubo.types.DoubleArrayType(double[])"""
        val = __DoubleArrayType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.DoubleArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__DoubleArrayType, self).write(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.DoubleArrayType.toString()"""
        return str.__wrap(super(DoubleArrayType, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.DoubleArrayType.equals(java.lang.Object)"""
        return bool.__wrap(super(__DoubleArrayType, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def copy(self) -> 'DoubleArrayType':
        """public dev.ultreon.ubo.types.DoubleArrayType dev.ultreon.ubo.types.DoubleArrayType.copy()"""
        return 'DoubleArrayType'.__wrap(super(DoubleArrayType, self).copy())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'DoubleArrayType':
        """public static dev.ultreon.ubo.types.DoubleArrayType dev.ultreon.ubo.types.DoubleArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return DoubleArrayType.__wrap(__DoubleArrayType.read(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.DoubleArrayType.hashCode()"""
        return int.__wrap(super(DoubleArrayType, self).hashCode())

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.DoubleArrayType.size()"""
        return int.__wrap(super(DoubleArrayType, self).size())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.DoubleArrayType.writeUso()"""
        return str.__wrap(super(DoubleArrayType, self).writeUso()) 
 
 
# CLASS: dev.ultreon.ubo.types.ListType
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
import java.util.Iterator as Iterator
import dev.ultreon.ubo.types.ListType as __ListType
__ListType = __ListType
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ListType(__DataType, DataType, __Iterable, Iterable):
    """dev.ultreon.ubo.types.ListType"""
 
    @staticmethod
    def __wrap(java_value: __ListType) -> 'ListType':
        return ListType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ListType):
        """
        Dynamic initializer for ListType.
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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> dev.ultreon.ubo.types.ListType.iterator()"""
        return 'Iterator'.__wrap(super(ListType, self).iterator())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'ListType':
        """public static dev.ultreon.ubo.types.ListType<?> dev.ultreon.ubo.types.ListType.read(java.io.DataInput) throws java.io.IOException"""
        return ListType.__wrap(__ListType.read(arg0))

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.ListType.size()"""
        return int.__wrap(super(ListType, self).size())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def copy(self) -> 'ListType':
        """public dev.ultreon.ubo.types.ListType<T> dev.ultreon.ubo.types.ListType.copy()"""
        return 'ListType'.__wrap(super(ListType, self).copy())

    @overload
    def set(self, arg0: int, arg1: 'DataType') -> 'DataType':
        """public T dev.ultreon.ubo.types.ListType.set(int,T)"""
        return 'DataType'.__wrap(super(__ListType, self).set(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.ListType(int)"""
        val = __ListType(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: 'DataType'):
        """public void dev.ultreon.ubo.types.ListType.add(T)"""
        super(__ListType, self).add(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.ListType.id()"""
        return int.__wrap(super(ListType, self).id())

    @overload
    def __init__(self, arg0: 'List', *arg1: 'DataType'):
        """public dev.ultreon.ubo.types.ListType(java.util.List<T>,T...)"""
        val = __ListType(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self):
        """public void dev.ultreon.ubo.types.ListType.clear()"""
        super(ListType, self).clear()

    @overload
    def __init__(self, *arg0: 'DataType'):
        """public dev.ultreon.ubo.types.ListType(T...)"""
        val = __ListType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setValue(self, arg0: 'List'):
        """public void dev.ultreon.ubo.types.ListType.setValue(java.util.List<T>)"""
        super(__ListType, self).setValue(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.ListType.equals(java.lang.Object)"""
        return bool.__wrap(super(__ListType, self).equals(arg0))

    @overload
    def pop(self, arg0: int) -> 'DataType':
        """public T dev.ultreon.ubo.types.ListType.pop(int)"""
        return 'DataType'.__wrap(super(__ListType, self).pop(__int.valueOf(arg0)))

    @overload
    def remove(self, arg0: 'DataType') -> 'DataType':
        """public T dev.ultreon.ubo.types.ListType.remove(T)"""
        return 'DataType'.__wrap(super(__ListType, self).remove(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.ListType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__ListType, self).write(arg0)

    @override
    @overload
    def getValue(self) -> 'List':
        """public java.util.List<T> dev.ultreon.ubo.types.ListType.getValue()"""
        return 'List'.__wrap(super(ListType, self).getValue())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.ListType.hashCode()"""
        return int.__wrap(super(ListType, self).hashCode())

    @overload
    def get(self, arg0: int) -> 'DataType':
        """public T dev.ultreon.ubo.types.ListType.get(int)"""
        return 'DataType'.__wrap(super(__ListType, self).get(__int.valueOf(arg0)))

    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.ubo.types.ListType.isEmpty()"""
        return bool.__wrap(super(ListType, self).isEmpty())

    @overload
    def contains(self, arg0: 'DataType') -> bool:
        """public boolean dev.ultreon.ubo.types.ListType.contains(T)"""
        return bool.__wrap(super(__ListType, self).contains(arg0))

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ListType.toString()"""
        return str.__wrap(super(ListType, self).toString())

    @overload
    def type(self) -> int:
        """public int dev.ultreon.ubo.types.ListType.type()"""
        return int.__wrap(super(ListType, self).type())

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ListType.writeUso()"""
        return str.__wrap(super(ListType, self).writeUso())

    @overload
    def remove(self, arg0: int) -> bool:
        """public boolean dev.ultreon.ubo.types.ListType.remove(int)"""
        return bool.__wrap(super(__ListType, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def cast(self, *arg0: 'DataType') -> 'ListType':
        """public final <C extends dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.types.ListType<C> dev.ultreon.ubo.types.ListType.cast(C...)"""
        return 'ListType'.__wrap(super(__ListType, self).cast(arg0)) 
 
 
# CLASS: dev.ultreon.ubo.types.LongArrayType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import dev.ultreon.ubo.types.LongArrayType as __LongArrayType
__LongArrayType = __LongArrayType
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LongArrayType(__DataType, DataType):
    """dev.ultreon.ubo.types.LongArrayType"""
 
    @staticmethod
    def __wrap(java_value: __LongArrayType) -> 'LongArrayType':
        return LongArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongArrayType):
        """
        Dynamic initializer for LongArrayType.
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
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.LongArrayType.size()"""
        return int.__wrap(super(LongArrayType, self).size())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'LongArrayType':
        """public static dev.ultreon.ubo.types.LongArrayType dev.ultreon.ubo.types.LongArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return LongArrayType.__wrap(__LongArrayType.read(arg0))

    @override
    @overload
    def copy(self) -> 'LongArrayType':
        """public dev.ultreon.ubo.types.LongArrayType dev.ultreon.ubo.types.LongArrayType.copy()"""
        return 'LongArrayType'.__wrap(super(LongArrayType, self).copy())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.LongArrayType.writeUso()"""
        return str.__wrap(super(LongArrayType, self).writeUso())

    @overload
    def __init__(self, arg0: 'long'):
        """public dev.ultreon.ubo.types.LongArrayType(long[])"""
        val = __LongArrayType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.LongArrayType.hashCode()"""
        return int.__wrap(super(LongArrayType, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.LongArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__LongArrayType, self).write(arg0)

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.LongArrayType.id()"""
        return int.__wrap(super(LongArrayType, self).id())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.LongArrayType.toString()"""
        return str.__wrap(super(LongArrayType, self).toString())

    @overload
    def setValue(self, arg0: 'long'):
        """public void dev.ultreon.ubo.types.LongArrayType.setValue(long[])"""
        super(__LongArrayType, self).setValue(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.LongArrayType.equals(java.lang.Object)"""
        return bool.__wrap(super(__LongArrayType, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getValue(self) -> List[int]:
        """public long[] dev.ultreon.ubo.types.LongArrayType.getValue()"""
        return List[int].__wrap(super(LongArrayType, self).getValue()) 
 
 
# CLASS: dev.ultreon.ubo.types.ShortType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Short as Short
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.ubo.types.ShortType as __ShortType
__ShortType = __ShortType
from builtins import bool
from builtins import int
 
class ShortType(__DataType, DataType):
    """dev.ultreon.ubo.types.ShortType"""
 
    @staticmethod
    def __wrap(java_value: __ShortType) -> 'ShortType':
        return ShortType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShortType):
        """
        Dynamic initializer for ShortType.
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
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.ShortType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__ShortType, self).write(arg0)

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.ShortType(short)"""
        val = __ShortType(__short.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setValue(self, arg0: 'Short'):
        """public void dev.ultreon.ubo.types.ShortType.setValue(java.lang.Short)"""
        super(__ShortType, self).setValue(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.ShortType.hashCode()"""
        return int.__wrap(super(ShortType, self).hashCode())

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.ShortType.id()"""
        return int.__wrap(super(ShortType, self).id())

    @override
    @overload
    def copy(self) -> 'ShortType':
        """public dev.ultreon.ubo.types.ShortType dev.ultreon.ubo.types.ShortType.copy()"""
        return 'ShortType'.__wrap(super(ShortType, self).copy())

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ShortType.writeUso()"""
        return str.__wrap(super(ShortType, self).writeUso())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ShortType.toString()"""
        return str.__wrap(super(ShortType, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getValue(self) -> 'Short':
        """public java.lang.Short dev.ultreon.ubo.types.ShortType.getValue()"""
        return __transform(super(ShortType, self).getValue()).'Short'Value()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.ShortType(int)"""
        val = __ShortType(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.ShortType.equals(java.lang.Object)"""
        return bool.__wrap(super(__ShortType, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'ShortType':
        """public static dev.ultreon.ubo.types.ShortType dev.ultreon.ubo.types.ShortType.read(java.io.DataInput) throws java.io.IOException"""
        return ShortType.__wrap(__ShortType.read(arg0)) 
 
 
# CLASS: dev.ultreon.ubo.types.StringType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

import dev.ultreon.ubo.types.StringType as __StringType
__StringType = __StringType
from builtins import object
import java.io.DataInput as DataInput
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StringType(__DataType, DataType):
    """dev.ultreon.ubo.types.StringType"""
 
    @staticmethod
    def __wrap(java_value: __StringType) -> 'StringType':
        return StringType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringType):
        """
        Dynamic initializer for StringType.
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
    def __init__(self, arg0: str):
        """public dev.ultreon.ubo.types.StringType(java.lang.String)"""
        val = __StringType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getValue(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.StringType.getValue()"""
        return str.__wrap(super(StringType, self).getValue())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.StringType.hashCode()"""
        return int.__wrap(super(StringType, self).hashCode())

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.StringType.id()"""
        return int.__wrap(super(StringType, self).id())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.StringType.toString()"""
        return str.__wrap(super(StringType, self).toString())

    @overload
    def setValue(self, arg0: str):
        """public void dev.ultreon.ubo.types.StringType.setValue(java.lang.String)"""
        super(__StringType, self).setValue(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.StringType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__StringType, self).write(arg0)

    @override
    @overload
    def copy(self) -> 'StringType':
        """public dev.ultreon.ubo.types.StringType dev.ultreon.ubo.types.StringType.copy()"""
        return 'StringType'.__wrap(super(StringType, self).copy())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'StringType':
        """public static dev.ultreon.ubo.types.StringType dev.ultreon.ubo.types.StringType.read(java.io.DataInput) throws java.io.IOException"""
        return StringType.__wrap(__StringType.read(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.StringType.writeUso()"""
        return str.__wrap(super(StringType, self).writeUso())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.StringType.equals(java.lang.Object)"""
        return bool.__wrap(super(__StringType, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.ubo.types.CharArrayType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.ubo.types.CharArrayType as __CharArrayType
__CharArrayType = __CharArrayType
from builtins import int
 
class CharArrayType(__DataType, DataType):
    """dev.ultreon.ubo.types.CharArrayType"""
 
    @staticmethod
    def __wrap(java_value: __CharArrayType) -> 'CharArrayType':
        return CharArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharArrayType):
        """
        Dynamic initializer for CharArrayType.
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
    def setValue(self, arg0: 'char'):
        """public void dev.ultreon.ubo.types.CharArrayType.setValue(char[])"""
        super(__CharArrayType, self).setValue(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.CharArrayType.hashCode()"""
        return int.__wrap(super(CharArrayType, self).hashCode())

    @override
    @overload
    def copy(self) -> 'CharArrayType':
        """public dev.ultreon.ubo.types.CharArrayType dev.ultreon.ubo.types.CharArrayType.copy()"""
        return 'CharArrayType'.__wrap(super(CharArrayType, self).copy())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.CharArrayType.writeUso()"""
        return str.__wrap(super(CharArrayType, self).writeUso())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.CharArrayType.toString()"""
        return str.__wrap(super(CharArrayType, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'char'):
        """public dev.ultreon.ubo.types.CharArrayType(char[])"""
        val = __CharArrayType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.CharArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__CharArrayType, self).write(arg0)

    @override
    @overload
    def getValue(self) -> List[str]:
        """public char[] dev.ultreon.ubo.types.CharArrayType.getValue()"""
        return List[str].__wrap(super(CharArrayType, self).getValue())

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.CharArrayType.id()"""
        return int.__wrap(super(CharArrayType, self).id())

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.CharArrayType.size()"""
        return int.__wrap(super(CharArrayType, self).size())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.CharArrayType.equals(java.lang.Object)"""
        return bool.__wrap(super(__CharArrayType, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'CharArrayType':
        """public static dev.ultreon.ubo.types.CharArrayType dev.ultreon.ubo.types.CharArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return CharArrayType.__wrap(__CharArrayType.read(arg0)) 
 
 
# CLASS: dev.ultreon.ubo.types.IntArrayType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.ubo.types.IntArrayType as __IntArrayType
__IntArrayType = __IntArrayType
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IntArrayType(__DataType, DataType):
    """dev.ultreon.ubo.types.IntArrayType"""
 
    @staticmethod
    def __wrap(java_value: __IntArrayType) -> 'IntArrayType':
        return IntArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntArrayType):
        """
        Dynamic initializer for IntArrayType.
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
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.IntArrayType.writeUso()"""
        return str.__wrap(super(IntArrayType, self).writeUso())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.IntArrayType.id()"""
        return int.__wrap(super(IntArrayType, self).id())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'IntArrayType':
        """public static dev.ultreon.ubo.types.IntArrayType dev.ultreon.ubo.types.IntArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return IntArrayType.__wrap(__IntArrayType.read(arg0))

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

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
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.IntArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__IntArrayType, self).write(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.IntArrayType.equals(java.lang.Object)"""
        return bool.__wrap(super(__IntArrayType, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.IntArrayType.toString()"""
        return str.__wrap(super(IntArrayType, self).toString())

    @override
    @overload
    def copy(self) -> 'IntArrayType':
        """public dev.ultreon.ubo.types.IntArrayType dev.ultreon.ubo.types.IntArrayType.copy()"""
        return 'IntArrayType'.__wrap(super(IntArrayType, self).copy())

    @overload
    def __init__(self, arg0: 'int'):
        """public dev.ultreon.ubo.types.IntArrayType(int[])"""
        val = __IntArrayType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setValue(self, arg0: 'int'):
        """public void dev.ultreon.ubo.types.IntArrayType.setValue(int[])"""
        super(__IntArrayType, self).setValue(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.IntArrayType.size()"""
        return int.__wrap(super(IntArrayType, self).size())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.IntArrayType.hashCode()"""
        return int.__wrap(super(IntArrayType, self).hashCode())

    @override
    @overload
    def getValue(self) -> List[int]:
        """public int[] dev.ultreon.ubo.types.IntArrayType.getValue()"""
        return List[int].__wrap(super(IntArrayType, self).getValue()) 
 
 
# CLASS: dev.ultreon.ubo.types.FloatArrayType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.FloatArrayType as __FloatArrayType
__FloatArrayType = __FloatArrayType
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FloatArrayType(__DataType, DataType):
    """dev.ultreon.ubo.types.FloatArrayType"""
 
    @staticmethod
    def __wrap(java_value: __FloatArrayType) -> 'FloatArrayType':
        return FloatArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatArrayType):
        """
        Dynamic initializer for FloatArrayType.
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
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.FloatArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__FloatArrayType, self).write(arg0)

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.FloatArrayType.toString()"""
        return str.__wrap(super(FloatArrayType, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.FloatArrayType.equals(java.lang.Object)"""
        return bool.__wrap(super(__FloatArrayType, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getValue(self) -> List[float]:
        """public float[] dev.ultreon.ubo.types.FloatArrayType.getValue()"""
        return List[float].__wrap(super(FloatArrayType, self).getValue())

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def copy(self) -> 'FloatArrayType':
        """public dev.ultreon.ubo.types.FloatArrayType dev.ultreon.ubo.types.FloatArrayType.copy()"""
        return 'FloatArrayType'.__wrap(super(FloatArrayType, self).copy())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'FloatArrayType':
        """public static dev.ultreon.ubo.types.FloatArrayType dev.ultreon.ubo.types.FloatArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return FloatArrayType.__wrap(__FloatArrayType.read(arg0))

    @overload
    def setValue(self, arg0: 'float'):
        """public void dev.ultreon.ubo.types.FloatArrayType.setValue(float[])"""
        super(__FloatArrayType, self).setValue(arg0)

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.FloatArrayType.size()"""
        return int.__wrap(super(FloatArrayType, self).size())

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.FloatArrayType.id()"""
        return int.__wrap(super(FloatArrayType, self).id())

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.FloatArrayType.writeUso()"""
        return str.__wrap(super(FloatArrayType, self).writeUso())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.FloatArrayType.hashCode()"""
        return int.__wrap(super(FloatArrayType, self).hashCode())

    @overload
    def __init__(self, arg0: 'float'):
        """public dev.ultreon.ubo.types.FloatArrayType(float[])"""
        val = __FloatArrayType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.ubo.types.ShortArrayType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

import dev.ultreon.ubo.types.ShortArrayType as __ShortArrayType
__ShortArrayType = __ShortArrayType
from builtins import object
import java.io.DataInput as DataInput
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ShortArrayType(__DataType, DataType):
    """dev.ultreon.ubo.types.ShortArrayType"""
 
    @staticmethod
    def __wrap(java_value: __ShortArrayType) -> 'ShortArrayType':
        return ShortArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShortArrayType):
        """
        Dynamic initializer for ShortArrayType.
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
    def copy(self) -> 'ShortArrayType':
        """public dev.ultreon.ubo.types.ShortArrayType dev.ultreon.ubo.types.ShortArrayType.copy()"""
        return 'ShortArrayType'.__wrap(super(ShortArrayType, self).copy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.ShortArrayType.size()"""
        return int.__wrap(super(ShortArrayType, self).size())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ShortArrayType.toString()"""
        return str.__wrap(super(ShortArrayType, self).toString())

    @override
    @overload
    def getValue(self) -> List[int]:
        """public short[] dev.ultreon.ubo.types.ShortArrayType.getValue()"""
        return List[int].__wrap(super(ShortArrayType, self).getValue())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.ShortArrayType.equals(java.lang.Object)"""
        return bool.__wrap(super(__ShortArrayType, self).equals(arg0))

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
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.ShortArrayType.id()"""
        return int.__wrap(super(ShortArrayType, self).id())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'short'):
        """public dev.ultreon.ubo.types.ShortArrayType(short[])"""
        val = __ShortArrayType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.ShortArrayType.hashCode()"""
        return int.__wrap(super(ShortArrayType, self).hashCode())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.ShortArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__ShortArrayType, self).write(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setValue(self, arg0: 'short'):
        """public void dev.ultreon.ubo.types.ShortArrayType.setValue(short[])"""
        super(__ShortArrayType, self).setValue(arg0)

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ShortArrayType.writeUso()"""
        return str.__wrap(super(ShortArrayType, self).writeUso())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'ShortArrayType':
        """public static dev.ultreon.ubo.types.ShortArrayType dev.ultreon.ubo.types.ShortArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return ShortArrayType.__wrap(__ShortArrayType.read(arg0)) 
 
 
# CLASS: dev.ultreon.ubo.types.CharType
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.CharType as __CharType
__CharType = __CharType
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.Character as __Character
__Character = __Character
import java.lang.Object as __Object
__Object = __Object
import java.lang.Character as Character
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CharType(__DataType, DataType):
    """dev.ultreon.ubo.types.CharType"""
 
    @staticmethod
    def __wrap(java_value: __CharType) -> 'CharType':
        return CharType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharType):
        """
        Dynamic initializer for CharType.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.CharType.hashCode()"""
        return int.__wrap(super(CharType, self).hashCode())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.CharType.writeUso()"""
        return str.__wrap(super(CharType, self).writeUso())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.CharType.equals(java.lang.Object)"""
        return bool.__wrap(super(__CharType, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'CharType':
        """public static dev.ultreon.ubo.types.CharType dev.ultreon.ubo.types.CharType.read(java.io.DataInput) throws java.io.IOException"""
        return CharType.__wrap(__CharType.read(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.CharType.toString()"""
        return str.__wrap(super(CharType, self).toString())

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.CharType.id()"""
        return int.__wrap(super(CharType, self).id())

    @override
    @overload
    def copy(self) -> 'CharType':
        """public dev.ultreon.ubo.types.CharType dev.ultreon.ubo.types.CharType.copy()"""
        return 'CharType'.__wrap(super(CharType, self).copy())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.CharType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__CharType, self).write(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getValue(self) -> 'Character':
        """public java.lang.Character dev.ultreon.ubo.types.CharType.getValue()"""
        return 'Character'.__wrap(super(CharType, self).getValue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.ubo.types.CharType(char)"""
        val = __CharType(__char.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setValue(self, arg0: 'Character'):
        """public void dev.ultreon.ubo.types.CharType.setValue(java.lang.Character)"""
        super(__CharType, self).setValue(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.ubo.types.ByteArrayType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.nio.charset.Charset as Charset
import java.lang.Object as __object
from builtins import type
import dev.ultreon.ubo.types.ByteArrayType as __ByteArrayType
__ByteArrayType = __ByteArrayType
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
import java.lang.Byte as Byte
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class ByteArrayType(__DataType, DataType):
    """dev.ultreon.ubo.types.ByteArrayType"""
 
    @staticmethod
    def __wrap(java_value: __ByteArrayType) -> 'ByteArrayType':
        return ByteArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteArrayType):
        """
        Dynamic initializer for ByteArrayType.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.ByteArrayType.hashCode()"""
        return int.__wrap(super(ByteArrayType, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: bytes, arg1: int):
        """public dev.ultreon.ubo.types.ByteArrayType(byte[],int)"""
        val = __ByteArrayType(bytes, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.ByteArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__ByteArrayType, self).write(arg0)

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.ByteArrayType.id()"""
        return int.__wrap(super(ByteArrayType, self).id())

    @override
    @overload
    def copy(self) -> 'ByteArrayType':
        """public dev.ultreon.ubo.types.ByteArrayType dev.ultreon.ubo.types.ByteArrayType.copy()"""
        return 'ByteArrayType'.__wrap(super(ByteArrayType, self).copy())

    @override
    @overload
    def getValue(self) -> List[int]:
        """public byte[] dev.ultreon.ubo.types.ByteArrayType.getValue()"""
        return List[int].__wrap(super(ByteArrayType, self).getValue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public dev.ultreon.ubo.types.ByteArrayType(java.nio.ByteBuffer)"""
        val = __ByteArrayType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.ubo.types.ByteArrayType(java.lang.String)"""
        val = __ByteArrayType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: bytes):
        """public dev.ultreon.ubo.types.ByteArrayType(byte[])"""
        val = __ByteArrayType(bytes)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ByteArrayType.toString()"""
        return str.__wrap(super(ByteArrayType, self).toString())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.ByteArrayType.equals(java.lang.Object)"""
        return bool.__wrap(super(__ByteArrayType, self).equals(arg0))

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ByteArrayType.writeUso()"""
        return str.__wrap(super(ByteArrayType, self).writeUso())

    @overload
    def setValue(self, arg0: bytes):
        """public void dev.ultreon.ubo.types.ByteArrayType.setValue(byte[])"""
        super(__ByteArrayType, self).setValue(bytes)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.ByteArrayType.size()"""
        return int.__wrap(super(ByteArrayType, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str, arg1: 'Charset'):
        """public dev.ultreon.ubo.types.ByteArrayType(java.lang.String,java.nio.charset.Charset)"""
        val = __ByteArrayType(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Byte'):
        """public dev.ultreon.ubo.types.ByteArrayType(java.lang.Byte[])"""
        val = __ByteArrayType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'ByteArrayType':
        """public static dev.ultreon.ubo.types.ByteArrayType dev.ultreon.ubo.types.ByteArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return ByteArrayType.__wrap(__ByteArrayType.read(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.ByteArrayType(int)"""
        val = __ByteArrayType(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.ubo.types.IntType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import dev.ultreon.ubo.types.IntType as __IntType
__IntType = __IntType
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IntType(__DataType, DataType):
    """dev.ultreon.ubo.types.IntType"""
 
    @staticmethod
    def __wrap(java_value: __IntType) -> 'IntType':
        return IntType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntType):
        """
        Dynamic initializer for IntType.
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
    def getValue(self) -> 'Integer':
        """public java.lang.Integer dev.ultreon.ubo.types.IntType.getValue()"""
        return __transform(super(IntType, self).getValue()).'Integer'Value()

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.IntType(int)"""
        val = __IntType(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.IntType.hashCode()"""
        return int.__wrap(super(IntType, self).hashCode())

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.IntType.id()"""
        return int.__wrap(super(IntType, self).id())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setValue(self, arg0: 'Integer'):
        """public void dev.ultreon.ubo.types.IntType.setValue(java.lang.Integer)"""
        super(__IntType, self).setValue(arg0)

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
    def copy(self) -> 'IntType':
        """public dev.ultreon.ubo.types.IntType dev.ultreon.ubo.types.IntType.copy()"""
        return 'IntType'.__wrap(super(IntType, self).copy())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.IntType.equals(java.lang.Object)"""
        return bool.__wrap(super(__IntType, self).equals(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.IntType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__IntType, self).write(arg0)

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.IntType.writeUso()"""
        return str.__wrap(super(IntType, self).writeUso())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.IntType.toString()"""
        return str.__wrap(super(IntType, self).toString())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'IntType':
        """public static dev.ultreon.ubo.types.IntType dev.ultreon.ubo.types.IntType.read(java.io.DataInput) throws java.io.IOException"""
        return IntType.__wrap(__IntType.read(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.ubo.types.ByteType
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.ByteType as __ByteType
__ByteType = __ByteType
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.lang.Byte as Byte
import java.io.DataInput as DataInput
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.Byte as __byte
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ByteType(__DataType, DataType):
    """dev.ultreon.ubo.types.ByteType"""
 
    @staticmethod
    def __wrap(java_value: __ByteType) -> 'ByteType':
        return ByteType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteType):
        """
        Dynamic initializer for ByteType.
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
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.ByteType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__ByteType, self).write(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'ByteType':
        """public static dev.ultreon.ubo.types.ByteType dev.ultreon.ubo.types.ByteType.read(java.io.DataInput) throws java.io.IOException"""
        return ByteType.__wrap(__ByteType.read(arg0))

    @overload
    def setValue(self, arg0: 'Byte'):
        """public void dev.ultreon.ubo.types.ByteType.setValue(java.lang.Byte)"""
        super(__ByteType, self).setValue(arg0)

    @override
    @overload
    def copy(self) -> 'ByteType':
        """public dev.ultreon.ubo.types.ByteType dev.ultreon.ubo.types.ByteType.copy()"""
        return 'ByteType'.__wrap(super(ByteType, self).copy())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.ByteType.hashCode()"""
        return int.__wrap(super(ByteType, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getValue(self) -> 'Byte':
        """public java.lang.Byte dev.ultreon.ubo.types.ByteType.getValue()"""
        return __transform(super(ByteType, self).getValue()).'Byte'Value()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ByteType.writeUso()"""
        return str.__wrap(super(ByteType, self).writeUso())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.ByteType.equals(java.lang.Object)"""
        return bool.__wrap(super(__ByteType, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.ByteType(int)"""
        val = __ByteType(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ByteType.toString()"""
        return str.__wrap(super(ByteType, self).toString())

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.ByteType.id()"""
        return int.__wrap(super(ByteType, self).id())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.ByteType(byte)"""
        val = __ByteType(__byte.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.ubo.types.BooleanType
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

import java.lang.Boolean as __Boolean
__Boolean = __Boolean
from builtins import object
import java.io.DataInput as DataInput
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import dev.ultreon.ubo.types.BooleanType as __BooleanType
__BooleanType = __BooleanType
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BooleanType(__DataType, DataType):
    """dev.ultreon.ubo.types.BooleanType"""
 
    @staticmethod
    def __wrap(java_value: __BooleanType) -> 'BooleanType':
        return BooleanType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BooleanType):
        """
        Dynamic initializer for BooleanType.
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
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.BooleanType.id()"""
        return int.__wrap(super(BooleanType, self).id())

    @override
    @overload
    def copy(self) -> 'BooleanType':
        """public dev.ultreon.ubo.types.BooleanType dev.ultreon.ubo.types.BooleanType.copy()"""
        return 'BooleanType'.__wrap(super(BooleanType, self).copy())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @overload
    def setValue(self, arg0: 'Boolean'):
        """public void dev.ultreon.ubo.types.BooleanType.setValue(java.lang.Boolean)"""
        super(__BooleanType, self).setValue(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.BooleanType.equals(java.lang.Object)"""
        return bool.__wrap(super(__BooleanType, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'BooleanType':
        """public static dev.ultreon.ubo.types.BooleanType dev.ultreon.ubo.types.BooleanType.read(java.io.DataInput) throws java.io.IOException"""
        return BooleanType.__wrap(__BooleanType.read(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.BooleanType.hashCode()"""
        return int.__wrap(super(BooleanType, self).hashCode())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.BooleanType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__BooleanType, self).write(arg0)

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BooleanType.writeUso()"""
        return str.__wrap(super(BooleanType, self).writeUso())

    @overload
    def __init__(self, arg0: bool):
        """public dev.ultreon.ubo.types.BooleanType(boolean)"""
        val = __BooleanType(__boolean.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BooleanType.toString()"""
        return str.__wrap(super(BooleanType, self).toString())

    @override
    @overload
    def getValue(self) -> 'Boolean':
        """public java.lang.Boolean dev.ultreon.ubo.types.BooleanType.getValue()"""
        return 'Boolean'.__wrap(super(BooleanType, self).getValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.ubo.types.BitSetType
from pyquantum_helper import import_once as __import_once__
import java.util.BitSet as __BitSet
__BitSet = __BitSet
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
import java.util.BitSet as BitSet
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.ubo.types.BitSetType as __BitSetType
__BitSetType = __BitSetType
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BitSetType(__DataType, DataType):
    """dev.ultreon.ubo.types.BitSetType"""
 
    @staticmethod
    def __wrap(java_value: __BitSetType) -> 'BitSetType':
        return BitSetType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BitSetType):
        """
        Dynamic initializer for BitSetType.
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
    def setValue(self, arg0: 'BitSet'):
        """public void dev.ultreon.ubo.types.BitSetType.setValue(java.util.BitSet)"""
        super(__BitSetType, self).setValue(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.BitSetType.equals(java.lang.Object)"""
        return bool.__wrap(super(__BitSetType, self).equals(arg0))

    @override
    @overload
    def copy(self) -> 'BitSetType':
        """public dev.ultreon.ubo.types.BitSetType dev.ultreon.ubo.types.BitSetType.copy()"""
        return 'BitSetType'.__wrap(super(BitSetType, self).copy())

    @override
    @overload
    def getValue(self) -> 'BitSet':
        """public java.util.BitSet dev.ultreon.ubo.types.BitSetType.getValue()"""
        return 'BitSet'.__wrap(super(BitSetType, self).getValue())

    @overload
    def length(self) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.length()"""
        return int.__wrap(super(BitSetType, self).length())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'long'):
        """public dev.ultreon.ubo.types.BitSetType(long[])"""
        val = __BitSetType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getBit(self, arg0: int) -> bool:
        """public boolean dev.ultreon.ubo.types.BitSetType.getBit(int)"""
        return bool.__wrap(super(__BitSetType, self).getBit(__int.valueOf(arg0)))

    @overload
    def nextSetBit(self, arg0: int) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.nextSetBit(int)"""
        return int.__wrap(super(__BitSetType, self).nextSetBit(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: bytes):
        """public dev.ultreon.ubo.types.BitSetType(byte[])"""
        val = __BitSetType(bytes)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.BitSetType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__BitSetType, self).write(arg0)

    @overload
    def previousClearBit(self, arg0: int) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.previousClearBit(int)"""
        return int.__wrap(super(__BitSetType, self).previousClearBit(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.hashCode()"""
        return int.__wrap(super(BitSetType, self).hashCode())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'BitSetType':
        """public static dev.ultreon.ubo.types.BitSetType dev.ultreon.ubo.types.BitSetType.read(java.io.DataInput) throws java.io.IOException"""
        return BitSetType.__wrap(__BitSetType.read(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.ubo.types.BitSetType(java.lang.String)"""
        val = __BitSetType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def cardinality(self) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.cardinality()"""
        return int.__wrap(super(BitSetType, self).cardinality())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.id()"""
        return int.__wrap(super(BitSetType, self).id())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BitSetType.toString()"""
        return str.__wrap(super(BitSetType, self).toString())

    @overload
    def setBit(self, arg0: int, arg1: bool):
        """public void dev.ultreon.ubo.types.BitSetType.setBit(int,boolean)"""
        super(__BitSetType, self).setBit(__int.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def nextClearBit(self, arg0: int) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.nextClearBit(int)"""
        return int.__wrap(super(__BitSetType, self).nextClearBit(__int.valueOf(arg0)))

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
    def previousSetBit(self, arg0: int) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.previousSetBit(int)"""
        return int.__wrap(super(__BitSetType, self).previousSetBit(__int.valueOf(arg0)))

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BitSetType.writeUso()"""
        return str.__wrap(super(BitSetType, self).writeUso())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'BitSet'):
        """public dev.ultreon.ubo.types.BitSetType(java.util.BitSet)"""
        val = __BitSetType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.ubo.types.DataType
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.io.DataOutput as DataOutput
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

import java.lang.Object as __Object
__Object = __Object
from abc import abstractmethod, ABC
from builtins import object
 
class DataType(ABC):
    """dev.ultreon.ubo.types.DataType"""
 
    @staticmethod
    def __wrap(java_value: __DataType) -> 'DataType':
        return DataType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DataType):
        """
        Dynamic initializer for DataType.
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
    def equals(self, arg0: object):
        """public abstract boolean dev.ultreon.ubo.types.DataType.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def id(self, ):
        """public abstract int dev.ultreon.ubo.types.DataType.id()"""
        pass

    @abstractmethod
    def copy(self, ):
        """public abstract dev.ultreon.ubo.types.DataType<T> dev.ultreon.ubo.types.DataType.copy()"""
        pass

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @abstractmethod
    def setValue(self, arg0: object):
        """public abstract void dev.ultreon.ubo.types.DataType.setValue(T)"""
        pass

    @abstractmethod
    def getValue(self, ):
        """public abstract T dev.ultreon.ubo.types.DataType.getValue()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int dev.ultreon.ubo.types.DataType.hashCode()"""
        pass

    @abstractmethod
    def writeUso(self, ):
        """public abstract java.lang.String dev.ultreon.ubo.types.DataType.writeUso()"""
        pass

    @abstractmethod
    def write(self, arg0: 'DataOutput'):
        """public abstract void dev.ultreon.ubo.types.DataType.write(java.io.DataOutput) throws java.io.IOException"""
        pass 
 
 
# CLASS: dev.ultreon.ubo.types.UUIDType
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.lang.String as __String
__String = __String
import java.util.UUID as __UUID
__UUID = __UUID
import java.io.DataOutput as DataOutput
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.ubo.types.UUIDType as __UUIDType
__UUIDType = __UUIDType
from builtins import int
 
class UUIDType(__DataType, DataType):
    """dev.ultreon.ubo.types.UUIDType"""
 
    @staticmethod
    def __wrap(java_value: __UUIDType) -> 'UUIDType':
        return UUIDType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UUIDType):
        """
        Dynamic initializer for UUIDType.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.UUIDType.hashCode()"""
        return int.__wrap(super(UUIDType, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def copy(self) -> 'UUIDType':
        """public dev.ultreon.ubo.types.UUIDType dev.ultreon.ubo.types.UUIDType.copy()"""
        return 'UUIDType'.__wrap(super(UUIDType, self).copy())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.UUIDType.writeUso()"""
        return str.__wrap(super(UUIDType, self).writeUso())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.UUIDType.equals(java.lang.Object)"""
        return bool.__wrap(super(__UUIDType, self).equals(arg0))

    @override
    @overload
    def getValue(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.ubo.types.UUIDType.getValue()"""
        return 'UUID'.__wrap(super(UUIDType, self).getValue())

    @overload
    def setValue(self, arg0: 'UUID'):
        """public void dev.ultreon.ubo.types.UUIDType.setValue(java.util.UUID)"""
        super(__UUIDType, self).setValue(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.UUIDType.toString()"""
        return str.__wrap(super(UUIDType, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'UUIDType':
        """public static dev.ultreon.ubo.types.UUIDType dev.ultreon.ubo.types.UUIDType.read(java.io.DataInput) throws java.io.IOException"""
        return UUIDType.__wrap(__UUIDType.read(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.UUIDType.id()"""
        return int.__wrap(super(UUIDType, self).id())

    @overload
    def __init__(self, arg0: 'UUID'):
        """public dev.ultreon.ubo.types.UUIDType(java.util.UUID)"""
        val = __UUIDType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.UUIDType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__UUIDType, self).write(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.ubo.types.BigDecType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = __import_once__("pyubo.util")

from builtins import object
import java.io.DataInput as DataInput
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import dev.ultreon.ubo.types.BigDecType as __BigDecType
__BigDecType = __BigDecType
import java.lang.String as __String
__String = __String
import java.io.DataOutput as DataOutput
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.math.BigDecimal as BigDecimal
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BigDecType(__DataType, DataType):
    """dev.ultreon.ubo.types.BigDecType"""
 
    @staticmethod
    def __wrap(java_value: __BigDecType) -> 'BigDecType':
        return BigDecType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BigDecType):
        """
        Dynamic initializer for BigDecType.
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
    def __init__(self, arg0: str):
        """public dev.ultreon.ubo.types.BigDecType(java.lang.String)"""
        val = __BigDecType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'BigDecType':
        """public dev.ultreon.ubo.types.BigDecType dev.ultreon.ubo.types.BigDecType.copy()"""
        return 'BigDecType'.__wrap(super(BigDecType, self).copy())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object.__wrap(super(__DataType, self).accept(arg0))

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BigDecType.writeUso()"""
        return str.__wrap(super(BigDecType, self).writeUso())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'BigDecimal'):
        """public dev.ultreon.ubo.types.BigDecType(java.math.BigDecimal)"""
        val = __BigDecType(arg0)
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

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.BigDecType.hashCode()"""
        return int.__wrap(super(BigDecType, self).hashCode())

    @overload
    def setValue(self, arg0: 'BigDecimal'):
        """public void dev.ultreon.ubo.types.BigDecType.setValue(java.math.BigDecimal)"""
        super(__BigDecType, self).setValue(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.BigDecType.write(java.io.DataOutput) throws java.io.IOException"""
        super(__BigDecType, self).write(arg0)

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'BigDecType':
        """public static dev.ultreon.ubo.types.BigDecType dev.ultreon.ubo.types.BigDecType.read(java.io.DataInput) throws java.io.IOException"""
        return BigDecType.__wrap(__BigDecType.read(arg0))

    @override
    @overload
    def getValue(self) -> 'BigDecimal':
        """public java.math.BigDecimal dev.ultreon.ubo.types.BigDecType.getValue()"""
        return __transform(super(BigDecType, self).getValue()).'BigDecimal'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BigDecType.toString()"""
        return str.__wrap(super(BigDecType, self).toString())

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.BigDecType.id()"""
        return int.__wrap(super(BigDecType, self).id())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.BigDecType.equals(java.lang.Object)"""
        return bool.__wrap(super(__BigDecType, self).equals(arg0))