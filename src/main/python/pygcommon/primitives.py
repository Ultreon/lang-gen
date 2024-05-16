from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
import com.google.common.base.Converter as __Converter
__Converter = __Converter
from pyquantum_helper import override
import com.google.common.primitives.Ints as __Ints
__Ints = __Ints
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
from typing import List
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Byte as __byte
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class Ints():
    """com.google.common.primitives.Ints"""
 
    @staticmethod
    def __wrap(java_value: __Ints) -> 'Ints':
        return Ints(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Ints):
        """
        Dynamic initializer for Ints.
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
 
    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.Ints.join(java.lang.String,int...)"""
        return str.__wrap(__Ints.join(separator, array))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def rotate(array: 'int', distance: int):
        """public static void com.google.common.primitives.Ints.rotate(int[],int)"""
        __Ints.rotate(array, __int.valueOf(distance))

    @staticmethod
    @overload
    def checkedCast(value: int) -> int:
        """public static int com.google.common.primitives.Ints.checkedCast(long)"""
        return int.__wrap(__Ints.checkedCast(__long.valueOf(value)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static int com.google.common.primitives.Ints.max(int...)"""
        return int.__wrap(__Ints.max(array))

    @staticmethod
    @overload
    def rotate(array: 'int', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Ints.rotate(int[],int,int,int)"""
        __Ints.rotate(array, __int.valueOf(distance), __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def reverse(array: 'int'):
        """public static void com.google.common.primitives.Ints.reverse(int[])"""
        __Ints.reverse(array)

    @staticmethod
    @overload
    def asList(*backingArray: int) -> 'List':
        """public static java.util.List<java.lang.Integer> com.google.common.primitives.Ints.asList(int...)"""
        return List.__wrap(__Ints.asList(backingArray))

    @staticmethod
    @overload
    def fromByteArray(bytes: bytes) -> int:
        """public static int com.google.common.primitives.Ints.fromByteArray(byte[])"""
        return int.__wrap(__Ints.fromByteArray(bytes))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def concat(*arrays: List[int]) -> List[int]:
        """public static int[] com.google.common.primitives.Ints.concat(int[]...)"""
        return List[int].__wrap(__Ints.concat(arrays))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<int[]> com.google.common.primitives.Ints.lexicographicalComparator()"""
        return Comparator.__wrap(__Ints.lexicographicalComparator())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def lastIndexOf(array: 'int', target: int) -> int:
        """public static int com.google.common.primitives.Ints.lastIndexOf(int[],int)"""
        return int.__wrap(__Ints.lastIndexOf(array, __int.valueOf(target)))

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.Ints.compare(int,int)"""
        return int.__wrap(__Ints.compare(__int.valueOf(a), __int.valueOf(b)))

    @staticmethod
    @overload
    def reverse(array: 'int', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Ints.reverse(int[],int,int)"""
        __Ints.reverse(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def indexOf(array: 'int', target: int) -> int:
        """public static int com.google.common.primitives.Ints.indexOf(int[],int)"""
        return int.__wrap(__Ints.indexOf(array, __int.valueOf(target)))

    @staticmethod
    @overload
    def toByteArray(value: int) -> List[int]:
        """public static byte[] com.google.common.primitives.Ints.toByteArray(int)"""
        return List[int].__wrap(__Ints.toByteArray(__int.valueOf(value)))

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Integer':
        """public static java.lang.Integer com.google.common.primitives.Ints.tryParse(java.lang.String,int)"""
        return __transform(__string, __int.valueOf(radix).Ints(string: str, radix: int)).'Integer'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def indexOf(array: 'int', target: 'int') -> int:
        """public static int com.google.common.primitives.Ints.indexOf(int[],int[])"""
        return int.__wrap(__Ints.indexOf(array, target))

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static int com.google.common.primitives.Ints.min(int...)"""
        return int.__wrap(__Ints.min(array))

    @staticmethod
    @overload
    def fromBytes(b1: int, b2: int, b3: int, b4: int) -> int:
        """public static int com.google.common.primitives.Ints.fromBytes(byte,byte,byte,byte)"""
        return int.__wrap(__Ints.fromBytes(__byte.valueOf(b1), __byte.valueOf(b2), __byte.valueOf(b3), __byte.valueOf(b4)))

    @staticmethod
    @overload
    def sortDescending(array: 'int'):
        """public static void com.google.common.primitives.Ints.sortDescending(int[])"""
        __Ints.sortDescending(array)

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[int]:
        """public static int[] com.google.common.primitives.Ints.toArray(java.util.Collection<? extends java.lang.Number>)"""
        return List[int].__wrap(__Ints.toArray(collection))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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
    def contains(array: 'int', target: int) -> bool:
        """public static boolean com.google.common.primitives.Ints.contains(int[],int)"""
        return bool.__wrap(__Ints.contains(array, __int.valueOf(target)))

    @staticmethod
    @overload
    def constrainToRange(value: int, min: int, max: int) -> int:
        """public static int com.google.common.primitives.Ints.constrainToRange(int,int,int)"""
        return int.__wrap(__Ints.constrainToRange(__int.valueOf(value), __int.valueOf(min), __int.valueOf(max)))

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Integer':
        """public static java.lang.Integer com.google.common.primitives.Ints.tryParse(java.lang.String)"""
        return __transform(__string.Ints(string: str)).'Integer'Value()

    @staticmethod
    @overload
    def ensureCapacity(array: 'int', minLength: int, padding: int) -> List[int]:
        """public static int[] com.google.common.primitives.Ints.ensureCapacity(int[],int,int)"""
        return List[int].__wrap(__Ints.ensureCapacity(array, __int.valueOf(minLength), __int.valueOf(padding)))

    @staticmethod
    @overload
    def stringConverter() -> 'base.Converter':
        """public static com.google.common.base.Converter<java.lang.String, java.lang.Integer> com.google.common.primitives.Ints.stringConverter()"""
        return base.Converter.__wrap(__Ints.stringConverter())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def saturatedCast(value: int) -> int:
        """public static int com.google.common.primitives.Ints.saturatedCast(long)"""
        return int.__wrap(__Ints.saturatedCast(__long.valueOf(value)))

    @staticmethod
    @overload
    def sortDescending(array: 'int', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Ints.sortDescending(int[],int,int)"""
        __Ints.sortDescending(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def hashCode(value: int) -> int:
        """public static int com.google.common.primitives.Ints.hashCode(int)"""
        return int.__wrap(__Ints.hashCode(__int.valueOf(value)))

 
 
 
# CLASS: com.google.common.primitives.Ints
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
import com.google.common.base.Converter as __Converter
__Converter = __Converter
from pyquantum_helper import override
import com.google.common.primitives.Ints as __Ints
__Ints = __Ints
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
from typing import List
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Byte as __byte
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class Ints():
    """com.google.common.primitives.Ints"""
 
    @staticmethod
    def __wrap(java_value: __Ints) -> 'Ints':
        return Ints(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Ints):
        """
        Dynamic initializer for Ints.
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
 
    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.Ints.join(java.lang.String,int...)"""
        return str.__wrap(__Ints.join(separator, array))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def rotate(array: 'int', distance: int):
        """public static void com.google.common.primitives.Ints.rotate(int[],int)"""
        __Ints.rotate(array, __int.valueOf(distance))

    @staticmethod
    @overload
    def checkedCast(value: int) -> int:
        """public static int com.google.common.primitives.Ints.checkedCast(long)"""
        return int.__wrap(__Ints.checkedCast(__long.valueOf(value)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static int com.google.common.primitives.Ints.max(int...)"""
        return int.__wrap(__Ints.max(array))

    @staticmethod
    @overload
    def rotate(array: 'int', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Ints.rotate(int[],int,int,int)"""
        __Ints.rotate(array, __int.valueOf(distance), __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def reverse(array: 'int'):
        """public static void com.google.common.primitives.Ints.reverse(int[])"""
        __Ints.reverse(array)

    @staticmethod
    @overload
    def asList(*backingArray: int) -> 'List':
        """public static java.util.List<java.lang.Integer> com.google.common.primitives.Ints.asList(int...)"""
        return List.__wrap(__Ints.asList(backingArray))

    @staticmethod
    @overload
    def fromByteArray(bytes: bytes) -> int:
        """public static int com.google.common.primitives.Ints.fromByteArray(byte[])"""
        return int.__wrap(__Ints.fromByteArray(bytes))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def concat(*arrays: List[int]) -> List[int]:
        """public static int[] com.google.common.primitives.Ints.concat(int[]...)"""
        return List[int].__wrap(__Ints.concat(arrays))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<int[]> com.google.common.primitives.Ints.lexicographicalComparator()"""
        return Comparator.__wrap(__Ints.lexicographicalComparator())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def lastIndexOf(array: 'int', target: int) -> int:
        """public static int com.google.common.primitives.Ints.lastIndexOf(int[],int)"""
        return int.__wrap(__Ints.lastIndexOf(array, __int.valueOf(target)))

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.Ints.compare(int,int)"""
        return int.__wrap(__Ints.compare(__int.valueOf(a), __int.valueOf(b)))

    @staticmethod
    @overload
    def reverse(array: 'int', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Ints.reverse(int[],int,int)"""
        __Ints.reverse(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def indexOf(array: 'int', target: int) -> int:
        """public static int com.google.common.primitives.Ints.indexOf(int[],int)"""
        return int.__wrap(__Ints.indexOf(array, __int.valueOf(target)))

    @staticmethod
    @overload
    def toByteArray(value: int) -> List[int]:
        """public static byte[] com.google.common.primitives.Ints.toByteArray(int)"""
        return List[int].__wrap(__Ints.toByteArray(__int.valueOf(value)))

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Integer':
        """public static java.lang.Integer com.google.common.primitives.Ints.tryParse(java.lang.String,int)"""
        return __transform(__string, __int.valueOf(radix).Ints(string: str, radix: int)).'Integer'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def indexOf(array: 'int', target: 'int') -> int:
        """public static int com.google.common.primitives.Ints.indexOf(int[],int[])"""
        return int.__wrap(__Ints.indexOf(array, target))

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static int com.google.common.primitives.Ints.min(int...)"""
        return int.__wrap(__Ints.min(array))

    @staticmethod
    @overload
    def fromBytes(b1: int, b2: int, b3: int, b4: int) -> int:
        """public static int com.google.common.primitives.Ints.fromBytes(byte,byte,byte,byte)"""
        return int.__wrap(__Ints.fromBytes(__byte.valueOf(b1), __byte.valueOf(b2), __byte.valueOf(b3), __byte.valueOf(b4)))

    @staticmethod
    @overload
    def sortDescending(array: 'int'):
        """public static void com.google.common.primitives.Ints.sortDescending(int[])"""
        __Ints.sortDescending(array)

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[int]:
        """public static int[] com.google.common.primitives.Ints.toArray(java.util.Collection<? extends java.lang.Number>)"""
        return List[int].__wrap(__Ints.toArray(collection))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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
    def contains(array: 'int', target: int) -> bool:
        """public static boolean com.google.common.primitives.Ints.contains(int[],int)"""
        return bool.__wrap(__Ints.contains(array, __int.valueOf(target)))

    @staticmethod
    @overload
    def constrainToRange(value: int, min: int, max: int) -> int:
        """public static int com.google.common.primitives.Ints.constrainToRange(int,int,int)"""
        return int.__wrap(__Ints.constrainToRange(__int.valueOf(value), __int.valueOf(min), __int.valueOf(max)))

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Integer':
        """public static java.lang.Integer com.google.common.primitives.Ints.tryParse(java.lang.String)"""
        return __transform(__string.Ints(string: str)).'Integer'Value()

    @staticmethod
    @overload
    def ensureCapacity(array: 'int', minLength: int, padding: int) -> List[int]:
        """public static int[] com.google.common.primitives.Ints.ensureCapacity(int[],int,int)"""
        return List[int].__wrap(__Ints.ensureCapacity(array, __int.valueOf(minLength), __int.valueOf(padding)))

    @staticmethod
    @overload
    def stringConverter() -> 'base.Converter':
        """public static com.google.common.base.Converter<java.lang.String, java.lang.Integer> com.google.common.primitives.Ints.stringConverter()"""
        return base.Converter.__wrap(__Ints.stringConverter())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def saturatedCast(value: int) -> int:
        """public static int com.google.common.primitives.Ints.saturatedCast(long)"""
        return int.__wrap(__Ints.saturatedCast(__long.valueOf(value)))

    @staticmethod
    @overload
    def sortDescending(array: 'int', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Ints.sortDescending(int[],int,int)"""
        __Ints.sortDescending(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def hashCode(value: int) -> int:
        """public static int com.google.common.primitives.Ints.hashCode(int)"""
        return int.__wrap(__Ints.hashCode(__int.valueOf(value)))

 
 
 
# CLASS: com.google.common.primitives.Ints 
 
 
# CLASS: com.google.common.primitives.ImmutableDoubleArray
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.stream.DoubleStream as __DoubleStream
__DoubleStream = __DoubleStream
import java.util.function.DoubleConsumer as DoubleConsumer
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
from typing import List
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import com.google.common.primitives.ImmutableDoubleArray as __ImmutableDoubleArray_Builder
__Builder = __ImmutableDoubleArray_Builder.Builder
import java.lang.Class as __Class
__Class = __Class
import com.google.common.primitives.ImmutableDoubleArray as __ImmutableDoubleArray
__ImmutableDoubleArray = __ImmutableDoubleArray
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.DoubleStream as DoubleStream
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
import java.util.List as List
 
class ImmutableDoubleArray():
    """com.google.common.primitives.ImmutableDoubleArray"""
 
    @staticmethod
    def __wrap(java_value: __ImmutableDoubleArray) -> 'ImmutableDoubleArray':
        return ImmutableDoubleArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImmutableDoubleArray):
        """
        Dynamic initializer for ImmutableDoubleArray.
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
    def asList(self) -> 'List':
        """public java.util.List<java.lang.Double> com.google.common.primitives.ImmutableDoubleArray.asList()"""
        return 'List'.__wrap(super(ImmutableDoubleArray, self).asList())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def of() -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of()"""
        return ImmutableDoubleArray.__wrap(__ImmutableDoubleArray.of())

    @staticmethod
    @overload
    def copyOf(values: 'double') -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.copyOf(double[])"""
        return ImmutableDoubleArray.__wrap(__ImmutableDoubleArray.copyOf(values))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def copyOf(values: 'Collection') -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.copyOf(java.util.Collection<java.lang.Double>)"""
        return ImmutableDoubleArray.__wrap(__ImmutableDoubleArray.copyOf(values))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.primitives.ImmutableDoubleArray.toString()"""
        return str.__wrap(super(ImmutableDoubleArray, self).toString())

    @overload
    def subArray(self, startIndex: int, endIndex: int) -> 'ImmutableDoubleArray':
        """public com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.subArray(int,int)"""
        return 'ImmutableDoubleArray'.__wrap(super(__ImmutableDoubleArray, self).subArray(__int.valueOf(startIndex), __int.valueOf(endIndex)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def copyOf(values: 'Iterable') -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.copyOf(java.lang.Iterable<java.lang.Double>)"""
        return ImmutableDoubleArray.__wrap(__ImmutableDoubleArray.copyOf(values))

    @staticmethod
    @overload
    def of(first: float, *rest: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double,double...)"""
        return ImmutableDoubleArray.__wrap(__ImmutableDoubleArray.of(__double.valueOf(first), rest))

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray.builder()"""
        return Builder.__wrap(__ImmutableDoubleArray.builder())

    @overload
    def stream(self) -> 'DoubleStream':
        """public java.util.stream.DoubleStream com.google.common.primitives.ImmutableDoubleArray.stream()"""
        return 'DoubleStream'.__wrap(super(ImmutableDoubleArray, self).stream())

    @staticmethod
    @overload
    def of(e0: float, e1: float, e2: float, e3: float, e4: float, e5: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double,double,double,double,double,double)"""
        return ImmutableDoubleArray.__wrap(__ImmutableDoubleArray.of(__double.valueOf(e0), __double.valueOf(e1), __double.valueOf(e2), __double.valueOf(e3), __double.valueOf(e4), __double.valueOf(e5)))

    @overload
    def trimmed(self) -> 'ImmutableDoubleArray':
        """public com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.trimmed()"""
        return 'ImmutableDoubleArray'.__wrap(super(ImmutableDoubleArray, self).trimmed())

    @overload
    def indexOf(self, target: float) -> int:
        """public int com.google.common.primitives.ImmutableDoubleArray.indexOf(double)"""
        return int.__wrap(super(__ImmutableDoubleArray, self).indexOf(__double.valueOf(target)))

    @overload
    def contains(self, target: float) -> bool:
        """public boolean com.google.common.primitives.ImmutableDoubleArray.contains(double)"""
        return bool.__wrap(super(__ImmutableDoubleArray, self).contains(__double.valueOf(target)))

    @staticmethod
    @overload
    def builder(initialCapacity: int) -> 'Builder':
        """public static com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray.builder(int)"""
        return Builder.__wrap(__ImmutableDoubleArray.builder(__int.valueOf(initialCapacity)))

    @staticmethod
    @overload
    def of(e0: float, e1: float, e2: float, e3: float, e4: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double,double,double,double,double)"""
        return ImmutableDoubleArray.__wrap(__ImmutableDoubleArray.of(__double.valueOf(e0), __double.valueOf(e1), __double.valueOf(e2), __double.valueOf(e3), __double.valueOf(e4)))

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.primitives.ImmutableDoubleArray.equals(java.lang.Object)"""
        return bool.__wrap(super(__ImmutableDoubleArray, self).equals(object))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.primitives.ImmutableDoubleArray.hashCode()"""
        return int.__wrap(super(ImmutableDoubleArray, self).hashCode())

    @staticmethod
    @overload
    def of(e0: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double)"""
        return ImmutableDoubleArray.__wrap(__ImmutableDoubleArray.of(__double.valueOf(e0)))

    @staticmethod
    @overload
    def copyOf(stream: 'DoubleStream') -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.copyOf(java.util.stream.DoubleStream)"""
        return ImmutableDoubleArray.__wrap(__ImmutableDoubleArray.copyOf(stream))

    @staticmethod
    @overload
    def of(e0: float, e1: float, e2: float, e3: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double,double,double,double)"""
        return ImmutableDoubleArray.__wrap(__ImmutableDoubleArray.of(__double.valueOf(e0), __double.valueOf(e1), __double.valueOf(e2), __double.valueOf(e3)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def toArray(self) -> List[float]:
        """public double[] com.google.common.primitives.ImmutableDoubleArray.toArray()"""
        return List[float].__wrap(super(ImmutableDoubleArray, self).toArray())

    @staticmethod
    @overload
    def of(e0: float, e1: float, e2: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double,double,double)"""
        return ImmutableDoubleArray.__wrap(__ImmutableDoubleArray.of(__double.valueOf(e0), __double.valueOf(e1), __double.valueOf(e2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def get(self, index: int) -> float:
        """public double com.google.common.primitives.ImmutableDoubleArray.get(int)"""
        return float.__wrap(super(__ImmutableDoubleArray, self).get(__int.valueOf(index)))

    @staticmethod
    @overload
    def of(e0: float, e1: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double,double)"""
        return ImmutableDoubleArray.__wrap(__ImmutableDoubleArray.of(__double.valueOf(e0), __double.valueOf(e1)))

    @overload
    def forEach(self, consumer: 'DoubleConsumer'):
        """public void com.google.common.primitives.ImmutableDoubleArray.forEach(java.util.function.DoubleConsumer)"""
        super(__ImmutableDoubleArray, self).forEach(consumer)

    @overload
    def lastIndexOf(self, target: float) -> int:
        """public int com.google.common.primitives.ImmutableDoubleArray.lastIndexOf(double)"""
        return int.__wrap(super(__ImmutableDoubleArray, self).lastIndexOf(__double.valueOf(target)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def length(self) -> int:
        """public int com.google.common.primitives.ImmutableDoubleArray.length()"""
        return int.__wrap(super(ImmutableDoubleArray, self).length())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.primitives.ImmutableDoubleArray.isEmpty()"""
        return bool.__wrap(super(ImmutableDoubleArray, self).isEmpty()) 
 
 
# CLASS: com.google.common.primitives.UnsignedInteger
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.primitives.UnsignedInteger as __UnsignedInteger
__UnsignedInteger = __UnsignedInteger
from builtins import float
import java.lang.Long as __long
import java.math.BigInteger as BigInteger
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Number as __Number
__Number = __Number
from builtins import int
 
class UnsignedInteger():
    """com.google.common.primitives.UnsignedInteger"""
 
    @staticmethod
    def __wrap(java_value: __UnsignedInteger) -> 'UnsignedInteger':
        return UnsignedInteger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnsignedInteger):
        """
        Dynamic initializer for UnsignedInteger.
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
    def compareTo(self, other: 'UnsignedInteger') -> int:
        """public int com.google.common.primitives.UnsignedInteger.compareTo(com.google.common.primitives.UnsignedInteger)"""
        return int.__wrap(super(__UnsignedInteger, self).compareTo(other))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.primitives.UnsignedInteger.toString()"""
        return str.__wrap(super(UnsignedInteger, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.primitives.UnsignedInteger.hashCode()"""
        return int.__wrap(super(UnsignedInteger, self).hashCode())

    @overload
    def mod(self, val: 'UnsignedInteger') -> 'UnsignedInteger':
        """public com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.mod(com.google.common.primitives.UnsignedInteger)"""
        return __transform(super(__UnsignedInteger, self).mod(val)).'UnsignedInteger'Value()

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedInteger':
        """public static com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.valueOf(java.lang.String)"""
        return __transform(__string.UnsignedInteger(string: str)).'UnsignedInteger'Value()

    @override
    @overload
    def intValue(self) -> int:
        """public int com.google.common.primitives.UnsignedInteger.intValue()"""
        return int.__wrap(super(UnsignedInteger, self).intValue())

    @overload
    def times(self, val: 'UnsignedInteger') -> 'UnsignedInteger':
        """public com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.times(com.google.common.primitives.UnsignedInteger)"""
        return __transform(super(__UnsignedInteger, self).times(val)).'UnsignedInteger'Value()

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedInteger':
        """public static com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.valueOf(long)"""
        return __transform(____long.valueOf(value).UnsignedInteger(value: int)).'UnsignedInteger'Value()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def bigIntegerValue(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.common.primitives.UnsignedInteger.bigIntegerValue()"""
        return __transform(super(UnsignedInteger, self).bigIntegerValue()).'BigInteger'Value()

    @staticmethod
    @overload
    def fromIntBits(fromIntBits) -> 'UnsignedInteger':
        """public static com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.fromIntBits(int)"""
        return __transform(____int.valueOf(bits).UnsignedInteger(bits: int)).'UnsignedInteger'Value()

    @override
    @overload
    def doubleValue(self) -> float:
        """public double com.google.common.primitives.UnsignedInteger.doubleValue()"""
        return float.__wrap(super(UnsignedInteger, self).doubleValue())

    @override
    @overload
    def floatValue(self) -> float:
        """public float com.google.common.primitives.UnsignedInteger.floatValue()"""
        return float.__wrap(super(UnsignedInteger, self).floatValue())

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int.__wrap(super(Number, self).shortValue())

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.primitives.UnsignedInteger.equals(java.lang.Object)"""
        return bool.__wrap(super(__UnsignedInteger, self).equals(obj))

    @overload
    def toString(self, radix: int) -> str:
        """public java.lang.String com.google.common.primitives.UnsignedInteger.toString(int)"""
        return str.__wrap(super(__UnsignedInteger, self).toString(__int.valueOf(radix)))

    @override
    @overload
    def longValue(self) -> int:
        """public long com.google.common.primitives.UnsignedInteger.longValue()"""
        return int.__wrap(super(UnsignedInteger, self).longValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def minus(self, val: 'UnsignedInteger') -> 'UnsignedInteger':
        """public com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.minus(com.google.common.primitives.UnsignedInteger)"""
        return __transform(super(__UnsignedInteger, self).minus(val)).'UnsignedInteger'Value()

    @overload
    def dividedBy(self, val: 'UnsignedInteger') -> 'UnsignedInteger':
        """public com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.dividedBy(com.google.common.primitives.UnsignedInteger)"""
        return __transform(super(__UnsignedInteger, self).dividedBy(val)).'UnsignedInteger'Value()

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int.__wrap(super(Number, self).byteValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def plus(self, val: 'UnsignedInteger') -> 'UnsignedInteger':
        """public com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.plus(com.google.common.primitives.UnsignedInteger)"""
        return __transform(super(__UnsignedInteger, self).plus(val)).'UnsignedInteger'Value()

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedInteger':
        """public static com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.valueOf(java.lang.String,int)"""
        return __transform(__string, __int.valueOf(radix).UnsignedInteger(string: str, radix: int)).'UnsignedInteger'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedInteger':
        """public static com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.valueOf(java.math.BigInteger)"""
        return __transform(__value.UnsignedInteger(value: 'BigInteger')).'UnsignedInteger'Value() 
 
 
# CLASS: com.google.common.primitives.ImmutableIntArray
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.primitives.ImmutableIntArray as __ImmutableIntArray_Builder
__Builder = __ImmutableIntArray_Builder.Builder
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
from typing import List
import com.google.common.primitives.ImmutableIntArray as __ImmutableIntArray
__ImmutableIntArray = __ImmutableIntArray
import java.util.stream.IntStream as __IntStream
__IntStream = __IntStream
import java.util.function.IntConsumer as IntConsumer
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
import java.util.stream.IntStream as IntStream
from builtins import bool
from builtins import int
import java.util.List as List
 
class ImmutableIntArray():
    """com.google.common.primitives.ImmutableIntArray"""
 
    @staticmethod
    def __wrap(java_value: __ImmutableIntArray) -> 'ImmutableIntArray':
        return ImmutableIntArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImmutableIntArray):
        """
        Dynamic initializer for ImmutableIntArray.
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
    def get(self, index: int) -> int:
        """public int com.google.common.primitives.ImmutableIntArray.get(int)"""
        return int.__wrap(super(__ImmutableIntArray, self).get(__int.valueOf(index)))

    @overload
    def stream(self) -> 'IntStream':
        """public java.util.stream.IntStream com.google.common.primitives.ImmutableIntArray.stream()"""
        return 'IntStream'.__wrap(super(ImmutableIntArray, self).stream())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def lastIndexOf(self, target: int) -> int:
        """public int com.google.common.primitives.ImmutableIntArray.lastIndexOf(int)"""
        return int.__wrap(super(__ImmutableIntArray, self).lastIndexOf(__int.valueOf(target)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def copyOf(stream: 'IntStream') -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.copyOf(java.util.stream.IntStream)"""
        return ImmutableIntArray.__wrap(__ImmutableIntArray.copyOf(stream))

    @overload
    def length(self) -> int:
        """public int com.google.common.primitives.ImmutableIntArray.length()"""
        return int.__wrap(super(ImmutableIntArray, self).length())

    @overload
    def contains(self, target: int) -> bool:
        """public boolean com.google.common.primitives.ImmutableIntArray.contains(int)"""
        return bool.__wrap(super(__ImmutableIntArray, self).contains(__int.valueOf(target)))

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.primitives.ImmutableIntArray.equals(java.lang.Object)"""
        return bool.__wrap(super(__ImmutableIntArray, self).equals(object))

    @staticmethod
    @overload
    def of(first: int, *rest: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int,int...)"""
        return ImmutableIntArray.__wrap(__ImmutableIntArray.of(__int.valueOf(first), rest))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toArray(self) -> List[int]:
        """public int[] com.google.common.primitives.ImmutableIntArray.toArray()"""
        return List[int].__wrap(super(ImmutableIntArray, self).toArray())

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int,int,int)"""
        return ImmutableIntArray.__wrap(__ImmutableIntArray.of(__int.valueOf(e0), __int.valueOf(e1), __int.valueOf(e2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.primitives.ImmutableIntArray.hashCode()"""
        return int.__wrap(super(ImmutableIntArray, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.primitives.ImmutableIntArray.toString()"""
        return str.__wrap(super(ImmutableIntArray, self).toString())

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int, e3: int, e4: int, e5: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int,int,int,int,int,int)"""
        return ImmutableIntArray.__wrap(__ImmutableIntArray.of(__int.valueOf(e0), __int.valueOf(e1), __int.valueOf(e2), __int.valueOf(e3), __int.valueOf(e4), __int.valueOf(e5)))

    @overload
    def trimmed(self) -> 'ImmutableIntArray':
        """public com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.trimmed()"""
        return 'ImmutableIntArray'.__wrap(super(ImmutableIntArray, self).trimmed())

    @overload
    def subArray(self, startIndex: int, endIndex: int) -> 'ImmutableIntArray':
        """public com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.subArray(int,int)"""
        return 'ImmutableIntArray'.__wrap(super(__ImmutableIntArray, self).subArray(__int.valueOf(startIndex), __int.valueOf(endIndex)))

    @overload
    def indexOf(self, target: int) -> int:
        """public int com.google.common.primitives.ImmutableIntArray.indexOf(int)"""
        return int.__wrap(super(__ImmutableIntArray, self).indexOf(__int.valueOf(target)))

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int, e3: int, e4: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int,int,int,int,int)"""
        return ImmutableIntArray.__wrap(__ImmutableIntArray.of(__int.valueOf(e0), __int.valueOf(e1), __int.valueOf(e2), __int.valueOf(e3), __int.valueOf(e4)))

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int, e3: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int,int,int,int)"""
        return ImmutableIntArray.__wrap(__ImmutableIntArray.of(__int.valueOf(e0), __int.valueOf(e1), __int.valueOf(e2), __int.valueOf(e3)))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.primitives.ImmutableIntArray.isEmpty()"""
        return bool.__wrap(super(ImmutableIntArray, self).isEmpty())

    @staticmethod
    @overload
    def builder(initialCapacity: int) -> 'Builder':
        """public static com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray.builder(int)"""
        return Builder.__wrap(__ImmutableIntArray.builder(__int.valueOf(initialCapacity)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def copyOf(values: 'Collection') -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.copyOf(java.util.Collection<java.lang.Integer>)"""
        return ImmutableIntArray.__wrap(__ImmutableIntArray.copyOf(values))

    @staticmethod
    @overload
    def copyOf(values: 'int') -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.copyOf(int[])"""
        return ImmutableIntArray.__wrap(__ImmutableIntArray.copyOf(values))

    @staticmethod
    @overload
    def of(e0: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int)"""
        return ImmutableIntArray.__wrap(__ImmutableIntArray.of(__int.valueOf(e0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray.builder()"""
        return Builder.__wrap(__ImmutableIntArray.builder())

    @overload
    def asList(self) -> 'List':
        """public java.util.List<java.lang.Integer> com.google.common.primitives.ImmutableIntArray.asList()"""
        return 'List'.__wrap(super(ImmutableIntArray, self).asList())

    @staticmethod
    @overload
    def of(e0: int, e1: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int,int)"""
        return ImmutableIntArray.__wrap(__ImmutableIntArray.of(__int.valueOf(e0), __int.valueOf(e1)))

    @staticmethod
    @overload
    def of() -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of()"""
        return ImmutableIntArray.__wrap(__ImmutableIntArray.of())

    @overload
    def forEach(self, consumer: 'IntConsumer'):
        """public void com.google.common.primitives.ImmutableIntArray.forEach(java.util.function.IntConsumer)"""
        super(__ImmutableIntArray, self).forEach(consumer)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def copyOf(values: 'Iterable') -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.copyOf(java.lang.Iterable<java.lang.Integer>)"""
        return ImmutableIntArray.__wrap(__ImmutableIntArray.copyOf(values)) 
 
 
# CLASS: com.google.common.primitives.ImmutableLongArray$Builder
from builtins import str
from pyquantum_helper import override
import com.google.common.primitives.ImmutableLongArray as __ImmutableLongArray_Builder
__Builder = __ImmutableLongArray_Builder.Builder
import java.lang.Object as __object
from builtins import type
import com.google.common.primitives.ImmutableLongArray as __ImmutableLongArray
__ImmutableLongArray = __ImmutableLongArray
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.stream.LongStream as LongStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Builder():
    """com.google.common.primitives.ImmutableLongArray.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def addAll(self, values: 'long') -> 'Builder':
        """public com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray$Builder.addAll(long[])"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(values))

    @overload
    def addAll(self, values: 'Collection') -> 'Builder':
        """public com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray$Builder.addAll(java.util.Collection<java.lang.Long>)"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(values))

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
    def add(self, value: int) -> 'Builder':
        """public com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray$Builder.add(long)"""
        return 'Builder'.__wrap(super(__Builder, self).add(__long.valueOf(value)))

    @overload
    def addAll(self, values: 'Iterable') -> 'Builder':
        """public com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray$Builder.addAll(java.lang.Iterable<java.lang.Long>)"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(values))

    @overload
    def build(self) -> 'ImmutableLongArray':
        """public com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray$Builder.build()"""
        return 'ImmutableLongArray'.__wrap(super(Builder, self).build())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def addAll(self, values: 'ImmutableLongArray') -> 'Builder':
        """public com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray$Builder.addAll(com.google.common.primitives.ImmutableLongArray)"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(values))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addAll(self, stream: 'LongStream') -> 'Builder':
        """public com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray$Builder.addAll(java.util.stream.LongStream)"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(stream))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.primitives.UnsignedBytes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.primitives.UnsignedBytes as __UnsignedBytes
__UnsignedBytes = __UnsignedBytes
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UnsignedBytes():
    """com.google.common.primitives.UnsignedBytes"""
 
    @staticmethod
    def __wrap(java_value: __UnsignedBytes) -> 'UnsignedBytes':
        return UnsignedBytes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnsignedBytes):
        """
        Dynamic initializer for UnsignedBytes.
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

    @staticmethod
    @overload
    def checkedCast(value: int) -> int:
        """public static byte com.google.common.primitives.UnsignedBytes.checkedCast(long)"""
        return int.__wrap(__UnsignedBytes.checkedCast(__long.valueOf(value)))

    @staticmethod
    @overload
    def toString(x: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedBytes.toString(byte)"""
        return str.__wrap(__UnsignedBytes.toString(__byte.valueOf(x)))

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.UnsignedBytes.compare(byte,byte)"""
        return int.__wrap(__UnsignedBytes.compare(__byte.valueOf(a), __byte.valueOf(b)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static byte com.google.common.primitives.UnsignedBytes.min(byte...)"""
        return int.__wrap(__UnsignedBytes.min(bytes))

    @staticmethod
    @overload
    def sort(array: bytes):
        """public static void com.google.common.primitives.UnsignedBytes.sort(byte[])"""
        __UnsignedBytes.sort(bytes)

    @staticmethod
    @overload
    def sortDescending(array: bytes, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedBytes.sortDescending(byte[],int,int)"""
        __UnsignedBytes.sortDescending(bytes, __int.valueOf(fromIndex), __int.valueOf(toIndex))

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

    @staticmethod
    @overload
    def saturatedCast(value: int) -> int:
        """public static byte com.google.common.primitives.UnsignedBytes.saturatedCast(long)"""
        return int.__wrap(__UnsignedBytes.saturatedCast(__long.valueOf(value)))

    @staticmethod
    @overload
    def parseUnsignedByte(string: str, radix: int) -> int:
        """public static byte com.google.common.primitives.UnsignedBytes.parseUnsignedByte(java.lang.String,int)"""
        return int.__wrap(__UnsignedBytes.parseUnsignedByte(string, __int.valueOf(radix)))

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedBytes.join(java.lang.String,byte...)"""
        return str.__wrap(__UnsignedBytes.join(separator, bytes))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static byte com.google.common.primitives.UnsignedBytes.max(byte...)"""
        return int.__wrap(__UnsignedBytes.max(bytes))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def sort(array: bytes, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedBytes.sort(byte[],int,int)"""
        __UnsignedBytes.sort(bytes, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<byte[]> com.google.common.primitives.UnsignedBytes.lexicographicalComparator()"""
        return Comparator.__wrap(__UnsignedBytes.lexicographicalComparator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def parseUnsignedByte(string: str) -> int:
        """public static byte com.google.common.primitives.UnsignedBytes.parseUnsignedByte(java.lang.String)"""
        return int.__wrap(__UnsignedBytes.parseUnsignedByte(string))

    @staticmethod
    @overload
    def sortDescending(array: bytes):
        """public static void com.google.common.primitives.UnsignedBytes.sortDescending(byte[])"""
        __UnsignedBytes.sortDescending(bytes)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toString(x: int, radix: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedBytes.toString(byte,int)"""
        return str.__wrap(__UnsignedBytes.toString(__byte.valueOf(x), __int.valueOf(radix)))

    @staticmethod
    @overload
    def toInt(value: int) -> int:
        """public static int com.google.common.primitives.UnsignedBytes.toInt(byte)"""
        return int.__wrap(__UnsignedBytes.toInt(__byte.valueOf(value))) 
 
 
# CLASS: com.google.common.primitives.Primitives
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import com.google.common.primitives.Primitives as __Primitives
__Primitives = __Primitives
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Primitives():
    """com.google.common.primitives.Primitives"""
 
    @staticmethod
    def __wrap(java_value: __Primitives) -> 'Primitives':
        return Primitives(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Primitives):
        """
        Dynamic initializer for Primitives.
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def wrap(type: 'Class') -> 'type.Class':
        """public static <T> java.lang.Class<T> com.google.common.primitives.Primitives.wrap(java.lang.Class<T>)"""
        return type.Class.__wrap(__Primitives.wrap(type))

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
    def allWrapperTypes() -> 'Set':
        """public static java.util.Set<java.lang.Class<?>> com.google.common.primitives.Primitives.allWrapperTypes()"""
        return Set.__wrap(__Primitives.allWrapperTypes())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def unwrap(type: 'Class') -> 'type.Class':
        """public static <T> java.lang.Class<T> com.google.common.primitives.Primitives.unwrap(java.lang.Class<T>)"""
        return type.Class.__wrap(__Primitives.unwrap(type))

    @staticmethod
    @overload
    def isWrapperType(type: 'Class') -> bool:
        """public static boolean com.google.common.primitives.Primitives.isWrapperType(java.lang.Class<?>)"""
        return bool.__wrap(__Primitives.isWrapperType(type))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def allPrimitiveTypes() -> 'Set':
        """public static java.util.Set<java.lang.Class<?>> com.google.common.primitives.Primitives.allPrimitiveTypes()"""
        return Set.__wrap(__Primitives.allPrimitiveTypes()) 
 
 
# CLASS: com.google.common.primitives.Floats
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
import com.google.common.base.Converter as __Converter
__Converter = __Converter
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Float as Float
import java.util.Collection as Collection
from typing import List
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.primitives.Floats as __Floats
__Floats = __Floats
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class Floats():
    """com.google.common.primitives.Floats"""
 
    @staticmethod
    def __wrap(java_value: __Floats) -> 'Floats':
        return Floats(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Floats):
        """
        Dynamic initializer for Floats.
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

    @staticmethod
    @overload
    def lastIndexOf(array: 'float', target: float) -> int:
        """public static int com.google.common.primitives.Floats.lastIndexOf(float[],float)"""
        return int.__wrap(__Floats.lastIndexOf(array, __float.valueOf(target)))

    @staticmethod
    @overload
    def join(separator: str, *array: float) -> str:
        """public static java.lang.String com.google.common.primitives.Floats.join(java.lang.String,float...)"""
        return str.__wrap(__Floats.join(separator, array))

    @staticmethod
    @overload
    def sortDescending(array: 'float', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Floats.sortDescending(float[],int,int)"""
        __Floats.sortDescending(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def stringConverter() -> 'base.Converter':
        """public static com.google.common.base.Converter<java.lang.String, java.lang.Float> com.google.common.primitives.Floats.stringConverter()"""
        return base.Converter.__wrap(__Floats.stringConverter())

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[float]:
        """public static float[] com.google.common.primitives.Floats.toArray(java.util.Collection<? extends java.lang.Number>)"""
        return List[float].__wrap(__Floats.toArray(collection))

    @staticmethod
    @overload
    def sortDescending(array: 'float'):
        """public static void com.google.common.primitives.Floats.sortDescending(float[])"""
        __Floats.sortDescending(array)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def reverse(array: 'float', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Floats.reverse(float[],int,int)"""
        __Floats.reverse(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def compare(a: float, b: float) -> int:
        """public static int com.google.common.primitives.Floats.compare(float,float)"""
        return int.__wrap(__Floats.compare(__float.valueOf(a), __float.valueOf(b)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isFinite(value: float) -> bool:
        """public static boolean com.google.common.primitives.Floats.isFinite(float)"""
        return bool.__wrap(__Floats.isFinite(__float.valueOf(value)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def rotate(array: 'float', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Floats.rotate(float[],int,int,int)"""
        __Floats.rotate(array, __int.valueOf(distance), __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def ensureCapacity(array: 'float', minLength: int, padding: int) -> List[float]:
        """public static float[] com.google.common.primitives.Floats.ensureCapacity(float[],int,int)"""
        return List[float].__wrap(__Floats.ensureCapacity(array, __int.valueOf(minLength), __int.valueOf(padding)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def contains(array: 'float', target: float) -> bool:
        """public static boolean com.google.common.primitives.Floats.contains(float[],float)"""
        return bool.__wrap(__Floats.contains(array, __float.valueOf(target)))

    @staticmethod
    @overload
    def max(*array: float) -> float:
        """public static float com.google.common.primitives.Floats.max(float...)"""
        return float.__wrap(__Floats.max(array))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def concat(*arrays: List[float]) -> List[float]:
        """public static float[] com.google.common.primitives.Floats.concat(float[]...)"""
        return List[float].__wrap(__Floats.concat(arrays))

    @staticmethod
    @overload
    def constrainToRange(value: float, min: float, max: float) -> float:
        """public static float com.google.common.primitives.Floats.constrainToRange(float,float,float)"""
        return float.__wrap(__Floats.constrainToRange(__float.valueOf(value), __float.valueOf(min), __float.valueOf(max)))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<float[]> com.google.common.primitives.Floats.lexicographicalComparator()"""
        return Comparator.__wrap(__Floats.lexicographicalComparator())

    @staticmethod
    @overload
    def reverse(array: 'float'):
        """public static void com.google.common.primitives.Floats.reverse(float[])"""
        __Floats.reverse(array)

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
    def rotate(array: 'float', distance: int):
        """public static void com.google.common.primitives.Floats.rotate(float[],int)"""
        __Floats.rotate(array, __int.valueOf(distance))

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Float':
        """public static java.lang.Float com.google.common.primitives.Floats.tryParse(java.lang.String)"""
        return __transform(__string.Floats(string: str)).'Float'Value()

    @staticmethod
    @overload
    def indexOf(array: 'float', target: float) -> int:
        """public static int com.google.common.primitives.Floats.indexOf(float[],float)"""
        return int.__wrap(__Floats.indexOf(array, __float.valueOf(target)))

    @staticmethod
    @overload
    def asList(*backingArray: float) -> 'List':
        """public static java.util.List<java.lang.Float> com.google.common.primitives.Floats.asList(float...)"""
        return List.__wrap(__Floats.asList(backingArray))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def min(*array: float) -> float:
        """public static float com.google.common.primitives.Floats.min(float...)"""
        return float.__wrap(__Floats.min(array))

    @staticmethod
    @overload
    def hashCode(value: float) -> int:
        """public static int com.google.common.primitives.Floats.hashCode(float)"""
        return int.__wrap(__Floats.hashCode(__float.valueOf(value)))

    @staticmethod
    @overload
    def indexOf(array: 'float', target: 'float') -> int:
        """public static int com.google.common.primitives.Floats.indexOf(float[],float[])"""
        return int.__wrap(__Floats.indexOf(array, target)) 
 
 
# CLASS: com.google.common.primitives.ImmutableDoubleArray$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.Long as __long
import com.google.common.primitives.ImmutableDoubleArray as __ImmutableDoubleArray_Builder
__Builder = __ImmutableDoubleArray_Builder.Builder
import java.lang.Class as __Class
__Class = __Class
import com.google.common.primitives.ImmutableDoubleArray as __ImmutableDoubleArray
__ImmutableDoubleArray = __ImmutableDoubleArray
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.DoubleStream as DoubleStream
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Builder():
    """com.google.common.primitives.ImmutableDoubleArray.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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
    def addAll(self, values: 'Iterable') -> 'Builder':
        """public com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray$Builder.addAll(java.lang.Iterable<java.lang.Double>)"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(values))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def add(self, value: float) -> 'Builder':
        """public com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray$Builder.add(double)"""
        return 'Builder'.__wrap(super(__Builder, self).add(__double.valueOf(value)))

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
    def addAll(self, stream: 'DoubleStream') -> 'Builder':
        """public com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray$Builder.addAll(java.util.stream.DoubleStream)"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(stream))

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
    def addAll(self, values: 'ImmutableDoubleArray') -> 'Builder':
        """public com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray$Builder.addAll(com.google.common.primitives.ImmutableDoubleArray)"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(values))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def addAll(self, values: 'Collection') -> 'Builder':
        """public com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray$Builder.addAll(java.util.Collection<java.lang.Double>)"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(values))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addAll(self, values: 'double') -> 'Builder':
        """public com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray$Builder.addAll(double[])"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(values))

    @overload
    def build(self) -> 'ImmutableDoubleArray':
        """public com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray$Builder.build()"""
        return 'ImmutableDoubleArray'.__wrap(super(Builder, self).build())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.primitives.Booleans
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
import com.google.common.primitives.Booleans as __Booleans
__Booleans = __Booleans
from typing import List
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class Booleans():
    """com.google.common.primitives.Booleans"""
 
    @staticmethod
    def __wrap(java_value: __Booleans) -> 'Booleans':
        return Booleans(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Booleans):
        """
        Dynamic initializer for Booleans.
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
 
    @staticmethod
    @overload
    def compare(a: bool, b: bool) -> int:
        """public static int com.google.common.primitives.Booleans.compare(boolean,boolean)"""
        return int.__wrap(__Booleans.compare(__boolean.valueOf(a), __boolean.valueOf(b)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def concat(*arrays: List[bool]) -> List[bool]:
        """public static boolean[] com.google.common.primitives.Booleans.concat(boolean[]...)"""
        return List[bool].__wrap(__Booleans.concat(arrays))

    @staticmethod
    @overload
    def rotate(array: 'boolean', distance: int):
        """public static void com.google.common.primitives.Booleans.rotate(boolean[],int)"""
        __Booleans.rotate(array, __int.valueOf(distance))

    @staticmethod
    @overload
    def indexOf(array: 'boolean', target: 'boolean') -> int:
        """public static int com.google.common.primitives.Booleans.indexOf(boolean[],boolean[])"""
        return int.__wrap(__Booleans.indexOf(array, target))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def asList(*backingArray: bool) -> 'List':
        """public static java.util.List<java.lang.Boolean> com.google.common.primitives.Booleans.asList(boolean...)"""
        return List.__wrap(__Booleans.asList(backingArray))

    @staticmethod
    @overload
    def reverse(array: 'boolean'):
        """public static void com.google.common.primitives.Booleans.reverse(boolean[])"""
        __Booleans.reverse(array)

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<boolean[]> com.google.common.primitives.Booleans.lexicographicalComparator()"""
        return Comparator.__wrap(__Booleans.lexicographicalComparator())

    @staticmethod
    @overload
    def join(separator: str, *array: bool) -> str:
        """public static java.lang.String com.google.common.primitives.Booleans.join(java.lang.String,boolean...)"""
        return str.__wrap(__Booleans.join(separator, array))

    @staticmethod
    @overload
    def contains(array: 'boolean', target: bool) -> bool:
        """public static boolean com.google.common.primitives.Booleans.contains(boolean[],boolean)"""
        return bool.__wrap(__Booleans.contains(array, __boolean.valueOf(target)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def reverse(array: 'boolean', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Booleans.reverse(boolean[],int,int)"""
        __Booleans.reverse(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def lastIndexOf(array: 'boolean', target: bool) -> int:
        """public static int com.google.common.primitives.Booleans.lastIndexOf(boolean[],boolean)"""
        return int.__wrap(__Booleans.lastIndexOf(array, __boolean.valueOf(target)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def trueFirst() -> 'Comparator':
        """public static java.util.Comparator<java.lang.Boolean> com.google.common.primitives.Booleans.trueFirst()"""
        return Comparator.__wrap(__Booleans.trueFirst())

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[bool]:
        """public static boolean[] com.google.common.primitives.Booleans.toArray(java.util.Collection<java.lang.Boolean>)"""
        return List[bool].__wrap(__Booleans.toArray(collection))

    @staticmethod
    @overload
    def falseFirst() -> 'Comparator':
        """public static java.util.Comparator<java.lang.Boolean> com.google.common.primitives.Booleans.falseFirst()"""
        return Comparator.__wrap(__Booleans.falseFirst())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def countTrue(*values: bool) -> int:
        """public static int com.google.common.primitives.Booleans.countTrue(boolean...)"""
        return int.__wrap(__Booleans.countTrue(values))

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
    def hashCode(value: bool) -> int:
        """public static int com.google.common.primitives.Booleans.hashCode(boolean)"""
        return int.__wrap(__Booleans.hashCode(__boolean.valueOf(value)))

    @staticmethod
    @overload
    def indexOf(array: 'boolean', target: bool) -> int:
        """public static int com.google.common.primitives.Booleans.indexOf(boolean[],boolean)"""
        return int.__wrap(__Booleans.indexOf(array, __boolean.valueOf(target)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def rotate(array: 'boolean', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Booleans.rotate(boolean[],int,int,int)"""
        __Booleans.rotate(array, __int.valueOf(distance), __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def ensureCapacity(array: 'boolean', minLength: int, padding: int) -> List[bool]:
        """public static boolean[] com.google.common.primitives.Booleans.ensureCapacity(boolean[],int,int)"""
        return List[bool].__wrap(__Booleans.ensureCapacity(array, __int.valueOf(minLength), __int.valueOf(padding))) 
 
 
# CLASS: com.google.common.primitives.UnsignedLong
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.google.common.primitives.UnsignedLong as __UnsignedLong
__UnsignedLong = __UnsignedLong
import java.lang.Long as __long
import java.math.BigInteger as BigInteger
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Number as __Number
__Number = __Number
from builtins import int
 
class UnsignedLong():
    """com.google.common.primitives.UnsignedLong"""
 
    @staticmethod
    def __wrap(java_value: __UnsignedLong) -> 'UnsignedLong':
        return UnsignedLong(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnsignedLong):
        """
        Dynamic initializer for UnsignedLong.
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
    def minus(self, val: 'UnsignedLong') -> 'UnsignedLong':
        """public com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.minus(com.google.common.primitives.UnsignedLong)"""
        return __transform(super(__UnsignedLong, self).minus(val)).'UnsignedLong'Value()

    @override
    @overload
    def doubleValue(self) -> float:
        """public double com.google.common.primitives.UnsignedLong.doubleValue()"""
        return float.__wrap(super(UnsignedLong, self).doubleValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def bigIntegerValue(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.common.primitives.UnsignedLong.bigIntegerValue()"""
        return __transform(super(UnsignedLong, self).bigIntegerValue()).'BigInteger'Value()

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.primitives.UnsignedLong.equals(java.lang.Object)"""
        return bool.__wrap(super(__UnsignedLong, self).equals(obj))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def fromLongBits(fromLongBits) -> 'UnsignedLong':
        """public static com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.fromLongBits(long)"""
        return __transform(____long.valueOf(bits).UnsignedLong(bits: int)).'UnsignedLong'Value()

    @overload
    def plus(self, val: 'UnsignedLong') -> 'UnsignedLong':
        """public com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.plus(com.google.common.primitives.UnsignedLong)"""
        return __transform(super(__UnsignedLong, self).plus(val)).'UnsignedLong'Value()

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedLong':
        """public static com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.valueOf(java.lang.String,int)"""
        return __transform(__string, __int.valueOf(radix).UnsignedLong(string: str, radix: int)).'UnsignedLong'Value()

    @overload
    def mod(self, val: 'UnsignedLong') -> 'UnsignedLong':
        """public com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.mod(com.google.common.primitives.UnsignedLong)"""
        return __transform(super(__UnsignedLong, self).mod(val)).'UnsignedLong'Value()

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedLong':
        """public static com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.valueOf(long)"""
        return __transform(____long.valueOf(value).UnsignedLong(value: int)).'UnsignedLong'Value()

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedLong':
        """public static com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.valueOf(java.lang.String)"""
        return __transform(__string.UnsignedLong(string: str)).'UnsignedLong'Value()

    @overload
    def times(self, val: 'UnsignedLong') -> 'UnsignedLong':
        """public com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.times(com.google.common.primitives.UnsignedLong)"""
        return __transform(super(__UnsignedLong, self).times(val)).'UnsignedLong'Value()

    @overload
    def dividedBy(self, val: 'UnsignedLong') -> 'UnsignedLong':
        """public com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.dividedBy(com.google.common.primitives.UnsignedLong)"""
        return __transform(super(__UnsignedLong, self).dividedBy(val)).'UnsignedLong'Value()

    @overload
    def toString(self, radix: int) -> str:
        """public java.lang.String com.google.common.primitives.UnsignedLong.toString(int)"""
        return str.__wrap(super(__UnsignedLong, self).toString(__int.valueOf(radix)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.primitives.UnsignedLong.hashCode()"""
        return int.__wrap(super(UnsignedLong, self).hashCode())

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int.__wrap(super(Number, self).shortValue())

    @overload
    def compareTo(self, o: 'UnsignedLong') -> int:
        """public int com.google.common.primitives.UnsignedLong.compareTo(com.google.common.primitives.UnsignedLong)"""
        return int.__wrap(super(__UnsignedLong, self).compareTo(o))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def longValue(self) -> int:
        """public long com.google.common.primitives.UnsignedLong.longValue()"""
        return int.__wrap(super(UnsignedLong, self).longValue())

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int.__wrap(super(Number, self).byteValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def floatValue(self) -> float:
        """public float com.google.common.primitives.UnsignedLong.floatValue()"""
        return float.__wrap(super(UnsignedLong, self).floatValue())

    @override
    @overload
    def intValue(self) -> int:
        """public int com.google.common.primitives.UnsignedLong.intValue()"""
        return int.__wrap(super(UnsignedLong, self).intValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedLong':
        """public static com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.valueOf(java.math.BigInteger)"""
        return __transform(__value.UnsignedLong(value: 'BigInteger')).'UnsignedLong'Value()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.primitives.UnsignedLong.toString()"""
        return str.__wrap(super(UnsignedLong, self).toString()) 
 
 
# CLASS: com.google.common.primitives.ImmutableIntArray$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.primitives.ImmutableIntArray as __ImmutableIntArray_Builder
__Builder = __ImmutableIntArray_Builder.Builder
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import com.google.common.primitives.ImmutableIntArray as __ImmutableIntArray
__ImmutableIntArray = __ImmutableIntArray
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.stream.IntStream as IntStream
from builtins import bool
from builtins import int
 
class Builder():
    """com.google.common.primitives.ImmutableIntArray.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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
    def addAll(self, values: 'Iterable') -> 'Builder':
        """public com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray$Builder.addAll(java.lang.Iterable<java.lang.Integer>)"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(values))

    @overload
    def addAll(self, values: 'int') -> 'Builder':
        """public com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray$Builder.addAll(int[])"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(values))

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

    @overload
    def build(self) -> 'ImmutableIntArray':
        """public com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray$Builder.build()"""
        return 'ImmutableIntArray'.__wrap(super(Builder, self).build())

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

    @overload
    def addAll(self, values: 'Collection') -> 'Builder':
        """public com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray$Builder.addAll(java.util.Collection<java.lang.Integer>)"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(values))

    @overload
    def addAll(self, stream: 'IntStream') -> 'Builder':
        """public com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray$Builder.addAll(java.util.stream.IntStream)"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(stream))

    @overload
    def add(self, value: int) -> 'Builder':
        """public com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray$Builder.add(int)"""
        return 'Builder'.__wrap(super(__Builder, self).add(__int.valueOf(value)))

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

    @overload
    def addAll(self, values: 'ImmutableIntArray') -> 'Builder':
        """public com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray$Builder.addAll(com.google.common.primitives.ImmutableIntArray)"""
        return 'Builder'.__wrap(super(__Builder, self).addAll(values))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.primitives.SignedBytes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.google.common.primitives.SignedBytes as __SignedBytes
__SignedBytes = __SignedBytes
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SignedBytes():
    """com.google.common.primitives.SignedBytes"""
 
    @staticmethod
    def __wrap(java_value: __SignedBytes) -> 'SignedBytes':
        return SignedBytes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SignedBytes):
        """
        Dynamic initializer for SignedBytes.
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

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<byte[]> com.google.common.primitives.SignedBytes.lexicographicalComparator()"""
        return Comparator.__wrap(__SignedBytes.lexicographicalComparator())

    @staticmethod
    @overload
    def sortDescending(array: bytes, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.SignedBytes.sortDescending(byte[],int,int)"""
        __SignedBytes.sortDescending(bytes, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def saturatedCast(value: int) -> int:
        """public static byte com.google.common.primitives.SignedBytes.saturatedCast(long)"""
        return int.__wrap(__SignedBytes.saturatedCast(__long.valueOf(value)))

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static byte com.google.common.primitives.SignedBytes.min(byte...)"""
        return int.__wrap(__SignedBytes.min(bytes))

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

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static byte com.google.common.primitives.SignedBytes.max(byte...)"""
        return int.__wrap(__SignedBytes.max(bytes))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.SignedBytes.join(java.lang.String,byte...)"""
        return str.__wrap(__SignedBytes.join(separator, bytes))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def sortDescending(array: bytes):
        """public static void com.google.common.primitives.SignedBytes.sortDescending(byte[])"""
        __SignedBytes.sortDescending(bytes)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.SignedBytes.compare(byte,byte)"""
        return int.__wrap(__SignedBytes.compare(__byte.valueOf(a), __byte.valueOf(b)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def checkedCast(value: int) -> int:
        """public static byte com.google.common.primitives.SignedBytes.checkedCast(long)"""
        return int.__wrap(__SignedBytes.checkedCast(__long.valueOf(value))) 
 
 
# CLASS: com.google.common.primitives.UnsignedLongs
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.primitives.UnsignedLongs as __UnsignedLongs
__UnsignedLongs = __UnsignedLongs
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UnsignedLongs():
    """com.google.common.primitives.UnsignedLongs"""
 
    @staticmethod
    def __wrap(java_value: __UnsignedLongs) -> 'UnsignedLongs':
        return UnsignedLongs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnsignedLongs):
        """
        Dynamic initializer for UnsignedLongs.
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

    @staticmethod
    @overload
    def toString(x: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedLongs.toString(long)"""
        return str.__wrap(__UnsignedLongs.toString(__long.valueOf(x)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def parseUnsignedLong(string: str) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.parseUnsignedLong(java.lang.String)"""
        return int.__wrap(__UnsignedLongs.parseUnsignedLong(string))

    @staticmethod
    @overload
    def sortDescending(array: 'long', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedLongs.sortDescending(long[],int,int)"""
        __UnsignedLongs.sortDescending(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.UnsignedLongs.compare(long,long)"""
        return int.__wrap(__UnsignedLongs.compare(__long.valueOf(a), __long.valueOf(b)))

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

    @staticmethod
    @overload
    def toString(x: int, radix: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedLongs.toString(long,int)"""
        return str.__wrap(__UnsignedLongs.toString(__long.valueOf(x), __int.valueOf(radix)))

    @staticmethod
    @overload
    def divide(dividend: int, divisor: int) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.divide(long,long)"""
        return int.__wrap(__UnsignedLongs.divide(__long.valueOf(dividend), __long.valueOf(divisor)))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<long[]> com.google.common.primitives.UnsignedLongs.lexicographicalComparator()"""
        return Comparator.__wrap(__UnsignedLongs.lexicographicalComparator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def decode(stringValue: str) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.decode(java.lang.String)"""
        return int.__wrap(__UnsignedLongs.decode(stringValue))

    @staticmethod
    @overload
    def sort(array: 'long', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedLongs.sort(long[],int,int)"""
        __UnsignedLongs.sort(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def parseUnsignedLong(string: str, radix: int) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.parseUnsignedLong(java.lang.String,int)"""
        return int.__wrap(__UnsignedLongs.parseUnsignedLong(string, __int.valueOf(radix)))

    @staticmethod
    @overload
    def remainder(dividend: int, divisor: int) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.remainder(long,long)"""
        return int.__wrap(__UnsignedLongs.remainder(__long.valueOf(dividend), __long.valueOf(divisor)))

    @staticmethod
    @overload
    def sortDescending(array: 'long'):
        """public static void com.google.common.primitives.UnsignedLongs.sortDescending(long[])"""
        __UnsignedLongs.sortDescending(array)

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedLongs.join(java.lang.String,long...)"""
        return str.__wrap(__UnsignedLongs.join(separator, array))

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
    def min(*array: int) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.min(long...)"""
        return int.__wrap(__UnsignedLongs.min(array))

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.max(long...)"""
        return int.__wrap(__UnsignedLongs.max(array))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def sort(array: 'long'):
        """public static void com.google.common.primitives.UnsignedLongs.sort(long[])"""
        __UnsignedLongs.sort(array) 
 
 
# CLASS: com.google.common.primitives.ImmutableLongArray
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.primitives.ImmutableLongArray as __ImmutableLongArray_Builder
__Builder = __ImmutableLongArray_Builder.Builder
import java.util.function.LongConsumer as LongConsumer
from builtins import type
import com.google.common.primitives.ImmutableLongArray as __ImmutableLongArray
__ImmutableLongArray = __ImmutableLongArray
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
from typing import List
import java.util.stream.LongStream as __LongStream
__LongStream = __LongStream
import java.lang.Long as __long
import java.util.List as __List
__List = __List
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.stream.LongStream as LongStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class ImmutableLongArray():
    """com.google.common.primitives.ImmutableLongArray"""
 
    @staticmethod
    def __wrap(java_value: __ImmutableLongArray) -> 'ImmutableLongArray':
        return ImmutableLongArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImmutableLongArray):
        """
        Dynamic initializer for ImmutableLongArray.
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

    @staticmethod
    @overload
    def of() -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of()"""
        return ImmutableLongArray.__wrap(__ImmutableLongArray.of())

    @staticmethod
    @overload
    def of(first: int, *rest: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long,long...)"""
        return ImmutableLongArray.__wrap(__ImmutableLongArray.of(__long.valueOf(first), rest))

    @overload
    def forEach(self, consumer: 'LongConsumer'):
        """public void com.google.common.primitives.ImmutableLongArray.forEach(java.util.function.LongConsumer)"""
        super(__ImmutableLongArray, self).forEach(consumer)

    @staticmethod
    @overload
    def copyOf(values: 'Iterable') -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.copyOf(java.lang.Iterable<java.lang.Long>)"""
        return ImmutableLongArray.__wrap(__ImmutableLongArray.copyOf(values))

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int, e3: int, e4: int, e5: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long,long,long,long,long,long)"""
        return ImmutableLongArray.__wrap(__ImmutableLongArray.of(__long.valueOf(e0), __long.valueOf(e1), __long.valueOf(e2), __long.valueOf(e3), __long.valueOf(e4), __long.valueOf(e5)))

    @overload
    def toArray(self) -> List[int]:
        """public long[] com.google.common.primitives.ImmutableLongArray.toArray()"""
        return List[int].__wrap(super(ImmutableLongArray, self).toArray())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.primitives.ImmutableLongArray.hashCode()"""
        return int.__wrap(super(ImmutableLongArray, self).hashCode())

    @overload
    def lastIndexOf(self, target: int) -> int:
        """public int com.google.common.primitives.ImmutableLongArray.lastIndexOf(long)"""
        return int.__wrap(super(__ImmutableLongArray, self).lastIndexOf(__long.valueOf(target)))

    @overload
    def get(self, index: int) -> int:
        """public long com.google.common.primitives.ImmutableLongArray.get(int)"""
        return int.__wrap(super(__ImmutableLongArray, self).get(__int.valueOf(index)))

    @staticmethod
    @overload
    def copyOf(stream: 'LongStream') -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.copyOf(java.util.stream.LongStream)"""
        return ImmutableLongArray.__wrap(__ImmutableLongArray.copyOf(stream))

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray.builder()"""
        return Builder.__wrap(__ImmutableLongArray.builder())

    @staticmethod
    @overload
    def of(e0: int, e1: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long,long)"""
        return ImmutableLongArray.__wrap(__ImmutableLongArray.of(__long.valueOf(e0), __long.valueOf(e1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def length(self) -> int:
        """public int com.google.common.primitives.ImmutableLongArray.length()"""
        return int.__wrap(super(ImmutableLongArray, self).length())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.primitives.ImmutableLongArray.isEmpty()"""
        return bool.__wrap(super(ImmutableLongArray, self).isEmpty())

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.primitives.ImmutableLongArray.equals(java.lang.Object)"""
        return bool.__wrap(super(__ImmutableLongArray, self).equals(object))

    @staticmethod
    @overload
    def of(e0: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long)"""
        return ImmutableLongArray.__wrap(__ImmutableLongArray.of(__long.valueOf(e0)))

    @overload
    def contains(self, target: int) -> bool:
        """public boolean com.google.common.primitives.ImmutableLongArray.contains(long)"""
        return bool.__wrap(super(__ImmutableLongArray, self).contains(__long.valueOf(target)))

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long,long,long)"""
        return ImmutableLongArray.__wrap(__ImmutableLongArray.of(__long.valueOf(e0), __long.valueOf(e1), __long.valueOf(e2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.primitives.ImmutableLongArray.toString()"""
        return str.__wrap(super(ImmutableLongArray, self).toString())

    @overload
    def asList(self) -> 'List':
        """public java.util.List<java.lang.Long> com.google.common.primitives.ImmutableLongArray.asList()"""
        return 'List'.__wrap(super(ImmutableLongArray, self).asList())

    @overload
    def subArray(self, startIndex: int, endIndex: int) -> 'ImmutableLongArray':
        """public com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.subArray(int,int)"""
        return 'ImmutableLongArray'.__wrap(super(__ImmutableLongArray, self).subArray(__int.valueOf(startIndex), __int.valueOf(endIndex)))

    @overload
    def indexOf(self, target: int) -> int:
        """public int com.google.common.primitives.ImmutableLongArray.indexOf(long)"""
        return int.__wrap(super(__ImmutableLongArray, self).indexOf(__long.valueOf(target)))

    @overload
    def stream(self) -> 'LongStream':
        """public java.util.stream.LongStream com.google.common.primitives.ImmutableLongArray.stream()"""
        return 'LongStream'.__wrap(super(ImmutableLongArray, self).stream())

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
    def copyOf(values: 'long') -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.copyOf(long[])"""
        return ImmutableLongArray.__wrap(__ImmutableLongArray.copyOf(values))

    @staticmethod
    @overload
    def copyOf(values: 'Collection') -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.copyOf(java.util.Collection<java.lang.Long>)"""
        return ImmutableLongArray.__wrap(__ImmutableLongArray.copyOf(values))

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int, e3: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long,long,long,long)"""
        return ImmutableLongArray.__wrap(__ImmutableLongArray.of(__long.valueOf(e0), __long.valueOf(e1), __long.valueOf(e2), __long.valueOf(e3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def builder(initialCapacity: int) -> 'Builder':
        """public static com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray.builder(int)"""
        return Builder.__wrap(__ImmutableLongArray.builder(__int.valueOf(initialCapacity)))

    @overload
    def trimmed(self) -> 'ImmutableLongArray':
        """public com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.trimmed()"""
        return 'ImmutableLongArray'.__wrap(super(ImmutableLongArray, self).trimmed())

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int, e3: int, e4: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long,long,long,long,long)"""
        return ImmutableLongArray.__wrap(__ImmutableLongArray.of(__long.valueOf(e0), __long.valueOf(e1), __long.valueOf(e2), __long.valueOf(e3), __long.valueOf(e4))) 
 
 
# CLASS: com.google.common.primitives.Bytes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
from typing import List
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.primitives.Bytes as __Bytes
__Bytes = __Bytes
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class Bytes():
    """com.google.common.primitives.Bytes"""
 
    @staticmethod
    def __wrap(java_value: __Bytes) -> 'Bytes':
        return Bytes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Bytes):
        """
        Dynamic initializer for Bytes.
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

    @staticmethod
    @overload
    def hashCode(value: int) -> int:
        """public static int com.google.common.primitives.Bytes.hashCode(byte)"""
        return int.__wrap(__Bytes.hashCode(__byte.valueOf(value)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def reverse(array: bytes):
        """public static void com.google.common.primitives.Bytes.reverse(byte[])"""
        __Bytes.reverse(bytes)

    @staticmethod
    @overload
    def reverse(array: bytes, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Bytes.reverse(byte[],int,int)"""
        __Bytes.reverse(bytes, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def asList(*backingArray: int) -> 'List':
        """public static java.util.List<java.lang.Byte> com.google.common.primitives.Bytes.asList(byte...)"""
        return List.__wrap(__Bytes.asList(bytes))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ensureCapacity(array: bytes, minLength: int, padding: int) -> List[int]:
        """public static byte[] com.google.common.primitives.Bytes.ensureCapacity(byte[],int,int)"""
        return List[int].__wrap(__Bytes.ensureCapacity(bytes, __int.valueOf(minLength), __int.valueOf(padding)))

    @staticmethod
    @overload
    def indexOf(array: bytes, target: int) -> int:
        """public static int com.google.common.primitives.Bytes.indexOf(byte[],byte)"""
        return int.__wrap(__Bytes.indexOf(bytes, __byte.valueOf(target)))

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[int]:
        """public static byte[] com.google.common.primitives.Bytes.toArray(java.util.Collection<? extends java.lang.Number>)"""
        return List[int].__wrap(__Bytes.toArray(collection))

    @staticmethod
    @overload
    def rotate(array: bytes, distance: int):
        """public static void com.google.common.primitives.Bytes.rotate(byte[],int)"""
        __Bytes.rotate(bytes, __int.valueOf(distance))

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
    def lastIndexOf(array: bytes, target: int) -> int:
        """public static int com.google.common.primitives.Bytes.lastIndexOf(byte[],byte)"""
        return int.__wrap(__Bytes.lastIndexOf(bytes, __byte.valueOf(target)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def contains(array: bytes, target: int) -> bool:
        """public static boolean com.google.common.primitives.Bytes.contains(byte[],byte)"""
        return bool.__wrap(__Bytes.contains(bytes, __byte.valueOf(target)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def concat(*arrays: List[int]) -> List[int]:
        """public static byte[] com.google.common.primitives.Bytes.concat(byte[]...)"""
        return List[int].__wrap(__Bytes.concat(arrays))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def indexOf(array: bytes, target: bytes) -> int:
        """public static int com.google.common.primitives.Bytes.indexOf(byte[],byte[])"""
        return int.__wrap(__Bytes.indexOf(bytes, bytes))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def rotate(array: bytes, distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Bytes.rotate(byte[],int,int,int)"""
        __Bytes.rotate(bytes, __int.valueOf(distance), __int.valueOf(fromIndex), __int.valueOf(toIndex)) 
 
 
# CLASS: com.google.common.primitives.Shorts
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
import com.google.common.base.Converter as __Converter
__Converter = __Converter
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
from typing import List
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import com.google.common.primitives.Shorts as __Shorts
__Shorts = __Shorts
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Byte as __byte
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class Shorts():
    """com.google.common.primitives.Shorts"""
 
    @staticmethod
    def __wrap(java_value: __Shorts) -> 'Shorts':
        return Shorts(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Shorts):
        """
        Dynamic initializer for Shorts.
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
 
    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static short com.google.common.primitives.Shorts.max(short...)"""
        return int.__wrap(__Shorts.max(array))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static short com.google.common.primitives.Shorts.min(short...)"""
        return int.__wrap(__Shorts.min(array))

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[int]:
        """public static short[] com.google.common.primitives.Shorts.toArray(java.util.Collection<? extends java.lang.Number>)"""
        return List[int].__wrap(__Shorts.toArray(collection))

    @staticmethod
    @overload
    def fromBytes(b1: int, b2: int) -> int:
        """public static short com.google.common.primitives.Shorts.fromBytes(byte,byte)"""
        return int.__wrap(__Shorts.fromBytes(__byte.valueOf(b1), __byte.valueOf(b2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def asList(*backingArray: int) -> 'List':
        """public static java.util.List<java.lang.Short> com.google.common.primitives.Shorts.asList(short...)"""
        return List.__wrap(__Shorts.asList(backingArray))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def checkedCast(value: int) -> int:
        """public static short com.google.common.primitives.Shorts.checkedCast(long)"""
        return int.__wrap(__Shorts.checkedCast(__long.valueOf(value)))

    @staticmethod
    @overload
    def reverse(array: 'short'):
        """public static void com.google.common.primitives.Shorts.reverse(short[])"""
        __Shorts.reverse(array)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def ensureCapacity(array: 'short', minLength: int, padding: int) -> List[int]:
        """public static short[] com.google.common.primitives.Shorts.ensureCapacity(short[],int,int)"""
        return List[int].__wrap(__Shorts.ensureCapacity(array, __int.valueOf(minLength), __int.valueOf(padding)))

    @staticmethod
    @overload
    def stringConverter() -> 'base.Converter':
        """public static com.google.common.base.Converter<java.lang.String, java.lang.Short> com.google.common.primitives.Shorts.stringConverter()"""
        return base.Converter.__wrap(__Shorts.stringConverter())

    @staticmethod
    @overload
    def toByteArray(value: int) -> List[int]:
        """public static byte[] com.google.common.primitives.Shorts.toByteArray(short)"""
        return List[int].__wrap(__Shorts.toByteArray(__short.valueOf(value)))

    @staticmethod
    @overload
    def indexOf(array: 'short', target: int) -> int:
        """public static int com.google.common.primitives.Shorts.indexOf(short[],short)"""
        return int.__wrap(__Shorts.indexOf(array, __short.valueOf(target)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def contains(array: 'short', target: int) -> bool:
        """public static boolean com.google.common.primitives.Shorts.contains(short[],short)"""
        return bool.__wrap(__Shorts.contains(array, __short.valueOf(target)))

    @staticmethod
    @overload
    def sortDescending(array: 'short', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Shorts.sortDescending(short[],int,int)"""
        __Shorts.sortDescending(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def lastIndexOf(array: 'short', target: int) -> int:
        """public static int com.google.common.primitives.Shorts.lastIndexOf(short[],short)"""
        return int.__wrap(__Shorts.lastIndexOf(array, __short.valueOf(target)))

    @staticmethod
    @overload
    def fromByteArray(bytes: bytes) -> int:
        """public static short com.google.common.primitives.Shorts.fromByteArray(byte[])"""
        return int.__wrap(__Shorts.fromByteArray(bytes))

    @staticmethod
    @overload
    def hashCode(value: int) -> int:
        """public static int com.google.common.primitives.Shorts.hashCode(short)"""
        return int.__wrap(__Shorts.hashCode(__short.valueOf(value)))

    @staticmethod
    @overload
    def concat(*arrays: List[int]) -> List[int]:
        """public static short[] com.google.common.primitives.Shorts.concat(short[]...)"""
        return List[int].__wrap(__Shorts.concat(arrays))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.Shorts.join(java.lang.String,short...)"""
        return str.__wrap(__Shorts.join(separator, array))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<short[]> com.google.common.primitives.Shorts.lexicographicalComparator()"""
        return Comparator.__wrap(__Shorts.lexicographicalComparator())

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.Shorts.compare(short,short)"""
        return int.__wrap(__Shorts.compare(__short.valueOf(a), __short.valueOf(b)))

    @staticmethod
    @overload
    def saturatedCast(value: int) -> int:
        """public static short com.google.common.primitives.Shorts.saturatedCast(long)"""
        return int.__wrap(__Shorts.saturatedCast(__long.valueOf(value)))

    @staticmethod
    @overload
    def constrainToRange(value: int, min: int, max: int) -> int:
        """public static short com.google.common.primitives.Shorts.constrainToRange(short,short,short)"""
        return int.__wrap(__Shorts.constrainToRange(__short.valueOf(value), __short.valueOf(min), __short.valueOf(max)))

    @staticmethod
    @overload
    def rotate(array: 'short', distance: int):
        """public static void com.google.common.primitives.Shorts.rotate(short[],int)"""
        __Shorts.rotate(array, __int.valueOf(distance))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def indexOf(array: 'short', target: 'short') -> int:
        """public static int com.google.common.primitives.Shorts.indexOf(short[],short[])"""
        return int.__wrap(__Shorts.indexOf(array, target))

    @staticmethod
    @overload
    def sortDescending(array: 'short'):
        """public static void com.google.common.primitives.Shorts.sortDescending(short[])"""
        __Shorts.sortDescending(array)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def reverse(array: 'short', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Shorts.reverse(short[],int,int)"""
        __Shorts.reverse(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def rotate(array: 'short', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Shorts.rotate(short[],int,int,int)"""
        __Shorts.rotate(array, __int.valueOf(distance), __int.valueOf(fromIndex), __int.valueOf(toIndex)) 
 
 
# CLASS: com.google.common.primitives.Doubles
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
import com.google.common.base.Converter as __Converter
__Converter = __Converter
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.util.Collection as Collection
from typing import List
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.google.common.primitives.Doubles as __Doubles
__Doubles = __Doubles
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
import java.lang.Double as Double
from builtins import int
import java.util.List as List
 
class Doubles():
    """com.google.common.primitives.Doubles"""
 
    @staticmethod
    def __wrap(java_value: __Doubles) -> 'Doubles':
        return Doubles(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Doubles):
        """
        Dynamic initializer for Doubles.
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

    @staticmethod
    @overload
    def hashCode(value: float) -> int:
        """public static int com.google.common.primitives.Doubles.hashCode(double)"""
        return int.__wrap(__Doubles.hashCode(__double.valueOf(value)))

    @staticmethod
    @overload
    def contains(array: 'double', target: float) -> bool:
        """public static boolean com.google.common.primitives.Doubles.contains(double[],double)"""
        return bool.__wrap(__Doubles.contains(array, __double.valueOf(target)))

    @staticmethod
    @overload
    def reverse(array: 'double', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Doubles.reverse(double[],int,int)"""
        __Doubles.reverse(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def sortDescending(array: 'double', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Doubles.sortDescending(double[],int,int)"""
        __Doubles.sortDescending(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Double':
        """public static java.lang.Double com.google.common.primitives.Doubles.tryParse(java.lang.String)"""
        return __transform(__string.Doubles(string: str)).'Double'Value()

    @staticmethod
    @overload
    def constrainToRange(value: float, min: float, max: float) -> float:
        """public static double com.google.common.primitives.Doubles.constrainToRange(double,double,double)"""
        return float.__wrap(__Doubles.constrainToRange(__double.valueOf(value), __double.valueOf(min), __double.valueOf(max)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def min(*array: float) -> float:
        """public static double com.google.common.primitives.Doubles.min(double...)"""
        return float.__wrap(__Doubles.min(array))

    @staticmethod
    @overload
    def join(separator: str, *array: float) -> str:
        """public static java.lang.String com.google.common.primitives.Doubles.join(java.lang.String,double...)"""
        return str.__wrap(__Doubles.join(separator, array))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def lastIndexOf(array: 'double', target: float) -> int:
        """public static int com.google.common.primitives.Doubles.lastIndexOf(double[],double)"""
        return int.__wrap(__Doubles.lastIndexOf(array, __double.valueOf(target)))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<double[]> com.google.common.primitives.Doubles.lexicographicalComparator()"""
        return Comparator.__wrap(__Doubles.lexicographicalComparator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def reverse(array: 'double'):
        """public static void com.google.common.primitives.Doubles.reverse(double[])"""
        __Doubles.reverse(array)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def rotate(array: 'double', distance: int):
        """public static void com.google.common.primitives.Doubles.rotate(double[],int)"""
        __Doubles.rotate(array, __int.valueOf(distance))

    @staticmethod
    @overload
    def indexOf(array: 'double', target: 'double') -> int:
        """public static int com.google.common.primitives.Doubles.indexOf(double[],double[])"""
        return int.__wrap(__Doubles.indexOf(array, target))

    @staticmethod
    @overload
    def stringConverter() -> 'base.Converter':
        """public static com.google.common.base.Converter<java.lang.String, java.lang.Double> com.google.common.primitives.Doubles.stringConverter()"""
        return base.Converter.__wrap(__Doubles.stringConverter())

    @staticmethod
    @overload
    def indexOf(array: 'double', target: float) -> int:
        """public static int com.google.common.primitives.Doubles.indexOf(double[],double)"""
        return int.__wrap(__Doubles.indexOf(array, __double.valueOf(target)))

    @staticmethod
    @overload
    def sortDescending(array: 'double'):
        """public static void com.google.common.primitives.Doubles.sortDescending(double[])"""
        __Doubles.sortDescending(array)

    @staticmethod
    @overload
    def compare(a: float, b: float) -> int:
        """public static int com.google.common.primitives.Doubles.compare(double,double)"""
        return int.__wrap(__Doubles.compare(__double.valueOf(a), __double.valueOf(b)))

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
    def isFinite(value: float) -> bool:
        """public static boolean com.google.common.primitives.Doubles.isFinite(double)"""
        return bool.__wrap(__Doubles.isFinite(__double.valueOf(value)))

    @staticmethod
    @overload
    def max(*array: float) -> float:
        """public static double com.google.common.primitives.Doubles.max(double...)"""
        return float.__wrap(__Doubles.max(array))

    @staticmethod
    @overload
    def concat(*arrays: List[float]) -> List[float]:
        """public static double[] com.google.common.primitives.Doubles.concat(double[]...)"""
        return List[float].__wrap(__Doubles.concat(arrays))

    @staticmethod
    @overload
    def ensureCapacity(array: 'double', minLength: int, padding: int) -> List[float]:
        """public static double[] com.google.common.primitives.Doubles.ensureCapacity(double[],int,int)"""
        return List[float].__wrap(__Doubles.ensureCapacity(array, __int.valueOf(minLength), __int.valueOf(padding)))

    @staticmethod
    @overload
    def rotate(array: 'double', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Doubles.rotate(double[],int,int,int)"""
        __Doubles.rotate(array, __int.valueOf(distance), __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[float]:
        """public static double[] com.google.common.primitives.Doubles.toArray(java.util.Collection<? extends java.lang.Number>)"""
        return List[float].__wrap(__Doubles.toArray(collection))

    @staticmethod
    @overload
    def asList(*backingArray: float) -> 'List':
        """public static java.util.List<java.lang.Double> com.google.common.primitives.Doubles.asList(double...)"""
        return List.__wrap(__Doubles.asList(backingArray))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.primitives.UnsignedInts
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.primitives.UnsignedInts as __UnsignedInts
__UnsignedInts = __UnsignedInts
from builtins import int
 
class UnsignedInts():
    """com.google.common.primitives.UnsignedInts"""
 
    @staticmethod
    def __wrap(java_value: __UnsignedInts) -> 'UnsignedInts':
        return UnsignedInts(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnsignedInts):
        """
        Dynamic initializer for UnsignedInts.
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

    @staticmethod
    @overload
    def sortDescending(array: 'int'):
        """public static void com.google.common.primitives.UnsignedInts.sortDescending(int[])"""
        __UnsignedInts.sortDescending(array)

    @staticmethod
    @overload
    def parseUnsignedInt(s: str) -> int:
        """public static int com.google.common.primitives.UnsignedInts.parseUnsignedInt(java.lang.String)"""
        return int.__wrap(__UnsignedInts.parseUnsignedInt(s))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def sortDescending(array: 'int', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedInts.sortDescending(int[],int,int)"""
        __UnsignedInts.sortDescending(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.min(int...)"""
        return int.__wrap(__UnsignedInts.min(array))

    @staticmethod
    @overload
    def toString(x: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedInts.toString(int)"""
        return str.__wrap(__UnsignedInts.toString(__int.valueOf(x)))

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedInts.join(java.lang.String,int...)"""
        return str.__wrap(__UnsignedInts.join(separator, array))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def toLong(value: int) -> int:
        """public static long com.google.common.primitives.UnsignedInts.toLong(int)"""
        return int.__wrap(__UnsignedInts.toLong(__int.valueOf(value)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def divide(dividend: int, divisor: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.divide(int,int)"""
        return int.__wrap(__UnsignedInts.divide(__int.valueOf(dividend), __int.valueOf(divisor)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.compare(int,int)"""
        return int.__wrap(__UnsignedInts.compare(__int.valueOf(a), __int.valueOf(b)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def remainder(dividend: int, divisor: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.remainder(int,int)"""
        return int.__wrap(__UnsignedInts.remainder(__int.valueOf(dividend), __int.valueOf(divisor)))

    @staticmethod
    @overload
    def saturatedCast(value: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.saturatedCast(long)"""
        return int.__wrap(__UnsignedInts.saturatedCast(__long.valueOf(value)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def sort(array: 'int'):
        """public static void com.google.common.primitives.UnsignedInts.sort(int[])"""
        __UnsignedInts.sort(array)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def toString(x: int, radix: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedInts.toString(int,int)"""
        return str.__wrap(__UnsignedInts.toString(__int.valueOf(x), __int.valueOf(radix)))

    @staticmethod
    @overload
    def decode(stringValue: str) -> int:
        """public static int com.google.common.primitives.UnsignedInts.decode(java.lang.String)"""
        return int.__wrap(__UnsignedInts.decode(stringValue))

    @staticmethod
    @overload
    def checkedCast(value: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.checkedCast(long)"""
        return int.__wrap(__UnsignedInts.checkedCast(__long.valueOf(value)))

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.max(int...)"""
        return int.__wrap(__UnsignedInts.max(array))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<int[]> com.google.common.primitives.UnsignedInts.lexicographicalComparator()"""
        return Comparator.__wrap(__UnsignedInts.lexicographicalComparator())

    @staticmethod
    @overload
    def parseUnsignedInt(string: str, radix: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.parseUnsignedInt(java.lang.String,int)"""
        return int.__wrap(__UnsignedInts.parseUnsignedInt(string, __int.valueOf(radix)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def sort(array: 'int', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedInts.sort(int[],int,int)"""
        __UnsignedInts.sort(array, __int.valueOf(fromIndex), __int.valueOf(toIndex)) 
 
 
# CLASS: com.google.common.primitives.Chars
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
from typing import List
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.primitives.Chars as __Chars
__Chars = __Chars
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Byte as __byte
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class Chars():
    """com.google.common.primitives.Chars"""
 
    @staticmethod
    def __wrap(java_value: __Chars) -> 'Chars':
        return Chars(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Chars):
        """
        Dynamic initializer for Chars.
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

    @staticmethod
    @overload
    def min(*array: str) -> str:
        """public static char com.google.common.primitives.Chars.min(char...)"""
        return str.__wrap(__Chars.min(array))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def checkedCast(value: int) -> str:
        """public static char com.google.common.primitives.Chars.checkedCast(long)"""
        return str.__wrap(__Chars.checkedCast(__long.valueOf(value)))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<char[]> com.google.common.primitives.Chars.lexicographicalComparator()"""
        return Comparator.__wrap(__Chars.lexicographicalComparator())

    @staticmethod
    @overload
    def concat(*arrays: List[str]) -> List[str]:
        """public static char[] com.google.common.primitives.Chars.concat(char[]...)"""
        return List[str].__wrap(__Chars.concat(arrays))

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

    @staticmethod
    @overload
    def toByteArray(value: str) -> List[int]:
        """public static byte[] com.google.common.primitives.Chars.toByteArray(char)"""
        return List[int].__wrap(__Chars.toByteArray(__char.valueOf(value)))

    @staticmethod
    @overload
    def compare(a: str, b: str) -> int:
        """public static int com.google.common.primitives.Chars.compare(char,char)"""
        return int.__wrap(__Chars.compare(__char.valueOf(a), __char.valueOf(b)))

    @staticmethod
    @overload
    def asList(*backingArray: str) -> 'List':
        """public static java.util.List<java.lang.Character> com.google.common.primitives.Chars.asList(char...)"""
        return List.__wrap(__Chars.asList(backingArray))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def join(separator: str, *array: str) -> str:
        """public static java.lang.String com.google.common.primitives.Chars.join(java.lang.String,char...)"""
        return str.__wrap(__Chars.join(separator, array))

    @staticmethod
    @overload
    def constrainToRange(value: str, min: str, max: str) -> str:
        """public static char com.google.common.primitives.Chars.constrainToRange(char,char,char)"""
        return str.__wrap(__Chars.constrainToRange(__char.valueOf(value), __char.valueOf(min), __char.valueOf(max)))

    @staticmethod
    @overload
    def ensureCapacity(array: 'char', minLength: int, padding: int) -> List[str]:
        """public static char[] com.google.common.primitives.Chars.ensureCapacity(char[],int,int)"""
        return List[str].__wrap(__Chars.ensureCapacity(array, __int.valueOf(minLength), __int.valueOf(padding)))

    @staticmethod
    @overload
    def sortDescending(array: 'char'):
        """public static void com.google.common.primitives.Chars.sortDescending(char[])"""
        __Chars.sortDescending(array)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def contains(array: 'char', target: str) -> bool:
        """public static boolean com.google.common.primitives.Chars.contains(char[],char)"""
        return bool.__wrap(__Chars.contains(array, __char.valueOf(target)))

    @staticmethod
    @overload
    def reverse(array: 'char', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Chars.reverse(char[],int,int)"""
        __Chars.reverse(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def reverse(array: 'char'):
        """public static void com.google.common.primitives.Chars.reverse(char[])"""
        __Chars.reverse(array)

    @staticmethod
    @overload
    def saturatedCast(value: int) -> str:
        """public static char com.google.common.primitives.Chars.saturatedCast(long)"""
        return str.__wrap(__Chars.saturatedCast(__long.valueOf(value)))

    @staticmethod
    @overload
    def indexOf(array: 'char', target: str) -> int:
        """public static int com.google.common.primitives.Chars.indexOf(char[],char)"""
        return int.__wrap(__Chars.indexOf(array, __char.valueOf(target)))

    @staticmethod
    @overload
    def rotate(array: 'char', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Chars.rotate(char[],int,int,int)"""
        __Chars.rotate(array, __int.valueOf(distance), __int.valueOf(fromIndex), __int.valueOf(toIndex))

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
    def fromBytes(b1: int, b2: int) -> str:
        """public static char com.google.common.primitives.Chars.fromBytes(byte,byte)"""
        return str.__wrap(__Chars.fromBytes(__byte.valueOf(b1), __byte.valueOf(b2)))

    @staticmethod
    @overload
    def sortDescending(array: 'char', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Chars.sortDescending(char[],int,int)"""
        __Chars.sortDescending(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def max(*array: str) -> str:
        """public static char com.google.common.primitives.Chars.max(char...)"""
        return str.__wrap(__Chars.max(array))

    @staticmethod
    @overload
    def lastIndexOf(array: 'char', target: str) -> int:
        """public static int com.google.common.primitives.Chars.lastIndexOf(char[],char)"""
        return int.__wrap(__Chars.lastIndexOf(array, __char.valueOf(target)))

    @staticmethod
    @overload
    def rotate(array: 'char', distance: int):
        """public static void com.google.common.primitives.Chars.rotate(char[],int)"""
        __Chars.rotate(array, __int.valueOf(distance))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def indexOf(array: 'char', target: 'char') -> int:
        """public static int com.google.common.primitives.Chars.indexOf(char[],char[])"""
        return int.__wrap(__Chars.indexOf(array, target))

    @staticmethod
    @overload
    def fromByteArray(bytes: bytes) -> str:
        """public static char com.google.common.primitives.Chars.fromByteArray(byte[])"""
        return str.__wrap(__Chars.fromByteArray(bytes))

    @staticmethod
    @overload
    def hashCode(value: str) -> int:
        """public static int com.google.common.primitives.Chars.hashCode(char)"""
        return int.__wrap(__Chars.hashCode(__char.valueOf(value)))

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[str]:
        """public static char[] com.google.common.primitives.Chars.toArray(java.util.Collection<java.lang.Character>)"""
        return List[str].__wrap(__Chars.toArray(collection)) 
 
 
# CLASS: com.google.common.primitives.Longs
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
import com.google.common.base.Converter as __Converter
__Converter = __Converter
import java.lang.Long as Long
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.primitives.Longs as __Longs
__Longs = __Longs
from builtins import type
import java.util.Collection as Collection
from typing import List
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.util.List as __List
__List = __List
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Byte as __byte
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class Longs():
    """com.google.common.primitives.Longs"""
 
    @staticmethod
    def __wrap(java_value: __Longs) -> 'Longs':
        return Longs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Longs):
        """
        Dynamic initializer for Longs.
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

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Long':
        """public static java.lang.Long com.google.common.primitives.Longs.tryParse(java.lang.String,int)"""
        return __transform(__string, __int.valueOf(radix).Longs(string: str, radix: int)).'Long'Value()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def indexOf(array: 'long', target: int) -> int:
        """public static int com.google.common.primitives.Longs.indexOf(long[],long)"""
        return int.__wrap(__Longs.indexOf(array, __long.valueOf(target)))

    @staticmethod
    @overload
    def hashCode(value: int) -> int:
        """public static int com.google.common.primitives.Longs.hashCode(long)"""
        return int.__wrap(__Longs.hashCode(__long.valueOf(value)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def stringConverter() -> 'base.Converter':
        """public static com.google.common.base.Converter<java.lang.String, java.lang.Long> com.google.common.primitives.Longs.stringConverter()"""
        return base.Converter.__wrap(__Longs.stringConverter())

    @staticmethod
    @overload
    def reverse(array: 'long'):
        """public static void com.google.common.primitives.Longs.reverse(long[])"""
        __Longs.reverse(array)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static long com.google.common.primitives.Longs.min(long...)"""
        return int.__wrap(__Longs.min(array))

    @staticmethod
    @overload
    def rotate(array: 'long', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Longs.rotate(long[],int,int,int)"""
        __Longs.rotate(array, __int.valueOf(distance), __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def sortDescending(array: 'long', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Longs.sortDescending(long[],int,int)"""
        __Longs.sortDescending(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.Longs.join(java.lang.String,long...)"""
        return str.__wrap(__Longs.join(separator, array))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static long com.google.common.primitives.Longs.max(long...)"""
        return int.__wrap(__Longs.max(array))

    @staticmethod
    @overload
    def constrainToRange(value: int, min: int, max: int) -> int:
        """public static long com.google.common.primitives.Longs.constrainToRange(long,long,long)"""
        return int.__wrap(__Longs.constrainToRange(__long.valueOf(value), __long.valueOf(min), __long.valueOf(max)))

    @staticmethod
    @overload
    def sortDescending(array: 'long'):
        """public static void com.google.common.primitives.Longs.sortDescending(long[])"""
        __Longs.sortDescending(array)

    @staticmethod
    @overload
    def lastIndexOf(array: 'long', target: int) -> int:
        """public static int com.google.common.primitives.Longs.lastIndexOf(long[],long)"""
        return int.__wrap(__Longs.lastIndexOf(array, __long.valueOf(target)))

    @staticmethod
    @overload
    def fromBytes(b1: int, b2: int, b3: int, b4: int, b5: int, b6: int, b7: int, b8: int) -> int:
        """public static long com.google.common.primitives.Longs.fromBytes(byte,byte,byte,byte,byte,byte,byte,byte)"""
        return int.__wrap(__Longs.fromBytes(__byte.valueOf(b1), __byte.valueOf(b2), __byte.valueOf(b3), __byte.valueOf(b4), __byte.valueOf(b5), __byte.valueOf(b6), __byte.valueOf(b7), __byte.valueOf(b8)))

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[int]:
        """public static long[] com.google.common.primitives.Longs.toArray(java.util.Collection<? extends java.lang.Number>)"""
        return List[int].__wrap(__Longs.toArray(collection))

    @staticmethod
    @overload
    def rotate(array: 'long', distance: int):
        """public static void com.google.common.primitives.Longs.rotate(long[],int)"""
        __Longs.rotate(array, __int.valueOf(distance))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<long[]> com.google.common.primitives.Longs.lexicographicalComparator()"""
        return Comparator.__wrap(__Longs.lexicographicalComparator())

    @staticmethod
    @overload
    def fromByteArray(bytes: bytes) -> int:
        """public static long com.google.common.primitives.Longs.fromByteArray(byte[])"""
        return int.__wrap(__Longs.fromByteArray(bytes))

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.Longs.compare(long,long)"""
        return int.__wrap(__Longs.compare(__long.valueOf(a), __long.valueOf(b)))

    @staticmethod
    @overload
    def concat(*arrays: List[int]) -> List[int]:
        """public static long[] com.google.common.primitives.Longs.concat(long[]...)"""
        return List[int].__wrap(__Longs.concat(arrays))

    @staticmethod
    @overload
    def asList(*backingArray: int) -> 'List':
        """public static java.util.List<java.lang.Long> com.google.common.primitives.Longs.asList(long...)"""
        return List.__wrap(__Longs.asList(backingArray))

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
    def contains(array: 'long', target: int) -> bool:
        """public static boolean com.google.common.primitives.Longs.contains(long[],long)"""
        return bool.__wrap(__Longs.contains(array, __long.valueOf(target)))

    @staticmethod
    @overload
    def reverse(array: 'long', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Longs.reverse(long[],int,int)"""
        __Longs.reverse(array, __int.valueOf(fromIndex), __int.valueOf(toIndex))

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Long':
        """public static java.lang.Long com.google.common.primitives.Longs.tryParse(java.lang.String)"""
        return __transform(__string.Longs(string: str)).'Long'Value()

    @staticmethod
    @overload
    def indexOf(array: 'long', target: 'long') -> int:
        """public static int com.google.common.primitives.Longs.indexOf(long[],long[])"""
        return int.__wrap(__Longs.indexOf(array, target))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def ensureCapacity(array: 'long', minLength: int, padding: int) -> List[int]:
        """public static long[] com.google.common.primitives.Longs.ensureCapacity(long[],int,int)"""
        return List[int].__wrap(__Longs.ensureCapacity(array, __int.valueOf(minLength), __int.valueOf(padding)))

    @staticmethod
    @overload
    def toByteArray(value: int) -> List[int]:
        """public static byte[] com.google.common.primitives.Longs.toByteArray(long)"""
        return List[int].__wrap(__Longs.toByteArray(__long.valueOf(value)))