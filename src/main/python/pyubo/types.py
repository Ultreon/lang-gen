from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.Float as Float
import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import java.lang.Float as _float
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
import dev.ultreon.ubo.types.FloatType as _FloatType
_FloatType = _FloatType
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatType():
    """dev.ultreon.ubo.types.FloatType"""
 
    @staticmethod
    def _wrap(java_value: _FloatType) -> 'FloatType':
        return FloatType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatType):
        """
        Dynamic initializer for FloatType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.FloatType.writeUso()"""
        return str._wrap(super(FloatType, self).writeUso())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

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
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.FloatType.id()"""
        return int._wrap(super(FloatType, self).id())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.FloatType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_FloatType, self).write(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.FloatType.toString()"""
        return str._wrap(super(FloatType, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.FloatType.hashCode()"""
        return int._wrap(super(FloatType, self).hashCode())

    @override
    @overload
    def getValue(self) -> 'Float':
        """public java.lang.Float dev.ultreon.ubo.types.FloatType.getValue()"""
        return _transform(super(FloatType, self).getValue()).'Float'Value()

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
    def __init__(self, arg0: float):
        """public dev.ultreon.ubo.types.FloatType(float)"""
        val = _FloatType(_float.valueOf(arg0))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.FloatType.equals(java.lang.Object)"""
        return bool._wrap(super(_FloatType, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'FloatType':
        """public static dev.ultreon.ubo.types.FloatType dev.ultreon.ubo.types.FloatType.read(java.io.DataInput) throws java.io.IOException"""
        return FloatType._wrap(_FloatType.read(arg0))

    @overload
    def setValue(self, arg0: 'Float'):
        """public void dev.ultreon.ubo.types.FloatType.setValue(java.lang.Float)"""
        super(_FloatType, self).setValue(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def copy(self) -> 'FloatType':
        """public dev.ultreon.ubo.types.FloatType dev.ultreon.ubo.types.FloatType.copy()"""
        return 'FloatType'._wrap(super(FloatType, self).copy())

 
 
 
# CLASS: dev.ultreon.ubo.types.FloatType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.Float as Float
import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import java.lang.Float as _float
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
import dev.ultreon.ubo.types.FloatType as _FloatType
_FloatType = _FloatType
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatType():
    """dev.ultreon.ubo.types.FloatType"""
 
    @staticmethod
    def _wrap(java_value: _FloatType) -> 'FloatType':
        return FloatType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatType):
        """
        Dynamic initializer for FloatType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.FloatType.writeUso()"""
        return str._wrap(super(FloatType, self).writeUso())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

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
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.FloatType.id()"""
        return int._wrap(super(FloatType, self).id())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.FloatType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_FloatType, self).write(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.FloatType.toString()"""
        return str._wrap(super(FloatType, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.FloatType.hashCode()"""
        return int._wrap(super(FloatType, self).hashCode())

    @override
    @overload
    def getValue(self) -> 'Float':
        """public java.lang.Float dev.ultreon.ubo.types.FloatType.getValue()"""
        return _transform(super(FloatType, self).getValue()).'Float'Value()

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
    def __init__(self, arg0: float):
        """public dev.ultreon.ubo.types.FloatType(float)"""
        val = _FloatType(_float.valueOf(arg0))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.FloatType.equals(java.lang.Object)"""
        return bool._wrap(super(_FloatType, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'FloatType':
        """public static dev.ultreon.ubo.types.FloatType dev.ultreon.ubo.types.FloatType.read(java.io.DataInput) throws java.io.IOException"""
        return FloatType._wrap(_FloatType.read(arg0))

    @overload
    def setValue(self, arg0: 'Float'):
        """public void dev.ultreon.ubo.types.FloatType.setValue(java.lang.Float)"""
        super(_FloatType, self).setValue(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def copy(self) -> 'FloatType':
        """public dev.ultreon.ubo.types.FloatType dev.ultreon.ubo.types.FloatType.copy()"""
        return 'FloatType'._wrap(super(FloatType, self).copy())

 
 
 
# CLASS: dev.ultreon.ubo.types.FloatType 
 
 
# CLASS: dev.ultreon.ubo.types.CharType
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import dev.ultreon.ubo.types.CharType as _CharType
_CharType = _CharType
import java.lang.Integer as _int
import java.lang.Character as _Character
_Character = _Character
import java.io.DataOutput as DataOutput
import java.lang.Character as Character
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharType():
    """dev.ultreon.ubo.types.CharType"""
 
    @staticmethod
    def _wrap(java_value: _CharType) -> 'CharType':
        return CharType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharType):
        """
        Dynamic initializer for CharType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.CharType.hashCode()"""
        return int._wrap(super(CharType, self).hashCode())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.CharType.toString()"""
        return str._wrap(super(CharType, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'CharType':
        """public static dev.ultreon.ubo.types.CharType dev.ultreon.ubo.types.CharType.read(java.io.DataInput) throws java.io.IOException"""
        return CharType._wrap(_CharType.read(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getValue(self) -> 'Character':
        """public java.lang.Character dev.ultreon.ubo.types.CharType.getValue()"""
        return 'Character'._wrap(super(CharType, self).getValue())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.ubo.types.CharType(char)"""
        val = _CharType(_char.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.CharType.equals(java.lang.Object)"""
        return bool._wrap(super(_CharType, self).equals(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.CharType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_CharType, self).write(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setValue(self, arg0: 'Character'):
        """public void dev.ultreon.ubo.types.CharType.setValue(java.lang.Character)"""
        super(_CharType, self).setValue(arg0)

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
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.CharType.id()"""
        return int._wrap(super(CharType, self).id())

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.CharType.writeUso()"""
        return str._wrap(super(CharType, self).writeUso())

    @override
    @overload
    def copy(self) -> 'CharType':
        """public dev.ultreon.ubo.types.CharType dev.ultreon.ubo.types.CharType.copy()"""
        return 'CharType'._wrap(super(CharType, self).copy()) 
 
 
# CLASS: dev.ultreon.ubo.types.DoubleArrayType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
from typing import List
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
import dev.ultreon.ubo.types.DoubleArrayType as _DoubleArrayType
_DoubleArrayType = _DoubleArrayType
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DoubleArrayType():
    """dev.ultreon.ubo.types.DoubleArrayType"""
 
    @staticmethod
    def _wrap(java_value: _DoubleArrayType) -> 'DoubleArrayType':
        return DoubleArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DoubleArrayType):
        """
        Dynamic initializer for DoubleArrayType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DoubleArrayType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DoubleArrayType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.DoubleArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_DoubleArrayType, self).write(arg0)

    @overload
    def __init__(self, arg0: 'double'):
        """public dev.ultreon.ubo.types.DoubleArrayType(double[])"""
        val = _DoubleArrayType(arg0)
        self.__wrapper = val

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.DoubleArrayType.equals(java.lang.Object)"""
        return bool._wrap(super(_DoubleArrayType, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.DoubleArrayType.hashCode()"""
        return int._wrap(super(DoubleArrayType, self).hashCode())

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
    def setValue(self, arg0: 'double'):
        """public void dev.ultreon.ubo.types.DoubleArrayType.setValue(double[])"""
        super(_DoubleArrayType, self).setValue(arg0)

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.DoubleArrayType.size()"""
        return int._wrap(super(DoubleArrayType, self).size())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.DoubleArrayType.toString()"""
        return str._wrap(super(DoubleArrayType, self).toString())

    @override
    @overload
    def copy(self) -> 'DoubleArrayType':
        """public dev.ultreon.ubo.types.DoubleArrayType dev.ultreon.ubo.types.DoubleArrayType.copy()"""
        return 'DoubleArrayType'._wrap(super(DoubleArrayType, self).copy())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'DoubleArrayType':
        """public static dev.ultreon.ubo.types.DoubleArrayType dev.ultreon.ubo.types.DoubleArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return DoubleArrayType._wrap(_DoubleArrayType.read(arg0))

    @override
    @overload
    def getValue(self) -> List[float]:
        """public double[] dev.ultreon.ubo.types.DoubleArrayType.getValue()"""
        return List[float]._wrap(super(DoubleArrayType, self).getValue())

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
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.DoubleArrayType.id()"""
        return int._wrap(super(DoubleArrayType, self).id())

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
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.DoubleArrayType.writeUso()"""
        return str._wrap(super(DoubleArrayType, self).writeUso()) 
 
 
# CLASS: dev.ultreon.ubo.types.FloatArrayType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
from typing import List
import dev.ultreon.ubo.types.FloatArrayType as _FloatArrayType
_FloatArrayType = _FloatArrayType
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatArrayType():
    """dev.ultreon.ubo.types.FloatArrayType"""
 
    @staticmethod
    def _wrap(java_value: _FloatArrayType) -> 'FloatArrayType':
        return FloatArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatArrayType):
        """
        Dynamic initializer for FloatArrayType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatArrayType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatArrayType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getValue(self) -> List[float]:
        """public float[] dev.ultreon.ubo.types.FloatArrayType.getValue()"""
        return List[float]._wrap(super(FloatArrayType, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.FloatArrayType.toString()"""
        return str._wrap(super(FloatArrayType, self).toString())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.FloatArrayType.size()"""
        return int._wrap(super(FloatArrayType, self).size())

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
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.FloatArrayType.hashCode()"""
        return int._wrap(super(FloatArrayType, self).hashCode())

    @overload
    def setValue(self, arg0: 'float'):
        """public void dev.ultreon.ubo.types.FloatArrayType.setValue(float[])"""
        super(_FloatArrayType, self).setValue(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.FloatArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_FloatArrayType, self).write(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.FloatArrayType.equals(java.lang.Object)"""
        return bool._wrap(super(_FloatArrayType, self).equals(arg0))

    @override
    @overload
    def copy(self) -> 'FloatArrayType':
        """public dev.ultreon.ubo.types.FloatArrayType dev.ultreon.ubo.types.FloatArrayType.copy()"""
        return 'FloatArrayType'._wrap(super(FloatArrayType, self).copy())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'FloatArrayType':
        """public static dev.ultreon.ubo.types.FloatArrayType dev.ultreon.ubo.types.FloatArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return FloatArrayType._wrap(_FloatArrayType.read(arg0))

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.FloatArrayType.writeUso()"""
        return str._wrap(super(FloatArrayType, self).writeUso())

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.FloatArrayType.id()"""
        return int._wrap(super(FloatArrayType, self).id())

    @overload
    def __init__(self, arg0: 'float'):
        """public dev.ultreon.ubo.types.FloatArrayType(float[])"""
        val = _FloatArrayType(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.ubo.types.ListType
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import dev.ultreon.ubo.types.ListType as _ListType
_ListType = _ListType
import java.lang.Object as _object
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.List as _List
_List = _List
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import java.util.Iterator as Iterator
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class ListType():
    """dev.ultreon.ubo.types.ListType"""
 
    @staticmethod
    def _wrap(java_value: _ListType) -> 'ListType':
        return ListType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ListType):
        """
        Dynamic initializer for ListType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ListType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ListType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> dev.ultreon.ubo.types.ListType.iterator()"""
        return 'Iterator'._wrap(super(ListType, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.ListType.equals(java.lang.Object)"""
        return bool._wrap(super(_ListType, self).equals(arg0))

    @overload
    def pop(self, arg0: int) -> 'DataType':
        """public T dev.ultreon.ubo.types.ListType.pop(int)"""
        return 'DataType'._wrap(super(_ListType, self).pop(_int.valueOf(arg0)))

    @overload
    def setValue(self, arg0: 'List'):
        """public void dev.ultreon.ubo.types.ListType.setValue(java.util.List<T>)"""
        super(_ListType, self).setValue(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getValue(self) -> 'List':
        """public java.util.List<T> dev.ultreon.ubo.types.ListType.getValue()"""
        return 'List'._wrap(super(ListType, self).getValue())

    @overload
    def remove(self, arg0: int) -> bool:
        """public boolean dev.ultreon.ubo.types.ListType.remove(int)"""
        return bool._wrap(super(_ListType, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.ListType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_ListType, self).write(arg0)

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
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.ubo.types.ListType.isEmpty()"""
        return bool._wrap(super(ListType, self).isEmpty())

    @overload
    def clear(self):
        """public void dev.ultreon.ubo.types.ListType.clear()"""
        super(ListType, self).clear()

    @overload
    def cast(self, *arg0: 'DataType') -> 'ListType':
        """public final <C extends dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.types.ListType<C> dev.ultreon.ubo.types.ListType.cast(C...)"""
        return 'ListType'._wrap(super(_ListType, self).cast(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.ListType.hashCode()"""
        return int._wrap(super(ListType, self).hashCode())

    @overload
    def __init__(self, *arg0: 'DataType'):
        """public dev.ultreon.ubo.types.ListType(T...)"""
        val = _ListType(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ListType.toString()"""
        return str._wrap(super(ListType, self).toString())

    @override
    @overload
    def copy(self) -> 'ListType':
        """public dev.ultreon.ubo.types.ListType<T> dev.ultreon.ubo.types.ListType.copy()"""
        return 'ListType'._wrap(super(ListType, self).copy())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def get(self, arg0: int) -> 'DataType':
        """public T dev.ultreon.ubo.types.ListType.get(int)"""
        return 'DataType'._wrap(super(_ListType, self).get(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'List', *arg1: 'DataType'):
        """public dev.ultreon.ubo.types.ListType(java.util.List<T>,T...)"""
        val = _ListType(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.ListType.id()"""
        return int._wrap(super(ListType, self).id())

    @overload
    def contains(self, arg0: 'DataType') -> bool:
        """public boolean dev.ultreon.ubo.types.ListType.contains(T)"""
        return bool._wrap(super(_ListType, self).contains(arg0))

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ListType.writeUso()"""
        return str._wrap(super(ListType, self).writeUso())

    @overload
    def set(self, arg0: int, arg1: 'DataType') -> 'DataType':
        """public T dev.ultreon.ubo.types.ListType.set(int,T)"""
        return 'DataType'._wrap(super(_ListType, self).set(_int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.ListType(int)"""
        val = _ListType(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def type(self) -> int:
        """public int dev.ultreon.ubo.types.ListType.type()"""
        return int._wrap(super(ListType, self).type())

    @overload
    def add(self, arg0: 'DataType'):
        """public void dev.ultreon.ubo.types.ListType.add(T)"""
        super(_ListType, self).add(arg0)

    @overload
    def remove(self, arg0: 'DataType') -> 'DataType':
        """public T dev.ultreon.ubo.types.ListType.remove(T)"""
        return 'DataType'._wrap(super(_ListType, self).remove(arg0))

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'ListType':
        """public static dev.ultreon.ubo.types.ListType<?> dev.ultreon.ubo.types.ListType.read(java.io.DataInput) throws java.io.IOException"""
        return ListType._wrap(_ListType.read(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.ListType.size()"""
        return int._wrap(super(ListType, self).size())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: dev.ultreon.ubo.types.ShortArrayType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
from typing import List
import dev.ultreon.ubo.types.ShortArrayType as _ShortArrayType
_ShortArrayType = _ShortArrayType
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShortArrayType():
    """dev.ultreon.ubo.types.ShortArrayType"""
 
    @staticmethod
    def _wrap(java_value: _ShortArrayType) -> 'ShortArrayType':
        return ShortArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShortArrayType):
        """
        Dynamic initializer for ShortArrayType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShortArrayType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShortArrayType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ShortArrayType.writeUso()"""
        return str._wrap(super(ShortArrayType, self).writeUso())

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.ShortArrayType.id()"""
        return int._wrap(super(ShortArrayType, self).id())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.ShortArrayType.hashCode()"""
        return int._wrap(super(ShortArrayType, self).hashCode())

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
    def __init__(self, arg0: 'short'):
        """public dev.ultreon.ubo.types.ShortArrayType(short[])"""
        val = _ShortArrayType(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> List[int]:
        """public short[] dev.ultreon.ubo.types.ShortArrayType.getValue()"""
        return List[int]._wrap(super(ShortArrayType, self).getValue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def copy(self) -> 'ShortArrayType':
        """public dev.ultreon.ubo.types.ShortArrayType dev.ultreon.ubo.types.ShortArrayType.copy()"""
        return 'ShortArrayType'._wrap(super(ShortArrayType, self).copy())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.ShortArrayType.size()"""
        return int._wrap(super(ShortArrayType, self).size())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'ShortArrayType':
        """public static dev.ultreon.ubo.types.ShortArrayType dev.ultreon.ubo.types.ShortArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return ShortArrayType._wrap(_ShortArrayType.read(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.ShortArrayType.equals(java.lang.Object)"""
        return bool._wrap(super(_ShortArrayType, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ShortArrayType.toString()"""
        return str._wrap(super(ShortArrayType, self).toString())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.ShortArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_ShortArrayType, self).write(arg0)

    @overload
    def setValue(self, arg0: 'short'):
        """public void dev.ultreon.ubo.types.ShortArrayType.setValue(short[])"""
        super(_ShortArrayType, self).setValue(arg0) 
 
 
# CLASS: dev.ultreon.ubo.types.IntType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import java.lang.Integer as _int
import dev.ultreon.ubo.types.IntType as _IntType
_IntType = _IntType
import java.io.DataOutput as DataOutput
import java.lang.Integer as Integer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntType():
    """dev.ultreon.ubo.types.IntType"""
 
    @staticmethod
    def _wrap(java_value: _IntType) -> 'IntType':
        return IntType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntType):
        """
        Dynamic initializer for IntType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'IntType':
        """public static dev.ultreon.ubo.types.IntType dev.ultreon.ubo.types.IntType.read(java.io.DataInput) throws java.io.IOException"""
        return IntType._wrap(_IntType.read(arg0))

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.IntType.id()"""
        return int._wrap(super(IntType, self).id())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getValue(self) -> 'Integer':
        """public java.lang.Integer dev.ultreon.ubo.types.IntType.getValue()"""
        return _transform(super(IntType, self).getValue()).'Integer'Value()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.IntType.hashCode()"""
        return int._wrap(super(IntType, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.IntType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_IntType, self).write(arg0)

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.IntType(int)"""
        val = _IntType(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'IntType':
        """public dev.ultreon.ubo.types.IntType dev.ultreon.ubo.types.IntType.copy()"""
        return 'IntType'._wrap(super(IntType, self).copy())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.IntType.equals(java.lang.Object)"""
        return bool._wrap(super(_IntType, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.IntType.toString()"""
        return str._wrap(super(IntType, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setValue(self, arg0: 'Integer'):
        """public void dev.ultreon.ubo.types.IntType.setValue(java.lang.Integer)"""
        super(_IntType, self).setValue(arg0)

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.IntType.writeUso()"""
        return str._wrap(super(IntType, self).writeUso()) 
 
 
# CLASS: dev.ultreon.ubo.types.CharArrayType
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.ubo.types.CharArrayType as _CharArrayType
_CharArrayType = _CharArrayType
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
from typing import List
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharArrayType():
    """dev.ultreon.ubo.types.CharArrayType"""
 
    @staticmethod
    def _wrap(java_value: _CharArrayType) -> 'CharArrayType':
        return CharArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharArrayType):
        """
        Dynamic initializer for CharArrayType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharArrayType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharArrayType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @overload
    def __init__(self, arg0: 'char'):
        """public dev.ultreon.ubo.types.CharArrayType(char[])"""
        val = _CharArrayType(arg0)
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

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.CharArrayType.size()"""
        return int._wrap(super(CharArrayType, self).size())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.CharArrayType.hashCode()"""
        return int._wrap(super(CharArrayType, self).hashCode())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'CharArrayType':
        """public static dev.ultreon.ubo.types.CharArrayType dev.ultreon.ubo.types.CharArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return CharArrayType._wrap(_CharArrayType.read(arg0))

    @override
    @overload
    def copy(self) -> 'CharArrayType':
        """public dev.ultreon.ubo.types.CharArrayType dev.ultreon.ubo.types.CharArrayType.copy()"""
        return 'CharArrayType'._wrap(super(CharArrayType, self).copy())

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
    def getValue(self) -> List[str]:
        """public char[] dev.ultreon.ubo.types.CharArrayType.getValue()"""
        return List[str]._wrap(super(CharArrayType, self).getValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.CharArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_CharArrayType, self).write(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.CharArrayType.toString()"""
        return str._wrap(super(CharArrayType, self).toString())

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.CharArrayType.id()"""
        return int._wrap(super(CharArrayType, self).id())

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.CharArrayType.writeUso()"""
        return str._wrap(super(CharArrayType, self).writeUso())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.CharArrayType.equals(java.lang.Object)"""
        return bool._wrap(super(_CharArrayType, self).equals(arg0))

    @overload
    def setValue(self, arg0: 'char'):
        """public void dev.ultreon.ubo.types.CharArrayType.setValue(char[])"""
        super(_CharArrayType, self).setValue(arg0) 
 
 
# CLASS: dev.ultreon.ubo.types.LongArrayType
from pyquantum_helper import import_once as _import_once
import dev.ultreon.ubo.types.LongArrayType as _LongArrayType
_LongArrayType = _LongArrayType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
from typing import List
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LongArrayType():
    """dev.ultreon.ubo.types.LongArrayType"""
 
    @staticmethod
    def _wrap(java_value: _LongArrayType) -> 'LongArrayType':
        return LongArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongArrayType):
        """
        Dynamic initializer for LongArrayType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongArrayType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongArrayType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.LongArrayType.id()"""
        return int._wrap(super(LongArrayType, self).id())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.LongArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_LongArrayType, self).write(arg0)

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @override
    @overload
    def copy(self) -> 'LongArrayType':
        """public dev.ultreon.ubo.types.LongArrayType dev.ultreon.ubo.types.LongArrayType.copy()"""
        return 'LongArrayType'._wrap(super(LongArrayType, self).copy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getValue(self) -> List[int]:
        """public long[] dev.ultreon.ubo.types.LongArrayType.getValue()"""
        return List[int]._wrap(super(LongArrayType, self).getValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setValue(self, arg0: 'long'):
        """public void dev.ultreon.ubo.types.LongArrayType.setValue(long[])"""
        super(_LongArrayType, self).setValue(arg0)

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.LongArrayType.writeUso()"""
        return str._wrap(super(LongArrayType, self).writeUso())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.LongArrayType.equals(java.lang.Object)"""
        return bool._wrap(super(_LongArrayType, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.LongArrayType.hashCode()"""
        return int._wrap(super(LongArrayType, self).hashCode())

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
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.LongArrayType.size()"""
        return int._wrap(super(LongArrayType, self).size())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'LongArrayType':
        """public static dev.ultreon.ubo.types.LongArrayType dev.ultreon.ubo.types.LongArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return LongArrayType._wrap(_LongArrayType.read(arg0))

    @overload
    def __init__(self, arg0: 'long'):
        """public dev.ultreon.ubo.types.LongArrayType(long[])"""
        val = _LongArrayType(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.LongArrayType.toString()"""
        return str._wrap(super(LongArrayType, self).toString()) 
 
 
# CLASS: dev.ultreon.ubo.types.BigIntType
from pyquantum_helper import import_once as _import_once
import dev.ultreon.ubo.types.BigIntType as _BigIntType
_BigIntType = _BigIntType
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import java.lang.String as _string
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BigIntType():
    """dev.ultreon.ubo.types.BigIntType"""
 
    @staticmethod
    def _wrap(java_value: _BigIntType) -> 'BigIntType':
        return BigIntType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BigIntType):
        """
        Dynamic initializer for BigIntType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BigIntType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BigIntType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setValue(self, arg0: 'BigInteger'):
        """public void dev.ultreon.ubo.types.BigIntType.setValue(java.math.BigInteger)"""
        super(_BigIntType, self).setValue(arg0)

    @overload
    def __init__(self, arg0: 'BigInteger'):
        """public dev.ultreon.ubo.types.BigIntType(java.math.BigInteger)"""
        val = _BigIntType(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'BigIntType':
        """public static dev.ultreon.ubo.types.BigIntType dev.ultreon.ubo.types.BigIntType.read(java.io.DataInput) throws java.io.IOException"""
        return BigIntType._wrap(_BigIntType.read(arg0))

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

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
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.BigIntType.id()"""
        return int._wrap(super(BigIntType, self).id())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.BigIntType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_BigIntType, self).write(arg0)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.ubo.types.BigIntType(java.lang.String)"""
        val = _BigIntType(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.BigIntType.hashCode()"""
        return int._wrap(super(BigIntType, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BigIntType.writeUso()"""
        return str._wrap(super(BigIntType, self).writeUso())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BigIntType.toString()"""
        return str._wrap(super(BigIntType, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.BigIntType.equals(java.lang.Object)"""
        return bool._wrap(super(_BigIntType, self).equals(arg0))

    @override
    @overload
    def getValue(self) -> 'BigInteger':
        """public java.math.BigInteger dev.ultreon.ubo.types.BigIntType.getValue()"""
        return _transform(super(BigIntType, self).getValue()).'BigInteger'Value()

    @override
    @overload
    def copy(self) -> 'BigIntType':
        """public dev.ultreon.ubo.types.BigIntType dev.ultreon.ubo.types.BigIntType.copy()"""
        return 'BigIntType'._wrap(super(BigIntType, self).copy())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.ubo.types.ByteArrayType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.nio.charset.Charset as Charset
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import java.lang.Byte as Byte
import dev.ultreon.ubo.types.ByteArrayType as _ByteArrayType
_ByteArrayType = _ByteArrayType
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ByteArrayType():
    """dev.ultreon.ubo.types.ByteArrayType"""
 
    @staticmethod
    def _wrap(java_value: _ByteArrayType) -> 'ByteArrayType':
        return ByteArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ByteArrayType):
        """
        Dynamic initializer for ByteArrayType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ByteArrayType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ByteArrayType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ByteArrayType.writeUso()"""
        return str._wrap(super(ByteArrayType, self).writeUso())

    @override
    @overload
    def copy(self) -> 'ByteArrayType':
        """public dev.ultreon.ubo.types.ByteArrayType dev.ultreon.ubo.types.ByteArrayType.copy()"""
        return 'ByteArrayType'._wrap(super(ByteArrayType, self).copy())

    @overload
    def __init__(self, arg0: str, arg1: 'Charset'):
        """public dev.ultreon.ubo.types.ByteArrayType(java.lang.String,java.nio.charset.Charset)"""
        val = _ByteArrayType(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getValue(self) -> List[int]:
        """public byte[] dev.ultreon.ubo.types.ByteArrayType.getValue()"""
        return List[int]._wrap(super(ByteArrayType, self).getValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.ByteArrayType(int)"""
        val = _ByteArrayType(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.ByteArrayType.size()"""
        return int._wrap(super(ByteArrayType, self).size())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.ByteArrayType.hashCode()"""
        return int._wrap(super(ByteArrayType, self).hashCode())

    @overload
    def __init__(self, arg0: 'Byte'):
        """public dev.ultreon.ubo.types.ByteArrayType(java.lang.Byte[])"""
        val = _ByteArrayType(arg0)
        self.__wrapper = val

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setValue(self, arg0: bytes):
        """public void dev.ultreon.ubo.types.ByteArrayType.setValue(byte[])"""
        super(_ByteArrayType, self).setValue(bytes)

    @overload
    def __init__(self, arg0: bytes):
        """public dev.ultreon.ubo.types.ByteArrayType(byte[])"""
        val = _ByteArrayType(bytes)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.ByteArrayType.equals(java.lang.Object)"""
        return bool._wrap(super(_ByteArrayType, self).equals(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.ByteArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_ByteArrayType, self).write(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ByteArrayType.toString()"""
        return str._wrap(super(ByteArrayType, self).toString())

    @overload
    def __init__(self, arg0: bytes, arg1: int):
        """public dev.ultreon.ubo.types.ByteArrayType(byte[],int)"""
        val = _ByteArrayType(bytes, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.ubo.types.ByteArrayType(java.lang.String)"""
        val = _ByteArrayType(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.ByteArrayType.id()"""
        return int._wrap(super(ByteArrayType, self).id())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'ByteArrayType':
        """public static dev.ultreon.ubo.types.ByteArrayType dev.ultreon.ubo.types.ByteArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return ByteArrayType._wrap(_ByteArrayType.read(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public dev.ultreon.ubo.types.ByteArrayType(java.nio.ByteBuffer)"""
        val = _ByteArrayType(arg0)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.ubo.types.LongType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Long as Long
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import dev.ultreon.ubo.types.LongType as _LongType
_LongType = _LongType
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LongType():
    """dev.ultreon.ubo.types.LongType"""
 
    @staticmethod
    def _wrap(java_value: _LongType) -> 'LongType':
        return LongType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongType):
        """
        Dynamic initializer for LongType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.LongType.toString()"""
        return str._wrap(super(LongType, self).toString())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'LongType':
        """public static dev.ultreon.ubo.types.LongType dev.ultreon.ubo.types.LongType.read(java.io.DataInput) throws java.io.IOException"""
        return LongType._wrap(_LongType.read(arg0))

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @overload
    def setValue(self, arg0: 'Long'):
        """public void dev.ultreon.ubo.types.LongType.setValue(java.lang.Long)"""
        super(_LongType, self).setValue(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.LongType.hashCode()"""
        return int._wrap(super(LongType, self).hashCode())

    @override
    @overload
    def getValue(self) -> 'Long':
        """public java.lang.Long dev.ultreon.ubo.types.LongType.getValue()"""
        return _transform(super(LongType, self).getValue()).'Long'Value()

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
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.LongType.writeUso()"""
        return str._wrap(super(LongType, self).writeUso())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def copy(self) -> 'LongType':
        """public dev.ultreon.ubo.types.LongType dev.ultreon.ubo.types.LongType.copy()"""
        return 'LongType'._wrap(super(LongType, self).copy())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.LongType.equals(java.lang.Object)"""
        return bool._wrap(super(_LongType, self).equals(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.LongType(long)"""
        val = _LongType(_long.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.LongType.id()"""
        return int._wrap(super(LongType, self).id())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.LongType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_LongType, self).write(arg0) 
 
 
# CLASS: dev.ultreon.ubo.types.MapType
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.lang.Short as _short
import java.util.Set as _Set
_Set = _Set
import java.util.BitSet as BitSet
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
from builtins import bool
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _object
import dev.ultreon.ubo.types.ListType as _ListType
_ListType = _ListType
from builtins import float
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import java.util.BitSet as _BitSet
_BitSet = _BitSet
from typing import List
import java.lang.Float as _float
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.util.Set as Set
import java.math.BigInteger as BigInteger
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
import java.math.BigDecimal as BigDecimal
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
 
class MapType():
    """dev.ultreon.ubo.types.MapType"""
 
    @staticmethod
    def _wrap(java_value: _MapType) -> 'MapType':
        return MapType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapType):
        """
        Dynamic initializer for MapType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getFloat(self, arg0: str) -> float:
        """public float dev.ultreon.ubo.types.MapType.getFloat(java.lang.String)"""
        return float._wrap(super(_MapType, self).getFloat(arg0))

    @overload
    def getInt(self, arg0: str, arg1: int) -> int:
        """public int dev.ultreon.ubo.types.MapType.getInt(java.lang.String,int)"""
        return int._wrap(super(_MapType, self).getInt(arg0, _int.valueOf(arg1)))

    @overload
    def getByte(self, arg0: str, arg1: int) -> int:
        """public byte dev.ultreon.ubo.types.MapType.getByte(java.lang.String,byte)"""
        return int._wrap(super(_MapType, self).getByte(arg0, _byte.valueOf(arg1)))

    @overload
    def putByte(self, arg0: str, arg1: int):
        """public void dev.ultreon.ubo.types.MapType.putByte(java.lang.String,byte)"""
        super(_MapType, self).putByte(arg0, _byte.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def putCharArray(self, arg0: str, arg1: 'char'):
        """public void dev.ultreon.ubo.types.MapType.putCharArray(java.lang.String,char[])"""
        super(_MapType, self).putCharArray(arg0, arg1)

    @overload
    def putFloatArray(self, arg0: str, arg1: 'float'):
        """public void dev.ultreon.ubo.types.MapType.putFloatArray(java.lang.String,float[])"""
        super(_MapType, self).putFloatArray(arg0, arg1)

    @overload
    def getShort(self, arg0: str, arg1: int) -> int:
        """public short dev.ultreon.ubo.types.MapType.getShort(java.lang.String,short)"""
        return int._wrap(super(_MapType, self).getShort(arg0, _short.valueOf(arg1)))

    @overload
    def getLong(self, arg0: str) -> int:
        """public long dev.ultreon.ubo.types.MapType.getLong(java.lang.String)"""
        return int._wrap(super(_MapType, self).getLong(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.MapType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_MapType, self).write(arg0)

    @overload
    def putByteArray(self, arg0: str, arg1: bytes):
        """public void dev.ultreon.ubo.types.MapType.putByteArray(java.lang.String,byte[])"""
        super(_MapType, self).putByteArray(arg0, bytes)

    @overload
    def getDoubleArray(self, arg0: str) -> List[float]:
        """public double[] dev.ultreon.ubo.types.MapType.getDoubleArray(java.lang.String)"""
        return List[float]._wrap(super(_MapType, self).getDoubleArray(arg0))

    @overload
    def putBigDec(self, arg0: str, arg1: 'BigDecimal'):
        """public void dev.ultreon.ubo.types.MapType.putBigDec(java.lang.String,java.math.BigDecimal)"""
        super(_MapType, self).putBigDec(arg0, arg1)

    @overload
    def getList(self, arg0: str, *arg1: 'DataType') -> 'ListType':
        """public final <T extends dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.types.ListType<T> dev.ultreon.ubo.types.MapType.getList(java.lang.String,T...)"""
        return 'ListType'._wrap(super(_MapType, self).getList(arg0, arg1))

    @overload
    def getChar(self, arg0: str, arg1: str) -> str:
        """public char dev.ultreon.ubo.types.MapType.getChar(java.lang.String,char)"""
        return str._wrap(super(_MapType, self).getChar(arg0, _char.valueOf(arg1)))

    @overload
    def putLong(self, arg0: str, arg1: int):
        """public void dev.ultreon.ubo.types.MapType.putLong(java.lang.String,long)"""
        super(_MapType, self).putLong(arg0, _long.valueOf(arg1))

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.MapType.writeUso()"""
        return str._wrap(super(MapType, self).writeUso())

    @overload
    def putIntArray(self, arg0: str, arg1: 'int'):
        """public void dev.ultreon.ubo.types.MapType.putIntArray(java.lang.String,int[])"""
        super(_MapType, self).putIntArray(arg0, arg1)

    @overload
    def putInt(self, arg0: str, arg1: int):
        """public void dev.ultreon.ubo.types.MapType.putInt(java.lang.String,int)"""
        super(_MapType, self).putInt(arg0, _int.valueOf(arg1))

    @overload
    def keys(self) -> 'Set':
        """public java.util.Set<java.lang.String> dev.ultreon.ubo.types.MapType.keys()"""
        return 'Set'._wrap(super(MapType, self).keys())

    @overload
    def getUUID(self, arg0: str, arg1: 'UUID') -> 'UUID':
        """public java.util.UUID dev.ultreon.ubo.types.MapType.getUUID(java.lang.String,java.util.UUID)"""
        return 'UUID'._wrap(super(_MapType, self).getUUID(arg0, arg1))

    @override
    @overload
    def copy(self) -> 'MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.ubo.types.MapType.copy()"""
        return 'MapType'._wrap(super(MapType, self).copy())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: str, *arg1: 'DataType') -> bool:
        """public final <T extends dev.ultreon.ubo.types.DataType<?>> boolean dev.ultreon.ubo.types.MapType.contains(java.lang.String,T...)"""
        return bool._wrap(super(_MapType, self).contains(arg0, arg1))

    @overload
    def putBigInt(self, arg0: str, arg1: 'BigInteger'):
        """public void dev.ultreon.ubo.types.MapType.putBigInt(java.lang.String,java.math.BigInteger)"""
        super(_MapType, self).putBigInt(arg0, arg1)

    @overload
    def remove(self, arg0: str) -> bool:
        """public boolean dev.ultreon.ubo.types.MapType.remove(java.lang.String)"""
        return bool._wrap(super(_MapType, self).remove(arg0))

    @overload
    def getCharArray(self, arg0: str) -> List[str]:
        """public char[] dev.ultreon.ubo.types.MapType.getCharArray(java.lang.String)"""
        return List[str]._wrap(super(_MapType, self).getCharArray(arg0))

    @overload
    def putUUID(self, arg0: str, arg1: 'UUID'):
        """public void dev.ultreon.ubo.types.MapType.putUUID(java.lang.String,java.util.UUID)"""
        super(_MapType, self).putUUID(arg0, arg1)

    @overload
    def getInt(self, arg0: str) -> int:
        """public int dev.ultreon.ubo.types.MapType.getInt(java.lang.String)"""
        return int._wrap(super(_MapType, self).getInt(arg0))

    @overload
    def setValue(self, arg0: 'Map'):
        """public void dev.ultreon.ubo.types.MapType.setValue(java.util.Map<java.lang.String, dev.ultreon.ubo.types.DataType<?>>)"""
        super(_MapType, self).setValue(arg0)

    @overload
    def getString(self, arg0: str, arg1: str) -> str:
        """public java.lang.String dev.ultreon.ubo.types.MapType.getString(java.lang.String,java.lang.String)"""
        return str._wrap(super(_MapType, self).getString(arg0, arg1))

    @overload
    def putBitSet(self, arg0: str, arg1: 'BitSet'):
        """public void dev.ultreon.ubo.types.MapType.putBitSet(java.lang.String,java.util.BitSet)"""
        super(_MapType, self).putBitSet(arg0, arg1)

    @overload
    def pop(self, arg0: str) -> 'DataType':
        """public dev.ultreon.ubo.types.DataType<?> dev.ultreon.ubo.types.MapType.pop(java.lang.String)"""
        return 'DataType'._wrap(super(_MapType, self).pop(arg0))

    @overload
    def putShortArray(self, arg0: str, arg1: 'short'):
        """public void dev.ultreon.ubo.types.MapType.putShortArray(java.lang.String,short[])"""
        super(_MapType, self).putShortArray(arg0, arg1)

    @overload
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.MapType.size()"""
        return int._wrap(super(MapType, self).size())

    @overload
    def __init__(self, ):
        """public dev.ultreon.ubo.types.MapType()"""
        val = _MapType()
        self.__wrapper = val

    @overload
    def put(self, arg0: str, arg1: 'DataType'):
        """public void dev.ultreon.ubo.types.MapType.put(java.lang.String,dev.ultreon.ubo.types.DataType<?>)"""
        super(_MapType, self).put(arg0, arg1)

    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.ubo.types.MapType.isEmpty()"""
        return bool._wrap(super(MapType, self).isEmpty())

    @overload
    def putBitSet(self, arg0: str, arg1: bytes):
        """public void dev.ultreon.ubo.types.MapType.putBitSet(java.lang.String,byte[])"""
        super(_MapType, self).putBitSet(arg0, bytes)

    @overload
    def getBoolean(self, arg0: str) -> bool:
        """public boolean dev.ultreon.ubo.types.MapType.getBoolean(java.lang.String)"""
        return bool._wrap(super(_MapType, self).getBoolean(arg0))

    @overload
    def getByteArray(self, arg0: str, arg1: bytes) -> List[int]:
        """public byte[] dev.ultreon.ubo.types.MapType.getByteArray(java.lang.String,byte[])"""
        return List[int]._wrap(super(_MapType, self).getByteArray(arg0, bytes))

    @overload
    def getBigInt(self, arg0: str, arg1: 'BigInteger') -> 'BigInteger':
        """public java.math.BigInteger dev.ultreon.ubo.types.MapType.getBigInt(java.lang.String,java.math.BigInteger)"""
        return _transform(super(_MapType, self).getBigInt(arg0, arg1)).'BigInteger'Value()

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @overload
    def get(self, arg0: str) -> 'DataType':
        """public dev.ultreon.ubo.types.DataType<?> dev.ultreon.ubo.types.MapType.get(java.lang.String)"""
        return 'DataType'._wrap(super(_MapType, self).get(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.ubo.types.MapType()"""
        val = _MapType()
        self.__wrapper = val

    @overload
    def getLongArray(self, arg0: str) -> List[int]:
        """public long[] dev.ultreon.ubo.types.MapType.getLongArray(java.lang.String)"""
        return List[int]._wrap(super(_MapType, self).getLongArray(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getBitSet(self, arg0: str, arg1: 'BitSet') -> 'BitSet':
        """public java.util.BitSet dev.ultreon.ubo.types.MapType.getBitSet(java.lang.String,java.util.BitSet)"""
        return 'BitSet'._wrap(super(_MapType, self).getBitSet(arg0, arg1))

    @overload
    def getMap(self, arg0: str) -> 'MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.ubo.types.MapType.getMap(java.lang.String)"""
        return 'MapType'._wrap(super(_MapType, self).getMap(arg0))

    @overload
    def putLongArray(self, arg0: str, arg1: 'long'):
        """public void dev.ultreon.ubo.types.MapType.putLongArray(java.lang.String,long[])"""
        super(_MapType, self).putLongArray(arg0, arg1)

    @overload
    def getString(self, arg0: str) -> str:
        """public java.lang.String dev.ultreon.ubo.types.MapType.getString(java.lang.String)"""
        return str._wrap(super(_MapType, self).getString(arg0))

    @overload
    def getUUID(self, arg0: str) -> 'UUID':
        """public java.util.UUID dev.ultreon.ubo.types.MapType.getUUID(java.lang.String)"""
        return 'UUID'._wrap(super(_MapType, self).getUUID(arg0))

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.MapType.id()"""
        return int._wrap(super(MapType, self).id())

    @overload
    def getLong(self, arg0: str, arg1: int) -> int:
        """public long dev.ultreon.ubo.types.MapType.getLong(java.lang.String,long)"""
        return int._wrap(super(_MapType, self).getLong(arg0, _long.valueOf(arg1)))

    @overload
    def contains(self, arg0: str, arg1: int) -> bool:
        """public boolean dev.ultreon.ubo.types.MapType.contains(java.lang.String,int)"""
        return bool._wrap(super(_MapType, self).contains(arg0, _int.valueOf(arg1)))

    @overload
    def putChar(self, arg0: str, arg1: str):
        """public void dev.ultreon.ubo.types.MapType.putChar(java.lang.String,char)"""
        super(_MapType, self).putChar(arg0, _char.valueOf(arg1))

    @overload
    def getDoubleArray(self, arg0: str, arg1: 'double') -> List[float]:
        """public double[] dev.ultreon.ubo.types.MapType.getDoubleArray(java.lang.String,double[])"""
        return List[float]._wrap(super(_MapType, self).getDoubleArray(arg0, arg1))

    @overload
    def getBitSet(self, arg0: str) -> 'BitSet':
        """public java.util.BitSet dev.ultreon.ubo.types.MapType.getBitSet(java.lang.String)"""
        return 'BitSet'._wrap(super(_MapType, self).getBitSet(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def putByte(self, arg0: str, arg1: int):
        """public void dev.ultreon.ubo.types.MapType.putByte(java.lang.String,int)"""
        super(_MapType, self).putByte(arg0, _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.MapType.toString()"""
        return str._wrap(super(MapType, self).toString())

    @overload
    def getFloatArray(self, arg0: str) -> List[float]:
        """public float[] dev.ultreon.ubo.types.MapType.getFloatArray(java.lang.String)"""
        return List[float]._wrap(super(_MapType, self).getFloatArray(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getChar(self, arg0: str) -> str:
        """public char dev.ultreon.ubo.types.MapType.getChar(java.lang.String)"""
        return str._wrap(super(_MapType, self).getChar(arg0))

    @overload
    def getList(self, arg0: str, arg1: 'ListType') -> 'ListType':
        """public <T extends dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.types.ListType<T> dev.ultreon.ubo.types.MapType.getList(java.lang.String,dev.ultreon.ubo.types.ListType<T>)"""
        return 'ListType'._wrap(super(_MapType, self).getList(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Map'):
        """public dev.ultreon.ubo.types.MapType(java.util.Map<java.lang.String, dev.ultreon.ubo.types.DataType<?>>)"""
        val = _MapType(arg0)
        self.__wrapper = val

    @overload
    def getIntArray(self, arg0: str) -> List[int]:
        """public int[] dev.ultreon.ubo.types.MapType.getIntArray(java.lang.String)"""
        return List[int]._wrap(super(_MapType, self).getIntArray(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.MapType.equals(java.lang.Object)"""
        return bool._wrap(super(_MapType, self).equals(arg0))

    @overload
    def getMap(self, arg0: str, arg1: 'MapType') -> 'MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.ubo.types.MapType.getMap(java.lang.String,dev.ultreon.ubo.types.MapType)"""
        return 'MapType'._wrap(super(_MapType, self).getMap(arg0, arg1))

    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<java.lang.String, dev.ultreon.ubo.types.DataType<?>>> dev.ultreon.ubo.types.MapType.entries()"""
        return 'Set'._wrap(super(MapType, self).entries())

    @override
    @overload
    def getValue(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.types.MapType.getValue()"""
        return 'Map'._wrap(super(MapType, self).getValue())

    @overload
    def putFloat(self, arg0: str, arg1: float):
        """public void dev.ultreon.ubo.types.MapType.putFloat(java.lang.String,float)"""
        super(_MapType, self).putFloat(arg0, _float.valueOf(arg1))

    @overload
    def putDouble(self, arg0: str, arg1: float):
        """public void dev.ultreon.ubo.types.MapType.putDouble(java.lang.String,double)"""
        super(_MapType, self).putDouble(arg0, _double.valueOf(arg1))

    @overload
    def putShort(self, arg0: str, arg1: int):
        """public void dev.ultreon.ubo.types.MapType.putShort(java.lang.String,int)"""
        super(_MapType, self).putShort(arg0, _int.valueOf(arg1))

    @overload
    def getDouble(self, arg0: str, arg1: float) -> float:
        """public double dev.ultreon.ubo.types.MapType.getDouble(java.lang.String,double)"""
        return float._wrap(super(_MapType, self).getDouble(arg0, _double.valueOf(arg1)))

    @overload
    def getBoolean(self, arg0: str, arg1: bool) -> bool:
        """public boolean dev.ultreon.ubo.types.MapType.getBoolean(java.lang.String,boolean)"""
        return bool._wrap(super(_MapType, self).getBoolean(arg0, _boolean.valueOf(arg1)))

    @overload
    def putString(self, arg0: str, arg1: str):
        """public void dev.ultreon.ubo.types.MapType.putString(java.lang.String,java.lang.String)"""
        super(_MapType, self).putString(arg0, arg1)

    @overload
    def __init__(self, arg0: str, arg1: 'DataType'):
        """public dev.ultreon.ubo.types.MapType(java.lang.String,dev.ultreon.ubo.types.DataType<?>)"""
        val = _MapType(arg0, arg1)
        self.__wrapper = val

    @overload
    def getShortArray(self, arg0: str) -> List[int]:
        """public short[] dev.ultreon.ubo.types.MapType.getShortArray(java.lang.String)"""
        return List[int]._wrap(super(_MapType, self).getShortArray(arg0))

    @overload
    def getDouble(self, arg0: str) -> float:
        """public double dev.ultreon.ubo.types.MapType.getDouble(java.lang.String)"""
        return float._wrap(super(_MapType, self).getDouble(arg0))

    @overload
    def getShortArray(self, arg0: str, arg1: 'short') -> List[int]:
        """public short[] dev.ultreon.ubo.types.MapType.getShortArray(java.lang.String,short[])"""
        return List[int]._wrap(super(_MapType, self).getShortArray(arg0, arg1))

    @overload
    def putShort(self, arg0: str, arg1: int):
        """public void dev.ultreon.ubo.types.MapType.putShort(java.lang.String,short)"""
        super(_MapType, self).putShort(arg0, _short.valueOf(arg1))

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'MapType':
        """public static dev.ultreon.ubo.types.MapType dev.ultreon.ubo.types.MapType.read(java.io.DataInput) throws java.io.IOException"""
        return MapType._wrap(_MapType.read(arg0))

    @overload
    def putDoubleArray(self, arg0: str, arg1: 'double'):
        """public void dev.ultreon.ubo.types.MapType.putDoubleArray(java.lang.String,double[])"""
        super(_MapType, self).putDoubleArray(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.MapType.hashCode()"""
        return int._wrap(super(MapType, self).hashCode())

    @overload
    def getFloatArray(self, arg0: str, arg1: 'float') -> List[float]:
        """public float[] dev.ultreon.ubo.types.MapType.getFloatArray(java.lang.String,float[])"""
        return List[float]._wrap(super(_MapType, self).getFloatArray(arg0, arg1))

    @overload
    def getFloat(self, arg0: str, arg1: float) -> float:
        """public float dev.ultreon.ubo.types.MapType.getFloat(java.lang.String,float)"""
        return float._wrap(super(_MapType, self).getFloat(arg0, _float.valueOf(arg1)))

    @overload
    def getCharArray(self, arg0: str, arg1: 'char') -> List[str]:
        """public char[] dev.ultreon.ubo.types.MapType.getCharArray(java.lang.String,char[])"""
        return List[str]._wrap(super(_MapType, self).getCharArray(arg0, arg1))

    @overload
    def getBigInt(self, arg0: str) -> 'BigInteger':
        """public java.math.BigInteger dev.ultreon.ubo.types.MapType.getBigInt(java.lang.String)"""
        return _transform(super(_MapType, self).getBigInt(arg0)).'BigInteger'Value()

    @overload
    def clear(self):
        """public void dev.ultreon.ubo.types.MapType.clear()"""
        super(MapType, self).clear()

    @overload
    def getBigDec(self, arg0: str, arg1: 'BigDecimal') -> 'BigDecimal':
        """public java.math.BigDecimal dev.ultreon.ubo.types.MapType.getBigDec(java.lang.String,java.math.BigDecimal)"""
        return _transform(super(_MapType, self).getBigDec(arg0, arg1)).'BigDecimal'Value()

    @overload
    def putBoolean(self, arg0: str, arg1: bool):
        """public void dev.ultreon.ubo.types.MapType.putBoolean(java.lang.String,boolean)"""
        super(_MapType, self).putBoolean(arg0, _boolean.valueOf(arg1))

    @overload
    def getIntArray(self, arg0: str, arg1: 'int') -> List[int]:
        """public int[] dev.ultreon.ubo.types.MapType.getIntArray(java.lang.String,int[])"""
        return List[int]._wrap(super(_MapType, self).getIntArray(arg0, arg1))

    @overload
    def getLongArray(self, arg0: str, arg1: 'long') -> List[int]:
        """public long[] dev.ultreon.ubo.types.MapType.getLongArray(java.lang.String,long[])"""
        return List[int]._wrap(super(_MapType, self).getLongArray(arg0, arg1))

    @overload
    def getBigDec(self, arg0: str) -> 'BigDecimal':
        """public java.math.BigDecimal dev.ultreon.ubo.types.MapType.getBigDec(java.lang.String)"""
        return _transform(super(_MapType, self).getBigDec(arg0)).'BigDecimal'Value()

    @overload
    def getByte(self, arg0: str) -> int:
        """public byte dev.ultreon.ubo.types.MapType.getByte(java.lang.String)"""
        return int._wrap(super(_MapType, self).getByte(arg0))

    @overload
    def getShort(self, arg0: str) -> int:
        """public short dev.ultreon.ubo.types.MapType.getShort(java.lang.String)"""
        return int._wrap(super(_MapType, self).getShort(arg0))

    @overload
    def getByteArray(self, arg0: str) -> List[int]:
        """public byte[] dev.ultreon.ubo.types.MapType.getByteArray(java.lang.String)"""
        return List[int]._wrap(super(_MapType, self).getByteArray(arg0))

    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.types.MapType.values()"""
        return 'Collection'._wrap(super(MapType, self).values()) 
 
 
# CLASS: dev.ultreon.ubo.types.DataType
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
import java.io.DataOutput as DataOutput
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

from abc import abstractmethod, ABC
from builtins import object
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
 
class DataType():
    """dev.ultreon.ubo.types.DataType"""
 
    @staticmethod
    def _wrap(java_value: _DataType) -> 'DataType':
        return DataType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DataType):
        """
        Dynamic initializer for DataType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DataType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DataType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
        return object._wrap(super(_DataType, self).accept(arg0))

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
 
 
# CLASS: dev.ultreon.ubo.types.BooleanType
from pyquantum_helper import import_once as _import_once
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.ubo.types.BooleanType as _BooleanType
_BooleanType = _BooleanType
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Boolean as _Boolean
_Boolean = _Boolean
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BooleanType():
    """dev.ultreon.ubo.types.BooleanType"""
 
    @staticmethod
    def _wrap(java_value: _BooleanType) -> 'BooleanType':
        return BooleanType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BooleanType):
        """
        Dynamic initializer for BooleanType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BooleanType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BooleanType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def copy(self) -> 'BooleanType':
        """public dev.ultreon.ubo.types.BooleanType dev.ultreon.ubo.types.BooleanType.copy()"""
        return 'BooleanType'._wrap(super(BooleanType, self).copy())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BooleanType.writeUso()"""
        return str._wrap(super(BooleanType, self).writeUso())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: bool):
        """public dev.ultreon.ubo.types.BooleanType(boolean)"""
        val = _BooleanType(_boolean.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.BooleanType.hashCode()"""
        return int._wrap(super(BooleanType, self).hashCode())

    @override
    @overload
    def getValue(self) -> 'Boolean':
        """public java.lang.Boolean dev.ultreon.ubo.types.BooleanType.getValue()"""
        return 'Boolean'._wrap(super(BooleanType, self).getValue())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.BooleanType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_BooleanType, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.BooleanType.equals(java.lang.Object)"""
        return bool._wrap(super(_BooleanType, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setValue(self, arg0: 'Boolean'):
        """public void dev.ultreon.ubo.types.BooleanType.setValue(java.lang.Boolean)"""
        super(_BooleanType, self).setValue(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.BooleanType.id()"""
        return int._wrap(super(BooleanType, self).id())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BooleanType.toString()"""
        return str._wrap(super(BooleanType, self).toString())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'BooleanType':
        """public static dev.ultreon.ubo.types.BooleanType dev.ultreon.ubo.types.BooleanType.read(java.io.DataInput) throws java.io.IOException"""
        return BooleanType._wrap(_BooleanType.read(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.ubo.types.DoubleType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import transform as _transform
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
import dev.ultreon.ubo.types.DoubleType as _DoubleType
_DoubleType = _DoubleType
from builtins import bool
import java.lang.Double as Double
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DoubleType():
    """dev.ultreon.ubo.types.DoubleType"""
 
    @staticmethod
    def _wrap(java_value: _DoubleType) -> 'DoubleType':
        return DoubleType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DoubleType):
        """
        Dynamic initializer for DoubleType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DoubleType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DoubleType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.ubo.types.DoubleType(double)"""
        val = _DoubleType(_double.valueOf(arg0))
        self.__wrapper = val

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'DoubleType':
        """public static dev.ultreon.ubo.types.DoubleType dev.ultreon.ubo.types.DoubleType.read(java.io.DataInput) throws java.io.IOException"""
        return DoubleType._wrap(_DoubleType.read(arg0))

    @override
    @overload
    def getValue(self) -> 'Double':
        """public java.lang.Double dev.ultreon.ubo.types.DoubleType.getValue()"""
        return _transform(super(DoubleType, self).getValue()).'Double'Value()

    @override
    @overload
    def copy(self) -> 'DoubleType':
        """public dev.ultreon.ubo.types.DoubleType dev.ultreon.ubo.types.DoubleType.copy()"""
        return 'DoubleType'._wrap(super(DoubleType, self).copy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setValue(self, arg0: 'Double'):
        """public void dev.ultreon.ubo.types.DoubleType.setValue(java.lang.Double)"""
        super(_DoubleType, self).setValue(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.DoubleType.toString()"""
        return str._wrap(super(DoubleType, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.DoubleType.hashCode()"""
        return int._wrap(super(DoubleType, self).hashCode())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.DoubleType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_DoubleType, self).write(arg0)

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
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.DoubleType.id()"""
        return int._wrap(super(DoubleType, self).id())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.DoubleType.equals(java.lang.Object)"""
        return bool._wrap(super(_DoubleType, self).equals(arg0))

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.DoubleType.writeUso()"""
        return str._wrap(super(DoubleType, self).writeUso())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.ubo.types.BitSetType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import java.util.BitSet as _BitSet
_BitSet = _BitSet
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import java.util.BitSet as BitSet
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
import dev.ultreon.ubo.types.BitSetType as _BitSetType
_BitSetType = _BitSetType
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BitSetType():
    """dev.ultreon.ubo.types.BitSetType"""
 
    @staticmethod
    def _wrap(java_value: _BitSetType) -> 'BitSetType':
        return BitSetType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BitSetType):
        """
        Dynamic initializer for BitSetType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BitSetType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BitSetType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: bytes):
        """public dev.ultreon.ubo.types.BitSetType(byte[])"""
        val = _BitSetType(bytes)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def length(self) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.length()"""
        return int._wrap(super(BitSetType, self).length())

    @override
    @overload
    def getValue(self) -> 'BitSet':
        """public java.util.BitSet dev.ultreon.ubo.types.BitSetType.getValue()"""
        return 'BitSet'._wrap(super(BitSetType, self).getValue())

    @overload
    def getBit(self, arg0: int) -> bool:
        """public boolean dev.ultreon.ubo.types.BitSetType.getBit(int)"""
        return bool._wrap(super(_BitSetType, self).getBit(_int.valueOf(arg0)))

    @overload
    def setBit(self, arg0: int, arg1: bool):
        """public void dev.ultreon.ubo.types.BitSetType.setBit(int,boolean)"""
        super(_BitSetType, self).setBit(_int.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BitSetType.toString()"""
        return str._wrap(super(BitSetType, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setValue(self, arg0: 'BitSet'):
        """public void dev.ultreon.ubo.types.BitSetType.setValue(java.util.BitSet)"""
        super(_BitSetType, self).setValue(arg0)

    @overload
    def nextSetBit(self, arg0: int) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.nextSetBit(int)"""
        return int._wrap(super(_BitSetType, self).nextSetBit(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def cardinality(self) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.cardinality()"""
        return int._wrap(super(BitSetType, self).cardinality())

    @overload
    def __init__(self, arg0: 'long'):
        """public dev.ultreon.ubo.types.BitSetType(long[])"""
        val = _BitSetType(arg0)
        self.__wrapper = val

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @overload
    def __init__(self, arg0: 'BitSet'):
        """public dev.ultreon.ubo.types.BitSetType(java.util.BitSet)"""
        val = _BitSetType(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'BitSetType':
        """public static dev.ultreon.ubo.types.BitSetType dev.ultreon.ubo.types.BitSetType.read(java.io.DataInput) throws java.io.IOException"""
        return BitSetType._wrap(_BitSetType.read(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.BitSetType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_BitSetType, self).write(arg0)

    @overload
    def nextClearBit(self, arg0: int) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.nextClearBit(int)"""
        return int._wrap(super(_BitSetType, self).nextClearBit(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.hashCode()"""
        return int._wrap(super(BitSetType, self).hashCode())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.ubo.types.BitSetType(java.lang.String)"""
        val = _BitSetType(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.BitSetType.equals(java.lang.Object)"""
        return bool._wrap(super(_BitSetType, self).equals(arg0))

    @overload
    def previousSetBit(self, arg0: int) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.previousSetBit(int)"""
        return int._wrap(super(_BitSetType, self).previousSetBit(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.id()"""
        return int._wrap(super(BitSetType, self).id())

    @override
    @overload
    def copy(self) -> 'BitSetType':
        """public dev.ultreon.ubo.types.BitSetType dev.ultreon.ubo.types.BitSetType.copy()"""
        return 'BitSetType'._wrap(super(BitSetType, self).copy())

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BitSetType.writeUso()"""
        return str._wrap(super(BitSetType, self).writeUso())

    @overload
    def previousClearBit(self, arg0: int) -> int:
        """public int dev.ultreon.ubo.types.BitSetType.previousClearBit(int)"""
        return int._wrap(super(_BitSetType, self).previousClearBit(_int.valueOf(arg0))) 
 
 
# CLASS: dev.ultreon.ubo.types.StringType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.ubo.types.StringType as _StringType
_StringType = _StringType
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StringType():
    """dev.ultreon.ubo.types.StringType"""
 
    @staticmethod
    def _wrap(java_value: _StringType) -> 'StringType':
        return StringType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringType):
        """
        Dynamic initializer for StringType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def copy(self) -> 'StringType':
        """public dev.ultreon.ubo.types.StringType dev.ultreon.ubo.types.StringType.copy()"""
        return 'StringType'._wrap(super(StringType, self).copy())

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.StringType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_StringType, self).write(arg0)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.ubo.types.StringType(java.lang.String)"""
        val = _StringType(arg0)
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

    @overload
    def setValue(self, arg0: str):
        """public void dev.ultreon.ubo.types.StringType.setValue(java.lang.String)"""
        super(_StringType, self).setValue(arg0)

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.StringType.writeUso()"""
        return str._wrap(super(StringType, self).writeUso())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'StringType':
        """public static dev.ultreon.ubo.types.StringType dev.ultreon.ubo.types.StringType.read(java.io.DataInput) throws java.io.IOException"""
        return StringType._wrap(_StringType.read(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.StringType.hashCode()"""
        return int._wrap(super(StringType, self).hashCode())

    @override
    @overload
    def getValue(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.StringType.getValue()"""
        return str._wrap(super(StringType, self).getValue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.StringType.id()"""
        return int._wrap(super(StringType, self).id())

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
        """public boolean dev.ultreon.ubo.types.StringType.equals(java.lang.Object)"""
        return bool._wrap(super(_StringType, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.StringType.toString()"""
        return str._wrap(super(StringType, self).toString()) 
 
 
# CLASS: dev.ultreon.ubo.types.BigDecType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import dev.ultreon.ubo.types.BigDecType as _BigDecType
_BigDecType = _BigDecType
import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
import java.math.BigDecimal as BigDecimal
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BigDecType():
    """dev.ultreon.ubo.types.BigDecType"""
 
    @staticmethod
    def _wrap(java_value: _BigDecType) -> 'BigDecType':
        return BigDecType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BigDecType):
        """
        Dynamic initializer for BigDecType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BigDecType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BigDecType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.ubo.types.BigDecType(java.lang.String)"""
        val = _BigDecType(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.BigDecType.equals(java.lang.Object)"""
        return bool._wrap(super(_BigDecType, self).equals(arg0))

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.BigDecType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_BigDecType, self).write(arg0)

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.BigDecType.id()"""
        return int._wrap(super(BigDecType, self).id())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def copy(self) -> 'BigDecType':
        """public dev.ultreon.ubo.types.BigDecType dev.ultreon.ubo.types.BigDecType.copy()"""
        return 'BigDecType'._wrap(super(BigDecType, self).copy())

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BigDecType.writeUso()"""
        return str._wrap(super(BigDecType, self).writeUso())

    @overload
    def setValue(self, arg0: 'BigDecimal'):
        """public void dev.ultreon.ubo.types.BigDecType.setValue(java.math.BigDecimal)"""
        super(_BigDecType, self).setValue(arg0)

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

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'BigDecType':
        """public static dev.ultreon.ubo.types.BigDecType dev.ultreon.ubo.types.BigDecType.read(java.io.DataInput) throws java.io.IOException"""
        return BigDecType._wrap(_BigDecType.read(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.BigDecType.hashCode()"""
        return int._wrap(super(BigDecType, self).hashCode())

    @override
    @overload
    def getValue(self) -> 'BigDecimal':
        """public java.math.BigDecimal dev.ultreon.ubo.types.BigDecType.getValue()"""
        return _transform(super(BigDecType, self).getValue()).'BigDecimal'Value()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.BigDecType.toString()"""
        return str._wrap(super(BigDecType, self).toString())

    @overload
    def __init__(self, arg0: 'BigDecimal'):
        """public dev.ultreon.ubo.types.BigDecType(java.math.BigDecimal)"""
        val = _BigDecType(arg0)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.ubo.types.IntArrayType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
from typing import List
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
import dev.ultreon.ubo.types.IntArrayType as _IntArrayType
_IntArrayType = _IntArrayType
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntArrayType():
    """dev.ultreon.ubo.types.IntArrayType"""
 
    @staticmethod
    def _wrap(java_value: _IntArrayType) -> 'IntArrayType':
        return IntArrayType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntArrayType):
        """
        Dynamic initializer for IntArrayType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntArrayType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntArrayType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.IntArrayType.toString()"""
        return str._wrap(super(IntArrayType, self).toString())

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.IntArrayType.writeUso()"""
        return str._wrap(super(IntArrayType, self).writeUso())

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
    def size(self) -> int:
        """public int dev.ultreon.ubo.types.IntArrayType.size()"""
        return int._wrap(super(IntArrayType, self).size())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.IntArrayType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_IntArrayType, self).write(arg0)

    @override
    @overload
    def copy(self) -> 'IntArrayType':
        """public dev.ultreon.ubo.types.IntArrayType dev.ultreon.ubo.types.IntArrayType.copy()"""
        return 'IntArrayType'._wrap(super(IntArrayType, self).copy())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.IntArrayType.hashCode()"""
        return int._wrap(super(IntArrayType, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'int'):
        """public dev.ultreon.ubo.types.IntArrayType(int[])"""
        val = _IntArrayType(arg0)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'IntArrayType':
        """public static dev.ultreon.ubo.types.IntArrayType dev.ultreon.ubo.types.IntArrayType.read(java.io.DataInput) throws java.io.IOException"""
        return IntArrayType._wrap(_IntArrayType.read(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.IntArrayType.equals(java.lang.Object)"""
        return bool._wrap(super(_IntArrayType, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getValue(self) -> List[int]:
        """public int[] dev.ultreon.ubo.types.IntArrayType.getValue()"""
        return List[int]._wrap(super(IntArrayType, self).getValue())

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.IntArrayType.id()"""
        return int._wrap(super(IntArrayType, self).id())

    @overload
    def setValue(self, arg0: 'int'):
        """public void dev.ultreon.ubo.types.IntArrayType.setValue(int[])"""
        super(_IntArrayType, self).setValue(arg0) 
 
 
# CLASS: dev.ultreon.ubo.types.ShortType
from pyquantum_helper import import_once as _import_once
import dev.ultreon.ubo.types.ShortType as _ShortType
_ShortType = _ShortType
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Short as Short
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import java.lang.Short as _short
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShortType():
    """dev.ultreon.ubo.types.ShortType"""
 
    @staticmethod
    def _wrap(java_value: _ShortType) -> 'ShortType':
        return ShortType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShortType):
        """
        Dynamic initializer for ShortType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShortType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShortType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def copy(self) -> 'ShortType':
        """public dev.ultreon.ubo.types.ShortType dev.ultreon.ubo.types.ShortType.copy()"""
        return 'ShortType'._wrap(super(ShortType, self).copy())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.ShortType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_ShortType, self).write(arg0)

    @overload
    def setValue(self, arg0: 'Short'):
        """public void dev.ultreon.ubo.types.ShortType.setValue(java.lang.Short)"""
        super(_ShortType, self).setValue(arg0)

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.ShortType.hashCode()"""
        return int._wrap(super(ShortType, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.ShortType(int)"""
        val = _ShortType(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ShortType.writeUso()"""
        return str._wrap(super(ShortType, self).writeUso())

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

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'ShortType':
        """public static dev.ultreon.ubo.types.ShortType dev.ultreon.ubo.types.ShortType.read(java.io.DataInput) throws java.io.IOException"""
        return ShortType._wrap(_ShortType.read(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getValue(self) -> 'Short':
        """public java.lang.Short dev.ultreon.ubo.types.ShortType.getValue()"""
        return _transform(super(ShortType, self).getValue()).'Short'Value()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ShortType.toString()"""
        return str._wrap(super(ShortType, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.ShortType(short)"""
        val = _ShortType(_short.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.ShortType.id()"""
        return int._wrap(super(ShortType, self).id())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.ShortType.equals(java.lang.Object)"""
        return bool._wrap(super(_ShortType, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.ubo.types.UUIDType
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import java.lang.String as _String
_String = _String
from builtins import object
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import dev.ultreon.ubo.types.UUIDType as _UUIDType
_UUIDType = _UUIDType
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
 
class UUIDType():
    """dev.ultreon.ubo.types.UUIDType"""
 
    @staticmethod
    def _wrap(java_value: _UUIDType) -> 'UUIDType':
        return UUIDType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UUIDType):
        """
        Dynamic initializer for UUIDType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UUIDType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UUIDType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.UUIDType.hashCode()"""
        return int._wrap(super(UUIDType, self).hashCode())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'UUIDType':
        """public static dev.ultreon.ubo.types.UUIDType dev.ultreon.ubo.types.UUIDType.read(java.io.DataInput) throws java.io.IOException"""
        return UUIDType._wrap(_UUIDType.read(arg0))

    @overload
    def __init__(self, arg0: 'UUID'):
        """public dev.ultreon.ubo.types.UUIDType(java.util.UUID)"""
        val = _UUIDType(arg0)
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
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.UUIDType.id()"""
        return int._wrap(super(UUIDType, self).id())

    @override
    @overload
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.UUIDType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_UUIDType, self).write(arg0)

    @override
    @overload
    def copy(self) -> 'UUIDType':
        """public dev.ultreon.ubo.types.UUIDType dev.ultreon.ubo.types.UUIDType.copy()"""
        return 'UUIDType'._wrap(super(UUIDType, self).copy())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.ubo.types.UUIDType.getValue()"""
        return 'UUID'._wrap(super(UUIDType, self).getValue())

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
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.UUIDType.writeUso()"""
        return str._wrap(super(UUIDType, self).writeUso())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.UUIDType.equals(java.lang.Object)"""
        return bool._wrap(super(_UUIDType, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.UUIDType.toString()"""
        return str._wrap(super(UUIDType, self).toString())

    @overload
    def setValue(self, arg0: 'UUID'):
        """public void dev.ultreon.ubo.types.UUIDType.setValue(java.util.UUID)"""
        super(_UUIDType, self).setValue(arg0) 
 
 
# CLASS: dev.ultreon.ubo.types.ByteType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyubo import util
except ImportError:
    util = _import_once("pyubo.util")

import dev.ultreon.ubo.types.ByteType as _ByteType
_ByteType = _ByteType
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Byte as Byte
import java.io.DataInput as DataInput
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import java.lang.Integer as _int
import java.io.DataOutput as DataOutput
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ByteType():
    """dev.ultreon.ubo.types.ByteType"""
 
    @staticmethod
    def _wrap(java_value: _ByteType) -> 'ByteType':
        return ByteType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ByteType):
        """
        Dynamic initializer for ByteType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ByteType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ByteType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.ByteType(int)"""
        val = _ByteType(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def accept(self, arg0: 'DataTypeVisitor') -> object:
        """public default <R> R dev.ultreon.ubo.types.DataType.accept(dev.ultreon.ubo.util.DataTypeVisitor<R>)"""
        return object._wrap(super(_DataType, self).accept(arg0))

    @override
    @overload
    def writeUso(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ByteType.writeUso()"""
        return str._wrap(super(ByteType, self).writeUso())

    @staticmethod
    @overload
    def read(arg0: 'DataInput') -> 'ByteType':
        """public static dev.ultreon.ubo.types.ByteType dev.ultreon.ubo.types.ByteType.read(java.io.DataInput) throws java.io.IOException"""
        return ByteType._wrap(_ByteType.read(arg0))

    @overload
    def setValue(self, arg0: 'Byte'):
        """public void dev.ultreon.ubo.types.ByteType.setValue(java.lang.Byte)"""
        super(_ByteType, self).setValue(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.ubo.types.ByteType.equals(java.lang.Object)"""
        return bool._wrap(super(_ByteType, self).equals(arg0))

    @override
    @overload
    def id(self) -> int:
        """public int dev.ultreon.ubo.types.ByteType.id()"""
        return int._wrap(super(ByteType, self).id())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.ubo.types.ByteType(byte)"""
        val = _ByteType(_byte.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def copy(self) -> 'ByteType':
        """public dev.ultreon.ubo.types.ByteType dev.ultreon.ubo.types.ByteType.copy()"""
        return 'ByteType'._wrap(super(ByteType, self).copy())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.ubo.types.ByteType.hashCode()"""
        return int._wrap(super(ByteType, self).hashCode())

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
    def write(self, arg0: 'DataOutput'):
        """public void dev.ultreon.ubo.types.ByteType.write(java.io.DataOutput) throws java.io.IOException"""
        super(_ByteType, self).write(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getValue(self) -> 'Byte':
        """public java.lang.Byte dev.ultreon.ubo.types.ByteType.getValue()"""
        return _transform(super(ByteType, self).getValue()).'Byte'Value()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.ubo.types.ByteType.toString()"""
        return str._wrap(super(ByteType, self).toString())