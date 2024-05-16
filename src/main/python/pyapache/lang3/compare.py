from __future__ import annotations
from overload import overload


 
import java.util.function.Predicate as Predicate
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.function.Predicate as __Predicate
__Predicate = __Predicate
import java.lang.Comparable as Comparable
import org.apache.commons.lang3.compare.ComparableUtils as __ComparableUtils_ComparableCheckBuilder
__ComparableCheckBuilder = __ComparableUtils_ComparableCheckBuilder.ComparableCheckBuilder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.compare.ComparableUtils as __ComparableUtils
__ComparableUtils = __ComparableUtils
import java.lang.Integer as __int
from builtins import bool
import java.lang.Comparable as __Comparable
__Comparable = __Comparable
from builtins import int
 
class ComparableUtils():
    """org.apache.commons.lang3.compare.ComparableUtils"""
 
    @staticmethod
    def __wrap(java_value: __ComparableUtils) -> 'ComparableUtils':
        return ComparableUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ComparableUtils):
        """
        Dynamic initializer for ComparableUtils.
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
    def is(arg0: 'Comparable') -> 'ComparableCheckBuilder':
        """public static <A extends java.lang.Comparable<A>> org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder<A> org.apache.commons.lang3.compare.ComparableUtils.is(A)"""
        return ComparableCheckBuilder.__wrap(__ComparableUtils.is(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.between(A,A)"""
        return Predicate.__wrap(__ComparableUtils.between(arg0, arg1))

    @staticmethod
    @overload
    def gt(arg0: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.gt(A)"""
        return Predicate.__wrap(__ComparableUtils.gt(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def lt(arg0: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.lt(A)"""
        return Predicate.__wrap(__ComparableUtils.lt(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def ge(arg0: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.ge(A)"""
        return Predicate.__wrap(__ComparableUtils.ge(arg0))

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
    def betweenExclusive(arg0: 'Comparable', arg1: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.betweenExclusive(A,A)"""
        return Predicate.__wrap(__ComparableUtils.betweenExclusive(arg0, arg1))

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
    def le(arg0: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.le(A)"""
        return Predicate.__wrap(__ComparableUtils.le(arg0))

    @staticmethod
    @overload
    def max(arg0: 'Comparable', arg1: 'Comparable') -> 'Comparable':
        """public static <A extends java.lang.Comparable<A>> A org.apache.commons.lang3.compare.ComparableUtils.max(A,A)"""
        return Comparable.__wrap(__ComparableUtils.max(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def min(arg0: 'Comparable', arg1: 'Comparable') -> 'Comparable':
        """public static <A extends java.lang.Comparable<A>> A org.apache.commons.lang3.compare.ComparableUtils.min(A,A)"""
        return Comparable.__wrap(__ComparableUtils.min(arg0, arg1))

 
 
 
# CLASS: org.apache.commons.lang3.compare.ComparableUtils
import java.util.function.Predicate as Predicate
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.function.Predicate as __Predicate
__Predicate = __Predicate
import java.lang.Comparable as Comparable
import org.apache.commons.lang3.compare.ComparableUtils as __ComparableUtils_ComparableCheckBuilder
__ComparableCheckBuilder = __ComparableUtils_ComparableCheckBuilder.ComparableCheckBuilder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.compare.ComparableUtils as __ComparableUtils
__ComparableUtils = __ComparableUtils
import java.lang.Integer as __int
from builtins import bool
import java.lang.Comparable as __Comparable
__Comparable = __Comparable
from builtins import int
 
class ComparableUtils():
    """org.apache.commons.lang3.compare.ComparableUtils"""
 
    @staticmethod
    def __wrap(java_value: __ComparableUtils) -> 'ComparableUtils':
        return ComparableUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ComparableUtils):
        """
        Dynamic initializer for ComparableUtils.
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
    def is(arg0: 'Comparable') -> 'ComparableCheckBuilder':
        """public static <A extends java.lang.Comparable<A>> org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder<A> org.apache.commons.lang3.compare.ComparableUtils.is(A)"""
        return ComparableCheckBuilder.__wrap(__ComparableUtils.is(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.between(A,A)"""
        return Predicate.__wrap(__ComparableUtils.between(arg0, arg1))

    @staticmethod
    @overload
    def gt(arg0: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.gt(A)"""
        return Predicate.__wrap(__ComparableUtils.gt(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def lt(arg0: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.lt(A)"""
        return Predicate.__wrap(__ComparableUtils.lt(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def ge(arg0: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.ge(A)"""
        return Predicate.__wrap(__ComparableUtils.ge(arg0))

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
    def betweenExclusive(arg0: 'Comparable', arg1: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.betweenExclusive(A,A)"""
        return Predicate.__wrap(__ComparableUtils.betweenExclusive(arg0, arg1))

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
    def le(arg0: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.le(A)"""
        return Predicate.__wrap(__ComparableUtils.le(arg0))

    @staticmethod
    @overload
    def max(arg0: 'Comparable', arg1: 'Comparable') -> 'Comparable':
        """public static <A extends java.lang.Comparable<A>> A org.apache.commons.lang3.compare.ComparableUtils.max(A,A)"""
        return Comparable.__wrap(__ComparableUtils.max(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def min(arg0: 'Comparable', arg1: 'Comparable') -> 'Comparable':
        """public static <A extends java.lang.Comparable<A>> A org.apache.commons.lang3.compare.ComparableUtils.min(A,A)"""
        return Comparable.__wrap(__ComparableUtils.min(arg0, arg1))

 
 
 
# CLASS: org.apache.commons.lang3.compare.ComparableUtils 
 
 
# CLASS: org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Comparable as Comparable
import org.apache.commons.lang3.compare.ComparableUtils as __ComparableUtils_ComparableCheckBuilder
__ComparableCheckBuilder = __ComparableUtils_ComparableCheckBuilder.ComparableCheckBuilder
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
 
class ComparableCheckBuilder():
    """org.apache.commons.lang3.compare.ComparableUtils.ComparableCheckBuilder"""
 
    @staticmethod
    def __wrap(java_value: __ComparableCheckBuilder) -> 'ComparableCheckBuilder':
        return ComparableCheckBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ComparableCheckBuilder):
        """
        Dynamic initializer for ComparableCheckBuilder.
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
    def lessThanOrEqualTo(self, arg0: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.lessThanOrEqualTo(A)"""
        return bool.__wrap(super(__ComparableCheckBuilder, self).lessThanOrEqualTo(arg0))

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
    def between(self, arg0: 'Comparable', arg1: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.between(A,A)"""
        return bool.__wrap(super(__ComparableCheckBuilder, self).between(arg0, arg1))

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
    def equalTo(self, arg0: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.equalTo(A)"""
        return bool.__wrap(super(__ComparableCheckBuilder, self).equalTo(arg0))

    @overload
    def betweenExclusive(self, arg0: 'Comparable', arg1: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.betweenExclusive(A,A)"""
        return bool.__wrap(super(__ComparableCheckBuilder, self).betweenExclusive(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def greaterThan(self, arg0: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.greaterThan(A)"""
        return bool.__wrap(super(__ComparableCheckBuilder, self).greaterThan(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def lessThan(self, arg0: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.lessThan(A)"""
        return bool.__wrap(super(__ComparableCheckBuilder, self).lessThan(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def greaterThanOrEqualTo(self, arg0: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.greaterThanOrEqualTo(A)"""
        return bool.__wrap(super(__ComparableCheckBuilder, self).greaterThanOrEqualTo(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.compare.ObjectToStringComparator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.compare.ObjectToStringComparator as __ObjectToStringComparator
__ObjectToStringComparator = __ObjectToStringComparator
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
 
class ObjectToStringComparator():
    """org.apache.commons.lang3.compare.ObjectToStringComparator"""
 
    @staticmethod
    def __wrap(java_value: __ObjectToStringComparator) -> 'ObjectToStringComparator':
        return ObjectToStringComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectToStringComparator):
        """
        Dynamic initializer for ObjectToStringComparator.
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
        """public org.apache.commons.lang3.compare.ObjectToStringComparator()"""
        val = __ObjectToStringComparator()
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
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.lang3.compare.ObjectToStringComparator.compare(java.lang.Object,java.lang.Object)"""
        return int.__wrap(super(__ObjectToStringComparator, self).compare(arg0, arg1))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.compare.ObjectToStringComparator()"""
        val = __ObjectToStringComparator()
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

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

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