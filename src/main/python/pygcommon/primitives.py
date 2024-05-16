from __future__ import annotations
from overload import overload


 
from builtins import str
import com.google.common.primitives.UnsignedInts as _UnsignedInts
_UnsignedInts = _UnsignedInts
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnsignedInts():
    """com.google.common.primitives.UnsignedInts"""
 
    @staticmethod
    def _wrap(java_value: _UnsignedInts) -> 'UnsignedInts':
        return UnsignedInts(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnsignedInts):
        """
        Dynamic initializer for UnsignedInts.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnsignedInts__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnsignedInts__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def toString(x: int, radix: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedInts.toString(int,int)"""
        return str._wrap(_UnsignedInts.toString(_int.valueOf(x), _int.valueOf(radix)))

    @staticmethod
    @overload
    def sort(array: 'int', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedInts.sort(int[],int,int)"""
        _UnsignedInts.sort(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<int[]> com.google.common.primitives.UnsignedInts.lexicographicalComparator()"""
        return Comparator._wrap(_UnsignedInts.lexicographicalComparator())

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.max(int...)"""
        return int._wrap(_UnsignedInts.max(array))

    @staticmethod
    @overload
    def parseUnsignedInt(s: str) -> int:
        """public static int com.google.common.primitives.UnsignedInts.parseUnsignedInt(java.lang.String)"""
        return int._wrap(_UnsignedInts.parseUnsignedInt(s))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.min(int...)"""
        return int._wrap(_UnsignedInts.min(array))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def saturatedCast(value: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.saturatedCast(long)"""
        return int._wrap(_UnsignedInts.saturatedCast(_long.valueOf(value)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedInts.join(java.lang.String,int...)"""
        return str._wrap(_UnsignedInts.join(separator, array))

    @staticmethod
    @overload
    def sortDescending(array: 'int', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedInts.sortDescending(int[],int,int)"""
        _UnsignedInts.sortDescending(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def checkedCast(value: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.checkedCast(long)"""
        return int._wrap(_UnsignedInts.checkedCast(_long.valueOf(value)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.compare(int,int)"""
        return int._wrap(_UnsignedInts.compare(_int.valueOf(a), _int.valueOf(b)))

    @staticmethod
    @overload
    def parseUnsignedInt(string: str, radix: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.parseUnsignedInt(java.lang.String,int)"""
        return int._wrap(_UnsignedInts.parseUnsignedInt(string, _int.valueOf(radix)))

    @staticmethod
    @overload
    def toLong(value: int) -> int:
        """public static long com.google.common.primitives.UnsignedInts.toLong(int)"""
        return int._wrap(_UnsignedInts.toLong(_int.valueOf(value)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def sort(array: 'int'):
        """public static void com.google.common.primitives.UnsignedInts.sort(int[])"""
        _UnsignedInts.sort(array)

    @staticmethod
    @overload
    def divide(dividend: int, divisor: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.divide(int,int)"""
        return int._wrap(_UnsignedInts.divide(_int.valueOf(dividend), _int.valueOf(divisor)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def sortDescending(array: 'int'):
        """public static void com.google.common.primitives.UnsignedInts.sortDescending(int[])"""
        _UnsignedInts.sortDescending(array)

    @staticmethod
    @overload
    def remainder(dividend: int, divisor: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.remainder(int,int)"""
        return int._wrap(_UnsignedInts.remainder(_int.valueOf(dividend), _int.valueOf(divisor)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toString(x: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedInts.toString(int)"""
        return str._wrap(_UnsignedInts.toString(_int.valueOf(x)))

    @staticmethod
    @overload
    def decode(stringValue: str) -> int:
        """public static int com.google.common.primitives.UnsignedInts.decode(java.lang.String)"""
        return int._wrap(_UnsignedInts.decode(stringValue))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.primitives.UnsignedInts
from builtins import str
import com.google.common.primitives.UnsignedInts as _UnsignedInts
_UnsignedInts = _UnsignedInts
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnsignedInts():
    """com.google.common.primitives.UnsignedInts"""
 
    @staticmethod
    def _wrap(java_value: _UnsignedInts) -> 'UnsignedInts':
        return UnsignedInts(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnsignedInts):
        """
        Dynamic initializer for UnsignedInts.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnsignedInts__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnsignedInts__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def toString(x: int, radix: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedInts.toString(int,int)"""
        return str._wrap(_UnsignedInts.toString(_int.valueOf(x), _int.valueOf(radix)))

    @staticmethod
    @overload
    def sort(array: 'int', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedInts.sort(int[],int,int)"""
        _UnsignedInts.sort(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<int[]> com.google.common.primitives.UnsignedInts.lexicographicalComparator()"""
        return Comparator._wrap(_UnsignedInts.lexicographicalComparator())

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.max(int...)"""
        return int._wrap(_UnsignedInts.max(array))

    @staticmethod
    @overload
    def parseUnsignedInt(s: str) -> int:
        """public static int com.google.common.primitives.UnsignedInts.parseUnsignedInt(java.lang.String)"""
        return int._wrap(_UnsignedInts.parseUnsignedInt(s))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.min(int...)"""
        return int._wrap(_UnsignedInts.min(array))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def saturatedCast(value: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.saturatedCast(long)"""
        return int._wrap(_UnsignedInts.saturatedCast(_long.valueOf(value)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedInts.join(java.lang.String,int...)"""
        return str._wrap(_UnsignedInts.join(separator, array))

    @staticmethod
    @overload
    def sortDescending(array: 'int', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedInts.sortDescending(int[],int,int)"""
        _UnsignedInts.sortDescending(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def checkedCast(value: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.checkedCast(long)"""
        return int._wrap(_UnsignedInts.checkedCast(_long.valueOf(value)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.compare(int,int)"""
        return int._wrap(_UnsignedInts.compare(_int.valueOf(a), _int.valueOf(b)))

    @staticmethod
    @overload
    def parseUnsignedInt(string: str, radix: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.parseUnsignedInt(java.lang.String,int)"""
        return int._wrap(_UnsignedInts.parseUnsignedInt(string, _int.valueOf(radix)))

    @staticmethod
    @overload
    def toLong(value: int) -> int:
        """public static long com.google.common.primitives.UnsignedInts.toLong(int)"""
        return int._wrap(_UnsignedInts.toLong(_int.valueOf(value)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def sort(array: 'int'):
        """public static void com.google.common.primitives.UnsignedInts.sort(int[])"""
        _UnsignedInts.sort(array)

    @staticmethod
    @overload
    def divide(dividend: int, divisor: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.divide(int,int)"""
        return int._wrap(_UnsignedInts.divide(_int.valueOf(dividend), _int.valueOf(divisor)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def sortDescending(array: 'int'):
        """public static void com.google.common.primitives.UnsignedInts.sortDescending(int[])"""
        _UnsignedInts.sortDescending(array)

    @staticmethod
    @overload
    def remainder(dividend: int, divisor: int) -> int:
        """public static int com.google.common.primitives.UnsignedInts.remainder(int,int)"""
        return int._wrap(_UnsignedInts.remainder(_int.valueOf(dividend), _int.valueOf(divisor)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toString(x: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedInts.toString(int)"""
        return str._wrap(_UnsignedInts.toString(_int.valueOf(x)))

    @staticmethod
    @overload
    def decode(stringValue: str) -> int:
        """public static int com.google.common.primitives.UnsignedInts.decode(java.lang.String)"""
        return int._wrap(_UnsignedInts.decode(stringValue))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.primitives.UnsignedInts 
 
 
# CLASS: com.google.common.primitives.UnsignedInteger
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Number as _Number
_Number = _Number
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import com.google.common.primitives.UnsignedInteger as _UnsignedInteger
_UnsignedInteger = _UnsignedInteger
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnsignedInteger():
    """com.google.common.primitives.UnsignedInteger"""
 
    @staticmethod
    def _wrap(java_value: _UnsignedInteger) -> 'UnsignedInteger':
        return UnsignedInteger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnsignedInteger):
        """
        Dynamic initializer for UnsignedInteger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnsignedInteger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnsignedInteger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def doubleValue(self) -> float:
        """public double com.google.common.primitives.UnsignedInteger.doubleValue()"""
        return float._wrap(super(UnsignedInteger, self).doubleValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def times(self, val: 'UnsignedInteger') -> 'UnsignedInteger':
        """public com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.times(com.google.common.primitives.UnsignedInteger)"""
        return _transform(super(_UnsignedInteger, self).times(val)).'UnsignedInteger'Value()

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int._wrap(super(Number, self).byteValue())

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
    def toString(self, radix: int) -> str:
        """public java.lang.String com.google.common.primitives.UnsignedInteger.toString(int)"""
        return str._wrap(super(_UnsignedInteger, self).toString(_int.valueOf(radix)))

    @override
    @overload
    def floatValue(self) -> float:
        """public float com.google.common.primitives.UnsignedInteger.floatValue()"""
        return float._wrap(super(UnsignedInteger, self).floatValue())

    @overload
    def compareTo(self, other: 'UnsignedInteger') -> int:
        """public int com.google.common.primitives.UnsignedInteger.compareTo(com.google.common.primitives.UnsignedInteger)"""
        return int._wrap(super(_UnsignedInteger, self).compareTo(other))

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedInteger':
        """public static com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.valueOf(java.lang.String)"""
        return _transform(_string.UnsignedInteger(string: str)).'UnsignedInteger'Value()

    @overload
    def plus(self, val: 'UnsignedInteger') -> 'UnsignedInteger':
        """public com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.plus(com.google.common.primitives.UnsignedInteger)"""
        return _transform(super(_UnsignedInteger, self).plus(val)).'UnsignedInteger'Value()

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int._wrap(super(Number, self).shortValue())

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedInteger':
        """public static com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.valueOf(java.lang.String,int)"""
        return _transform(_string, _int.valueOf(radix).UnsignedInteger(string: str, radix: int)).'UnsignedInteger'Value()

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedInteger':
        """public static com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.valueOf(long)"""
        return _transform(__long.valueOf(value).UnsignedInteger(value: int)).'UnsignedInteger'Value()

    @overload
    def minus(self, val: 'UnsignedInteger') -> 'UnsignedInteger':
        """public com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.minus(com.google.common.primitives.UnsignedInteger)"""
        return _transform(super(_UnsignedInteger, self).minus(val)).'UnsignedInteger'Value()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.primitives.UnsignedInteger.toString()"""
        return str._wrap(super(UnsignedInteger, self).toString())

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedInteger':
        """public static com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.valueOf(java.math.BigInteger)"""
        return _transform(_value.UnsignedInteger(value: 'BigInteger')).'UnsignedInteger'Value()

    @overload
    def dividedBy(self, val: 'UnsignedInteger') -> 'UnsignedInteger':
        """public com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.dividedBy(com.google.common.primitives.UnsignedInteger)"""
        return _transform(super(_UnsignedInteger, self).dividedBy(val)).'UnsignedInteger'Value()

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.primitives.UnsignedInteger.equals(java.lang.Object)"""
        return bool._wrap(super(_UnsignedInteger, self).equals(obj))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def fromIntBits(fromIntBits) -> 'UnsignedInteger':
        """public static com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.fromIntBits(int)"""
        return _transform(__int.valueOf(bits).UnsignedInteger(bits: int)).'UnsignedInteger'Value()

    @override
    @overload
    def intValue(self) -> int:
        """public int com.google.common.primitives.UnsignedInteger.intValue()"""
        return int._wrap(super(UnsignedInteger, self).intValue())

    @override
    @overload
    def longValue(self) -> int:
        """public long com.google.common.primitives.UnsignedInteger.longValue()"""
        return int._wrap(super(UnsignedInteger, self).longValue())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.primitives.UnsignedInteger.hashCode()"""
        return int._wrap(super(UnsignedInteger, self).hashCode())

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
    def bigIntegerValue(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.common.primitives.UnsignedInteger.bigIntegerValue()"""
        return _transform(super(UnsignedInteger, self).bigIntegerValue()).'BigInteger'Value()

    @overload
    def mod(self, val: 'UnsignedInteger') -> 'UnsignedInteger':
        """public com.google.common.primitives.UnsignedInteger com.google.common.primitives.UnsignedInteger.mod(com.google.common.primitives.UnsignedInteger)"""
        return _transform(super(_UnsignedInteger, self).mod(val)).'UnsignedInteger'Value() 
 
 
# CLASS: com.google.common.primitives.UnsignedLong
import com.google.common.primitives.UnsignedLong as _UnsignedLong
_UnsignedLong = _UnsignedLong
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Number as _Number
_Number = _Number
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnsignedLong():
    """com.google.common.primitives.UnsignedLong"""
 
    @staticmethod
    def _wrap(java_value: _UnsignedLong) -> 'UnsignedLong':
        return UnsignedLong(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnsignedLong):
        """
        Dynamic initializer for UnsignedLong.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnsignedLong__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnsignedLong__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def dividedBy(self, val: 'UnsignedLong') -> 'UnsignedLong':
        """public com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.dividedBy(com.google.common.primitives.UnsignedLong)"""
        return _transform(super(_UnsignedLong, self).dividedBy(val)).'UnsignedLong'Value()

    @overload
    def bigIntegerValue(self) -> 'BigInteger':
        """public java.math.BigInteger com.google.common.primitives.UnsignedLong.bigIntegerValue()"""
        return _transform(super(UnsignedLong, self).bigIntegerValue()).'BigInteger'Value()

    @override
    @overload
    def doubleValue(self) -> float:
        """public double com.google.common.primitives.UnsignedLong.doubleValue()"""
        return float._wrap(super(UnsignedLong, self).doubleValue())

    @staticmethod
    @overload
    def fromLongBits(fromLongBits) -> 'UnsignedLong':
        """public static com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.fromLongBits(long)"""
        return _transform(__long.valueOf(bits).UnsignedLong(bits: int)).'UnsignedLong'Value()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int._wrap(super(Number, self).byteValue())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.primitives.UnsignedLong.hashCode()"""
        return int._wrap(super(UnsignedLong, self).hashCode())

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
    def valueOf(valueOf) -> 'UnsignedLong':
        """public static com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.valueOf(java.lang.String,int)"""
        return _transform(_string, _int.valueOf(radix).UnsignedLong(string: str, radix: int)).'UnsignedLong'Value()

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int._wrap(super(Number, self).shortValue())

    @override
    @overload
    def intValue(self) -> int:
        """public int com.google.common.primitives.UnsignedLong.intValue()"""
        return int._wrap(super(UnsignedLong, self).intValue())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def toString(self, radix: int) -> str:
        """public java.lang.String com.google.common.primitives.UnsignedLong.toString(int)"""
        return str._wrap(super(_UnsignedLong, self).toString(_int.valueOf(radix)))

    @override
    @overload
    def floatValue(self) -> float:
        """public float com.google.common.primitives.UnsignedLong.floatValue()"""
        return float._wrap(super(UnsignedLong, self).floatValue())

    @override
    @overload
    def longValue(self) -> int:
        """public long com.google.common.primitives.UnsignedLong.longValue()"""
        return int._wrap(super(UnsignedLong, self).longValue())

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedLong':
        """public static com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.valueOf(java.math.BigInteger)"""
        return _transform(_value.UnsignedLong(value: 'BigInteger')).'UnsignedLong'Value()

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedLong':
        """public static com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.valueOf(java.lang.String)"""
        return _transform(_string.UnsignedLong(string: str)).'UnsignedLong'Value()

    @overload
    def plus(self, val: 'UnsignedLong') -> 'UnsignedLong':
        """public com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.plus(com.google.common.primitives.UnsignedLong)"""
        return _transform(super(_UnsignedLong, self).plus(val)).'UnsignedLong'Value()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.primitives.UnsignedLong.toString()"""
        return str._wrap(super(UnsignedLong, self).toString())

    @overload
    def compareTo(self, o: 'UnsignedLong') -> int:
        """public int com.google.common.primitives.UnsignedLong.compareTo(com.google.common.primitives.UnsignedLong)"""
        return int._wrap(super(_UnsignedLong, self).compareTo(o))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(valueOf) -> 'UnsignedLong':
        """public static com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.valueOf(long)"""
        return _transform(__long.valueOf(value).UnsignedLong(value: int)).'UnsignedLong'Value()

    @overload
    def mod(self, val: 'UnsignedLong') -> 'UnsignedLong':
        """public com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.mod(com.google.common.primitives.UnsignedLong)"""
        return _transform(super(_UnsignedLong, self).mod(val)).'UnsignedLong'Value()

    @overload
    def minus(self, val: 'UnsignedLong') -> 'UnsignedLong':
        """public com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.minus(com.google.common.primitives.UnsignedLong)"""
        return _transform(super(_UnsignedLong, self).minus(val)).'UnsignedLong'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.primitives.UnsignedLong.equals(java.lang.Object)"""
        return bool._wrap(super(_UnsignedLong, self).equals(obj))

    @overload
    def times(self, val: 'UnsignedLong') -> 'UnsignedLong':
        """public com.google.common.primitives.UnsignedLong com.google.common.primitives.UnsignedLong.times(com.google.common.primitives.UnsignedLong)"""
        return _transform(super(_UnsignedLong, self).times(val)).'UnsignedLong'Value() 
 
 
# CLASS: com.google.common.primitives.ImmutableDoubleArray$Builder
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import com.google.common.primitives.ImmutableDoubleArray as _ImmutableDoubleArray_Builder
_Builder = _ImmutableDoubleArray_Builder.Builder
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.stream.DoubleStream as DoubleStream
from builtins import bool
import java.lang.Long as _long
import com.google.common.primitives.ImmutableDoubleArray as _ImmutableDoubleArray
_ImmutableDoubleArray = _ImmutableDoubleArray
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """com.google.common.primitives.ImmutableDoubleArray.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, stream: 'DoubleStream') -> 'Builder':
        """public com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray$Builder.addAll(java.util.stream.DoubleStream)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(stream))

    @overload
    def addAll(self, values: 'ImmutableDoubleArray') -> 'Builder':
        """public com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray$Builder.addAll(com.google.common.primitives.ImmutableDoubleArray)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(values))

    @overload
    def addAll(self, values: 'Iterable') -> 'Builder':
        """public com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray$Builder.addAll(java.lang.Iterable<java.lang.Double>)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(values))

    @overload
    def build(self) -> 'ImmutableDoubleArray':
        """public com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray$Builder.build()"""
        return 'ImmutableDoubleArray'._wrap(super(Builder, self).build())

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
    def add(self, value: float) -> 'Builder':
        """public com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray$Builder.add(double)"""
        return 'Builder'._wrap(super(_Builder, self).add(_double.valueOf(value)))

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

    @overload
    def addAll(self, values: 'double') -> 'Builder':
        """public com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray$Builder.addAll(double[])"""
        return 'Builder'._wrap(super(_Builder, self).addAll(values))

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
    def addAll(self, values: 'Collection') -> 'Builder':
        """public com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray$Builder.addAll(java.util.Collection<java.lang.Double>)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(values))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.Shorts
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
import com.google.common.primitives.Shorts as _Shorts
_Shorts = _Shorts
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Short as _short
from typing import List
import com.google.common.base.Converter as _Converter
_Converter = _Converter
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.lang.Byte as _byte
import java.util.Comparator as _Comparator
_Comparator = _Comparator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Shorts():
    """com.google.common.primitives.Shorts"""
 
    @staticmethod
    def _wrap(java_value: _Shorts) -> 'Shorts':
        return Shorts(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Shorts):
        """
        Dynamic initializer for Shorts.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Shorts__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Shorts__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<short[]> com.google.common.primitives.Shorts.lexicographicalComparator()"""
        return Comparator._wrap(_Shorts.lexicographicalComparator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def indexOf(array: 'short', target: int) -> int:
        """public static int com.google.common.primitives.Shorts.indexOf(short[],short)"""
        return int._wrap(_Shorts.indexOf(array, _short.valueOf(target)))

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.Shorts.compare(short,short)"""
        return int._wrap(_Shorts.compare(_short.valueOf(a), _short.valueOf(b)))

    @staticmethod
    @overload
    def sortDescending(array: 'short', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Shorts.sortDescending(short[],int,int)"""
        _Shorts.sortDescending(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def contains(array: 'short', target: int) -> bool:
        """public static boolean com.google.common.primitives.Shorts.contains(short[],short)"""
        return bool._wrap(_Shorts.contains(array, _short.valueOf(target)))

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
    def rotate(array: 'short', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Shorts.rotate(short[],int,int,int)"""
        _Shorts.rotate(array, _int.valueOf(distance), _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def saturatedCast(value: int) -> int:
        """public static short com.google.common.primitives.Shorts.saturatedCast(long)"""
        return int._wrap(_Shorts.saturatedCast(_long.valueOf(value)))

    @staticmethod
    @overload
    def reverse(array: 'short'):
        """public static void com.google.common.primitives.Shorts.reverse(short[])"""
        _Shorts.reverse(array)

    @staticmethod
    @overload
    def stringConverter() -> 'base.Converter':
        """public static com.google.common.base.Converter<java.lang.String, java.lang.Short> com.google.common.primitives.Shorts.stringConverter()"""
        return base.Converter._wrap(_Shorts.stringConverter())

    @staticmethod
    @overload
    def constrainToRange(value: int, min: int, max: int) -> int:
        """public static short com.google.common.primitives.Shorts.constrainToRange(short,short,short)"""
        return int._wrap(_Shorts.constrainToRange(_short.valueOf(value), _short.valueOf(min), _short.valueOf(max)))

    @staticmethod
    @overload
    def rotate(array: 'short', distance: int):
        """public static void com.google.common.primitives.Shorts.rotate(short[],int)"""
        _Shorts.rotate(array, _int.valueOf(distance))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def toByteArray(value: int) -> List[int]:
        """public static byte[] com.google.common.primitives.Shorts.toByteArray(short)"""
        return List[int]._wrap(_Shorts.toByteArray(_short.valueOf(value)))

    @staticmethod
    @overload
    def sortDescending(array: 'short'):
        """public static void com.google.common.primitives.Shorts.sortDescending(short[])"""
        _Shorts.sortDescending(array)

    @staticmethod
    @overload
    def asList(*backingArray: int) -> 'List':
        """public static java.util.List<java.lang.Short> com.google.common.primitives.Shorts.asList(short...)"""
        return List._wrap(_Shorts.asList(backingArray))

    @staticmethod
    @overload
    def reverse(array: 'short', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Shorts.reverse(short[],int,int)"""
        _Shorts.reverse(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def hashCode(value: int) -> int:
        """public static int com.google.common.primitives.Shorts.hashCode(short)"""
        return int._wrap(_Shorts.hashCode(_short.valueOf(value)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static short com.google.common.primitives.Shorts.max(short...)"""
        return int._wrap(_Shorts.max(array))

    @staticmethod
    @overload
    def indexOf(array: 'short', target: 'short') -> int:
        """public static int com.google.common.primitives.Shorts.indexOf(short[],short[])"""
        return int._wrap(_Shorts.indexOf(array, target))

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.Shorts.join(java.lang.String,short...)"""
        return str._wrap(_Shorts.join(separator, array))

    @staticmethod
    @overload
    def concat(*arrays: List[int]) -> List[int]:
        """public static short[] com.google.common.primitives.Shorts.concat(short[]...)"""
        return List[int]._wrap(_Shorts.concat(arrays))

    @staticmethod
    @overload
    def fromByteArray(bytes: bytes) -> int:
        """public static short com.google.common.primitives.Shorts.fromByteArray(byte[])"""
        return int._wrap(_Shorts.fromByteArray(bytes))

    @staticmethod
    @overload
    def ensureCapacity(array: 'short', minLength: int, padding: int) -> List[int]:
        """public static short[] com.google.common.primitives.Shorts.ensureCapacity(short[],int,int)"""
        return List[int]._wrap(_Shorts.ensureCapacity(array, _int.valueOf(minLength), _int.valueOf(padding)))

    @staticmethod
    @overload
    def fromBytes(b1: int, b2: int) -> int:
        """public static short com.google.common.primitives.Shorts.fromBytes(byte,byte)"""
        return int._wrap(_Shorts.fromBytes(_byte.valueOf(b1), _byte.valueOf(b2)))

    @staticmethod
    @overload
    def lastIndexOf(array: 'short', target: int) -> int:
        """public static int com.google.common.primitives.Shorts.lastIndexOf(short[],short)"""
        return int._wrap(_Shorts.lastIndexOf(array, _short.valueOf(target)))

    @staticmethod
    @overload
    def checkedCast(value: int) -> int:
        """public static short com.google.common.primitives.Shorts.checkedCast(long)"""
        return int._wrap(_Shorts.checkedCast(_long.valueOf(value)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static short com.google.common.primitives.Shorts.min(short...)"""
        return int._wrap(_Shorts.min(array))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[int]:
        """public static short[] com.google.common.primitives.Shorts.toArray(java.util.Collection<? extends java.lang.Number>)"""
        return List[int]._wrap(_Shorts.toArray(collection))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.ImmutableLongArray$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import com.google.common.primitives.ImmutableLongArray as _ImmutableLongArray
_ImmutableLongArray = _ImmutableLongArray
import java.lang.Integer as _int
import java.util.stream.LongStream as LongStream
import com.google.common.primitives.ImmutableLongArray as _ImmutableLongArray_Builder
_Builder = _ImmutableLongArray_Builder.Builder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """com.google.common.primitives.ImmutableLongArray.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, values: 'Collection') -> 'Builder':
        """public com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray$Builder.addAll(java.util.Collection<java.lang.Long>)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(values))

    @overload
    def addAll(self, values: 'Iterable') -> 'Builder':
        """public com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray$Builder.addAll(java.lang.Iterable<java.lang.Long>)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(values))

    @overload
    def build(self) -> 'ImmutableLongArray':
        """public com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray$Builder.build()"""
        return 'ImmutableLongArray'._wrap(super(Builder, self).build())

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
    def addAll(self, stream: 'LongStream') -> 'Builder':
        """public com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray$Builder.addAll(java.util.stream.LongStream)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(stream))

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
    def addAll(self, values: 'long') -> 'Builder':
        """public com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray$Builder.addAll(long[])"""
        return 'Builder'._wrap(super(_Builder, self).addAll(values))

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
    def add(self, value: int) -> 'Builder':
        """public com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray$Builder.add(long)"""
        return 'Builder'._wrap(super(_Builder, self).add(_long.valueOf(value)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addAll(self, values: 'ImmutableLongArray') -> 'Builder':
        """public com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray$Builder.addAll(com.google.common.primitives.ImmutableLongArray)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(values))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.ImmutableLongArray
from builtins import str
from pyquantum_helper import override
import java.util.function.LongConsumer as LongConsumer
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import com.google.common.primitives.ImmutableLongArray as _ImmutableLongArray
_ImmutableLongArray = _ImmutableLongArray
import java.util.List as _List
_List = _List
from typing import List
import java.util.stream.LongStream as _LongStream
_LongStream = _LongStream
import java.lang.Integer as _int
import java.util.stream.LongStream as LongStream
import com.google.common.primitives.ImmutableLongArray as _ImmutableLongArray_Builder
_Builder = _ImmutableLongArray_Builder.Builder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class ImmutableLongArray():
    """com.google.common.primitives.ImmutableLongArray"""
 
    @staticmethod
    def _wrap(java_value: _ImmutableLongArray) -> 'ImmutableLongArray':
        return ImmutableLongArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImmutableLongArray):
        """
        Dynamic initializer for ImmutableLongArray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImmutableLongArray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImmutableLongArray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def asList(self) -> 'List':
        """public java.util.List<java.lang.Long> com.google.common.primitives.ImmutableLongArray.asList()"""
        return 'List'._wrap(super(ImmutableLongArray, self).asList())

    @staticmethod
    @overload
    def of(e0: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long)"""
        return ImmutableLongArray._wrap(_ImmutableLongArray.of(_long.valueOf(e0)))

    @staticmethod
    @overload
    def copyOf(stream: 'LongStream') -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.copyOf(java.util.stream.LongStream)"""
        return ImmutableLongArray._wrap(_ImmutableLongArray.copyOf(stream))

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray.builder()"""
        return Builder._wrap(_ImmutableLongArray.builder())

    @staticmethod
    @overload
    def of() -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of()"""
        return ImmutableLongArray._wrap(_ImmutableLongArray.of())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def indexOf(self, target: int) -> int:
        """public int com.google.common.primitives.ImmutableLongArray.indexOf(long)"""
        return int._wrap(super(_ImmutableLongArray, self).indexOf(_long.valueOf(target)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.primitives.ImmutableLongArray.hashCode()"""
        return int._wrap(super(ImmutableLongArray, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, index: int) -> int:
        """public long com.google.common.primitives.ImmutableLongArray.get(int)"""
        return int._wrap(super(_ImmutableLongArray, self).get(_int.valueOf(index)))

    @overload
    def trimmed(self) -> 'ImmutableLongArray':
        """public com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.trimmed()"""
        return 'ImmutableLongArray'._wrap(super(ImmutableLongArray, self).trimmed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long,long,long)"""
        return ImmutableLongArray._wrap(_ImmutableLongArray.of(_long.valueOf(e0), _long.valueOf(e1), _long.valueOf(e2)))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.primitives.ImmutableLongArray.isEmpty()"""
        return bool._wrap(super(ImmutableLongArray, self).isEmpty())

    @overload
    def stream(self) -> 'LongStream':
        """public java.util.stream.LongStream com.google.common.primitives.ImmutableLongArray.stream()"""
        return 'LongStream'._wrap(super(ImmutableLongArray, self).stream())

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int, e3: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long,long,long,long)"""
        return ImmutableLongArray._wrap(_ImmutableLongArray.of(_long.valueOf(e0), _long.valueOf(e1), _long.valueOf(e2), _long.valueOf(e3)))

    @overload
    def lastIndexOf(self, target: int) -> int:
        """public int com.google.common.primitives.ImmutableLongArray.lastIndexOf(long)"""
        return int._wrap(super(_ImmutableLongArray, self).lastIndexOf(_long.valueOf(target)))

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int, e3: int, e4: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long,long,long,long,long)"""
        return ImmutableLongArray._wrap(_ImmutableLongArray.of(_long.valueOf(e0), _long.valueOf(e1), _long.valueOf(e2), _long.valueOf(e3), _long.valueOf(e4)))

    @overload
    def subArray(self, startIndex: int, endIndex: int) -> 'ImmutableLongArray':
        """public com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.subArray(int,int)"""
        return 'ImmutableLongArray'._wrap(super(_ImmutableLongArray, self).subArray(_int.valueOf(startIndex), _int.valueOf(endIndex)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.primitives.ImmutableLongArray.toString()"""
        return str._wrap(super(ImmutableLongArray, self).toString())

    @staticmethod
    @overload
    def of(e0: int, e1: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long,long)"""
        return ImmutableLongArray._wrap(_ImmutableLongArray.of(_long.valueOf(e0), _long.valueOf(e1)))

    @staticmethod
    @overload
    def copyOf(values: 'Collection') -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.copyOf(java.util.Collection<java.lang.Long>)"""
        return ImmutableLongArray._wrap(_ImmutableLongArray.copyOf(values))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def copyOf(values: 'Iterable') -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.copyOf(java.lang.Iterable<java.lang.Long>)"""
        return ImmutableLongArray._wrap(_ImmutableLongArray.copyOf(values))

    @staticmethod
    @overload
    def builder(initialCapacity: int) -> 'Builder':
        """public static com.google.common.primitives.ImmutableLongArray$Builder com.google.common.primitives.ImmutableLongArray.builder(int)"""
        return Builder._wrap(_ImmutableLongArray.builder(_int.valueOf(initialCapacity)))

    @staticmethod
    @overload
    def of(first: int, *rest: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long,long...)"""
        return ImmutableLongArray._wrap(_ImmutableLongArray.of(_long.valueOf(first), rest))

    @overload
    def toArray(self) -> List[int]:
        """public long[] com.google.common.primitives.ImmutableLongArray.toArray()"""
        return List[int]._wrap(super(ImmutableLongArray, self).toArray())

    @overload
    def length(self) -> int:
        """public int com.google.common.primitives.ImmutableLongArray.length()"""
        return int._wrap(super(ImmutableLongArray, self).length())

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.primitives.ImmutableLongArray.equals(java.lang.Object)"""
        return bool._wrap(super(_ImmutableLongArray, self).equals(object))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def forEach(self, consumer: 'LongConsumer'):
        """public void com.google.common.primitives.ImmutableLongArray.forEach(java.util.function.LongConsumer)"""
        super(_ImmutableLongArray, self).forEach(consumer)

    @overload
    def contains(self, target: int) -> bool:
        """public boolean com.google.common.primitives.ImmutableLongArray.contains(long)"""
        return bool._wrap(super(_ImmutableLongArray, self).contains(_long.valueOf(target)))

    @staticmethod
    @overload
    def copyOf(values: 'long') -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.copyOf(long[])"""
        return ImmutableLongArray._wrap(_ImmutableLongArray.copyOf(values))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int, e3: int, e4: int, e5: int) -> 'ImmutableLongArray':
        """public static com.google.common.primitives.ImmutableLongArray com.google.common.primitives.ImmutableLongArray.of(long,long,long,long,long,long)"""
        return ImmutableLongArray._wrap(_ImmutableLongArray.of(_long.valueOf(e0), _long.valueOf(e1), _long.valueOf(e2), _long.valueOf(e3), _long.valueOf(e4), _long.valueOf(e5))) 
 
 
# CLASS: com.google.common.primitives.SignedBytes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.primitives.SignedBytes as _SignedBytes
_SignedBytes = _SignedBytes
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.lang.Byte as _byte
import java.util.Comparator as _Comparator
_Comparator = _Comparator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SignedBytes():
    """com.google.common.primitives.SignedBytes"""
 
    @staticmethod
    def _wrap(java_value: _SignedBytes) -> 'SignedBytes':
        return SignedBytes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SignedBytes):
        """
        Dynamic initializer for SignedBytes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SignedBytes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SignedBytes__wrapper":
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

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static byte com.google.common.primitives.SignedBytes.min(byte...)"""
        return int._wrap(_SignedBytes.min(bytes))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<byte[]> com.google.common.primitives.SignedBytes.lexicographicalComparator()"""
        return Comparator._wrap(_SignedBytes.lexicographicalComparator())

    @staticmethod
    @overload
    def sortDescending(array: bytes):
        """public static void com.google.common.primitives.SignedBytes.sortDescending(byte[])"""
        _SignedBytes.sortDescending(bytes)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def sortDescending(array: bytes, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.SignedBytes.sortDescending(byte[],int,int)"""
        _SignedBytes.sortDescending(bytes, _int.valueOf(fromIndex), _int.valueOf(toIndex))

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

    @staticmethod
    @overload
    def checkedCast(value: int) -> int:
        """public static byte com.google.common.primitives.SignedBytes.checkedCast(long)"""
        return int._wrap(_SignedBytes.checkedCast(_long.valueOf(value)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static byte com.google.common.primitives.SignedBytes.max(byte...)"""
        return int._wrap(_SignedBytes.max(bytes))

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.SignedBytes.join(java.lang.String,byte...)"""
        return str._wrap(_SignedBytes.join(separator, bytes))

    @staticmethod
    @overload
    def saturatedCast(value: int) -> int:
        """public static byte com.google.common.primitives.SignedBytes.saturatedCast(long)"""
        return int._wrap(_SignedBytes.saturatedCast(_long.valueOf(value)))

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.SignedBytes.compare(byte,byte)"""
        return int._wrap(_SignedBytes.compare(_byte.valueOf(a), _byte.valueOf(b)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.Ints
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import com.google.common.primitives.Ints as _Ints
_Ints = _Ints
from typing import List
import com.google.common.base.Converter as _Converter
_Converter = _Converter
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.lang.Byte as _byte
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Integer as Integer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Ints():
    """com.google.common.primitives.Ints"""
 
    @staticmethod
    def _wrap(java_value: _Ints) -> 'Ints':
        return Ints(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Ints):
        """
        Dynamic initializer for Ints.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Ints__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Ints__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def reverse(array: 'int'):
        """public static void com.google.common.primitives.Ints.reverse(int[])"""
        _Ints.reverse(array)

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.Ints.compare(int,int)"""
        return int._wrap(_Ints.compare(_int.valueOf(a), _int.valueOf(b)))

    @staticmethod
    @overload
    def checkedCast(value: int) -> int:
        """public static int com.google.common.primitives.Ints.checkedCast(long)"""
        return int._wrap(_Ints.checkedCast(_long.valueOf(value)))

    @staticmethod
    @overload
    def indexOf(array: 'int', target: 'int') -> int:
        """public static int com.google.common.primitives.Ints.indexOf(int[],int[])"""
        return int._wrap(_Ints.indexOf(array, target))

    @staticmethod
    @overload
    def fromByteArray(bytes: bytes) -> int:
        """public static int com.google.common.primitives.Ints.fromByteArray(byte[])"""
        return int._wrap(_Ints.fromByteArray(bytes))

    @staticmethod
    @overload
    def asList(*backingArray: int) -> 'List':
        """public static java.util.List<java.lang.Integer> com.google.common.primitives.Ints.asList(int...)"""
        return List._wrap(_Ints.asList(backingArray))

    @staticmethod
    @overload
    def toByteArray(value: int) -> List[int]:
        """public static byte[] com.google.common.primitives.Ints.toByteArray(int)"""
        return List[int]._wrap(_Ints.toByteArray(_int.valueOf(value)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Integer':
        """public static java.lang.Integer com.google.common.primitives.Ints.tryParse(java.lang.String)"""
        return _transform(_string.Ints(string: str)).'Integer'Value()

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<int[]> com.google.common.primitives.Ints.lexicographicalComparator()"""
        return Comparator._wrap(_Ints.lexicographicalComparator())

    @staticmethod
    @overload
    def saturatedCast(value: int) -> int:
        """public static int com.google.common.primitives.Ints.saturatedCast(long)"""
        return int._wrap(_Ints.saturatedCast(_long.valueOf(value)))

    @staticmethod
    @overload
    def sortDescending(array: 'int', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Ints.sortDescending(int[],int,int)"""
        _Ints.sortDescending(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static int com.google.common.primitives.Ints.max(int...)"""
        return int._wrap(_Ints.max(array))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.Ints.join(java.lang.String,int...)"""
        return str._wrap(_Ints.join(separator, array))

    @staticmethod
    @overload
    def concat(*arrays: List[int]) -> List[int]:
        """public static int[] com.google.common.primitives.Ints.concat(int[]...)"""
        return List[int]._wrap(_Ints.concat(arrays))

    @staticmethod
    @overload
    def ensureCapacity(array: 'int', minLength: int, padding: int) -> List[int]:
        """public static int[] com.google.common.primitives.Ints.ensureCapacity(int[],int,int)"""
        return List[int]._wrap(_Ints.ensureCapacity(array, _int.valueOf(minLength), _int.valueOf(padding)))

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Integer':
        """public static java.lang.Integer com.google.common.primitives.Ints.tryParse(java.lang.String,int)"""
        return _transform(_string, _int.valueOf(radix).Ints(string: str, radix: int)).'Integer'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def constrainToRange(value: int, min: int, max: int) -> int:
        """public static int com.google.common.primitives.Ints.constrainToRange(int,int,int)"""
        return int._wrap(_Ints.constrainToRange(_int.valueOf(value), _int.valueOf(min), _int.valueOf(max)))

    @staticmethod
    @overload
    def stringConverter() -> 'base.Converter':
        """public static com.google.common.base.Converter<java.lang.String, java.lang.Integer> com.google.common.primitives.Ints.stringConverter()"""
        return base.Converter._wrap(_Ints.stringConverter())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def hashCode(value: int) -> int:
        """public static int com.google.common.primitives.Ints.hashCode(int)"""
        return int._wrap(_Ints.hashCode(_int.valueOf(value)))

    @staticmethod
    @overload
    def indexOf(array: 'int', target: int) -> int:
        """public static int com.google.common.primitives.Ints.indexOf(int[],int)"""
        return int._wrap(_Ints.indexOf(array, _int.valueOf(target)))

    @staticmethod
    @overload
    def lastIndexOf(array: 'int', target: int) -> int:
        """public static int com.google.common.primitives.Ints.lastIndexOf(int[],int)"""
        return int._wrap(_Ints.lastIndexOf(array, _int.valueOf(target)))

    @staticmethod
    @overload
    def contains(array: 'int', target: int) -> bool:
        """public static boolean com.google.common.primitives.Ints.contains(int[],int)"""
        return bool._wrap(_Ints.contains(array, _int.valueOf(target)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static int com.google.common.primitives.Ints.min(int...)"""
        return int._wrap(_Ints.min(array))

    @staticmethod
    @overload
    def reverse(array: 'int', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Ints.reverse(int[],int,int)"""
        _Ints.reverse(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def rotate(array: 'int', distance: int):
        """public static void com.google.common.primitives.Ints.rotate(int[],int)"""
        _Ints.rotate(array, _int.valueOf(distance))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[int]:
        """public static int[] com.google.common.primitives.Ints.toArray(java.util.Collection<? extends java.lang.Number>)"""
        return List[int]._wrap(_Ints.toArray(collection))

    @staticmethod
    @overload
    def sortDescending(array: 'int'):
        """public static void com.google.common.primitives.Ints.sortDescending(int[])"""
        _Ints.sortDescending(array)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def fromBytes(b1: int, b2: int, b3: int, b4: int) -> int:
        """public static int com.google.common.primitives.Ints.fromBytes(byte,byte,byte,byte)"""
        return int._wrap(_Ints.fromBytes(_byte.valueOf(b1), _byte.valueOf(b2), _byte.valueOf(b3), _byte.valueOf(b4)))

    @staticmethod
    @overload
    def rotate(array: 'int', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Ints.rotate(int[],int,int,int)"""
        _Ints.rotate(array, _int.valueOf(distance), _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.Chars
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
from typing import List
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.lang.Byte as _byte
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import com.google.common.primitives.Chars as _Chars
_Chars = _Chars
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Chars():
    """com.google.common.primitives.Chars"""
 
    @staticmethod
    def _wrap(java_value: _Chars) -> 'Chars':
        return Chars(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Chars):
        """
        Dynamic initializer for Chars.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Chars__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Chars__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def compare(a: str, b: str) -> int:
        """public static int com.google.common.primitives.Chars.compare(char,char)"""
        return int._wrap(_Chars.compare(_char.valueOf(a), _char.valueOf(b)))

    @staticmethod
    @overload
    def concat(*arrays: List[str]) -> List[str]:
        """public static char[] com.google.common.primitives.Chars.concat(char[]...)"""
        return List[str]._wrap(_Chars.concat(arrays))

    @staticmethod
    @overload
    def reverse(array: 'char', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Chars.reverse(char[],int,int)"""
        _Chars.reverse(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def fromByteArray(bytes: bytes) -> str:
        """public static char com.google.common.primitives.Chars.fromByteArray(byte[])"""
        return str._wrap(_Chars.fromByteArray(bytes))

    @staticmethod
    @overload
    def saturatedCast(value: int) -> str:
        """public static char com.google.common.primitives.Chars.saturatedCast(long)"""
        return str._wrap(_Chars.saturatedCast(_long.valueOf(value)))

    @staticmethod
    @overload
    def reverse(array: 'char'):
        """public static void com.google.common.primitives.Chars.reverse(char[])"""
        _Chars.reverse(array)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def constrainToRange(value: str, min: str, max: str) -> str:
        """public static char com.google.common.primitives.Chars.constrainToRange(char,char,char)"""
        return str._wrap(_Chars.constrainToRange(_char.valueOf(value), _char.valueOf(min), _char.valueOf(max)))

    @staticmethod
    @overload
    def rotate(array: 'char', distance: int):
        """public static void com.google.common.primitives.Chars.rotate(char[],int)"""
        _Chars.rotate(array, _int.valueOf(distance))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def asList(*backingArray: str) -> 'List':
        """public static java.util.List<java.lang.Character> com.google.common.primitives.Chars.asList(char...)"""
        return List._wrap(_Chars.asList(backingArray))

    @staticmethod
    @overload
    def ensureCapacity(array: 'char', minLength: int, padding: int) -> List[str]:
        """public static char[] com.google.common.primitives.Chars.ensureCapacity(char[],int,int)"""
        return List[str]._wrap(_Chars.ensureCapacity(array, _int.valueOf(minLength), _int.valueOf(padding)))

    @staticmethod
    @overload
    def toByteArray(value: str) -> List[int]:
        """public static byte[] com.google.common.primitives.Chars.toByteArray(char)"""
        return List[int]._wrap(_Chars.toByteArray(_char.valueOf(value)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def checkedCast(value: int) -> str:
        """public static char com.google.common.primitives.Chars.checkedCast(long)"""
        return str._wrap(_Chars.checkedCast(_long.valueOf(value)))

    @staticmethod
    @overload
    def min(*array: str) -> str:
        """public static char com.google.common.primitives.Chars.min(char...)"""
        return str._wrap(_Chars.min(array))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<char[]> com.google.common.primitives.Chars.lexicographicalComparator()"""
        return Comparator._wrap(_Chars.lexicographicalComparator())

    @staticmethod
    @overload
    def lastIndexOf(array: 'char', target: str) -> int:
        """public static int com.google.common.primitives.Chars.lastIndexOf(char[],char)"""
        return int._wrap(_Chars.lastIndexOf(array, _char.valueOf(target)))

    @staticmethod
    @overload
    def rotate(array: 'char', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Chars.rotate(char[],int,int,int)"""
        _Chars.rotate(array, _int.valueOf(distance), _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def sortDescending(array: 'char'):
        """public static void com.google.common.primitives.Chars.sortDescending(char[])"""
        _Chars.sortDescending(array)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def sortDescending(array: 'char', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Chars.sortDescending(char[],int,int)"""
        _Chars.sortDescending(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def indexOf(array: 'char', target: str) -> int:
        """public static int com.google.common.primitives.Chars.indexOf(char[],char)"""
        return int._wrap(_Chars.indexOf(array, _char.valueOf(target)))

    @staticmethod
    @overload
    def max(*array: str) -> str:
        """public static char com.google.common.primitives.Chars.max(char...)"""
        return str._wrap(_Chars.max(array))

    @staticmethod
    @overload
    def join(separator: str, *array: str) -> str:
        """public static java.lang.String com.google.common.primitives.Chars.join(java.lang.String,char...)"""
        return str._wrap(_Chars.join(separator, array))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[str]:
        """public static char[] com.google.common.primitives.Chars.toArray(java.util.Collection<java.lang.Character>)"""
        return List[str]._wrap(_Chars.toArray(collection))

    @staticmethod
    @overload
    def fromBytes(b1: int, b2: int) -> str:
        """public static char com.google.common.primitives.Chars.fromBytes(byte,byte)"""
        return str._wrap(_Chars.fromBytes(_byte.valueOf(b1), _byte.valueOf(b2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def contains(array: 'char', target: str) -> bool:
        """public static boolean com.google.common.primitives.Chars.contains(char[],char)"""
        return bool._wrap(_Chars.contains(array, _char.valueOf(target)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def hashCode(value: str) -> int:
        """public static int com.google.common.primitives.Chars.hashCode(char)"""
        return int._wrap(_Chars.hashCode(_char.valueOf(value)))

    @staticmethod
    @overload
    def indexOf(array: 'char', target: 'char') -> int:
        """public static int com.google.common.primitives.Chars.indexOf(char[],char[])"""
        return int._wrap(_Chars.indexOf(array, target))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.Doubles
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import com.google.common.primitives.Doubles as _Doubles
_Doubles = _Doubles
from typing import List
import com.google.common.base.Converter as _Converter
_Converter = _Converter
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
from builtins import bool
import java.lang.Double as Double
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Doubles():
    """com.google.common.primitives.Doubles"""
 
    @staticmethod
    def _wrap(java_value: _Doubles) -> 'Doubles':
        return Doubles(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Doubles):
        """
        Dynamic initializer for Doubles.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Doubles__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Doubles__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def reverse(array: 'double', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Doubles.reverse(double[],int,int)"""
        _Doubles.reverse(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Double':
        """public static java.lang.Double com.google.common.primitives.Doubles.tryParse(java.lang.String)"""
        return _transform(_string.Doubles(string: str)).'Double'Value()

    @staticmethod
    @overload
    def constrainToRange(value: float, min: float, max: float) -> float:
        """public static double com.google.common.primitives.Doubles.constrainToRange(double,double,double)"""
        return float._wrap(_Doubles.constrainToRange(_double.valueOf(value), _double.valueOf(min), _double.valueOf(max)))

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[float]:
        """public static double[] com.google.common.primitives.Doubles.toArray(java.util.Collection<? extends java.lang.Number>)"""
        return List[float]._wrap(_Doubles.toArray(collection))

    @staticmethod
    @overload
    def reverse(array: 'double'):
        """public static void com.google.common.primitives.Doubles.reverse(double[])"""
        _Doubles.reverse(array)

    @staticmethod
    @overload
    def lastIndexOf(array: 'double', target: float) -> int:
        """public static int com.google.common.primitives.Doubles.lastIndexOf(double[],double)"""
        return int._wrap(_Doubles.lastIndexOf(array, _double.valueOf(target)))

    @staticmethod
    @overload
    def concat(*arrays: List[float]) -> List[float]:
        """public static double[] com.google.common.primitives.Doubles.concat(double[]...)"""
        return List[float]._wrap(_Doubles.concat(arrays))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def contains(array: 'double', target: float) -> bool:
        """public static boolean com.google.common.primitives.Doubles.contains(double[],double)"""
        return bool._wrap(_Doubles.contains(array, _double.valueOf(target)))

    @staticmethod
    @overload
    def stringConverter() -> 'base.Converter':
        """public static com.google.common.base.Converter<java.lang.String, java.lang.Double> com.google.common.primitives.Doubles.stringConverter()"""
        return base.Converter._wrap(_Doubles.stringConverter())

    @staticmethod
    @overload
    def isFinite(value: float) -> bool:
        """public static boolean com.google.common.primitives.Doubles.isFinite(double)"""
        return bool._wrap(_Doubles.isFinite(_double.valueOf(value)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def sortDescending(array: 'double', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Doubles.sortDescending(double[],int,int)"""
        _Doubles.sortDescending(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def rotate(array: 'double', distance: int):
        """public static void com.google.common.primitives.Doubles.rotate(double[],int)"""
        _Doubles.rotate(array, _int.valueOf(distance))

    @staticmethod
    @overload
    def indexOf(array: 'double', target: float) -> int:
        """public static int com.google.common.primitives.Doubles.indexOf(double[],double)"""
        return int._wrap(_Doubles.indexOf(array, _double.valueOf(target)))

    @staticmethod
    @overload
    def sortDescending(array: 'double'):
        """public static void com.google.common.primitives.Doubles.sortDescending(double[])"""
        _Doubles.sortDescending(array)

    @staticmethod
    @overload
    def asList(*backingArray: float) -> 'List':
        """public static java.util.List<java.lang.Double> com.google.common.primitives.Doubles.asList(double...)"""
        return List._wrap(_Doubles.asList(backingArray))

    @staticmethod
    @overload
    def hashCode(value: float) -> int:
        """public static int com.google.common.primitives.Doubles.hashCode(double)"""
        return int._wrap(_Doubles.hashCode(_double.valueOf(value)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def compare(a: float, b: float) -> int:
        """public static int com.google.common.primitives.Doubles.compare(double,double)"""
        return int._wrap(_Doubles.compare(_double.valueOf(a), _double.valueOf(b)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def indexOf(array: 'double', target: 'double') -> int:
        """public static int com.google.common.primitives.Doubles.indexOf(double[],double[])"""
        return int._wrap(_Doubles.indexOf(array, target))

    @staticmethod
    @overload
    def max(*array: float) -> float:
        """public static double com.google.common.primitives.Doubles.max(double...)"""
        return float._wrap(_Doubles.max(array))

    @staticmethod
    @overload
    def ensureCapacity(array: 'double', minLength: int, padding: int) -> List[float]:
        """public static double[] com.google.common.primitives.Doubles.ensureCapacity(double[],int,int)"""
        return List[float]._wrap(_Doubles.ensureCapacity(array, _int.valueOf(minLength), _int.valueOf(padding)))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<double[]> com.google.common.primitives.Doubles.lexicographicalComparator()"""
        return Comparator._wrap(_Doubles.lexicographicalComparator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def rotate(array: 'double', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Doubles.rotate(double[],int,int,int)"""
        _Doubles.rotate(array, _int.valueOf(distance), _int.valueOf(fromIndex), _int.valueOf(toIndex))

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
    def min(*array: float) -> float:
        """public static double com.google.common.primitives.Doubles.min(double...)"""
        return float._wrap(_Doubles.min(array))

    @staticmethod
    @overload
    def join(separator: str, *array: float) -> str:
        """public static java.lang.String com.google.common.primitives.Doubles.join(java.lang.String,double...)"""
        return str._wrap(_Doubles.join(separator, array))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.Primitives
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
import java.util.Set as Set
import java.lang.Integer as _int
import com.google.common.primitives.Primitives as _Primitives
_Primitives = _Primitives
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class Primitives():
    """com.google.common.primitives.Primitives"""
 
    @staticmethod
    def _wrap(java_value: _Primitives) -> 'Primitives':
        return Primitives(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Primitives):
        """
        Dynamic initializer for Primitives.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Primitives__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Primitives__wrapper":
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

    @staticmethod
    @overload
    def isWrapperType(type: 'Class') -> bool:
        """public static boolean com.google.common.primitives.Primitives.isWrapperType(java.lang.Class<?>)"""
        return bool._wrap(_Primitives.isWrapperType(type))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def unwrap(type: 'Class') -> 'type.Class':
        """public static <T> java.lang.Class<T> com.google.common.primitives.Primitives.unwrap(java.lang.Class<T>)"""
        return type.Class._wrap(_Primitives.unwrap(type))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def allPrimitiveTypes() -> 'Set':
        """public static java.util.Set<java.lang.Class<?>> com.google.common.primitives.Primitives.allPrimitiveTypes()"""
        return Set._wrap(_Primitives.allPrimitiveTypes())

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

    @staticmethod
    @overload
    def wrap(type: 'Class') -> 'type.Class':
        """public static <T> java.lang.Class<T> com.google.common.primitives.Primitives.wrap(java.lang.Class<T>)"""
        return type.Class._wrap(_Primitives.wrap(type))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def allWrapperTypes() -> 'Set':
        """public static java.util.Set<java.lang.Class<?>> com.google.common.primitives.Primitives.allWrapperTypes()"""
        return Set._wrap(_Primitives.allWrapperTypes())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.UnsignedLongs
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.primitives.UnsignedLongs as _UnsignedLongs
_UnsignedLongs = _UnsignedLongs
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnsignedLongs():
    """com.google.common.primitives.UnsignedLongs"""
 
    @staticmethod
    def _wrap(java_value: _UnsignedLongs) -> 'UnsignedLongs':
        return UnsignedLongs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnsignedLongs):
        """
        Dynamic initializer for UnsignedLongs.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnsignedLongs__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnsignedLongs__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def remainder(dividend: int, divisor: int) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.remainder(long,long)"""
        return int._wrap(_UnsignedLongs.remainder(_long.valueOf(dividend), _long.valueOf(divisor)))

    @staticmethod
    @overload
    def toString(x: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedLongs.toString(long)"""
        return str._wrap(_UnsignedLongs.toString(_long.valueOf(x)))

    @staticmethod
    @overload
    def sortDescending(array: 'long'):
        """public static void com.google.common.primitives.UnsignedLongs.sortDescending(long[])"""
        _UnsignedLongs.sortDescending(array)

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.min(long...)"""
        return int._wrap(_UnsignedLongs.min(array))

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

    @staticmethod
    @overload
    def sort(array: 'long', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedLongs.sort(long[],int,int)"""
        _UnsignedLongs.sort(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def sortDescending(array: 'long', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedLongs.sortDescending(long[],int,int)"""
        _UnsignedLongs.sortDescending(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.max(long...)"""
        return int._wrap(_UnsignedLongs.max(array))

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.UnsignedLongs.compare(long,long)"""
        return int._wrap(_UnsignedLongs.compare(_long.valueOf(a), _long.valueOf(b)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def parseUnsignedLong(string: str, radix: int) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.parseUnsignedLong(java.lang.String,int)"""
        return int._wrap(_UnsignedLongs.parseUnsignedLong(string, _int.valueOf(radix)))

    @staticmethod
    @overload
    def sort(array: 'long'):
        """public static void com.google.common.primitives.UnsignedLongs.sort(long[])"""
        _UnsignedLongs.sort(array)

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<long[]> com.google.common.primitives.UnsignedLongs.lexicographicalComparator()"""
        return Comparator._wrap(_UnsignedLongs.lexicographicalComparator())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedLongs.join(java.lang.String,long...)"""
        return str._wrap(_UnsignedLongs.join(separator, array))

    @staticmethod
    @overload
    def parseUnsignedLong(string: str) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.parseUnsignedLong(java.lang.String)"""
        return int._wrap(_UnsignedLongs.parseUnsignedLong(string))

    @staticmethod
    @overload
    def divide(dividend: int, divisor: int) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.divide(long,long)"""
        return int._wrap(_UnsignedLongs.divide(_long.valueOf(dividend), _long.valueOf(divisor)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def toString(x: int, radix: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedLongs.toString(long,int)"""
        return str._wrap(_UnsignedLongs.toString(_long.valueOf(x), _int.valueOf(radix)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def decode(stringValue: str) -> int:
        """public static long com.google.common.primitives.UnsignedLongs.decode(java.lang.String)"""
        return int._wrap(_UnsignedLongs.decode(stringValue))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.Bytes
import com.google.common.primitives.Bytes as _Bytes
_Bytes = _Bytes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
from typing import List
import java.lang.Integer as _int
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Bytes():
    """com.google.common.primitives.Bytes"""
 
    @staticmethod
    def _wrap(java_value: _Bytes) -> 'Bytes':
        return Bytes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Bytes):
        """
        Dynamic initializer for Bytes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Bytes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Bytes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def rotate(array: bytes, distance: int):
        """public static void com.google.common.primitives.Bytes.rotate(byte[],int)"""
        _Bytes.rotate(bytes, _int.valueOf(distance))

    @staticmethod
    @overload
    def hashCode(value: int) -> int:
        """public static int com.google.common.primitives.Bytes.hashCode(byte)"""
        return int._wrap(_Bytes.hashCode(_byte.valueOf(value)))

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[int]:
        """public static byte[] com.google.common.primitives.Bytes.toArray(java.util.Collection<? extends java.lang.Number>)"""
        return List[int]._wrap(_Bytes.toArray(collection))

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

    @staticmethod
    @overload
    def contains(array: bytes, target: int) -> bool:
        """public static boolean com.google.common.primitives.Bytes.contains(byte[],byte)"""
        return bool._wrap(_Bytes.contains(bytes, _byte.valueOf(target)))

    @staticmethod
    @overload
    def reverse(array: bytes):
        """public static void com.google.common.primitives.Bytes.reverse(byte[])"""
        _Bytes.reverse(bytes)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def concat(*arrays: List[int]) -> List[int]:
        """public static byte[] com.google.common.primitives.Bytes.concat(byte[]...)"""
        return List[int]._wrap(_Bytes.concat(arrays))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def ensureCapacity(array: bytes, minLength: int, padding: int) -> List[int]:
        """public static byte[] com.google.common.primitives.Bytes.ensureCapacity(byte[],int,int)"""
        return List[int]._wrap(_Bytes.ensureCapacity(bytes, _int.valueOf(minLength), _int.valueOf(padding)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def rotate(array: bytes, distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Bytes.rotate(byte[],int,int,int)"""
        _Bytes.rotate(bytes, _int.valueOf(distance), _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def indexOf(array: bytes, target: int) -> int:
        """public static int com.google.common.primitives.Bytes.indexOf(byte[],byte)"""
        return int._wrap(_Bytes.indexOf(bytes, _byte.valueOf(target)))

    @staticmethod
    @overload
    def asList(*backingArray: int) -> 'List':
        """public static java.util.List<java.lang.Byte> com.google.common.primitives.Bytes.asList(byte...)"""
        return List._wrap(_Bytes.asList(bytes))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def reverse(array: bytes, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Bytes.reverse(byte[],int,int)"""
        _Bytes.reverse(bytes, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def indexOf(array: bytes, target: bytes) -> int:
        """public static int com.google.common.primitives.Bytes.indexOf(byte[],byte[])"""
        return int._wrap(_Bytes.indexOf(bytes, bytes))

    @staticmethod
    @overload
    def lastIndexOf(array: bytes, target: int) -> int:
        """public static int com.google.common.primitives.Bytes.lastIndexOf(byte[],byte)"""
        return int._wrap(_Bytes.lastIndexOf(bytes, _byte.valueOf(target)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.ImmutableIntArray$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.google.common.primitives.ImmutableIntArray as _ImmutableIntArray
_ImmutableIntArray = _ImmutableIntArray
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import com.google.common.primitives.ImmutableIntArray as _ImmutableIntArray_Builder
_Builder = _ImmutableIntArray_Builder.Builder
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.stream.IntStream as IntStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """com.google.common.primitives.ImmutableIntArray.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def addAll(self, values: 'Collection') -> 'Builder':
        """public com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray$Builder.addAll(java.util.Collection<java.lang.Integer>)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(values))

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
    def add(self, value: int) -> 'Builder':
        """public com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray$Builder.add(int)"""
        return 'Builder'._wrap(super(_Builder, self).add(_int.valueOf(value)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addAll(self, values: 'int') -> 'Builder':
        """public com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray$Builder.addAll(int[])"""
        return 'Builder'._wrap(super(_Builder, self).addAll(values))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addAll(self, stream: 'IntStream') -> 'Builder':
        """public com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray$Builder.addAll(java.util.stream.IntStream)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(stream))

    @overload
    def addAll(self, values: 'Iterable') -> 'Builder':
        """public com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray$Builder.addAll(java.lang.Iterable<java.lang.Integer>)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(values))

    @overload
    def build(self) -> 'ImmutableIntArray':
        """public com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray$Builder.build()"""
        return 'ImmutableIntArray'._wrap(super(Builder, self).build())

    @overload
    def addAll(self, values: 'ImmutableIntArray') -> 'Builder':
        """public com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray$Builder.addAll(com.google.common.primitives.ImmutableIntArray)"""
        return 'Builder'._wrap(super(_Builder, self).addAll(values))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.ImmutableIntArray
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.google.common.primitives.ImmutableIntArray as _ImmutableIntArray
_ImmutableIntArray = _ImmutableIntArray
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import com.google.common.primitives.ImmutableIntArray as _ImmutableIntArray_Builder
_Builder = _ImmutableIntArray_Builder.Builder
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
from typing import List
import java.util.stream.IntStream as _IntStream
_IntStream = _IntStream
import java.util.function.IntConsumer as IntConsumer
import java.lang.Integer as _int
import java.util.stream.IntStream as IntStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class ImmutableIntArray():
    """com.google.common.primitives.ImmutableIntArray"""
 
    @staticmethod
    def _wrap(java_value: _ImmutableIntArray) -> 'ImmutableIntArray':
        return ImmutableIntArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImmutableIntArray):
        """
        Dynamic initializer for ImmutableIntArray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImmutableIntArray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImmutableIntArray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def of(e0: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int)"""
        return ImmutableIntArray._wrap(_ImmutableIntArray.of(_int.valueOf(e0)))

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int, e3: int, e4: int, e5: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int,int,int,int,int,int)"""
        return ImmutableIntArray._wrap(_ImmutableIntArray.of(_int.valueOf(e0), _int.valueOf(e1), _int.valueOf(e2), _int.valueOf(e3), _int.valueOf(e4), _int.valueOf(e5)))

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int, e3: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int,int,int,int)"""
        return ImmutableIntArray._wrap(_ImmutableIntArray.of(_int.valueOf(e0), _int.valueOf(e1), _int.valueOf(e2), _int.valueOf(e3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def forEach(self, consumer: 'IntConsumer'):
        """public void com.google.common.primitives.ImmutableIntArray.forEach(java.util.function.IntConsumer)"""
        super(_ImmutableIntArray, self).forEach(consumer)

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int,int,int)"""
        return ImmutableIntArray._wrap(_ImmutableIntArray.of(_int.valueOf(e0), _int.valueOf(e1), _int.valueOf(e2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def trimmed(self) -> 'ImmutableIntArray':
        """public com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.trimmed()"""
        return 'ImmutableIntArray'._wrap(super(ImmutableIntArray, self).trimmed())

    @overload
    def length(self) -> int:
        """public int com.google.common.primitives.ImmutableIntArray.length()"""
        return int._wrap(super(ImmutableIntArray, self).length())

    @staticmethod
    @overload
    def copyOf(values: 'int') -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.copyOf(int[])"""
        return ImmutableIntArray._wrap(_ImmutableIntArray.copyOf(values))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def subArray(self, startIndex: int, endIndex: int) -> 'ImmutableIntArray':
        """public com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.subArray(int,int)"""
        return 'ImmutableIntArray'._wrap(super(_ImmutableIntArray, self).subArray(_int.valueOf(startIndex), _int.valueOf(endIndex)))

    @staticmethod
    @overload
    def copyOf(values: 'Iterable') -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.copyOf(java.lang.Iterable<java.lang.Integer>)"""
        return ImmutableIntArray._wrap(_ImmutableIntArray.copyOf(values))

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.primitives.ImmutableIntArray.equals(java.lang.Object)"""
        return bool._wrap(super(_ImmutableIntArray, self).equals(object))

    @overload
    def lastIndexOf(self, target: int) -> int:
        """public int com.google.common.primitives.ImmutableIntArray.lastIndexOf(int)"""
        return int._wrap(super(_ImmutableIntArray, self).lastIndexOf(_int.valueOf(target)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.primitives.ImmutableIntArray.toString()"""
        return str._wrap(super(ImmutableIntArray, self).toString())

    @overload
    def get(self, index: int) -> int:
        """public int com.google.common.primitives.ImmutableIntArray.get(int)"""
        return int._wrap(super(_ImmutableIntArray, self).get(_int.valueOf(index)))

    @staticmethod
    @overload
    def copyOf(values: 'Collection') -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.copyOf(java.util.Collection<java.lang.Integer>)"""
        return ImmutableIntArray._wrap(_ImmutableIntArray.copyOf(values))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.primitives.ImmutableIntArray.hashCode()"""
        return int._wrap(super(ImmutableIntArray, self).hashCode())

    @overload
    def stream(self) -> 'IntStream':
        """public java.util.stream.IntStream com.google.common.primitives.ImmutableIntArray.stream()"""
        return 'IntStream'._wrap(super(ImmutableIntArray, self).stream())

    @staticmethod
    @overload
    def copyOf(stream: 'IntStream') -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.copyOf(java.util.stream.IntStream)"""
        return ImmutableIntArray._wrap(_ImmutableIntArray.copyOf(stream))

    @staticmethod
    @overload
    def of(first: int, *rest: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int,int...)"""
        return ImmutableIntArray._wrap(_ImmutableIntArray.of(_int.valueOf(first), rest))

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray.builder()"""
        return Builder._wrap(_ImmutableIntArray.builder())

    @staticmethod
    @overload
    def builder(initialCapacity: int) -> 'Builder':
        """public static com.google.common.primitives.ImmutableIntArray$Builder com.google.common.primitives.ImmutableIntArray.builder(int)"""
        return Builder._wrap(_ImmutableIntArray.builder(_int.valueOf(initialCapacity)))

    @overload
    def toArray(self) -> List[int]:
        """public int[] com.google.common.primitives.ImmutableIntArray.toArray()"""
        return List[int]._wrap(super(ImmutableIntArray, self).toArray())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def of(e0: int, e1: int, e2: int, e3: int, e4: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int,int,int,int,int)"""
        return ImmutableIntArray._wrap(_ImmutableIntArray.of(_int.valueOf(e0), _int.valueOf(e1), _int.valueOf(e2), _int.valueOf(e3), _int.valueOf(e4)))

    @staticmethod
    @overload
    def of(e0: int, e1: int) -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of(int,int)"""
        return ImmutableIntArray._wrap(_ImmutableIntArray.of(_int.valueOf(e0), _int.valueOf(e1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def of() -> 'ImmutableIntArray':
        """public static com.google.common.primitives.ImmutableIntArray com.google.common.primitives.ImmutableIntArray.of()"""
        return ImmutableIntArray._wrap(_ImmutableIntArray.of())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.primitives.ImmutableIntArray.isEmpty()"""
        return bool._wrap(super(ImmutableIntArray, self).isEmpty())

    @overload
    def contains(self, target: int) -> bool:
        """public boolean com.google.common.primitives.ImmutableIntArray.contains(int)"""
        return bool._wrap(super(_ImmutableIntArray, self).contains(_int.valueOf(target)))

    @overload
    def indexOf(self, target: int) -> int:
        """public int com.google.common.primitives.ImmutableIntArray.indexOf(int)"""
        return int._wrap(super(_ImmutableIntArray, self).indexOf(_int.valueOf(target)))

    @overload
    def asList(self) -> 'List':
        """public java.util.List<java.lang.Integer> com.google.common.primitives.ImmutableIntArray.asList()"""
        return 'List'._wrap(super(ImmutableIntArray, self).asList()) 
 
 
# CLASS: com.google.common.primitives.Booleans
from builtins import str
import com.google.common.primitives.Booleans as _Booleans
_Booleans = _Booleans
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
from typing import List
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Booleans():
    """com.google.common.primitives.Booleans"""
 
    @staticmethod
    def _wrap(java_value: _Booleans) -> 'Booleans':
        return Booleans(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Booleans):
        """
        Dynamic initializer for Booleans.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Booleans__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Booleans__wrapper":
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
    def reverse(array: 'boolean', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Booleans.reverse(boolean[],int,int)"""
        _Booleans.reverse(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def reverse(array: 'boolean'):
        """public static void com.google.common.primitives.Booleans.reverse(boolean[])"""
        _Booleans.reverse(array)

    @staticmethod
    @overload
    def rotate(array: 'boolean', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Booleans.rotate(boolean[],int,int,int)"""
        _Booleans.rotate(array, _int.valueOf(distance), _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def join(separator: str, *array: bool) -> str:
        """public static java.lang.String com.google.common.primitives.Booleans.join(java.lang.String,boolean...)"""
        return str._wrap(_Booleans.join(separator, array))

    @staticmethod
    @overload
    def falseFirst() -> 'Comparator':
        """public static java.util.Comparator<java.lang.Boolean> com.google.common.primitives.Booleans.falseFirst()"""
        return Comparator._wrap(_Booleans.falseFirst())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def indexOf(array: 'boolean', target: bool) -> int:
        """public static int com.google.common.primitives.Booleans.indexOf(boolean[],boolean)"""
        return int._wrap(_Booleans.indexOf(array, _boolean.valueOf(target)))

    @staticmethod
    @overload
    def ensureCapacity(array: 'boolean', minLength: int, padding: int) -> List[bool]:
        """public static boolean[] com.google.common.primitives.Booleans.ensureCapacity(boolean[],int,int)"""
        return List[bool]._wrap(_Booleans.ensureCapacity(array, _int.valueOf(minLength), _int.valueOf(padding)))

    @staticmethod
    @overload
    def rotate(array: 'boolean', distance: int):
        """public static void com.google.common.primitives.Booleans.rotate(boolean[],int)"""
        _Booleans.rotate(array, _int.valueOf(distance))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def compare(a: bool, b: bool) -> int:
        """public static int com.google.common.primitives.Booleans.compare(boolean,boolean)"""
        return int._wrap(_Booleans.compare(_boolean.valueOf(a), _boolean.valueOf(b)))

    @staticmethod
    @overload
    def countTrue(*values: bool) -> int:
        """public static int com.google.common.primitives.Booleans.countTrue(boolean...)"""
        return int._wrap(_Booleans.countTrue(values))

    @staticmethod
    @overload
    def contains(array: 'boolean', target: bool) -> bool:
        """public static boolean com.google.common.primitives.Booleans.contains(boolean[],boolean)"""
        return bool._wrap(_Booleans.contains(array, _boolean.valueOf(target)))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<boolean[]> com.google.common.primitives.Booleans.lexicographicalComparator()"""
        return Comparator._wrap(_Booleans.lexicographicalComparator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def lastIndexOf(array: 'boolean', target: bool) -> int:
        """public static int com.google.common.primitives.Booleans.lastIndexOf(boolean[],boolean)"""
        return int._wrap(_Booleans.lastIndexOf(array, _boolean.valueOf(target)))

    @staticmethod
    @overload
    def concat(*arrays: List[bool]) -> List[bool]:
        """public static boolean[] com.google.common.primitives.Booleans.concat(boolean[]...)"""
        return List[bool]._wrap(_Booleans.concat(arrays))

    @staticmethod
    @overload
    def indexOf(array: 'boolean', target: 'boolean') -> int:
        """public static int com.google.common.primitives.Booleans.indexOf(boolean[],boolean[])"""
        return int._wrap(_Booleans.indexOf(array, target))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def hashCode(value: bool) -> int:
        """public static int com.google.common.primitives.Booleans.hashCode(boolean)"""
        return int._wrap(_Booleans.hashCode(_boolean.valueOf(value)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[bool]:
        """public static boolean[] com.google.common.primitives.Booleans.toArray(java.util.Collection<java.lang.Boolean>)"""
        return List[bool]._wrap(_Booleans.toArray(collection))

    @staticmethod
    @overload
    def asList(*backingArray: bool) -> 'List':
        """public static java.util.List<java.lang.Boolean> com.google.common.primitives.Booleans.asList(boolean...)"""
        return List._wrap(_Booleans.asList(backingArray))

    @staticmethod
    @overload
    def trueFirst() -> 'Comparator':
        """public static java.util.Comparator<java.lang.Boolean> com.google.common.primitives.Booleans.trueFirst()"""
        return Comparator._wrap(_Booleans.trueFirst())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.Floats
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.Float as Float
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
from typing import List
import com.google.common.base.Converter as _Converter
_Converter = _Converter
import com.google.common.primitives.Floats as _Floats
_Floats = _Floats
import java.lang.Float as _float
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Floats():
    """com.google.common.primitives.Floats"""
 
    @staticmethod
    def _wrap(java_value: _Floats) -> 'Floats':
        return Floats(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Floats):
        """
        Dynamic initializer for Floats.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Floats__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Floats__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def indexOf(array: 'float', target: float) -> int:
        """public static int com.google.common.primitives.Floats.indexOf(float[],float)"""
        return int._wrap(_Floats.indexOf(array, _float.valueOf(target)))

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Float':
        """public static java.lang.Float com.google.common.primitives.Floats.tryParse(java.lang.String)"""
        return _transform(_string.Floats(string: str)).'Float'Value()

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
    def sortDescending(array: 'float', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Floats.sortDescending(float[],int,int)"""
        _Floats.sortDescending(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def join(separator: str, *array: float) -> str:
        """public static java.lang.String com.google.common.primitives.Floats.join(java.lang.String,float...)"""
        return str._wrap(_Floats.join(separator, array))

    @staticmethod
    @overload
    def stringConverter() -> 'base.Converter':
        """public static com.google.common.base.Converter<java.lang.String, java.lang.Float> com.google.common.primitives.Floats.stringConverter()"""
        return base.Converter._wrap(_Floats.stringConverter())

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[float]:
        """public static float[] com.google.common.primitives.Floats.toArray(java.util.Collection<? extends java.lang.Number>)"""
        return List[float]._wrap(_Floats.toArray(collection))

    @staticmethod
    @overload
    def min(*array: float) -> float:
        """public static float com.google.common.primitives.Floats.min(float...)"""
        return float._wrap(_Floats.min(array))

    @staticmethod
    @overload
    def ensureCapacity(array: 'float', minLength: int, padding: int) -> List[float]:
        """public static float[] com.google.common.primitives.Floats.ensureCapacity(float[],int,int)"""
        return List[float]._wrap(_Floats.ensureCapacity(array, _int.valueOf(minLength), _int.valueOf(padding)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def reverse(array: 'float', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Floats.reverse(float[],int,int)"""
        _Floats.reverse(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def contains(array: 'float', target: float) -> bool:
        """public static boolean com.google.common.primitives.Floats.contains(float[],float)"""
        return bool._wrap(_Floats.contains(array, _float.valueOf(target)))

    @staticmethod
    @overload
    def lastIndexOf(array: 'float', target: float) -> int:
        """public static int com.google.common.primitives.Floats.lastIndexOf(float[],float)"""
        return int._wrap(_Floats.lastIndexOf(array, _float.valueOf(target)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def rotate(array: 'float', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Floats.rotate(float[],int,int,int)"""
        _Floats.rotate(array, _int.valueOf(distance), _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def hashCode(value: float) -> int:
        """public static int com.google.common.primitives.Floats.hashCode(float)"""
        return int._wrap(_Floats.hashCode(_float.valueOf(value)))

    @staticmethod
    @overload
    def indexOf(array: 'float', target: 'float') -> int:
        """public static int com.google.common.primitives.Floats.indexOf(float[],float[])"""
        return int._wrap(_Floats.indexOf(array, target))

    @staticmethod
    @overload
    def isFinite(value: float) -> bool:
        """public static boolean com.google.common.primitives.Floats.isFinite(float)"""
        return bool._wrap(_Floats.isFinite(_float.valueOf(value)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def rotate(array: 'float', distance: int):
        """public static void com.google.common.primitives.Floats.rotate(float[],int)"""
        _Floats.rotate(array, _int.valueOf(distance))

    @staticmethod
    @overload
    def concat(*arrays: List[float]) -> List[float]:
        """public static float[] com.google.common.primitives.Floats.concat(float[]...)"""
        return List[float]._wrap(_Floats.concat(arrays))

    @staticmethod
    @overload
    def sortDescending(array: 'float'):
        """public static void com.google.common.primitives.Floats.sortDescending(float[])"""
        _Floats.sortDescending(array)

    @staticmethod
    @overload
    def max(*array: float) -> float:
        """public static float com.google.common.primitives.Floats.max(float...)"""
        return float._wrap(_Floats.max(array))

    @staticmethod
    @overload
    def asList(*backingArray: float) -> 'List':
        """public static java.util.List<java.lang.Float> com.google.common.primitives.Floats.asList(float...)"""
        return List._wrap(_Floats.asList(backingArray))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def constrainToRange(value: float, min: float, max: float) -> float:
        """public static float com.google.common.primitives.Floats.constrainToRange(float,float,float)"""
        return float._wrap(_Floats.constrainToRange(_float.valueOf(value), _float.valueOf(min), _float.valueOf(max)))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<float[]> com.google.common.primitives.Floats.lexicographicalComparator()"""
        return Comparator._wrap(_Floats.lexicographicalComparator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def compare(a: float, b: float) -> int:
        """public static int com.google.common.primitives.Floats.compare(float,float)"""
        return int._wrap(_Floats.compare(_float.valueOf(a), _float.valueOf(b)))

    @staticmethod
    @overload
    def reverse(array: 'float'):
        """public static void com.google.common.primitives.Floats.reverse(float[])"""
        _Floats.reverse(array)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.Longs
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
import java.lang.Long as Long
from pyquantum_helper import override
import com.google.common.primitives.Longs as _Longs
_Longs = _Longs
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
from typing import List
import com.google.common.base.Converter as _Converter
_Converter = _Converter
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.lang.Byte as _byte
import java.util.Comparator as _Comparator
_Comparator = _Comparator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Longs():
    """com.google.common.primitives.Longs"""
 
    @staticmethod
    def _wrap(java_value: _Longs) -> 'Longs':
        return Longs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Longs):
        """
        Dynamic initializer for Longs.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Longs__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Longs__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def toByteArray(value: int) -> List[int]:
        """public static byte[] com.google.common.primitives.Longs.toByteArray(long)"""
        return List[int]._wrap(_Longs.toByteArray(_long.valueOf(value)))

    @staticmethod
    @overload
    def fromBytes(b1: int, b2: int, b3: int, b4: int, b5: int, b6: int, b7: int, b8: int) -> int:
        """public static long com.google.common.primitives.Longs.fromBytes(byte,byte,byte,byte,byte,byte,byte,byte)"""
        return int._wrap(_Longs.fromBytes(_byte.valueOf(b1), _byte.valueOf(b2), _byte.valueOf(b3), _byte.valueOf(b4), _byte.valueOf(b5), _byte.valueOf(b6), _byte.valueOf(b7), _byte.valueOf(b8)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def sortDescending(array: 'long', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Longs.sortDescending(long[],int,int)"""
        _Longs.sortDescending(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def reverse(array: 'long'):
        """public static void com.google.common.primitives.Longs.reverse(long[])"""
        _Longs.reverse(array)

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static long com.google.common.primitives.Longs.max(long...)"""
        return int._wrap(_Longs.max(array))

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.Longs.join(java.lang.String,long...)"""
        return str._wrap(_Longs.join(separator, array))

    @staticmethod
    @overload
    def indexOf(array: 'long', target: 'long') -> int:
        """public static int com.google.common.primitives.Longs.indexOf(long[],long[])"""
        return int._wrap(_Longs.indexOf(array, target))

    @staticmethod
    @overload
    def reverse(array: 'long', fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Longs.reverse(long[],int,int)"""
        _Longs.reverse(array, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def rotate(array: 'long', distance: int):
        """public static void com.google.common.primitives.Longs.rotate(long[],int)"""
        _Longs.rotate(array, _int.valueOf(distance))

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
    def lastIndexOf(array: 'long', target: int) -> int:
        """public static int com.google.common.primitives.Longs.lastIndexOf(long[],long)"""
        return int._wrap(_Longs.lastIndexOf(array, _long.valueOf(target)))

    @staticmethod
    @overload
    def ensureCapacity(array: 'long', minLength: int, padding: int) -> List[int]:
        """public static long[] com.google.common.primitives.Longs.ensureCapacity(long[],int,int)"""
        return List[int]._wrap(_Longs.ensureCapacity(array, _int.valueOf(minLength), _int.valueOf(padding)))

    @staticmethod
    @overload
    def indexOf(array: 'long', target: int) -> int:
        """public static int com.google.common.primitives.Longs.indexOf(long[],long)"""
        return int._wrap(_Longs.indexOf(array, _long.valueOf(target)))

    @staticmethod
    @overload
    def stringConverter() -> 'base.Converter':
        """public static com.google.common.base.Converter<java.lang.String, java.lang.Long> com.google.common.primitives.Longs.stringConverter()"""
        return base.Converter._wrap(_Longs.stringConverter())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Long':
        """public static java.lang.Long com.google.common.primitives.Longs.tryParse(java.lang.String)"""
        return _transform(_string.Longs(string: str)).'Long'Value()

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static long com.google.common.primitives.Longs.min(long...)"""
        return int._wrap(_Longs.min(array))

    @staticmethod
    @overload
    def tryParse(tryParse) -> 'Long':
        """public static java.lang.Long com.google.common.primitives.Longs.tryParse(java.lang.String,int)"""
        return _transform(_string, _int.valueOf(radix).Longs(string: str, radix: int)).'Long'Value()

    @staticmethod
    @overload
    def concat(*arrays: List[int]) -> List[int]:
        """public static long[] com.google.common.primitives.Longs.concat(long[]...)"""
        return List[int]._wrap(_Longs.concat(arrays))

    @staticmethod
    @overload
    def fromByteArray(bytes: bytes) -> int:
        """public static long com.google.common.primitives.Longs.fromByteArray(byte[])"""
        return int._wrap(_Longs.fromByteArray(bytes))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def constrainToRange(value: int, min: int, max: int) -> int:
        """public static long com.google.common.primitives.Longs.constrainToRange(long,long,long)"""
        return int._wrap(_Longs.constrainToRange(_long.valueOf(value), _long.valueOf(min), _long.valueOf(max)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def toArray(collection: 'Collection') -> List[int]:
        """public static long[] com.google.common.primitives.Longs.toArray(java.util.Collection<? extends java.lang.Number>)"""
        return List[int]._wrap(_Longs.toArray(collection))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<long[]> com.google.common.primitives.Longs.lexicographicalComparator()"""
        return Comparator._wrap(_Longs.lexicographicalComparator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def rotate(array: 'long', distance: int, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.Longs.rotate(long[],int,int,int)"""
        _Longs.rotate(array, _int.valueOf(distance), _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def asList(*backingArray: int) -> 'List':
        """public static java.util.List<java.lang.Long> com.google.common.primitives.Longs.asList(long...)"""
        return List._wrap(_Longs.asList(backingArray))

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.Longs.compare(long,long)"""
        return int._wrap(_Longs.compare(_long.valueOf(a), _long.valueOf(b)))

    @staticmethod
    @overload
    def sortDescending(array: 'long'):
        """public static void com.google.common.primitives.Longs.sortDescending(long[])"""
        _Longs.sortDescending(array)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def hashCode(value: int) -> int:
        """public static int com.google.common.primitives.Longs.hashCode(long)"""
        return int._wrap(_Longs.hashCode(_long.valueOf(value)))

    @staticmethod
    @overload
    def contains(array: 'long', target: int) -> bool:
        """public static boolean com.google.common.primitives.Longs.contains(long[],long)"""
        return bool._wrap(_Longs.contains(array, _long.valueOf(target)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.primitives.ImmutableDoubleArray
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import com.google.common.primitives.ImmutableDoubleArray as _ImmutableDoubleArray_Builder
_Builder = _ImmutableDoubleArray_Builder.Builder
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import java.util.function.DoubleConsumer as DoubleConsumer
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.stream.DoubleStream as _DoubleStream
_DoubleStream = _DoubleStream
import java.util.List as _List
_List = _List
from typing import List
import java.lang.Integer as _int
import java.util.stream.DoubleStream as DoubleStream
from builtins import bool
import java.lang.Long as _long
import com.google.common.primitives.ImmutableDoubleArray as _ImmutableDoubleArray
_ImmutableDoubleArray = _ImmutableDoubleArray
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class ImmutableDoubleArray():
    """com.google.common.primitives.ImmutableDoubleArray"""
 
    @staticmethod
    def _wrap(java_value: _ImmutableDoubleArray) -> 'ImmutableDoubleArray':
        return ImmutableDoubleArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImmutableDoubleArray):
        """
        Dynamic initializer for ImmutableDoubleArray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImmutableDoubleArray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImmutableDoubleArray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def stream(self) -> 'DoubleStream':
        """public java.util.stream.DoubleStream com.google.common.primitives.ImmutableDoubleArray.stream()"""
        return 'DoubleStream'._wrap(super(ImmutableDoubleArray, self).stream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.primitives.ImmutableDoubleArray.toString()"""
        return str._wrap(super(ImmutableDoubleArray, self).toString())

    @overload
    def indexOf(self, target: float) -> int:
        """public int com.google.common.primitives.ImmutableDoubleArray.indexOf(double)"""
        return int._wrap(super(_ImmutableDoubleArray, self).indexOf(_double.valueOf(target)))

    @staticmethod
    @overload
    def of(first: float, *rest: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double,double...)"""
        return ImmutableDoubleArray._wrap(_ImmutableDoubleArray.of(_double.valueOf(first), rest))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.primitives.ImmutableDoubleArray.hashCode()"""
        return int._wrap(super(ImmutableDoubleArray, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def of(e0: float, e1: float, e2: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double,double,double)"""
        return ImmutableDoubleArray._wrap(_ImmutableDoubleArray.of(_double.valueOf(e0), _double.valueOf(e1), _double.valueOf(e2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def copyOf(stream: 'DoubleStream') -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.copyOf(java.util.stream.DoubleStream)"""
        return ImmutableDoubleArray._wrap(_ImmutableDoubleArray.copyOf(stream))

    @overload
    def lastIndexOf(self, target: float) -> int:
        """public int com.google.common.primitives.ImmutableDoubleArray.lastIndexOf(double)"""
        return int._wrap(super(_ImmutableDoubleArray, self).lastIndexOf(_double.valueOf(target)))

    @staticmethod
    @overload
    def of(e0: float, e1: float, e2: float, e3: float, e4: float, e5: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double,double,double,double,double,double)"""
        return ImmutableDoubleArray._wrap(_ImmutableDoubleArray.of(_double.valueOf(e0), _double.valueOf(e1), _double.valueOf(e2), _double.valueOf(e3), _double.valueOf(e4), _double.valueOf(e5)))

    @staticmethod
    @overload
    def of() -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of()"""
        return ImmutableDoubleArray._wrap(_ImmutableDoubleArray.of())

    @staticmethod
    @overload
    def builder(initialCapacity: int) -> 'Builder':
        """public static com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray.builder(int)"""
        return Builder._wrap(_ImmutableDoubleArray.builder(_int.valueOf(initialCapacity)))

    @staticmethod
    @overload
    def of(e0: float, e1: float, e2: float, e3: float, e4: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double,double,double,double,double)"""
        return ImmutableDoubleArray._wrap(_ImmutableDoubleArray.of(_double.valueOf(e0), _double.valueOf(e1), _double.valueOf(e2), _double.valueOf(e3), _double.valueOf(e4)))

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static com.google.common.primitives.ImmutableDoubleArray$Builder com.google.common.primitives.ImmutableDoubleArray.builder()"""
        return Builder._wrap(_ImmutableDoubleArray.builder())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def length(self) -> int:
        """public int com.google.common.primitives.ImmutableDoubleArray.length()"""
        return int._wrap(super(ImmutableDoubleArray, self).length())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.primitives.ImmutableDoubleArray.isEmpty()"""
        return bool._wrap(super(ImmutableDoubleArray, self).isEmpty())

    @staticmethod
    @overload
    def of(e0: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double)"""
        return ImmutableDoubleArray._wrap(_ImmutableDoubleArray.of(_double.valueOf(e0)))

    @overload
    def trimmed(self) -> 'ImmutableDoubleArray':
        """public com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.trimmed()"""
        return 'ImmutableDoubleArray'._wrap(super(ImmutableDoubleArray, self).trimmed())

    @staticmethod
    @overload
    def copyOf(values: 'double') -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.copyOf(double[])"""
        return ImmutableDoubleArray._wrap(_ImmutableDoubleArray.copyOf(values))

    @overload
    def asList(self) -> 'List':
        """public java.util.List<java.lang.Double> com.google.common.primitives.ImmutableDoubleArray.asList()"""
        return 'List'._wrap(super(ImmutableDoubleArray, self).asList())

    @overload
    def get(self, index: int) -> float:
        """public double com.google.common.primitives.ImmutableDoubleArray.get(int)"""
        return float._wrap(super(_ImmutableDoubleArray, self).get(_int.valueOf(index)))

    @overload
    def contains(self, target: float) -> bool:
        """public boolean com.google.common.primitives.ImmutableDoubleArray.contains(double)"""
        return bool._wrap(super(_ImmutableDoubleArray, self).contains(_double.valueOf(target)))

    @staticmethod
    @overload
    def copyOf(values: 'Iterable') -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.copyOf(java.lang.Iterable<java.lang.Double>)"""
        return ImmutableDoubleArray._wrap(_ImmutableDoubleArray.copyOf(values))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def of(e0: float, e1: float, e2: float, e3: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double,double,double,double)"""
        return ImmutableDoubleArray._wrap(_ImmutableDoubleArray.of(_double.valueOf(e0), _double.valueOf(e1), _double.valueOf(e2), _double.valueOf(e3)))

    @overload
    def forEach(self, consumer: 'DoubleConsumer'):
        """public void com.google.common.primitives.ImmutableDoubleArray.forEach(java.util.function.DoubleConsumer)"""
        super(_ImmutableDoubleArray, self).forEach(consumer)

    @overload
    def toArray(self) -> List[float]:
        """public double[] com.google.common.primitives.ImmutableDoubleArray.toArray()"""
        return List[float]._wrap(super(ImmutableDoubleArray, self).toArray())

    @overload
    def subArray(self, startIndex: int, endIndex: int) -> 'ImmutableDoubleArray':
        """public com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.subArray(int,int)"""
        return 'ImmutableDoubleArray'._wrap(super(_ImmutableDoubleArray, self).subArray(_int.valueOf(startIndex), _int.valueOf(endIndex)))

    @staticmethod
    @overload
    def of(e0: float, e1: float) -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.of(double,double)"""
        return ImmutableDoubleArray._wrap(_ImmutableDoubleArray.of(_double.valueOf(e0), _double.valueOf(e1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.primitives.ImmutableDoubleArray.equals(java.lang.Object)"""
        return bool._wrap(super(_ImmutableDoubleArray, self).equals(object))

    @staticmethod
    @overload
    def copyOf(values: 'Collection') -> 'ImmutableDoubleArray':
        """public static com.google.common.primitives.ImmutableDoubleArray com.google.common.primitives.ImmutableDoubleArray.copyOf(java.util.Collection<java.lang.Double>)"""
        return ImmutableDoubleArray._wrap(_ImmutableDoubleArray.copyOf(values)) 
 
 
# CLASS: com.google.common.primitives.UnsignedBytes
from builtins import str
import com.google.common.primitives.UnsignedBytes as _UnsignedBytes
_UnsignedBytes = _UnsignedBytes
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.lang.Byte as _byte
import java.util.Comparator as _Comparator
_Comparator = _Comparator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnsignedBytes():
    """com.google.common.primitives.UnsignedBytes"""
 
    @staticmethod
    def _wrap(java_value: _UnsignedBytes) -> 'UnsignedBytes':
        return UnsignedBytes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnsignedBytes):
        """
        Dynamic initializer for UnsignedBytes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnsignedBytes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnsignedBytes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def parseUnsignedByte(string: str, radix: int) -> int:
        """public static byte com.google.common.primitives.UnsignedBytes.parseUnsignedByte(java.lang.String,int)"""
        return int._wrap(_UnsignedBytes.parseUnsignedByte(string, _int.valueOf(radix)))

    @staticmethod
    @overload
    def parseUnsignedByte(string: str) -> int:
        """public static byte com.google.common.primitives.UnsignedBytes.parseUnsignedByte(java.lang.String)"""
        return int._wrap(_UnsignedBytes.parseUnsignedByte(string))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def toString(x: int, radix: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedBytes.toString(byte,int)"""
        return str._wrap(_UnsignedBytes.toString(_byte.valueOf(x), _int.valueOf(radix)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def max(*array: int) -> int:
        """public static byte com.google.common.primitives.UnsignedBytes.max(byte...)"""
        return int._wrap(_UnsignedBytes.max(bytes))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def toString(x: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedBytes.toString(byte)"""
        return str._wrap(_UnsignedBytes.toString(_byte.valueOf(x)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def join(separator: str, *array: int) -> str:
        """public static java.lang.String com.google.common.primitives.UnsignedBytes.join(java.lang.String,byte...)"""
        return str._wrap(_UnsignedBytes.join(separator, bytes))

    @staticmethod
    @overload
    def sortDescending(array: bytes):
        """public static void com.google.common.primitives.UnsignedBytes.sortDescending(byte[])"""
        _UnsignedBytes.sortDescending(bytes)

    @staticmethod
    @overload
    def sortDescending(array: bytes, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedBytes.sortDescending(byte[],int,int)"""
        _UnsignedBytes.sortDescending(bytes, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @staticmethod
    @overload
    def saturatedCast(value: int) -> int:
        """public static byte com.google.common.primitives.UnsignedBytes.saturatedCast(long)"""
        return int._wrap(_UnsignedBytes.saturatedCast(_long.valueOf(value)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def sort(array: bytes, fromIndex: int, toIndex: int):
        """public static void com.google.common.primitives.UnsignedBytes.sort(byte[],int,int)"""
        _UnsignedBytes.sort(bytes, _int.valueOf(fromIndex), _int.valueOf(toIndex))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def checkedCast(value: int) -> int:
        """public static byte com.google.common.primitives.UnsignedBytes.checkedCast(long)"""
        return int._wrap(_UnsignedBytes.checkedCast(_long.valueOf(value)))

    @staticmethod
    @overload
    def sort(array: bytes):
        """public static void com.google.common.primitives.UnsignedBytes.sort(byte[])"""
        _UnsignedBytes.sort(bytes)

    @staticmethod
    @overload
    def min(*array: int) -> int:
        """public static byte com.google.common.primitives.UnsignedBytes.min(byte...)"""
        return int._wrap(_UnsignedBytes.min(bytes))

    @staticmethod
    @overload
    def lexicographicalComparator() -> 'Comparator':
        """public static java.util.Comparator<byte[]> com.google.common.primitives.UnsignedBytes.lexicographicalComparator()"""
        return Comparator._wrap(_UnsignedBytes.lexicographicalComparator())

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
    def toInt(value: int) -> int:
        """public static int com.google.common.primitives.UnsignedBytes.toInt(byte)"""
        return int._wrap(_UnsignedBytes.toInt(_byte.valueOf(value)))

    @staticmethod
    @overload
    def compare(a: int, b: int) -> int:
        """public static int com.google.common.primitives.UnsignedBytes.compare(byte,byte)"""
        return int._wrap(_UnsignedBytes.compare(_byte.valueOf(a), _byte.valueOf(b)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())