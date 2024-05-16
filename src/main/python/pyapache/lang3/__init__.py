from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.Range as __Range
__Range = __Range
import java.lang.Comparable as Comparable
from builtins import object
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
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
 
class Range():
    """org.apache.commons.lang3.Range"""
 
    @staticmethod
    def __wrap(java_value: __Range) -> 'Range':
        return Range(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Range):
        """
        Dynamic initializer for Range.
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
    def getMinimum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMinimum()"""
        return object.__wrap(super(Range, self).getMinimum())

    @overload
    def getComparator(self) -> 'Comparator':
        """public java.util.Comparator<T> org.apache.commons.lang3.Range.getComparator()"""
        return 'Comparator'.__wrap(super(Range, self).getComparator())

    @staticmethod
    @overload
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T)"""
        return Range.__wrap(__Range.between(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isAfter(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfter(T)"""
        return bool.__wrap(super(__Range, self).isAfter(arg0))

    @overload
    def getMaximum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMaximum()"""
        return object.__wrap(super(Range, self).getMaximum())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.contains(T)"""
        return bool.__wrap(super(__Range, self).contains(arg0))

    @staticmethod
    @overload
    def is(arg0: object, arg1: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.is(arg0, arg1))

    @overload
    def isNaturalOrdering(self) -> bool:
        """public boolean org.apache.commons.lang3.Range.isNaturalOrdering()"""
        return bool.__wrap(super(Range, self).isNaturalOrdering())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.equals(java.lang.Object)"""
        return bool.__wrap(super(__Range, self).equals(arg0))

    @overload
    def isStartedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isStartedBy(T)"""
        return bool.__wrap(super(__Range, self).isStartedBy(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.Range.hashCode()"""
        return int.__wrap(super(Range, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString()"""
        return str.__wrap(super(Range, self).toString())

    @overload
    def isBefore(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isBefore(T)"""
        return bool.__wrap(super(__Range, self).isBefore(arg0))

    @overload
    def intersectionWith(self, arg0: 'Range') -> 'Range':
        """public org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.intersectionWith(org.apache.commons.lang3.Range<T>)"""
        return 'Range'.__wrap(super(__Range, self).intersectionWith(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T)"""
        return Range.__wrap(__Range.of(arg0, arg1))

    @overload
    def isAfterRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfterRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isAfterRange(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isEndedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isEndedBy(T)"""
        return bool.__wrap(super(__Range, self).isEndedBy(arg0))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString(java.lang.String)"""
        return str.__wrap(super(__Range, self).toString(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def isOverlappedBy(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isOverlappedBy(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isOverlappedBy(arg0))

    @overload
    def fit(self, arg0: object) -> object:
        """public T org.apache.commons.lang3.Range.fit(T)"""
        return object.__wrap(super(__Range, self).fit(arg0))

    @overload
    def elementCompareTo(self, arg0: object) -> int:
        """public int org.apache.commons.lang3.Range.elementCompareTo(T)"""
        return int.__wrap(super(__Range, self).elementCompareTo(arg0))

    @overload
    def isBeforeRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isBeforeRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isBeforeRange(arg0))

    @staticmethod
    @overload
    def is(arg0: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T)"""
        return Range.__wrap(__Range.is(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def between(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.between(arg0, arg1, arg2))

    @overload
    def containsRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.containsRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).containsRange(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.Range
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.Range as __Range
__Range = __Range
import java.lang.Comparable as Comparable
from builtins import object
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
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
 
class Range():
    """org.apache.commons.lang3.Range"""
 
    @staticmethod
    def __wrap(java_value: __Range) -> 'Range':
        return Range(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Range):
        """
        Dynamic initializer for Range.
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
    def getMinimum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMinimum()"""
        return object.__wrap(super(Range, self).getMinimum())

    @overload
    def getComparator(self) -> 'Comparator':
        """public java.util.Comparator<T> org.apache.commons.lang3.Range.getComparator()"""
        return 'Comparator'.__wrap(super(Range, self).getComparator())

    @staticmethod
    @overload
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T)"""
        return Range.__wrap(__Range.between(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isAfter(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfter(T)"""
        return bool.__wrap(super(__Range, self).isAfter(arg0))

    @overload
    def getMaximum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMaximum()"""
        return object.__wrap(super(Range, self).getMaximum())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.contains(T)"""
        return bool.__wrap(super(__Range, self).contains(arg0))

    @staticmethod
    @overload
    def is(arg0: object, arg1: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.is(arg0, arg1))

    @overload
    def isNaturalOrdering(self) -> bool:
        """public boolean org.apache.commons.lang3.Range.isNaturalOrdering()"""
        return bool.__wrap(super(Range, self).isNaturalOrdering())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.equals(java.lang.Object)"""
        return bool.__wrap(super(__Range, self).equals(arg0))

    @overload
    def isStartedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isStartedBy(T)"""
        return bool.__wrap(super(__Range, self).isStartedBy(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.Range.hashCode()"""
        return int.__wrap(super(Range, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString()"""
        return str.__wrap(super(Range, self).toString())

    @overload
    def isBefore(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isBefore(T)"""
        return bool.__wrap(super(__Range, self).isBefore(arg0))

    @overload
    def intersectionWith(self, arg0: 'Range') -> 'Range':
        """public org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.intersectionWith(org.apache.commons.lang3.Range<T>)"""
        return 'Range'.__wrap(super(__Range, self).intersectionWith(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T)"""
        return Range.__wrap(__Range.of(arg0, arg1))

    @overload
    def isAfterRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfterRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isAfterRange(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isEndedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isEndedBy(T)"""
        return bool.__wrap(super(__Range, self).isEndedBy(arg0))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString(java.lang.String)"""
        return str.__wrap(super(__Range, self).toString(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def isOverlappedBy(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isOverlappedBy(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isOverlappedBy(arg0))

    @overload
    def fit(self, arg0: object) -> object:
        """public T org.apache.commons.lang3.Range.fit(T)"""
        return object.__wrap(super(__Range, self).fit(arg0))

    @overload
    def elementCompareTo(self, arg0: object) -> int:
        """public int org.apache.commons.lang3.Range.elementCompareTo(T)"""
        return int.__wrap(super(__Range, self).elementCompareTo(arg0))

    @overload
    def isBeforeRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isBeforeRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isBeforeRange(arg0))

    @staticmethod
    @overload
    def is(arg0: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T)"""
        return Range.__wrap(__Range.is(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def between(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.between(arg0, arg1, arg2))

    @overload
    def containsRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.containsRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).containsRange(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.Range 
 
 
# CLASS: org.apache.commons.lang3.ThreadUtils$ThreadPredicate
import java.lang.Thread as Thread
import org.apache.commons.lang3.ThreadUtils as __ThreadUtils_ThreadPredicate
__ThreadPredicate = __ThreadUtils_ThreadPredicate.ThreadPredicate
from abc import abstractmethod, ABC
 
class ThreadPredicate(ABC):
    """org.apache.commons.lang3.ThreadUtils.ThreadPredicate"""
 
    @staticmethod
    def __wrap(java_value: __ThreadPredicate) -> 'ThreadPredicate':
        return ThreadPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadPredicate):
        """
        Dynamic initializer for ThreadPredicate.
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
    def test(self, arg0: 'Thread'):
        """public abstract boolean org.apache.commons.lang3.ThreadUtils$ThreadPredicate.test(java.lang.Thread)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.BitField
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.lang3.BitField as __BitField
__BitField = __BitField
from builtins import bool
from builtins import int
 
class BitField():
    """org.apache.commons.lang3.BitField"""
 
    @staticmethod
    def __wrap(java_value: __BitField) -> 'BitField':
        return BitField(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BitField):
        """
        Dynamic initializer for BitField.
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
    def setByteBoolean(self, arg0: int, arg1: bool) -> int:
        """public byte org.apache.commons.lang3.BitField.setByteBoolean(byte,boolean)"""
        return int.__wrap(super(__BitField, self).setByteBoolean(__byte.valueOf(arg0), __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def set(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.BitField.set(int)"""
        return int.__wrap(super(__BitField, self).set(__int.valueOf(arg0)))

    @overload
    def setValue(self, arg0: int, arg1: int) -> int:
        """public int org.apache.commons.lang3.BitField.setValue(int,int)"""
        return int.__wrap(super(__BitField, self).setValue(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getShortRawValue(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.BitField.getShortRawValue(short)"""
        return int.__wrap(super(__BitField, self).getShortRawValue(__short.valueOf(arg0)))

    @overload
    def getValue(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.BitField.getValue(int)"""
        return int.__wrap(super(__BitField, self).getValue(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def clear(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.BitField.clear(int)"""
        return int.__wrap(super(__BitField, self).clear(__int.valueOf(arg0)))

    @overload
    def setShort(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.BitField.setShort(short)"""
        return int.__wrap(super(__BitField, self).setShort(__short.valueOf(arg0)))

    @overload
    def getShortValue(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.BitField.getShortValue(short)"""
        return int.__wrap(super(__BitField, self).getShortValue(__short.valueOf(arg0)))

    @overload
    def setShortValue(self, arg0: int, arg1: int) -> int:
        """public short org.apache.commons.lang3.BitField.setShortValue(short,short)"""
        return int.__wrap(super(__BitField, self).setShortValue(__short.valueOf(arg0), __short.valueOf(arg1)))

    @overload
    def clearByte(self, arg0: int) -> int:
        """public byte org.apache.commons.lang3.BitField.clearByte(byte)"""
        return int.__wrap(super(__BitField, self).clearByte(__byte.valueOf(arg0)))

    @overload
    def clearShort(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.BitField.clearShort(short)"""
        return int.__wrap(super(__BitField, self).clearShort(__short.valueOf(arg0)))

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
    def setBoolean(self, arg0: int, arg1: bool) -> int:
        """public int org.apache.commons.lang3.BitField.setBoolean(int,boolean)"""
        return int.__wrap(super(__BitField, self).setBoolean(__int.valueOf(arg0), __boolean.valueOf(arg1)))

    @overload
    def isAllSet(self, arg0: int) -> bool:
        """public boolean org.apache.commons.lang3.BitField.isAllSet(int)"""
        return bool.__wrap(super(__BitField, self).isAllSet(__int.valueOf(arg0)))

    @overload
    def isSet(self, arg0: int) -> bool:
        """public boolean org.apache.commons.lang3.BitField.isSet(int)"""
        return bool.__wrap(super(__BitField, self).isSet(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setShortBoolean(self, arg0: int, arg1: bool) -> int:
        """public short org.apache.commons.lang3.BitField.setShortBoolean(short,boolean)"""
        return int.__wrap(super(__BitField, self).setShortBoolean(__short.valueOf(arg0), __boolean.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setByte(self, arg0: int) -> int:
        """public byte org.apache.commons.lang3.BitField.setByte(byte)"""
        return int.__wrap(super(__BitField, self).setByte(__byte.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.BitField(int)"""
        val = __BitField(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getRawValue(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.BitField.getRawValue(int)"""
        return int.__wrap(super(__BitField, self).getRawValue(__int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailablePredicate
import org.apache.commons.lang3.Functions as __Functions_FailablePredicate
__FailablePredicate = __Functions_FailablePredicate.FailablePredicate
from abc import abstractmethod, ABC
 
class FailablePredicate(ABC):
    """org.apache.commons.lang3.Functions.FailablePredicate"""
 
    @staticmethod
    def __wrap(java_value: __FailablePredicate) -> 'FailablePredicate':
        return FailablePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailablePredicate):
        """
        Dynamic initializer for FailablePredicate.
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
    def test(self, arg0: object):
        """public abstract boolean org.apache.commons.lang3.Functions$FailablePredicate.test(I) throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.ClassUtils
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.ClassLoader as ClassLoader
from builtins import bool
import org.apache.commons.lang3.ClassUtils as __ClassUtils
__ClassUtils = __ClassUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Iterable as Iterable
from builtins import object
from typing import List
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.reflect.Method as __Method
__Method = __Method
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.List as List
import java.lang.reflect.Method as Method
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
 
class ClassUtils():
    """org.apache.commons.lang3.ClassUtils"""
 
    @staticmethod
    def __wrap(java_value: __ClassUtils) -> 'ClassUtils':
        return ClassUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClassUtils):
        """
        Dynamic initializer for ClassUtils.
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
    def isInnerClass(arg0: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isInnerClass(java.lang.Class<?>)"""
        return bool.__wrap(__ClassUtils.isInnerClass(arg0))

    @staticmethod
    @overload
    def getShortClassName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getShortClassName(java.lang.Object,java.lang.String)"""
        return str.__wrap(__ClassUtils.getShortClassName(arg0, arg1))

    @staticmethod
    @overload
    def getName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getName(java.lang.Class<?>)"""
        return str.__wrap(__ClassUtils.getName(arg0))

    @staticmethod
    @overload
    def getAbbreviatedName(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getAbbreviatedName(java.lang.String,int)"""
        return str.__wrap(__ClassUtils.getAbbreviatedName(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def hierarchy(arg0: 'Class', arg1: 'Interfaces') -> 'Iterable':
        """public static java.lang.Iterable<java.lang.Class<?>> org.apache.commons.lang3.ClassUtils.hierarchy(java.lang.Class<?>,org.apache.commons.lang3.ClassUtils$Interfaces)"""
        return Iterable.__wrap(__ClassUtils.hierarchy(arg0, arg1))

    @staticmethod
    @overload
    def isPrimitiveOrWrapper(arg0: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isPrimitiveOrWrapper(java.lang.Class<?>)"""
        return bool.__wrap(__ClassUtils.isPrimitiveOrWrapper(arg0))

    @staticmethod
    @overload
    def getPackageName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getPackageName(java.lang.Object,java.lang.String)"""
        return str.__wrap(__ClassUtils.getPackageName(arg0, arg1))

    @staticmethod
    @overload
    def primitiveToWrapper(arg0: 'Class') -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.ClassUtils.primitiveToWrapper(java.lang.Class<?>)"""
        return type.Class.__wrap(__ClassUtils.primitiveToWrapper(arg0))

    @staticmethod
    @overload
    def convertClassesToClassNames(arg0: 'List') -> 'List':
        """public static java.util.List<java.lang.String> org.apache.commons.lang3.ClassUtils.convertClassesToClassNames(java.util.List<java.lang.Class<?>>)"""
        return List.__wrap(__ClassUtils.convertClassesToClassNames(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getSimpleName(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getSimpleName(java.lang.Object)"""
        return str.__wrap(__ClassUtils.getSimpleName(arg0))

    @staticmethod
    @overload
    def isPublic(arg0: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isPublic(java.lang.Class<?>)"""
        return bool.__wrap(__ClassUtils.isPublic(arg0))

    @staticmethod
    @overload
    def isPrimitiveWrapper(arg0: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isPrimitiveWrapper(java.lang.Class<?>)"""
        return bool.__wrap(__ClassUtils.isPrimitiveWrapper(arg0))

    @staticmethod
    @overload
    def getAllSuperclasses(arg0: 'Class') -> 'List':
        """public static java.util.List<java.lang.Class<?>> org.apache.commons.lang3.ClassUtils.getAllSuperclasses(java.lang.Class<?>)"""
        return List.__wrap(__ClassUtils.getAllSuperclasses(arg0))

    @staticmethod
    @overload
    def getClass(arg0: str) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.ClassUtils.getClass(java.lang.String) throws java.lang.ClassNotFoundException"""
        return type.Class.__wrap(__ClassUtils.getClass(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def isAssignable(arg0: 'Class', arg1: 'Class', arg2: bool) -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isAssignable(java.lang.Class<?>[],java.lang.Class<?>[],boolean)"""
        return bool.__wrap(__ClassUtils.isAssignable(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def toClass(*arg0: object) -> List['type.Class']:
        """public static java.lang.Class<?>[] org.apache.commons.lang3.ClassUtils.toClass(java.lang.Object...)"""
        return List[type.Class].__wrap(__ClassUtils.toClass(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getName(arg0: 'Class', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getName(java.lang.Class<?>,java.lang.String)"""
        return str.__wrap(__ClassUtils.getName(arg0, arg1))

    @staticmethod
    @overload
    def getShortCanonicalName(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getShortCanonicalName(java.lang.String)"""
        return str.__wrap(__ClassUtils.getShortCanonicalName(arg0))

    @staticmethod
    @overload
    def getPublicMethod(arg0: 'Class', arg1: str, *arg2: 'type.Class') -> 'Method':
        """public static java.lang.reflect.Method org.apache.commons.lang3.ClassUtils.getPublicMethod(java.lang.Class<?>,java.lang.String,java.lang.Class<?>...) throws java.lang.NoSuchMethodException"""
        return Method.__wrap(__ClassUtils.getPublicMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getClass(arg0: str, arg1: bool) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.ClassUtils.getClass(java.lang.String,boolean) throws java.lang.ClassNotFoundException"""
        return type.Class.__wrap(__ClassUtils.getClass(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def wrapperToPrimitive(arg0: 'Class') -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.ClassUtils.wrapperToPrimitive(java.lang.Class<?>)"""
        return type.Class.__wrap(__ClassUtils.wrapperToPrimitive(arg0))

    @staticmethod
    @overload
    def getPackageCanonicalName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getPackageCanonicalName(java.lang.Object,java.lang.String)"""
        return str.__wrap(__ClassUtils.getPackageCanonicalName(arg0, arg1))

    @staticmethod
    @overload
    def convertClassNamesToClasses(arg0: 'List') -> 'List':
        """public static java.util.List<java.lang.Class<?>> org.apache.commons.lang3.ClassUtils.convertClassNamesToClasses(java.util.List<java.lang.String>)"""
        return List.__wrap(__ClassUtils.convertClassNamesToClasses(arg0))

    @staticmethod
    @overload
    def isAssignable(arg0: 'Class', arg1: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isAssignable(java.lang.Class<?>,java.lang.Class<?>)"""
        return bool.__wrap(__ClassUtils.isAssignable(arg0, arg1))

    @staticmethod
    @overload
    def comparator() -> 'Comparator':
        """public static java.util.Comparator<java.lang.Class<?>> org.apache.commons.lang3.ClassUtils.comparator()"""
        return Comparator.__wrap(__ClassUtils.comparator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ClassUtils()"""
        val = __ClassUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getPackageCanonicalName(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getPackageCanonicalName(java.lang.String)"""
        return str.__wrap(__ClassUtils.getPackageCanonicalName(arg0))

    @staticmethod
    @overload
    def getComponentType(arg0: 'Class') -> 'type.Class':
        """public static <T> java.lang.Class<T> org.apache.commons.lang3.ClassUtils.getComponentType(java.lang.Class<T[]>)"""
        return type.Class.__wrap(__ClassUtils.getComponentType(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def primitivesToWrappers(*arg0: 'type.Class') -> List['type.Class']:
        """public static java.lang.Class<?>[] org.apache.commons.lang3.ClassUtils.primitivesToWrappers(java.lang.Class<?>...)"""
        return List[type.Class].__wrap(__ClassUtils.primitivesToWrappers(arg0))

    @staticmethod
    @overload
    def getCanonicalName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getCanonicalName(java.lang.Class<?>)"""
        return str.__wrap(__ClassUtils.getCanonicalName(arg0))

    @staticmethod
    @overload
    def getAbbreviatedName(arg0: 'Class', arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getAbbreviatedName(java.lang.Class<?>,int)"""
        return str.__wrap(__ClassUtils.getAbbreviatedName(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def isAssignable(arg0: 'Class', arg1: 'Class', arg2: bool) -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isAssignable(java.lang.Class<?>,java.lang.Class<?>,boolean)"""
        return bool.__wrap(__ClassUtils.isAssignable(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def getCanonicalName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getCanonicalName(java.lang.Object,java.lang.String)"""
        return str.__wrap(__ClassUtils.getCanonicalName(arg0, arg1))

    @staticmethod
    @overload
    def getShortClassName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getShortClassName(java.lang.Class<?>)"""
        return str.__wrap(__ClassUtils.getShortClassName(arg0))

    @staticmethod
    @overload
    def getShortCanonicalName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getShortCanonicalName(java.lang.Object,java.lang.String)"""
        return str.__wrap(__ClassUtils.getShortCanonicalName(arg0, arg1))

    @staticmethod
    @overload
    def wrappersToPrimitives(*arg0: 'type.Class') -> List['type.Class']:
        """public static java.lang.Class<?>[] org.apache.commons.lang3.ClassUtils.wrappersToPrimitives(java.lang.Class<?>...)"""
        return List[type.Class].__wrap(__ClassUtils.wrappersToPrimitives(arg0))

    @staticmethod
    @overload
    def isAssignable(arg0: 'Class', *arg1: 'type.Class') -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isAssignable(java.lang.Class<?>[],java.lang.Class<?>...)"""
        return bool.__wrap(__ClassUtils.isAssignable(arg0, arg1))

    @staticmethod
    @overload
    def getPackageName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getPackageName(java.lang.Class<?>)"""
        return str.__wrap(__ClassUtils.getPackageName(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getAllInterfaces(arg0: 'Class') -> 'List':
        """public static java.util.List<java.lang.Class<?>> org.apache.commons.lang3.ClassUtils.getAllInterfaces(java.lang.Class<?>)"""
        return List.__wrap(__ClassUtils.getAllInterfaces(arg0))

    @staticmethod
    @overload
    def getShortCanonicalName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getShortCanonicalName(java.lang.Class<?>)"""
        return str.__wrap(__ClassUtils.getShortCanonicalName(arg0))

    @staticmethod
    @overload
    def getCanonicalName(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getCanonicalName(java.lang.Object)"""
        return str.__wrap(__ClassUtils.getCanonicalName(arg0))

    @staticmethod
    @overload
    def getPackageCanonicalName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getPackageCanonicalName(java.lang.Class<?>)"""
        return str.__wrap(__ClassUtils.getPackageCanonicalName(arg0))

    @staticmethod
    @overload
    def getName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getName(java.lang.Object,java.lang.String)"""
        return str.__wrap(__ClassUtils.getName(arg0, arg1))

    @staticmethod
    @overload
    def getSimpleName(arg0: 'Class', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getSimpleName(java.lang.Class<?>,java.lang.String)"""
        return str.__wrap(__ClassUtils.getSimpleName(arg0, arg1))

    @staticmethod
    @overload
    def getSimpleName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getSimpleName(java.lang.Class<?>)"""
        return str.__wrap(__ClassUtils.getSimpleName(arg0))

    @staticmethod
    @overload
    def getClass(arg0: 'ClassLoader', arg1: str, arg2: bool) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.ClassUtils.getClass(java.lang.ClassLoader,java.lang.String,boolean) throws java.lang.ClassNotFoundException"""
        return type.Class.__wrap(__ClassUtils.getClass(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def getCanonicalName(arg0: 'Class', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getCanonicalName(java.lang.Class<?>,java.lang.String)"""
        return str.__wrap(__ClassUtils.getCanonicalName(arg0, arg1))

    @staticmethod
    @overload
    def getPackageName(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getPackageName(java.lang.String)"""
        return str.__wrap(__ClassUtils.getPackageName(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getClass(arg0: 'ClassLoader', arg1: str) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.ClassUtils.getClass(java.lang.ClassLoader,java.lang.String) throws java.lang.ClassNotFoundException"""
        return type.Class.__wrap(__ClassUtils.getClass(arg0, arg1))

    @staticmethod
    @overload
    def hierarchy(arg0: 'Class') -> 'Iterable':
        """public static java.lang.Iterable<java.lang.Class<?>> org.apache.commons.lang3.ClassUtils.hierarchy(java.lang.Class<?>)"""
        return Iterable.__wrap(__ClassUtils.hierarchy(arg0))

    @staticmethod
    @overload
    def getSimpleName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getSimpleName(java.lang.Object,java.lang.String)"""
        return str.__wrap(__ClassUtils.getSimpleName(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ClassUtils()"""
        val = __ClassUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getName(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getName(java.lang.Object)"""
        return str.__wrap(__ClassUtils.getName(arg0))

    @staticmethod
    @overload
    def getShortClassName(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getShortClassName(java.lang.String)"""
        return str.__wrap(__ClassUtils.getShortClassName(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.ThreadUtils$ThreadIdPredicate
import java.lang.Thread as Thread
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.ThreadUtils as __ThreadUtils_ThreadIdPredicate
__ThreadIdPredicate = __ThreadUtils_ThreadIdPredicate.ThreadIdPredicate
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
 
class ThreadIdPredicate():
    """org.apache.commons.lang3.ThreadUtils.ThreadIdPredicate"""
 
    @staticmethod
    def __wrap(java_value: __ThreadIdPredicate) -> 'ThreadIdPredicate':
        return ThreadIdPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadIdPredicate):
        """
        Dynamic initializer for ThreadIdPredicate.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.ThreadUtils$ThreadIdPredicate(long)"""
        val = __ThreadIdPredicate(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
    def test(self, arg0: 'Thread') -> bool:
        """public boolean org.apache.commons.lang3.ThreadUtils$ThreadIdPredicate.test(java.lang.Thread)"""
        return bool.__wrap(super(__ThreadIdPredicate, self).test(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.ObjectUtils$Null
from builtins import str
import org.apache.commons.lang3.ObjectUtils as __ObjectUtils_Null
__Null = __ObjectUtils_Null.Null
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Null():
    """org.apache.commons.lang3.ObjectUtils.Null"""
 
    @staticmethod
    def __wrap(java_value: __Null) -> 'Null':
        return Null(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Null):
        """
        Dynamic initializer for Null.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.SystemUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import org.apache.commons.lang3.SystemUtils as __SystemUtils
__SystemUtils = __SystemUtils
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.File as __File
__File = __File
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SystemUtils():
    """org.apache.commons.lang3.SystemUtils"""
 
    @staticmethod
    def __wrap(java_value: __SystemUtils) -> 'SystemUtils':
        return SystemUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SystemUtils):
        """
        Dynamic initializer for SystemUtils.
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
    def __init__(self):
        """public org.apache.commons.lang3.SystemUtils()"""
        val = __SystemUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getHostName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemUtils.getHostName()"""
        return str.__wrap(__SystemUtils.getHostName())

    @staticmethod
    @overload
    def getUserDir() -> 'File':
        """public static java.io.File org.apache.commons.lang3.SystemUtils.getUserDir()"""
        return File.__wrap(__SystemUtils.getUserDir())

    @staticmethod
    @overload
    def getJavaIoTmpDir() -> 'File':
        """public static java.io.File org.apache.commons.lang3.SystemUtils.getJavaIoTmpDir()"""
        return File.__wrap(__SystemUtils.getJavaIoTmpDir())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getEnvironmentVariable(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemUtils.getEnvironmentVariable(java.lang.String,java.lang.String)"""
        return str.__wrap(__SystemUtils.getEnvironmentVariable(arg0, arg1))

    @staticmethod
    @overload
    def getUserName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemUtils.getUserName()"""
        return str.__wrap(__SystemUtils.getUserName())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.SystemUtils()"""
        val = __SystemUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getUserHome() -> 'File':
        """public static java.io.File org.apache.commons.lang3.SystemUtils.getUserHome()"""
        return File.__wrap(__SystemUtils.getUserHome())

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
    def getUserName(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemUtils.getUserName(java.lang.String)"""
        return str.__wrap(__SystemUtils.getUserName(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isJavaVersionAtLeast(arg0: 'JavaVersion') -> bool:
        """public static boolean org.apache.commons.lang3.SystemUtils.isJavaVersionAtLeast(org.apache.commons.lang3.JavaVersion)"""
        return bool.__wrap(__SystemUtils.isJavaVersionAtLeast(arg0))

    @staticmethod
    @overload
    def isJavaAwtHeadless() -> bool:
        """public static boolean org.apache.commons.lang3.SystemUtils.isJavaAwtHeadless()"""
        return bool.__wrap(__SystemUtils.isJavaAwtHeadless())

    @staticmethod
    @overload
    def isJavaVersionAtMost(arg0: 'JavaVersion') -> bool:
        """public static boolean org.apache.commons.lang3.SystemUtils.isJavaVersionAtMost(org.apache.commons.lang3.JavaVersion)"""
        return bool.__wrap(__SystemUtils.isJavaVersionAtMost(arg0))

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

    @staticmethod
    @overload
    def getJavaHome() -> 'File':
        """public static java.io.File org.apache.commons.lang3.SystemUtils.getJavaHome()"""
        return File.__wrap(__SystemUtils.getJavaHome())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.RandomStringUtils
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.RandomStringUtils as __RandomStringUtils
__RandomStringUtils = __RandomStringUtils
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
import java.util.Random as Random
from builtins import int
 
class RandomStringUtils():
    """org.apache.commons.lang3.RandomStringUtils"""
 
    @staticmethod
    def __wrap(java_value: __RandomStringUtils) -> 'RandomStringUtils':
        return RandomStringUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RandomStringUtils):
        """
        Dynamic initializer for RandomStringUtils.
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
    def random(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int,int,int,boolean,boolean)"""
        return str.__wrap(__RandomStringUtils.random(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def randomAlphanumeric(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(int)"""
        return str.__wrap(__RandomStringUtils.randomAlphanumeric(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def randomPrint(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomPrint(int)"""
        return str.__wrap(__RandomStringUtils.randomPrint(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def randomAscii(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomAscii(int)"""
        return str.__wrap(__RandomStringUtils.randomAscii(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def randomAlphanumeric(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(int,int)"""
        return str.__wrap(__RandomStringUtils.randomAlphanumeric(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def randomAscii(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomAscii(int,int)"""
        return str.__wrap(__RandomStringUtils.randomAscii(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def randomGraph(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomGraph(int)"""
        return str.__wrap(__RandomStringUtils.randomGraph(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def random(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: bool, *arg5: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int,int,int,boolean,boolean,char...)"""
        return str.__wrap(__RandomStringUtils.random(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def randomAlphabetic(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomAlphabetic(int)"""
        return str.__wrap(__RandomStringUtils.randomAlphabetic(__int.valueOf(arg0)))

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
    def randomNumeric(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomNumeric(int)"""
        return str.__wrap(__RandomStringUtils.randomNumeric(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def random(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int)"""
        return str.__wrap(__RandomStringUtils.random(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def random(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: bool, arg5: 'char', arg6: 'Random') -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int,int,int,boolean,boolean,char[],java.util.Random)"""
        return str.__wrap(__RandomStringUtils.random(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4), arg5, arg6))

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
    def randomAlphabetic(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomAlphabetic(int,int)"""
        return str.__wrap(__RandomStringUtils.randomAlphabetic(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def randomPrint(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomPrint(int,int)"""
        return str.__wrap(__RandomStringUtils.randomPrint(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def randomGraph(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomGraph(int,int)"""
        return str.__wrap(__RandomStringUtils.randomGraph(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.RandomStringUtils()"""
        val = __RandomStringUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def random(arg0: int, arg1: bool, arg2: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int,boolean,boolean)"""
        return str.__wrap(__RandomStringUtils.random(__int.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def random(arg0: int, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int,char...)"""
        return str.__wrap(__RandomStringUtils.random(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def randomNumeric(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomNumeric(int,int)"""
        return str.__wrap(__RandomStringUtils.randomNumeric(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def random(arg0: int, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int,java.lang.String)"""
        return str.__wrap(__RandomStringUtils.random(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.RandomStringUtils()"""
        val = __RandomStringUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.DoubleRange
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.DoubleRange as __DoubleRange
__DoubleRange = __DoubleRange
import org.apache.commons.lang3.Range as __Range
__Range = __Range
import java.lang.Comparable as Comparable
from builtins import object
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
import java.lang.Double as Double
from builtins import int
 
class DoubleRange():
    """org.apache.commons.lang3.DoubleRange"""
 
    @staticmethod
    def __wrap(java_value: __DoubleRange) -> 'DoubleRange':
        return DoubleRange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DoubleRange):
        """
        Dynamic initializer for DoubleRange.
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
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T)"""
        return Range.__wrap(__Range.between(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isAfter(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfter(T)"""
        return bool.__wrap(super(__Range, self).isAfter(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.contains(T)"""
        return bool.__wrap(super(__Range, self).contains(arg0))

    @override
    @overload
    def isNaturalOrdering(self) -> bool:
        """public boolean org.apache.commons.lang3.Range.isNaturalOrdering()"""
        return bool.__wrap(super(Range, self).isNaturalOrdering())

    @staticmethod
    @overload
    def is(arg0: object, arg1: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.is(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.equals(java.lang.Object)"""
        return bool.__wrap(super(__Range, self).equals(arg0))

    @overload
    def isStartedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isStartedBy(T)"""
        return bool.__wrap(super(__Range, self).isStartedBy(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.Range.hashCode()"""
        return int.__wrap(super(Range, self).hashCode())

    @staticmethod
    @overload
    def of(arg0: 'Double', arg1: 'Double') -> 'DoubleRange':
        """public static org.apache.commons.lang3.DoubleRange org.apache.commons.lang3.DoubleRange.of(java.lang.Double,java.lang.Double)"""
        return DoubleRange.__wrap(__DoubleRange.of(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString()"""
        return str.__wrap(super(Range, self).toString())

    @overload
    def isBefore(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isBefore(T)"""
        return bool.__wrap(super(__Range, self).isBefore(arg0))

    @overload
    def intersectionWith(self, arg0: 'Range') -> 'Range':
        """public org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.intersectionWith(org.apache.commons.lang3.Range<T>)"""
        return 'Range'.__wrap(super(__Range, self).intersectionWith(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T)"""
        return Range.__wrap(__Range.of(arg0, arg1))

    @overload
    def isAfterRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfterRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isAfterRange(arg0))

    @override
    @overload
    def getMinimum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMinimum()"""
        return object.__wrap(super(Range, self).getMinimum())

    @override
    @overload
    def getComparator(self) -> 'Comparator':
        """public java.util.Comparator<T> org.apache.commons.lang3.Range.getComparator()"""
        return 'Comparator'.__wrap(super(Range, self).getComparator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isEndedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isEndedBy(T)"""
        return bool.__wrap(super(__Range, self).isEndedBy(arg0))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString(java.lang.String)"""
        return str.__wrap(super(__Range, self).toString(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getMaximum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMaximum()"""
        return object.__wrap(super(Range, self).getMaximum())

    @overload
    def isOverlappedBy(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isOverlappedBy(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isOverlappedBy(arg0))

    @overload
    def fit(self, arg0: object) -> object:
        """public T org.apache.commons.lang3.Range.fit(T)"""
        return object.__wrap(super(__Range, self).fit(arg0))

    @overload
    def elementCompareTo(self, arg0: object) -> int:
        """public int org.apache.commons.lang3.Range.elementCompareTo(T)"""
        return int.__wrap(super(__Range, self).elementCompareTo(arg0))

    @overload
    def isBeforeRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isBeforeRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isBeforeRange(arg0))

    @staticmethod
    @overload
    def is(arg0: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T)"""
        return Range.__wrap(__Range.is(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def between(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.between(arg0, arg1, arg2))

    @overload
    def containsRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.containsRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).containsRange(arg0))

    @staticmethod
    @overload
    def of(arg0: float, arg1: float) -> 'DoubleRange':
        """public static org.apache.commons.lang3.DoubleRange org.apache.commons.lang3.DoubleRange.of(double,double)"""
        return DoubleRange.__wrap(__DoubleRange.of(__double.valueOf(arg0), __double.valueOf(arg1))) 
 
 
# CLASS: org.apache.commons.lang3.BooleanUtils
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Boolean as __Boolean
__Boolean = __Boolean
import org.apache.commons.lang3.BooleanUtils as __BooleanUtils
__BooleanUtils = __BooleanUtils
import java.util.function.Consumer as Consumer
from typing import List
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class BooleanUtils():
    """org.apache.commons.lang3.BooleanUtils"""
 
    @staticmethod
    def __wrap(java_value: __BooleanUtils) -> 'BooleanUtils':
        return BooleanUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BooleanUtils):
        """
        Dynamic initializer for BooleanUtils.
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
    def toStringOnOff(arg0: 'Boolean') -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toStringOnOff(java.lang.Boolean)"""
        return str.__wrap(__BooleanUtils.toStringOnOff(arg0))

    @staticmethod
    @overload
    def isFalse(arg0: 'Boolean') -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.isFalse(java.lang.Boolean)"""
        return bool.__wrap(__BooleanUtils.isFalse(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def toBoolean(arg0: int, arg1: int, arg2: int) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBoolean(int,int,int)"""
        return bool.__wrap(__BooleanUtils.toBoolean(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def compare(arg0: bool, arg1: bool) -> int:
        """public static int org.apache.commons.lang3.BooleanUtils.compare(boolean,boolean)"""
        return int.__wrap(__BooleanUtils.compare(__boolean.valueOf(arg0), __boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def xor(*arg0: bool) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.xor(boolean...)"""
        return bool.__wrap(__BooleanUtils.xor(arg0))

    @staticmethod
    @overload
    def toStringTrueFalse(arg0: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toStringTrueFalse(boolean)"""
        return str.__wrap(__BooleanUtils.toStringTrueFalse(__boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def toBooleanDefaultIfNull(arg0: 'Boolean', arg1: bool) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBooleanDefaultIfNull(java.lang.Boolean,boolean)"""
        return bool.__wrap(__BooleanUtils.toBooleanDefaultIfNull(arg0, __boolean.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.BooleanUtils()"""
        val = __BooleanUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def oneHot(*arg0: 'Boolean') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.oneHot(java.lang.Boolean...)"""
        return Boolean.__wrap(__BooleanUtils.oneHot(arg0))

    @staticmethod
    @overload
    def toInteger(arg0: 'Boolean', arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.apache.commons.lang3.BooleanUtils.toInteger(java.lang.Boolean,int,int,int)"""
        return int.__wrap(__BooleanUtils.toInteger(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def toIntegerObject(toIntegerObject) -> 'Integer':
        """public static java.lang.Integer org.apache.commons.lang3.BooleanUtils.toIntegerObject(boolean)"""
        return __transform(____boolean.valueOf(arg0).BooleanUtils(arg0: bool)).'Integer'Value()

    @staticmethod
    @overload
    def toIntegerObject(toIntegerObject) -> 'Integer':
        """public static java.lang.Integer org.apache.commons.lang3.BooleanUtils.toIntegerObject(java.lang.Boolean)"""
        return __transform(__arg0.BooleanUtils(arg0: 'Boolean')).'Integer'Value()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def booleanValues() -> List['Boolean']:
        """public static java.lang.Boolean[] org.apache.commons.lang3.BooleanUtils.booleanValues()"""
        return List[Boolean].__wrap(__BooleanUtils.booleanValues())

    @staticmethod
    @overload
    def toBoolean(arg0: str, arg1: str, arg2: str) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBoolean(java.lang.String,java.lang.String,java.lang.String)"""
        return bool.__wrap(__BooleanUtils.toBoolean(arg0, arg1, arg2))

    @staticmethod
    @overload
    def toString(arg0: bool, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toString(boolean,java.lang.String,java.lang.String)"""
        return str.__wrap(__BooleanUtils.toString(__boolean.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def toBoolean(arg0: int) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBoolean(int)"""
        return bool.__wrap(__BooleanUtils.toBoolean(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def toIntegerObject(toIntegerObject) -> 'Integer':
        """public static java.lang.Integer org.apache.commons.lang3.BooleanUtils.toIntegerObject(java.lang.Boolean,java.lang.Integer,java.lang.Integer,java.lang.Integer)"""
        return __transform(__arg0, arg1, arg2, arg3.BooleanUtils(arg0: 'Boolean', arg1: 'Integer', arg2: 'Integer', arg3: 'Integer')).'Integer'Value()

    @staticmethod
    @overload
    def toStringTrueFalse(arg0: 'Boolean') -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toStringTrueFalse(java.lang.Boolean)"""
        return str.__wrap(__BooleanUtils.toStringTrueFalse(arg0))

    @staticmethod
    @overload
    def and(*arg0: 'Boolean') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.and(java.lang.Boolean...)"""
        return Boolean.__wrap(__BooleanUtils.and(arg0))

    @staticmethod
    @overload
    def values() -> 'List':
        """public static java.util.List<java.lang.Boolean> org.apache.commons.lang3.BooleanUtils.values()"""
        return List.__wrap(__BooleanUtils.values())

    @staticmethod
    @overload
    def toBooleanObject(arg0: str) -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.toBooleanObject(java.lang.String)"""
        return Boolean.__wrap(__BooleanUtils.toBooleanObject(arg0))

    @staticmethod
    @overload
    def negate(arg0: 'Boolean') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.negate(java.lang.Boolean)"""
        return Boolean.__wrap(__BooleanUtils.negate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.BooleanUtils()"""
        val = __BooleanUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def forEach(arg0: 'Consumer'):
        """public static void org.apache.commons.lang3.BooleanUtils.forEach(java.util.function.Consumer<java.lang.Boolean>)"""
        __BooleanUtils.forEach(arg0)

    @staticmethod
    @overload
    def xor(*arg0: 'Boolean') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.xor(java.lang.Boolean...)"""
        return Boolean.__wrap(__BooleanUtils.xor(arg0))

    @staticmethod
    @overload
    def or(*arg0: bool) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.or(boolean...)"""
        return bool.__wrap(__BooleanUtils.or(arg0))

    @staticmethod
    @overload
    def toIntegerObject(toIntegerObject) -> 'Integer':
        """public static java.lang.Integer org.apache.commons.lang3.BooleanUtils.toIntegerObject(boolean,java.lang.Integer,java.lang.Integer)"""
        return __transform(____boolean.valueOf(arg0), arg1, arg2.BooleanUtils(arg0: bool, arg1: 'Integer', arg2: 'Integer')).'Integer'Value()

    @staticmethod
    @overload
    def isNotTrue(arg0: 'Boolean') -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.isNotTrue(java.lang.Boolean)"""
        return bool.__wrap(__BooleanUtils.isNotTrue(arg0))

    @staticmethod
    @overload
    def toBoolean(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBoolean(java.lang.String)"""
        return bool.__wrap(__BooleanUtils.toBoolean(arg0))

    @staticmethod
    @overload
    def isTrue(arg0: 'Boolean') -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.isTrue(java.lang.Boolean)"""
        return bool.__wrap(__BooleanUtils.isTrue(arg0))

    @staticmethod
    @overload
    def toBooleanObject(arg0: int, arg1: int, arg2: int, arg3: int) -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.toBooleanObject(int,int,int,int)"""
        return Boolean.__wrap(__BooleanUtils.toBooleanObject(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def toBoolean(arg0: 'Integer', arg1: 'Integer', arg2: 'Integer') -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBoolean(java.lang.Integer,java.lang.Integer,java.lang.Integer)"""
        return bool.__wrap(__BooleanUtils.toBoolean(arg0, arg1, arg2))

    @staticmethod
    @overload
    def toString(arg0: 'Boolean', arg1: str, arg2: str, arg3: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toString(java.lang.Boolean,java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__BooleanUtils.toString(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def toBoolean(arg0: 'Boolean') -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBoolean(java.lang.Boolean)"""
        return bool.__wrap(__BooleanUtils.toBoolean(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def toStringOnOff(arg0: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toStringOnOff(boolean)"""
        return str.__wrap(__BooleanUtils.toStringOnOff(__boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def toStringYesNo(arg0: 'Boolean') -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toStringYesNo(java.lang.Boolean)"""
        return str.__wrap(__BooleanUtils.toStringYesNo(arg0))

    @staticmethod
    @overload
    def or(*arg0: 'Boolean') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.or(java.lang.Boolean...)"""
        return Boolean.__wrap(__BooleanUtils.or(arg0))

    @staticmethod
    @overload
    def toBooleanObject(arg0: 'Integer') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.toBooleanObject(java.lang.Integer)"""
        return Boolean.__wrap(__BooleanUtils.toBooleanObject(arg0))

    @staticmethod
    @overload
    def toBooleanObject(arg0: 'Integer', arg1: 'Integer', arg2: 'Integer', arg3: 'Integer') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.toBooleanObject(java.lang.Integer,java.lang.Integer,java.lang.Integer,java.lang.Integer)"""
        return Boolean.__wrap(__BooleanUtils.toBooleanObject(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def primitiveValues() -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.BooleanUtils.primitiveValues()"""
        return List[bool].__wrap(__BooleanUtils.primitiveValues())

    @staticmethod
    @overload
    def isNotFalse(arg0: 'Boolean') -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.isNotFalse(java.lang.Boolean)"""
        return bool.__wrap(__BooleanUtils.isNotFalse(arg0))

    @staticmethod
    @overload
    def toInteger(arg0: bool, arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.BooleanUtils.toInteger(boolean,int,int)"""
        return int.__wrap(__BooleanUtils.toInteger(__boolean.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def oneHot(*arg0: bool) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.oneHot(boolean...)"""
        return bool.__wrap(__BooleanUtils.oneHot(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def and(*arg0: bool) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.and(boolean...)"""
        return bool.__wrap(__BooleanUtils.and(arg0))

    @staticmethod
    @overload
    def toBooleanObject(arg0: str, arg1: str, arg2: str, arg3: str) -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.toBooleanObject(java.lang.String,java.lang.String,java.lang.String,java.lang.String)"""
        return Boolean.__wrap(__BooleanUtils.toBooleanObject(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def toBooleanObject(arg0: int) -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.toBooleanObject(int)"""
        return Boolean.__wrap(__BooleanUtils.toBooleanObject(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def toInteger(arg0: bool) -> int:
        """public static int org.apache.commons.lang3.BooleanUtils.toInteger(boolean)"""
        return int.__wrap(__BooleanUtils.toInteger(__boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def toStringYesNo(arg0: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toStringYesNo(boolean)"""
        return str.__wrap(__BooleanUtils.toStringYesNo(__boolean.valueOf(arg0))) 
 
 
# CLASS: org.apache.commons.lang3.ArraySorter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.lang3.ArraySorter as __ArraySorter
__ArraySorter = __ArraySorter
from builtins import type
from builtins import float
from builtins import object
from typing import List
import java.util.Comparator as Comparator
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
 
class ArraySorter():
    """org.apache.commons.lang3.ArraySorter"""
 
    @staticmethod
    def __wrap(java_value: __ArraySorter) -> 'ArraySorter':
        return ArraySorter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArraySorter):
        """
        Dynamic initializer for ArraySorter.
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
    def sort(arg0: 'int') -> List[int]:
        """public static int[] org.apache.commons.lang3.ArraySorter.sort(int[])"""
        return List[int].__wrap(__ArraySorter.sort(arg0))

    @staticmethod
    @overload
    def sort(arg0: 'Object', arg1: 'Comparator') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArraySorter.sort(T[],java.util.Comparator<? super T>)"""
        return List[object].__wrap(__ArraySorter.sort(arg0, arg1))

    @staticmethod
    @overload
    def sort(arg0: bytes) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArraySorter.sort(byte[])"""
        return List[int].__wrap(__ArraySorter.sort(bytes))

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
    def __init__(self):
        """public org.apache.commons.lang3.ArraySorter()"""
        val = __ArraySorter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def sort(arg0: 'float') -> List[float]:
        """public static float[] org.apache.commons.lang3.ArraySorter.sort(float[])"""
        return List[float].__wrap(__ArraySorter.sort(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def sort(arg0: 'char') -> List[str]:
        """public static char[] org.apache.commons.lang3.ArraySorter.sort(char[])"""
        return List[str].__wrap(__ArraySorter.sort(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def sort(arg0: 'double') -> List[float]:
        """public static double[] org.apache.commons.lang3.ArraySorter.sort(double[])"""
        return List[float].__wrap(__ArraySorter.sort(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def sort(arg0: 'short') -> List[int]:
        """public static short[] org.apache.commons.lang3.ArraySorter.sort(short[])"""
        return List[int].__wrap(__ArraySorter.sort(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def sort(arg0: 'Object') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArraySorter.sort(T[])"""
        return List[object].__wrap(__ArraySorter.sort(arg0))

    @staticmethod
    @overload
    def sort(arg0: 'long') -> List[int]:
        """public static long[] org.apache.commons.lang3.ArraySorter.sort(long[])"""
        return List[int].__wrap(__ArraySorter.sort(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ArraySorter()"""
        val = __ArraySorter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.ThreadUtils
import java.lang.Thread as Thread
import java.lang.ThreadGroup as __ThreadGroup
__ThreadGroup = __ThreadGroup
import java.util.function.Predicate as Predicate
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.time.Duration as Duration
import java.util.Collection as Collection
import java.lang.Thread as __Thread
__Thread = __Thread
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.ThreadGroup as ThreadGroup
import org.apache.commons.lang3.ThreadUtils as __ThreadUtils
__ThreadUtils = __ThreadUtils
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ThreadUtils():
    """org.apache.commons.lang3.ThreadUtils"""
 
    @staticmethod
    def __wrap(java_value: __ThreadUtils) -> 'ThreadUtils':
        return ThreadUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadUtils):
        """
        Dynamic initializer for ThreadUtils.
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
    def findThreadGroups(arg0: 'ThreadGroup', arg1: bool, arg2: 'Predicate') -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroups(java.lang.ThreadGroup,boolean,java.util.function.Predicate<java.lang.ThreadGroup>)"""
        return Collection.__wrap(__ThreadUtils.findThreadGroups(arg0, __boolean.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getAllThreads() -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.getAllThreads()"""
        return Collection.__wrap(__ThreadUtils.getAllThreads())

    @staticmethod
    @overload
    def getSystemThreadGroup() -> 'ThreadGroup':
        """public static java.lang.ThreadGroup org.apache.commons.lang3.ThreadUtils.getSystemThreadGroup()"""
        return ThreadGroup.__wrap(__ThreadUtils.getSystemThreadGroup())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getAllThreadGroups() -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.getAllThreadGroups()"""
        return Collection.__wrap(__ThreadUtils.getAllThreadGroups())

    @staticmethod
    @overload
    def sleep(arg0: 'Duration'):
        """public static void org.apache.commons.lang3.ThreadUtils.sleep(java.time.Duration) throws java.lang.InterruptedException"""
        __ThreadUtils.sleep(arg0)

    @staticmethod
    @overload
    def findThreads(arg0: 'ThreadGroup', arg1: bool, arg2: 'ThreadPredicate') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreads(java.lang.ThreadGroup,boolean,org.apache.commons.lang3.ThreadUtils$ThreadPredicate)"""
        return Collection.__wrap(__ThreadUtils.findThreads(arg0, __boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def findThreadsByName(arg0: str) -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreadsByName(java.lang.String)"""
        return Collection.__wrap(__ThreadUtils.findThreadsByName(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def findThreadById(arg0: int, arg1: str) -> 'Thread':
        """public static java.lang.Thread org.apache.commons.lang3.ThreadUtils.findThreadById(long,java.lang.String)"""
        return Thread.__wrap(__ThreadUtils.findThreadById(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def findThreadById(arg0: int) -> 'Thread':
        """public static java.lang.Thread org.apache.commons.lang3.ThreadUtils.findThreadById(long)"""
        return Thread.__wrap(__ThreadUtils.findThreadById(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def sleepQuietly(arg0: 'Duration'):
        """public static void org.apache.commons.lang3.ThreadUtils.sleepQuietly(java.time.Duration)"""
        __ThreadUtils.sleepQuietly(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def join(arg0: 'Thread', arg1: 'Duration'):
        """public static void org.apache.commons.lang3.ThreadUtils.join(java.lang.Thread,java.time.Duration) throws java.lang.InterruptedException"""
        __ThreadUtils.join(arg0, arg1)

    @staticmethod
    @overload
    def findThreads(arg0: 'ThreadPredicate') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreads(org.apache.commons.lang3.ThreadUtils$ThreadPredicate)"""
        return Collection.__wrap(__ThreadUtils.findThreads(arg0))

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
    def findThreads(arg0: 'Predicate') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreads(java.util.function.Predicate<java.lang.Thread>)"""
        return Collection.__wrap(__ThreadUtils.findThreads(arg0))

    @staticmethod
    @overload
    def findThreadGroups(arg0: 'Predicate') -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroups(java.util.function.Predicate<java.lang.ThreadGroup>)"""
        return Collection.__wrap(__ThreadUtils.findThreadGroups(arg0))

    @staticmethod
    @overload
    def findThreads(arg0: 'ThreadGroup', arg1: bool, arg2: 'Predicate') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreads(java.lang.ThreadGroup,boolean,java.util.function.Predicate<java.lang.Thread>)"""
        return Collection.__wrap(__ThreadUtils.findThreads(arg0, __boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def findThreadGroups(arg0: 'ThreadGroup', arg1: bool, arg2: 'ThreadGroupPredicate') -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroups(java.lang.ThreadGroup,boolean,org.apache.commons.lang3.ThreadUtils$ThreadGroupPredicate)"""
        return Collection.__wrap(__ThreadUtils.findThreadGroups(arg0, __boolean.valueOf(arg1), arg2))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ThreadUtils()"""
        val = __ThreadUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def findThreadGroupsByName(arg0: str) -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroupsByName(java.lang.String)"""
        return Collection.__wrap(__ThreadUtils.findThreadGroupsByName(arg0))

    @staticmethod
    @overload
    def findThreadById(arg0: int, arg1: 'ThreadGroup') -> 'Thread':
        """public static java.lang.Thread org.apache.commons.lang3.ThreadUtils.findThreadById(long,java.lang.ThreadGroup)"""
        return Thread.__wrap(__ThreadUtils.findThreadById(__long.valueOf(arg0), arg1))

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
    def findThreadsByName(arg0: str, arg1: 'ThreadGroup') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreadsByName(java.lang.String,java.lang.ThreadGroup)"""
        return Collection.__wrap(__ThreadUtils.findThreadsByName(arg0, arg1))

    @staticmethod
    @overload
    def findThreadGroups(arg0: 'ThreadGroupPredicate') -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroups(org.apache.commons.lang3.ThreadUtils$ThreadGroupPredicate)"""
        return Collection.__wrap(__ThreadUtils.findThreadGroups(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ThreadUtils()"""
        val = __ThreadUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def findThreadsByName(arg0: str, arg1: str) -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreadsByName(java.lang.String,java.lang.String)"""
        return Collection.__wrap(__ThreadUtils.findThreadsByName(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableSupplier
import org.apache.commons.lang3.Functions as __Functions_FailableSupplier
__FailableSupplier = __Functions_FailableSupplier.FailableSupplier
from abc import abstractmethod, ABC
 
class FailableSupplier(ABC):
    """org.apache.commons.lang3.Functions.FailableSupplier"""
 
    @staticmethod
    def __wrap(java_value: __FailableSupplier) -> 'FailableSupplier':
        return FailableSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableSupplier):
        """
        Dynamic initializer for FailableSupplier.
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
    def get(self, ):
        """public abstract R org.apache.commons.lang3.Functions$FailableSupplier.get() throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableBiPredicate
import org.apache.commons.lang3.Functions as __Functions_FailableBiPredicate
__FailableBiPredicate = __Functions_FailableBiPredicate.FailableBiPredicate
from abc import abstractmethod, ABC
 
class FailableBiPredicate(ABC):
    """org.apache.commons.lang3.Functions.FailableBiPredicate"""
 
    @staticmethod
    def __wrap(java_value: __FailableBiPredicate) -> 'FailableBiPredicate':
        return FailableBiPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableBiPredicate):
        """
        Dynamic initializer for FailableBiPredicate.
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
    def test(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.lang3.Functions$FailableBiPredicate.test(O1,O2) throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableFunction
import org.apache.commons.lang3.Functions as __Functions_FailableFunction
__FailableFunction = __Functions_FailableFunction.FailableFunction
from abc import abstractmethod, ABC
 
class FailableFunction(ABC):
    """org.apache.commons.lang3.Functions.FailableFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableFunction) -> 'FailableFunction':
        return FailableFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableFunction):
        """
        Dynamic initializer for FailableFunction.
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
    def apply(self, arg0: object):
        """public abstract R org.apache.commons.lang3.Functions$FailableFunction.apply(I) throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.NotImplementedException
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
import org.apache.commons.lang3.NotImplementedException as __NotImplementedException
__NotImplementedException = __NotImplementedException
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
 
class NotImplementedException():
    """org.apache.commons.lang3.NotImplementedException"""
 
    @staticmethod
    def __wrap(java_value: __NotImplementedException) -> 'NotImplementedException':
        return NotImplementedException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NotImplementedException):
        """
        Dynamic initializer for NotImplementedException.
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

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.NotImplementedException(java.lang.Throwable)"""
        val = __NotImplementedException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.NotImplementedException(java.lang.String,java.lang.Throwable)"""
        val = __NotImplementedException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.NotImplementedException()"""
        val = __NotImplementedException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Throwable', arg1: str):
        """public org.apache.commons.lang3.NotImplementedException(java.lang.Throwable,java.lang.String)"""
        val = __NotImplementedException(arg0, arg1)
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
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.NotImplementedException(java.lang.String)"""
        val = __NotImplementedException(arg0)
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

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.NotImplementedException()"""
        val = __NotImplementedException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable', arg2: str):
        """public org.apache.commons.lang3.NotImplementedException(java.lang.String,java.lang.Throwable,java.lang.String)"""
        val = __NotImplementedException(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCode(self) -> str:
        """public java.lang.String org.apache.commons.lang3.NotImplementedException.getCode()"""
        return str.__wrap(super(NotImplementedException, self).getCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public org.apache.commons.lang3.NotImplementedException(java.lang.String,java.lang.String)"""
        val = __NotImplementedException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: org.apache.commons.lang3.JavaVersion
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import org.apache.commons.lang3.JavaVersion as __JavaVersion
__JavaVersion = __JavaVersion
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import int
 
class JavaVersion():
    """org.apache.commons.lang3.JavaVersion"""
 
    @staticmethod
    def __wrap(java_value: __JavaVersion) -> 'JavaVersion':
        return JavaVersion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JavaVersion):
        """
        Dynamic initializer for JavaVersion.
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
    def atLeast(self, arg0: 'JavaVersion') -> bool:
        """public boolean org.apache.commons.lang3.JavaVersion.atLeast(org.apache.commons.lang3.JavaVersion)"""
        return bool.__wrap(super(__JavaVersion, self).atLeast(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def values() -> List['JavaVersion']:
        """public static org.apache.commons.lang3.JavaVersion[] org.apache.commons.lang3.JavaVersion.values()"""
        return List[JavaVersion].__wrap(__JavaVersion.values())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'JavaVersion':
        """public static org.apache.commons.lang3.JavaVersion org.apache.commons.lang3.JavaVersion.valueOf(java.lang.String)"""
        return JavaVersion.__wrap(__JavaVersion.valueOf(arg0))

    @overload
    def atMost(self, arg0: 'JavaVersion') -> bool:
        """public boolean org.apache.commons.lang3.JavaVersion.atMost(org.apache.commons.lang3.JavaVersion)"""
        return bool.__wrap(super(__JavaVersion, self).atMost(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.JavaVersion.toString()"""
        return str.__wrap(super(JavaVersion, self).toString()) 
 
 
# CLASS: org.apache.commons.lang3.ClassUtils$Interfaces
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.ClassUtils as __ClassUtils_Interfaces
__Interfaces = __ClassUtils_Interfaces.Interfaces
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Interfaces():
    """org.apache.commons.lang3.ClassUtils.Interfaces"""
 
    @staticmethod
    def __wrap(java_value: __Interfaces) -> 'Interfaces':
        return Interfaces(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Interfaces):
        """
        Dynamic initializer for Interfaces.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Interfaces':
        """public static org.apache.commons.lang3.ClassUtils$Interfaces org.apache.commons.lang3.ClassUtils$Interfaces.valueOf(java.lang.String)"""
        return Interfaces.__wrap(__Interfaces.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @staticmethod
    @overload
    def values() -> List['Interfaces']:
        """public static org.apache.commons.lang3.ClassUtils$Interfaces[] org.apache.commons.lang3.ClassUtils$Interfaces.values()"""
        return List[Interfaces].__wrap(__Interfaces.values())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: org.apache.commons.lang3.IntegerRange
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.Range as __Range
__Range = __Range
import java.lang.Comparable as Comparable
from builtins import object
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.IntegerRange as __IntegerRange
__IntegerRange = __IntegerRange
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IntegerRange():
    """org.apache.commons.lang3.IntegerRange"""
 
    @staticmethod
    def __wrap(java_value: __IntegerRange) -> 'IntegerRange':
        return IntegerRange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntegerRange):
        """
        Dynamic initializer for IntegerRange.
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
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T)"""
        return Range.__wrap(__Range.between(arg0, arg1))

    @staticmethod
    @overload
    def of(arg0: int, arg1: int) -> 'IntegerRange':
        """public static org.apache.commons.lang3.IntegerRange org.apache.commons.lang3.IntegerRange.of(int,int)"""
        return IntegerRange.__wrap(__IntegerRange.of(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isAfter(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfter(T)"""
        return bool.__wrap(super(__Range, self).isAfter(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.contains(T)"""
        return bool.__wrap(super(__Range, self).contains(arg0))

    @override
    @overload
    def isNaturalOrdering(self) -> bool:
        """public boolean org.apache.commons.lang3.Range.isNaturalOrdering()"""
        return bool.__wrap(super(Range, self).isNaturalOrdering())

    @staticmethod
    @overload
    def is(arg0: object, arg1: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.is(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.equals(java.lang.Object)"""
        return bool.__wrap(super(__Range, self).equals(arg0))

    @overload
    def isStartedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isStartedBy(T)"""
        return bool.__wrap(super(__Range, self).isStartedBy(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Integer', arg1: 'Integer') -> 'IntegerRange':
        """public static org.apache.commons.lang3.IntegerRange org.apache.commons.lang3.IntegerRange.of(java.lang.Integer,java.lang.Integer)"""
        return IntegerRange.__wrap(__IntegerRange.of(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.Range.hashCode()"""
        return int.__wrap(super(Range, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString()"""
        return str.__wrap(super(Range, self).toString())

    @overload
    def isBefore(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isBefore(T)"""
        return bool.__wrap(super(__Range, self).isBefore(arg0))

    @overload
    def intersectionWith(self, arg0: 'Range') -> 'Range':
        """public org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.intersectionWith(org.apache.commons.lang3.Range<T>)"""
        return 'Range'.__wrap(super(__Range, self).intersectionWith(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T)"""
        return Range.__wrap(__Range.of(arg0, arg1))

    @overload
    def isAfterRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfterRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isAfterRange(arg0))

    @override
    @overload
    def getMinimum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMinimum()"""
        return object.__wrap(super(Range, self).getMinimum())

    @override
    @overload
    def getComparator(self) -> 'Comparator':
        """public java.util.Comparator<T> org.apache.commons.lang3.Range.getComparator()"""
        return 'Comparator'.__wrap(super(Range, self).getComparator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isEndedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isEndedBy(T)"""
        return bool.__wrap(super(__Range, self).isEndedBy(arg0))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString(java.lang.String)"""
        return str.__wrap(super(__Range, self).toString(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getMaximum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMaximum()"""
        return object.__wrap(super(Range, self).getMaximum())

    @overload
    def isOverlappedBy(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isOverlappedBy(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isOverlappedBy(arg0))

    @overload
    def fit(self, arg0: object) -> object:
        """public T org.apache.commons.lang3.Range.fit(T)"""
        return object.__wrap(super(__Range, self).fit(arg0))

    @overload
    def elementCompareTo(self, arg0: object) -> int:
        """public int org.apache.commons.lang3.Range.elementCompareTo(T)"""
        return int.__wrap(super(__Range, self).elementCompareTo(arg0))

    @overload
    def isBeforeRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isBeforeRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isBeforeRange(arg0))

    @staticmethod
    @overload
    def is(arg0: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T)"""
        return Range.__wrap(__Range.is(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def between(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.between(arg0, arg1, arg2))

    @overload
    def containsRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.containsRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).containsRange(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.CharSetUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.CharSetUtils as __CharSetUtils
__CharSetUtils = __CharSetUtils
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
 
class CharSetUtils():
    """org.apache.commons.lang3.CharSetUtils"""
 
    @staticmethod
    def __wrap(java_value: __CharSetUtils) -> 'CharSetUtils':
        return CharSetUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharSetUtils):
        """
        Dynamic initializer for CharSetUtils.
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
    def count(arg0: str, *arg1: str) -> int:
        """public static int org.apache.commons.lang3.CharSetUtils.count(java.lang.String,java.lang.String...)"""
        return int.__wrap(__CharSetUtils.count(arg0, arg1))

    @staticmethod
    @overload
    def containsAny(arg0: str, *arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharSetUtils.containsAny(java.lang.String,java.lang.String...)"""
        return bool.__wrap(__CharSetUtils.containsAny(arg0, arg1))

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

    @staticmethod
    @overload
    def delete(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.CharSetUtils.delete(java.lang.String,java.lang.String...)"""
        return str.__wrap(__CharSetUtils.delete(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.CharSetUtils()"""
        val = __CharSetUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def keep(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.CharSetUtils.keep(java.lang.String,java.lang.String...)"""
        return str.__wrap(__CharSetUtils.keep(arg0, arg1))

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
    def squeeze(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.CharSetUtils.squeeze(java.lang.String,java.lang.String...)"""
        return str.__wrap(__CharSetUtils.squeeze(arg0, arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.CharSetUtils()"""
        val = __CharSetUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.Streams$ArrayCollector
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.util.function.BinaryOperator as __BinaryOperator
__BinaryOperator = __BinaryOperator
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.function.Function as __Function
__Function = __Function
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.lang3.Streams as __Streams_ArrayCollector
__ArrayCollector = __Streams_ArrayCollector.ArrayCollector
import java.lang.String as __String
__String = __String
import java.util.function.BinaryOperator as BinaryOperator
import java.lang.Object as __Object
__Object = __Object
import java.util.function.Supplier as __Supplier
__Supplier = __Supplier
import java.util.function.BiConsumer as __BiConsumer
__BiConsumer = __BiConsumer
import java.util.function.Function as Function
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ArrayCollector():
    """org.apache.commons.lang3.Streams.ArrayCollector"""
 
    @staticmethod
    def __wrap(java_value: __ArrayCollector) -> 'ArrayCollector':
        return ArrayCollector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayCollector):
        """
        Dynamic initializer for ArrayCollector.
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
    def __init__(self, arg0: 'Class'):
        """public org.apache.commons.lang3.Streams$ArrayCollector(java.lang.Class<O>)"""
        val = __ArrayCollector(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def characteristics(self) -> 'Set':
        """public java.util.Set<java.util.stream.Collector$Characteristics> org.apache.commons.lang3.Streams$ArrayCollector.characteristics()"""
        return 'Set'.__wrap(super(ArrayCollector, self).characteristics())

    @override
    @overload
    def combiner(self) -> 'BinaryOperator':
        """public java.util.function.BinaryOperator<java.util.List<O>> org.apache.commons.lang3.Streams$ArrayCollector.combiner()"""
        return 'BinaryOperator'.__wrap(super(ArrayCollector, self).combiner())

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def accumulator(self) -> 'BiConsumer':
        """public java.util.function.BiConsumer<java.util.List<O>, O> org.apache.commons.lang3.Streams$ArrayCollector.accumulator()"""
        return 'BiConsumer'.__wrap(super(ArrayCollector, self).accumulator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def finisher(self) -> 'Function':
        """public java.util.function.Function<java.util.List<O>, O[]> org.apache.commons.lang3.Streams$ArrayCollector.finisher()"""
        return 'Function'.__wrap(super(ArrayCollector, self).finisher())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def supplier(self) -> 'Supplier':
        """public java.util.function.Supplier<java.util.List<O>> org.apache.commons.lang3.Streams$ArrayCollector.supplier()"""
        return 'Supplier'.__wrap(super(ArrayCollector, self).supplier()) 
 
 
# CLASS: org.apache.commons.lang3.LongRange
from builtins import str
import java.lang.Long as Long
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.Range as __Range
__Range = __Range
import java.lang.Comparable as Comparable
from builtins import object
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.LongRange as __LongRange
__LongRange = __LongRange
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LongRange():
    """org.apache.commons.lang3.LongRange"""
 
    @staticmethod
    def __wrap(java_value: __LongRange) -> 'LongRange':
        return LongRange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongRange):
        """
        Dynamic initializer for LongRange.
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
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T)"""
        return Range.__wrap(__Range.between(arg0, arg1))

    @staticmethod
    @overload
    def of(arg0: int, arg1: int) -> 'LongRange':
        """public static org.apache.commons.lang3.LongRange org.apache.commons.lang3.LongRange.of(long,long)"""
        return LongRange.__wrap(__LongRange.of(__long.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isAfter(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfter(T)"""
        return bool.__wrap(super(__Range, self).isAfter(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.contains(T)"""
        return bool.__wrap(super(__Range, self).contains(arg0))

    @override
    @overload
    def isNaturalOrdering(self) -> bool:
        """public boolean org.apache.commons.lang3.Range.isNaturalOrdering()"""
        return bool.__wrap(super(Range, self).isNaturalOrdering())

    @staticmethod
    @overload
    def is(arg0: object, arg1: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.is(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.equals(java.lang.Object)"""
        return bool.__wrap(super(__Range, self).equals(arg0))

    @overload
    def isStartedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isStartedBy(T)"""
        return bool.__wrap(super(__Range, self).isStartedBy(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.Range.hashCode()"""
        return int.__wrap(super(Range, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString()"""
        return str.__wrap(super(Range, self).toString())

    @overload
    def isBefore(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isBefore(T)"""
        return bool.__wrap(super(__Range, self).isBefore(arg0))

    @overload
    def intersectionWith(self, arg0: 'Range') -> 'Range':
        """public org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.intersectionWith(org.apache.commons.lang3.Range<T>)"""
        return 'Range'.__wrap(super(__Range, self).intersectionWith(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T)"""
        return Range.__wrap(__Range.of(arg0, arg1))

    @overload
    def isAfterRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfterRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isAfterRange(arg0))

    @override
    @overload
    def getMinimum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMinimum()"""
        return object.__wrap(super(Range, self).getMinimum())

    @override
    @overload
    def getComparator(self) -> 'Comparator':
        """public java.util.Comparator<T> org.apache.commons.lang3.Range.getComparator()"""
        return 'Comparator'.__wrap(super(Range, self).getComparator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isEndedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isEndedBy(T)"""
        return bool.__wrap(super(__Range, self).isEndedBy(arg0))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString(java.lang.String)"""
        return str.__wrap(super(__Range, self).toString(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getMaximum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMaximum()"""
        return object.__wrap(super(Range, self).getMaximum())

    @overload
    def isOverlappedBy(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isOverlappedBy(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isOverlappedBy(arg0))

    @overload
    def fit(self, arg0: object) -> object:
        """public T org.apache.commons.lang3.Range.fit(T)"""
        return object.__wrap(super(__Range, self).fit(arg0))

    @overload
    def elementCompareTo(self, arg0: object) -> int:
        """public int org.apache.commons.lang3.Range.elementCompareTo(T)"""
        return int.__wrap(super(__Range, self).elementCompareTo(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Long', arg1: 'Long') -> 'LongRange':
        """public static org.apache.commons.lang3.LongRange org.apache.commons.lang3.LongRange.of(java.lang.Long,java.lang.Long)"""
        return LongRange.__wrap(__LongRange.of(arg0, arg1))

    @overload
    def isBeforeRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isBeforeRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isBeforeRange(arg0))

    @staticmethod
    @overload
    def is(arg0: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T)"""
        return Range.__wrap(__Range.is(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def between(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.between(arg0, arg1, arg2))

    @overload
    def containsRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.containsRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).containsRange(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.Streams
from builtins import str
import org.apache.commons.lang3.Streams as __Streams_FailableStream
__FailableStream = __Streams_FailableStream.FailableStream
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.stream.Collector as __Collector
__Collector = __Collector
import java.util.Collection as Collection
import java.util.stream.Collector as Collector
import org.apache.commons.lang3.Streams as __Streams
__Streams = __Streams
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Streams():
    """org.apache.commons.lang3.Streams"""
 
    @staticmethod
    def __wrap(java_value: __Streams) -> 'Streams':
        return Streams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Streams):
        """
        Dynamic initializer for Streams.
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
    def stream(arg0: 'Collection') -> 'FailableStream':
        """public static <O> org.apache.commons.lang3.Streams$FailableStream<O> org.apache.commons.lang3.Streams.stream(java.util.Collection<O>)"""
        return FailableStream.__wrap(__Streams.stream(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def toArray(arg0: 'Class') -> 'Collector':
        """public static <O> java.util.stream.Collector<O, ?, O[]> org.apache.commons.lang3.Streams.toArray(java.lang.Class<O>)"""
        return Collector.__wrap(__Streams.toArray(arg0))

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.Streams()"""
        val = __Streams()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.Streams()"""
        val = __Streams()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @staticmethod
    @overload
    def stream(arg0: 'Stream') -> 'FailableStream':
        """public static <O> org.apache.commons.lang3.Streams$FailableStream<O> org.apache.commons.lang3.Streams.stream(java.util.stream.Stream<O>)"""
        return FailableStream.__wrap(__Streams.stream(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableBiFunction
from abc import abstractmethod, ABC
import org.apache.commons.lang3.Functions as __Functions_FailableBiFunction
__FailableBiFunction = __Functions_FailableBiFunction.FailableBiFunction
 
class FailableBiFunction(ABC):
    """org.apache.commons.lang3.Functions.FailableBiFunction"""
 
    @staticmethod
    def __wrap(java_value: __FailableBiFunction) -> 'FailableBiFunction':
        return FailableBiFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableBiFunction):
        """
        Dynamic initializer for FailableBiFunction.
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
    def apply(self, arg0: object, arg1: object):
        """public abstract R org.apache.commons.lang3.Functions$FailableBiFunction.apply(O1,O2) throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableConsumer
import org.apache.commons.lang3.Functions as __Functions_FailableConsumer
__FailableConsumer = __Functions_FailableConsumer.FailableConsumer
from abc import abstractmethod, ABC
 
class FailableConsumer(ABC):
    """org.apache.commons.lang3.Functions.FailableConsumer"""
 
    @staticmethod
    def __wrap(java_value: __FailableConsumer) -> 'FailableConsumer':
        return FailableConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableConsumer):
        """
        Dynamic initializer for FailableConsumer.
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
    def accept(self, arg0: object):
        """public abstract void org.apache.commons.lang3.Functions$FailableConsumer.accept(O) throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.ObjectUtils
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
import java.lang.Double as __double
from builtins import bool
import java.lang.Comparable as __Comparable
__Comparable = __Comparable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.lang3.ObjectUtils as __ObjectUtils
__ObjectUtils = __ObjectUtils
from builtins import float
import java.time.Duration as Duration
from builtins import object
import java.lang.Comparable as Comparable
import java.lang.Appendable as Appendable
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
try:
    from pyapache.lang3 import text
except ImportError:
    text = __import_once__("pyapache.lang3.text")

from builtins import int
 
class ObjectUtils():
    """org.apache.commons.lang3.ObjectUtils"""
 
    @staticmethod
    def __wrap(java_value: __ObjectUtils) -> 'ObjectUtils':
        return ObjectUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectUtils):
        """
        Dynamic initializer for ObjectUtils.
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
    def firstNonNull(*arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.firstNonNull(T...)"""
        return object.__wrap(__ObjectUtils.firstNonNull(arg0))

    @staticmethod
    @overload
    def CONST_BYTE(arg0: int) -> int:
        """public static byte org.apache.commons.lang3.ObjectUtils.CONST_BYTE(int)"""
        return int.__wrap(__ObjectUtils.CONST_BYTE(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def getFirstNonNull(*arg0: 'Supplier') -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.getFirstNonNull(java.util.function.Supplier<T>...)"""
        return object.__wrap(__ObjectUtils.getFirstNonNull(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ObjectUtils()"""
        val = __ObjectUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def isEmpty(arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.isEmpty(java.lang.Object)"""
        return bool.__wrap(__ObjectUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def mode(*arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.mode(T...)"""
        return object.__wrap(__ObjectUtils.mode(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def CONST(arg0: float) -> float:
        """public static float org.apache.commons.lang3.ObjectUtils.CONST(float)"""
        return float.__wrap(__ObjectUtils.CONST(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def isArray(arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.isArray(java.lang.Object)"""
        return bool.__wrap(__ObjectUtils.isArray(arg0))

    @staticmethod
    @overload
    def getIfNull(arg0: object, arg1: 'Supplier') -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.getIfNull(T,java.util.function.Supplier<T>)"""
        return object.__wrap(__ObjectUtils.getIfNull(arg0, arg1))

    @staticmethod
    @overload
    def CONST(arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.CONST(T)"""
        return object.__wrap(__ObjectUtils.CONST(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def requireNonEmpty(arg0: object, arg1: str) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.requireNonEmpty(T,java.lang.String)"""
        return object.__wrap(__ObjectUtils.requireNonEmpty(arg0, arg1))

    @staticmethod
    @overload
    def anyNull(*arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.anyNull(java.lang.Object...)"""
        return bool.__wrap(__ObjectUtils.anyNull(arg0))

    @staticmethod
    @overload
    def max(*arg0: 'Comparable') -> 'Comparable':
        """public static <T extends java.lang.Comparable<? super T>> T org.apache.commons.lang3.ObjectUtils.max(T...)"""
        return Comparable.__wrap(__ObjectUtils.max(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ObjectUtils()"""
        val = __ObjectUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def hashCodeMulti(*arg0: object) -> int:
        """public static int org.apache.commons.lang3.ObjectUtils.hashCodeMulti(java.lang.Object...)"""
        return int.__wrap(__ObjectUtils.hashCodeMulti(arg0))

    @staticmethod
    @overload
    def CONST(arg0: float) -> float:
        """public static double org.apache.commons.lang3.ObjectUtils.CONST(double)"""
        return float.__wrap(__ObjectUtils.CONST(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def anyNotNull(*arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.anyNotNull(java.lang.Object...)"""
        return bool.__wrap(__ObjectUtils.anyNotNull(arg0))

    @staticmethod
    @overload
    def wait(arg0: object, arg1: 'Duration'):
        """public static void org.apache.commons.lang3.ObjectUtils.wait(java.lang.Object,java.time.Duration) throws java.lang.InterruptedException"""
        __ObjectUtils.wait(arg0, arg1)

    @staticmethod
    @overload
    def CONST(arg0: str) -> str:
        """public static char org.apache.commons.lang3.ObjectUtils.CONST(char)"""
        return str.__wrap(__ObjectUtils.CONST(__char.valueOf(arg0)))

    @staticmethod
    @overload
    def identityToString(arg0: 'StringBuffer', arg1: object):
        """public static void org.apache.commons.lang3.ObjectUtils.identityToString(java.lang.StringBuffer,java.lang.Object)"""
        __ObjectUtils.identityToString(arg0, arg1)

    @staticmethod
    @overload
    def toString(arg0: object, arg1: 'Supplier') -> str:
        """public static java.lang.String org.apache.commons.lang3.ObjectUtils.toString(java.lang.Object,java.util.function.Supplier<java.lang.String>)"""
        return str.__wrap(__ObjectUtils.toString(arg0, arg1))

    @staticmethod
    @overload
    def CONST(arg0: int) -> int:
        """public static byte org.apache.commons.lang3.ObjectUtils.CONST(byte)"""
        return int.__wrap(__ObjectUtils.CONST(__byte.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def compare(arg0: 'Comparable', arg1: 'Comparable', arg2: bool) -> int:
        """public static <T extends java.lang.Comparable<? super T>> int org.apache.commons.lang3.ObjectUtils.compare(T,T,boolean)"""
        return int.__wrap(__ObjectUtils.compare(arg0, arg1, __boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def median(arg0: 'Comparator', *arg1: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.median(java.util.Comparator<T>,T...)"""
        return object.__wrap(__ObjectUtils.median(arg0, arg1))

    @staticmethod
    @overload
    def hashCode(arg0: object) -> int:
        """public static int org.apache.commons.lang3.ObjectUtils.hashCode(java.lang.Object)"""
        return int.__wrap(__ObjectUtils.hashCode(arg0))

    @staticmethod
    @overload
    def CONST(arg0: int) -> int:
        """public static long org.apache.commons.lang3.ObjectUtils.CONST(long)"""
        return int.__wrap(__ObjectUtils.CONST(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def CONST_SHORT(arg0: int) -> int:
        """public static short org.apache.commons.lang3.ObjectUtils.CONST_SHORT(int)"""
        return int.__wrap(__ObjectUtils.CONST_SHORT(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def isNotEmpty(arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.isNotEmpty(java.lang.Object)"""
        return bool.__wrap(__ObjectUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def identityToString(arg0: 'Appendable', arg1: object):
        """public static void org.apache.commons.lang3.ObjectUtils.identityToString(java.lang.Appendable,java.lang.Object) throws java.io.IOException"""
        __ObjectUtils.identityToString(arg0, arg1)

    @staticmethod
    @overload
    def clone(arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.clone(T)"""
        return object.__wrap(__ObjectUtils.clone(arg0))

    @staticmethod
    @overload
    def median(*arg0: 'Comparable') -> 'Comparable':
        """public static <T extends java.lang.Comparable<? super T>> T org.apache.commons.lang3.ObjectUtils.median(T...)"""
        return Comparable.__wrap(__ObjectUtils.median(arg0))

    @staticmethod
    @overload
    def cloneIfPossible(arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.cloneIfPossible(T)"""
        return object.__wrap(__ObjectUtils.cloneIfPossible(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def notEqual(arg0: object, arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.notEqual(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(__ObjectUtils.notEqual(arg0, arg1))

    @staticmethod
    @overload
    def toString(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ObjectUtils.toString(java.lang.Object,java.lang.String)"""
        return str.__wrap(__ObjectUtils.toString(arg0, arg1))

    @staticmethod
    @overload
    def identityToString(arg0: 'StrBuilder', arg1: object):
        """public static void org.apache.commons.lang3.ObjectUtils.identityToString(org.apache.commons.lang3.text.StrBuilder,java.lang.Object)"""
        __ObjectUtils.identityToString(arg0, arg1)

    @staticmethod
    @overload
    def min(*arg0: 'Comparable') -> 'Comparable':
        """public static <T extends java.lang.Comparable<? super T>> T org.apache.commons.lang3.ObjectUtils.min(T...)"""
        return Comparable.__wrap(__ObjectUtils.min(arg0))

    @staticmethod
    @overload
    def allNotNull(*arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.allNotNull(java.lang.Object...)"""
        return bool.__wrap(__ObjectUtils.allNotNull(arg0))

    @staticmethod
    @overload
    def toString(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ObjectUtils.toString(java.lang.Object)"""
        return str.__wrap(__ObjectUtils.toString(arg0))

    @staticmethod
    @overload
    def CONST(arg0: int) -> int:
        """public static short org.apache.commons.lang3.ObjectUtils.CONST(short)"""
        return int.__wrap(__ObjectUtils.CONST(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def equals(arg0: object, arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.equals(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(__ObjectUtils.equals(arg0, arg1))

    @staticmethod
    @overload
    def getClass(arg0: object) -> 'type.Class':
        """public static <T> java.lang.Class<T> org.apache.commons.lang3.ObjectUtils.getClass(T)"""
        return type.Class.__wrap(__ObjectUtils.getClass(arg0))

    @staticmethod
    @overload
    def CONST(arg0: bool) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.CONST(boolean)"""
        return bool.__wrap(__ObjectUtils.CONST(__boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def identityToString(arg0: 'StringBuilder', arg1: object):
        """public static void org.apache.commons.lang3.ObjectUtils.identityToString(java.lang.StringBuilder,java.lang.Object)"""
        __ObjectUtils.identityToString(arg0, arg1)

    @staticmethod
    @overload
    def defaultIfNull(arg0: object, arg1: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.defaultIfNull(T,T)"""
        return object.__wrap(__ObjectUtils.defaultIfNull(arg0, arg1))

    @staticmethod
    @overload
    def compare(arg0: 'Comparable', arg1: 'Comparable') -> int:
        """public static <T extends java.lang.Comparable<? super T>> int org.apache.commons.lang3.ObjectUtils.compare(T,T)"""
        return int.__wrap(__ObjectUtils.compare(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def identityToString(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ObjectUtils.identityToString(java.lang.Object)"""
        return str.__wrap(__ObjectUtils.identityToString(arg0))

    @staticmethod
    @overload
    def allNull(*arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.allNull(java.lang.Object...)"""
        return bool.__wrap(__ObjectUtils.allNull(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def hashCodeHex(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ObjectUtils.hashCodeHex(java.lang.Object)"""
        return str.__wrap(__ObjectUtils.hashCodeHex(arg0))

    @staticmethod
    @overload
    def CONST(arg0: int) -> int:
        """public static int org.apache.commons.lang3.ObjectUtils.CONST(int)"""
        return int.__wrap(__ObjectUtils.CONST(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def requireNonEmpty(arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.requireNonEmpty(T)"""
        return object.__wrap(__ObjectUtils.requireNonEmpty(arg0))

    @staticmethod
    @overload
    def identityHashCodeHex(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ObjectUtils.identityHashCodeHex(java.lang.Object)"""
        return str.__wrap(__ObjectUtils.identityHashCodeHex(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.ClassPathUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Package as Package
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.ClassPathUtils as __ClassPathUtils
__ClassPathUtils = __ClassPathUtils
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClassPathUtils():
    """org.apache.commons.lang3.ClassPathUtils"""
 
    @staticmethod
    def __wrap(java_value: __ClassPathUtils) -> 'ClassPathUtils':
        return ClassPathUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClassPathUtils):
        """
        Dynamic initializer for ClassPathUtils.
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
    def toFullyQualifiedPath(arg0: 'Class', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassPathUtils.toFullyQualifiedPath(java.lang.Class<?>,java.lang.String)"""
        return str.__wrap(__ClassPathUtils.toFullyQualifiedPath(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ClassPathUtils()"""
        val = __ClassPathUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def toFullyQualifiedPath(arg0: 'Package', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassPathUtils.toFullyQualifiedPath(java.lang.Package,java.lang.String)"""
        return str.__wrap(__ClassPathUtils.toFullyQualifiedPath(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ClassPathUtils()"""
        val = __ClassPathUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def pathToPackage(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassPathUtils.pathToPackage(java.lang.String)"""
        return str.__wrap(__ClassPathUtils.pathToPackage(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def packageToPath(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassPathUtils.packageToPath(java.lang.String)"""
        return str.__wrap(__ClassPathUtils.packageToPath(arg0))

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

    @staticmethod
    @overload
    def toFullyQualifiedName(arg0: 'Class', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassPathUtils.toFullyQualifiedName(java.lang.Class<?>,java.lang.String)"""
        return str.__wrap(__ClassPathUtils.toFullyQualifiedName(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def toFullyQualifiedName(arg0: 'Package', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassPathUtils.toFullyQualifiedName(java.lang.Package,java.lang.String)"""
        return str.__wrap(__ClassPathUtils.toFullyQualifiedName(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableBiConsumer
import org.apache.commons.lang3.Functions as __Functions_FailableBiConsumer
__FailableBiConsumer = __Functions_FailableBiConsumer.FailableBiConsumer
from abc import abstractmethod, ABC
 
class FailableBiConsumer(ABC):
    """org.apache.commons.lang3.Functions.FailableBiConsumer"""
 
    @staticmethod
    def __wrap(java_value: __FailableBiConsumer) -> 'FailableBiConsumer':
        return FailableBiConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableBiConsumer):
        """
        Dynamic initializer for FailableBiConsumer.
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
    def accept(self, arg0: object, arg1: object):
        """public abstract void org.apache.commons.lang3.Functions$FailableBiConsumer.accept(O1,O2) throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableCallable
from abc import abstractmethod, ABC
import org.apache.commons.lang3.Functions as __Functions_FailableCallable
__FailableCallable = __Functions_FailableCallable.FailableCallable
 
class FailableCallable(ABC):
    """org.apache.commons.lang3.Functions.FailableCallable"""
 
    @staticmethod
    def __wrap(java_value: __FailableCallable) -> 'FailableCallable':
        return FailableCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableCallable):
        """
        Dynamic initializer for FailableCallable.
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
    def call(self, ):
        """public abstract R org.apache.commons.lang3.Functions$FailableCallable.call() throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.SerializationUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import org.apache.commons.lang3.SerializationUtils as __SerializationUtils
__SerializationUtils = __SerializationUtils
import java.io.Serializable as __Serializable
__Serializable = __Serializable
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.io.Serializable as Serializable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SerializationUtils():
    """org.apache.commons.lang3.SerializationUtils"""
 
    @staticmethod
    def __wrap(java_value: __SerializationUtils) -> 'SerializationUtils':
        return SerializationUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SerializationUtils):
        """
        Dynamic initializer for SerializationUtils.
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
    def deserialize(arg0: 'InputStream') -> object:
        """public static <T> T org.apache.commons.lang3.SerializationUtils.deserialize(java.io.InputStream)"""
        return object.__wrap(__SerializationUtils.deserialize(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def clone(arg0: 'Serializable') -> 'Serializable':
        """public static <T extends java.io.Serializable> T org.apache.commons.lang3.SerializationUtils.clone(T)"""
        return Serializable.__wrap(__SerializationUtils.clone(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def serialize(arg0: 'Serializable', arg1: 'OutputStream'):
        """public static void org.apache.commons.lang3.SerializationUtils.serialize(java.io.Serializable,java.io.OutputStream)"""
        __SerializationUtils.serialize(arg0, arg1)

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

    @staticmethod
    @overload
    def serialize(arg0: 'Serializable') -> List[int]:
        """public static byte[] org.apache.commons.lang3.SerializationUtils.serialize(java.io.Serializable)"""
        return List[int].__wrap(__SerializationUtils.serialize(arg0))

    @staticmethod
    @overload
    def deserialize(arg0: bytes) -> object:
        """public static <T> T org.apache.commons.lang3.SerializationUtils.deserialize(byte[])"""
        return object.__wrap(__SerializationUtils.deserialize(bytes))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.SerializationUtils()"""
        val = __SerializationUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def roundtrip(arg0: 'Serializable') -> 'Serializable':
        """public static <T extends java.io.Serializable> T org.apache.commons.lang3.SerializationUtils.roundtrip(T)"""
        return Serializable.__wrap(__SerializationUtils.roundtrip(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.SerializationUtils()"""
        val = __SerializationUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.Conversion
from builtins import str
import java.util.UUID as UUID
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.Conversion as __Conversion
__Conversion = __Conversion
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Conversion():
    """org.apache.commons.lang3.Conversion"""
 
    @staticmethod
    def __wrap(java_value: __Conversion) -> 'Conversion':
        return Conversion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Conversion):
        """
        Dynamic initializer for Conversion.
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
    def intArrayToLong(arg0: 'int', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.apache.commons.lang3.Conversion.intArrayToLong(int[],int,long,int,int)"""
        return int.__wrap(__Conversion.intArrayToLong(arg0, __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def longToHex(arg0: int, arg1: int, arg2: str, arg3: int, arg4: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.Conversion.longToHex(long,int,java.lang.String,int,int)"""
        return str.__wrap(__Conversion.longToHex(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def intToShortArray(arg0: int, arg1: int, arg2: 'short', arg3: int, arg4: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.Conversion.intToShortArray(int,int,short[],int,int)"""
        return List[int].__wrap(__Conversion.intToShortArray(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def hexDigitToInt(arg0: str) -> int:
        """public static int org.apache.commons.lang3.Conversion.hexDigitToInt(char)"""
        return int.__wrap(__Conversion.hexDigitToInt(__char.valueOf(arg0)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.Conversion()"""
        val = __Conversion()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def byteArrayToLong(arg0: bytes, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.apache.commons.lang3.Conversion.byteArrayToLong(byte[],int,long,int,int)"""
        return int.__wrap(__Conversion.byteArrayToLong(bytes, __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def intToHexDigitMsb0(arg0: int) -> str:
        """public static char org.apache.commons.lang3.Conversion.intToHexDigitMsb0(int)"""
        return str.__wrap(__Conversion.intToHexDigitMsb0(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def byteArrayToInt(arg0: bytes, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.apache.commons.lang3.Conversion.byteArrayToInt(byte[],int,int,int,int)"""
        return int.__wrap(__Conversion.byteArrayToInt(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def intToByteArray(arg0: int, arg1: int, arg2: bytes, arg3: int, arg4: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.Conversion.intToByteArray(int,int,byte[],int,int)"""
        return List[int].__wrap(__Conversion.intToByteArray(__int.valueOf(arg0), __int.valueOf(arg1), bytes, __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def byteToHex(arg0: int, arg1: int, arg2: str, arg3: int, arg4: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.Conversion.byteToHex(byte,int,java.lang.String,int,int)"""
        return str.__wrap(__Conversion.byteToHex(__byte.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def hexDigitToBinary(arg0: str) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.Conversion.hexDigitToBinary(char)"""
        return List[bool].__wrap(__Conversion.hexDigitToBinary(__char.valueOf(arg0)))

    @staticmethod
    @overload
    def hexToInt(arg0: str, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.apache.commons.lang3.Conversion.hexToInt(java.lang.String,int,int,int,int)"""
        return int.__wrap(__Conversion.hexToInt(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def hexToByte(arg0: str, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static byte org.apache.commons.lang3.Conversion.hexToByte(java.lang.String,int,byte,int,int)"""
        return int.__wrap(__Conversion.hexToByte(arg0, __int.valueOf(arg1), __byte.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryBeMsb0ToHexDigit(arg0: 'boolean', arg1: int) -> str:
        """public static char org.apache.commons.lang3.Conversion.binaryBeMsb0ToHexDigit(boolean[],int)"""
        return str.__wrap(__Conversion.binaryBeMsb0ToHexDigit(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def longToByteArray(arg0: int, arg1: int, arg2: bytes, arg3: int, arg4: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.Conversion.longToByteArray(long,int,byte[],int,int)"""
        return List[int].__wrap(__Conversion.longToByteArray(__long.valueOf(arg0), __int.valueOf(arg1), bytes, __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryToHexDigit(arg0: 'boolean', arg1: int) -> str:
        """public static char org.apache.commons.lang3.Conversion.binaryToHexDigit(boolean[],int)"""
        return str.__wrap(__Conversion.binaryToHexDigit(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def uuidToByteArray(arg0: 'UUID', arg1: bytes, arg2: int, arg3: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.Conversion.uuidToByteArray(java.util.UUID,byte[],int,int)"""
        return List[int].__wrap(__Conversion.uuidToByteArray(arg0, bytes, __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def hexDigitMsb0ToBinary(arg0: str) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.Conversion.hexDigitMsb0ToBinary(char)"""
        return List[bool].__wrap(__Conversion.hexDigitMsb0ToBinary(__char.valueOf(arg0)))

    @staticmethod
    @overload
    def binaryToLong(arg0: 'boolean', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.apache.commons.lang3.Conversion.binaryToLong(boolean[],int,long,int,int)"""
        return int.__wrap(__Conversion.binaryToLong(arg0, __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryToInt(arg0: 'boolean', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.apache.commons.lang3.Conversion.binaryToInt(boolean[],int,int,int,int)"""
        return int.__wrap(__Conversion.binaryToInt(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def shortArrayToInt(arg0: 'short', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.apache.commons.lang3.Conversion.shortArrayToInt(short[],int,int,int,int)"""
        return int.__wrap(__Conversion.shortArrayToInt(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def intToHex(arg0: int, arg1: int, arg2: str, arg3: int, arg4: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.Conversion.intToHex(int,int,java.lang.String,int,int)"""
        return str.__wrap(__Conversion.intToHex(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def shortArrayToLong(arg0: 'short', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.apache.commons.lang3.Conversion.shortArrayToLong(short[],int,long,int,int)"""
        return int.__wrap(__Conversion.shortArrayToLong(arg0, __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def byteArrayToShort(arg0: bytes, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static short org.apache.commons.lang3.Conversion.byteArrayToShort(byte[],int,short,int,int)"""
        return int.__wrap(__Conversion.byteArrayToShort(bytes, __int.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def hexToLong(arg0: str, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.apache.commons.lang3.Conversion.hexToLong(java.lang.String,int,long,int,int)"""
        return int.__wrap(__Conversion.hexToLong(arg0, __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def longToShortArray(arg0: int, arg1: int, arg2: 'short', arg3: int, arg4: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.Conversion.longToShortArray(long,int,short[],int,int)"""
        return List[int].__wrap(__Conversion.longToShortArray(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def shortToByteArray(arg0: int, arg1: int, arg2: bytes, arg3: int, arg4: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.Conversion.shortToByteArray(short,int,byte[],int,int)"""
        return List[int].__wrap(__Conversion.shortToByteArray(__short.valueOf(arg0), __int.valueOf(arg1), bytes, __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.Conversion()"""
        val = __Conversion()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def binaryToHexDigit(arg0: 'boolean') -> str:
        """public static char org.apache.commons.lang3.Conversion.binaryToHexDigit(boolean[])"""
        return str.__wrap(__Conversion.binaryToHexDigit(arg0))

    @staticmethod
    @overload
    def binaryToHexDigitMsb0_4bits(arg0: 'boolean', arg1: int) -> str:
        """public static char org.apache.commons.lang3.Conversion.binaryToHexDigitMsb0_4bits(boolean[],int)"""
        return str.__wrap(__Conversion.binaryToHexDigitMsb0_4bits(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def hexDigitMsb0ToInt(arg0: str) -> int:
        """public static int org.apache.commons.lang3.Conversion.hexDigitMsb0ToInt(char)"""
        return int.__wrap(__Conversion.hexDigitMsb0ToInt(__char.valueOf(arg0)))

    @staticmethod
    @overload
    def intToHexDigit(arg0: int) -> str:
        """public static char org.apache.commons.lang3.Conversion.intToHexDigit(int)"""
        return str.__wrap(__Conversion.intToHexDigit(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def longToIntArray(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.Conversion.longToIntArray(long,int,int[],int,int)"""
        return List[int].__wrap(__Conversion.longToIntArray(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def shortToBinary(arg0: int, arg1: int, arg2: 'boolean', arg3: int, arg4: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.Conversion.shortToBinary(short,int,boolean[],int,int)"""
        return List[bool].__wrap(__Conversion.shortToBinary(__short.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def binaryToShort(arg0: 'boolean', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static short org.apache.commons.lang3.Conversion.binaryToShort(boolean[],int,short,int,int)"""
        return int.__wrap(__Conversion.binaryToShort(arg0, __int.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryToHexDigitMsb0_4bits(arg0: 'boolean') -> str:
        """public static char org.apache.commons.lang3.Conversion.binaryToHexDigitMsb0_4bits(boolean[])"""
        return str.__wrap(__Conversion.binaryToHexDigitMsb0_4bits(arg0))

    @staticmethod
    @overload
    def byteArrayToUuid(arg0: bytes, arg1: int) -> 'UUID':
        """public static java.util.UUID org.apache.commons.lang3.Conversion.byteArrayToUuid(byte[],int)"""
        return UUID.__wrap(__Conversion.byteArrayToUuid(bytes, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def intToBinary(arg0: int, arg1: int, arg2: 'boolean', arg3: int, arg4: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.Conversion.intToBinary(int,int,boolean[],int,int)"""
        return List[bool].__wrap(__Conversion.intToBinary(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def byteToBinary(arg0: int, arg1: int, arg2: 'boolean', arg3: int, arg4: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.Conversion.byteToBinary(byte,int,boolean[],int,int)"""
        return List[bool].__wrap(__Conversion.byteToBinary(__byte.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def shortToHex(arg0: int, arg1: int, arg2: str, arg3: int, arg4: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.Conversion.shortToHex(short,int,java.lang.String,int,int)"""
        return str.__wrap(__Conversion.shortToHex(__short.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def longToBinary(arg0: int, arg1: int, arg2: 'boolean', arg3: int, arg4: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.Conversion.longToBinary(long,int,boolean[],int,int)"""
        return List[bool].__wrap(__Conversion.longToBinary(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryBeMsb0ToHexDigit(arg0: 'boolean') -> str:
        """public static char org.apache.commons.lang3.Conversion.binaryBeMsb0ToHexDigit(boolean[])"""
        return str.__wrap(__Conversion.binaryBeMsb0ToHexDigit(arg0))

    @staticmethod
    @overload
    def hexToShort(arg0: str, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static short org.apache.commons.lang3.Conversion.hexToShort(java.lang.String,int,short,int,int)"""
        return int.__wrap(__Conversion.hexToShort(arg0, __int.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryToByte(arg0: 'boolean', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static byte org.apache.commons.lang3.Conversion.binaryToByte(boolean[],int,byte,int,int)"""
        return int.__wrap(__Conversion.binaryToByte(arg0, __int.valueOf(arg1), __byte.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))) 
 
 
# CLASS: org.apache.commons.lang3.CharEncoding
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.CharEncoding as __CharEncoding
__CharEncoding = __CharEncoding
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
 
class CharEncoding():
    """org.apache.commons.lang3.CharEncoding"""
 
    @staticmethod
    def __wrap(java_value: __CharEncoding) -> 'CharEncoding':
        return CharEncoding(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharEncoding):
        """
        Dynamic initializer for CharEncoding.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.CharEncoding()"""
        val = __CharEncoding()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.CharEncoding()"""
        val = __CharEncoding()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @staticmethod
    @overload
    def isSupported(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharEncoding.isSupported(java.lang.String)"""
        return bool.__wrap(__CharEncoding.isSupported(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.StringUtils
import java.util.Locale as Locale
import java.util.function.Supplier as Supplier
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.charset.Charset as Charset
from builtins import type
import org.apache.commons.lang3.StringUtils as __StringUtils
__StringUtils = __StringUtils
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import java.lang.Iterable as Iterable
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
 
class StringUtils():
    """org.apache.commons.lang3.StringUtils"""
 
    @staticmethod
    def __wrap(java_value: __StringUtils) -> 'StringUtils':
        return StringUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringUtils):
        """
        Dynamic initializer for StringUtils.
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
    def isAnyEmpty(*arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAnyEmpty(java.lang.CharSequence...)"""
        return bool.__wrap(__StringUtils.isAnyEmpty(arg0))

    @staticmethod
    @overload
    def substringBefore(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringBefore(java.lang.String,int)"""
        return str.__wrap(__StringUtils.substringBefore(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def removeEnd(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeEnd(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.removeEnd(arg0, arg1))

    @staticmethod
    @overload
    def split(arg0: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.split(java.lang.String)"""
        return List[str].__wrap(__StringUtils.split(arg0))

    @staticmethod
    @overload
    def firstNonEmpty(*arg0: 'CharSequence') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.StringUtils.firstNonEmpty(T...)"""
        return CharSequence.__wrap(__StringUtils.firstNonEmpty(arg0))

    @staticmethod
    @overload
    def substring(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substring(java.lang.String,int)"""
        return str.__wrap(__StringUtils.substring(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def strip(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.strip(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.strip(arg0, arg1))

    @staticmethod
    @overload
    def joinWith(arg0: str, *arg1: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.joinWith(java.lang.String,java.lang.Object...)"""
        return str.__wrap(__StringUtils.joinWith(arg0, arg1))

    @staticmethod
    @overload
    def defaultString(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.defaultString(java.lang.String)"""
        return str.__wrap(__StringUtils.defaultString(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.StringUtils()"""
        val = __StringUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def defaultIfEmpty(arg0: 'CharSequence', arg1: 'CharSequence') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.StringUtils.defaultIfEmpty(T,T)"""
        return CharSequence.__wrap(__StringUtils.defaultIfEmpty(arg0, arg1))

    @staticmethod
    @overload
    def join(arg0: 'long', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(long[],char)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def contains(arg0: 'CharSequence', arg1: int) -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.contains(java.lang.CharSequence,int)"""
        return bool.__wrap(__StringUtils.contains(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def removeStart(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeStart(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.removeStart(arg0, arg1))

    @staticmethod
    @overload
    def splitByCharacterType(arg0: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitByCharacterType(java.lang.String)"""
        return List[str].__wrap(__StringUtils.splitByCharacterType(arg0))

    @staticmethod
    @overload
    def mid(arg0: str, arg1: int, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.mid(java.lang.String,int,int)"""
        return str.__wrap(__StringUtils.mid(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def join(arg0: 'short', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(short[],char)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def replaceChars(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceChars(java.lang.String,char,char)"""
        return str.__wrap(__StringUtils.replaceChars(arg0, __char.valueOf(arg1), __char.valueOf(arg2)))

    @staticmethod
    @overload
    def abbreviate(arg0: str, arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.abbreviate(java.lang.String,java.lang.String,int,int)"""
        return str.__wrap(__StringUtils.abbreviate(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def normalizeSpace(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.normalizeSpace(java.lang.String)"""
        return str.__wrap(__StringUtils.normalizeSpace(arg0))

    @staticmethod
    @overload
    def isAllEmpty(*arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAllEmpty(java.lang.CharSequence...)"""
        return bool.__wrap(__StringUtils.isAllEmpty(arg0))

    @staticmethod
    @overload
    def appendIfMissing(arg0: str, arg1: 'CharSequence', *arg2: 'CharSequence') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.appendIfMissing(java.lang.String,java.lang.CharSequence,java.lang.CharSequence...)"""
        return str.__wrap(__StringUtils.appendIfMissing(arg0, arg1, arg2))

    @staticmethod
    @overload
    def lastIndexOfAny(arg0: 'CharSequence', *arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOfAny(java.lang.CharSequence,java.lang.CharSequence...)"""
        return int.__wrap(__StringUtils.lastIndexOfAny(arg0, arg1))

    @staticmethod
    @overload
    def isNoneEmpty(*arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isNoneEmpty(java.lang.CharSequence...)"""
        return bool.__wrap(__StringUtils.isNoneEmpty(arg0))

    @staticmethod
    @overload
    def leftPad(arg0: str, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.leftPad(java.lang.String,int,char)"""
        return str.__wrap(__StringUtils.leftPad(arg0, __int.valueOf(arg1), __char.valueOf(arg2)))

    @staticmethod
    @overload
    def isAlphanumeric(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAlphanumeric(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isAlphanumeric(arg0))

    @staticmethod
    @overload
    def replaceOnce(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceOnce(java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.replaceOnce(arg0, arg1, arg2))

    @staticmethod
    @overload
    def swapCase(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.swapCase(java.lang.String)"""
        return str.__wrap(__StringUtils.swapCase(arg0))

    @staticmethod
    @overload
    def splitByCharacterTypeCamelCase(arg0: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitByCharacterTypeCamelCase(java.lang.String)"""
        return List[str].__wrap(__StringUtils.splitByCharacterTypeCamelCase(arg0))

    @staticmethod
    @overload
    def split(arg0: str, arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.split(java.lang.String,char)"""
        return List[str].__wrap(__StringUtils.split(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def lastIndexOfIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOfIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return int.__wrap(__StringUtils.lastIndexOfIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def substringAfterLast(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringAfterLast(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.substringAfterLast(arg0, arg1))

    @staticmethod
    @overload
    def endsWithAny(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.endsWithAny(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool.__wrap(__StringUtils.endsWithAny(arg0, arg1))

    @staticmethod
    @overload
    def isAllBlank(*arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAllBlank(java.lang.CharSequence...)"""
        return bool.__wrap(__StringUtils.isAllBlank(arg0))

    @staticmethod
    @overload
    def reverse(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.reverse(java.lang.String)"""
        return str.__wrap(__StringUtils.reverse(arg0))

    @staticmethod
    @overload
    def unwrap(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.unwrap(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.unwrap(arg0, arg1))

    @staticmethod
    @overload
    def splitByWholeSeparatorPreserveAllTokens(arg0: str, arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitByWholeSeparatorPreserveAllTokens(java.lang.String,java.lang.String)"""
        return List[str].__wrap(__StringUtils.splitByWholeSeparatorPreserveAllTokens(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getBytes(arg0: str, arg1: str) -> List[int]:
        """public static byte[] org.apache.commons.lang3.StringUtils.getBytes(java.lang.String,java.lang.String) throws java.io.UnsupportedEncodingException"""
        return List[int].__wrap(__StringUtils.getBytes(arg0, arg1))

    @staticmethod
    @overload
    def indexOfAny(arg0: 'CharSequence', arg1: str) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfAny(java.lang.CharSequence,java.lang.String)"""
        return int.__wrap(__StringUtils.indexOfAny(arg0, arg1))

    @staticmethod
    @overload
    def leftPad(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.leftPad(java.lang.String,int)"""
        return str.__wrap(__StringUtils.leftPad(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def wrapIfMissing(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.wrapIfMissing(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.wrapIfMissing(arg0, arg1))

    @staticmethod
    @overload
    def center(arg0: str, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.center(java.lang.String,int,java.lang.String)"""
        return str.__wrap(__StringUtils.center(arg0, __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def indexOfIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return int.__wrap(__StringUtils.indexOfIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def split(arg0: str, arg1: str, arg2: int) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.split(java.lang.String,java.lang.String,int)"""
        return List[str].__wrap(__StringUtils.split(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def substring(arg0: str, arg1: int, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substring(java.lang.String,int,int)"""
        return str.__wrap(__StringUtils.substring(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def indexOfDifference(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfDifference(java.lang.CharSequence,java.lang.CharSequence)"""
        return int.__wrap(__StringUtils.indexOfDifference(arg0, arg1))

    @staticmethod
    @overload
    def join(arg0: 'Object', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.lang.Object[],char)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def replaceEach(arg0: str, arg1: 'String', arg2: 'String') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceEach(java.lang.String,java.lang.String[],java.lang.String[])"""
        return str.__wrap(__StringUtils.replaceEach(arg0, arg1, arg2))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isNotEmpty(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def stripEnd(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.stripEnd(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.stripEnd(arg0, arg1))

    @staticmethod
    @overload
    def getLevenshteinDistance(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.getLevenshteinDistance(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int.__wrap(__StringUtils.getLevenshteinDistance(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def isAllLowerCase(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAllLowerCase(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isAllLowerCase(arg0))

    @staticmethod
    @overload
    def endsWithIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.endsWithIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.endsWithIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def stripToNull(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.stripToNull(java.lang.String)"""
        return str.__wrap(__StringUtils.stripToNull(arg0))

    @staticmethod
    @overload
    def splitPreserveAllTokens(arg0: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitPreserveAllTokens(java.lang.String)"""
        return List[str].__wrap(__StringUtils.splitPreserveAllTokens(arg0))

    @staticmethod
    @overload
    def join(arg0: 'short', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(short[],char,int,int)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def prependIfMissing(arg0: str, arg1: 'CharSequence', *arg2: 'CharSequence') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.prependIfMissing(java.lang.String,java.lang.CharSequence,java.lang.CharSequence...)"""
        return str.__wrap(__StringUtils.prependIfMissing(arg0, arg1, arg2))

    @staticmethod
    @overload
    def isAnyBlank(*arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAnyBlank(java.lang.CharSequence...)"""
        return bool.__wrap(__StringUtils.isAnyBlank(arg0))

    @staticmethod
    @overload
    def reverseDelimited(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.reverseDelimited(java.lang.String,char)"""
        return str.__wrap(__StringUtils.reverseDelimited(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def replacePattern(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replacePattern(java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.replacePattern(arg0, arg1, arg2))

    @staticmethod
    @overload
    def trim(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.trim(java.lang.String)"""
        return str.__wrap(__StringUtils.trim(arg0))

    @staticmethod
    @overload
    def getLevenshteinDistance(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.getLevenshteinDistance(java.lang.CharSequence,java.lang.CharSequence)"""
        return int.__wrap(__StringUtils.getLevenshteinDistance(arg0, arg1))

    @staticmethod
    @overload
    def rotate(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.rotate(java.lang.String,int)"""
        return str.__wrap(__StringUtils.rotate(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'CharSequence', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOf(java.lang.CharSequence,int,int)"""
        return int.__wrap(__StringUtils.lastIndexOf(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def replace(arg0: str, arg1: str, arg2: str, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replace(java.lang.String,java.lang.String,java.lang.String,int)"""
        return str.__wrap(__StringUtils.replace(arg0, arg1, arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def containsNone(arg0: 'CharSequence', arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsNone(java.lang.CharSequence,java.lang.String)"""
        return bool.__wrap(__StringUtils.containsNone(arg0, arg1))

    @staticmethod
    @overload
    def wrapIfMissing(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.wrapIfMissing(java.lang.String,char)"""
        return str.__wrap(__StringUtils.wrapIfMissing(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def split(arg0: str, arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.split(java.lang.String,java.lang.String)"""
        return List[str].__wrap(__StringUtils.split(arg0, arg1))

    @staticmethod
    @overload
    def substringAfterLast(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringAfterLast(java.lang.String,int)"""
        return str.__wrap(__StringUtils.substringAfterLast(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def length(arg0: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.length(java.lang.CharSequence)"""
        return int.__wrap(__StringUtils.length(arg0))

    @staticmethod
    @overload
    def rightPad(arg0: str, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.rightPad(java.lang.String,int,char)"""
        return str.__wrap(__StringUtils.rightPad(arg0, __int.valueOf(arg1), __char.valueOf(arg2)))

    @staticmethod
    @overload
    def indexOf(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOf(java.lang.CharSequence,java.lang.CharSequence)"""
        return int.__wrap(__StringUtils.indexOf(arg0, arg1))

    @staticmethod
    @overload
    def indexOf(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOf(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int.__wrap(__StringUtils.indexOf(arg0, arg1, __int.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def containsOnly(arg0: 'CharSequence', arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsOnly(java.lang.CharSequence,java.lang.String)"""
        return bool.__wrap(__StringUtils.containsOnly(arg0, arg1))

    @staticmethod
    @overload
    def splitPreserveAllTokens(arg0: str, arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitPreserveAllTokens(java.lang.String,java.lang.String)"""
        return List[str].__wrap(__StringUtils.splitPreserveAllTokens(arg0, arg1))

    @staticmethod
    @overload
    def getIfBlank(arg0: 'CharSequence', arg1: 'Supplier') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.StringUtils.getIfBlank(T,java.util.function.Supplier<T>)"""
        return CharSequence.__wrap(__StringUtils.getIfBlank(arg0, arg1))

    @staticmethod
    @overload
    def stripStart(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.stripStart(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.stripStart(arg0, arg1))

    @staticmethod
    @overload
    def abbreviateMiddle(arg0: str, arg1: str, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.abbreviateMiddle(java.lang.String,java.lang.String,int)"""
        return str.__wrap(__StringUtils.abbreviateMiddle(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def equalsAny(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.equalsAny(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool.__wrap(__StringUtils.equalsAny(arg0, arg1))

    @staticmethod
    @overload
    def join(arg0: bytes, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(byte[],char)"""
        return str.__wrap(__StringUtils.join(bytes, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def replaceFirst(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceFirst(java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.replaceFirst(arg0, arg1, arg2))

    @staticmethod
    @overload
    def isNotBlank(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isNotBlank(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isNotBlank(arg0))

    @staticmethod
    @overload
    def removeStartIgnoreCase(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeStartIgnoreCase(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.removeStartIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def join(arg0: 'boolean', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(boolean[],char)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def wrap(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.wrap(java.lang.String,char)"""
        return str.__wrap(__StringUtils.wrap(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def splitByWholeSeparator(arg0: str, arg1: str, arg2: int) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitByWholeSeparator(java.lang.String,java.lang.String,int)"""
        return List[str].__wrap(__StringUtils.splitByWholeSeparator(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def getJaroWinklerDistance(arg0: 'CharSequence', arg1: 'CharSequence') -> float:
        """public static double org.apache.commons.lang3.StringUtils.getJaroWinklerDistance(java.lang.CharSequence,java.lang.CharSequence)"""
        return float.__wrap(__StringUtils.getJaroWinklerDistance(arg0, arg1))

    @staticmethod
    @overload
    def startsWithIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.startsWithIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.startsWithIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def equalsAnyIgnoreCase(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.equalsAnyIgnoreCase(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool.__wrap(__StringUtils.equalsAnyIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def indexOfAnyBut(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfAnyBut(java.lang.CharSequence,java.lang.CharSequence)"""
        return int.__wrap(__StringUtils.indexOfAnyBut(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'char') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.valueOf(char[])"""
        return str.__wrap(__StringUtils.valueOf(arg0))

    @staticmethod
    @overload
    def removeStart(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeStart(java.lang.String,char)"""
        return str.__wrap(__StringUtils.removeStart(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def truncate(arg0: str, arg1: int, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.truncate(java.lang.String,int,int)"""
        return str.__wrap(__StringUtils.truncate(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def trimToNull(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.trimToNull(java.lang.String)"""
        return str.__wrap(__StringUtils.trimToNull(arg0))

    @staticmethod
    @overload
    def capitalize(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.capitalize(java.lang.String)"""
        return str.__wrap(__StringUtils.capitalize(arg0))

    @staticmethod
    @overload
    def substringBeforeLast(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringBeforeLast(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.substringBeforeLast(arg0, arg1))

    @staticmethod
    @overload
    def leftPad(arg0: str, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.leftPad(java.lang.String,int,java.lang.String)"""
        return str.__wrap(__StringUtils.leftPad(arg0, __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def substringAfter(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringAfter(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.substringAfter(arg0, arg1))

    @staticmethod
    @overload
    def join(arg0: 'char', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(char[],char)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def replaceOnceIgnoreCase(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceOnceIgnoreCase(java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.replaceOnceIgnoreCase(arg0, arg1, arg2))

    @staticmethod
    @overload
    def countMatches(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.countMatches(java.lang.CharSequence,java.lang.CharSequence)"""
        return int.__wrap(__StringUtils.countMatches(arg0, arg1))

    @staticmethod
    @overload
    def firstNonBlank(*arg0: 'CharSequence') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.StringUtils.firstNonBlank(T...)"""
        return CharSequence.__wrap(__StringUtils.firstNonBlank(arg0))

    @staticmethod
    @overload
    def equals(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.equals(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.equals(arg0, arg1))

    @staticmethod
    @overload
    def getIfEmpty(arg0: 'CharSequence', arg1: 'Supplier') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.StringUtils.getIfEmpty(T,java.util.function.Supplier<T>)"""
        return CharSequence.__wrap(__StringUtils.getIfEmpty(arg0, arg1))

    @staticmethod
    @overload
    def toEncodedString(arg0: bytes, arg1: 'Charset') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.toEncodedString(byte[],java.nio.charset.Charset)"""
        return str.__wrap(__StringUtils.toEncodedString(bytes, arg1))

    @staticmethod
    @overload
    def defaultIfBlank(arg0: 'CharSequence', arg1: 'CharSequence') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.StringUtils.defaultIfBlank(T,T)"""
        return CharSequence.__wrap(__StringUtils.defaultIfBlank(arg0, arg1))

    @staticmethod
    @overload
    def join(*arg0: object) -> str:
        """public static <T> java.lang.String org.apache.commons.lang3.StringUtils.join(T...)"""
        return str.__wrap(__StringUtils.join(arg0))

    @staticmethod
    @overload
    def indexOfIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfIgnoreCase(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int.__wrap(__StringUtils.indexOfIgnoreCase(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def abbreviate(arg0: str, arg1: int, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.abbreviate(java.lang.String,int,int)"""
        return str.__wrap(__StringUtils.abbreviate(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeEndIgnoreCase(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeEndIgnoreCase(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.removeEndIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def center(arg0: str, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.center(java.lang.String,int,char)"""
        return str.__wrap(__StringUtils.center(arg0, __int.valueOf(arg1), __char.valueOf(arg2)))

    @staticmethod
    @overload
    def difference(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.difference(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.difference(arg0, arg1))

    @staticmethod
    @overload
    def chomp(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.chomp(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.chomp(arg0, arg1))

    @staticmethod
    @overload
    def isBlank(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isBlank(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isBlank(arg0))

    @staticmethod
    @overload
    def join(arg0: 'Object', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.lang.Object[],char,int,int)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def containsAny(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsAny(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.containsAny(arg0, arg1))

    @staticmethod
    @overload
    def repeat(arg0: str, arg1: str, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.repeat(java.lang.String,java.lang.String,int)"""
        return str.__wrap(__StringUtils.repeat(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def upperCase(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.upperCase(java.lang.String)"""
        return str.__wrap(__StringUtils.upperCase(arg0))

    @staticmethod
    @overload
    def remove(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.remove(java.lang.String,char)"""
        return str.__wrap(__StringUtils.remove(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def join(arg0: 'Iterator', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.util.Iterator<?>,char)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def endsWith(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.endsWith(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.endsWith(arg0, arg1))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOf(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int.__wrap(__StringUtils.lastIndexOf(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def join(arg0: 'boolean', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(boolean[],char,int,int)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def left(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.left(java.lang.String,int)"""
        return str.__wrap(__StringUtils.left(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def isEmpty(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isEmpty(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOf(java.lang.CharSequence,java.lang.CharSequence)"""
        return int.__wrap(__StringUtils.lastIndexOf(arg0, arg1))

    @staticmethod
    @overload
    def startsWithAny(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.startsWithAny(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool.__wrap(__StringUtils.startsWithAny(arg0, arg1))

    @staticmethod
    @overload
    def indexOf(arg0: 'CharSequence', arg1: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOf(java.lang.CharSequence,int)"""
        return int.__wrap(__StringUtils.indexOf(arg0, __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def substringBefore(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringBefore(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.substringBefore(arg0, arg1))

    @staticmethod
    @overload
    def lastOrdinalIndexOf(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastOrdinalIndexOf(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int.__wrap(__StringUtils.lastOrdinalIndexOf(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def isAsciiPrintable(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAsciiPrintable(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isAsciiPrintable(arg0))

    @staticmethod
    @overload
    def containsAnyIgnoreCase(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsAnyIgnoreCase(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool.__wrap(__StringUtils.containsAnyIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def containsAny(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsAny(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool.__wrap(__StringUtils.containsAny(arg0, arg1))

    @staticmethod
    @overload
    def join(arg0: 'Iterator', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.util.Iterator<?>,java.lang.String)"""
        return str.__wrap(__StringUtils.join(arg0, arg1))

    @staticmethod
    @overload
    def join(arg0: 'long', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(long[],char,int,int)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def indexOfDifference(*arg0: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfDifference(java.lang.CharSequence...)"""
        return int.__wrap(__StringUtils.indexOfDifference(arg0))

    @staticmethod
    @overload
    def compareIgnoreCase(arg0: str, arg1: str) -> int:
        """public static int org.apache.commons.lang3.StringUtils.compareIgnoreCase(java.lang.String,java.lang.String)"""
        return int.__wrap(__StringUtils.compareIgnoreCase(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toRootUpperCase(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.toRootUpperCase(java.lang.String)"""
        return str.__wrap(__StringUtils.toRootUpperCase(arg0))

    @staticmethod
    @overload
    def join(arg0: 'Iterable', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.lang.Iterable<?>,java.lang.String)"""
        return str.__wrap(__StringUtils.join(arg0, arg1))

    @staticmethod
    @overload
    def contains(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.contains(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.contains(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def isNumericSpace(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isNumericSpace(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isNumericSpace(arg0))

    @staticmethod
    @overload
    def stripToEmpty(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.stripToEmpty(java.lang.String)"""
        return str.__wrap(__StringUtils.stripToEmpty(arg0))

    @staticmethod
    @overload
    def containsIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.containsIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def trimToEmpty(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.trimToEmpty(java.lang.String)"""
        return str.__wrap(__StringUtils.trimToEmpty(arg0))

    @staticmethod
    @overload
    def removeAll(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeAll(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def indexOf(arg0: 'CharSequence', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOf(java.lang.CharSequence,int,int)"""
        return int.__wrap(__StringUtils.indexOf(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def substringBetween(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringBetween(java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.substringBetween(arg0, arg1, arg2))

    @staticmethod
    @overload
    def isWhitespace(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isWhitespace(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isWhitespace(arg0))

    @staticmethod
    @overload
    def wrap(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.wrap(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.wrap(arg0, arg1))

    @staticmethod
    @overload
    def substringsBetween(arg0: str, arg1: str, arg2: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.substringsBetween(java.lang.String,java.lang.String,java.lang.String)"""
        return List[str].__wrap(__StringUtils.substringsBetween(arg0, arg1, arg2))

    @staticmethod
    @overload
    def center(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.center(java.lang.String,int)"""
        return str.__wrap(__StringUtils.center(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOfAnyBut(arg0: 'CharSequence', *arg1: str) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfAnyBut(java.lang.CharSequence,char...)"""
        return int.__wrap(__StringUtils.indexOfAnyBut(arg0, arg1))

    @staticmethod
    @overload
    def getDigits(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.getDigits(java.lang.String)"""
        return str.__wrap(__StringUtils.getDigits(arg0))

    @staticmethod
    @overload
    def join(arg0: 'List', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.util.List<?>,java.lang.String,int,int)"""
        return str.__wrap(__StringUtils.join(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def join(arg0: 'float', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(float[],char)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def upperCase(arg0: str, arg1: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.upperCase(java.lang.String,java.util.Locale)"""
        return str.__wrap(__StringUtils.upperCase(arg0, arg1))

    @staticmethod
    @overload
    def prependIfMissingIgnoreCase(arg0: str, arg1: 'CharSequence', *arg2: 'CharSequence') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.prependIfMissingIgnoreCase(java.lang.String,java.lang.CharSequence,java.lang.CharSequence...)"""
        return str.__wrap(__StringUtils.prependIfMissingIgnoreCase(arg0, arg1, arg2))

    @staticmethod
    @overload
    def replaceIgnoreCase(arg0: str, arg1: str, arg2: str, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceIgnoreCase(java.lang.String,java.lang.String,java.lang.String,int)"""
        return str.__wrap(__StringUtils.replaceIgnoreCase(arg0, arg1, arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def removeFirst(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeFirst(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.removeFirst(arg0, arg1))

    @staticmethod
    @overload
    def defaultString(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.defaultString(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.defaultString(arg0, arg1))

    @staticmethod
    @overload
    def compareIgnoreCase(arg0: str, arg1: str, arg2: bool) -> int:
        """public static int org.apache.commons.lang3.StringUtils.compareIgnoreCase(java.lang.String,java.lang.String,boolean)"""
        return int.__wrap(__StringUtils.compareIgnoreCase(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def join(arg0: 'int', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(int[],char,int,int)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def join(arg0: bytes, arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(byte[],char,int,int)"""
        return str.__wrap(__StringUtils.join(bytes, __char.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def join(arg0: 'float', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(float[],char,int,int)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def abbreviate(arg0: str, arg1: str, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.abbreviate(java.lang.String,java.lang.String,int)"""
        return str.__wrap(__StringUtils.abbreviate(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def appendIfMissingIgnoreCase(arg0: str, arg1: 'CharSequence', *arg2: 'CharSequence') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.appendIfMissingIgnoreCase(java.lang.String,java.lang.CharSequence,java.lang.CharSequence...)"""
        return str.__wrap(__StringUtils.appendIfMissingIgnoreCase(arg0, arg1, arg2))

    @staticmethod
    @overload
    def isAlphanumericSpace(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAlphanumericSpace(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isAlphanumericSpace(arg0))

    @staticmethod
    @overload
    def isAlpha(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAlpha(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isAlpha(arg0))

    @staticmethod
    @overload
    def truncate(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.truncate(java.lang.String,int)"""
        return str.__wrap(__StringUtils.truncate(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def getFuzzyDistance(arg0: 'CharSequence', arg1: 'CharSequence', arg2: 'Locale') -> int:
        """public static int org.apache.commons.lang3.StringUtils.getFuzzyDistance(java.lang.CharSequence,java.lang.CharSequence,java.util.Locale)"""
        return int.__wrap(__StringUtils.getFuzzyDistance(arg0, arg1, arg2))

    @staticmethod
    @overload
    def deleteWhitespace(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.deleteWhitespace(java.lang.String)"""
        return str.__wrap(__StringUtils.deleteWhitespace(arg0))

    @staticmethod
    @overload
    def overlay(arg0: str, arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.overlay(java.lang.String,java.lang.String,int,int)"""
        return str.__wrap(__StringUtils.overlay(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def rightPad(arg0: str, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.rightPad(java.lang.String,int,java.lang.String)"""
        return str.__wrap(__StringUtils.rightPad(arg0, __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def lowerCase(arg0: str, arg1: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.lowerCase(java.lang.String,java.util.Locale)"""
        return str.__wrap(__StringUtils.lowerCase(arg0, arg1))

    @staticmethod
    @overload
    def chop(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.chop(java.lang.String)"""
        return str.__wrap(__StringUtils.chop(arg0))

    @staticmethod
    @overload
    def replaceEachRepeatedly(arg0: str, arg1: 'String', arg2: 'String') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceEachRepeatedly(java.lang.String,java.lang.String[],java.lang.String[])"""
        return str.__wrap(__StringUtils.replaceEachRepeatedly(arg0, arg1, arg2))

    @staticmethod
    @overload
    def remove(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.remove(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.remove(arg0, arg1))

    @staticmethod
    @overload
    def containsAny(arg0: 'CharSequence', *arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsAny(java.lang.CharSequence,char...)"""
        return bool.__wrap(__StringUtils.containsAny(arg0, arg1))

    @staticmethod
    @overload
    def replace(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replace(java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.replace(arg0, arg1, arg2))

    @staticmethod
    @overload
    def countMatches(arg0: 'CharSequence', arg1: str) -> int:
        """public static int org.apache.commons.lang3.StringUtils.countMatches(java.lang.CharSequence,char)"""
        return int.__wrap(__StringUtils.countMatches(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def containsWhitespace(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsWhitespace(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.containsWhitespace(arg0))

    @staticmethod
    @overload
    def repeat(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.repeat(char,int)"""
        return str.__wrap(__StringUtils.repeat(__char.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def repeat(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.repeat(java.lang.String,int)"""
        return str.__wrap(__StringUtils.repeat(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def isMixedCase(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isMixedCase(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isMixedCase(arg0))

    @staticmethod
    @overload
    def strip(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.strip(java.lang.String)"""
        return str.__wrap(__StringUtils.strip(arg0))

    @staticmethod
    @overload
    def startsWith(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.startsWith(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.startsWith(arg0, arg1))

    @staticmethod
    @overload
    def lastIndexOfIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOfIgnoreCase(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int.__wrap(__StringUtils.lastIndexOfIgnoreCase(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def join(arg0: 'double', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(double[],char,int,int)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def toString(arg0: bytes, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.toString(byte[],java.lang.String) throws java.io.UnsupportedEncodingException"""
        return str.__wrap(__StringUtils.toString(bytes, arg1))

    @staticmethod
    @overload
    def toRootLowerCase(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.toRootLowerCase(java.lang.String)"""
        return str.__wrap(__StringUtils.toRootLowerCase(arg0))

    @staticmethod
    @overload
    def isAllUpperCase(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAllUpperCase(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isAllUpperCase(arg0))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'CharSequence', arg1: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOf(java.lang.CharSequence,int)"""
        return int.__wrap(__StringUtils.lastIndexOf(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def join(arg0: 'char', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(char[],char,int,int)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def join(arg0: 'int', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(int[],char)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def getCommonPrefix(*arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.getCommonPrefix(java.lang.String...)"""
        return str.__wrap(__StringUtils.getCommonPrefix(arg0))

    @staticmethod
    @overload
    def substringBetween(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringBetween(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.substringBetween(arg0, arg1))

    @staticmethod
    @overload
    def removeIgnoreCase(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeIgnoreCase(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.removeIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def right(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.right(java.lang.String,int)"""
        return str.__wrap(__StringUtils.right(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def compare(arg0: str, arg1: str, arg2: bool) -> int:
        """public static int org.apache.commons.lang3.StringUtils.compare(java.lang.String,java.lang.String,boolean)"""
        return int.__wrap(__StringUtils.compare(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def replaceAll(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceAll(java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.replaceAll(arg0, arg1, arg2))

    @staticmethod
    @overload
    def unwrap(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.unwrap(java.lang.String,char)"""
        return str.__wrap(__StringUtils.unwrap(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def substringAfter(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringAfter(java.lang.String,int)"""
        return str.__wrap(__StringUtils.substringAfter(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ordinalIndexOf(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.ordinalIndexOf(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int.__wrap(__StringUtils.ordinalIndexOf(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def uncapitalize(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.uncapitalize(java.lang.String)"""
        return str.__wrap(__StringUtils.uncapitalize(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.StringUtils()"""
        val = __StringUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def containsNone(arg0: 'CharSequence', *arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsNone(java.lang.CharSequence,char...)"""
        return bool.__wrap(__StringUtils.containsNone(arg0, arg1))

    @staticmethod
    @overload
    def stripAccents(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.stripAccents(java.lang.String)"""
        return str.__wrap(__StringUtils.stripAccents(arg0))

    @staticmethod
    @overload
    def equalsIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.equalsIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.equalsIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def splitPreserveAllTokens(arg0: str, arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitPreserveAllTokens(java.lang.String,char)"""
        return List[str].__wrap(__StringUtils.splitPreserveAllTokens(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def replaceChars(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceChars(java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.replaceChars(arg0, arg1, arg2))

    @staticmethod
    @overload
    def splitPreserveAllTokens(arg0: str, arg1: str, arg2: int) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitPreserveAllTokens(java.lang.String,java.lang.String,int)"""
        return List[str].__wrap(__StringUtils.splitPreserveAllTokens(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def join(arg0: 'Iterable', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.lang.Iterable<?>,char)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def join(arg0: 'Object', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.lang.Object[],java.lang.String)"""
        return str.__wrap(__StringUtils.join(arg0, arg1))

    @staticmethod
    @overload
    def lowerCase(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.lowerCase(java.lang.String)"""
        return str.__wrap(__StringUtils.lowerCase(arg0))

    @staticmethod
    @overload
    def removePattern(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removePattern(java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.removePattern(arg0, arg1))

    @staticmethod
    @overload
    def splitByWholeSeparator(arg0: str, arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitByWholeSeparator(java.lang.String,java.lang.String)"""
        return List[str].__wrap(__StringUtils.splitByWholeSeparator(arg0, arg1))

    @staticmethod
    @overload
    def isAlphaSpace(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAlphaSpace(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isAlphaSpace(arg0))

    @staticmethod
    @overload
    def rightPad(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.rightPad(java.lang.String,int)"""
        return str.__wrap(__StringUtils.rightPad(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def chomp(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.chomp(java.lang.String)"""
        return str.__wrap(__StringUtils.chomp(arg0))

    @staticmethod
    @overload
    def replaceIgnoreCase(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceIgnoreCase(java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__StringUtils.replaceIgnoreCase(arg0, arg1, arg2))

    @staticmethod
    @overload
    def isNumeric(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isNumeric(java.lang.CharSequence)"""
        return bool.__wrap(__StringUtils.isNumeric(arg0))

    @staticmethod
    @overload
    def abbreviate(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.abbreviate(java.lang.String,int)"""
        return str.__wrap(__StringUtils.abbreviate(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def containsOnly(arg0: 'CharSequence', *arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsOnly(java.lang.CharSequence,char...)"""
        return bool.__wrap(__StringUtils.containsOnly(arg0, arg1))

    @staticmethod
    @overload
    def indexOfAny(arg0: 'CharSequence', *arg1: str) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfAny(java.lang.CharSequence,char...)"""
        return int.__wrap(__StringUtils.indexOfAny(arg0, arg1))

    @staticmethod
    @overload
    def stripAll(arg0: 'String', arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.stripAll(java.lang.String[],java.lang.String)"""
        return List[str].__wrap(__StringUtils.stripAll(arg0, arg1))

    @staticmethod
    @overload
    def join(arg0: 'Object', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.lang.Object[],java.lang.String,int,int)"""
        return str.__wrap(__StringUtils.join(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def splitByWholeSeparatorPreserveAllTokens(arg0: str, arg1: str, arg2: int) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitByWholeSeparatorPreserveAllTokens(java.lang.String,java.lang.String,int)"""
        return List[str].__wrap(__StringUtils.splitByWholeSeparatorPreserveAllTokens(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def isNoneBlank(*arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isNoneBlank(java.lang.CharSequence...)"""
        return bool.__wrap(__StringUtils.isNoneBlank(arg0))

    @staticmethod
    @overload
    def getBytes(arg0: str, arg1: 'Charset') -> List[int]:
        """public static byte[] org.apache.commons.lang3.StringUtils.getBytes(java.lang.String,java.nio.charset.Charset)"""
        return List[int].__wrap(__StringUtils.getBytes(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def join(arg0: 'List', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.util.List<?>,char,int,int)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def toCodePoints(arg0: 'CharSequence') -> List[int]:
        """public static int[] org.apache.commons.lang3.StringUtils.toCodePoints(java.lang.CharSequence)"""
        return List[int].__wrap(__StringUtils.toCodePoints(arg0))

    @staticmethod
    @overload
    def stripAll(*arg0: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.stripAll(java.lang.String...)"""
        return List[str].__wrap(__StringUtils.stripAll(arg0))

    @staticmethod
    @overload
    def indexOfAny(arg0: 'CharSequence', *arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfAny(java.lang.CharSequence,java.lang.CharSequence...)"""
        return int.__wrap(__StringUtils.indexOfAny(arg0, arg1))

    @staticmethod
    @overload
    def compare(arg0: str, arg1: str) -> int:
        """public static int org.apache.commons.lang3.StringUtils.compare(java.lang.String,java.lang.String)"""
        return int.__wrap(__StringUtils.compare(arg0, arg1))

    @staticmethod
    @overload
    def join(arg0: 'double', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(double[],char)"""
        return str.__wrap(__StringUtils.join(arg0, __char.valueOf(arg1))) 
 
 
# CLASS: org.apache.commons.lang3.ClassLoaderUtils
from builtins import str
from pyquantum_helper import override
import java.net.URLClassLoader as URLClassLoader
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.ClassLoaderUtils as __ClassLoaderUtils
__ClassLoaderUtils = __ClassLoaderUtils
from typing import List
import java.net.URL as URL
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.net.URL as __URL
__URL = __URL
import java.lang.ClassLoader as ClassLoader
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClassLoaderUtils():
    """org.apache.commons.lang3.ClassLoaderUtils"""
 
    @staticmethod
    def __wrap(java_value: __ClassLoaderUtils) -> 'ClassLoaderUtils':
        return ClassLoaderUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClassLoaderUtils):
        """
        Dynamic initializer for ClassLoaderUtils.
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
    def getSystemURLs() -> List['URL']:
        """public static java.net.URL[] org.apache.commons.lang3.ClassLoaderUtils.getSystemURLs()"""
        return List[URL].__wrap(__ClassLoaderUtils.getSystemURLs())

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

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ClassLoaderUtils()"""
        val = __ClassLoaderUtils()
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

    @staticmethod
    @overload
    def toString(arg0: 'URLClassLoader') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassLoaderUtils.toString(java.net.URLClassLoader)"""
        return str.__wrap(__ClassLoaderUtils.toString(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ClassLoaderUtils()"""
        val = __ClassLoaderUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def toString(arg0: 'ClassLoader') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassLoaderUtils.toString(java.lang.ClassLoader)"""
        return str.__wrap(__ClassLoaderUtils.toString(arg0))

    @staticmethod
    @overload
    def getThreadURLs() -> List['URL']:
        """public static java.net.URL[] org.apache.commons.lang3.ClassLoaderUtils.getThreadURLs()"""
        return List[URL].__wrap(__ClassLoaderUtils.getThreadURLs())

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
 
 
# CLASS: org.apache.commons.lang3.ThreadUtils$NamePredicate
import java.lang.Thread as Thread
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.ThreadGroup as ThreadGroup
import org.apache.commons.lang3.ThreadUtils as __ThreadUtils_NamePredicate
__NamePredicate = __ThreadUtils_NamePredicate.NamePredicate
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NamePredicate():
    """org.apache.commons.lang3.ThreadUtils.NamePredicate"""
 
    @staticmethod
    def __wrap(java_value: __NamePredicate) -> 'NamePredicate':
        return NamePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NamePredicate):
        """
        Dynamic initializer for NamePredicate.
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
    def test(self, arg0: 'ThreadGroup') -> bool:
        """public boolean org.apache.commons.lang3.ThreadUtils$NamePredicate.test(java.lang.ThreadGroup)"""
        return bool.__wrap(super(__NamePredicate, self).test(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.ThreadUtils$NamePredicate(java.lang.String)"""
        val = __NamePredicate(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def test(self, arg0: 'Thread') -> bool:
        """public boolean org.apache.commons.lang3.ThreadUtils$NamePredicate.test(java.lang.Thread)"""
        return bool.__wrap(super(__NamePredicate, self).test(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.ArrayUtils
import java.util.function.Supplier as Supplier
import java.lang.Integer as __Integer
__Integer = __Integer
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.lang.Long as Long
import java.lang.Double as __Double
__Double = __Double
import java.lang.Short as Short
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Boolean as __Boolean
__Boolean = __Boolean
import java.lang.Byte as __Byte
__Byte = __Byte
import java.lang.Short as __Short
__Short = __Short
import java.util.BitSet as BitSet
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
import java.lang.Double as __double
import java.lang.Character as Character
from builtins import bool
import java.lang.Boolean as Boolean
import java.util.BitSet as __BitSet
__BitSet = __BitSet
from builtins import str
import org.apache.commons.lang3.ArrayUtils as __ArrayUtils
__ArrayUtils = __ArrayUtils
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.function.IntFunction as IntFunction
from builtins import float
import java.lang.Float as Float
from builtins import object
import java.lang.Comparable as Comparable
import java.lang.Byte as Byte
from typing import List
import java.lang.Long as __Long
__Long = __Long
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Character as __Character
__Character = __Character
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
import java.lang.Double as Double
from builtins import int
import java.util.Random as Random
import java.lang.Float as __Float
__Float = __Float
 
class ArrayUtils():
    """org.apache.commons.lang3.ArrayUtils"""
 
    @staticmethod
    def __wrap(java_value: __ArrayUtils) -> 'ArrayUtils':
        return ArrayUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayUtils):
        """
        Dynamic initializer for ArrayUtils.
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
    def isEmpty(arg0: 'long') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(long[])"""
        return bool.__wrap(__ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def shuffle(arg0: 'char'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(char[])"""
        __ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def indexesOf(arg0: 'char', arg1: str, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(char[],char,int)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __char.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeAll(arg0: bytes, *arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.removeAll(byte[],int...)"""
        return List[int].__wrap(__ArrayUtils.removeAll(bytes, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def indexesOf(arg0: 'double', arg1: float, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(double[],double,int)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __double.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def remove(arg0: 'float', arg1: int) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.remove(float[],int)"""
        return List[float].__wrap(__ArrayUtils.remove(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def shift(arg0: 'short', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(short[],int,int,int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def isSorted(arg0: bytes) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(byte[])"""
        return bool.__wrap(__ArrayUtils.isSorted(bytes))

    @staticmethod
    @overload
    def shuffle(arg0: 'long', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(long[],java.util.Random)"""
        __ArrayUtils.shuffle(arg0, arg1)

    @staticmethod
    @overload
    def reverse(arg0: 'long', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(long[],int,int)"""
        __ArrayUtils.reverse(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def indexOf(arg0: 'boolean', arg1: bool) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(boolean[],boolean)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Class') -> List['type.Class']:
        """public static java.lang.Class<?>[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Class<?>[])"""
        return List[type.Class].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: 'long', arg1: int, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(long[],long,int)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def addAll(arg0: 'boolean', *arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.addAll(boolean[],boolean...)"""
        return List[bool].__wrap(__ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def addFirst(arg0: 'int', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.addFirst(int[],int)"""
        return List[int].__wrap(__ArrayUtils.addFirst(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'char', *arg2: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.insert(int,char[],char...)"""
        return List[str].__wrap(__ArrayUtils.insert(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'short') -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(short[])"""
        return List[int].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Short') -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Short[])"""
        return List[int].__wrap(__ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def removeElement(arg0: 'short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.removeElement(short[],short)"""
        return List[int].__wrap(__ArrayUtils.removeElement(arg0, __short.valueOf(arg1)))

    @staticmethod
    @overload
    def addFirst(arg0: 'Object', arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.addFirst(T[],T)"""
        return List[object].__wrap(__ArrayUtils.addFirst(arg0, arg1))

    @staticmethod
    @overload
    def subarray(arg0: 'Object', arg1: int, arg2: int) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.subarray(T[],int,int)"""
        return List[object].__wrap(__ArrayUtils.subarray(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def isSameLength(arg0: 'long', arg1: 'long') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(long[],long[])"""
        return bool.__wrap(__ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def clone(arg0: bytes) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.clone(byte[])"""
        return List[int].__wrap(__ArrayUtils.clone(bytes))

    @staticmethod
    @overload
    def addAll(arg0: 'Object', *arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.addAll(T[],T...)"""
        return List[object].__wrap(__ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def remove(arg0: 'int', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.remove(int[],int)"""
        return List[int].__wrap(__ArrayUtils.remove(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def shift(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(byte[],int,int,int)"""
        __ArrayUtils.shift(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def removeElements(arg0: bytes, *arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.removeElements(byte[],byte...)"""
        return List[int].__wrap(__ArrayUtils.removeElements(bytes, bytes))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'Object', *arg2: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.insert(int,T[],T...)"""
        return List[object].__wrap(__ArrayUtils.insert(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def shift(arg0: 'boolean', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(boolean[],int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def newInstance(arg0: 'Class', arg1: int) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.newInstance(java.lang.Class<T>,int)"""
        return List[object].__wrap(__ArrayUtils.newInstance(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def shift(arg0: 'char', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(char[],int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def removeAll(arg0: 'float', *arg1: int) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.removeAll(float[],int...)"""
        return List[float].__wrap(__ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def subarray(arg0: 'long', arg1: int, arg2: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.subarray(long[],int,int)"""
        return List[int].__wrap(__ArrayUtils.subarray(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Float', arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Float[],float)"""
        return List[float].__wrap(__ArrayUtils.toPrimitive(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def shuffle(arg0: 'int'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(int[])"""
        __ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def removeAll(arg0: 'int', *arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.removeAll(int[],int...)"""
        return List[int].__wrap(__ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def addAll(arg0: 'char', *arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.addAll(char[],char...)"""
        return List[str].__wrap(__ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def toStringArray(arg0: 'Object', arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.ArrayUtils.toStringArray(java.lang.Object[],java.lang.String)"""
        return List[str].__wrap(__ArrayUtils.toStringArray(arg0, arg1))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'double') -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(double[])"""
        return List[float].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Object', arg1: 'Class') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(T[],java.lang.Class<T[]>)"""
        return List[object].__wrap(__ArrayUtils.nullToEmpty(arg0, arg1))

    @staticmethod
    @overload
    def addFirst(arg0: 'double', arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.addFirst(double[],double)"""
        return List[float].__wrap(__ArrayUtils.addFirst(arg0, __double.valueOf(arg1)))

    @staticmethod
    @overload
    def shuffle(arg0: bytes):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(byte[])"""
        __ArrayUtils.shuffle(bytes)

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Integer') -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Integer[])"""
        return List[int].__wrap(__ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def indexOf(arg0: 'double', arg1: float, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(double[],double,int)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __double.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def shuffle(arg0: 'long'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(long[])"""
        __ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'boolean') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(boolean[])"""
        return bool.__wrap(__ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def indexOf(arg0: bytes, arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(byte[],byte)"""
        return int.__wrap(__ArrayUtils.indexOf(bytes, __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOf(arg0: 'long', arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(long[],long)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def remove(arg0: bytes, arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.remove(byte[],int)"""
        return List[int].__wrap(__ArrayUtils.remove(bytes, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Long[],long)"""
        return List[int].__wrap(__ArrayUtils.toPrimitive(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'Object', arg1: int, arg2: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.add(T[],int,T)"""
        return List[object].__wrap(__ArrayUtils.add(arg0, __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def indexesOf(arg0: bytes, arg1: int, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(byte[],byte,int)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(bytes, __byte.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeElement(arg0: 'Object', arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.removeElement(T[],java.lang.Object)"""
        return List[object].__wrap(__ArrayUtils.removeElement(arg0, arg1))

    @staticmethod
    @overload
    def reverse(arg0: 'boolean'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(boolean[])"""
        __ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def toPrimitive(arg0: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Object)"""
        return object.__wrap(__ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def isSameLength(arg0: 'double', arg1: 'double') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(double[],double[])"""
        return bool.__wrap(__ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'short', arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(short[],short)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __short.valueOf(arg1)))

    @staticmethod
    @overload
    def shift(arg0: 'int', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(int[],int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def removeElement(arg0: 'long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.removeElement(long[],long)"""
        return List[int].__wrap(__ArrayUtils.removeElement(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def isSorted(arg0: 'short') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(short[])"""
        return bool.__wrap(__ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'short', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(short[],short,int)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __short.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def indexesOf(arg0: 'float', arg1: float, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(float[],float,int)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __float.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def contains(arg0: 'Object', arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(java.lang.Object[],java.lang.Object)"""
        return bool.__wrap(__ArrayUtils.contains(arg0, arg1))

    @staticmethod
    @overload
    def swap(arg0: 'long', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(long[],int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Object') -> List[object]:
        """public static java.lang.Object[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Object[])"""
        return List[object].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def swap(arg0: 'short', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(short[],int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def add(arg0: bytes, arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.add(byte[],byte)"""
        return List[int].__wrap(__ArrayUtils.add(bytes, __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Boolean') -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Boolean[])"""
        return List[bool].__wrap(__ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def add(arg0: 'int', arg1: int, arg2: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.add(int[],int,int)"""
        return List[int].__wrap(__ArrayUtils.add(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def addAll(arg0: 'short', *arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.addAll(short[],short...)"""
        return List[int].__wrap(__ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'short', *arg2: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.insert(int,short[],short...)"""
        return List[int].__wrap(__ArrayUtils.insert(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def indexesOf(arg0: 'boolean', arg1: bool) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(boolean[],boolean)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def isEquals(arg0: object, arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEquals(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(__ArrayUtils.isEquals(arg0, arg1))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'char', arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(char[],char)"""
        return List[str].__wrap(__ArrayUtils.removeAllOccurrences(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'Object', arg1: object) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(java.lang.Object[],java.lang.Object)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, arg1))

    @staticmethod
    @overload
    def indexOf(arg0: 'float', arg1: float, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(float[],float,int)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __float.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def contains(arg0: 'double', arg1: float) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(double[],double)"""
        return bool.__wrap(__ArrayUtils.contains(arg0, __double.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOf(arg0: 'Object', arg1: object) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(java.lang.Object[],java.lang.Object)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, arg1))

    @staticmethod
    @overload
    def isSameLength(arg0: bytes, arg1: bytes) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(byte[],byte[])"""
        return bool.__wrap(__ArrayUtils.isSameLength(bytes, bytes))

    @staticmethod
    @overload
    def shift(arg0: 'double', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(double[],int,int,int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def indexesOf(arg0: 'int', arg1: int, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(int[],int,int)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'boolean', arg1: bool) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(boolean[],boolean)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def toMap(arg0: 'Object') -> 'Map':
        """public static java.util.Map<java.lang.Object, java.lang.Object> org.apache.commons.lang3.ArrayUtils.toMap(java.lang.Object[])"""
        return Map.__wrap(__ArrayUtils.toMap(arg0))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'int', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(int[],int,int)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def subarray(arg0: 'char', arg1: int, arg2: int) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.subarray(char[],int,int)"""
        return List[str].__wrap(__ArrayUtils.subarray(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'float', *arg2: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.insert(int,float[],float...)"""
        return List[float].__wrap(__ArrayUtils.insert(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def indexesOf(arg0: 'short', arg1: int, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(short[],short,int)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __short.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeAll(arg0: 'boolean', *arg1: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.removeAll(boolean[],int...)"""
        return List[bool].__wrap(__ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(long[],long)"""
        return List[int].__wrap(__ArrayUtils.removeAllOccurrences(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Integer') -> List['Integer']:
        """public static java.lang.Integer[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Integer[])"""
        return List[Integer].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def get(arg0: 'Object', arg1: int) -> object:
        """public static <T> T org.apache.commons.lang3.ArrayUtils.get(T[],int)"""
        return object.__wrap(__ArrayUtils.get(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def getComponentType(arg0: 'Object') -> 'type.Class':
        """public static <T> java.lang.Class<T> org.apache.commons.lang3.ArrayUtils.getComponentType(T[])"""
        return type.Class.__wrap(__ArrayUtils.getComponentType(arg0))

    @staticmethod
    @overload
    def clone(arg0: 'char') -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.clone(char[])"""
        return List[str].__wrap(__ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: bytes, arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(byte[],byte)"""
        return List[int].__wrap(__ArrayUtils.removeAllOccurrences(bytes, __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def contains(arg0: 'boolean', arg1: bool) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(boolean[],boolean)"""
        return bool.__wrap(__ArrayUtils.contains(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def shift(arg0: bytes, arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(byte[],int)"""
        __ArrayUtils.shift(bytes, __int.valueOf(arg1))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'double', arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(double[],double)"""
        return List[float].__wrap(__ArrayUtils.removeAllOccurrences(arg0, __double.valueOf(arg1)))

    @staticmethod
    @overload
    def remove(arg0: 'Object', arg1: int) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.remove(T[],int)"""
        return List[object].__wrap(__ArrayUtils.remove(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: bytes) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(byte[])"""
        return List[int].__wrap(__ArrayUtils.nullToEmpty(bytes))

    @staticmethod
    @overload
    def isEmpty(arg0: 'Object') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(java.lang.Object[])"""
        return bool.__wrap(__ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def shuffle(arg0: 'boolean', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(boolean[],java.util.Random)"""
        __ArrayUtils.shuffle(arg0, arg1)

    @staticmethod
    @overload
    def isEmpty(arg0: bytes) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(byte[])"""
        return bool.__wrap(__ArrayUtils.isEmpty(bytes))

    @staticmethod
    @overload
    def swap(arg0: 'boolean', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(boolean[],int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def shuffle(arg0: 'Object'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(java.lang.Object[])"""
        __ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def clone(arg0: 'Object') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.clone(T[])"""
        return List[object].__wrap(__ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Character', arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Character[],char)"""
        return List[str].__wrap(__ArrayUtils.toPrimitive(arg0, __char.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'double', arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(double[],double)"""
        return List[float].__wrap(__ArrayUtils.removeAllOccurences(arg0, __double.valueOf(arg1)))

    @staticmethod
    @overload
    def subarray(arg0: 'int', arg1: int, arg2: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.subarray(int[],int,int)"""
        return List[int].__wrap(__ArrayUtils.subarray(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def shuffle(arg0: 'double'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(double[])"""
        __ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def indexesOf(arg0: 'int', arg1: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(int[],int)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'char') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(char[])"""
        return bool.__wrap(__ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'double', arg1: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(double[],double)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __double.valueOf(arg1)))

    @staticmethod
    @overload
    def shift(arg0: 'float', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(float[],int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def toStringArray(arg0: 'Object') -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.ArrayUtils.toStringArray(java.lang.Object[])"""
        return List[str].__wrap(__ArrayUtils.toStringArray(arg0))

    @staticmethod
    @overload
    def shuffle(arg0: 'boolean'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(boolean[])"""
        __ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'long', arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(long[],long)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'float') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(float[])"""
        return bool.__wrap(__ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def toObject(arg0: 'long') -> List['Long']:
        """public static java.lang.Long[] org.apache.commons.lang3.ArrayUtils.toObject(long[])"""
        return List[Long].__wrap(__ArrayUtils.toObject(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def contains(arg0: 'int', arg1: int) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(int[],int)"""
        return bool.__wrap(__ArrayUtils.contains(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def isSameLength(arg0: 'float', arg1: 'float') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(float[],float[])"""
        return bool.__wrap(__ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'double', arg1: float, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(double[],double,int)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __double.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def shift(arg0: 'int', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(int[],int,int,int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def reverse(arg0: 'int', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(int[],int,int)"""
        __ArrayUtils.reverse(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def shuffle(arg0: 'char', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(char[],java.util.Random)"""
        __ArrayUtils.shuffle(arg0, arg1)

    @staticmethod
    @overload
    def swap(arg0: 'char', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(char[],int,int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def addFirst(arg0: 'short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.addFirst(short[],short)"""
        return List[int].__wrap(__ArrayUtils.addFirst(arg0, __short.valueOf(arg1)))

    @staticmethod
    @overload
    def isSameLength(arg0: 'short', arg1: 'short') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(short[],short[])"""
        return bool.__wrap(__ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Byte') -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Byte[])"""
        return List[int].__wrap(__ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def isEmpty(arg0: 'int') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(int[])"""
        return bool.__wrap(__ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def isEmpty(arg0: 'float') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(float[])"""
        return bool.__wrap(__ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def subarray(arg0: 'short', arg1: int, arg2: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.subarray(short[],int,int)"""
        return List[int].__wrap(__ArrayUtils.subarray(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(long[],long)"""
        return List[int].__wrap(__ArrayUtils.removeAllOccurences(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'long') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(long[])"""
        return bool.__wrap(__ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def indexOf(arg0: 'float', arg1: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(float[],float)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.add(long[],long)"""
        return List[int].__wrap(__ArrayUtils.add(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'double', arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.add(double[],double)"""
        return List[float].__wrap(__ArrayUtils.add(arg0, __double.valueOf(arg1)))

    @staticmethod
    @overload
    def hashCode(arg0: object) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.hashCode(java.lang.Object)"""
        return int.__wrap(__ArrayUtils.hashCode(arg0))

    @staticmethod
    @overload
    def shuffle(arg0: 'short', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(short[],java.util.Random)"""
        __ArrayUtils.shuffle(arg0, arg1)

    @staticmethod
    @overload
    def contains(arg0: 'char', arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(char[],char)"""
        return bool.__wrap(__ArrayUtils.contains(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'float', arg1: float, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(float[],float,int)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __float.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def addAll(arg0: 'float', *arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.addAll(float[],float...)"""
        return List[float].__wrap(__ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def swap(arg0: bytes, arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(byte[],int,int)"""
        __ArrayUtils.swap(bytes, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def isSorted(arg0: 'char') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(char[])"""
        return bool.__wrap(__ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: 'long', arg1: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(long[],long)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'boolean', arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.add(boolean[],boolean)"""
        return List[bool].__wrap(__ArrayUtils.add(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def isSorted(arg0: 'Object', arg1: 'Comparator') -> bool:
        """public static <T> boolean org.apache.commons.lang3.ArrayUtils.isSorted(T[],java.util.Comparator<T>)"""
        return bool.__wrap(__ArrayUtils.isSorted(arg0, arg1))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Character') -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Character[])"""
        return List[str].__wrap(__ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def isEmpty(arg0: 'short') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(short[])"""
        return bool.__wrap(__ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def addAll(arg0: 'long', *arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.addAll(long[],long...)"""
        return List[int].__wrap(__ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def swap(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(byte[],int,int,int)"""
        __ArrayUtils.swap(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def removeElements(arg0: 'boolean', *arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.removeElements(boolean[],boolean...)"""
        return List[bool].__wrap(__ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def swap(arg0: 'float', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(float[],int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def isSameLength(arg0: 'char', arg1: 'char') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(char[],char[])"""
        return bool.__wrap(__ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(short[],short)"""
        return List[int].__wrap(__ArrayUtils.removeAllOccurrences(arg0, __short.valueOf(arg1)))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Integer', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Integer[],int)"""
        return List[int].__wrap(__ArrayUtils.toPrimitive(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def swap(arg0: 'short', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(short[],int,int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def reverse(arg0: 'double', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(double[],int,int)"""
        __ArrayUtils.reverse(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'float') -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(float[])"""
        return List[float].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def toObject(arg0: 'double') -> List['Double']:
        """public static java.lang.Double[] org.apache.commons.lang3.ArrayUtils.toObject(double[])"""
        return List[Double].__wrap(__ArrayUtils.toObject(arg0))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'int', arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(int[],int)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOf(arg0: 'char', arg1: str, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(char[],char,int)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __char.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def indexesOf(arg0: 'short', arg1: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(short[],short)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __short.valueOf(arg1)))

    @staticmethod
    @overload
    def reverse(arg0: 'float', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(float[],int,int)"""
        __ArrayUtils.reverse(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def reverse(arg0: 'char', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(char[],int,int)"""
        __ArrayUtils.reverse(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def setAll(arg0: 'Object', arg1: 'Supplier') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.setAll(T[],java.util.function.Supplier<? extends T>)"""
        return List[object].__wrap(__ArrayUtils.setAll(arg0, arg1))

    @staticmethod
    @overload
    def getLength(arg0: object) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.getLength(java.lang.Object)"""
        return int.__wrap(__ArrayUtils.getLength(arg0))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Float') -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Float[])"""
        return List[float].__wrap(__ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def shift(arg0: 'Object', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(java.lang.Object[],int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def reverse(arg0: 'float'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(float[])"""
        __ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def add(arg0: 'float', arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.add(float[],float)"""
        return List[float].__wrap(__ArrayUtils.add(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def removeElements(arg0: 'float', *arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.removeElements(float[],float...)"""
        return List[float].__wrap(__ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def reverse(arg0: 'long'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(long[])"""
        __ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def addFirst(arg0: 'float', arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.addFirst(float[],float)"""
        return List[float].__wrap(__ArrayUtils.addFirst(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def swap(arg0: 'char', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(char[],int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def toObject(arg0: 'short') -> List['Short']:
        """public static java.lang.Short[] org.apache.commons.lang3.ArrayUtils.toObject(short[])"""
        return List[Short].__wrap(__ArrayUtils.toObject(arg0))

    @staticmethod
    @overload
    def remove(arg0: 'short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.remove(short[],int)"""
        return List[int].__wrap(__ArrayUtils.remove(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def remove(arg0: 'double', arg1: int) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.remove(double[],int)"""
        return List[float].__wrap(__ArrayUtils.remove(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def toObject(arg0: 'boolean') -> List['Boolean']:
        """public static java.lang.Boolean[] org.apache.commons.lang3.ArrayUtils.toObject(boolean[])"""
        return List[Boolean].__wrap(__ArrayUtils.toObject(arg0))

    @staticmethod
    @overload
    def shuffle(arg0: bytes, arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(byte[],java.util.Random)"""
        __ArrayUtils.shuffle(bytes, arg1)

    @staticmethod
    @overload
    def shuffle(arg0: 'float'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(float[])"""
        __ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def toObject(arg0: 'char') -> List['Character']:
        """public static java.lang.Character[] org.apache.commons.lang3.ArrayUtils.toObject(char[])"""
        return List[Character].__wrap(__ArrayUtils.toObject(arg0))

    @staticmethod
    @overload
    def add(arg0: 'char', arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.add(char[],char)"""
        return List[str].__wrap(__ArrayUtils.add(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def isSorted(arg0: 'int') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(int[])"""
        return bool.__wrap(__ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def clone(arg0: 'long') -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.clone(long[])"""
        return List[int].__wrap(__ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def toString(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ArrayUtils.toString(java.lang.Object)"""
        return str.__wrap(__ArrayUtils.toString(arg0))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'boolean', arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(boolean[],boolean)"""
        return List[bool].__wrap(__ArrayUtils.removeAllOccurences(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'char', arg1: str, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(char[],char,int)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __char.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeElements(arg0: 'Object', *arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.removeElements(T[],T...)"""
        return List[object].__wrap(__ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def swap(arg0: 'double', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(double[],int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'Object', arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(T[],T)"""
        return List[object].__wrap(__ArrayUtils.removeAllOccurrences(arg0, arg1))

    @staticmethod
    @overload
    def add(arg0: bytes, arg1: int, arg2: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.add(byte[],int,byte)"""
        return List[int].__wrap(__ArrayUtils.add(bytes, __int.valueOf(arg1), __byte.valueOf(arg2)))

    @staticmethod
    @overload
    def toObject(arg0: bytes) -> List['Byte']:
        """public static java.lang.Byte[] org.apache.commons.lang3.ArrayUtils.toObject(byte[])"""
        return List[Byte].__wrap(__ArrayUtils.toObject(bytes))

    @staticmethod
    @overload
    def isNotEmpty(arg0: bytes) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(byte[])"""
        return bool.__wrap(__ArrayUtils.isNotEmpty(bytes))

    @staticmethod
    @overload
    def contains(arg0: 'float', arg1: float) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(float[],float)"""
        return bool.__wrap(__ArrayUtils.contains(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def indexesOf(arg0: 'char', arg1: str) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(char[],char)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def contains(arg0: 'short', arg1: int) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(short[],short)"""
        return bool.__wrap(__ArrayUtils.contains(arg0, __short.valueOf(arg1)))

    @staticmethod
    @overload
    def removeElement(arg0: bytes, arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.removeElement(byte[],byte)"""
        return List[int].__wrap(__ArrayUtils.removeElement(bytes, __byte.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'double') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(double[])"""
        return bool.__wrap(__ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Double') -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Double[])"""
        return List[float].__wrap(__ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def indexOf(arg0: 'long', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(long[],long,int)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def clone(arg0: 'boolean') -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.clone(boolean[])"""
        return List[bool].__wrap(__ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: 'double', arg1: float, arg2: float) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(double[],double,double)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def toString(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ArrayUtils.toString(java.lang.Object,java.lang.String)"""
        return str.__wrap(__ArrayUtils.toString(arg0, arg1))

    @staticmethod
    @overload
    def reverse(arg0: 'Object'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(java.lang.Object[])"""
        __ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def indexOf(arg0: 'short', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(short[],short,int)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __short.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def isEmpty(arg0: 'double') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(double[])"""
        return bool.__wrap(__ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'boolean', arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(boolean[],boolean)"""
        return List[bool].__wrap(__ArrayUtils.removeAllOccurrences(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Short') -> List['Short']:
        """public static java.lang.Short[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Short[])"""
        return List[Short].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def indexOf(arg0: 'short', arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(short[],short)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __short.valueOf(arg1)))

    @staticmethod
    @overload
    def shift(arg0: 'long', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(long[],int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'int') -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(int[])"""
        return List[int].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Long') -> List['Long']:
        """public static java.lang.Long[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Long[])"""
        return List[Long].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: 'Object', arg1: object) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(java.lang.Object[],java.lang.Object)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, arg1))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Boolean') -> List['Boolean']:
        """public static java.lang.Boolean[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Boolean[])"""
        return List[Boolean].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def isSameLength(arg0: 'int', arg1: 'int') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(int[],int[])"""
        return bool.__wrap(__ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'int', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(int[],int)"""
        return List[int].__wrap(__ArrayUtils.removeAllOccurrences(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOf(arg0: 'Object', arg1: object, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(java.lang.Object[],java.lang.Object,int)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeElements(arg0: 'int', *arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.removeElements(int[],int...)"""
        return List[int].__wrap(__ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def removeElement(arg0: 'int', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.removeElement(int[],int)"""
        return List[int].__wrap(__ArrayUtils.removeElement(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def get(arg0: 'Object', arg1: int, arg2: object) -> object:
        """public static <T> T org.apache.commons.lang3.ArrayUtils.get(T[],int,T)"""
        return object.__wrap(__ArrayUtils.get(arg0, __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def indexesOf(arg0: 'Object', arg1: object, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(java.lang.Object[],java.lang.Object,int)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def reverse(arg0: 'int'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(int[])"""
        __ArrayUtils.reverse(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def reverse(arg0: bytes):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(byte[])"""
        __ArrayUtils.reverse(bytes)

    @staticmethod
    @overload
    def removeElements(arg0: 'short', *arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.removeElements(short[],short...)"""
        return List[int].__wrap(__ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def add(arg0: 'boolean', arg1: int, arg2: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.add(boolean[],int,boolean)"""
        return List[bool].__wrap(__ArrayUtils.add(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def contains(arg0: 'double', arg1: float, arg2: float) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(double[],double,double)"""
        return bool.__wrap(__ArrayUtils.contains(arg0, __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def toObject(arg0: 'int') -> List['Integer']:
        """public static java.lang.Integer[] org.apache.commons.lang3.ArrayUtils.toObject(int[])"""
        return List[Integer].__wrap(__ArrayUtils.toObject(arg0))

    @staticmethod
    @overload
    def shift(arg0: 'float', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(float[],int,int,int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def indexOf(arg0: 'int', arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(int[],int)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: bytes, *arg2: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.insert(int,byte[],byte...)"""
        return List[int].__wrap(__ArrayUtils.insert(__int.valueOf(arg0), bytes, bytes))

    @staticmethod
    @overload
    def isEmpty(arg0: 'char') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(char[])"""
        return bool.__wrap(__ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def swap(arg0: 'int', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(int[],int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def toObject(arg0: 'float') -> List['Float']:
        """public static java.lang.Float[] org.apache.commons.lang3.ArrayUtils.toObject(float[])"""
        return List[Float].__wrap(__ArrayUtils.toObject(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: 'float', arg1: float) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(float[],float)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOf(arg0: 'double', arg1: float, arg2: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(double[],double,double)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def shuffle(arg0: 'float', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(float[],java.util.Random)"""
        __ArrayUtils.shuffle(arg0, arg1)

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'int') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(int[])"""
        return bool.__wrap(__ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def containsAny(arg0: 'Object', *arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.containsAny(java.lang.Object[],java.lang.Object...)"""
        return bool.__wrap(__ArrayUtils.containsAny(arg0, arg1))

    @staticmethod
    @overload
    def removeElement(arg0: 'float', arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.removeElement(float[],float)"""
        return List[float].__wrap(__ArrayUtils.removeElement(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'double', arg1: float, arg2: int, arg3: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(double[],double,int,double)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __double.valueOf(arg1), __int.valueOf(arg2), __double.valueOf(arg3)))

    @staticmethod
    @overload
    def indexesOf(arg0: 'double', arg1: float) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(double[],double)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __double.valueOf(arg1)))

    @staticmethod
    @overload
    def subarray(arg0: 'boolean', arg1: int, arg2: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.subarray(boolean[],int,int)"""
        return List[bool].__wrap(__ArrayUtils.subarray(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'float', arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(float[],float)"""
        return List[float].__wrap(__ArrayUtils.removeAllOccurrences(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def swap(arg0: 'double', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(double[],int,int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Character') -> List['Character']:
        """public static java.lang.Character[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Character[])"""
        return List[Character].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'float', arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(float[],float)"""
        return List[float].__wrap(__ArrayUtils.removeAllOccurences(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: bytes, arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(byte[],byte)"""
        return List[int].__wrap(__ArrayUtils.removeAllOccurences(bytes, __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def addAll(arg0: bytes, *arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.addAll(byte[],byte...)"""
        return List[int].__wrap(__ArrayUtils.addAll(bytes, bytes))

    @staticmethod
    @overload
    def clone(arg0: 'double') -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.clone(double[])"""
        return List[float].__wrap(__ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def addFirst(arg0: bytes, arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.addFirst(byte[],byte)"""
        return List[int].__wrap(__ArrayUtils.addFirst(bytes, __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Double') -> List['Double']:
        """public static java.lang.Double[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Double[])"""
        return List[Double].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def add(arg0: 'short', arg1: int, arg2: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.add(short[],int,short)"""
        return List[int].__wrap(__ArrayUtils.add(arg0, __int.valueOf(arg1), __short.valueOf(arg2)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'String') -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.String[])"""
        return List[str].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def isSorted(arg0: 'Comparable') -> bool:
        """public static <T extends java.lang.Comparable<? super T>> boolean org.apache.commons.lang3.ArrayUtils.isSorted(T[])"""
        return bool.__wrap(__ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def add(arg0: 'char', arg1: int, arg2: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.add(char[],int,char)"""
        return List[str].__wrap(__ArrayUtils.add(arg0, __int.valueOf(arg1), __char.valueOf(arg2)))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(short[],short)"""
        return List[int].__wrap(__ArrayUtils.removeAllOccurences(arg0, __short.valueOf(arg1)))

    @staticmethod
    @overload
    def removeAll(arg0: 'char', *arg1: int) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.removeAll(char[],int...)"""
        return List[str].__wrap(__ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'Object', arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(T[],T)"""
        return List[object].__wrap(__ArrayUtils.removeAllOccurences(arg0, arg1))

    @staticmethod
    @overload
    def indexOf(arg0: 'double', arg1: float, arg2: int, arg3: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(double[],double,int,double)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __double.valueOf(arg1), __int.valueOf(arg2), __double.valueOf(arg3)))

    @staticmethod
    @overload
    def reverse(arg0: 'short'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(short[])"""
        __ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def lastIndexOf(arg0: bytes, arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(byte[],byte)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(bytes, __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOf(arg0: 'char', arg1: str) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(char[],char)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def removeElement(arg0: 'char', arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.removeElement(char[],char)"""
        return List[str].__wrap(__ArrayUtils.removeElement(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def clone(arg0: 'float') -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.clone(float[])"""
        return List[float].__wrap(__ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'boolean', *arg2: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.insert(int,boolean[],boolean...)"""
        return List[bool].__wrap(__ArrayUtils.insert(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def clone(arg0: 'int') -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.clone(int[])"""
        return List[int].__wrap(__ArrayUtils.clone(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ArrayUtils()"""
        val = __ArrayUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def reverse(arg0: bytes, arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(byte[],int,int)"""
        __ArrayUtils.reverse(bytes, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def indexesOf(arg0: 'boolean', arg1: bool, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(boolean[],boolean,int)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __boolean.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def add(arg0: 'Object', arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.add(T[],T)"""
        return List[object].__wrap(__ArrayUtils.add(arg0, arg1))

    @staticmethod
    @overload
    def indexesOf(arg0: 'double', arg1: float, arg2: int, arg3: float) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(double[],double,int,double)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(arg0, __double.valueOf(arg1), __int.valueOf(arg2), __double.valueOf(arg3)))

    @staticmethod
    @overload
    def setAll(arg0: 'Object', arg1: 'IntFunction') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.setAll(T[],java.util.function.IntFunction<? extends T>)"""
        return List[object].__wrap(__ArrayUtils.setAll(arg0, arg1))

    @staticmethod
    @overload
    def addFirst(arg0: 'long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.addFirst(long[],long)"""
        return List[int].__wrap(__ArrayUtils.addFirst(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def swap(arg0: 'boolean', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(boolean[],int,int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'boolean') -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(boolean[])"""
        return List[bool].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Byte', arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Byte[],byte)"""
        return List[int].__wrap(__ArrayUtils.toPrimitive(arg0, __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def reverse(arg0: 'double'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(double[])"""
        __ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def subarray(arg0: 'float', arg1: int, arg2: int) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.subarray(float[],int,int)"""
        return List[float].__wrap(__ArrayUtils.subarray(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def isSameType(arg0: object, arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameType(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(__ArrayUtils.isSameType(arg0, arg1))

    @staticmethod
    @overload
    def indexesOf(arg0: bytes, arg1: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(byte[],byte)"""
        return BitSet.__wrap(__ArrayUtils.indexesOf(bytes, __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def removeElement(arg0: 'boolean', arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.removeElement(boolean[],boolean)"""
        return List[bool].__wrap(__ArrayUtils.removeElement(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'Object', arg1: object, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(java.lang.Object[],java.lang.Object,int)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def addAll(arg0: 'int', *arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.addAll(int[],int...)"""
        return List[int].__wrap(__ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def isSameLength(arg0: 'Object', arg1: 'Object') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(java.lang.Object[],java.lang.Object[])"""
        return bool.__wrap(__ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def reverse(arg0: 'char'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(char[])"""
        __ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def isSameLength(arg0: object, arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(__ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'float', arg1: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(float[],float)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def shuffle(arg0: 'short'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(short[])"""
        __ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def shift(arg0: 'boolean', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(boolean[],int,int,int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def swap(arg0: 'long', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(long[],int,int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'char', arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(char[],char)"""
        return List[str].__wrap(__ArrayUtils.removeAllOccurences(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'long', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(long[],long,int)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeAll(arg0: 'double', *arg1: int) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.removeAll(double[],int...)"""
        return List[float].__wrap(__ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'char') -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(char[])"""
        return List[str].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def removeElement(arg0: 'double', arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.removeElement(double[],double)"""
        return List[float].__wrap(__ArrayUtils.removeElement(arg0, __double.valueOf(arg1)))

    @staticmethod
    @overload
    def shift(arg0: 'double', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(double[],int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'short') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(short[])"""
        return bool.__wrap(__ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def isSorted(arg0: 'double') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(double[])"""
        return bool.__wrap(__ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def clone(arg0: 'short') -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.clone(short[])"""
        return List[int].__wrap(__ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def shift(arg0: 'long', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(long[],int,int,int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def shuffle(arg0: 'int', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(int[],java.util.Random)"""
        __ArrayUtils.shuffle(arg0, arg1)

    @staticmethod
    @overload
    def shift(arg0: 'short', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(short[],int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'int', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(int[],int)"""
        return List[int].__wrap(__ArrayUtils.removeAllOccurences(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def addFirst(arg0: 'boolean', arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.addFirst(boolean[],boolean)"""
        return List[bool].__wrap(__ArrayUtils.addFirst(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def remove(arg0: 'char', arg1: int) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.remove(char[],int)"""
        return List[str].__wrap(__ArrayUtils.remove(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Boolean', arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Boolean[],boolean)"""
        return List[bool].__wrap(__ArrayUtils.toPrimitive(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def subarray(arg0: bytes, arg1: int, arg2: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.subarray(byte[],int,int)"""
        return List[int].__wrap(__ArrayUtils.subarray(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def isSameLength(arg0: 'boolean', arg1: 'boolean') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(boolean[],boolean[])"""
        return bool.__wrap(__ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def removeElements(arg0: 'char', *arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.removeElements(char[],char...)"""
        return List[str].__wrap(__ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def isEmpty(arg0: 'boolean') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(boolean[])"""
        return bool.__wrap(__ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def removeAll(arg0: 'long', *arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.removeAll(long[],int...)"""
        return List[int].__wrap(__ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def reverse(arg0: 'Object', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(java.lang.Object[],int,int)"""
        __ArrayUtils.reverse(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Double', arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Double[],double)"""
        return List[float].__wrap(__ArrayUtils.toPrimitive(arg0, __double.valueOf(arg1)))

    @staticmethod
    @overload
    def shift(arg0: 'Object', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(java.lang.Object[],int,int,int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ArrayUtils()"""
        val = __ArrayUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def isSorted(arg0: 'long') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(long[])"""
        return bool.__wrap(__ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def swap(arg0: 'float', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(float[],int,int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def remove(arg0: 'long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.remove(long[],int)"""
        return List[int].__wrap(__ArrayUtils.remove(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'float', arg1: int, arg2: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.add(float[],int,float)"""
        return List[float].__wrap(__ArrayUtils.add(arg0, __int.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def shuffle(arg0: 'Object', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(java.lang.Object[],java.util.Random)"""
        __ArrayUtils.shuffle(arg0, arg1)

    @staticmethod
    @overload
    def indexOf(arg0: bytes, arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(byte[],byte,int)"""
        return int.__wrap(__ArrayUtils.indexOf(bytes, __byte.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def swap(arg0: 'Object', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(java.lang.Object[],int,int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def swap(arg0: 'Object', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(java.lang.Object[],int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def isSorted(arg0: 'boolean') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(boolean[])"""
        return bool.__wrap(__ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'Object') -> bool:
        """public static <T> boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(T[])"""
        return bool.__wrap(__ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def reverse(arg0: 'boolean', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(boolean[],int,int)"""
        __ArrayUtils.reverse(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def add(arg0: 'double', arg1: int, arg2: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.add(double[],int,double)"""
        return List[float].__wrap(__ArrayUtils.add(arg0, __int.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def isSorted(arg0: 'float') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(float[])"""
        return bool.__wrap(__ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'double', arg1: float, arg2: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(double[],double,double)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'long', *arg2: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.insert(int,long[],long...)"""
        return List[int].__wrap(__ArrayUtils.insert(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'char', arg1: str) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(char[],char)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'double', *arg2: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.insert(int,double[],double...)"""
        return List[float].__wrap(__ArrayUtils.insert(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Byte') -> List['Byte']:
        """public static java.lang.Byte[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Byte[])"""
        return List[Byte].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def swap(arg0: 'int', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(int[],int,int,int)"""
        __ArrayUtils.swap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def removeElements(arg0: 'long', *arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.removeElements(long[],long...)"""
        return List[int].__wrap(__ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def removeAll(arg0: 'Object', *arg1: int) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.removeAll(T[],int...)"""
        return List[object].__wrap(__ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def indexOf(arg0: 'int', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(int[],int,int)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def toArray(*arg0: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.toArray(T...)"""
        return List[object].__wrap(__ArrayUtils.toArray(arg0))

    @staticmethod
    @overload
    def subarray(arg0: 'double', arg1: int, arg2: int) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.subarray(double[],int,int)"""
        return List[float].__wrap(__ArrayUtils.subarray(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'int', *arg2: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.insert(int,int[],int...)"""
        return List[int].__wrap(__ArrayUtils.insert(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def indexOf(arg0: 'double', arg1: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(double[],double)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __double.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'long', arg1: int, arg2: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.add(long[],int,long)"""
        return List[int].__wrap(__ArrayUtils.add(arg0, __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def isArrayIndexValid(arg0: 'Object', arg1: int) -> bool:
        """public static <T> boolean org.apache.commons.lang3.ArrayUtils.isArrayIndexValid(T[],int)"""
        return bool.__wrap(__ArrayUtils.isArrayIndexValid(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def removeAll(arg0: 'short', *arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.removeAll(short[],int...)"""
        return List[int].__wrap(__ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Long') -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Long[])"""
        return List[int].__wrap(__ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def lastIndexOf(arg0: bytes, arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(byte[],byte,int)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(bytes, __byte.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def addFirst(arg0: 'char', arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.addFirst(char[],char)"""
        return List[str].__wrap(__ArrayUtils.addFirst(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def shift(arg0: 'char', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(char[],int,int,int)"""
        __ArrayUtils.shift(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def add(arg0: 'short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.add(short[],short)"""
        return List[int].__wrap(__ArrayUtils.add(arg0, __short.valueOf(arg1)))

    @staticmethod
    @overload
    def contains(arg0: 'long', arg1: int) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(long[],long)"""
        return bool.__wrap(__ArrayUtils.contains(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'int', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.add(int[],int)"""
        return List[int].__wrap(__ArrayUtils.add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Short[],short)"""
        return List[int].__wrap(__ArrayUtils.toPrimitive(arg0, __short.valueOf(arg1)))

    @staticmethod
    @overload
    def addAll(arg0: 'double', *arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.addAll(double[],double...)"""
        return List[float].__wrap(__ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'long') -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(long[])"""
        return List[int].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def reverse(arg0: 'short', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(short[],int,int)"""
        __ArrayUtils.reverse(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def contains(arg0: bytes, arg1: int) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(byte[],byte)"""
        return bool.__wrap(__ArrayUtils.contains(bytes, __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Float') -> List['Float']:
        """public static java.lang.Float[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Float[])"""
        return List[Float].__wrap(__ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def remove(arg0: 'boolean', arg1: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.remove(boolean[],int)"""
        return List[bool].__wrap(__ArrayUtils.remove(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOf(arg0: 'boolean', arg1: bool, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(boolean[],boolean,int)"""
        return int.__wrap(__ArrayUtils.indexOf(arg0, __boolean.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'boolean', arg1: bool, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(boolean[],boolean,int)"""
        return int.__wrap(__ArrayUtils.lastIndexOf(arg0, __boolean.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeElements(arg0: 'double', *arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.removeElements(double[],double...)"""
        return List[float].__wrap(__ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def shuffle(arg0: 'double', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(double[],java.util.Random)"""
        __ArrayUtils.shuffle(arg0, arg1) 
 
 
# CLASS: org.apache.commons.lang3.Validate
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import java.lang.Double as __double
from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Iterable as Iterable
from builtins import object
import java.lang.Comparable as Comparable
from typing import List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.lang3.Validate as __Validate
__Validate = __Validate
import java.util.Map as Map
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
 
class Validate():
    """org.apache.commons.lang3.Validate"""
 
    @staticmethod
    def __wrap(java_value: __Validate) -> 'Validate':
        return Validate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Validate):
        """
        Dynamic initializer for Validate.
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
    def isAssignableFrom(arg0: 'Class', arg1: 'Class', arg2: str, *arg3: object):
        """public static void org.apache.commons.lang3.Validate.isAssignableFrom(java.lang.Class<?>,java.lang.Class<?>,java.lang.String,java.lang.Object...)"""
        __Validate.isAssignableFrom(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def noNullElements(arg0: 'Iterable', arg1: str, *arg2: object) -> 'Iterable':
        """public static <T extends java.lang.Iterable<?>> T org.apache.commons.lang3.Validate.noNullElements(T,java.lang.String,java.lang.Object...)"""
        return Iterable.__wrap(__Validate.noNullElements(arg0, arg1, arg2))

    @staticmethod
    @overload
    def notEmpty(arg0: 'Object', arg1: str, *arg2: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.Validate.notEmpty(T[],java.lang.String,java.lang.Object...)"""
        return List[object].__wrap(__Validate.notEmpty(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def validIndex(arg0: 'CharSequence', arg1: int) -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.Validate.validIndex(T,int)"""
        return CharSequence.__wrap(__Validate.validIndex(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def noNullElements(arg0: 'Object', arg1: str, *arg2: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.Validate.noNullElements(T[],java.lang.String,java.lang.Object...)"""
        return List[object].__wrap(__Validate.noNullElements(arg0, arg1, arg2))

    @staticmethod
    @overload
    def validIndex(arg0: 'CharSequence', arg1: int, arg2: str, *arg3: object) -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.Validate.validIndex(T,int,java.lang.String,java.lang.Object...)"""
        return CharSequence.__wrap(__Validate.validIndex(arg0, __int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def notEmpty(arg0: 'CharSequence', arg1: str, *arg2: object) -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.Validate.notEmpty(T,java.lang.String,java.lang.Object...)"""
        return CharSequence.__wrap(__Validate.notEmpty(arg0, arg1, arg2))

    @staticmethod
    @overload
    def notNull(arg0: object, arg1: str, *arg2: object) -> object:
        """public static <T> T org.apache.commons.lang3.Validate.notNull(T,java.lang.String,java.lang.Object...)"""
        return object.__wrap(__Validate.notNull(arg0, arg1, arg2))

    @staticmethod
    @overload
    def exclusiveBetween(arg0: float, arg1: float, arg2: float, arg3: str):
        """public static void org.apache.commons.lang3.Validate.exclusiveBetween(double,double,double,java.lang.String)"""
        __Validate.exclusiveBetween(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def notEmpty(arg0: 'CharSequence') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.Validate.notEmpty(T)"""
        return CharSequence.__wrap(__Validate.notEmpty(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def finite(arg0: float):
        """public static void org.apache.commons.lang3.Validate.finite(double)"""
        __Validate.finite(__double.valueOf(arg0))

    @staticmethod
    @overload
    def notNaN(arg0: float, arg1: str, *arg2: object):
        """public static void org.apache.commons.lang3.Validate.notNaN(double,java.lang.String,java.lang.Object...)"""
        __Validate.notNaN(__double.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def notEmpty(arg0: 'Object') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.Validate.notEmpty(T[])"""
        return List[object].__wrap(__Validate.notEmpty(arg0))

    @staticmethod
    @overload
    def notNaN(arg0: float):
        """public static void org.apache.commons.lang3.Validate.notNaN(double)"""
        __Validate.notNaN(__double.valueOf(arg0))

    @staticmethod
    @overload
    def notEmpty(arg0: 'Collection', arg1: str, *arg2: object) -> 'Collection':
        """public static <T extends java.util.Collection<?>> T org.apache.commons.lang3.Validate.notEmpty(T,java.lang.String,java.lang.Object...)"""
        return Collection.__wrap(__Validate.notEmpty(arg0, arg1, arg2))

    @staticmethod
    @overload
    def notBlank(arg0: 'CharSequence') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.Validate.notBlank(T)"""
        return CharSequence.__wrap(__Validate.notBlank(arg0))

    @staticmethod
    @overload
    def noNullElements(arg0: 'Iterable') -> 'Iterable':
        """public static <T extends java.lang.Iterable<?>> T org.apache.commons.lang3.Validate.noNullElements(T)"""
        return Iterable.__wrap(__Validate.noNullElements(arg0))

    @staticmethod
    @overload
    def inclusiveBetween(arg0: object, arg1: object, arg2: 'Comparable'):
        """public static <T> void org.apache.commons.lang3.Validate.inclusiveBetween(T,T,java.lang.Comparable<T>)"""
        __Validate.inclusiveBetween(arg0, arg1, arg2)

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.Validate()"""
        val = __Validate()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def notEmpty(arg0: 'Map', arg1: str, *arg2: object) -> 'Map':
        """public static <T extends java.util.Map<?, ?>> T org.apache.commons.lang3.Validate.notEmpty(T,java.lang.String,java.lang.Object...)"""
        return Map.__wrap(__Validate.notEmpty(arg0, arg1, arg2))

    @staticmethod
    @overload
    def validIndex(arg0: 'Object', arg1: int) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.Validate.validIndex(T[],int)"""
        return List[object].__wrap(__Validate.validIndex(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def exclusiveBetween(arg0: int, arg1: int, arg2: int, arg3: str):
        """public static void org.apache.commons.lang3.Validate.exclusiveBetween(long,long,long,java.lang.String)"""
        __Validate.exclusiveBetween(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def isInstanceOf(arg0: 'Class', arg1: object):
        """public static void org.apache.commons.lang3.Validate.isInstanceOf(java.lang.Class<?>,java.lang.Object)"""
        __Validate.isInstanceOf(arg0, arg1)

    @staticmethod
    @overload
    def inclusiveBetween(arg0: object, arg1: object, arg2: 'Comparable', arg3: str, *arg4: object):
        """public static <T> void org.apache.commons.lang3.Validate.inclusiveBetween(T,T,java.lang.Comparable<T>,java.lang.String,java.lang.Object...)"""
        __Validate.inclusiveBetween(arg0, arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def matchesPattern(arg0: 'CharSequence', arg1: str, arg2: str, *arg3: object):
        """public static void org.apache.commons.lang3.Validate.matchesPattern(java.lang.CharSequence,java.lang.String,java.lang.String,java.lang.Object...)"""
        __Validate.matchesPattern(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def isTrue(arg0: bool, arg1: str, *arg2: object):
        """public static void org.apache.commons.lang3.Validate.isTrue(boolean,java.lang.String,java.lang.Object...)"""
        __Validate.isTrue(__boolean.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def validIndex(arg0: 'Collection', arg1: int, arg2: str, *arg3: object) -> 'Collection':
        """public static <T extends java.util.Collection<?>> T org.apache.commons.lang3.Validate.validIndex(T,int,java.lang.String,java.lang.Object...)"""
        return Collection.__wrap(__Validate.validIndex(arg0, __int.valueOf(arg1), arg2, arg3))

    @staticmethod
    @overload
    def isInstanceOf(arg0: 'Class', arg1: object, arg2: str, *arg3: object):
        """public static void org.apache.commons.lang3.Validate.isInstanceOf(java.lang.Class<?>,java.lang.Object,java.lang.String,java.lang.Object...)"""
        __Validate.isInstanceOf(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def isAssignableFrom(arg0: 'Class', arg1: 'Class'):
        """public static void org.apache.commons.lang3.Validate.isAssignableFrom(java.lang.Class<?>,java.lang.Class<?>)"""
        __Validate.isAssignableFrom(arg0, arg1)

    @staticmethod
    @overload
    def inclusiveBetween(arg0: float, arg1: float, arg2: float):
        """public static void org.apache.commons.lang3.Validate.inclusiveBetween(double,double,double)"""
        __Validate.inclusiveBetween(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @staticmethod
    @overload
    def validState(arg0: bool):
        """public static void org.apache.commons.lang3.Validate.validState(boolean)"""
        __Validate.validState(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def validIndex(arg0: 'Collection', arg1: int) -> 'Collection':
        """public static <T extends java.util.Collection<?>> T org.apache.commons.lang3.Validate.validIndex(T,int)"""
        return Collection.__wrap(__Validate.validIndex(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def inclusiveBetween(arg0: int, arg1: int, arg2: int, arg3: str):
        """public static void org.apache.commons.lang3.Validate.inclusiveBetween(long,long,long,java.lang.String)"""
        __Validate.inclusiveBetween(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def notBlank(arg0: 'CharSequence', arg1: str, *arg2: object) -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.Validate.notBlank(T,java.lang.String,java.lang.Object...)"""
        return CharSequence.__wrap(__Validate.notBlank(arg0, arg1, arg2))

    @staticmethod
    @overload
    def exclusiveBetween(arg0: object, arg1: object, arg2: 'Comparable'):
        """public static <T> void org.apache.commons.lang3.Validate.exclusiveBetween(T,T,java.lang.Comparable<T>)"""
        __Validate.exclusiveBetween(arg0, arg1, arg2)

    @staticmethod
    @overload
    def inclusiveBetween(arg0: int, arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.Validate.inclusiveBetween(long,long,long)"""
        __Validate.inclusiveBetween(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def isTrue(arg0: bool, arg1: str, arg2: float):
        """public static void org.apache.commons.lang3.Validate.isTrue(boolean,java.lang.String,double)"""
        __Validate.isTrue(__boolean.valueOf(arg0), arg1, __double.valueOf(arg2))

    @staticmethod
    @overload
    def notNull(arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.Validate.notNull(T)"""
        return object.__wrap(__Validate.notNull(arg0))

    @staticmethod
    @overload
    def validIndex(arg0: 'Object', arg1: int, arg2: str, *arg3: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.Validate.validIndex(T[],int,java.lang.String,java.lang.Object...)"""
        return List[object].__wrap(__Validate.validIndex(arg0, __int.valueOf(arg1), arg2, arg3))

    @staticmethod
    @overload
    def isTrue(arg0: bool, arg1: str, arg2: int):
        """public static void org.apache.commons.lang3.Validate.isTrue(boolean,java.lang.String,long)"""
        __Validate.isTrue(__boolean.valueOf(arg0), arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def matchesPattern(arg0: 'CharSequence', arg1: str):
        """public static void org.apache.commons.lang3.Validate.matchesPattern(java.lang.CharSequence,java.lang.String)"""
        __Validate.matchesPattern(arg0, arg1)

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
    def notEmpty(arg0: 'Collection') -> 'Collection':
        """public static <T extends java.util.Collection<?>> T org.apache.commons.lang3.Validate.notEmpty(T)"""
        return Collection.__wrap(__Validate.notEmpty(arg0))

    @staticmethod
    @overload
    def noNullElements(arg0: 'Object') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.Validate.noNullElements(T[])"""
        return List[object].__wrap(__Validate.noNullElements(arg0))

    @staticmethod
    @overload
    def exclusiveBetween(arg0: float, arg1: float, arg2: float):
        """public static void org.apache.commons.lang3.Validate.exclusiveBetween(double,double,double)"""
        __Validate.exclusiveBetween(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @staticmethod
    @overload
    def exclusiveBetween(arg0: object, arg1: object, arg2: 'Comparable', arg3: str, *arg4: object):
        """public static <T> void org.apache.commons.lang3.Validate.exclusiveBetween(T,T,java.lang.Comparable<T>,java.lang.String,java.lang.Object...)"""
        __Validate.exclusiveBetween(arg0, arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def validState(arg0: bool, arg1: str, *arg2: object):
        """public static void org.apache.commons.lang3.Validate.validState(boolean,java.lang.String,java.lang.Object...)"""
        __Validate.validState(__boolean.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def inclusiveBetween(arg0: float, arg1: float, arg2: float, arg3: str):
        """public static void org.apache.commons.lang3.Validate.inclusiveBetween(double,double,double,java.lang.String)"""
        __Validate.inclusiveBetween(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def exclusiveBetween(arg0: int, arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.Validate.exclusiveBetween(long,long,long)"""
        __Validate.exclusiveBetween(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def notEmpty(arg0: 'Map') -> 'Map':
        """public static <T extends java.util.Map<?, ?>> T org.apache.commons.lang3.Validate.notEmpty(T)"""
        return Map.__wrap(__Validate.notEmpty(arg0))

    @staticmethod
    @overload
    def isTrue(arg0: bool):
        """public static void org.apache.commons.lang3.Validate.isTrue(boolean)"""
        __Validate.isTrue(__boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.Validate()"""
        val = __Validate()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def finite(arg0: float, arg1: str, *arg2: object):
        """public static void org.apache.commons.lang3.Validate.finite(double,java.lang.String,java.lang.Object...)"""
        __Validate.finite(__double.valueOf(arg0), arg1, arg2) 
 
 
# CLASS: org.apache.commons.lang3.Streams$FailableStream
import java.util.function.Supplier as Supplier
from builtins import str
import org.apache.commons.lang3.Streams as __Streams_FailableStream
__FailableStream = __Streams_FailableStream.FailableStream
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.stream.Collector as Collector
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.util.function.BinaryOperator as BinaryOperator
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FailableStream():
    """org.apache.commons.lang3.Streams.FailableStream"""
 
    @staticmethod
    def __wrap(java_value: __FailableStream) -> 'FailableStream':
        return FailableStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableStream):
        """
        Dynamic initializer for FailableStream.
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
    def map(self, arg0: 'FailableFunction') -> 'FailableStream':
        """public <R> org.apache.commons.lang3.Streams$FailableStream<R> org.apache.commons.lang3.Streams$FailableStream.map(org.apache.commons.lang3.Functions$FailableFunction<O, R, ?>)"""
        return 'FailableStream'.__wrap(super(__FailableStream, self).map(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def reduce(self, arg0: object, arg1: 'BinaryOperator') -> object:
        """public O org.apache.commons.lang3.Streams$FailableStream.reduce(O,java.util.function.BinaryOperator<O>)"""
        return object.__wrap(super(__FailableStream, self).reduce(arg0, arg1))

    @overload
    def allMatch(self, arg0: 'FailablePredicate') -> bool:
        """public boolean org.apache.commons.lang3.Streams$FailableStream.allMatch(org.apache.commons.lang3.Functions$FailablePredicate<O, ?>)"""
        return bool.__wrap(super(__FailableStream, self).allMatch(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def filter(self, arg0: 'FailablePredicate') -> 'FailableStream':
        """public org.apache.commons.lang3.Streams$FailableStream<O> org.apache.commons.lang3.Streams$FailableStream.filter(org.apache.commons.lang3.Functions$FailablePredicate<O, ?>)"""
        return 'FailableStream'.__wrap(super(__FailableStream, self).filter(arg0))

    @overload
    def collect(self, arg0: 'Collector') -> object:
        """public <A,R> R org.apache.commons.lang3.Streams$FailableStream.collect(java.util.stream.Collector<? super O, A, R>)"""
        return object.__wrap(super(__FailableStream, self).collect(arg0))

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
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<O> org.apache.commons.lang3.Streams$FailableStream.stream()"""
        return 'Stream'.__wrap(super(FailableStream, self).stream())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def collect(self, arg0: 'Supplier', arg1: 'BiConsumer', arg2: 'BiConsumer') -> object:
        """public <A,R> R org.apache.commons.lang3.Streams$FailableStream.collect(java.util.function.Supplier<R>,java.util.function.BiConsumer<R, ? super O>,java.util.function.BiConsumer<R, R>)"""
        return object.__wrap(super(__FailableStream, self).collect(arg0, arg1, arg2))

    @overload
    def forEach(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.Streams$FailableStream.forEach(org.apache.commons.lang3.Functions$FailableConsumer<O, ?>)"""
        super(__FailableStream, self).forEach(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Stream'):
        """public org.apache.commons.lang3.Streams$FailableStream(java.util.stream.Stream<O>)"""
        val = __FailableStream(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def anyMatch(self, arg0: 'FailablePredicate') -> bool:
        """public boolean org.apache.commons.lang3.Streams$FailableStream.anyMatch(org.apache.commons.lang3.Functions$FailablePredicate<O, ?>)"""
        return bool.__wrap(super(__FailableStream, self).anyMatch(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.CharSet
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.CharSet as __CharSet
__CharSet = __CharSet
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
 
class CharSet():
    """org.apache.commons.lang3.CharSet"""
 
    @staticmethod
    def __wrap(java_value: __CharSet) -> 'CharSet':
        return CharSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharSet):
        """
        Dynamic initializer for CharSet.
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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.CharSet.toString()"""
        return str.__wrap(super(CharSet, self).toString())

    @staticmethod
    @overload
    def getInstance(*arg0: str) -> 'CharSet':
        """public static org.apache.commons.lang3.CharSet org.apache.commons.lang3.CharSet.getInstance(java.lang.String...)"""
        return CharSet.__wrap(__CharSet.getInstance(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.CharSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__CharSet, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.CharSet.hashCode()"""
        return int.__wrap(super(CharSet, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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
    def contains(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.CharSet.contains(char)"""
        return bool.__wrap(super(__CharSet, self).contains(__char.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.StringEscapeUtils
from builtins import str
from pyquantum_helper import override
import org.apache.commons.lang3.StringEscapeUtils as __StringEscapeUtils
__StringEscapeUtils = __StringEscapeUtils
import java.lang.Object as __object
from builtins import type
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
 
class StringEscapeUtils():
    """org.apache.commons.lang3.StringEscapeUtils"""
 
    @staticmethod
    def __wrap(java_value: __StringEscapeUtils) -> 'StringEscapeUtils':
        return StringEscapeUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringEscapeUtils):
        """
        Dynamic initializer for StringEscapeUtils.
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
    def __init__(self, ):
        """public org.apache.commons.lang3.StringEscapeUtils()"""
        val = __StringEscapeUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def escapeJson(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeJson(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.escapeJson(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def escapeJava(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeJava(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.escapeJava(arg0))

    @staticmethod
    @overload
    def unescapeHtml4(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeHtml4(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.unescapeHtml4(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.StringEscapeUtils()"""
        val = __StringEscapeUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def unescapeHtml3(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeHtml3(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.unescapeHtml3(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def unescapeJava(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeJava(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.unescapeJava(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def escapeCsv(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeCsv(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.escapeCsv(arg0))

    @staticmethod
    @overload
    def unescapeCsv(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeCsv(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.unescapeCsv(arg0))

    @staticmethod
    @overload
    def escapeHtml3(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeHtml3(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.escapeHtml3(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def escapeXml11(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeXml11(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.escapeXml11(arg0))

    @staticmethod
    @overload
    def escapeHtml4(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeHtml4(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.escapeHtml4(arg0))

    @staticmethod
    @overload
    def escapeXml(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeXml(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.escapeXml(arg0))

    @staticmethod
    @overload
    def unescapeEcmaScript(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeEcmaScript(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.unescapeEcmaScript(arg0))

    @staticmethod
    @overload
    def unescapeJson(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeJson(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.unescapeJson(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def unescapeXml(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeXml(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.unescapeXml(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def escapeEcmaScript(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeEcmaScript(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.escapeEcmaScript(arg0))

    @staticmethod
    @overload
    def escapeXml10(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeXml10(java.lang.String)"""
        return str.__wrap(__StringEscapeUtils.escapeXml10(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.lang3.AnnotationUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.AnnotationUtils as __AnnotationUtils
__AnnotationUtils = __AnnotationUtils
import java.lang.annotation.Annotation as Annotation
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
 
class AnnotationUtils():
    """org.apache.commons.lang3.AnnotationUtils"""
 
    @staticmethod
    def __wrap(java_value: __AnnotationUtils) -> 'AnnotationUtils':
        return AnnotationUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AnnotationUtils):
        """
        Dynamic initializer for AnnotationUtils.
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
    def hashCode(arg0: 'Annotation') -> int:
        """public static int org.apache.commons.lang3.AnnotationUtils.hashCode(java.lang.annotation.Annotation)"""
        return int.__wrap(__AnnotationUtils.hashCode(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.AnnotationUtils()"""
        val = __AnnotationUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def isValidAnnotationMemberType(arg0: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.AnnotationUtils.isValidAnnotationMemberType(java.lang.Class<?>)"""
        return bool.__wrap(__AnnotationUtils.isValidAnnotationMemberType(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.AnnotationUtils()"""
        val = __AnnotationUtils()
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

    @staticmethod
    @overload
    def equals(arg0: 'Annotation', arg1: 'Annotation') -> bool:
        """public static boolean org.apache.commons.lang3.AnnotationUtils.equals(java.lang.annotation.Annotation,java.lang.annotation.Annotation)"""
        return bool.__wrap(__AnnotationUtils.equals(arg0, arg1))

    @staticmethod
    @overload
    def toString(arg0: 'Annotation') -> str:
        """public static java.lang.String org.apache.commons.lang3.AnnotationUtils.toString(java.lang.annotation.Annotation)"""
        return str.__wrap(__AnnotationUtils.toString(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.RandomUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import org.apache.commons.lang3.RandomUtils as __RandomUtils
__RandomUtils = __RandomUtils
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RandomUtils():
    """org.apache.commons.lang3.RandomUtils"""
 
    @staticmethod
    def __wrap(java_value: __RandomUtils) -> 'RandomUtils':
        return RandomUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RandomUtils):
        """
        Dynamic initializer for RandomUtils.
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
    def __init__(self):
        """public org.apache.commons.lang3.RandomUtils()"""
        val = __RandomUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def nextDouble() -> float:
        """public static double org.apache.commons.lang3.RandomUtils.nextDouble()"""
        return float.__wrap(__RandomUtils.nextDouble())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.RandomUtils()"""
        val = __RandomUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nextLong(arg0: int, arg1: int) -> int:
        """public static long org.apache.commons.lang3.RandomUtils.nextLong(long,long)"""
        return int.__wrap(__RandomUtils.nextLong(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nextFloat(arg0: float, arg1: float) -> float:
        """public static float org.apache.commons.lang3.RandomUtils.nextFloat(float,float)"""
        return float.__wrap(__RandomUtils.nextFloat(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nextLong() -> int:
        """public static long org.apache.commons.lang3.RandomUtils.nextLong()"""
        return int.__wrap(__RandomUtils.nextLong())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nextBytes(arg0: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.RandomUtils.nextBytes(int)"""
        return List[int].__wrap(__RandomUtils.nextBytes(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nextBoolean() -> bool:
        """public static boolean org.apache.commons.lang3.RandomUtils.nextBoolean()"""
        return bool.__wrap(__RandomUtils.nextBoolean())

    @staticmethod
    @overload
    def nextInt(arg0: int, arg1: int) -> int:
        """public static int org.apache.commons.lang3.RandomUtils.nextInt(int,int)"""
        return int.__wrap(__RandomUtils.nextInt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nextFloat() -> float:
        """public static float org.apache.commons.lang3.RandomUtils.nextFloat()"""
        return float.__wrap(__RandomUtils.nextFloat())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nextInt() -> int:
        """public static int org.apache.commons.lang3.RandomUtils.nextInt()"""
        return int.__wrap(__RandomUtils.nextInt())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nextDouble(arg0: float, arg1: float) -> float:
        """public static double org.apache.commons.lang3.RandomUtils.nextDouble(double,double)"""
        return float.__wrap(__RandomUtils.nextDouble(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.RegExUtils
import java.util.regex.Pattern as __Pattern
__Pattern = __Pattern
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.regex.Matcher as __Matcher
__Matcher = __Matcher
import java.util.regex.Matcher as Matcher
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.commons.lang3.RegExUtils as __RegExUtils
__RegExUtils = __RegExUtils
import java.lang.Object as __Object
__Object = __Object
import java.util.regex.Pattern as Pattern
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RegExUtils():
    """org.apache.commons.lang3.RegExUtils"""
 
    @staticmethod
    def __wrap(java_value: __RegExUtils) -> 'RegExUtils':
        return RegExUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegExUtils):
        """
        Dynamic initializer for RegExUtils.
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
    def replaceAll(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.replaceAll(java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__RegExUtils.replaceAll(arg0, arg1, arg2))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.RegExUtils()"""
        val = __RegExUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def removeFirst(arg0: str, arg1: 'Pattern') -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.removeFirst(java.lang.String,java.util.regex.Pattern)"""
        return str.__wrap(__RegExUtils.removeFirst(arg0, arg1))

    @staticmethod
    @overload
    def dotAllMatcher(arg0: str, arg1: str) -> 'Matcher':
        """public static java.util.regex.Matcher org.apache.commons.lang3.RegExUtils.dotAllMatcher(java.lang.String,java.lang.String)"""
        return Matcher.__wrap(__RegExUtils.dotAllMatcher(arg0, arg1))

    @staticmethod
    @overload
    def removePattern(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.removePattern(java.lang.String,java.lang.String)"""
        return str.__wrap(__RegExUtils.removePattern(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def replaceAll(arg0: str, arg1: 'Pattern', arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.replaceAll(java.lang.String,java.util.regex.Pattern,java.lang.String)"""
        return str.__wrap(__RegExUtils.replaceAll(arg0, arg1, arg2))

    @staticmethod
    @overload
    def removeAll(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.removeAll(java.lang.String,java.lang.String)"""
        return str.__wrap(__RegExUtils.removeAll(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.RegExUtils()"""
        val = __RegExUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def replacePattern(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.replacePattern(java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__RegExUtils.replacePattern(arg0, arg1, arg2))

    @staticmethod
    @overload
    def removeFirst(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.removeFirst(java.lang.String,java.lang.String)"""
        return str.__wrap(__RegExUtils.removeFirst(arg0, arg1))

    @staticmethod
    @overload
    def dotAll(arg0: str) -> 'Pattern':
        """public static java.util.regex.Pattern org.apache.commons.lang3.RegExUtils.dotAll(java.lang.String)"""
        return Pattern.__wrap(__RegExUtils.dotAll(arg0))

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
    def removeAll(arg0: str, arg1: 'Pattern') -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.removeAll(java.lang.String,java.util.regex.Pattern)"""
        return str.__wrap(__RegExUtils.removeAll(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def replaceFirst(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.replaceFirst(java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__RegExUtils.replaceFirst(arg0, arg1, arg2))

    @staticmethod
    @overload
    def replaceFirst(arg0: str, arg1: 'Pattern', arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.replaceFirst(java.lang.String,java.util.regex.Pattern,java.lang.String)"""
        return str.__wrap(__RegExUtils.replaceFirst(arg0, arg1, arg2))

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
 
 
# CLASS: org.apache.commons.lang3.CharUtils
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.CharUtils as __CharUtils
__CharUtils = __CharUtils
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Character as __Character
__Character = __Character
import java.lang.Object as __Object
__Object = __Object
import java.lang.Character as Character
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CharUtils():
    """org.apache.commons.lang3.CharUtils"""
 
    @staticmethod
    def __wrap(java_value: __CharUtils) -> 'CharUtils':
        return CharUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharUtils):
        """
        Dynamic initializer for CharUtils.
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
    def toChar(arg0: str, arg1: str) -> str:
        """public static char org.apache.commons.lang3.CharUtils.toChar(java.lang.String,char)"""
        return str.__wrap(__CharUtils.toChar(arg0, __char.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def toString(arg0: 'Character') -> str:
        """public static java.lang.String org.apache.commons.lang3.CharUtils.toString(java.lang.Character)"""
        return str.__wrap(__CharUtils.toString(arg0))

    @staticmethod
    @overload
    def isAsciiPrintable(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiPrintable(char)"""
        return bool.__wrap(__CharUtils.isAsciiPrintable(__char.valueOf(arg0)))

    @staticmethod
    @overload
    def isAsciiAlphanumeric(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiAlphanumeric(char)"""
        return bool.__wrap(__CharUtils.isAsciiAlphanumeric(__char.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def toString(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.CharUtils.toString(char)"""
        return str.__wrap(__CharUtils.toString(__char.valueOf(arg0)))

    @staticmethod
    @overload
    def isAsciiAlphaUpper(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiAlphaUpper(char)"""
        return bool.__wrap(__CharUtils.isAsciiAlphaUpper(__char.valueOf(arg0)))

    @staticmethod
    @overload
    def toIntValue(arg0: str) -> int:
        """public static int org.apache.commons.lang3.CharUtils.toIntValue(char)"""
        return int.__wrap(__CharUtils.toIntValue(__char.valueOf(arg0)))

    @staticmethod
    @overload
    def unicodeEscaped(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.CharUtils.unicodeEscaped(char)"""
        return str.__wrap(__CharUtils.unicodeEscaped(__char.valueOf(arg0)))

    @staticmethod
    @overload
    def isAscii(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAscii(char)"""
        return bool.__wrap(__CharUtils.isAscii(__char.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isAsciiAlpha(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiAlpha(char)"""
        return bool.__wrap(__CharUtils.isAsciiAlpha(__char.valueOf(arg0)))

    @staticmethod
    @overload
    def unicodeEscaped(arg0: 'Character') -> str:
        """public static java.lang.String org.apache.commons.lang3.CharUtils.unicodeEscaped(java.lang.Character)"""
        return str.__wrap(__CharUtils.unicodeEscaped(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def toIntValue(arg0: str, arg1: int) -> int:
        """public static int org.apache.commons.lang3.CharUtils.toIntValue(char,int)"""
        return int.__wrap(__CharUtils.toIntValue(__char.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def isAsciiAlphaLower(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiAlphaLower(char)"""
        return bool.__wrap(__CharUtils.isAsciiAlphaLower(__char.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def toChar(arg0: 'Character', arg1: str) -> str:
        """public static char org.apache.commons.lang3.CharUtils.toChar(java.lang.Character,char)"""
        return str.__wrap(__CharUtils.toChar(arg0, __char.valueOf(arg1)))

    @staticmethod
    @overload
    def toChar(arg0: str) -> str:
        """public static char org.apache.commons.lang3.CharUtils.toChar(java.lang.String)"""
        return str.__wrap(__CharUtils.toChar(arg0))

    @staticmethod
    @overload
    def isAsciiNumeric(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiNumeric(char)"""
        return bool.__wrap(__CharUtils.isAsciiNumeric(__char.valueOf(arg0)))

    @staticmethod
    @overload
    def toCharacterObject(arg0: str) -> 'Character':
        """public static java.lang.Character org.apache.commons.lang3.CharUtils.toCharacterObject(java.lang.String)"""
        return Character.__wrap(__CharUtils.toCharacterObject(arg0))

    @staticmethod
    @overload
    def isAsciiControl(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiControl(char)"""
        return bool.__wrap(__CharUtils.isAsciiControl(__char.valueOf(arg0)))

    @staticmethod
    @overload
    def toIntValue(arg0: 'Character') -> int:
        """public static int org.apache.commons.lang3.CharUtils.toIntValue(java.lang.Character)"""
        return int.__wrap(__CharUtils.toIntValue(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.CharUtils()"""
        val = __CharUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def toChar(arg0: 'Character') -> str:
        """public static char org.apache.commons.lang3.CharUtils.toChar(java.lang.Character)"""
        return str.__wrap(__CharUtils.toChar(arg0))

    @staticmethod
    @overload
    def toIntValue(arg0: 'Character', arg1: int) -> int:
        """public static int org.apache.commons.lang3.CharUtils.toIntValue(java.lang.Character,int)"""
        return int.__wrap(__CharUtils.toIntValue(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def compare(arg0: str, arg1: str) -> int:
        """public static int org.apache.commons.lang3.CharUtils.compare(char,char)"""
        return int.__wrap(__CharUtils.compare(__char.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.CharUtils()"""
        val = __CharUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toCharacterObject(arg0: str) -> 'Character':
        """public static java.lang.Character org.apache.commons.lang3.CharUtils.toCharacterObject(char)"""
        return Character.__wrap(__CharUtils.toCharacterObject(__char.valueOf(arg0))) 
 
 
# CLASS: org.apache.commons.lang3.SystemProperties
import org.apache.commons.lang3.SystemProperties as __SystemProperties
__SystemProperties = __SystemProperties
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.function.BooleanSupplier as BooleanSupplier
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.function.IntSupplier as IntSupplier
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.function.LongSupplier as LongSupplier
 
class SystemProperties():
    """org.apache.commons.lang3.SystemProperties"""
 
    @staticmethod
    def __wrap(java_value: __SystemProperties) -> 'SystemProperties':
        return SystemProperties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SystemProperties):
        """
        Dynamic initializer for SystemProperties.
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
    def getJavaSpecificationVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaSpecificationVersion()"""
        return str.__wrap(__SystemProperties.getJavaSpecificationVersion())

    @staticmethod
    @overload
    def getOsArch() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getOsArch()"""
        return str.__wrap(__SystemProperties.getOsArch())

    @staticmethod
    @overload
    def getJavaAwtHeadless() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaAwtHeadless()"""
        return str.__wrap(__SystemProperties.getJavaAwtHeadless())

    @staticmethod
    @overload
    def getJavaVmVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmVersion()"""
        return str.__wrap(__SystemProperties.getJavaVmVersion())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getJavaEndorsedDirs() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaEndorsedDirs()"""
        return str.__wrap(__SystemProperties.getJavaEndorsedDirs())

    @staticmethod
    @overload
    def getProperty(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getProperty(java.lang.String)"""
        return str.__wrap(__SystemProperties.getProperty(arg0))

    @staticmethod
    @overload
    def getJavaVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVersion()"""
        return str.__wrap(__SystemProperties.getJavaVersion())

    @staticmethod
    @overload
    def getJavaClassVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaClassVersion()"""
        return str.__wrap(__SystemProperties.getJavaClassVersion())

    @staticmethod
    @overload
    def getOsName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getOsName()"""
        return str.__wrap(__SystemProperties.getOsName())

    @staticmethod
    @overload
    def getLong(arg0: str, arg1: 'LongSupplier') -> int:
        """public static long org.apache.commons.lang3.SystemProperties.getLong(java.lang.String,java.util.function.LongSupplier)"""
        return int.__wrap(__SystemProperties.getLong(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getJavaClassPath() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaClassPath()"""
        return str.__wrap(__SystemProperties.getJavaClassPath())

    @staticmethod
    @overload
    def getJavaVmSpecificationVendor() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmSpecificationVendor()"""
        return str.__wrap(__SystemProperties.getJavaVmSpecificationVendor())

    @staticmethod
    @overload
    def getUserLanguage() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getUserLanguage()"""
        return str.__wrap(__SystemProperties.getUserLanguage())

    @staticmethod
    @overload
    def getJavaAwtGraphicsenv() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaAwtGraphicsenv()"""
        return str.__wrap(__SystemProperties.getJavaAwtGraphicsenv())

    @staticmethod
    @overload
    def getJavaVendor() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVendor()"""
        return str.__wrap(__SystemProperties.getJavaVendor())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def getUserTimezone() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getUserTimezone()"""
        return str.__wrap(__SystemProperties.getUserTimezone())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getFileSeparator() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getFileSeparator()"""
        return str.__wrap(__SystemProperties.getFileSeparator())

    @staticmethod
    @overload
    def getJavaVmVendor() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmVendor()"""
        return str.__wrap(__SystemProperties.getJavaVmVendor())

    @staticmethod
    @overload
    def getOsVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getOsVersion()"""
        return str.__wrap(__SystemProperties.getOsVersion())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.SystemProperties()"""
        val = __SystemProperties()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getJavaSpecificationName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaSpecificationName()"""
        return str.__wrap(__SystemProperties.getJavaSpecificationName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getLineSeparator() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getLineSeparator()"""
        return str.__wrap(__SystemProperties.getLineSeparator())

    @staticmethod
    @overload
    def getJavaHome() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaHome()"""
        return str.__wrap(__SystemProperties.getJavaHome())

    @staticmethod
    @overload
    def getUserHome() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getUserHome()"""
        return str.__wrap(__SystemProperties.getUserHome())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getJavaVendorUrl() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVendorUrl()"""
        return str.__wrap(__SystemProperties.getJavaVendorUrl())

    @staticmethod
    @overload
    def getJavaVmSpecificationVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmSpecificationVersion()"""
        return str.__wrap(__SystemProperties.getJavaVmSpecificationVersion())

    @staticmethod
    @overload
    def getJavaVmName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmName()"""
        return str.__wrap(__SystemProperties.getJavaVmName())

    @staticmethod
    @overload
    def getJavaVmInfo() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmInfo()"""
        return str.__wrap(__SystemProperties.getJavaVmInfo())

    @staticmethod
    @overload
    def getAwtToolkit() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getAwtToolkit()"""
        return str.__wrap(__SystemProperties.getAwtToolkit())

    @staticmethod
    @overload
    def getUserDir() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getUserDir()"""
        return str.__wrap(__SystemProperties.getUserDir())

    @staticmethod
    @overload
    def getInt(arg0: str, arg1: 'IntSupplier') -> int:
        """public static int org.apache.commons.lang3.SystemProperties.getInt(java.lang.String,java.util.function.IntSupplier)"""
        return int.__wrap(__SystemProperties.getInt(arg0, arg1))

    @staticmethod
    @overload
    def getUserCountry() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getUserCountry()"""
        return str.__wrap(__SystemProperties.getUserCountry())

    @staticmethod
    @overload
    def getFileEncoding() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getFileEncoding()"""
        return str.__wrap(__SystemProperties.getFileEncoding())

    @staticmethod
    @overload
    def getJavaLibraryPath() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaLibraryPath()"""
        return str.__wrap(__SystemProperties.getJavaLibraryPath())

    @staticmethod
    @overload
    def getJavaVmSpecificationName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmSpecificationName()"""
        return str.__wrap(__SystemProperties.getJavaVmSpecificationName())

    @staticmethod
    @overload
    def getBoolean(arg0: str, arg1: 'BooleanSupplier') -> bool:
        """public static boolean org.apache.commons.lang3.SystemProperties.getBoolean(java.lang.String,java.util.function.BooleanSupplier)"""
        return bool.__wrap(__SystemProperties.getBoolean(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getJavaIoTmpdir() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaIoTmpdir()"""
        return str.__wrap(__SystemProperties.getJavaIoTmpdir())

    @staticmethod
    @overload
    def getJavaUtilPrefsPreferencesFactory() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaUtilPrefsPreferencesFactory()"""
        return str.__wrap(__SystemProperties.getJavaUtilPrefsPreferencesFactory())

    @staticmethod
    @overload
    def getJavaExtDirs() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaExtDirs()"""
        return str.__wrap(__SystemProperties.getJavaExtDirs())

    @staticmethod
    @overload
    def getJavaRuntimeName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaRuntimeName()"""
        return str.__wrap(__SystemProperties.getJavaRuntimeName())

    @staticmethod
    @overload
    def getJavaCompiler() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaCompiler()"""
        return str.__wrap(__SystemProperties.getJavaCompiler())

    @staticmethod
    @overload
    def getUserName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getUserName()"""
        return str.__wrap(__SystemProperties.getUserName())

    @staticmethod
    @overload
    def getJavaAwtPrinterjob() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaAwtPrinterjob()"""
        return str.__wrap(__SystemProperties.getJavaAwtPrinterjob())

    @staticmethod
    @overload
    def getPathSeparator() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getPathSeparator()"""
        return str.__wrap(__SystemProperties.getPathSeparator())

    @staticmethod
    @overload
    def getJavaRuntimeVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaRuntimeVersion()"""
        return str.__wrap(__SystemProperties.getJavaRuntimeVersion())

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
    def __init__(self, ):
        """public org.apache.commons.lang3.SystemProperties()"""
        val = __SystemProperties()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getJavaAwtFonts() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaAwtFonts()"""
        return str.__wrap(__SystemProperties.getJavaAwtFonts())

    @staticmethod
    @overload
    def getJavaLocaleProviders() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaLocaleProviders()"""
        return str.__wrap(__SystemProperties.getJavaLocaleProviders())

    @staticmethod
    @overload
    def getJavaSpecificationVendor() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaSpecificationVendor()"""
        return str.__wrap(__SystemProperties.getJavaSpecificationVendor()) 
 
 
# CLASS: org.apache.commons.lang3.NumberRange
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.lang3.NumberRange as __NumberRange
__NumberRange = __NumberRange
from builtins import type
import org.apache.commons.lang3.Range as __Range
__Range = __Range
import java.lang.Comparable as Comparable
from builtins import object
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
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
 
class NumberRange():
    """org.apache.commons.lang3.NumberRange"""
 
    @staticmethod
    def __wrap(java_value: __NumberRange) -> 'NumberRange':
        return NumberRange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NumberRange):
        """
        Dynamic initializer for NumberRange.
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
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T)"""
        return Range.__wrap(__Range.between(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isAfter(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfter(T)"""
        return bool.__wrap(super(__Range, self).isAfter(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.contains(T)"""
        return bool.__wrap(super(__Range, self).contains(arg0))

    @override
    @overload
    def isNaturalOrdering(self) -> bool:
        """public boolean org.apache.commons.lang3.Range.isNaturalOrdering()"""
        return bool.__wrap(super(Range, self).isNaturalOrdering())

    @staticmethod
    @overload
    def is(arg0: object, arg1: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.is(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.equals(java.lang.Object)"""
        return bool.__wrap(super(__Range, self).equals(arg0))

    @overload
    def isStartedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isStartedBy(T)"""
        return bool.__wrap(super(__Range, self).isStartedBy(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.Range.hashCode()"""
        return int.__wrap(super(Range, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString()"""
        return str.__wrap(super(Range, self).toString())

    @overload
    def isBefore(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isBefore(T)"""
        return bool.__wrap(super(__Range, self).isBefore(arg0))

    @overload
    def intersectionWith(self, arg0: 'Range') -> 'Range':
        """public org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.intersectionWith(org.apache.commons.lang3.Range<T>)"""
        return 'Range'.__wrap(super(__Range, self).intersectionWith(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T)"""
        return Range.__wrap(__Range.of(arg0, arg1))

    @overload
    def isAfterRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfterRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isAfterRange(arg0))

    @override
    @overload
    def getMinimum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMinimum()"""
        return object.__wrap(super(Range, self).getMinimum())

    @override
    @overload
    def getComparator(self) -> 'Comparator':
        """public java.util.Comparator<T> org.apache.commons.lang3.Range.getComparator()"""
        return 'Comparator'.__wrap(super(Range, self).getComparator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isEndedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isEndedBy(T)"""
        return bool.__wrap(super(__Range, self).isEndedBy(arg0))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString(java.lang.String)"""
        return str.__wrap(super(__Range, self).toString(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getMaximum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMaximum()"""
        return object.__wrap(super(Range, self).getMaximum())

    @overload
    def isOverlappedBy(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isOverlappedBy(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isOverlappedBy(arg0))

    @overload
    def fit(self, arg0: object) -> object:
        """public T org.apache.commons.lang3.Range.fit(T)"""
        return object.__wrap(super(__Range, self).fit(arg0))

    @overload
    def elementCompareTo(self, arg0: object) -> int:
        """public int org.apache.commons.lang3.Range.elementCompareTo(T)"""
        return int.__wrap(super(__Range, self).elementCompareTo(arg0))

    @overload
    def isBeforeRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isBeforeRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).isBeforeRange(arg0))

    @staticmethod
    @overload
    def is(arg0: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T)"""
        return Range.__wrap(__Range.is(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def between(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T,java.util.Comparator<T>)"""
        return Range.__wrap(__Range.between(arg0, arg1, arg2))

    @overload
    def containsRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.containsRange(org.apache.commons.lang3.Range<T>)"""
        return bool.__wrap(super(__Range, self).containsRange(arg0))

    @overload
    def __init__(self, arg0: 'Number', arg1: 'Number', arg2: 'Comparator'):
        """public org.apache.commons.lang3.NumberRange(N,N,java.util.Comparator<N>)"""
        val = __NumberRange(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.LocaleUtils
import java.util.Locale as Locale
from builtins import str
import org.apache.commons.lang3.LocaleUtils as __LocaleUtils
__LocaleUtils = __LocaleUtils
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.List as __List
__List = __List
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Locale as __Locale
__Locale = __Locale
from builtins import bool
import java.util.List as List
from builtins import int
 
class LocaleUtils():
    """org.apache.commons.lang3.LocaleUtils"""
 
    @staticmethod
    def __wrap(java_value: __LocaleUtils) -> 'LocaleUtils':
        return LocaleUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LocaleUtils):
        """
        Dynamic initializer for LocaleUtils.
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
    def __init__(self):
        """public org.apache.commons.lang3.LocaleUtils()"""
        val = __LocaleUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def localeLookupList(arg0: 'Locale', arg1: 'Locale') -> 'List':
        """public static java.util.List<java.util.Locale> org.apache.commons.lang3.LocaleUtils.localeLookupList(java.util.Locale,java.util.Locale)"""
        return List.__wrap(__LocaleUtils.localeLookupList(arg0, arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.LocaleUtils()"""
        val = __LocaleUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def languagesByCountry(arg0: str) -> 'List':
        """public static java.util.List<java.util.Locale> org.apache.commons.lang3.LocaleUtils.languagesByCountry(java.lang.String)"""
        return List.__wrap(__LocaleUtils.languagesByCountry(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def toLocale(arg0: 'Locale') -> 'Locale':
        """public static java.util.Locale org.apache.commons.lang3.LocaleUtils.toLocale(java.util.Locale)"""
        return Locale.__wrap(__LocaleUtils.toLocale(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def localeLookupList(arg0: 'Locale') -> 'List':
        """public static java.util.List<java.util.Locale> org.apache.commons.lang3.LocaleUtils.localeLookupList(java.util.Locale)"""
        return List.__wrap(__LocaleUtils.localeLookupList(arg0))

    @staticmethod
    @overload
    def countriesByLanguage(arg0: str) -> 'List':
        """public static java.util.List<java.util.Locale> org.apache.commons.lang3.LocaleUtils.countriesByLanguage(java.lang.String)"""
        return List.__wrap(__LocaleUtils.countriesByLanguage(arg0))

    @staticmethod
    @overload
    def availableLocaleList() -> 'List':
        """public static java.util.List<java.util.Locale> org.apache.commons.lang3.LocaleUtils.availableLocaleList()"""
        return List.__wrap(__LocaleUtils.availableLocaleList())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isAvailableLocale(arg0: 'Locale') -> bool:
        """public static boolean org.apache.commons.lang3.LocaleUtils.isAvailableLocale(java.util.Locale)"""
        return bool.__wrap(__LocaleUtils.isAvailableLocale(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def toLocale(arg0: str) -> 'Locale':
        """public static java.util.Locale org.apache.commons.lang3.LocaleUtils.toLocale(java.lang.String)"""
        return Locale.__wrap(__LocaleUtils.toLocale(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def availableLocaleSet() -> 'Set':
        """public static java.util.Set<java.util.Locale> org.apache.commons.lang3.LocaleUtils.availableLocaleSet()"""
        return Set.__wrap(__LocaleUtils.availableLocaleSet())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.ThreadUtils$ThreadGroupPredicate
import java.lang.ThreadGroup as ThreadGroup
from abc import abstractmethod, ABC
import org.apache.commons.lang3.ThreadUtils as __ThreadUtils_ThreadGroupPredicate
__ThreadGroupPredicate = __ThreadUtils_ThreadGroupPredicate.ThreadGroupPredicate
 
class ThreadGroupPredicate(ABC):
    """org.apache.commons.lang3.ThreadUtils.ThreadGroupPredicate"""
 
    @staticmethod
    def __wrap(java_value: __ThreadGroupPredicate) -> 'ThreadGroupPredicate':
        return ThreadGroupPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadGroupPredicate):
        """
        Dynamic initializer for ThreadGroupPredicate.
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
    def test(self, arg0: 'ThreadGroup'):
        """public abstract boolean org.apache.commons.lang3.ThreadUtils$ThreadGroupPredicate.test(java.lang.ThreadGroup)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.Functions
import java.util.function.Predicate as Predicate
import java.util.function.Supplier as Supplier
import org.apache.commons.lang3.Streams as __Streams_FailableStream
__FailableStream = __Streams_FailableStream.FailableStream
from builtins import type
import java.util.Collection as Collection
import java.lang.Runnable as __Runnable
__Runnable = __Runnable
import java.util.function.Consumer as Consumer
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiFunction as __BiFunction
__BiFunction = __BiFunction
import java.lang.RuntimeException as RuntimeException
import java.util.function.Supplier as __Supplier
__Supplier = __Supplier
import java.util.concurrent.Callable as Callable
from builtins import bool
import org.apache.commons.lang3.Functions as __Functions
__Functions = __Functions
import java.util.function.Consumer as __Consumer
__Consumer = __Consumer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Runnable as Runnable
import java.util.function.BiPredicate as __BiPredicate
__BiPredicate = __BiPredicate
import java.util.function.Predicate as __Predicate
__Predicate = __Predicate
import java.util.function.Function as __Function
__Function = __Function
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.lang.RuntimeException as __RuntimeException
__RuntimeException = __RuntimeException
import java.util.concurrent.Callable as __Callable
__Callable = __Callable
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.util.function.BiPredicate as BiPredicate
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Throwable as Throwable
import java.util.function.Function as Function
import java.util.function.BiConsumer as __BiConsumer
__BiConsumer = __BiConsumer
import java.lang.Integer as __int
from builtins import int
 
class Functions():
    """org.apache.commons.lang3.Functions"""
 
    @staticmethod
    def __wrap(java_value: __Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Functions):
        """
        Dynamic initializer for Functions.
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
    def get(arg0: 'FailableSupplier') -> object:
        """public static <O,T extends java.lang.Throwable> O org.apache.commons.lang3.Functions.get(org.apache.commons.lang3.Functions$FailableSupplier<O, T>)"""
        return object.__wrap(__Functions.get(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def stream(arg0: 'Collection') -> 'FailableStream':
        """public static <O> org.apache.commons.lang3.Streams$FailableStream<O> org.apache.commons.lang3.Functions.stream(java.util.Collection<O>)"""
        return FailableStream.__wrap(__Functions.stream(arg0))

    @staticmethod
    @overload
    def asBiPredicate(arg0: 'FailableBiPredicate') -> 'BiPredicate':
        """public static <O1,O2> java.util.function.BiPredicate<O1, O2> org.apache.commons.lang3.Functions.asBiPredicate(org.apache.commons.lang3.Functions$FailableBiPredicate<O1, O2, ?>)"""
        return BiPredicate.__wrap(__Functions.asBiPredicate(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def rethrow(arg0: 'Throwable') -> 'RuntimeException':
        """public static java.lang.RuntimeException org.apache.commons.lang3.Functions.rethrow(java.lang.Throwable)"""
        return RuntimeException.__wrap(__Functions.rethrow(arg0))

    @staticmethod
    @overload
    def accept(arg0: 'FailableBiConsumer', arg1: object, arg2: object):
        """public static <O1,O2,T extends java.lang.Throwable> void org.apache.commons.lang3.Functions.accept(org.apache.commons.lang3.Functions$FailableBiConsumer<O1, O2, T>,O1,O2)"""
        __Functions.accept(arg0, arg1, arg2)

    @staticmethod
    @overload
    def tryWithResources(arg0: 'FailableRunnable', arg1: 'FailableConsumer', *arg2: 'FailableRunnable'):
        """public static void org.apache.commons.lang3.Functions.tryWithResources(org.apache.commons.lang3.Functions$FailableRunnable<? extends java.lang.Throwable>,org.apache.commons.lang3.Functions$FailableConsumer<java.lang.Throwable, ? extends java.lang.Throwable>,org.apache.commons.lang3.Functions$FailableRunnable<? extends java.lang.Throwable>...)"""
        __Functions.tryWithResources(arg0, arg1, arg2)

    @staticmethod
    @overload
    def asFunction(arg0: 'FailableFunction') -> 'Function':
        """public static <I,O> java.util.function.Function<I, O> org.apache.commons.lang3.Functions.asFunction(org.apache.commons.lang3.Functions$FailableFunction<I, O, ?>)"""
        return Function.__wrap(__Functions.asFunction(arg0))

    @staticmethod
    @overload
    def apply(arg0: 'FailableFunction', arg1: object) -> object:
        """public static <I,O,T extends java.lang.Throwable> O org.apache.commons.lang3.Functions.apply(org.apache.commons.lang3.Functions$FailableFunction<I, O, T>,I)"""
        return object.__wrap(__Functions.apply(arg0, arg1))

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
    def run(arg0: 'FailableRunnable'):
        """public static <T extends java.lang.Throwable> void org.apache.commons.lang3.Functions.run(org.apache.commons.lang3.Functions$FailableRunnable<T>)"""
        __Functions.run(arg0)

    @staticmethod
    @overload
    def asCallable(arg0: 'FailableCallable') -> 'Callable':
        """public static <O> java.util.concurrent.Callable<O> org.apache.commons.lang3.Functions.asCallable(org.apache.commons.lang3.Functions$FailableCallable<O, ?>)"""
        return Callable.__wrap(__Functions.asCallable(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.Functions()"""
        val = __Functions()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def asConsumer(arg0: 'FailableConsumer') -> 'Consumer':
        """public static <I> java.util.function.Consumer<I> org.apache.commons.lang3.Functions.asConsumer(org.apache.commons.lang3.Functions$FailableConsumer<I, ?>)"""
        return Consumer.__wrap(__Functions.asConsumer(arg0))

    @staticmethod
    @overload
    def accept(arg0: 'FailableConsumer', arg1: object):
        """public static <O,T extends java.lang.Throwable> void org.apache.commons.lang3.Functions.accept(org.apache.commons.lang3.Functions$FailableConsumer<O, T>,O)"""
        __Functions.accept(arg0, arg1)

    @staticmethod
    @overload
    def asSupplier(arg0: 'FailableSupplier') -> 'Supplier':
        """public static <O> java.util.function.Supplier<O> org.apache.commons.lang3.Functions.asSupplier(org.apache.commons.lang3.Functions$FailableSupplier<O, ?>)"""
        return Supplier.__wrap(__Functions.asSupplier(arg0))

    @staticmethod
    @overload
    def apply(arg0: 'FailableBiFunction', arg1: object, arg2: object) -> object:
        """public static <O1,O2,O,T extends java.lang.Throwable> O org.apache.commons.lang3.Functions.apply(org.apache.commons.lang3.Functions$FailableBiFunction<O1, O2, O, T>,O1,O2)"""
        return object.__wrap(__Functions.apply(arg0, arg1, arg2))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.Functions()"""
        val = __Functions()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def test(arg0: 'FailablePredicate', arg1: object) -> bool:
        """public static <O,T extends java.lang.Throwable> boolean org.apache.commons.lang3.Functions.test(org.apache.commons.lang3.Functions$FailablePredicate<O, T>,O)"""
        return bool.__wrap(__Functions.test(arg0, arg1))

    @staticmethod
    @overload
    def tryWithResources(arg0: 'FailableRunnable', *arg1: 'FailableRunnable'):
        """public static void org.apache.commons.lang3.Functions.tryWithResources(org.apache.commons.lang3.Functions$FailableRunnable<? extends java.lang.Throwable>,org.apache.commons.lang3.Functions$FailableRunnable<? extends java.lang.Throwable>...)"""
        __Functions.tryWithResources(arg0, arg1)

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
    def stream(arg0: 'Stream') -> 'FailableStream':
        """public static <O> org.apache.commons.lang3.Streams$FailableStream<O> org.apache.commons.lang3.Functions.stream(java.util.stream.Stream<O>)"""
        return FailableStream.__wrap(__Functions.stream(arg0))

    @staticmethod
    @overload
    def asPredicate(arg0: 'FailablePredicate') -> 'Predicate':
        """public static <I> java.util.function.Predicate<I> org.apache.commons.lang3.Functions.asPredicate(org.apache.commons.lang3.Functions$FailablePredicate<I, ?>)"""
        return Predicate.__wrap(__Functions.asPredicate(arg0))

    @staticmethod
    @overload
    def asBiFunction(arg0: 'FailableBiFunction') -> 'BiFunction':
        """public static <O1,O2,O> java.util.function.BiFunction<O1, O2, O> org.apache.commons.lang3.Functions.asBiFunction(org.apache.commons.lang3.Functions$FailableBiFunction<O1, O2, O, ?>)"""
        return BiFunction.__wrap(__Functions.asBiFunction(arg0))

    @staticmethod
    @overload
    def asBiConsumer(arg0: 'FailableBiConsumer') -> 'BiConsumer':
        """public static <O1,O2> java.util.function.BiConsumer<O1, O2> org.apache.commons.lang3.Functions.asBiConsumer(org.apache.commons.lang3.Functions$FailableBiConsumer<O1, O2, ?>)"""
        return BiConsumer.__wrap(__Functions.asBiConsumer(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def call(arg0: 'FailableCallable') -> object:
        """public static <O,T extends java.lang.Throwable> O org.apache.commons.lang3.Functions.call(org.apache.commons.lang3.Functions$FailableCallable<O, T>)"""
        return object.__wrap(__Functions.call(arg0))

    @staticmethod
    @overload
    def test(arg0: 'FailableBiPredicate', arg1: object, arg2: object) -> bool:
        """public static <O1,O2,T extends java.lang.Throwable> boolean org.apache.commons.lang3.Functions.test(org.apache.commons.lang3.Functions$FailableBiPredicate<O1, O2, T>,O1,O2)"""
        return bool.__wrap(__Functions.test(arg0, arg1, arg2))

    @staticmethod
    @overload
    def asRunnable(arg0: 'FailableRunnable') -> 'Runnable':
        """public static java.lang.Runnable org.apache.commons.lang3.Functions.asRunnable(org.apache.commons.lang3.Functions$FailableRunnable<?>)"""
        return Runnable.__wrap(__Functions.asRunnable(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.ArchUtils
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import org.apache.commons.lang3.arch.Processor as __Processor
__Processor = __Processor
import java.lang.String as __String
__String = __String
import org.apache.commons.lang3.ArchUtils as __ArchUtils
__ArchUtils = __ArchUtils
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyapache.lang3 import arch
except ImportError:
    arch = __import_once__("pyapache.lang3.arch")

from builtins import bool
from builtins import int
 
class ArchUtils():
    """org.apache.commons.lang3.ArchUtils"""
 
    @staticmethod
    def __wrap(java_value: __ArchUtils) -> 'ArchUtils':
        return ArchUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArchUtils):
        """
        Dynamic initializer for ArchUtils.
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

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ArchUtils()"""
        val = __ArchUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getProcessor(arg0: str) -> 'arch.Processor':
        """public static org.apache.commons.lang3.arch.Processor org.apache.commons.lang3.ArchUtils.getProcessor(java.lang.String)"""
        return arch.Processor.__wrap(__ArchUtils.getProcessor(arg0))

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getProcessor() -> 'arch.Processor':
        """public static org.apache.commons.lang3.arch.Processor org.apache.commons.lang3.ArchUtils.getProcessor()"""
        return arch.Processor.__wrap(__ArchUtils.getProcessor())

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
    def __init__(self):
        """public org.apache.commons.lang3.ArchUtils()"""
        val = __ArchUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.CharSequenceUtils
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.CharSequenceUtils as __CharSequenceUtils
__CharSequenceUtils = __CharSequenceUtils
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CharSequenceUtils():
    """org.apache.commons.lang3.CharSequenceUtils"""
 
    @staticmethod
    def __wrap(java_value: __CharSequenceUtils) -> 'CharSequenceUtils':
        return CharSequenceUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharSequenceUtils):
        """
        Dynamic initializer for CharSequenceUtils.
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

    @staticmethod
    @overload
    def toCharArray(arg0: 'CharSequence') -> List[str]:
        """public static char[] org.apache.commons.lang3.CharSequenceUtils.toCharArray(java.lang.CharSequence)"""
        return List[str].__wrap(__CharSequenceUtils.toCharArray(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.CharSequenceUtils()"""
        val = __CharSequenceUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def subSequence(arg0: 'CharSequence', arg1: int) -> 'CharSequence':
        """public static java.lang.CharSequence org.apache.commons.lang3.CharSequenceUtils.subSequence(java.lang.CharSequence,int)"""
        return CharSequence.__wrap(__CharSequenceUtils.subSequence(arg0, __int.valueOf(arg1)))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.CharSequenceUtils()"""
        val = __CharSequenceUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.SerializationException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import org.apache.commons.lang3.SerializationException as __SerializationException
__SerializationException = __SerializationException
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
 
class SerializationException():
    """org.apache.commons.lang3.SerializationException"""
 
    @staticmethod
    def __wrap(java_value: __SerializationException) -> 'SerializationException':
        return SerializationException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SerializationException):
        """
        Dynamic initializer for SerializationException.
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

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.SerializationException(java.lang.String)"""
        val = __SerializationException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.SerializationException()"""
        val = __SerializationException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.SerializationException(java.lang.String,java.lang.Throwable)"""
        val = __SerializationException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.SerializationException(java.lang.Throwable)"""
        val = __SerializationException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.SerializationException()"""
        val = __SerializationException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: org.apache.commons.lang3.EnumUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Iterable as Iterable
from typing import List
import java.lang.Enum as Enum
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.EnumSet as EnumSet
import java.util.EnumSet as __EnumSet
__EnumSet = __EnumSet
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.EnumUtils as __EnumUtils
__EnumUtils = __EnumUtils
import java.util.function.Function as Function
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
import java.util.Map as Map
from builtins import bool
from builtins import int
import java.util.List as List
 
class EnumUtils():
    """org.apache.commons.lang3.EnumUtils"""
 
    @staticmethod
    def __wrap(java_value: __EnumUtils) -> 'EnumUtils':
        return EnumUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EnumUtils):
        """
        Dynamic initializer for EnumUtils.
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
    def getEnumIgnoreCase(arg0: 'Class', arg1: str, arg2: 'Enum') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E org.apache.commons.lang3.EnumUtils.getEnumIgnoreCase(java.lang.Class<E>,java.lang.String,E)"""
        return Enum.__wrap(__EnumUtils.getEnumIgnoreCase(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getEnumMap(arg0: 'Class') -> 'Map':
        """public static <E extends java.lang.Enum<E>> java.util.Map<java.lang.String, E> org.apache.commons.lang3.EnumUtils.getEnumMap(java.lang.Class<E>)"""
        return Map.__wrap(__EnumUtils.getEnumMap(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.EnumUtils()"""
        val = __EnumUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def isValidEnumIgnoreCase(arg0: 'Class', arg1: str) -> bool:
        """public static <E extends java.lang.Enum<E>> boolean org.apache.commons.lang3.EnumUtils.isValidEnumIgnoreCase(java.lang.Class<E>,java.lang.String)"""
        return bool.__wrap(__EnumUtils.isValidEnumIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def generateBitVectors(arg0: 'Class', arg1: 'Iterable') -> List[int]:
        """public static <E extends java.lang.Enum<E>> long[] org.apache.commons.lang3.EnumUtils.generateBitVectors(java.lang.Class<E>,java.lang.Iterable<? extends E>)"""
        return List[int].__wrap(__EnumUtils.generateBitVectors(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getEnum(arg0: 'Class', arg1: str, arg2: 'Enum') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E org.apache.commons.lang3.EnumUtils.getEnum(java.lang.Class<E>,java.lang.String,E)"""
        return Enum.__wrap(__EnumUtils.getEnum(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getEnumMap(arg0: 'Class', arg1: 'Function') -> 'Map':
        """public static <E extends java.lang.Enum<E>,K> java.util.Map<K, E> org.apache.commons.lang3.EnumUtils.getEnumMap(java.lang.Class<E>,java.util.function.Function<E, K>)"""
        return Map.__wrap(__EnumUtils.getEnumMap(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def processBitVectors(arg0: 'Class', *arg1: int) -> 'EnumSet':
        """public static <E extends java.lang.Enum<E>> java.util.EnumSet<E> org.apache.commons.lang3.EnumUtils.processBitVectors(java.lang.Class<E>,long...)"""
        return EnumSet.__wrap(__EnumUtils.processBitVectors(arg0, arg1))

    @staticmethod
    @overload
    def generateBitVector(arg0: 'Class', arg1: 'Iterable') -> int:
        """public static <E extends java.lang.Enum<E>> long org.apache.commons.lang3.EnumUtils.generateBitVector(java.lang.Class<E>,java.lang.Iterable<? extends E>)"""
        return int.__wrap(__EnumUtils.generateBitVector(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getEnum(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E org.apache.commons.lang3.EnumUtils.getEnum(java.lang.Class<E>,java.lang.String)"""
        return Enum.__wrap(__EnumUtils.getEnum(arg0, arg1))

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
    def getEnumIgnoreCase(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E org.apache.commons.lang3.EnumUtils.getEnumIgnoreCase(java.lang.Class<E>,java.lang.String)"""
        return Enum.__wrap(__EnumUtils.getEnumIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def generateBitVectors(arg0: 'Class', *arg1: 'Enum') -> List[int]:
        """public static <E extends java.lang.Enum<E>> long[] org.apache.commons.lang3.EnumUtils.generateBitVectors(java.lang.Class<E>,E...)"""
        return List[int].__wrap(__EnumUtils.generateBitVectors(arg0, arg1))

    @staticmethod
    @overload
    def getEnumList(arg0: 'Class') -> 'List':
        """public static <E extends java.lang.Enum<E>> java.util.List<E> org.apache.commons.lang3.EnumUtils.getEnumList(java.lang.Class<E>)"""
        return List.__wrap(__EnumUtils.getEnumList(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def processBitVector(arg0: 'Class', arg1: int) -> 'EnumSet':
        """public static <E extends java.lang.Enum<E>> java.util.EnumSet<E> org.apache.commons.lang3.EnumUtils.processBitVector(java.lang.Class<E>,long)"""
        return EnumSet.__wrap(__EnumUtils.processBitVector(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def generateBitVector(arg0: 'Class', *arg1: 'Enum') -> int:
        """public static <E extends java.lang.Enum<E>> long org.apache.commons.lang3.EnumUtils.generateBitVector(java.lang.Class<E>,E...)"""
        return int.__wrap(__EnumUtils.generateBitVector(arg0, arg1))

    @staticmethod
    @overload
    def getEnumSystemProperty(arg0: 'Class', arg1: str, arg2: 'Enum') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E org.apache.commons.lang3.EnumUtils.getEnumSystemProperty(java.lang.Class<E>,java.lang.String,E)"""
        return Enum.__wrap(__EnumUtils.getEnumSystemProperty(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getFirstEnumIgnoreCase(arg0: 'Class', arg1: str, arg2: 'Function', arg3: 'Enum') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E org.apache.commons.lang3.EnumUtils.getFirstEnumIgnoreCase(java.lang.Class<E>,java.lang.String,java.util.function.Function<E, java.lang.String>,E)"""
        return Enum.__wrap(__EnumUtils.getFirstEnumIgnoreCase(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def isValidEnum(arg0: 'Class', arg1: str) -> bool:
        """public static <E extends java.lang.Enum<E>> boolean org.apache.commons.lang3.EnumUtils.isValidEnum(java.lang.Class<E>,java.lang.String)"""
        return bool.__wrap(__EnumUtils.isValidEnum(arg0, arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.EnumUtils()"""
        val = __EnumUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableRunnable
import org.apache.commons.lang3.Functions as __Functions_FailableRunnable
__FailableRunnable = __Functions_FailableRunnable.FailableRunnable
from abc import abstractmethod, ABC
 
class FailableRunnable(ABC):
    """org.apache.commons.lang3.Functions.FailableRunnable"""
 
    @staticmethod
    def __wrap(java_value: __FailableRunnable) -> 'FailableRunnable':
        return FailableRunnable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FailableRunnable):
        """
        Dynamic initializer for FailableRunnable.
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
    def run(self, ):
        """public abstract void org.apache.commons.lang3.Functions$FailableRunnable.run() throws T"""
        pass