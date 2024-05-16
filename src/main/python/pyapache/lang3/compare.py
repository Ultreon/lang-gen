from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.compare.ObjectToStringComparator as _ObjectToStringComparator
_ObjectToStringComparator = _ObjectToStringComparator
import java.lang.String as _String
_String = _String
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjectToStringComparator():
    """org.apache.commons.lang3.compare.ObjectToStringComparator"""
 
    @staticmethod
    def _wrap(java_value: _ObjectToStringComparator) -> 'ObjectToStringComparator':
        return ObjectToStringComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectToStringComparator):
        """
        Dynamic initializer for ObjectToStringComparator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectToStringComparator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectToStringComparator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingInt(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.compare.ObjectToStringComparator()"""
        val = _ObjectToStringComparator()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.lang3.compare.ObjectToStringComparator.compare(java.lang.Object,java.lang.Object)"""
        return int._wrap(super(_ObjectToStringComparator, self).compare(arg0, arg1))

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

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
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.compare.ObjectToStringComparator()"""
        val = _ObjectToStringComparator()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.compare.ObjectToStringComparator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.compare.ObjectToStringComparator as _ObjectToStringComparator
_ObjectToStringComparator = _ObjectToStringComparator
import java.lang.String as _String
_String = _String
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjectToStringComparator():
    """org.apache.commons.lang3.compare.ObjectToStringComparator"""
 
    @staticmethod
    def _wrap(java_value: _ObjectToStringComparator) -> 'ObjectToStringComparator':
        return ObjectToStringComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectToStringComparator):
        """
        Dynamic initializer for ObjectToStringComparator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectToStringComparator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectToStringComparator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingInt(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.compare.ObjectToStringComparator()"""
        val = _ObjectToStringComparator()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.lang3.compare.ObjectToStringComparator.compare(java.lang.Object,java.lang.Object)"""
        return int._wrap(super(_ObjectToStringComparator, self).compare(arg0, arg1))

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

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
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.compare.ObjectToStringComparator()"""
        val = _ObjectToStringComparator()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.compare.ObjectToStringComparator 
 
 
# CLASS: org.apache.commons.lang3.compare.ComparableUtils
import java.util.function.Predicate as Predicate
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Comparable as Comparable
import java.lang.String as _String
_String = _String
import java.util.function.Predicate as _Predicate
_Predicate = _Predicate
import org.apache.commons.lang3.compare.ComparableUtils as _ComparableUtils_ComparableCheckBuilder
_ComparableCheckBuilder = _ComparableUtils_ComparableCheckBuilder.ComparableCheckBuilder
import java.lang.Integer as _int
import org.apache.commons.lang3.compare.ComparableUtils as _ComparableUtils
_ComparableUtils = _ComparableUtils
import java.lang.Comparable as _Comparable
_Comparable = _Comparable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ComparableUtils():
    """org.apache.commons.lang3.compare.ComparableUtils"""
 
    @staticmethod
    def _wrap(java_value: _ComparableUtils) -> 'ComparableUtils':
        return ComparableUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ComparableUtils):
        """
        Dynamic initializer for ComparableUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ComparableUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ComparableUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def ge(arg0: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.ge(A)"""
        return Predicate._wrap(_ComparableUtils.ge(arg0))

    @staticmethod
    @overload
    def gt(arg0: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.gt(A)"""
        return Predicate._wrap(_ComparableUtils.gt(arg0))

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
    def is(arg0: 'Comparable') -> 'ComparableCheckBuilder':
        """public static <A extends java.lang.Comparable<A>> org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder<A> org.apache.commons.lang3.compare.ComparableUtils.is(A)"""
        return ComparableCheckBuilder._wrap(_ComparableUtils.is(arg0))

    @staticmethod
    @overload
    def lt(arg0: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.lt(A)"""
        return Predicate._wrap(_ComparableUtils.lt(arg0))

    @staticmethod
    @overload
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.between(A,A)"""
        return Predicate._wrap(_ComparableUtils.between(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def min(arg0: 'Comparable', arg1: 'Comparable') -> 'Comparable':
        """public static <A extends java.lang.Comparable<A>> A org.apache.commons.lang3.compare.ComparableUtils.min(A,A)"""
        return Comparable._wrap(_ComparableUtils.min(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def le(arg0: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.le(A)"""
        return Predicate._wrap(_ComparableUtils.le(arg0))

    @staticmethod
    @overload
    def betweenExclusive(arg0: 'Comparable', arg1: 'Comparable') -> 'Predicate':
        """public static <A extends java.lang.Comparable<A>> java.util.function.Predicate<A> org.apache.commons.lang3.compare.ComparableUtils.betweenExclusive(A,A)"""
        return Predicate._wrap(_ComparableUtils.betweenExclusive(arg0, arg1))

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
    def max(arg0: 'Comparable', arg1: 'Comparable') -> 'Comparable':
        """public static <A extends java.lang.Comparable<A>> A org.apache.commons.lang3.compare.ComparableUtils.max(A,A)"""
        return Comparable._wrap(_ComparableUtils.max(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Comparable as Comparable
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.compare.ComparableUtils as _ComparableUtils_ComparableCheckBuilder
_ComparableCheckBuilder = _ComparableUtils_ComparableCheckBuilder.ComparableCheckBuilder
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ComparableCheckBuilder():
    """org.apache.commons.lang3.compare.ComparableUtils.ComparableCheckBuilder"""
 
    @staticmethod
    def _wrap(java_value: _ComparableCheckBuilder) -> 'ComparableCheckBuilder':
        return ComparableCheckBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ComparableCheckBuilder):
        """
        Dynamic initializer for ComparableCheckBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ComparableCheckBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ComparableCheckBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def greaterThan(self, arg0: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.greaterThan(A)"""
        return bool._wrap(super(_ComparableCheckBuilder, self).greaterThan(arg0))

    @overload
    def lessThanOrEqualTo(self, arg0: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.lessThanOrEqualTo(A)"""
        return bool._wrap(super(_ComparableCheckBuilder, self).lessThanOrEqualTo(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def greaterThanOrEqualTo(self, arg0: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.greaterThanOrEqualTo(A)"""
        return bool._wrap(super(_ComparableCheckBuilder, self).greaterThanOrEqualTo(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def between(self, arg0: 'Comparable', arg1: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.between(A,A)"""
        return bool._wrap(super(_ComparableCheckBuilder, self).between(arg0, arg1))

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
    def equalTo(self, arg0: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.equalTo(A)"""
        return bool._wrap(super(_ComparableCheckBuilder, self).equalTo(arg0))

    @overload
    def betweenExclusive(self, arg0: 'Comparable', arg1: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.betweenExclusive(A,A)"""
        return bool._wrap(super(_ComparableCheckBuilder, self).betweenExclusive(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def lessThan(self, arg0: 'Comparable') -> bool:
        """public boolean org.apache.commons.lang3.compare.ComparableUtils$ComparableCheckBuilder.lessThan(A)"""
        return bool._wrap(super(_ComparableCheckBuilder, self).lessThan(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())