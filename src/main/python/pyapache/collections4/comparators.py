from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.BitSet as BitSet
import java.util.Comparator as Comparator
import org.apache.commons.collections4.comparators.ComparatorChain as __ComparatorChain
__ComparatorChain = __ComparatorChain
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import java.util.function.ToLongFunction as ToLongFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
from builtins import int
import java.util.List as List
 
class ComparatorChain():
    """org.apache.commons.collections4.comparators.ComparatorChain"""
 
    @staticmethod
    def __wrap(java_value: __ComparatorChain) -> 'ComparatorChain':
        return ComparatorChain(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ComparatorChain):
        """
        Dynamic initializer for ComparatorChain.
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
    def setComparator(self, arg0: int, arg1: 'Comparator', arg2: bool):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.setComparator(int,java.util.Comparator<E>,boolean)"""
        super(__ComparatorChain, self).setComparator(__int.valueOf(arg0), arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.comparators.ComparatorChain.compare(E,E) throws java.lang.UnsupportedOperationException"""
        return int.__wrap(super(__ComparatorChain, self).compare(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.ComparatorChain.hashCode()"""
        return int.__wrap(super(ComparatorChain, self).hashCode())

    @overload
    def isLocked(self) -> bool:
        """public boolean org.apache.commons.collections4.comparators.ComparatorChain.isLocked()"""
        return bool.__wrap(super(ComparatorChain, self).isLocked())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Comparator'):
        """public org.apache.commons.collections4.comparators.ComparatorChain(java.util.Comparator<E>)"""
        val = __ComparatorChain(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setForwardSort(self, arg0: int):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.setForwardSort(int)"""
        super(__ComparatorChain, self).setForwardSort(__int.valueOf(arg0))

    @overload
    def addComparator(self, arg0: 'Comparator', arg1: bool):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.addComparator(java.util.Comparator<E>,boolean)"""
        super(__ComparatorChain, self).addComparator(arg0, __boolean.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'List'):
        """public org.apache.commons.collections4.comparators.ComparatorChain(java.util.List<java.util.Comparator<E>>)"""
        val = __ComparatorChain(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setComparator(self, arg0: int, arg1: 'Comparator'):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.setComparator(int,java.util.Comparator<E>) throws java.lang.IndexOutOfBoundsException"""
        super(__ComparatorChain, self).setComparator(__int.valueOf(arg0), arg1)

    @overload
    def __init__(self, arg0: 'List', arg1: 'BitSet'):
        """public org.apache.commons.collections4.comparators.ComparatorChain(java.util.List<java.util.Comparator<E>>,java.util.BitSet)"""
        val = __ComparatorChain(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Comparator', arg1: bool):
        """public org.apache.commons.collections4.comparators.ComparatorChain(java.util.Comparator<E>,boolean)"""
        val = __ComparatorChain(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.comparators.ComparatorChain.size()"""
        return int.__wrap(super(ComparatorChain, self).size())

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.comparators.ComparatorChain()"""
        val = __ComparatorChain()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.ComparatorChain.equals(java.lang.Object)"""
        return bool.__wrap(super(__ComparatorChain, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.comparators.ComparatorChain()"""
        val = __ComparatorChain()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setReverseSort(self, arg0: int):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.setReverseSort(int)"""
        super(__ComparatorChain, self).setReverseSort(__int.valueOf(arg0))

    @overload
    def addComparator(self, arg0: 'Comparator'):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.addComparator(java.util.Comparator<E>)"""
        super(__ComparatorChain, self).addComparator(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.comparators.ComparatorChain
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.BitSet as BitSet
import java.util.Comparator as Comparator
import org.apache.commons.collections4.comparators.ComparatorChain as __ComparatorChain
__ComparatorChain = __ComparatorChain
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import java.util.function.ToLongFunction as ToLongFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
from builtins import int
import java.util.List as List
 
class ComparatorChain():
    """org.apache.commons.collections4.comparators.ComparatorChain"""
 
    @staticmethod
    def __wrap(java_value: __ComparatorChain) -> 'ComparatorChain':
        return ComparatorChain(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ComparatorChain):
        """
        Dynamic initializer for ComparatorChain.
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
    def setComparator(self, arg0: int, arg1: 'Comparator', arg2: bool):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.setComparator(int,java.util.Comparator<E>,boolean)"""
        super(__ComparatorChain, self).setComparator(__int.valueOf(arg0), arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.comparators.ComparatorChain.compare(E,E) throws java.lang.UnsupportedOperationException"""
        return int.__wrap(super(__ComparatorChain, self).compare(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.ComparatorChain.hashCode()"""
        return int.__wrap(super(ComparatorChain, self).hashCode())

    @overload
    def isLocked(self) -> bool:
        """public boolean org.apache.commons.collections4.comparators.ComparatorChain.isLocked()"""
        return bool.__wrap(super(ComparatorChain, self).isLocked())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Comparator'):
        """public org.apache.commons.collections4.comparators.ComparatorChain(java.util.Comparator<E>)"""
        val = __ComparatorChain(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setForwardSort(self, arg0: int):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.setForwardSort(int)"""
        super(__ComparatorChain, self).setForwardSort(__int.valueOf(arg0))

    @overload
    def addComparator(self, arg0: 'Comparator', arg1: bool):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.addComparator(java.util.Comparator<E>,boolean)"""
        super(__ComparatorChain, self).addComparator(arg0, __boolean.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'List'):
        """public org.apache.commons.collections4.comparators.ComparatorChain(java.util.List<java.util.Comparator<E>>)"""
        val = __ComparatorChain(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setComparator(self, arg0: int, arg1: 'Comparator'):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.setComparator(int,java.util.Comparator<E>) throws java.lang.IndexOutOfBoundsException"""
        super(__ComparatorChain, self).setComparator(__int.valueOf(arg0), arg1)

    @overload
    def __init__(self, arg0: 'List', arg1: 'BitSet'):
        """public org.apache.commons.collections4.comparators.ComparatorChain(java.util.List<java.util.Comparator<E>>,java.util.BitSet)"""
        val = __ComparatorChain(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Comparator', arg1: bool):
        """public org.apache.commons.collections4.comparators.ComparatorChain(java.util.Comparator<E>,boolean)"""
        val = __ComparatorChain(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.comparators.ComparatorChain.size()"""
        return int.__wrap(super(ComparatorChain, self).size())

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.comparators.ComparatorChain()"""
        val = __ComparatorChain()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.ComparatorChain.equals(java.lang.Object)"""
        return bool.__wrap(super(__ComparatorChain, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.comparators.ComparatorChain()"""
        val = __ComparatorChain()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setReverseSort(self, arg0: int):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.setReverseSort(int)"""
        super(__ComparatorChain, self).setReverseSort(__int.valueOf(arg0))

    @overload
    def addComparator(self, arg0: 'Comparator'):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.addComparator(java.util.Comparator<E>)"""
        super(__ComparatorChain, self).addComparator(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.comparators.ComparatorChain 
 
 
# CLASS: org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import org.apache.commons.collections4.comparators.FixedOrderComparator as __FixedOrderComparator_UnknownObjectBehavior
__UnknownObjectBehavior = __FixedOrderComparator_UnknownObjectBehavior.UnknownObjectBehavior
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
 
class UnknownObjectBehavior():
    """org.apache.commons.collections4.comparators.FixedOrderComparator.UnknownObjectBehavior"""
 
    @staticmethod
    def __wrap(java_value: __UnknownObjectBehavior) -> 'UnknownObjectBehavior':
        return UnknownObjectBehavior(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnknownObjectBehavior):
        """
        Dynamic initializer for UnknownObjectBehavior.
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'UnknownObjectBehavior':
        """public static org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior.valueOf(java.lang.String)"""
        return UnknownObjectBehavior.__wrap(__UnknownObjectBehavior.valueOf(arg0))

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

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @staticmethod
    @overload
    def values() -> List['UnknownObjectBehavior']:
        """public static org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior[] org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior.values()"""
        return List[UnknownObjectBehavior].__wrap(__UnknownObjectBehavior.values())

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
 
 
# CLASS: org.apache.commons.collections4.comparators.BooleanComparator
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
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
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.comparators.BooleanComparator as __BooleanComparator
__BooleanComparator = __BooleanComparator
import java.util.function.ToLongFunction as ToLongFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
from builtins import int
 
class BooleanComparator():
    """org.apache.commons.collections4.comparators.BooleanComparator"""
 
    @staticmethod
    def __wrap(java_value: __BooleanComparator) -> 'BooleanComparator':
        return BooleanComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BooleanComparator):
        """
        Dynamic initializer for BooleanComparator.
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
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @staticmethod
    @overload
    def getFalseFirstComparator() -> 'BooleanComparator':
        """public static org.apache.commons.collections4.comparators.BooleanComparator org.apache.commons.collections4.comparators.BooleanComparator.getFalseFirstComparator()"""
        return BooleanComparator.__wrap(__BooleanComparator.getFalseFirstComparator())

    @overload
    def __init__(self, arg0: bool):
        """public org.apache.commons.collections4.comparators.BooleanComparator(boolean)"""
        val = __BooleanComparator(__boolean.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getTrueFirstComparator() -> 'BooleanComparator':
        """public static org.apache.commons.collections4.comparators.BooleanComparator org.apache.commons.collections4.comparators.BooleanComparator.getTrueFirstComparator()"""
        return BooleanComparator.__wrap(__BooleanComparator.getTrueFirstComparator())

    @staticmethod
    @overload
    def booleanComparator(arg0: bool) -> 'BooleanComparator':
        """public static org.apache.commons.collections4.comparators.BooleanComparator org.apache.commons.collections4.comparators.BooleanComparator.booleanComparator(boolean)"""
        return BooleanComparator.__wrap(__BooleanComparator.booleanComparator(__boolean.valueOf(arg0)))

    @overload
    def sortsTrueFirst(self) -> bool:
        """public boolean org.apache.commons.collections4.comparators.BooleanComparator.sortsTrueFirst()"""
        return bool.__wrap(super(BooleanComparator, self).sortsTrueFirst())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.comparators.BooleanComparator()"""
        val = __BooleanComparator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.BooleanComparator.hashCode()"""
        return int.__wrap(super(BooleanComparator, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compare(self, arg0: 'Boolean', arg1: 'Boolean') -> int:
        """public int org.apache.commons.collections4.comparators.BooleanComparator.compare(java.lang.Boolean,java.lang.Boolean)"""
        return int.__wrap(super(__BooleanComparator, self).compare(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.BooleanComparator.equals(java.lang.Object)"""
        return bool.__wrap(super(__BooleanComparator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.comparators.BooleanComparator()"""
        val = __BooleanComparator()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.comparators.NullComparator
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
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
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import java.util.function.ToLongFunction as ToLongFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
import org.apache.commons.collections4.comparators.NullComparator as __NullComparator
__NullComparator = __NullComparator
from builtins import bool
from builtins import int
 
class NullComparator():
    """org.apache.commons.collections4.comparators.NullComparator"""
 
    @staticmethod
    def __wrap(java_value: __NullComparator) -> 'NullComparator':
        return NullComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NullComparator):
        """
        Dynamic initializer for NullComparator.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.NullComparator.equals(java.lang.Object)"""
        return bool.__wrap(super(__NullComparator, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Comparator'):
        """public org.apache.commons.collections4.comparators.NullComparator(java.util.Comparator<? super E>)"""
        val = __NullComparator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.comparators.NullComparator()"""
        val = __NullComparator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def __init__(self, arg0: 'Comparator', arg1: bool):
        """public org.apache.commons.collections4.comparators.NullComparator(java.util.Comparator<? super E>,boolean)"""
        val = __NullComparator(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.comparators.NullComparator.compare(E,E)"""
        return int.__wrap(super(__NullComparator, self).compare(arg0, arg1))

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
        """public int org.apache.commons.collections4.comparators.NullComparator.hashCode()"""
        return int.__wrap(super(NullComparator, self).hashCode())

    @overload
    def __init__(self, arg0: bool):
        """public org.apache.commons.collections4.comparators.NullComparator(boolean)"""
        val = __NullComparator(__boolean.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.comparators.NullComparator()"""
        val = __NullComparator()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.comparators.TransformingComparator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Comparator as __Comparator
__Comparator = __Comparator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import java.util.function.ToLongFunction as ToLongFunction
import org.apache.commons.collections4.comparators.TransformingComparator as __TransformingComparator
__TransformingComparator = __TransformingComparator
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
from builtins import int
 
class TransformingComparator():
    """org.apache.commons.collections4.comparators.TransformingComparator"""
 
    @staticmethod
    def __wrap(java_value: __TransformingComparator) -> 'TransformingComparator':
        return TransformingComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformingComparator):
        """
        Dynamic initializer for TransformingComparator.
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
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.comparators.TransformingComparator.compare(I,I)"""
        return int.__wrap(super(__TransformingComparator, self).compare(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.TransformingComparator.hashCode()"""
        return int.__wrap(super(TransformingComparator, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Transformer', arg1: 'Comparator'):
        """public org.apache.commons.collections4.comparators.TransformingComparator(org.apache.commons.collections4.Transformer<? super I, ? extends O>,java.util.Comparator<O>)"""
        val = __TransformingComparator(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def __init__(self, arg0: 'Transformer'):
        """public org.apache.commons.collections4.comparators.TransformingComparator(org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        val = __TransformingComparator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

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
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.TransformingComparator.equals(java.lang.Object)"""
        return bool.__wrap(super(__TransformingComparator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.comparators.FixedOrderComparator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.comparators.FixedOrderComparator as __FixedOrderComparator
__FixedOrderComparator = __FixedOrderComparator
from builtins import object
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import org.apache.commons.collections4.comparators.FixedOrderComparator as __FixedOrderComparator_UnknownObjectBehavior
__UnknownObjectBehavior = __FixedOrderComparator_UnknownObjectBehavior.UnknownObjectBehavior
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import java.util.function.ToLongFunction as ToLongFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
from builtins import int
import java.util.List as List
 
class FixedOrderComparator():
    """org.apache.commons.collections4.comparators.FixedOrderComparator"""
 
    @staticmethod
    def __wrap(java_value: __FixedOrderComparator) -> 'FixedOrderComparator':
        return FixedOrderComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FixedOrderComparator):
        """
        Dynamic initializer for FixedOrderComparator.
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
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.comparators.FixedOrderComparator.compare(T,T)"""
        return int.__wrap(super(__FixedOrderComparator, self).compare(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setUnknownObjectBehavior(self, arg0: 'UnknownObjectBehavior'):
        """public void org.apache.commons.collections4.comparators.FixedOrderComparator.setUnknownObjectBehavior(org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior)"""
        super(__FixedOrderComparator, self).setUnknownObjectBehavior(arg0)

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.comparators.FixedOrderComparator()"""
        val = __FixedOrderComparator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.FixedOrderComparator.add(T)"""
        return bool.__wrap(super(__FixedOrderComparator, self).add(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.comparators.FixedOrderComparator()"""
        val = __FixedOrderComparator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def addAsEqual(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.FixedOrderComparator.addAsEqual(T,T)"""
        return bool.__wrap(super(__FixedOrderComparator, self).addAsEqual(arg0, arg1))

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
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @overload
    def isLocked(self) -> bool:
        """public boolean org.apache.commons.collections4.comparators.FixedOrderComparator.isLocked()"""
        return bool.__wrap(super(FixedOrderComparator, self).isLocked())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.FixedOrderComparator.equals(java.lang.Object)"""
        return bool.__wrap(super(__FixedOrderComparator, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.FixedOrderComparator.hashCode()"""
        return int.__wrap(super(FixedOrderComparator, self).hashCode())

    @overload
    def getUnknownObjectBehavior(self) -> 'UnknownObjectBehavior':
        """public org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior org.apache.commons.collections4.comparators.FixedOrderComparator.getUnknownObjectBehavior()"""
        return 'UnknownObjectBehavior'.__wrap(super(FixedOrderComparator, self).getUnknownObjectBehavior())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'List'):
        """public org.apache.commons.collections4.comparators.FixedOrderComparator(java.util.List<T>)"""
        val = __FixedOrderComparator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, *arg0: object):
        """public org.apache.commons.collections4.comparators.FixedOrderComparator(T...)"""
        val = __FixedOrderComparator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.comparators.ComparableComparator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.comparators.ComparableComparator as __ComparableComparator
__ComparableComparator = __ComparableComparator
import java.lang.Comparable as Comparable
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import java.util.function.ToLongFunction as ToLongFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
from builtins import int
 
class ComparableComparator():
    """org.apache.commons.collections4.comparators.ComparableComparator"""
 
    @staticmethod
    def __wrap(java_value: __ComparableComparator) -> 'ComparableComparator':
        return ComparableComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ComparableComparator):
        """
        Dynamic initializer for ComparableComparator.
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
        """public org.apache.commons.collections4.comparators.ComparableComparator()"""
        val = __ComparableComparator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def compare(self, arg0: 'Comparable', arg1: 'Comparable') -> int:
        """public int org.apache.commons.collections4.comparators.ComparableComparator.compare(E,E)"""
        return int.__wrap(super(__ComparableComparator, self).compare(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.ComparableComparator.equals(java.lang.Object)"""
        return bool.__wrap(super(__ComparableComparator, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.comparators.ComparableComparator()"""
        val = __ComparableComparator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.ComparableComparator.hashCode()"""
        return int.__wrap(super(ComparableComparator, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def comparableComparator() -> 'ComparableComparator':
        """public static <E extends java.lang.Comparable<? super E>> org.apache.commons.collections4.comparators.ComparableComparator<E> org.apache.commons.collections4.comparators.ComparableComparator.comparableComparator()"""
        return ComparableComparator.__wrap(__ComparableComparator.comparableComparator())

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.comparators.ReverseComparator
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
import org.apache.commons.collections4.comparators.ReverseComparator as __ReverseComparator
__ReverseComparator = __ReverseComparator
import java.lang.String as __String
__String = __String
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import java.util.function.ToLongFunction as ToLongFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
from builtins import int
 
class ReverseComparator():
    """org.apache.commons.collections4.comparators.ReverseComparator"""
 
    @staticmethod
    def __wrap(java_value: __ReverseComparator) -> 'ReverseComparator':
        return ReverseComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReverseComparator):
        """
        Dynamic initializer for ReverseComparator.
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
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def __init__(self, arg0: 'Comparator'):
        """public org.apache.commons.collections4.comparators.ReverseComparator(java.util.Comparator<? super E>)"""
        val = __ReverseComparator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.comparators.ReverseComparator.compare(E,E)"""
        return int.__wrap(super(__ReverseComparator, self).compare(arg0, arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.comparators.ReverseComparator()"""
        val = __ReverseComparator()
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
    def __init__(self):
        """public org.apache.commons.collections4.comparators.ReverseComparator()"""
        val = __ReverseComparator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.ReverseComparator.hashCode()"""
        return int.__wrap(super(ReverseComparator, self).hashCode())

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.ReverseComparator.equals(java.lang.Object)"""
        return bool.__wrap(super(__ReverseComparator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0))