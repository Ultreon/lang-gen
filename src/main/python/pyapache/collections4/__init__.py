from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Comparator as Comparator
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.apache.commons.collections4.ComparatorUtils as _ComparatorUtils
_ComparatorUtils = _ComparatorUtils
import java.util.Comparator as _Comparator
_Comparator = _Comparator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ComparatorUtils():
    """org.apache.commons.collections4.ComparatorUtils"""
 
    @staticmethod
    def _wrap(java_value: _ComparatorUtils) -> 'ComparatorUtils':
        return ComparatorUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ComparatorUtils):
        """
        Dynamic initializer for ComparatorUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ComparatorUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ComparatorUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def reversedComparator(arg0: 'Comparator') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.reversedComparator(java.util.Comparator<E>)"""
        return Comparator._wrap(_ComparatorUtils.reversedComparator(arg0))

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
    def booleanComparator(arg0: bool) -> 'Comparator':
        """public static java.util.Comparator<java.lang.Boolean> org.apache.commons.collections4.ComparatorUtils.booleanComparator(boolean)"""
        return Comparator._wrap(_ComparatorUtils.booleanComparator(_boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def naturalComparator() -> 'Comparator':
        """public static <E extends java.lang.Comparable<? super E>> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.naturalComparator()"""
        return Comparator._wrap(_ComparatorUtils.naturalComparator())

    @staticmethod
    @overload
    def nullLowComparator(arg0: 'Comparator') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.nullLowComparator(java.util.Comparator<E>)"""
        return Comparator._wrap(_ComparatorUtils.nullLowComparator(arg0))

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
    def chainedComparator(arg0: 'Collection') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.chainedComparator(java.util.Collection<java.util.Comparator<E>>)"""
        return Comparator._wrap(_ComparatorUtils.chainedComparator(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def max(arg0: object, arg1: object, arg2: 'Comparator') -> object:
        """public static <E> E org.apache.commons.collections4.ComparatorUtils.max(E,E,java.util.Comparator<E>)"""
        return object._wrap(_ComparatorUtils.max(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nullHighComparator(arg0: 'Comparator') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.nullHighComparator(java.util.Comparator<E>)"""
        return Comparator._wrap(_ComparatorUtils.nullHighComparator(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def transformedComparator(arg0: 'Comparator', arg1: 'Transformer') -> 'Comparator':
        """public static <I,O> java.util.Comparator<I> org.apache.commons.collections4.ComparatorUtils.transformedComparator(java.util.Comparator<O>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Comparator._wrap(_ComparatorUtils.transformedComparator(arg0, arg1))

    @staticmethod
    @overload
    def min(arg0: object, arg1: object, arg2: 'Comparator') -> object:
        """public static <E> E org.apache.commons.collections4.ComparatorUtils.min(E,E,java.util.Comparator<E>)"""
        return object._wrap(_ComparatorUtils.min(arg0, arg1, arg2))

    @staticmethod
    @overload
    def chainedComparator(*arg0: 'Comparator') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.chainedComparator(java.util.Comparator<E>...)"""
        return Comparator._wrap(_ComparatorUtils.chainedComparator(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.collections4.ComparatorUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Comparator as Comparator
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.apache.commons.collections4.ComparatorUtils as _ComparatorUtils
_ComparatorUtils = _ComparatorUtils
import java.util.Comparator as _Comparator
_Comparator = _Comparator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ComparatorUtils():
    """org.apache.commons.collections4.ComparatorUtils"""
 
    @staticmethod
    def _wrap(java_value: _ComparatorUtils) -> 'ComparatorUtils':
        return ComparatorUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ComparatorUtils):
        """
        Dynamic initializer for ComparatorUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ComparatorUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ComparatorUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def reversedComparator(arg0: 'Comparator') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.reversedComparator(java.util.Comparator<E>)"""
        return Comparator._wrap(_ComparatorUtils.reversedComparator(arg0))

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
    def booleanComparator(arg0: bool) -> 'Comparator':
        """public static java.util.Comparator<java.lang.Boolean> org.apache.commons.collections4.ComparatorUtils.booleanComparator(boolean)"""
        return Comparator._wrap(_ComparatorUtils.booleanComparator(_boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def naturalComparator() -> 'Comparator':
        """public static <E extends java.lang.Comparable<? super E>> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.naturalComparator()"""
        return Comparator._wrap(_ComparatorUtils.naturalComparator())

    @staticmethod
    @overload
    def nullLowComparator(arg0: 'Comparator') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.nullLowComparator(java.util.Comparator<E>)"""
        return Comparator._wrap(_ComparatorUtils.nullLowComparator(arg0))

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
    def chainedComparator(arg0: 'Collection') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.chainedComparator(java.util.Collection<java.util.Comparator<E>>)"""
        return Comparator._wrap(_ComparatorUtils.chainedComparator(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def max(arg0: object, arg1: object, arg2: 'Comparator') -> object:
        """public static <E> E org.apache.commons.collections4.ComparatorUtils.max(E,E,java.util.Comparator<E>)"""
        return object._wrap(_ComparatorUtils.max(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nullHighComparator(arg0: 'Comparator') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.nullHighComparator(java.util.Comparator<E>)"""
        return Comparator._wrap(_ComparatorUtils.nullHighComparator(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def transformedComparator(arg0: 'Comparator', arg1: 'Transformer') -> 'Comparator':
        """public static <I,O> java.util.Comparator<I> org.apache.commons.collections4.ComparatorUtils.transformedComparator(java.util.Comparator<O>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Comparator._wrap(_ComparatorUtils.transformedComparator(arg0, arg1))

    @staticmethod
    @overload
    def min(arg0: object, arg1: object, arg2: 'Comparator') -> object:
        """public static <E> E org.apache.commons.collections4.ComparatorUtils.min(E,E,java.util.Comparator<E>)"""
        return object._wrap(_ComparatorUtils.min(arg0, arg1, arg2))

    @staticmethod
    @overload
    def chainedComparator(*arg0: 'Comparator') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.chainedComparator(java.util.Comparator<E>...)"""
        return Comparator._wrap(_ComparatorUtils.chainedComparator(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.collections4.ComparatorUtils 
 
 
# CLASS: org.apache.commons.collections4.FactoryUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.FactoryUtils as _FactoryUtils
_FactoryUtils = _FactoryUtils
import java.lang.Integer as _int
import org.apache.commons.collections4.Factory as _Factory
_Factory = _Factory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FactoryUtils():
    """org.apache.commons.collections4.FactoryUtils"""
 
    @staticmethod
    def _wrap(java_value: _FactoryUtils) -> 'FactoryUtils':
        return FactoryUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FactoryUtils):
        """
        Dynamic initializer for FactoryUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FactoryUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FactoryUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def instantiateFactory(arg0: 'Class', arg1: 'Class', arg2: 'Object') -> 'Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.FactoryUtils.instantiateFactory(java.lang.Class<T>,java.lang.Class<?>[],java.lang.Object[])"""
        return Factory._wrap(_FactoryUtils.instantiateFactory(arg0, arg1, arg2))

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
    def constantFactory(arg0: object) -> 'Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.FactoryUtils.constantFactory(T)"""
        return Factory._wrap(_FactoryUtils.constantFactory(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def instantiateFactory(arg0: 'Class') -> 'Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.FactoryUtils.instantiateFactory(java.lang.Class<T>)"""
        return Factory._wrap(_FactoryUtils.instantiateFactory(arg0))

    @staticmethod
    @overload
    def exceptionFactory() -> 'Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.FactoryUtils.exceptionFactory()"""
        return Factory._wrap(_FactoryUtils.exceptionFactory())

    @staticmethod
    @overload
    def nullFactory() -> 'Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.FactoryUtils.nullFactory()"""
        return Factory._wrap(_FactoryUtils.nullFactory())

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
    def prototypeFactory(arg0: object) -> 'Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.FactoryUtils.prototypeFactory(T)"""
        return Factory._wrap(_FactoryUtils.prototypeFactory(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.BagUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.Bag as _Bag
_Bag = _Bag
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.BagUtils as _BagUtils
_BagUtils = _BagUtils
import java.lang.Integer as _int
import org.apache.commons.collections4.SortedBag as _SortedBag
_SortedBag = _SortedBag
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BagUtils():
    """org.apache.commons.collections4.BagUtils"""
 
    @staticmethod
    def _wrap(java_value: _BagUtils) -> 'BagUtils':
        return BagUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BagUtils):
        """
        Dynamic initializer for BagUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BagUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BagUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def transformingSortedBag(arg0: 'SortedBag', arg1: 'Transformer') -> 'SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.BagUtils.transformingSortedBag(org.apache.commons.collections4.SortedBag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return SortedBag._wrap(_BagUtils.transformingSortedBag(arg0, arg1))

    @staticmethod
    @overload
    def predicatedBag(arg0: 'Bag', arg1: 'Predicate') -> 'Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.BagUtils.predicatedBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return Bag._wrap(_BagUtils.predicatedBag(arg0, arg1))

    @staticmethod
    @overload
    def transformingBag(arg0: 'Bag', arg1: 'Transformer') -> 'Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.BagUtils.transformingBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Bag._wrap(_BagUtils.transformingBag(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableBag(arg0: 'Bag') -> 'Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.BagUtils.unmodifiableBag(org.apache.commons.collections4.Bag<? extends E>)"""
        return Bag._wrap(_BagUtils.unmodifiableBag(arg0))

    @staticmethod
    @overload
    def synchronizedBag(arg0: 'Bag') -> 'Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.BagUtils.synchronizedBag(org.apache.commons.collections4.Bag<E>)"""
        return Bag._wrap(_BagUtils.synchronizedBag(arg0))

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
    def synchronizedSortedBag(arg0: 'SortedBag') -> 'SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.BagUtils.synchronizedSortedBag(org.apache.commons.collections4.SortedBag<E>)"""
        return SortedBag._wrap(_BagUtils.synchronizedSortedBag(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def predicatedSortedBag(arg0: 'SortedBag', arg1: 'Predicate') -> 'SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.BagUtils.predicatedSortedBag(org.apache.commons.collections4.SortedBag<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return SortedBag._wrap(_BagUtils.predicatedSortedBag(arg0, arg1))

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
    def unmodifiableSortedBag(arg0: 'SortedBag') -> 'SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.BagUtils.unmodifiableSortedBag(org.apache.commons.collections4.SortedBag<E>)"""
        return SortedBag._wrap(_BagUtils.unmodifiableSortedBag(arg0))

    @staticmethod
    @overload
    def collectionBag(arg0: 'Bag') -> 'Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.BagUtils.collectionBag(org.apache.commons.collections4.Bag<E>)"""
        return Bag._wrap(_BagUtils.collectionBag(arg0))

    @staticmethod
    @overload
    def emptyBag() -> 'Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.BagUtils.emptyBag()"""
        return Bag._wrap(_BagUtils.emptyBag())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def emptySortedBag() -> 'SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.BagUtils.emptySortedBag()"""
        return SortedBag._wrap(_BagUtils.emptySortedBag())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.Transformer
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from abc import abstractmethod, ABC
 
class Transformer():
    """org.apache.commons.collections4.Transformer"""
 
    @staticmethod
    def _wrap(java_value: _Transformer) -> 'Transformer':
        return Transformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Transformer):
        """
        Dynamic initializer for Transformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Transformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Transformer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def transform(self, arg0: object):
        """public abstract O org.apache.commons.collections4.Transformer.transform(I)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.OrderedBidiMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.Get as _Get
_Get = _Get
from abc import abstractmethod, ABC
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.Put as _Put
_Put = _Put
import org.apache.commons.collections4.OrderedBidiMap as _OrderedBidiMap
_OrderedBidiMap = _OrderedBidiMap
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.OrderedMap as _OrderedMap
_OrderedMap = _OrderedMap
import org.apache.commons.collections4.BidiMap as _BidiMap
_BidiMap = _BidiMap
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class OrderedBidiMap():
    """org.apache.commons.collections4.OrderedBidiMap"""
 
    @staticmethod
    def _wrap(java_value: _OrderedBidiMap) -> 'OrderedBidiMap':
        return OrderedBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OrderedBidiMap):
        """
        Dynamic initializer for OrderedBidiMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OrderedBidiMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OrderedBidiMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def getKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.BidiMap.getKey(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.firstKey()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.OrderedMap.mapIterator()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @abstractmethod
    def nextKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.nextKey(K)"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def inverseBidiMap(self, ):
        """public abstract org.apache.commons.collections4.OrderedBidiMap<V, K> org.apache.commons.collections4.OrderedBidiMap.inverseBidiMap()"""
        pass

    @abstractmethod
    def previousKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.previousKey(K)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

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

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Set<V> org.apache.commons.collections4.BidiMap.values()"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V org.apache.commons.collections4.BidiMap.put(K,V)"""
        pass

    @abstractmethod
    def removeValue(self, arg0: object):
        """public abstract K org.apache.commons.collections4.BidiMap.removeValue(java.lang.Object)"""
        pass

    @abstractmethod
    def lastKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.lastKey()"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

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
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.SortedBag
import java.util.function.Predicate as Predicate
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.Bag as _Bag
_Bag = _Bag
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
from typing import List
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import org.apache.commons.collections4.SortedBag as _SortedBag
_SortedBag = _SortedBag
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
from builtins import bool
 
class SortedBag():
    """org.apache.commons.collections4.SortedBag"""
 
    @staticmethod
    def _wrap(java_value: _SortedBag) -> 'SortedBag':
        return SortedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SortedBag):
        """
        Dynamic initializer for SortedBag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SortedBag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SortedBag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def add(self, arg0: object, arg1: int):
        """public abstract boolean org.apache.commons.collections4.Bag.add(E,int)"""
        pass

    @abstractmethod
    def removeAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.Bag.removeAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Collection.isEmpty()"""
        pass

    @abstractmethod
    def uniqueSet(self, ):
        """public abstract java.util.Set<E> org.apache.commons.collections4.Bag.uniqueSet()"""
        pass

    @abstractmethod
    def comparator(self, ):
        """public abstract java.util.Comparator<? super E> org.apache.commons.collections4.SortedBag.comparator()"""
        pass

    @abstractmethod
    def getCount(self, arg0: object):
        """public abstract int org.apache.commons.collections4.Bag.getCount(java.lang.Object)"""
        pass

    @abstractmethod
    def containsAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.Bag.containsAll(java.util.Collection<?>)"""
        pass

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @abstractmethod
    def remove(self, arg0: object, arg1: int):
        """public abstract boolean org.apache.commons.collections4.Bag.remove(java.lang.Object,int)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Bag.size()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Collection.hashCode()"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @abstractmethod
    def toArray(self, arg0: 'Object'):
        """public abstract <T> T[] java.util.Collection.toArray(T[])"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Collection.clear()"""
        pass

    @abstractmethod
    def first(self, ):
        """public abstract E org.apache.commons.collections4.SortedBag.first()"""
        pass

    @abstractmethod
    def retainAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.Bag.retainAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def last(self, ):
        """public abstract E org.apache.commons.collections4.SortedBag.last()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Collection.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def contains(self, arg0: object):
        """public abstract boolean java.util.Collection.contains(java.lang.Object)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.addAll(java.util.Collection<? extends E>)"""
        pass

    @abstractmethod
    def add(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Bag.add(E)"""
        pass

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @abstractmethod
    def toArray(self, ):
        """public abstract java.lang.Object[] java.util.Collection.toArray()"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<E> org.apache.commons.collections4.Bag.iterator()"""
        pass

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Bag.remove(java.lang.Object)"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.MultiMapUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.Bag as _Bag
_Bag = _Bag
import org.apache.commons.collections4.SetValuedMap as _SetValuedMap
_SetValuedMap = _SetValuedMap
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MultiValuedMap as _MultiValuedMap
_MultiValuedMap = _MultiValuedMap
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import org.apache.commons.collections4.MultiMapUtils as _MultiMapUtils
_MultiMapUtils = _MultiMapUtils
import org.apache.commons.collections4.ListValuedMap as _ListValuedMap
_ListValuedMap = _ListValuedMap
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MultiMapUtils():
    """org.apache.commons.collections4.MultiMapUtils"""
 
    @staticmethod
    def _wrap(java_value: _MultiMapUtils) -> 'MultiMapUtils':
        return MultiMapUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiMapUtils):
        """
        Dynamic initializer for MultiMapUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiMapUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiMapUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getValuesAsSet(arg0: 'MultiValuedMap', arg1: object) -> 'Set':
        """public static <K,V> java.util.Set<V> org.apache.commons.collections4.MultiMapUtils.getValuesAsSet(org.apache.commons.collections4.MultiValuedMap<K, V>,K)"""
        return Set._wrap(_MultiMapUtils.getValuesAsSet(arg0, arg1))

    @staticmethod
    @overload
    def getCollection(arg0: 'MultiValuedMap', arg1: object) -> 'Collection':
        """public static <K,V> java.util.Collection<V> org.apache.commons.collections4.MultiMapUtils.getCollection(org.apache.commons.collections4.MultiValuedMap<K, V>,K)"""
        return Collection._wrap(_MultiMapUtils.getCollection(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def isEmpty(arg0: 'MultiValuedMap') -> bool:
        """public static boolean org.apache.commons.collections4.MultiMapUtils.isEmpty(org.apache.commons.collections4.MultiValuedMap<?, ?>)"""
        return bool._wrap(_MultiMapUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def emptyMultiValuedMap() -> 'MultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.MultiValuedMap<K, V> org.apache.commons.collections4.MultiMapUtils.emptyMultiValuedMap()"""
        return MultiValuedMap._wrap(_MultiMapUtils.emptyMultiValuedMap())

    @staticmethod
    @overload
    def transformedMultiValuedMap(arg0: 'MultiValuedMap', arg1: 'Transformer', arg2: 'Transformer') -> 'MultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.MultiValuedMap<K, V> org.apache.commons.collections4.MultiMapUtils.transformedMultiValuedMap(org.apache.commons.collections4.MultiValuedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return MultiValuedMap._wrap(_MultiMapUtils.transformedMultiValuedMap(arg0, arg1, arg2))

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

    @staticmethod
    @overload
    def emptyIfNull(arg0: 'MultiValuedMap') -> 'MultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.MultiValuedMap<K, V> org.apache.commons.collections4.MultiMapUtils.emptyIfNull(org.apache.commons.collections4.MultiValuedMap<K, V>)"""
        return MultiValuedMap._wrap(_MultiMapUtils.emptyIfNull(arg0))

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
    def getValuesAsBag(arg0: 'MultiValuedMap', arg1: object) -> 'Bag':
        """public static <K,V> org.apache.commons.collections4.Bag<V> org.apache.commons.collections4.MultiMapUtils.getValuesAsBag(org.apache.commons.collections4.MultiValuedMap<K, V>,K)"""
        return Bag._wrap(_MultiMapUtils.getValuesAsBag(arg0, arg1))

    @staticmethod
    @overload
    def getValuesAsList(arg0: 'MultiValuedMap', arg1: object) -> 'List':
        """public static <K,V> java.util.List<V> org.apache.commons.collections4.MultiMapUtils.getValuesAsList(org.apache.commons.collections4.MultiValuedMap<K, V>,K)"""
        return List._wrap(_MultiMapUtils.getValuesAsList(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def newListValuedHashMap() -> 'ListValuedMap':
        """public static <K,V> org.apache.commons.collections4.ListValuedMap<K, V> org.apache.commons.collections4.MultiMapUtils.newListValuedHashMap()"""
        return ListValuedMap._wrap(_MultiMapUtils.newListValuedHashMap())

    @staticmethod
    @overload
    def newSetValuedHashMap() -> 'SetValuedMap':
        """public static <K,V> org.apache.commons.collections4.SetValuedMap<K, V> org.apache.commons.collections4.MultiMapUtils.newSetValuedHashMap()"""
        return SetValuedMap._wrap(_MultiMapUtils.newSetValuedHashMap())

    @staticmethod
    @overload
    def unmodifiableMultiValuedMap(arg0: 'MultiValuedMap') -> 'MultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.MultiValuedMap<K, V> org.apache.commons.collections4.MultiMapUtils.unmodifiableMultiValuedMap(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return MultiValuedMap._wrap(_MultiMapUtils.unmodifiableMultiValuedMap(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.CollectionUtils
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Map.Entry as Entry
import java.lang.Boolean as _boolean
import java.util.Enumeration as Enumeration
from builtins import bool
from builtins import str
import org.apache.commons.collections4.Closure as _Closure
_Closure = _Closure
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Iterable as Iterable
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
import java.util.Comparator as Comparator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import org.apache.commons.collections4.CollectionUtils as _CollectionUtils
_CollectionUtils = _CollectionUtils
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class CollectionUtils():
    """org.apache.commons.collections4.CollectionUtils"""
 
    @staticmethod
    def _wrap(java_value: _CollectionUtils) -> 'CollectionUtils':
        return CollectionUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CollectionUtils):
        """
        Dynamic initializer for CollectionUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CollectionUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CollectionUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def emptyIfNull(arg0: 'Collection') -> 'Collection':
        """public static <T> java.util.Collection<T> org.apache.commons.collections4.CollectionUtils.emptyIfNull(java.util.Collection<T>)"""
        return Collection._wrap(_CollectionUtils.emptyIfNull(arg0))

    @staticmethod
    @overload
    def reverseArray(arg0: 'Object'):
        """public static void org.apache.commons.collections4.CollectionUtils.reverseArray(java.lang.Object[])"""
        _CollectionUtils.reverseArray(arg0)

    @staticmethod
    @overload
    def select(arg0: 'Iterable', arg1: 'Predicate', arg2: 'Collection') -> 'Collection':
        """public static <O,R extends java.util.Collection<? super O>> R org.apache.commons.collections4.CollectionUtils.select(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>,R)"""
        return Collection._wrap(_CollectionUtils.select(arg0, arg1, arg2))

    @staticmethod
    @overload
    def isProperSubCollection(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.isProperSubCollection(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool._wrap(_CollectionUtils.isProperSubCollection(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def removeAll(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Equator') -> 'Collection':
        """public static <E> java.util.Collection<E> org.apache.commons.collections4.CollectionUtils.removeAll(java.lang.Iterable<E>,java.lang.Iterable<? extends E>,org.apache.commons.collections4.Equator<? super E>)"""
        return Collection._wrap(_CollectionUtils.removeAll(arg0, arg1, arg2))

    @staticmethod
    @overload
    def predicatedCollection(arg0: 'Collection', arg1: 'Predicate') -> 'Collection':
        """public static <C> java.util.Collection<C> org.apache.commons.collections4.CollectionUtils.predicatedCollection(java.util.Collection<C>,org.apache.commons.collections4.Predicate<? super C>)"""
        return Collection._wrap(_CollectionUtils.predicatedCollection(arg0, arg1))

    @staticmethod
    @overload
    def containsAny(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.containsAny(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool._wrap(_CollectionUtils.containsAny(arg0, arg1))

    @staticmethod
    @overload
    def retainAll(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Equator') -> 'Collection':
        """public static <E> java.util.Collection<E> org.apache.commons.collections4.CollectionUtils.retainAll(java.lang.Iterable<E>,java.lang.Iterable<? extends E>,org.apache.commons.collections4.Equator<? super E>)"""
        return Collection._wrap(_CollectionUtils.retainAll(arg0, arg1, arg2))

    @staticmethod
    @overload
    def forAllDo(arg0: 'Iterable', arg1: 'Closure') -> 'Closure':
        """public static <T,C extends org.apache.commons.collections4.Closure<? super T>> C org.apache.commons.collections4.CollectionUtils.forAllDo(java.lang.Iterable<T>,C)"""
        return Closure._wrap(_CollectionUtils.forAllDo(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def subtract(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Predicate') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.subtract(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<O>)"""
        return Collection._wrap(_CollectionUtils.subtract(arg0, arg1, arg2))

    @staticmethod
    @overload
    def forAllButLastDo(arg0: 'Iterable', arg1: 'Closure') -> object:
        """public static <T,C extends org.apache.commons.collections4.Closure<? super T>> T org.apache.commons.collections4.CollectionUtils.forAllButLastDo(java.lang.Iterable<T>,C)"""
        return object._wrap(_CollectionUtils.forAllButLastDo(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def forAllDo(arg0: 'Iterator', arg1: 'Closure') -> 'Closure':
        """public static <T,C extends org.apache.commons.collections4.Closure<? super T>> C org.apache.commons.collections4.CollectionUtils.forAllDo(java.util.Iterator<T>,C)"""
        return Closure._wrap(_CollectionUtils.forAllDo(arg0, arg1))

    @staticmethod
    @overload
    def disjunction(arg0: 'Iterable', arg1: 'Iterable') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.disjunction(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>)"""
        return Collection._wrap(_CollectionUtils.disjunction(arg0, arg1))

    @staticmethod
    @overload
    def addAll(arg0: 'Collection', arg1: 'Iterator') -> bool:
        """public static <C> boolean org.apache.commons.collections4.CollectionUtils.addAll(java.util.Collection<C>,java.util.Iterator<? extends C>)"""
        return bool._wrap(_CollectionUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def get(arg0: 'Map', arg1: int) -> 'Entry.Map$Entry':
        """public static <K,V> java.util.Map$Entry<K, V> org.apache.commons.collections4.CollectionUtils.get(java.util.Map<K, V>,int)"""
        return Entry.Map$Entry._wrap(_CollectionUtils.get(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def addAll(arg0: 'Collection', arg1: 'Iterable') -> bool:
        """public static <C> boolean org.apache.commons.collections4.CollectionUtils.addAll(java.util.Collection<C>,java.lang.Iterable<? extends C>)"""
        return bool._wrap(_CollectionUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def getCardinalityMap(arg0: 'Iterable') -> 'Map':
        """public static <O> java.util.Map<O, java.lang.Integer> org.apache.commons.collections4.CollectionUtils.getCardinalityMap(java.lang.Iterable<? extends O>)"""
        return Map._wrap(_CollectionUtils.getCardinalityMap(arg0))

    @staticmethod
    @overload
    def permutations(arg0: 'Collection') -> 'Collection':
        """public static <E> java.util.Collection<java.util.List<E>> org.apache.commons.collections4.CollectionUtils.permutations(java.util.Collection<E>)"""
        return Collection._wrap(_CollectionUtils.permutations(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def find(arg0: 'Iterable', arg1: 'Predicate') -> object:
        """public static <T> T org.apache.commons.collections4.CollectionUtils.find(java.lang.Iterable<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return object._wrap(_CollectionUtils.find(arg0, arg1))

    @staticmethod
    @overload
    def isEqualCollection(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.isEqualCollection(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool._wrap(_CollectionUtils.isEqualCollection(arg0, arg1))

    @staticmethod
    @overload
    def containsAny(arg0: 'Collection', *arg1: object) -> bool:
        """public static <T> boolean org.apache.commons.collections4.CollectionUtils.containsAny(java.util.Collection<?>,T...)"""
        return bool._wrap(_CollectionUtils.containsAny(arg0, arg1))

    @staticmethod
    @overload
    def isEqualCollection(arg0: 'Collection', arg1: 'Collection', arg2: 'Equator') -> bool:
        """public static <E> boolean org.apache.commons.collections4.CollectionUtils.isEqualCollection(java.util.Collection<? extends E>,java.util.Collection<? extends E>,org.apache.commons.collections4.Equator<? super E>)"""
        return bool._wrap(_CollectionUtils.isEqualCollection(arg0, arg1, arg2))

    @staticmethod
    @overload
    def size(arg0: object) -> int:
        """public static int org.apache.commons.collections4.CollectionUtils.size(java.lang.Object)"""
        return int._wrap(_CollectionUtils.size(arg0))

    @staticmethod
    @overload
    def sizeIsEmpty(arg0: object) -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.sizeIsEmpty(java.lang.Object)"""
        return bool._wrap(_CollectionUtils.sizeIsEmpty(arg0))

    @staticmethod
    @overload
    def collect(arg0: 'Iterable', arg1: 'Transformer', arg2: 'Collection') -> 'Collection':
        """public static <I,O,R extends java.util.Collection<? super O>> R org.apache.commons.collections4.CollectionUtils.collect(java.lang.Iterable<? extends I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>,R)"""
        return Collection._wrap(_CollectionUtils.collect(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def intersection(arg0: 'Iterable', arg1: 'Iterable') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.intersection(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>)"""
        return Collection._wrap(_CollectionUtils.intersection(arg0, arg1))

    @staticmethod
    @overload
    def get(arg0: object, arg1: int) -> object:
        """public static java.lang.Object org.apache.commons.collections4.CollectionUtils.get(java.lang.Object,int)"""
        return object._wrap(_CollectionUtils.get(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def get(arg0: 'Iterator', arg1: int) -> object:
        """public static <T> T org.apache.commons.collections4.CollectionUtils.get(java.util.Iterator<T>,int)"""
        return object._wrap(_CollectionUtils.get(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def transform(arg0: 'Collection', arg1: 'Transformer'):
        """public static <C> void org.apache.commons.collections4.CollectionUtils.transform(java.util.Collection<C>,org.apache.commons.collections4.Transformer<? super C, ? extends C>)"""
        _CollectionUtils.transform(arg0, arg1)

    @staticmethod
    @overload
    def filterInverse(arg0: 'Iterable', arg1: 'Predicate') -> bool:
        """public static <T> boolean org.apache.commons.collections4.CollectionUtils.filterInverse(java.lang.Iterable<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return bool._wrap(_CollectionUtils.filterInverse(arg0, arg1))

    @staticmethod
    @overload
    def collate(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Comparator', arg3: bool) -> 'List':
        """public static <O> java.util.List<O> org.apache.commons.collections4.CollectionUtils.collate(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>,java.util.Comparator<? super O>,boolean)"""
        return List._wrap(_CollectionUtils.collate(arg0, arg1, arg2, _boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def collect(arg0: 'Iterator', arg1: 'Transformer') -> 'Collection':
        """public static <I,O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.collect(java.util.Iterator<I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Collection._wrap(_CollectionUtils.collect(arg0, arg1))

    @staticmethod
    @overload
    def addAll(arg0: 'Collection', *arg1: object) -> bool:
        """public static <C> boolean org.apache.commons.collections4.CollectionUtils.addAll(java.util.Collection<C>,C...)"""
        return bool._wrap(_CollectionUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def selectRejected(arg0: 'Iterable', arg1: 'Predicate', arg2: 'Collection') -> 'Collection':
        """public static <O,R extends java.util.Collection<? super O>> R org.apache.commons.collections4.CollectionUtils.selectRejected(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>,R)"""
        return Collection._wrap(_CollectionUtils.selectRejected(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def collect(arg0: 'Iterable', arg1: 'Transformer') -> 'Collection':
        """public static <I,O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.collect(java.lang.Iterable<I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Collection._wrap(_CollectionUtils.collect(arg0, arg1))

    @staticmethod
    @overload
    def union(arg0: 'Iterable', arg1: 'Iterable') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.union(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>)"""
        return Collection._wrap(_CollectionUtils.union(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def isEmpty(arg0: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.isEmpty(java.util.Collection<?>)"""
        return bool._wrap(_CollectionUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def select(arg0: 'Iterable', arg1: 'Predicate', arg2: 'Collection', arg3: 'Collection') -> 'Collection':
        """public static <O,R extends java.util.Collection<? super O>> R org.apache.commons.collections4.CollectionUtils.select(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>,R,R)"""
        return Collection._wrap(_CollectionUtils.select(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def transformingCollection(arg0: 'Collection', arg1: 'Transformer') -> 'Collection':
        """public static <E> java.util.Collection<E> org.apache.commons.collections4.CollectionUtils.transformingCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Collection._wrap(_CollectionUtils.transformingCollection(arg0, arg1))

    @staticmethod
    @overload
    def filter(arg0: 'Iterable', arg1: 'Predicate') -> bool:
        """public static <T> boolean org.apache.commons.collections4.CollectionUtils.filter(java.lang.Iterable<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return bool._wrap(_CollectionUtils.filter(arg0, arg1))

    @staticmethod
    @overload
    def collate(arg0: 'Iterable', arg1: 'Iterable') -> 'List':
        """public static <O extends java.lang.Comparable<? super O>> java.util.List<O> org.apache.commons.collections4.CollectionUtils.collate(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>)"""
        return List._wrap(_CollectionUtils.collate(arg0, arg1))

    @staticmethod
    @overload
    def get(arg0: 'Iterable', arg1: int) -> object:
        """public static <T> T org.apache.commons.collections4.CollectionUtils.get(java.lang.Iterable<T>,int)"""
        return object._wrap(_CollectionUtils.get(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.isNotEmpty(java.util.Collection<?>)"""
        return bool._wrap(_CollectionUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def unmodifiableCollection(arg0: 'Collection') -> 'Collection':
        """public static <C> java.util.Collection<C> org.apache.commons.collections4.CollectionUtils.unmodifiableCollection(java.util.Collection<? extends C>)"""
        return Collection._wrap(_CollectionUtils.unmodifiableCollection(arg0))

    @staticmethod
    @overload
    def containsAll(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.containsAll(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool._wrap(_CollectionUtils.containsAll(arg0, arg1))

    @staticmethod
    @overload
    def isFull(arg0: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.isFull(java.util.Collection<?>)"""
        return bool._wrap(_CollectionUtils.isFull(arg0))

    @staticmethod
    @overload
    def isSubCollection(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.isSubCollection(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool._wrap(_CollectionUtils.isSubCollection(arg0, arg1))

    @staticmethod
    @overload
    def synchronizedCollection(arg0: 'Collection') -> 'Collection':
        """public static <C> java.util.Collection<C> org.apache.commons.collections4.CollectionUtils.synchronizedCollection(java.util.Collection<C>)"""
        return Collection._wrap(_CollectionUtils.synchronizedCollection(arg0))

    @staticmethod
    @overload
    def addAll(arg0: 'Collection', arg1: 'Enumeration') -> bool:
        """public static <C> boolean org.apache.commons.collections4.CollectionUtils.addAll(java.util.Collection<C>,java.util.Enumeration<? extends C>)"""
        return bool._wrap(_CollectionUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def exists(arg0: 'Iterable', arg1: 'Predicate') -> bool:
        """public static <C> boolean org.apache.commons.collections4.CollectionUtils.exists(java.lang.Iterable<C>,org.apache.commons.collections4.Predicate<? super C>)"""
        return bool._wrap(_CollectionUtils.exists(arg0, arg1))

    @staticmethod
    @overload
    def extractSingleton(arg0: 'Collection') -> object:
        """public static <E> E org.apache.commons.collections4.CollectionUtils.extractSingleton(java.util.Collection<E>)"""
        return object._wrap(_CollectionUtils.extractSingleton(arg0))

    @staticmethod
    @overload
    def subtract(arg0: 'Iterable', arg1: 'Iterable') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.subtract(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>)"""
        return Collection._wrap(_CollectionUtils.subtract(arg0, arg1))

    @staticmethod
    @overload
    def retainAll(arg0: 'Collection', arg1: 'Collection') -> 'Collection':
        """public static <C> java.util.Collection<C> org.apache.commons.collections4.CollectionUtils.retainAll(java.util.Collection<C>,java.util.Collection<?>)"""
        return Collection._wrap(_CollectionUtils.retainAll(arg0, arg1))

    @staticmethod
    @overload
    def select(arg0: 'Iterable', arg1: 'Predicate') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.select(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>)"""
        return Collection._wrap(_CollectionUtils.select(arg0, arg1))

    @staticmethod
    @overload
    def matchesAll(arg0: 'Iterable', arg1: 'Predicate') -> bool:
        """public static <C> boolean org.apache.commons.collections4.CollectionUtils.matchesAll(java.lang.Iterable<C>,org.apache.commons.collections4.Predicate<? super C>)"""
        return bool._wrap(_CollectionUtils.matchesAll(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def emptyCollection() -> 'Collection':
        """public static <T> java.util.Collection<T> org.apache.commons.collections4.CollectionUtils.emptyCollection()"""
        return Collection._wrap(_CollectionUtils.emptyCollection())

    @staticmethod
    @overload
    def addIgnoreNull(arg0: 'Collection', arg1: object) -> bool:
        """public static <T> boolean org.apache.commons.collections4.CollectionUtils.addIgnoreNull(java.util.Collection<T>,T)"""
        return bool._wrap(_CollectionUtils.addIgnoreNull(arg0, arg1))

    @staticmethod
    @overload
    def cardinality(arg0: object, arg1: 'Iterable') -> int:
        """public static <O> int org.apache.commons.collections4.CollectionUtils.cardinality(O,java.lang.Iterable<? super O>)"""
        return int._wrap(_CollectionUtils.cardinality(arg0, arg1))

    @staticmethod
    @overload
    def countMatches(arg0: 'Iterable', arg1: 'Predicate') -> int:
        """public static <C> int org.apache.commons.collections4.CollectionUtils.countMatches(java.lang.Iterable<C>,org.apache.commons.collections4.Predicate<? super C>)"""
        return int._wrap(_CollectionUtils.countMatches(arg0, arg1))

    @staticmethod
    @overload
    def collect(arg0: 'Iterator', arg1: 'Transformer', arg2: 'Collection') -> 'Collection':
        """public static <I,O,R extends java.util.Collection<? super O>> R org.apache.commons.collections4.CollectionUtils.collect(java.util.Iterator<? extends I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>,R)"""
        return Collection._wrap(_CollectionUtils.collect(arg0, arg1, arg2))

    @staticmethod
    @overload
    def collate(arg0: 'Iterable', arg1: 'Iterable', arg2: bool) -> 'List':
        """public static <O extends java.lang.Comparable<? super O>> java.util.List<O> org.apache.commons.collections4.CollectionUtils.collate(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>,boolean)"""
        return List._wrap(_CollectionUtils.collate(arg0, arg1, _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def forAllButLastDo(arg0: 'Iterator', arg1: 'Closure') -> object:
        """public static <T,C extends org.apache.commons.collections4.Closure<? super T>> T org.apache.commons.collections4.CollectionUtils.forAllButLastDo(java.util.Iterator<T>,C)"""
        return object._wrap(_CollectionUtils.forAllButLastDo(arg0, arg1))

    @staticmethod
    @overload
    def removeAll(arg0: 'Collection', arg1: 'Collection') -> 'Collection':
        """public static <E> java.util.Collection<E> org.apache.commons.collections4.CollectionUtils.removeAll(java.util.Collection<E>,java.util.Collection<?>)"""
        return Collection._wrap(_CollectionUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def collate(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Comparator') -> 'List':
        """public static <O> java.util.List<O> org.apache.commons.collections4.CollectionUtils.collate(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>,java.util.Comparator<? super O>)"""
        return List._wrap(_CollectionUtils.collate(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def selectRejected(arg0: 'Iterable', arg1: 'Predicate') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.selectRejected(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>)"""
        return Collection._wrap(_CollectionUtils.selectRejected(arg0, arg1))

    @staticmethod
    @overload
    def maxSize(arg0: 'Collection') -> int:
        """public static int org.apache.commons.collections4.CollectionUtils.maxSize(java.util.Collection<?>)"""
        return int._wrap(_CollectionUtils.maxSize(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.OrderedIterator
from pyquantum_helper import override
import org.apache.commons.collections4.OrderedIterator as _OrderedIterator
_OrderedIterator = _OrderedIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class OrderedIterator():
    """org.apache.commons.collections4.OrderedIterator"""
 
    @staticmethod
    def _wrap(java_value: _OrderedIterator) -> 'OrderedIterator':
        return OrderedIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OrderedIterator):
        """
        Dynamic initializer for OrderedIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OrderedIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OrderedIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def hasPrevious(self, ):
        """public abstract boolean org.apache.commons.collections4.OrderedIterator.hasPrevious()"""
        pass

    @abstractmethod
    def previous(self, ):
        """public abstract E org.apache.commons.collections4.OrderedIterator.previous()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @abstractmethod
    def next(self, ):
        """public abstract E java.util.Iterator.next()"""
        pass

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.IterableMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.IterableMap as _IterableMap
_IterableMap = _IterableMap
import org.apache.commons.collections4.Get as _Get
_Get = _Get
import org.apache.commons.collections4.IterableGet as _IterableGet
_IterableGet = _IterableGet
from abc import abstractmethod, ABC
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.Put as _Put
_Put = _Put
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class IterableMap():
    """org.apache.commons.collections4.IterableMap"""
 
    @staticmethod
    def _wrap(java_value: _IterableMap) -> 'IterableMap':
        return IterableMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IterableMap):
        """
        Dynamic initializer for IterableMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IterableMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IterableMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.Put.put(K,V)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V java.util.Map.put(K,V)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

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

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IterableGet.mapIterator()"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.Map.values()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.SortedBidiMap
import java.lang.Object as _Object
_Object = _Object
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.Get as _Get
_Get = _Get
import java.util.SequencedSet as _SequencedSet
_SequencedSet = _SequencedSet
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Put as _Put
_Put = _Put
import java.util.SequencedCollection as SequencedCollection
import java.util.Map.Entry as Entry
import java.util.SortedMap as _SortedMap
_SortedMap = _SortedMap
import org.apache.commons.collections4.BidiMap as _BidiMap
_BidiMap = _BidiMap
import java.util.SortedMap as SortedMap
import java.util.SequencedSet as SequencedSet
from builtins import bool
import java.util.SequencedMap as _SequencedMap
_SequencedMap = _SequencedMap
from pyquantum_helper import override
import java.util.SequencedCollection as _SequencedCollection
_SequencedCollection = _SequencedCollection
import java.lang.Object as _object
import org.apache.commons.collections4.SortedBidiMap as _SortedBidiMap
_SortedBidiMap = _SortedBidiMap
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.function.BiConsumer as BiConsumer
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import org.apache.commons.collections4.OrderedMap as _OrderedMap
_OrderedMap = _OrderedMap
import java.util.function.Function as Function
import java.util.Map as Map
 
class SortedBidiMap():
    """org.apache.commons.collections4.SortedBidiMap"""
 
    @staticmethod
    def _wrap(java_value: _SortedBidiMap) -> 'SortedBidiMap':
        return SortedBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SortedBidiMap):
        """
        Dynamic initializer for SortedBidiMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SortedBidiMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SortedBidiMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.BidiMap.getKey(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.firstKey()"""
        pass

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.OrderedMap.mapIterator()"""
        pass

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollLastEntry())

    @abstractmethod
    def nextKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.nextKey(K)"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def tailMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.tailMap(K)"""
        pass

    @abstractmethod
    def previousKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.previousKey(K)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @abstractmethod
    def firstKey(self, ):
        """public abstract K java.util.SortedMap.firstKey()"""
        pass

    @abstractmethod
    def lastKey(self, ):
        """public abstract K java.util.SortedMap.lastKey()"""
        pass

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.SortedMap.entrySet()"""
        pass

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Set<V> org.apache.commons.collections4.BidiMap.values()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V org.apache.commons.collections4.BidiMap.put(K,V)"""
        pass

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object._wrap(super(_SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).lastEntry())

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'._wrap(super(SortedMap, self).reversed())

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object._wrap(super(_SortedMap, self).putFirst(arg0, arg1))

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.SortedMap.keySet()"""
        pass

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def headMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.headMap(K)"""
        pass

    @abstractmethod
    def subMap(self, arg0: object, arg1: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.subMap(K,K)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.SortedMap.values()"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).firstEntry())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @abstractmethod
    def valueComparator(self, ):
        """public abstract java.util.Comparator<? super V> org.apache.commons.collections4.SortedBidiMap.valueComparator()"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @abstractmethod
    def removeValue(self, arg0: object):
        """public abstract K org.apache.commons.collections4.BidiMap.removeValue(java.lang.Object)"""
        pass

    @abstractmethod
    def lastKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.lastKey()"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def inverseBidiMap(self, ):
        """public abstract org.apache.commons.collections4.SortedBidiMap<V, K> org.apache.commons.collections4.SortedBidiMap.inverseBidiMap()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def comparator(self, ):
        """public abstract java.util.Comparator<? super K> java.util.SortedMap.comparator()"""
        pass

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.OrderedMapIterator
import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
from pyquantum_helper import override
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from abc import abstractmethod, ABC
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import java.util.function.Consumer as Consumer
 
class OrderedMapIterator():
    """org.apache.commons.collections4.OrderedMapIterator"""
 
    @staticmethod
    def _wrap(java_value: _OrderedMapIterator) -> 'OrderedMapIterator':
        return OrderedMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OrderedMapIterator):
        """
        Dynamic initializer for OrderedMapIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OrderedMapIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OrderedMapIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def remove(self, ):
        """public abstract void org.apache.commons.collections4.MapIterator.remove()"""
        pass

    @abstractmethod
    def previous(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMapIterator.previous()"""
        pass

    @abstractmethod
    def getValue(self, ):
        """public abstract V org.apache.commons.collections4.MapIterator.getValue()"""
        pass

    @abstractmethod
    def hasPrevious(self, ):
        """public abstract boolean org.apache.commons.collections4.OrderedMapIterator.hasPrevious()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @abstractmethod
    def next(self, ):
        """public abstract K org.apache.commons.collections4.MapIterator.next()"""
        pass

    @abstractmethod
    def getKey(self, ):
        """public abstract K org.apache.commons.collections4.MapIterator.getKey()"""
        pass

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean org.apache.commons.collections4.MapIterator.hasNext()"""
        pass

    @abstractmethod
    def setValue(self, arg0: object):
        """public abstract V org.apache.commons.collections4.MapIterator.setValue(V)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.ClosureUtils
from builtins import str
import org.apache.commons.collections4.Closure as _Closure
_Closure = _Closure
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import org.apache.commons.collections4.ClosureUtils as _ClosureUtils
_ClosureUtils = _ClosureUtils
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClosureUtils():
    """org.apache.commons.collections4.ClosureUtils"""
 
    @staticmethod
    def _wrap(java_value: _ClosureUtils) -> 'ClosureUtils':
        return ClosureUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClosureUtils):
        """
        Dynamic initializer for ClosureUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClosureUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClosureUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def switchClosure(arg0: 'Predicate', arg1: 'Closure', arg2: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.switchClosure(org.apache.commons.collections4.Predicate<? super E>[],org.apache.commons.collections4.Closure<? super E>[],org.apache.commons.collections4.Closure<? super E>)"""
        return Closure._wrap(_ClosureUtils.switchClosure(arg0, arg1, arg2))

    @staticmethod
    @overload
    def invokerClosure(arg0: str, arg1: 'Class', arg2: 'Object') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.invokerClosure(java.lang.String,java.lang.Class<?>[],java.lang.Object[])"""
        return Closure._wrap(_ClosureUtils.invokerClosure(arg0, arg1, arg2))

    @staticmethod
    @overload
    def switchClosure(arg0: 'Predicate', arg1: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.switchClosure(org.apache.commons.collections4.Predicate<? super E>[],org.apache.commons.collections4.Closure<? super E>[])"""
        return Closure._wrap(_ClosureUtils.switchClosure(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def asClosure(arg0: 'Transformer') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.asClosure(org.apache.commons.collections4.Transformer<? super E, ?>)"""
        return Closure._wrap(_ClosureUtils.asClosure(arg0))

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
    def invokerClosure(arg0: str) -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.invokerClosure(java.lang.String)"""
        return Closure._wrap(_ClosureUtils.invokerClosure(arg0))

    @staticmethod
    @overload
    def exceptionClosure() -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.exceptionClosure()"""
        return Closure._wrap(_ClosureUtils.exceptionClosure())

    @staticmethod
    @overload
    def ifClosure(arg0: 'Predicate', arg1: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.ifClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        return Closure._wrap(_ClosureUtils.ifClosure(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def doWhileClosure(arg0: 'Closure', arg1: 'Predicate') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.doWhileClosure(org.apache.commons.collections4.Closure<? super E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return Closure._wrap(_ClosureUtils.doWhileClosure(arg0, arg1))

    @staticmethod
    @overload
    def switchMapClosure(arg0: 'Map') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.switchMapClosure(java.util.Map<? extends E, org.apache.commons.collections4.Closure<E>>)"""
        return Closure._wrap(_ClosureUtils.switchMapClosure(arg0))

    @staticmethod
    @overload
    def nopClosure() -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.nopClosure()"""
        return Closure._wrap(_ClosureUtils.nopClosure())

    @staticmethod
    @overload
    def forClosure(arg0: int, arg1: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.forClosure(int,org.apache.commons.collections4.Closure<? super E>)"""
        return Closure._wrap(_ClosureUtils.forClosure(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def whileClosure(arg0: 'Predicate', arg1: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.whileClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        return Closure._wrap(_ClosureUtils.whileClosure(arg0, arg1))

    @staticmethod
    @overload
    def chainedClosure(*arg0: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.chainedClosure(org.apache.commons.collections4.Closure<? super E>...)"""
        return Closure._wrap(_ClosureUtils.chainedClosure(arg0))

    @staticmethod
    @overload
    def switchClosure(arg0: 'Map') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.switchClosure(java.util.Map<org.apache.commons.collections4.Predicate<E>, org.apache.commons.collections4.Closure<E>>)"""
        return Closure._wrap(_ClosureUtils.switchClosure(arg0))

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
    def chainedClosure(arg0: 'Collection') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.chainedClosure(java.util.Collection<? extends org.apache.commons.collections4.Closure<? super E>>)"""
        return Closure._wrap(_ClosureUtils.chainedClosure(arg0))

    @staticmethod
    @overload
    def ifClosure(arg0: 'Predicate', arg1: 'Closure', arg2: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.ifClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        return Closure._wrap(_ClosureUtils.ifClosure(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.Unmodifiable
import org.apache.commons.collections4.Unmodifiable as _Unmodifiable
_Unmodifiable = _Unmodifiable
 
class Unmodifiable():
    """org.apache.commons.collections4.Unmodifiable"""
 
    @staticmethod
    def _wrap(java_value: _Unmodifiable) -> 'Unmodifiable':
        return Unmodifiable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Unmodifiable):
        """
        Dynamic initializer for Unmodifiable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Unmodifiable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Unmodifiable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__)) 
 
 
# CLASS: org.apache.commons.collections4.Put
from abc import abstractmethod, ABC
import java.util.Map as Map
import org.apache.commons.collections4.Put as _Put
_Put = _Put
 
class Put():
    """org.apache.commons.collections4.Put"""
 
    @staticmethod
    def _wrap(java_value: _Put) -> 'Put':
        return Put(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Put):
        """
        Dynamic initializer for Put.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Put__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Put__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.Put.put(K,V)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.KeyValue
import org.apache.commons.collections4.KeyValue as _KeyValue
_KeyValue = _KeyValue
from abc import abstractmethod, ABC
 
class KeyValue():
    """org.apache.commons.collections4.KeyValue"""
 
    @staticmethod
    def _wrap(java_value: _KeyValue) -> 'KeyValue':
        return KeyValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KeyValue):
        """
        Dynamic initializer for KeyValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KeyValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KeyValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getValue(self, ):
        """public abstract V org.apache.commons.collections4.KeyValue.getValue()"""
        pass

    @abstractmethod
    def getKey(self, ):
        """public abstract K org.apache.commons.collections4.KeyValue.getKey()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.MultiSet
import java.util.function.Predicate as Predicate
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
from typing import List
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
from builtins import bool
 
class MultiSet():
    """org.apache.commons.collections4.MultiSet"""
 
    @staticmethod
    def _wrap(java_value: _MultiSet) -> 'MultiSet':
        return MultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiSet):
        """
        Dynamic initializer for MultiSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def retainAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.MultiSet.retainAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Collection.isEmpty()"""
        pass

    @abstractmethod
    def add(self, arg0: object, arg1: int):
        """public abstract int org.apache.commons.collections4.MultiSet.add(E,int)"""
        pass

    @abstractmethod
    def setCount(self, arg0: object, arg1: int):
        """public abstract int org.apache.commons.collections4.MultiSet.setCount(E,int)"""
        pass

    @abstractmethod
    def getCount(self, arg0: object):
        """public abstract int org.apache.commons.collections4.MultiSet.getCount(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object, arg1: int):
        """public abstract int org.apache.commons.collections4.MultiSet.remove(java.lang.Object,int)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.MultiSet.size()"""
        pass

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @abstractmethod
    def toArray(self, arg0: 'Object'):
        """public abstract <T> T[] java.util.Collection.toArray(T[])"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiSet.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Collection.clear()"""
        pass

    @abstractmethod
    def add(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiSet.add(E)"""
        pass

    @abstractmethod
    def uniqueSet(self, ):
        """public abstract java.util.Set<E> org.apache.commons.collections4.MultiSet.uniqueSet()"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<E> org.apache.commons.collections4.MultiSet.iterator()"""
        pass

    @abstractmethod
    def contains(self, arg0: object):
        """public abstract boolean java.util.Collection.contains(java.lang.Object)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.addAll(java.util.Collection<? extends E>)"""
        pass

    @abstractmethod
    def containsAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.MultiSet.containsAll(java.util.Collection<?>)"""
        pass

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiSet.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int org.apache.commons.collections4.MultiSet.hashCode()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.MultiSet.entrySet()"""
        pass

    @abstractmethod
    def toArray(self, ):
        """public abstract java.lang.Object[] java.util.Collection.toArray()"""
        pass

    @abstractmethod
    def removeAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.MultiSet.removeAll(java.util.Collection<?>)"""
        pass

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.SetValuedMap
import org.apache.commons.collections4.MultiValuedMap as _MultiValuedMap
_MultiValuedMap = _MultiValuedMap
import org.apache.commons.collections4.SetValuedMap as _SetValuedMap
_SetValuedMap = _SetValuedMap
import java.lang.Iterable as Iterable
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class SetValuedMap():
    """org.apache.commons.collections4.SetValuedMap"""
 
    @staticmethod
    def _wrap(java_value: _SetValuedMap) -> 'SetValuedMap':
        return SetValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SetValuedMap):
        """
        Dynamic initializer for SetValuedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SetValuedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SetValuedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.MultiValuedMap.mapIterator()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract java.util.Set<V> org.apache.commons.collections4.SetValuedMap.get(K)"""
        pass

    @abstractmethod
    def putAll(self, arg0: object, arg1: 'Iterable'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def removeMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.MultiValuedMap.clear()"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.MultiValuedMap.values()"""
        pass

    @abstractmethod
    def containsMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.isEmpty()"""
        pass

    @abstractmethod
    def keys(self, ):
        """public abstract org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.MultiValuedMap.keys()"""
        pass

    @abstractmethod
    def entries(self, ):
        """public abstract java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.MultiValuedMap.entries()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.put(K,V)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.MultiValuedMap.keySet()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'MultiValuedMap'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.MultiValuedMap.size()"""
        pass

    @abstractmethod
    def asMap(self, ):
        """public abstract java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.MultiValuedMap.asMap()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract java.util.Set<V> org.apache.commons.collections4.SetValuedMap.remove(java.lang.Object)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.ResettableIterator
import org.apache.commons.collections4.ResettableIterator as _ResettableIterator
_ResettableIterator = _ResettableIterator
from pyquantum_helper import override
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class ResettableIterator():
    """org.apache.commons.collections4.ResettableIterator"""
 
    @staticmethod
    def _wrap(java_value: _ResettableIterator) -> 'ResettableIterator':
        return ResettableIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ResettableIterator):
        """
        Dynamic initializer for ResettableIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ResettableIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ResettableIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def reset(self, ):
        """public abstract void org.apache.commons.collections4.ResettableIterator.reset()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @abstractmethod
    def next(self, ):
        """public abstract E java.util.Iterator.next()"""
        pass

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.TrieUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.TrieUtils as _TrieUtils
_TrieUtils = _TrieUtils
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.apache.commons.collections4.Trie as _Trie
_Trie = _Trie
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TrieUtils():
    """org.apache.commons.collections4.TrieUtils"""
 
    @staticmethod
    def _wrap(java_value: _TrieUtils) -> 'TrieUtils':
        return TrieUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TrieUtils):
        """
        Dynamic initializer for TrieUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TrieUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TrieUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def unmodifiableTrie(arg0: 'Trie') -> 'Trie':
        """public static <K,V> org.apache.commons.collections4.Trie<K, V> org.apache.commons.collections4.TrieUtils.unmodifiableTrie(org.apache.commons.collections4.Trie<K, ? extends V>)"""
        return Trie._wrap(_TrieUtils.unmodifiableTrie(arg0))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.MapIterator
from pyquantum_helper import override
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from abc import abstractmethod, ABC
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import java.util.function.Consumer as Consumer
 
class MapIterator():
    """org.apache.commons.collections4.MapIterator"""
 
    @staticmethod
    def _wrap(java_value: _MapIterator) -> 'MapIterator':
        return MapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapIterator):
        """
        Dynamic initializer for MapIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def remove(self, ):
        """public abstract void org.apache.commons.collections4.MapIterator.remove()"""
        pass

    @abstractmethod
    def getValue(self, ):
        """public abstract V org.apache.commons.collections4.MapIterator.getValue()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @abstractmethod
    def next(self, ):
        """public abstract K org.apache.commons.collections4.MapIterator.next()"""
        pass

    @abstractmethod
    def getKey(self, ):
        """public abstract K org.apache.commons.collections4.MapIterator.getKey()"""
        pass

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean org.apache.commons.collections4.MapIterator.hasNext()"""
        pass

    @abstractmethod
    def setValue(self, arg0: object):
        """public abstract V org.apache.commons.collections4.MapIterator.setValue(V)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.IterableUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.String as _string
import java.util.Comparator as Comparator
import org.apache.commons.collections4.IterableUtils as _IterableUtils
_IterableUtils = _IterableUtils
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class IterableUtils():
    """org.apache.commons.collections4.IterableUtils"""
 
    @staticmethod
    def _wrap(java_value: _IterableUtils) -> 'IterableUtils':
        return IterableUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IterableUtils):
        """
        Dynamic initializer for IterableUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IterableUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IterableUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def matchesAll(arg0: 'Iterable', arg1: 'Predicate') -> bool:
        """public static <E> boolean org.apache.commons.collections4.IterableUtils.matchesAll(java.lang.Iterable<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return bool._wrap(_IterableUtils.matchesAll(arg0, arg1))

    @staticmethod
    @overload
    def toList(arg0: 'Iterable') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.IterableUtils.toList(java.lang.Iterable<E>)"""
        return List._wrap(_IterableUtils.toList(arg0))

    @staticmethod
    @overload
    def loopingIterable(arg0: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.loopingIterable(java.lang.Iterable<E>)"""
        return Iterable._wrap(_IterableUtils.loopingIterable(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def first(arg0: 'Iterable') -> object:
        """public static <T> T org.apache.commons.collections4.IterableUtils.first(java.lang.Iterable<T>)"""
        return object._wrap(_IterableUtils.first(arg0))

    @staticmethod
    @overload
    def matchesAny(arg0: 'Iterable', arg1: 'Predicate') -> bool:
        """public static <E> boolean org.apache.commons.collections4.IterableUtils.matchesAny(java.lang.Iterable<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return bool._wrap(_IterableUtils.matchesAny(arg0, arg1))

    @staticmethod
    @overload
    def chainedIterable(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Iterable', arg3: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.chainedIterable(java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>)"""
        return Iterable._wrap(_IterableUtils.chainedIterable(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def reversedIterable(arg0: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.reversedIterable(java.lang.Iterable<E>)"""
        return Iterable._wrap(_IterableUtils.reversedIterable(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def zippingIterable(arg0: 'Iterable', *arg1: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.zippingIterable(java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>...)"""
        return Iterable._wrap(_IterableUtils.zippingIterable(arg0, arg1))

    @staticmethod
    @overload
    def transformedIterable(arg0: 'Iterable', arg1: 'Transformer') -> 'Iterable':
        """public static <I,O> java.lang.Iterable<O> org.apache.commons.collections4.IterableUtils.transformedIterable(java.lang.Iterable<I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Iterable._wrap(_IterableUtils.transformedIterable(arg0, arg1))

    @staticmethod
    @overload
    def find(arg0: 'Iterable', arg1: 'Predicate') -> object:
        """public static <E> E org.apache.commons.collections4.IterableUtils.find(java.lang.Iterable<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return object._wrap(_IterableUtils.find(arg0, arg1))

    @staticmethod
    @overload
    def frequency(arg0: 'Iterable', arg1: object) -> int:
        """public static <E,T extends E> int org.apache.commons.collections4.IterableUtils.frequency(java.lang.Iterable<E>,T)"""
        return int._wrap(_IterableUtils.frequency(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def get(arg0: 'Iterable', arg1: int) -> object:
        """public static <T> T org.apache.commons.collections4.IterableUtils.get(java.lang.Iterable<T>,int)"""
        return object._wrap(_IterableUtils.get(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def size(arg0: 'Iterable') -> int:
        """public static int org.apache.commons.collections4.IterableUtils.size(java.lang.Iterable<?>)"""
        return int._wrap(_IterableUtils.size(arg0))

    @staticmethod
    @overload
    def boundedIterable(arg0: 'Iterable', arg1: int) -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.boundedIterable(java.lang.Iterable<E>,long)"""
        return Iterable._wrap(_IterableUtils.boundedIterable(arg0, _long.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def toString(arg0: 'Iterable') -> str:
        """public static <E> java.lang.String org.apache.commons.collections4.IterableUtils.toString(java.lang.Iterable<E>)"""
        return str._wrap(_IterableUtils.toString(arg0))

    @staticmethod
    @overload
    def toString(arg0: 'Iterable', arg1: 'Transformer', arg2: str, arg3: str, arg4: str) -> str:
        """public static <E> java.lang.String org.apache.commons.collections4.IterableUtils.toString(java.lang.Iterable<E>,org.apache.commons.collections4.Transformer<? super E, java.lang.String>,java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_IterableUtils.toString(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def partition(arg0: 'Iterable', arg1: 'Factory', *arg2: 'Predicate') -> 'List':
        """public static <O,R extends java.util.Collection<O>> java.util.List<R> org.apache.commons.collections4.IterableUtils.partition(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Factory<R>,org.apache.commons.collections4.Predicate<? super O>...)"""
        return List._wrap(_IterableUtils.partition(arg0, arg1, arg2))

    @staticmethod
    @overload
    def unmodifiableIterable(arg0: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.unmodifiableIterable(java.lang.Iterable<E>)"""
        return Iterable._wrap(_IterableUtils.unmodifiableIterable(arg0))

    @staticmethod
    @overload
    def collatedIterable(arg0: 'Comparator', arg1: 'Iterable', arg2: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.collatedIterable(java.util.Comparator<? super E>,java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>)"""
        return Iterable._wrap(_IterableUtils.collatedIterable(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def partition(arg0: 'Iterable', *arg1: 'Predicate') -> 'List':
        """public static <O> java.util.List<java.util.List<O>> org.apache.commons.collections4.IterableUtils.partition(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>...)"""
        return List._wrap(_IterableUtils.partition(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def emptyIterable() -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.emptyIterable()"""
        return Iterable._wrap(_IterableUtils.emptyIterable())

    @staticmethod
    @overload
    def chainedIterable(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.chainedIterable(java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>)"""
        return Iterable._wrap(_IterableUtils.chainedIterable(arg0, arg1, arg2))

    @staticmethod
    @overload
    def zippingIterable(arg0: 'Iterable', arg1: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.zippingIterable(java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>)"""
        return Iterable._wrap(_IterableUtils.zippingIterable(arg0, arg1))

    @staticmethod
    @overload
    def isEmpty(arg0: 'Iterable') -> bool:
        """public static boolean org.apache.commons.collections4.IterableUtils.isEmpty(java.lang.Iterable<?>)"""
        return bool._wrap(_IterableUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def partition(arg0: 'Iterable', arg1: 'Predicate') -> 'List':
        """public static <O> java.util.List<java.util.List<O>> org.apache.commons.collections4.IterableUtils.partition(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>)"""
        return List._wrap(_IterableUtils.partition(arg0, arg1))

    @staticmethod
    @overload
    def chainedIterable(arg0: 'Iterable', arg1: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.chainedIterable(java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>)"""
        return Iterable._wrap(_IterableUtils.chainedIterable(arg0, arg1))

    @staticmethod
    @overload
    def contains(arg0: 'Iterable', arg1: object) -> bool:
        """public static <E> boolean org.apache.commons.collections4.IterableUtils.contains(java.lang.Iterable<E>,java.lang.Object)"""
        return bool._wrap(_IterableUtils.contains(arg0, arg1))

    @staticmethod
    @overload
    def chainedIterable(*arg0: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.chainedIterable(java.lang.Iterable<? extends E>...)"""
        return Iterable._wrap(_IterableUtils.chainedIterable(arg0))

    @staticmethod
    @overload
    def collatedIterable(arg0: 'Iterable', arg1: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.collatedIterable(java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>)"""
        return Iterable._wrap(_IterableUtils.collatedIterable(arg0, arg1))

    @staticmethod
    @overload
    def indexOf(arg0: 'Iterable', arg1: 'Predicate') -> int:
        """public static <E> int org.apache.commons.collections4.IterableUtils.indexOf(java.lang.Iterable<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return int._wrap(_IterableUtils.indexOf(arg0, arg1))

    @staticmethod
    @overload
    def forEach(arg0: 'Iterable', arg1: 'Closure'):
        """public static <E> void org.apache.commons.collections4.IterableUtils.forEach(java.lang.Iterable<E>,org.apache.commons.collections4.Closure<? super E>)"""
        _IterableUtils.forEach(arg0, arg1)

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.IterableUtils()"""
        val = _IterableUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def emptyIfNull(arg0: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.emptyIfNull(java.lang.Iterable<E>)"""
        return Iterable._wrap(_IterableUtils.emptyIfNull(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def uniqueIterable(arg0: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.uniqueIterable(java.lang.Iterable<E>)"""
        return Iterable._wrap(_IterableUtils.uniqueIterable(arg0))

    @staticmethod
    @overload
    def contains(arg0: 'Iterable', arg1: object, arg2: 'Equator') -> bool:
        """public static <E> boolean org.apache.commons.collections4.IterableUtils.contains(java.lang.Iterable<? extends E>,E,org.apache.commons.collections4.Equator<? super E>)"""
        return bool._wrap(_IterableUtils.contains(arg0, arg1, arg2))

    @staticmethod
    @overload
    def countMatches(arg0: 'Iterable', arg1: 'Predicate') -> int:
        """public static <E> long org.apache.commons.collections4.IterableUtils.countMatches(java.lang.Iterable<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return int._wrap(_IterableUtils.countMatches(arg0, arg1))

    @staticmethod
    @overload
    def filteredIterable(arg0: 'Iterable', arg1: 'Predicate') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.filteredIterable(java.lang.Iterable<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return Iterable._wrap(_IterableUtils.filteredIterable(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.IterableUtils()"""
        val = _IterableUtils()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def toString(arg0: 'Iterable', arg1: 'Transformer') -> str:
        """public static <E> java.lang.String org.apache.commons.collections4.IterableUtils.toString(java.lang.Iterable<E>,org.apache.commons.collections4.Transformer<? super E, java.lang.String>)"""
        return str._wrap(_IterableUtils.toString(arg0, arg1))

    @staticmethod
    @overload
    def forEachButLast(arg0: 'Iterable', arg1: 'Closure') -> object:
        """public static <E> E org.apache.commons.collections4.IterableUtils.forEachButLast(java.lang.Iterable<E>,org.apache.commons.collections4.Closure<? super E>)"""
        return object._wrap(_IterableUtils.forEachButLast(arg0, arg1))

    @staticmethod
    @overload
    def skippingIterable(arg0: 'Iterable', arg1: int) -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.skippingIterable(java.lang.Iterable<E>,long)"""
        return Iterable._wrap(_IterableUtils.skippingIterable(arg0, _long.valueOf(arg1))) 
 
 
# CLASS: org.apache.commons.collections4.IteratorUtils
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.iterators.ZippingIterator as _ZippingIterator
_ZippingIterator = _ZippingIterator
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import java.lang.String as _string
import org.w3c.dom.NodeList as NodeList
import java.util.Enumeration as Enumeration
try:
    from pyapache.collections4 import iterators
except ImportError:
    iterators = _import_once("pyapache.collections4.iterators")

import org.apache.commons.collections4.iterators.SkippingIterator as _SkippingIterator
_SkippingIterator = _SkippingIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.w3c.dom.Node as Node
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.ResettableListIterator as _ResettableListIterator
_ResettableListIterator = _ResettableListIterator
import java.util.Enumeration as _Enumeration
_Enumeration = _Enumeration
import java.lang.Object as _object
import java.lang.Iterable as Iterable
import org.apache.commons.collections4.IteratorUtils as _IteratorUtils
_IteratorUtils = _IteratorUtils
import org.apache.commons.collections4.OrderedIterator as _OrderedIterator
_OrderedIterator = _OrderedIterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.util.Comparator as Comparator
import org.apache.commons.collections4.ResettableIterator as _ResettableIterator
_ResettableIterator = _ResettableIterator
import org.apache.commons.collections4.iterators.NodeListIterator as _NodeListIterator
_NodeListIterator = _NodeListIterator
import java.util.ListIterator as ListIterator
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import org.apache.commons.collections4.iterators.BoundedIterator as _BoundedIterator
_BoundedIterator = _BoundedIterator
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class IteratorUtils():
    """org.apache.commons.collections4.IteratorUtils"""
 
    @staticmethod
    def _wrap(java_value: _IteratorUtils) -> 'IteratorUtils':
        return IteratorUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IteratorUtils):
        """
        Dynamic initializer for IteratorUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IteratorUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IteratorUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def collatedIterator(arg0: 'Comparator', arg1: 'Iterator', arg2: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.collatedIterator(java.util.Comparator<? super E>,java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        return Iterator._wrap(_IteratorUtils.collatedIterator(arg0, arg1, arg2))

    @staticmethod
    @overload
    def pushbackIterator(arg0: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.pushbackIterator(java.util.Iterator<? extends E>)"""
        return Iterator._wrap(_IteratorUtils.pushbackIterator(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def boundedIterator(arg0: 'Iterator', arg1: int) -> 'iterators.BoundedIterator':
        """public static <E> org.apache.commons.collections4.iterators.BoundedIterator<E> org.apache.commons.collections4.IteratorUtils.boundedIterator(java.util.Iterator<? extends E>,long)"""
        return iterators.BoundedIterator._wrap(_IteratorUtils.boundedIterator(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def collatedIterator(arg0: 'Comparator', arg1: 'Collection') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.collatedIterator(java.util.Comparator<? super E>,java.util.Collection<java.util.Iterator<? extends E>>)"""
        return Iterator._wrap(_IteratorUtils.collatedIterator(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def indexOf(arg0: 'Iterator', arg1: 'Predicate') -> int:
        """public static <E> int org.apache.commons.collections4.IteratorUtils.indexOf(java.util.Iterator<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return int._wrap(_IteratorUtils.indexOf(arg0, arg1))

    @staticmethod
    @overload
    def arrayIterator(arg0: object) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.arrayIterator(java.lang.Object)"""
        return ResettableIterator._wrap(_IteratorUtils.arrayIterator(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def arrayListIterator(arg0: object, arg1: int, arg2: int) -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.arrayListIterator(java.lang.Object,int,int)"""
        return ResettableListIterator._wrap(_IteratorUtils.arrayListIterator(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def toArray(arg0: 'Iterator', arg1: 'Class') -> List[object]:
        """public static <E> E[] org.apache.commons.collections4.IteratorUtils.toArray(java.util.Iterator<? extends E>,java.lang.Class<E>)"""
        return List[object]._wrap(_IteratorUtils.toArray(arg0, arg1))

    @staticmethod
    @overload
    def isEmpty(arg0: 'Iterator') -> bool:
        """public static boolean org.apache.commons.collections4.IteratorUtils.isEmpty(java.util.Iterator<?>)"""
        return bool._wrap(_IteratorUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def emptyIterator() -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.emptyIterator()"""
        return ResettableIterator._wrap(_IteratorUtils.emptyIterator())

    @staticmethod
    @overload
    def zippingIterator(arg0: 'Iterator', arg1: 'Iterator') -> 'iterators.ZippingIterator':
        """public static <E> org.apache.commons.collections4.iterators.ZippingIterator<E> org.apache.commons.collections4.IteratorUtils.zippingIterator(java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        return iterators.ZippingIterator._wrap(_IteratorUtils.zippingIterator(arg0, arg1))

    @staticmethod
    @overload
    def matchesAny(arg0: 'Iterator', arg1: 'Predicate') -> bool:
        """public static <E> boolean org.apache.commons.collections4.IteratorUtils.matchesAny(java.util.Iterator<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return bool._wrap(_IteratorUtils.matchesAny(arg0, arg1))

    @staticmethod
    @overload
    def transformedIterator(arg0: 'Iterator', arg1: 'Transformer') -> 'Iterator':
        """public static <I,O> java.util.Iterator<O> org.apache.commons.collections4.IteratorUtils.transformedIterator(java.util.Iterator<? extends I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Iterator._wrap(_IteratorUtils.transformedIterator(arg0, arg1))

    @staticmethod
    @overload
    def matchesAll(arg0: 'Iterator', arg1: 'Predicate') -> bool:
        """public static <E> boolean org.apache.commons.collections4.IteratorUtils.matchesAll(java.util.Iterator<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return bool._wrap(_IteratorUtils.matchesAll(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableIterator(arg0: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.unmodifiableIterator(java.util.Iterator<E>)"""
        return Iterator._wrap(_IteratorUtils.unmodifiableIterator(arg0))

    @staticmethod
    @overload
    def emptyListIterator() -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.emptyListIterator()"""
        return ResettableListIterator._wrap(_IteratorUtils.emptyListIterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def toList(arg0: 'Iterator', arg1: int) -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.IteratorUtils.toList(java.util.Iterator<? extends E>,int)"""
        return List._wrap(_IteratorUtils.toList(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def chainedIterator(*arg0: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.chainedIterator(java.util.Iterator<? extends E>...)"""
        return Iterator._wrap(_IteratorUtils.chainedIterator(arg0))

    @staticmethod
    @overload
    def arrayIterator(arg0: 'Object', arg1: int) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.arrayIterator(E[],int)"""
        return ResettableIterator._wrap(_IteratorUtils.arrayIterator(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def arrayIterator(arg0: object, arg1: int) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.arrayIterator(java.lang.Object,int)"""
        return ResettableIterator._wrap(_IteratorUtils.arrayIterator(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def unmodifiableMapIterator(arg0: 'MapIterator') -> 'MapIterator':
        """public static <K,V> org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IteratorUtils.unmodifiableMapIterator(org.apache.commons.collections4.MapIterator<K, V>)"""
        return MapIterator._wrap(_IteratorUtils.unmodifiableMapIterator(arg0))

    @staticmethod
    @overload
    def toString(arg0: 'Iterator', arg1: 'Transformer', arg2: str, arg3: str, arg4: str) -> str:
        """public static <E> java.lang.String org.apache.commons.collections4.IteratorUtils.toString(java.util.Iterator<E>,org.apache.commons.collections4.Transformer<? super E, java.lang.String>,java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_IteratorUtils.toString(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def emptyMapIterator() -> 'MapIterator':
        """public static <K,V> org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IteratorUtils.emptyMapIterator()"""
        return MapIterator._wrap(_IteratorUtils.emptyMapIterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def arrayListIterator(arg0: object, arg1: int) -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.arrayListIterator(java.lang.Object,int)"""
        return ResettableListIterator._wrap(_IteratorUtils.arrayListIterator(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def unmodifiableListIterator(arg0: 'ListIterator') -> 'ListIterator':
        """public static <E> java.util.ListIterator<E> org.apache.commons.collections4.IteratorUtils.unmodifiableListIterator(java.util.ListIterator<E>)"""
        return ListIterator._wrap(_IteratorUtils.unmodifiableListIterator(arg0))

    @staticmethod
    @overload
    def zippingIterator(arg0: 'Iterator', arg1: 'Iterator', arg2: 'Iterator') -> 'iterators.ZippingIterator':
        """public static <E> org.apache.commons.collections4.iterators.ZippingIterator<E> org.apache.commons.collections4.IteratorUtils.zippingIterator(java.util.Iterator<? extends E>,java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        return iterators.ZippingIterator._wrap(_IteratorUtils.zippingIterator(arg0, arg1, arg2))

    @staticmethod
    @overload
    def size(arg0: 'Iterator') -> int:
        """public static int org.apache.commons.collections4.IteratorUtils.size(java.util.Iterator<?>)"""
        return int._wrap(_IteratorUtils.size(arg0))

    @staticmethod
    @overload
    def forEachButLast(arg0: 'Iterator', arg1: 'Closure') -> object:
        """public static <E> E org.apache.commons.collections4.IteratorUtils.forEachButLast(java.util.Iterator<E>,org.apache.commons.collections4.Closure<? super E>)"""
        return object._wrap(_IteratorUtils.forEachButLast(arg0, arg1))

    @staticmethod
    @overload
    def toString(arg0: 'Iterator', arg1: 'Transformer') -> str:
        """public static <E> java.lang.String org.apache.commons.collections4.IteratorUtils.toString(java.util.Iterator<E>,org.apache.commons.collections4.Transformer<? super E, java.lang.String>)"""
        return str._wrap(_IteratorUtils.toString(arg0, arg1))

    @staticmethod
    @overload
    def toList(arg0: 'Iterator') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.IteratorUtils.toList(java.util.Iterator<? extends E>)"""
        return List._wrap(_IteratorUtils.toList(arg0))

    @staticmethod
    @overload
    def getIterator(arg0: object) -> 'Iterator':
        """public static java.util.Iterator<?> org.apache.commons.collections4.IteratorUtils.getIterator(java.lang.Object)"""
        return Iterator._wrap(_IteratorUtils.getIterator(arg0))

    @staticmethod
    @overload
    def chainedIterator(arg0: 'Collection') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.chainedIterator(java.util.Collection<java.util.Iterator<? extends E>>)"""
        return Iterator._wrap(_IteratorUtils.chainedIterator(arg0))

    @staticmethod
    @overload
    def nodeListIterator(arg0: 'Node') -> 'iterators.NodeListIterator':
        """public static org.apache.commons.collections4.iterators.NodeListIterator org.apache.commons.collections4.IteratorUtils.nodeListIterator(org.w3c.dom.Node)"""
        return iterators.NodeListIterator._wrap(_IteratorUtils.nodeListIterator(arg0))

    @staticmethod
    @overload
    def singletonListIterator(arg0: object) -> 'ListIterator':
        """public static <E> java.util.ListIterator<E> org.apache.commons.collections4.IteratorUtils.singletonListIterator(E)"""
        return ListIterator._wrap(_IteratorUtils.singletonListIterator(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def get(arg0: 'Iterator', arg1: int) -> object:
        """public static <E> E org.apache.commons.collections4.IteratorUtils.get(java.util.Iterator<E>,int)"""
        return object._wrap(_IteratorUtils.get(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def asEnumeration(arg0: 'Iterator') -> 'Enumeration':
        """public static <E> java.util.Enumeration<E> org.apache.commons.collections4.IteratorUtils.asEnumeration(java.util.Iterator<? extends E>)"""
        return Enumeration._wrap(_IteratorUtils.asEnumeration(arg0))

    @staticmethod
    @overload
    def collatedIterator(arg0: 'Comparator', *arg1: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.collatedIterator(java.util.Comparator<? super E>,java.util.Iterator<? extends E>...)"""
        return Iterator._wrap(_IteratorUtils.collatedIterator(arg0, arg1))

    @staticmethod
    @overload
    def filteredListIterator(arg0: 'ListIterator', arg1: 'Predicate') -> 'ListIterator':
        """public static <E> java.util.ListIterator<E> org.apache.commons.collections4.IteratorUtils.filteredListIterator(java.util.ListIterator<? extends E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return ListIterator._wrap(_IteratorUtils.filteredListIterator(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def emptyOrderedMapIterator() -> 'OrderedMapIterator':
        """public static <K,V> org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.IteratorUtils.emptyOrderedMapIterator()"""
        return OrderedMapIterator._wrap(_IteratorUtils.emptyOrderedMapIterator())

    @staticmethod
    @overload
    def arrayIterator(*arg0: object) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.arrayIterator(E...)"""
        return ResettableIterator._wrap(_IteratorUtils.arrayIterator(arg0))

    @staticmethod
    @overload
    def arrayIterator(arg0: 'Object', arg1: int, arg2: int) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.arrayIterator(E[],int,int)"""
        return ResettableIterator._wrap(_IteratorUtils.arrayIterator(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def arrayListIterator(arg0: object) -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.arrayListIterator(java.lang.Object)"""
        return ResettableListIterator._wrap(_IteratorUtils.arrayListIterator(arg0))

    @staticmethod
    @overload
    def loopingIterator(arg0: 'Collection') -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.loopingIterator(java.util.Collection<? extends E>)"""
        return ResettableIterator._wrap(_IteratorUtils.loopingIterator(arg0))

    @staticmethod
    @overload
    def contains(arg0: 'Iterator', arg1: object) -> bool:
        """public static <E> boolean org.apache.commons.collections4.IteratorUtils.contains(java.util.Iterator<E>,java.lang.Object)"""
        return bool._wrap(_IteratorUtils.contains(arg0, arg1))

    @staticmethod
    @overload
    def chainedIterator(arg0: 'Iterator', arg1: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.chainedIterator(java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        return Iterator._wrap(_IteratorUtils.chainedIterator(arg0, arg1))

    @staticmethod
    @overload
    def arrayIterator(arg0: object, arg1: int, arg2: int) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.arrayIterator(java.lang.Object,int,int)"""
        return ResettableIterator._wrap(_IteratorUtils.arrayIterator(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def toString(arg0: 'Iterator') -> str:
        """public static <E> java.lang.String org.apache.commons.collections4.IteratorUtils.toString(java.util.Iterator<E>)"""
        return str._wrap(_IteratorUtils.toString(arg0))

    @staticmethod
    @overload
    def toArray(arg0: 'Iterator') -> List[object]:
        """public static java.lang.Object[] org.apache.commons.collections4.IteratorUtils.toArray(java.util.Iterator<?>)"""
        return List[object]._wrap(_IteratorUtils.toArray(arg0))

    @staticmethod
    @overload
    def forEach(arg0: 'Iterator', arg1: 'Closure'):
        """public static <E> void org.apache.commons.collections4.IteratorUtils.forEach(java.util.Iterator<E>,org.apache.commons.collections4.Closure<? super E>)"""
        _IteratorUtils.forEach(arg0, arg1)

    @staticmethod
    @overload
    def toListIterator(arg0: 'Iterator') -> 'ListIterator':
        """public static <E> java.util.ListIterator<E> org.apache.commons.collections4.IteratorUtils.toListIterator(java.util.Iterator<? extends E>)"""
        return ListIterator._wrap(_IteratorUtils.toListIterator(arg0))

    @staticmethod
    @overload
    def boundedIterator(arg0: 'Iterator', arg1: int, arg2: int) -> 'iterators.BoundedIterator':
        """public static <E> org.apache.commons.collections4.iterators.BoundedIterator<E> org.apache.commons.collections4.IteratorUtils.boundedIterator(java.util.Iterator<? extends E>,long,long)"""
        return iterators.BoundedIterator._wrap(_IteratorUtils.boundedIterator(arg0, _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def peekingIterator(arg0: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.peekingIterator(java.util.Iterator<? extends E>)"""
        return Iterator._wrap(_IteratorUtils.peekingIterator(arg0))

    @staticmethod
    @overload
    def objectGraphIterator(arg0: object, arg1: 'Transformer') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.objectGraphIterator(E,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Iterator._wrap(_IteratorUtils.objectGraphIterator(arg0, arg1))

    @staticmethod
    @overload
    def loopingListIterator(arg0: 'List') -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.loopingListIterator(java.util.List<E>)"""
        return ResettableListIterator._wrap(_IteratorUtils.loopingListIterator(arg0))

    @staticmethod
    @overload
    def skippingIterator(arg0: 'Iterator', arg1: int) -> 'iterators.SkippingIterator':
        """public static <E> org.apache.commons.collections4.iterators.SkippingIterator<E> org.apache.commons.collections4.IteratorUtils.skippingIterator(java.util.Iterator<E>,long)"""
        return iterators.SkippingIterator._wrap(_IteratorUtils.skippingIterator(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def filteredIterator(arg0: 'Iterator', arg1: 'Predicate') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.filteredIterator(java.util.Iterator<? extends E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return Iterator._wrap(_IteratorUtils.filteredIterator(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def zippingIterator(*arg0: 'Iterator') -> 'iterators.ZippingIterator':
        """public static <E> org.apache.commons.collections4.iterators.ZippingIterator<E> org.apache.commons.collections4.IteratorUtils.zippingIterator(java.util.Iterator<? extends E>...)"""
        return iterators.ZippingIterator._wrap(_IteratorUtils.zippingIterator(arg0))

    @staticmethod
    @overload
    def asIterable(arg0: 'Iterator') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IteratorUtils.asIterable(java.util.Iterator<? extends E>)"""
        return Iterable._wrap(_IteratorUtils.asIterable(arg0))

    @staticmethod
    @overload
    def nodeListIterator(arg0: 'NodeList') -> 'iterators.NodeListIterator':
        """public static org.apache.commons.collections4.iterators.NodeListIterator org.apache.commons.collections4.IteratorUtils.nodeListIterator(org.w3c.dom.NodeList)"""
        return iterators.NodeListIterator._wrap(_IteratorUtils.nodeListIterator(arg0))

    @staticmethod
    @overload
    def asMultipleUseIterable(arg0: 'Iterator') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IteratorUtils.asMultipleUseIterable(java.util.Iterator<? extends E>)"""
        return Iterable._wrap(_IteratorUtils.asMultipleUseIterable(arg0))

    @staticmethod
    @overload
    def arrayListIterator(arg0: 'Object', arg1: int) -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.arrayListIterator(E[],int)"""
        return ResettableListIterator._wrap(_IteratorUtils.arrayListIterator(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def find(arg0: 'Iterator', arg1: 'Predicate') -> object:
        """public static <E> E org.apache.commons.collections4.IteratorUtils.find(java.util.Iterator<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return object._wrap(_IteratorUtils.find(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def arrayListIterator(arg0: 'Object', arg1: int, arg2: int) -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.arrayListIterator(E[],int,int)"""
        return ResettableListIterator._wrap(_IteratorUtils.arrayListIterator(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def emptyOrderedIterator() -> 'OrderedIterator':
        """public static <E> org.apache.commons.collections4.OrderedIterator<E> org.apache.commons.collections4.IteratorUtils.emptyOrderedIterator()"""
        return OrderedIterator._wrap(_IteratorUtils.emptyOrderedIterator())

    @staticmethod
    @overload
    def asIterator(arg0: 'Enumeration') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.asIterator(java.util.Enumeration<? extends E>)"""
        return Iterator._wrap(_IteratorUtils.asIterator(arg0))

    @staticmethod
    @overload
    def arrayListIterator(*arg0: object) -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.arrayListIterator(E...)"""
        return ResettableListIterator._wrap(_IteratorUtils.arrayListIterator(arg0))

    @staticmethod
    @overload
    def singletonIterator(arg0: object) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.singletonIterator(E)"""
        return ResettableIterator._wrap(_IteratorUtils.singletonIterator(arg0))

    @staticmethod
    @overload
    def first(arg0: 'Iterator') -> object:
        """public static <E> E org.apache.commons.collections4.IteratorUtils.first(java.util.Iterator<E>)"""
        return object._wrap(_IteratorUtils.first(arg0))

    @staticmethod
    @overload
    def asIterator(arg0: 'Enumeration', arg1: 'Collection') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.asIterator(java.util.Enumeration<? extends E>,java.util.Collection<? super E>)"""
        return Iterator._wrap(_IteratorUtils.asIterator(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.MultiSetUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.MultiSetUtils as _MultiSetUtils
_MultiSetUtils = _MultiSetUtils
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MultiSetUtils():
    """org.apache.commons.collections4.MultiSetUtils"""
 
    @staticmethod
    def _wrap(java_value: _MultiSetUtils) -> 'MultiSetUtils':
        return MultiSetUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiSetUtils):
        """
        Dynamic initializer for MultiSetUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiSetUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiSetUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def unmodifiableMultiSet(arg0: 'MultiSet') -> 'MultiSet':
        """public static <E> org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.MultiSetUtils.unmodifiableMultiSet(org.apache.commons.collections4.MultiSet<? extends E>)"""
        return MultiSet._wrap(_MultiSetUtils.unmodifiableMultiSet(arg0))

    @staticmethod
    @overload
    def emptyMultiSet() -> 'MultiSet':
        """public static <E> org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.MultiSetUtils.emptyMultiSet()"""
        return MultiSet._wrap(_MultiSetUtils.emptyMultiSet())

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
    def synchronizedMultiSet(arg0: 'MultiSet') -> 'MultiSet':
        """public static <E> org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.MultiSetUtils.synchronizedMultiSet(org.apache.commons.collections4.MultiSet<E>)"""
        return MultiSet._wrap(_MultiSetUtils.synchronizedMultiSet(arg0))

    @staticmethod
    @overload
    def predicatedMultiSet(arg0: 'MultiSet', arg1: 'Predicate') -> 'MultiSet':
        """public static <E> org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.MultiSetUtils.predicatedMultiSet(org.apache.commons.collections4.MultiSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return MultiSet._wrap(_MultiSetUtils.predicatedMultiSet(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.ListUtils
from builtins import str
import java.lang.CharSequence as CharSequence
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
import java.lang.Integer as _int
import org.apache.commons.collections4.ListUtils as _ListUtils
_ListUtils = _ListUtils
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ListUtils():
    """org.apache.commons.collections4.ListUtils"""
 
    @staticmethod
    def _wrap(java_value: _ListUtils) -> 'ListUtils':
        return ListUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ListUtils):
        """
        Dynamic initializer for ListUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ListUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ListUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def longestCommonSubsequence(arg0: 'List', arg1: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.longestCommonSubsequence(java.util.List<E>,java.util.List<E>)"""
        return List._wrap(_ListUtils.longestCommonSubsequence(arg0, arg1))

    @staticmethod
    @overload
    def partition(arg0: 'List', arg1: int) -> 'List':
        """public static <T> java.util.List<java.util.List<T>> org.apache.commons.collections4.ListUtils.partition(java.util.List<T>,int)"""
        return List._wrap(_ListUtils.partition(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def defaultIfNull(arg0: 'List', arg1: 'List') -> 'List':
        """public static <T> java.util.List<T> org.apache.commons.collections4.ListUtils.defaultIfNull(java.util.List<T>,java.util.List<T>)"""
        return List._wrap(_ListUtils.defaultIfNull(arg0, arg1))

    @staticmethod
    @overload
    def transformedList(arg0: 'List', arg1: 'Transformer') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.transformedList(java.util.List<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return List._wrap(_ListUtils.transformedList(arg0, arg1))

    @staticmethod
    @overload
    def isEqualList(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.ListUtils.isEqualList(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool._wrap(_ListUtils.isEqualList(arg0, arg1))

    @staticmethod
    @overload
    def retainAll(arg0: 'Collection', arg1: 'Collection') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.retainAll(java.util.Collection<E>,java.util.Collection<?>)"""
        return List._wrap(_ListUtils.retainAll(arg0, arg1))

    @staticmethod
    @overload
    def removeAll(arg0: 'Collection', arg1: 'Collection') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.removeAll(java.util.Collection<E>,java.util.Collection<?>)"""
        return List._wrap(_ListUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def subtract(arg0: 'List', arg1: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.subtract(java.util.List<E>,java.util.List<? extends E>)"""
        return List._wrap(_ListUtils.subtract(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def fixedSizeList(arg0: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.fixedSizeList(java.util.List<E>)"""
        return List._wrap(_ListUtils.fixedSizeList(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def union(arg0: 'List', arg1: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.union(java.util.List<? extends E>,java.util.List<? extends E>)"""
        return List._wrap(_ListUtils.union(arg0, arg1))

    @staticmethod
    @overload
    def emptyIfNull(arg0: 'List') -> 'List':
        """public static <T> java.util.List<T> org.apache.commons.collections4.ListUtils.emptyIfNull(java.util.List<T>)"""
        return List._wrap(_ListUtils.emptyIfNull(arg0))

    @staticmethod
    @overload
    def unmodifiableList(arg0: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.unmodifiableList(java.util.List<? extends E>)"""
        return List._wrap(_ListUtils.unmodifiableList(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def predicatedList(arg0: 'List', arg1: 'Predicate') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.predicatedList(java.util.List<E>,org.apache.commons.collections4.Predicate<E>)"""
        return List._wrap(_ListUtils.predicatedList(arg0, arg1))

    @staticmethod
    @overload
    def hashCodeForList(arg0: 'Collection') -> int:
        """public static int org.apache.commons.collections4.ListUtils.hashCodeForList(java.util.Collection<?>)"""
        return int._wrap(_ListUtils.hashCodeForList(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def intersection(arg0: 'List', arg1: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.intersection(java.util.List<? extends E>,java.util.List<? extends E>)"""
        return List._wrap(_ListUtils.intersection(arg0, arg1))

    @staticmethod
    @overload
    def lazyList(arg0: 'List', arg1: 'Transformer') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.lazyList(java.util.List<E>,org.apache.commons.collections4.Transformer<java.lang.Integer, ? extends E>)"""
        return List._wrap(_ListUtils.lazyList(arg0, arg1))

    @staticmethod
    @overload
    def longestCommonSubsequence(arg0: 'CharSequence', arg1: 'CharSequence') -> str:
        """public static java.lang.String org.apache.commons.collections4.ListUtils.longestCommonSubsequence(java.lang.CharSequence,java.lang.CharSequence)"""
        return str._wrap(_ListUtils.longestCommonSubsequence(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def select(arg0: 'Collection', arg1: 'Predicate') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.select(java.util.Collection<? extends E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return List._wrap(_ListUtils.select(arg0, arg1))

    @staticmethod
    @overload
    def selectRejected(arg0: 'Collection', arg1: 'Predicate') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.selectRejected(java.util.Collection<? extends E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return List._wrap(_ListUtils.selectRejected(arg0, arg1))

    @staticmethod
    @overload
    def longestCommonSubsequence(arg0: 'List', arg1: 'List', arg2: 'Equator') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.longestCommonSubsequence(java.util.List<E>,java.util.List<E>,org.apache.commons.collections4.Equator<? super E>)"""
        return List._wrap(_ListUtils.longestCommonSubsequence(arg0, arg1, arg2))

    @staticmethod
    @overload
    def synchronizedList(arg0: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.synchronizedList(java.util.List<E>)"""
        return List._wrap(_ListUtils.synchronizedList(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def sum(arg0: 'List', arg1: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.sum(java.util.List<? extends E>,java.util.List<? extends E>)"""
        return List._wrap(_ListUtils.sum(arg0, arg1))

    @staticmethod
    @overload
    def indexOf(arg0: 'List', arg1: 'Predicate') -> int:
        """public static <E> int org.apache.commons.collections4.ListUtils.indexOf(java.util.List<E>,org.apache.commons.collections4.Predicate<E>)"""
        return int._wrap(_ListUtils.indexOf(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def lazyList(arg0: 'List', arg1: 'Factory') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.lazyList(java.util.List<E>,org.apache.commons.collections4.Factory<? extends E>)"""
        return List._wrap(_ListUtils.lazyList(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.OrderedMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.Get as _Get
_Get = _Get
from abc import abstractmethod, ABC
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.Put as _Put
_Put = _Put
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.OrderedMap as _OrderedMap
_OrderedMap = _OrderedMap
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class OrderedMap():
    """org.apache.commons.collections4.OrderedMap"""
 
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
 
    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.Put.put(K,V)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.firstKey()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V java.util.Map.put(K,V)"""
        pass

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.OrderedMap.mapIterator()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @abstractmethod
    def nextKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.nextKey(K)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def previousKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.previousKey(K)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

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

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @abstractmethod
    def lastKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.lastKey()"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.Map.values()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.BidiMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.Get as _Get
_Get = _Get
import org.apache.commons.collections4.IterableGet as _IterableGet
_IterableGet = _IterableGet
from abc import abstractmethod, ABC
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.Put as _Put
_Put = _Put
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.BidiMap as _BidiMap
_BidiMap = _BidiMap
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class BidiMap():
    """org.apache.commons.collections4.BidiMap"""
 
    @staticmethod
    def _wrap(java_value: _BidiMap) -> 'BidiMap':
        return BidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BidiMap):
        """
        Dynamic initializer for BidiMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BidiMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BidiMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def getKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.BidiMap.getKey(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

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

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IterableGet.mapIterator()"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Set<V> org.apache.commons.collections4.BidiMap.values()"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V org.apache.commons.collections4.BidiMap.put(K,V)"""
        pass

    @abstractmethod
    def removeValue(self, arg0: object):
        """public abstract K org.apache.commons.collections4.BidiMap.removeValue(java.lang.Object)"""
        pass

    @abstractmethod
    def inverseBidiMap(self, ):
        """public abstract org.apache.commons.collections4.BidiMap<V, K> org.apache.commons.collections4.BidiMap.inverseBidiMap()"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

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
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.Bag
import java.util.function.Predicate as Predicate
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.Bag as _Bag
_Bag = _Bag
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
from typing import List
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
from builtins import bool
 
class Bag():
    """org.apache.commons.collections4.Bag"""
 
    @staticmethod
    def _wrap(java_value: _Bag) -> 'Bag':
        return Bag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Bag):
        """
        Dynamic initializer for Bag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Bag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Bag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def add(self, arg0: object, arg1: int):
        """public abstract boolean org.apache.commons.collections4.Bag.add(E,int)"""
        pass

    @abstractmethod
    def removeAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.Bag.removeAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Collection.isEmpty()"""
        pass

    @abstractmethod
    def uniqueSet(self, ):
        """public abstract java.util.Set<E> org.apache.commons.collections4.Bag.uniqueSet()"""
        pass

    @abstractmethod
    def getCount(self, arg0: object):
        """public abstract int org.apache.commons.collections4.Bag.getCount(java.lang.Object)"""
        pass

    @abstractmethod
    def containsAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.Bag.containsAll(java.util.Collection<?>)"""
        pass

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @abstractmethod
    def remove(self, arg0: object, arg1: int):
        """public abstract boolean org.apache.commons.collections4.Bag.remove(java.lang.Object,int)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Bag.size()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Collection.hashCode()"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @abstractmethod
    def toArray(self, arg0: 'Object'):
        """public abstract <T> T[] java.util.Collection.toArray(T[])"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Collection.clear()"""
        pass

    @abstractmethod
    def retainAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.Bag.retainAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Collection.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def contains(self, arg0: object):
        """public abstract boolean java.util.Collection.contains(java.lang.Object)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.addAll(java.util.Collection<? extends E>)"""
        pass

    @abstractmethod
    def add(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Bag.add(E)"""
        pass

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @abstractmethod
    def toArray(self, ):
        """public abstract java.lang.Object[] java.util.Collection.toArray()"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<E> org.apache.commons.collections4.Bag.iterator()"""
        pass

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Bag.remove(java.lang.Object)"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.MultiMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.Get as _Get
_Get = _Get
import org.apache.commons.collections4.IterableGet as _IterableGet
_IterableGet = _IterableGet
from abc import abstractmethod, ABC
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.Put as _Put
_Put = _Put
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.MultiMap as _MultiMap
_MultiMap = _MultiMap
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class MultiMap():
    """org.apache.commons.collections4.MultiMap"""
 
    @staticmethod
    def _wrap(java_value: _MultiMap) -> 'MultiMap':
        return MultiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiMap):
        """
        Dynamic initializer for MultiMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.MultiMap.put(K,java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract java.lang.Object org.apache.commons.collections4.MultiMap.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.MultiMap.size()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiMap.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @abstractmethod
    def removeMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiMap.removeMapping(K,V)"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IterableGet.mapIterator()"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @abstractmethod
    def get(self, arg0: object):
        """public abstract java.lang.Object org.apache.commons.collections4.MultiMap.get(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<java.lang.Object> org.apache.commons.collections4.MultiMap.values()"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

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
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.ListValuedMap
import org.apache.commons.collections4.MultiValuedMap as _MultiValuedMap
_MultiValuedMap = _MultiValuedMap
import java.lang.Iterable as Iterable
import org.apache.commons.collections4.ListValuedMap as _ListValuedMap
_ListValuedMap = _ListValuedMap
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class ListValuedMap():
    """org.apache.commons.collections4.ListValuedMap"""
 
    @staticmethod
    def _wrap(java_value: _ListValuedMap) -> 'ListValuedMap':
        return ListValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ListValuedMap):
        """
        Dynamic initializer for ListValuedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ListValuedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ListValuedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.MultiValuedMap.mapIterator()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract java.util.List<V> org.apache.commons.collections4.ListValuedMap.get(K)"""
        pass

    @abstractmethod
    def putAll(self, arg0: object, arg1: 'Iterable'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def removeMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.MultiValuedMap.clear()"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.MultiValuedMap.values()"""
        pass

    @abstractmethod
    def containsMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.isEmpty()"""
        pass

    @abstractmethod
    def keys(self, ):
        """public abstract org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.MultiValuedMap.keys()"""
        pass

    @abstractmethod
    def entries(self, ):
        """public abstract java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.MultiValuedMap.entries()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.put(K,V)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.MultiValuedMap.keySet()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'MultiValuedMap'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.MultiValuedMap.size()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract java.util.List<V> org.apache.commons.collections4.ListValuedMap.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def asMap(self, ):
        """public abstract java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.MultiValuedMap.asMap()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.Equator
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Equator as _Equator
_Equator = _Equator
 
class Equator():
    """org.apache.commons.collections4.Equator"""
 
    @staticmethod
    def _wrap(java_value: _Equator) -> 'Equator':
        return Equator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Equator):
        """
        Dynamic initializer for Equator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Equator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Equator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def equate(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.Equator.equate(T,T)"""
        pass

    @abstractmethod
    def hash(self, arg0: object):
        """public abstract int org.apache.commons.collections4.Equator.hash(T)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.MapUtils
from pyquantum_helper import import_once as _import_once
import java.lang.Double as _double
import java.lang.Long as Long
import java.lang.Short as Short
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.ResourceBundle as ResourceBundle
import java.util.Properties as _Properties
_Properties = _Properties
import java.lang.Boolean as _Boolean
_Boolean = _Boolean
import java.lang.Short as _short
import java.lang.String as _string
import org.apache.commons.collections4.map.MultiValueMap as _MultiValueMap
_MultiValueMap = _MultiValueMap
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
import org.apache.commons.collections4.MapUtils as _MapUtils
_MapUtils = _MapUtils
import java.util.SortedMap as _SortedMap
_SortedMap = _SortedMap
import java.util.SortedMap as SortedMap
import org.apache.commons.collections4.IterableSortedMap as _IterableSortedMap
_IterableSortedMap = _IterableSortedMap
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.Float as Float
import java.lang.Iterable as Iterable
import org.apache.commons.collections4.IterableMap as _IterableMap
_IterableMap = _IterableMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Byte as Byte
try:
    from pyapache.collections4 import map
except ImportError:
    map = _import_once("pyapache.collections4.map")

import java.lang.Float as _float
import java.lang.Integer as _int
import java.io.PrintStream as PrintStream
import java.lang.Integer as Integer
import org.apache.commons.collections4.OrderedMap as _OrderedMap
_OrderedMap = _OrderedMap
import java.util.Properties as Properties
import java.util.Map as Map
import java.lang.Double as Double
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapUtils():
    """org.apache.commons.collections4.MapUtils"""
 
    @staticmethod
    def _wrap(java_value: _MapUtils) -> 'MapUtils':
        return MapUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapUtils):
        """
        Dynamic initializer for MapUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getByte(getByte) -> 'Byte':
        """public static <K> java.lang.Byte org.apache.commons.collections4.MapUtils.getByte(java.util.Map<? super K, ?>,K)"""
        return _transform(_arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Byte'Value()

    @staticmethod
    @overload
    def getShort(getShort) -> 'Short':
        """public static <K> java.lang.Short org.apache.commons.collections4.MapUtils.getShort(java.util.Map<? super K, ?>,K,java.lang.Short)"""
        return _transform(_arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Short')).'Short'Value()

    @staticmethod
    @overload
    def isEmpty(arg0: 'Map') -> bool:
        """public static boolean org.apache.commons.collections4.MapUtils.isEmpty(java.util.Map<?, ?>)"""
        return bool._wrap(_MapUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def iterableMap(arg0: 'Map') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.MapUtils.iterableMap(java.util.Map<K, V>)"""
        return IterableMap._wrap(_MapUtils.iterableMap(arg0))

    @staticmethod
    @overload
    def getLongValue(arg0: 'Map', arg1: object, arg2: int) -> int:
        """public static <K> long org.apache.commons.collections4.MapUtils.getLongValue(java.util.Map<? super K, ?>,K,long)"""
        return int._wrap(_MapUtils.getLongValue(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def size(arg0: 'Map') -> int:
        """public static int org.apache.commons.collections4.MapUtils.size(java.util.Map<?, ?>)"""
        return int._wrap(_MapUtils.size(arg0))

    @staticmethod
    @overload
    def getLong(getLong) -> 'Long':
        """public static <K> java.lang.Long org.apache.commons.collections4.MapUtils.getLong(java.util.Map<? super K, ?>,K,java.lang.Long)"""
        return _transform(_arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Long')).'Long'Value()

    @staticmethod
    @overload
    def predicatedSortedMap(arg0: 'SortedMap', arg1: 'Predicate', arg2: 'Predicate') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.predicatedSortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Predicate<? super K>,org.apache.commons.collections4.Predicate<? super V>)"""
        return SortedMap._wrap(_MapUtils.predicatedSortedMap(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def multiValueMap(arg0: 'Map', arg1: 'Class') -> 'map.MultiValueMap':
        """public static <K,V,C extends java.util.Collection<V>> org.apache.commons.collections4.map.MultiValueMap<K, V> org.apache.commons.collections4.MapUtils.multiValueMap(java.util.Map<K, C>,java.lang.Class<C>)"""
        return map.MultiValueMap._wrap(_MapUtils.multiValueMap(arg0, arg1))

    @staticmethod
    @overload
    def orderedMap(arg0: 'Map') -> 'OrderedMap':
        """public static <K,V> org.apache.commons.collections4.OrderedMap<K, V> org.apache.commons.collections4.MapUtils.orderedMap(java.util.Map<K, V>)"""
        return OrderedMap._wrap(_MapUtils.orderedMap(arg0))

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
    def getLong(getLong) -> 'Long':
        """public static <K> java.lang.Long org.apache.commons.collections4.MapUtils.getLong(java.util.Map<? super K, ?>,K)"""
        return _transform(_arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Long'Value()

    @staticmethod
    @overload
    def predicatedMap(arg0: 'Map', arg1: 'Predicate', arg2: 'Predicate') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.MapUtils.predicatedMap(java.util.Map<K, V>,org.apache.commons.collections4.Predicate<? super K>,org.apache.commons.collections4.Predicate<? super V>)"""
        return IterableMap._wrap(_MapUtils.predicatedMap(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getBoolean(arg0: 'Map', arg1: object, arg2: 'Boolean') -> 'Boolean':
        """public static <K> java.lang.Boolean org.apache.commons.collections4.MapUtils.getBoolean(java.util.Map<? super K, ?>,K,java.lang.Boolean)"""
        return Boolean._wrap(_MapUtils.getBoolean(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getNumber(getNumber) -> 'Number':
        """public static <K> java.lang.Number org.apache.commons.collections4.MapUtils.getNumber(java.util.Map<? super K, ?>,K)"""
        return _transform(_arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Number'Value()

    @staticmethod
    @overload
    def getString(arg0: 'Map', arg1: object, arg2: str) -> str:
        """public static <K> java.lang.String org.apache.commons.collections4.MapUtils.getString(java.util.Map<? super K, ?>,K,java.lang.String)"""
        return str._wrap(_MapUtils.getString(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getObject(arg0: 'Map', arg1: object, arg2: object) -> object:
        """public static <K,V> V org.apache.commons.collections4.MapUtils.getObject(java.util.Map<K, V>,K,V)"""
        return object._wrap(_MapUtils.getObject(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def getDouble(getDouble) -> 'Double':
        """public static <K> java.lang.Double org.apache.commons.collections4.MapUtils.getDouble(java.util.Map<? super K, ?>,K,java.lang.Double)"""
        return _transform(_arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Double')).'Double'Value()

    @staticmethod
    @overload
    def getObject(arg0: 'Map', arg1: object) -> object:
        """public static <K,V> V org.apache.commons.collections4.MapUtils.getObject(java.util.Map<? super K, V>,K)"""
        return object._wrap(_MapUtils.getObject(arg0, arg1))

    @staticmethod
    @overload
    def getShortValue(arg0: 'Map', arg1: object) -> int:
        """public static <K> short org.apache.commons.collections4.MapUtils.getShortValue(java.util.Map<? super K, ?>,K)"""
        return int._wrap(_MapUtils.getShortValue(arg0, arg1))

    @staticmethod
    @overload
    def populateMap(arg0: 'MultiMap', arg1: 'Iterable', arg2: 'Transformer'):
        """public static <K,V> void org.apache.commons.collections4.MapUtils.populateMap(org.apache.commons.collections4.MultiMap<K, V>,java.lang.Iterable<? extends V>,org.apache.commons.collections4.Transformer<V, K>)"""
        _MapUtils.populateMap(arg0, arg1, arg2)

    @staticmethod
    @overload
    def populateMap(arg0: 'Map', arg1: 'Iterable', arg2: 'Transformer', arg3: 'Transformer'):
        """public static <K,V,E> void org.apache.commons.collections4.MapUtils.populateMap(java.util.Map<K, V>,java.lang.Iterable<? extends E>,org.apache.commons.collections4.Transformer<E, K>,org.apache.commons.collections4.Transformer<E, V>)"""
        _MapUtils.populateMap(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def getFloatValue(arg0: 'Map', arg1: object) -> float:
        """public static <K> float org.apache.commons.collections4.MapUtils.getFloatValue(java.util.Map<? super K, ?>,K)"""
        return float._wrap(_MapUtils.getFloatValue(arg0, arg1))

    @staticmethod
    @overload
    def getFloat(getFloat) -> 'Float':
        """public static <K> java.lang.Float org.apache.commons.collections4.MapUtils.getFloat(java.util.Map<? super K, ?>,K,java.lang.Float)"""
        return _transform(_arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Float')).'Float'Value()

    @staticmethod
    @overload
    def getMap(arg0: 'Map', arg1: object, arg2: 'Map') -> 'Map':
        """public static <K> java.util.Map<?, ?> org.apache.commons.collections4.MapUtils.getMap(java.util.Map<? super K, ?>,K,java.util.Map<?, ?>)"""
        return Map._wrap(_MapUtils.getMap(arg0, arg1, arg2))

    @staticmethod
    @overload
    def emptyIfNull(arg0: 'Map') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.MapUtils.emptyIfNull(java.util.Map<K, V>)"""
        return Map._wrap(_MapUtils.emptyIfNull(arg0))

    @staticmethod
    @overload
    def lazySortedMap(arg0: 'SortedMap', arg1: 'Factory') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.lazySortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Factory<? extends V>)"""
        return SortedMap._wrap(_MapUtils.lazySortedMap(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def lazyMap(arg0: 'Map', arg1: 'Transformer') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.MapUtils.lazyMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        return IterableMap._wrap(_MapUtils.lazyMap(arg0, arg1))

    @staticmethod
    @overload
    def getDoubleValue(arg0: 'Map', arg1: object, arg2: float) -> float:
        """public static <K> double org.apache.commons.collections4.MapUtils.getDoubleValue(java.util.Map<? super K, ?>,K,double)"""
        return float._wrap(_MapUtils.getDoubleValue(arg0, arg1, _double.valueOf(arg2)))

    @staticmethod
    @overload
    def populateMap(arg0: 'MultiMap', arg1: 'Iterable', arg2: 'Transformer', arg3: 'Transformer'):
        """public static <K,V,E> void org.apache.commons.collections4.MapUtils.populateMap(org.apache.commons.collections4.MultiMap<K, V>,java.lang.Iterable<? extends E>,org.apache.commons.collections4.Transformer<E, K>,org.apache.commons.collections4.Transformer<E, V>)"""
        _MapUtils.populateMap(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def invertMap(arg0: 'Map') -> 'Map':
        """public static <K,V> java.util.Map<V, K> org.apache.commons.collections4.MapUtils.invertMap(java.util.Map<K, V>)"""
        return Map._wrap(_MapUtils.invertMap(arg0))

    @staticmethod
    @overload
    def transformedSortedMap(arg0: 'SortedMap', arg1: 'Transformer', arg2: 'Transformer') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.transformedSortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return SortedMap._wrap(_MapUtils.transformedSortedMap(arg0, arg1, arg2))

    @staticmethod
    @overload
    def unmodifiableSortedMap(arg0: 'SortedMap') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.unmodifiableSortedMap(java.util.SortedMap<K, ? extends V>)"""
        return SortedMap._wrap(_MapUtils.unmodifiableSortedMap(arg0))

    @staticmethod
    @overload
    def getByte(getByte) -> 'Byte':
        """public static <K> java.lang.Byte org.apache.commons.collections4.MapUtils.getByte(java.util.Map<? super K, ?>,K,java.lang.Byte)"""
        return _transform(_arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Byte')).'Byte'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def transformedMap(arg0: 'Map', arg1: 'Transformer', arg2: 'Transformer') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.MapUtils.transformedMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return IterableMap._wrap(_MapUtils.transformedMap(arg0, arg1, arg2))

    @staticmethod
    @overload
    def iterableSortedMap(arg0: 'SortedMap') -> 'IterableSortedMap':
        """public static <K,V> org.apache.commons.collections4.IterableSortedMap<K, V> org.apache.commons.collections4.MapUtils.iterableSortedMap(java.util.SortedMap<K, V>)"""
        return IterableSortedMap._wrap(_MapUtils.iterableSortedMap(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getInteger(getInteger) -> 'Integer':
        """public static <K> java.lang.Integer org.apache.commons.collections4.MapUtils.getInteger(java.util.Map<? super K, ?>,K,java.lang.Integer)"""
        return _transform(_arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Integer')).'Integer'Value()

    @staticmethod
    @overload
    def multiValueMap(arg0: 'Map') -> 'map.MultiValueMap':
        """public static <K,V> org.apache.commons.collections4.map.MultiValueMap<K, V> org.apache.commons.collections4.MapUtils.multiValueMap(java.util.Map<K, ? super java.util.Collection<V>>)"""
        return map.MultiValueMap._wrap(_MapUtils.multiValueMap(arg0))

    @staticmethod
    @overload
    def fixedSizeMap(arg0: 'Map') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.MapUtils.fixedSizeMap(java.util.Map<K, V>)"""
        return IterableMap._wrap(_MapUtils.fixedSizeMap(arg0))

    @staticmethod
    @overload
    def lazyMap(arg0: 'Map', arg1: 'Factory') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.MapUtils.lazyMap(java.util.Map<K, V>,org.apache.commons.collections4.Factory<? extends V>)"""
        return IterableMap._wrap(_MapUtils.lazyMap(arg0, arg1))

    @staticmethod
    @overload
    def putAll(arg0: 'Map', arg1: 'Object') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.MapUtils.putAll(java.util.Map<K, V>,java.lang.Object[])"""
        return Map._wrap(_MapUtils.putAll(arg0, arg1))

    @staticmethod
    @overload
    def lazySortedMap(arg0: 'SortedMap', arg1: 'Transformer') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.lazySortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        return SortedMap._wrap(_MapUtils.lazySortedMap(arg0, arg1))

    @staticmethod
    @overload
    def getDouble(getDouble) -> 'Double':
        """public static <K> java.lang.Double org.apache.commons.collections4.MapUtils.getDouble(java.util.Map<? super K, ?>,K)"""
        return _transform(_arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Double'Value()

    @staticmethod
    @overload
    def verbosePrint(arg0: 'PrintStream', arg1: object, arg2: 'Map'):
        """public static void org.apache.commons.collections4.MapUtils.verbosePrint(java.io.PrintStream,java.lang.Object,java.util.Map<?, ?>)"""
        _MapUtils.verbosePrint(arg0, arg1, arg2)

    @staticmethod
    @overload
    def getIntValue(arg0: 'Map', arg1: object) -> int:
        """public static <K> int org.apache.commons.collections4.MapUtils.getIntValue(java.util.Map<? super K, ?>,K)"""
        return int._wrap(_MapUtils.getIntValue(arg0, arg1))

    @staticmethod
    @overload
    def getShortValue(arg0: 'Map', arg1: object, arg2: int) -> int:
        """public static <K> short org.apache.commons.collections4.MapUtils.getShortValue(java.util.Map<? super K, ?>,K,short)"""
        return int._wrap(_MapUtils.getShortValue(arg0, arg1, _short.valueOf(arg2)))

    @staticmethod
    @overload
    def safeAddToMap(arg0: 'Map', arg1: object, arg2: object):
        """public static <K> void org.apache.commons.collections4.MapUtils.safeAddToMap(java.util.Map<? super K, java.lang.Object>,K,java.lang.Object) throws java.lang.NullPointerException"""
        _MapUtils.safeAddToMap(arg0, arg1, arg2)

    @staticmethod
    @overload
    def getNumber(getNumber) -> 'Number':
        """public static <K> java.lang.Number org.apache.commons.collections4.MapUtils.getNumber(java.util.Map<? super K, ?>,K,java.lang.Number)"""
        return _transform(_arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Number')).'Number'Value()

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'Map') -> bool:
        """public static boolean org.apache.commons.collections4.MapUtils.isNotEmpty(java.util.Map<?, ?>)"""
        return bool._wrap(_MapUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def getFloatValue(arg0: 'Map', arg1: object, arg2: float) -> float:
        """public static <K> float org.apache.commons.collections4.MapUtils.getFloatValue(java.util.Map<? super K, ?>,K,float)"""
        return float._wrap(_MapUtils.getFloatValue(arg0, arg1, _float.valueOf(arg2)))

    @staticmethod
    @overload
    def populateMap(arg0: 'Map', arg1: 'Iterable', arg2: 'Transformer'):
        """public static <K,V> void org.apache.commons.collections4.MapUtils.populateMap(java.util.Map<K, V>,java.lang.Iterable<? extends V>,org.apache.commons.collections4.Transformer<V, K>)"""
        _MapUtils.populateMap(arg0, arg1, arg2)

    @staticmethod
    @overload
    def getFloat(getFloat) -> 'Float':
        """public static <K> java.lang.Float org.apache.commons.collections4.MapUtils.getFloat(java.util.Map<? super K, ?>,K)"""
        return _transform(_arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Float'Value()

    @staticmethod
    @overload
    def getByteValue(arg0: 'Map', arg1: object) -> int:
        """public static <K> byte org.apache.commons.collections4.MapUtils.getByteValue(java.util.Map<? super K, ?>,K)"""
        return int._wrap(_MapUtils.getByteValue(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableMap(arg0: 'Map') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.MapUtils.unmodifiableMap(java.util.Map<? extends K, ? extends V>)"""
        return Map._wrap(_MapUtils.unmodifiableMap(arg0))

    @staticmethod
    @overload
    def synchronizedMap(arg0: 'Map') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.MapUtils.synchronizedMap(java.util.Map<K, V>)"""
        return Map._wrap(_MapUtils.synchronizedMap(arg0))

    @staticmethod
    @overload
    def getIntValue(arg0: 'Map', arg1: object, arg2: int) -> int:
        """public static <K> int org.apache.commons.collections4.MapUtils.getIntValue(java.util.Map<? super K, ?>,K,int)"""
        return int._wrap(_MapUtils.getIntValue(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def getBooleanValue(arg0: 'Map', arg1: object, arg2: bool) -> bool:
        """public static <K> boolean org.apache.commons.collections4.MapUtils.getBooleanValue(java.util.Map<? super K, ?>,K,boolean)"""
        return bool._wrap(_MapUtils.getBooleanValue(arg0, arg1, _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def debugPrint(arg0: 'PrintStream', arg1: object, arg2: 'Map'):
        """public static void org.apache.commons.collections4.MapUtils.debugPrint(java.io.PrintStream,java.lang.Object,java.util.Map<?, ?>)"""
        _MapUtils.debugPrint(arg0, arg1, arg2)

    @staticmethod
    @overload
    def getInteger(getInteger) -> 'Integer':
        """public static <K> java.lang.Integer org.apache.commons.collections4.MapUtils.getInteger(java.util.Map<? super K, ?>,K)"""
        return _transform(_arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Integer'Value()

    @staticmethod
    @overload
    def getShort(getShort) -> 'Short':
        """public static <K> java.lang.Short org.apache.commons.collections4.MapUtils.getShort(java.util.Map<? super K, ?>,K)"""
        return _transform(_arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Short'Value()

    @staticmethod
    @overload
    def synchronizedSortedMap(arg0: 'SortedMap') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.synchronizedSortedMap(java.util.SortedMap<K, V>)"""
        return SortedMap._wrap(_MapUtils.synchronizedSortedMap(arg0))

    @staticmethod
    @overload
    def toProperties(arg0: 'Map') -> 'Properties':
        """public static <K,V> java.util.Properties org.apache.commons.collections4.MapUtils.toProperties(java.util.Map<K, V>)"""
        return Properties._wrap(_MapUtils.toProperties(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getMap(arg0: 'Map', arg1: object) -> 'Map':
        """public static <K> java.util.Map<?, ?> org.apache.commons.collections4.MapUtils.getMap(java.util.Map<? super K, ?>,K)"""
        return Map._wrap(_MapUtils.getMap(arg0, arg1))

    @staticmethod
    @overload
    def getString(arg0: 'Map', arg1: object) -> str:
        """public static <K> java.lang.String org.apache.commons.collections4.MapUtils.getString(java.util.Map<? super K, ?>,K)"""
        return str._wrap(_MapUtils.getString(arg0, arg1))

    @staticmethod
    @overload
    def toMap(arg0: 'ResourceBundle') -> 'Map':
        """public static java.util.Map<java.lang.String, java.lang.Object> org.apache.commons.collections4.MapUtils.toMap(java.util.ResourceBundle)"""
        return Map._wrap(_MapUtils.toMap(arg0))

    @staticmethod
    @overload
    def multiValueMap(arg0: 'Map', arg1: 'Factory') -> 'map.MultiValueMap':
        """public static <K,V,C extends java.util.Collection<V>> org.apache.commons.collections4.map.MultiValueMap<K, V> org.apache.commons.collections4.MapUtils.multiValueMap(java.util.Map<K, C>,org.apache.commons.collections4.Factory<C>)"""
        return map.MultiValueMap._wrap(_MapUtils.multiValueMap(arg0, arg1))

    @staticmethod
    @overload
    def getBooleanValue(arg0: 'Map', arg1: object) -> bool:
        """public static <K> boolean org.apache.commons.collections4.MapUtils.getBooleanValue(java.util.Map<? super K, ?>,K)"""
        return bool._wrap(_MapUtils.getBooleanValue(arg0, arg1))

    @staticmethod
    @overload
    def getLongValue(arg0: 'Map', arg1: object) -> int:
        """public static <K> long org.apache.commons.collections4.MapUtils.getLongValue(java.util.Map<? super K, ?>,K)"""
        return int._wrap(_MapUtils.getLongValue(arg0, arg1))

    @staticmethod
    @overload
    def getBoolean(arg0: 'Map', arg1: object) -> 'Boolean':
        """public static <K> java.lang.Boolean org.apache.commons.collections4.MapUtils.getBoolean(java.util.Map<? super K, ?>,K)"""
        return Boolean._wrap(_MapUtils.getBoolean(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getByteValue(arg0: 'Map', arg1: object, arg2: int) -> int:
        """public static <K> byte org.apache.commons.collections4.MapUtils.getByteValue(java.util.Map<? super K, ?>,K,byte)"""
        return int._wrap(_MapUtils.getByteValue(arg0, arg1, _byte.valueOf(arg2)))

    @staticmethod
    @overload
    def fixedSizeSortedMap(arg0: 'SortedMap') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.fixedSizeSortedMap(java.util.SortedMap<K, V>)"""
        return SortedMap._wrap(_MapUtils.fixedSizeSortedMap(arg0))

    @staticmethod
    @overload
    def getDoubleValue(arg0: 'Map', arg1: object) -> float:
        """public static <K> double org.apache.commons.collections4.MapUtils.getDoubleValue(java.util.Map<? super K, ?>,K)"""
        return float._wrap(_MapUtils.getDoubleValue(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.Factory
import org.apache.commons.collections4.Factory as _Factory
_Factory = _Factory
from abc import abstractmethod, ABC
 
class Factory():
    """org.apache.commons.collections4.Factory"""
 
    @staticmethod
    def _wrap(java_value: _Factory) -> 'Factory':
        return Factory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Factory):
        """
        Dynamic initializer for Factory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Factory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Factory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def create(self, ):
        """public abstract T org.apache.commons.collections4.Factory.create()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.ArrayStack
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.ArrayStack as _ArrayStack
_ArrayStack = _ArrayStack
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class ArrayStack():
    """org.apache.commons.collections4.ArrayStack"""
 
    @staticmethod
    def _wrap(java_value: _ArrayStack) -> 'ArrayStack':
        return ArrayStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayStack):
        """
        Dynamic initializer for ArrayStack.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayStack__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayStack__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def addLast(self, arg0: object):
        """public void java.util.ArrayList.addLast(E)"""
        super(_ArrayList, self).addLast(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.ArrayList.hashCode()"""
        return int._wrap(super(ArrayList, self).hashCode())

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_ArrayList, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def getFirst(self) -> object:
        """public E java.util.ArrayList.getFirst()"""
        return object._wrap(super(ArrayList, self).getFirst())

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator()"""
        return 'ListIterator'._wrap(super(ArrayList, self).listIterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void java.util.ArrayList.add(int,E)"""
        super(_ArrayList, self).add(_int.valueOf(arg0), arg1)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_ArrayList, self).removeAll(arg0))

    @overload
    def peek(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.ArrayStack.peek(int) throws java.util.EmptyStackException"""
        return object._wrap(super(_ArrayStack, self).peek(_int.valueOf(arg0)))

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
    def empty(self) -> bool:
        """public boolean org.apache.commons.collections4.ArrayStack.empty()"""
        return bool._wrap(super(ArrayStack, self).empty())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.add(E)"""
        return bool._wrap(super(_ArrayList, self).add(arg0))

    @overload
    def push(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.ArrayStack.push(E)"""
        return object._wrap(super(_ArrayStack, self).push(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.ArrayList.isEmpty()"""
        return bool._wrap(super(ArrayList, self).isEmpty())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean java.util.ArrayList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_ArrayList, self).removeIf(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.indexOf(java.lang.Object)"""
        return int._wrap(super(_ArrayList, self).indexOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.ArrayStack()"""
        val = _ArrayStack()
        self.__wrapper = val

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @overload
    def peek(self) -> object:
        """public E org.apache.commons.collections4.ArrayStack.peek() throws java.util.EmptyStackException"""
        return object._wrap(super(ArrayStack, self).peek())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<E> java.util.ArrayList.spliterator()"""
        return 'Spliterator'._wrap(super(ArrayList, self).spliterator())

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void java.util.ArrayList.ensureCapacity(int)"""
        super(_ArrayList, self).ensureCapacity(_int.valueOf(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_ArrayList, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void java.util.ArrayList.forEach(java.util.function.Consumer<? super E>)"""
        super(_ArrayList, self).forEach(arg0)

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public void java.util.ArrayList.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_ArrayList, self).replaceAll(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public void java.util.ArrayList.addFirst(E)"""
        super(_ArrayList, self).addFirst(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public void java.util.ArrayList.sort(java.util.Comparator<? super E>)"""
        super(_ArrayList, self).sort(arg0)

    @override
    @overload
    def removeFirst(self) -> object:
        """public E java.util.ArrayList.removeFirst()"""
        return object._wrap(super(ArrayList, self).removeFirst())

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.util.ArrayList.clone()"""
        return object._wrap(super(ArrayList, self).clone())

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E java.util.ArrayList.set(int,E)"""
        return object._wrap(super(_ArrayList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.ArrayList.toArray(T[])"""
        return List[object]._wrap(super(_ArrayList, self).toArray(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_ArrayList, self).addAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def get(self, arg0: int) -> object:
        """public E java.util.ArrayList.get(int)"""
        return object._wrap(super(_ArrayList, self).get(_int.valueOf(arg0)))

    @overload
    def pop(self) -> object:
        """public E org.apache.commons.collections4.ArrayStack.pop() throws java.util.EmptyStackException"""
        return object._wrap(super(ArrayStack, self).pop())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.ArrayStack(int)"""
        val = _ArrayStack(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def trimToSize(self):
        """public void java.util.ArrayList.trimToSize()"""
        super(ArrayList, self).trimToSize()

    @override
    @overload
    def getLast(self) -> object:
        """public E java.util.ArrayList.getLast()"""
        return object._wrap(super(ArrayList, self).getLast())

    @override
    @overload
    def clear(self):
        """public void java.util.ArrayList.clear()"""
        super(ArrayList, self).clear()

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_ArrayList, self).lastIndexOf(arg0))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> java.util.ArrayList.subList(int,int)"""
        return 'List'._wrap(super(_ArrayList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str._wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.contains(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).contains(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.ArrayStack()"""
        val = _ArrayStack()
        self.__wrapper = val

    @overload
    def search(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.ArrayStack.search(java.lang.Object)"""
        return int._wrap(super(_ArrayStack, self).search(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public E java.util.ArrayList.remove(int)"""
        return object._wrap(super(_ArrayList, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def size(self) -> int:
        """public int java.util.ArrayList.size()"""
        return int._wrap(super(ArrayList, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.ArrayList.toArray()"""
        return List[object]._wrap(super(ArrayList, self).toArray())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_ArrayList, self).retainAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.remove(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).remove(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.equals(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).equals(arg0))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def removeLast(self) -> object:
        """public E java.util.ArrayList.removeLast()"""
        return object._wrap(super(ArrayList, self).removeLast())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> java.util.ArrayList.iterator()"""
        return 'Iterator'._wrap(super(ArrayList, self).iterator()) 
 
 
# CLASS: org.apache.commons.collections4.TransformerUtils
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
import org.apache.commons.collections4.TransformerUtils as _TransformerUtils
_TransformerUtils = _TransformerUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformerUtils():
    """org.apache.commons.collections4.TransformerUtils"""
 
    @staticmethod
    def _wrap(java_value: _TransformerUtils) -> 'TransformerUtils':
        return TransformerUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformerUtils):
        """
        Dynamic initializer for TransformerUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformerUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformerUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def invokerTransformer(arg0: str) -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.invokerTransformer(java.lang.String)"""
        return Transformer._wrap(_TransformerUtils.invokerTransformer(arg0))

    @staticmethod
    @overload
    def switchTransformer(arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.switchTransformer(org.apache.commons.collections4.Predicate<? super I>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Transformer._wrap(_TransformerUtils.switchTransformer(arg0, arg1, arg2))

    @staticmethod
    @overload
    def cloneTransformer() -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.TransformerUtils.cloneTransformer()"""
        return Transformer._wrap(_TransformerUtils.cloneTransformer())

    @staticmethod
    @overload
    def asTransformer(arg0: 'Factory') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.asTransformer(org.apache.commons.collections4.Factory<? extends O>)"""
        return Transformer._wrap(_TransformerUtils.asTransformer(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def chainedTransformer(arg0: 'Collection') -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.TransformerUtils.chainedTransformer(java.util.Collection<? extends org.apache.commons.collections4.Transformer<? super T, ? extends T>>)"""
        return Transformer._wrap(_TransformerUtils.chainedTransformer(arg0))

    @staticmethod
    @overload
    def ifTransformer(arg0: 'Predicate', arg1: 'Transformer') -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.TransformerUtils.ifTransformer(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Transformer<? super T, ? extends T>)"""
        return Transformer._wrap(_TransformerUtils.ifTransformer(arg0, arg1))

    @staticmethod
    @overload
    def switchMapTransformer(arg0: 'Map') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.switchMapTransformer(java.util.Map<I, org.apache.commons.collections4.Transformer<I, O>>)"""
        return Transformer._wrap(_TransformerUtils.switchMapTransformer(arg0))

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
    def mapTransformer(arg0: 'Map') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.mapTransformer(java.util.Map<? super I, ? extends O>)"""
        return Transformer._wrap(_TransformerUtils.mapTransformer(arg0))

    @staticmethod
    @overload
    def nullTransformer() -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.nullTransformer()"""
        return Transformer._wrap(_TransformerUtils.nullTransformer())

    @staticmethod
    @overload
    def switchTransformer(arg0: 'Predicate', arg1: 'Transformer') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.switchTransformer(org.apache.commons.collections4.Predicate<? super I>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>[])"""
        return Transformer._wrap(_TransformerUtils.switchTransformer(arg0, arg1))

    @staticmethod
    @overload
    def ifTransformer(arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.ifTransformer(org.apache.commons.collections4.Predicate<? super I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Transformer._wrap(_TransformerUtils.ifTransformer(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def asTransformer(arg0: 'Closure') -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.TransformerUtils.asTransformer(org.apache.commons.collections4.Closure<? super T>)"""
        return Transformer._wrap(_TransformerUtils.asTransformer(arg0))

    @staticmethod
    @overload
    def constantTransformer(arg0: object) -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.constantTransformer(O)"""
        return Transformer._wrap(_TransformerUtils.constantTransformer(arg0))

    @staticmethod
    @overload
    def switchTransformer(arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.switchTransformer(org.apache.commons.collections4.Predicate<? super I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Transformer._wrap(_TransformerUtils.switchTransformer(arg0, arg1, arg2))

    @staticmethod
    @overload
    def instantiateTransformer(arg0: 'Class', arg1: 'Object') -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<java.lang.Class<? extends T>, T> org.apache.commons.collections4.TransformerUtils.instantiateTransformer(java.lang.Class<?>[],java.lang.Object[])"""
        return Transformer._wrap(_TransformerUtils.instantiateTransformer(arg0, arg1))

    @staticmethod
    @overload
    def invokerTransformer(arg0: str, arg1: 'Class', arg2: 'Object') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.invokerTransformer(java.lang.String,java.lang.Class<?>[],java.lang.Object[])"""
        return Transformer._wrap(_TransformerUtils.invokerTransformer(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nopTransformer() -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.TransformerUtils.nopTransformer()"""
        return Transformer._wrap(_TransformerUtils.nopTransformer())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def stringValueTransformer() -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, java.lang.String> org.apache.commons.collections4.TransformerUtils.stringValueTransformer()"""
        return Transformer._wrap(_TransformerUtils.stringValueTransformer())

    @staticmethod
    @overload
    def instantiateTransformer() -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<java.lang.Class<? extends T>, T> org.apache.commons.collections4.TransformerUtils.instantiateTransformer()"""
        return Transformer._wrap(_TransformerUtils.instantiateTransformer())

    @staticmethod
    @overload
    def switchTransformer(arg0: 'Map') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.switchTransformer(java.util.Map<org.apache.commons.collections4.Predicate<I>, org.apache.commons.collections4.Transformer<I, O>>)"""
        return Transformer._wrap(_TransformerUtils.switchTransformer(arg0))

    @staticmethod
    @overload
    def exceptionTransformer() -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.exceptionTransformer()"""
        return Transformer._wrap(_TransformerUtils.exceptionTransformer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def asTransformer(arg0: 'Predicate') -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, java.lang.Boolean> org.apache.commons.collections4.TransformerUtils.asTransformer(org.apache.commons.collections4.Predicate<? super T>)"""
        return Transformer._wrap(_TransformerUtils.asTransformer(arg0))

    @staticmethod
    @overload
    def chainedTransformer(*arg0: 'Transformer') -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.TransformerUtils.chainedTransformer(org.apache.commons.collections4.Transformer<? super T, ? extends T>...)"""
        return Transformer._wrap(_TransformerUtils.chainedTransformer(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.BoundedMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.BoundedMap as _BoundedMap
_BoundedMap = _BoundedMap
import org.apache.commons.collections4.Get as _Get
_Get = _Get
import org.apache.commons.collections4.IterableGet as _IterableGet
_IterableGet = _IterableGet
from abc import abstractmethod, ABC
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.Put as _Put
_Put = _Put
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class BoundedMap():
    """org.apache.commons.collections4.BoundedMap"""
 
    @staticmethod
    def _wrap(java_value: _BoundedMap) -> 'BoundedMap':
        return BoundedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BoundedMap):
        """
        Dynamic initializer for BoundedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BoundedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BoundedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.Put.put(K,V)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def maxSize(self, ):
        """public abstract int org.apache.commons.collections4.BoundedMap.maxSize()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V java.util.Map.put(K,V)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

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

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IterableGet.mapIterator()"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @abstractmethod
    def isFull(self, ):
        """public abstract boolean org.apache.commons.collections4.BoundedMap.isFull()"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.Map.values()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.BoundedCollection
import java.util.function.Predicate as Predicate
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.BoundedCollection as _BoundedCollection
_BoundedCollection = _BoundedCollection
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
from typing import List
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
from builtins import bool
 
class BoundedCollection():
    """org.apache.commons.collections4.BoundedCollection"""
 
    @staticmethod
    def _wrap(java_value: _BoundedCollection) -> 'BoundedCollection':
        return BoundedCollection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BoundedCollection):
        """
        Dynamic initializer for BoundedCollection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BoundedCollection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BoundedCollection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Collection.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Collection.size()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Collection.isEmpty()"""
        pass

    @abstractmethod
    def maxSize(self, ):
        """public abstract int org.apache.commons.collections4.BoundedCollection.maxSize()"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<E> java.util.Collection.iterator()"""
        pass

    @abstractmethod
    def contains(self, arg0: object):
        """public abstract boolean java.util.Collection.contains(java.lang.Object)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.addAll(java.util.Collection<? extends E>)"""
        pass

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @abstractmethod
    def add(self, arg0: object):
        """public abstract boolean java.util.Collection.add(E)"""
        pass

    @abstractmethod
    def retainAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.retainAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def toArray(self, ):
        """public abstract java.lang.Object[] java.util.Collection.toArray()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Collection.hashCode()"""
        pass

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @abstractmethod
    def toArray(self, arg0: 'Object'):
        """public abstract <T> T[] java.util.Collection.toArray(T[])"""
        pass

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Collection.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract boolean java.util.Collection.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def removeAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.removeAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def containsAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.containsAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def isFull(self, ):
        """public abstract boolean org.apache.commons.collections4.BoundedCollection.isFull()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.FunctorException
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
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import org.apache.commons.collections4.FunctorException as _FunctorException
_FunctorException = _FunctorException
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FunctorException():
    """org.apache.commons.collections4.FunctorException"""
 
    @staticmethod
    def _wrap(java_value: _FunctorException) -> 'FunctorException':
        return FunctorException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FunctorException):
        """
        Dynamic initializer for FunctorException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FunctorException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FunctorException__wrapper":
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

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.collections4.FunctorException(java.lang.String)"""
        val = _FunctorException(arg0)
        self.__wrapper = val

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
    def __init__(self, ):
        """public org.apache.commons.collections4.FunctorException()"""
        val = _FunctorException()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.collections4.FunctorException(java.lang.String,java.lang.Throwable)"""
        val = _FunctorException(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.FunctorException()"""
        val = _FunctorException()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.collections4.FunctorException(java.lang.Throwable)"""
        val = _FunctorException(arg0)
        self.__wrapper = val

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
 
 
# CLASS: org.apache.commons.collections4.Closure
import org.apache.commons.collections4.Closure as _Closure
_Closure = _Closure
from abc import abstractmethod, ABC
 
class Closure():
    """org.apache.commons.collections4.Closure"""
 
    @staticmethod
    def _wrap(java_value: _Closure) -> 'Closure':
        return Closure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Closure):
        """
        Dynamic initializer for Closure.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Closure__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Closure__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def execute(self, arg0: object):
        """public abstract void org.apache.commons.collections4.Closure.execute(T)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.EnumerationUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Integer as _int
import java.util.Enumeration as Enumeration
import org.apache.commons.collections4.EnumerationUtils as _EnumerationUtils
_EnumerationUtils = _EnumerationUtils
import java.util.StringTokenizer as StringTokenizer
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EnumerationUtils():
    """org.apache.commons.collections4.EnumerationUtils"""
 
    @staticmethod
    def _wrap(java_value: _EnumerationUtils) -> 'EnumerationUtils':
        return EnumerationUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EnumerationUtils):
        """
        Dynamic initializer for EnumerationUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EnumerationUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EnumerationUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def toList(arg0: 'StringTokenizer') -> 'List':
        """public static java.util.List<java.lang.String> org.apache.commons.collections4.EnumerationUtils.toList(java.util.StringTokenizer)"""
        return List._wrap(_EnumerationUtils.toList(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def get(arg0: 'Enumeration', arg1: int) -> object:
        """public static <T> T org.apache.commons.collections4.EnumerationUtils.get(java.util.Enumeration<T>,int)"""
        return object._wrap(_EnumerationUtils.get(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def toList(arg0: 'Enumeration') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.EnumerationUtils.toList(java.util.Enumeration<? extends E>)"""
        return List._wrap(_EnumerationUtils.toList(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.SplitMapUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.IterableMap as _IterableMap
_IterableMap = _IterableMap
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.apache.commons.collections4.SplitMapUtils as _SplitMapUtils
_SplitMapUtils = _SplitMapUtils
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SplitMapUtils():
    """org.apache.commons.collections4.SplitMapUtils"""
 
    @staticmethod
    def _wrap(java_value: _SplitMapUtils) -> 'SplitMapUtils':
        return SplitMapUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SplitMapUtils):
        """
        Dynamic initializer for SplitMapUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SplitMapUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SplitMapUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def readableMap(arg0: 'Get') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.SplitMapUtils.readableMap(org.apache.commons.collections4.Get<K, V>)"""
        return IterableMap._wrap(_SplitMapUtils.readableMap(arg0))

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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def writableMap(arg0: 'Put') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.SplitMapUtils.writableMap(org.apache.commons.collections4.Put<K, V>)"""
        return Map._wrap(_SplitMapUtils.writableMap(arg0))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.SetUtils$SetView
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.AbstractSet as _AbstractSet
_AbstractSet = _AbstractSet
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Set as Set
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import org.apache.commons.collections4.SetUtils as _SetUtils_SetView
_SetView = _SetUtils_SetView.SetView
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SetView():
    """org.apache.commons.collections4.SetUtils.SetView"""
 
    @staticmethod
    def _wrap(java_value: _SetView) -> 'SetView':
        return SetView(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SetView):
        """
        Dynamic initializer for SetView.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SetView__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SetView__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractCollection, self).addAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractSet.hashCode()"""
        return int._wrap(super(AbstractSet, self).hashCode())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.SetUtils$SetView()"""
        val = _SetView()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.SetUtils$SetView()"""
        val = _SetView()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.contains(java.lang.Object)"""
        return bool._wrap(super(_AbstractCollection, self).contains(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.AbstractCollection.toArray()"""
        return List[object]._wrap(super(AbstractCollection, self).toArray())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractSet, self).removeAll(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractSet.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractSet, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).retainAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @overload
    def toSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.SetUtils$SetView.toSet()"""
        return 'Set'._wrap(super(SetView, self).toSet())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str._wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void java.util.AbstractCollection.clear()"""
        super(AbstractCollection, self).clear()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.add(E)"""
        return bool._wrap(super(_AbstractCollection, self).add(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @overload
    def copyInto(self, arg0: 'Set'):
        """public <S extends java.util.Set<E>> void org.apache.commons.collections4.SetUtils$SetView.copyInto(S)"""
        super(_SetView, self).copyInto(arg0)

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object]._wrap(super(_AbstractCollection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.SetUtils$SetView.iterator()"""
        return 'Iterator'._wrap(super(SetView, self).iterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.SetUtils$SetView.size()"""
        return int._wrap(super(SetView, self).size())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractCollection, self).remove(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool._wrap(super(AbstractCollection, self).isEmpty()) 
 
 
# CLASS: org.apache.commons.collections4.FluentIterable
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Enumeration as Enumeration
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Enumeration as _Enumeration
_Enumeration = _Enumeration
import java.lang.Object as _object
import java.lang.Iterable as Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import org.apache.commons.collections4.FluentIterable as _FluentIterable
_FluentIterable = _FluentIterable
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class FluentIterable():
    """org.apache.commons.collections4.FluentIterable"""
 
    @staticmethod
    def _wrap(java_value: _FluentIterable) -> 'FluentIterable':
        return FluentIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FluentIterable):
        """
        Dynamic initializer for FluentIterable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FluentIterable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FluentIterable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.FluentIterable.toString()"""
        return str._wrap(super(FluentIterable, self).toString())

    @overload
    def append(self, arg0: 'Iterable') -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.append(java.lang.Iterable<? extends E>)"""
        return 'FluentIterable'._wrap(super(_FluentIterable, self).append(arg0))

    @overload
    def transform(self, arg0: 'Transformer') -> 'FluentIterable':
        """public <O> org.apache.commons.collections4.FluentIterable<O> org.apache.commons.collections4.FluentIterable.transform(org.apache.commons.collections4.Transformer<? super E, ? extends O>)"""
        return 'FluentIterable'._wrap(super(_FluentIterable, self).transform(arg0))

    @overload
    def copyInto(self, arg0: 'Collection'):
        """public void org.apache.commons.collections4.FluentIterable.copyInto(java.util.Collection<? super E>)"""
        super(_FluentIterable, self).copyInto(arg0)

    @overload
    def unmodifiable(self) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.unmodifiable()"""
        return 'FluentIterable'._wrap(super(FluentIterable, self).unmodifiable())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def zip(self, arg0: 'Iterable') -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.zip(java.lang.Iterable<? extends E>)"""
        return 'FluentIterable'._wrap(super(_FluentIterable, self).zip(arg0))

    @overload
    def append(self, *arg0: object) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.append(E...)"""
        return 'FluentIterable'._wrap(super(_FluentIterable, self).append(arg0))

    @overload
    def loop(self) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.loop()"""
        return 'FluentIterable'._wrap(super(FluentIterable, self).loop())

    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.FluentIterable.isEmpty()"""
        return bool._wrap(super(FluentIterable, self).isEmpty())

    @overload
    def limit(self, arg0: int) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.limit(long)"""
        return 'FluentIterable'._wrap(super(_FluentIterable, self).limit(_long.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @overload
    def toArray(self, arg0: 'Class') -> List[object]:
        """public E[] org.apache.commons.collections4.FluentIterable.toArray(java.lang.Class<E>)"""
        return List[object]._wrap(super(_FluentIterable, self).toArray(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def of(*arg0: object) -> 'FluentIterable':
        """public static <T> org.apache.commons.collections4.FluentIterable<T> org.apache.commons.collections4.FluentIterable.of(T...)"""
        return FluentIterable._wrap(_FluentIterable.of(arg0))

    @overload
    def collate(self, arg0: 'Iterable') -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.collate(java.lang.Iterable<? extends E>)"""
        return 'FluentIterable'._wrap(super(_FluentIterable, self).collate(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def empty() -> 'FluentIterable':
        """public static <T> org.apache.commons.collections4.FluentIterable<T> org.apache.commons.collections4.FluentIterable.empty()"""
        return FluentIterable._wrap(_FluentIterable.empty())

    @overload
    def allMatch(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.FluentIterable.allMatch(org.apache.commons.collections4.Predicate<? super E>)"""
        return bool._wrap(super(_FluentIterable, self).allMatch(arg0))

    @overload
    def anyMatch(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.FluentIterable.anyMatch(org.apache.commons.collections4.Predicate<? super E>)"""
        return bool._wrap(super(_FluentIterable, self).anyMatch(arg0))

    @overload
    def zip(self, *arg0: 'Iterable') -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.zip(java.lang.Iterable<? extends E>...)"""
        return 'FluentIterable'._wrap(super(_FluentIterable, self).zip(arg0))

    @overload
    def collate(self, arg0: 'Iterable', arg1: 'Comparator') -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.collate(java.lang.Iterable<? extends E>,java.util.Comparator<? super E>)"""
        return 'FluentIterable'._wrap(super(_FluentIterable, self).collate(arg0, arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.FluentIterable.iterator()"""
        return 'Iterator'._wrap(super(FluentIterable, self).iterator())

    @overload
    def toList(self) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.FluentIterable.toList()"""
        return 'List'._wrap(super(FluentIterable, self).toList())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.FluentIterable.get(int)"""
        return object._wrap(super(_FluentIterable, self).get(_int.valueOf(arg0)))

    @overload
    def reverse(self) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.reverse()"""
        return 'FluentIterable'._wrap(super(FluentIterable, self).reverse())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def of(arg0: object) -> 'FluentIterable':
        """public static <T> org.apache.commons.collections4.FluentIterable<T> org.apache.commons.collections4.FluentIterable.of(T)"""
        return FluentIterable._wrap(_FluentIterable.of(arg0))

    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.FluentIterable.size()"""
        return int._wrap(super(FluentIterable, self).size())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.FluentIterable.contains(java.lang.Object)"""
        return bool._wrap(super(_FluentIterable, self).contains(arg0))

    @overload
    def asEnumeration(self) -> 'Enumeration':
        """public java.util.Enumeration<E> org.apache.commons.collections4.FluentIterable.asEnumeration()"""
        return 'Enumeration'._wrap(super(FluentIterable, self).asEnumeration())

    @staticmethod
    @overload
    def of(arg0: 'Iterable') -> 'FluentIterable':
        """public static <T> org.apache.commons.collections4.FluentIterable<T> org.apache.commons.collections4.FluentIterable.of(java.lang.Iterable<T>)"""
        return FluentIterable._wrap(_FluentIterable.of(arg0))

    @overload
    def filter(self, arg0: 'Predicate') -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.filter(org.apache.commons.collections4.Predicate<? super E>)"""
        return 'FluentIterable'._wrap(super(_FluentIterable, self).filter(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def forEach(self, arg0: 'Closure'):
        """public void org.apache.commons.collections4.FluentIterable.forEach(org.apache.commons.collections4.Closure<? super E>)"""
        super(_FluentIterable, self).forEach(arg0)

    @overload
    def skip(self, arg0: int) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.skip(long)"""
        return 'FluentIterable'._wrap(super(_FluentIterable, self).skip(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def eval(self) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.eval()"""
        return 'FluentIterable'._wrap(super(FluentIterable, self).eval())

    @overload
    def unique(self) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.unique()"""
        return 'FluentIterable'._wrap(super(FluentIterable, self).unique())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.Predicate
import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
from abc import abstractmethod, ABC
 
class Predicate():
    """org.apache.commons.collections4.Predicate"""
 
    @staticmethod
    def _wrap(java_value: _Predicate) -> 'Predicate':
        return Predicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Predicate):
        """
        Dynamic initializer for Predicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Predicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Predicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def evaluate(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Predicate.evaluate(T)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.PredicateUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.PredicateUtils as _PredicateUtils
_PredicateUtils = _PredicateUtils
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PredicateUtils():
    """org.apache.commons.collections4.PredicateUtils"""
 
    @staticmethod
    def _wrap(java_value: _PredicateUtils) -> 'PredicateUtils':
        return PredicateUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicateUtils):
        """
        Dynamic initializer for PredicateUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicateUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicateUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def exceptionPredicate() -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.exceptionPredicate()"""
        return Predicate._wrap(_PredicateUtils.exceptionPredicate())

    @staticmethod
    @overload
    def nonePredicate(*arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.nonePredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return Predicate._wrap(_PredicateUtils.nonePredicate(arg0))

    @staticmethod
    @overload
    def eitherPredicate(arg0: 'Predicate', arg1: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.eitherPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate._wrap(_PredicateUtils.eitherPredicate(arg0, arg1))

    @staticmethod
    @overload
    def falsePredicate() -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.falsePredicate()"""
        return Predicate._wrap(_PredicateUtils.falsePredicate())

    @staticmethod
    @overload
    def allPredicate(*arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.allPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return Predicate._wrap(_PredicateUtils.allPredicate(arg0))

    @staticmethod
    @overload
    def orPredicate(arg0: 'Predicate', arg1: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.orPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate._wrap(_PredicateUtils.orPredicate(arg0, arg1))

    @staticmethod
    @overload
    def invokerPredicate(arg0: str, arg1: 'Class', arg2: 'Object') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.invokerPredicate(java.lang.String,java.lang.Class<?>[],java.lang.Object[])"""
        return Predicate._wrap(_PredicateUtils.invokerPredicate(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def asPredicate(arg0: 'Transformer') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.asPredicate(org.apache.commons.collections4.Transformer<? super T, java.lang.Boolean>)"""
        return Predicate._wrap(_PredicateUtils.asPredicate(arg0))

    @staticmethod
    @overload
    def allPredicate(arg0: 'Collection') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.allPredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return Predicate._wrap(_PredicateUtils.allPredicate(arg0))

    @staticmethod
    @overload
    def nonePredicate(arg0: 'Collection') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.nonePredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return Predicate._wrap(_PredicateUtils.nonePredicate(arg0))

    @staticmethod
    @overload
    def instanceofPredicate(arg0: 'Class') -> 'Predicate':
        """public static org.apache.commons.collections4.Predicate<java.lang.Object> org.apache.commons.collections4.PredicateUtils.instanceofPredicate(java.lang.Class<?>)"""
        return Predicate._wrap(_PredicateUtils.instanceofPredicate(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def notNullPredicate() -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.notNullPredicate()"""
        return Predicate._wrap(_PredicateUtils.notNullPredicate())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def andPredicate(arg0: 'Predicate', arg1: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.andPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate._wrap(_PredicateUtils.andPredicate(arg0, arg1))

    @staticmethod
    @overload
    def equalPredicate(arg0: object) -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.equalPredicate(T)"""
        return Predicate._wrap(_PredicateUtils.equalPredicate(arg0))

    @staticmethod
    @overload
    def nullPredicate() -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.nullPredicate()"""
        return Predicate._wrap(_PredicateUtils.nullPredicate())

    @staticmethod
    @overload
    def identityPredicate(arg0: object) -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.identityPredicate(T)"""
        return Predicate._wrap(_PredicateUtils.identityPredicate(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def nullIsFalsePredicate(arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.nullIsFalsePredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate._wrap(_PredicateUtils.nullIsFalsePredicate(arg0))

    @staticmethod
    @overload
    def onePredicate(*arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.onePredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return Predicate._wrap(_PredicateUtils.onePredicate(arg0))

    @staticmethod
    @overload
    def anyPredicate(arg0: 'Collection') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.anyPredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return Predicate._wrap(_PredicateUtils.anyPredicate(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nullIsExceptionPredicate(arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.nullIsExceptionPredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate._wrap(_PredicateUtils.nullIsExceptionPredicate(arg0))

    @staticmethod
    @overload
    def truePredicate() -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.truePredicate()"""
        return Predicate._wrap(_PredicateUtils.truePredicate())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def transformedPredicate(arg0: 'Transformer', arg1: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.transformedPredicate(org.apache.commons.collections4.Transformer<? super T, ? extends T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate._wrap(_PredicateUtils.transformedPredicate(arg0, arg1))

    @staticmethod
    @overload
    def anyPredicate(*arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.anyPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return Predicate._wrap(_PredicateUtils.anyPredicate(arg0))

    @staticmethod
    @overload
    def notPredicate(arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.notPredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate._wrap(_PredicateUtils.notPredicate(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def invokerPredicate(arg0: str) -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.invokerPredicate(java.lang.String)"""
        return Predicate._wrap(_PredicateUtils.invokerPredicate(arg0))

    @staticmethod
    @overload
    def neitherPredicate(arg0: 'Predicate', arg1: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.neitherPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate._wrap(_PredicateUtils.neitherPredicate(arg0, arg1))

    @staticmethod
    @overload
    def nullIsTruePredicate(arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.nullIsTruePredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate._wrap(_PredicateUtils.nullIsTruePredicate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def uniquePredicate() -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.uniquePredicate()"""
        return Predicate._wrap(_PredicateUtils.uniquePredicate())

    @staticmethod
    @overload
    def onePredicate(arg0: 'Collection') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.onePredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return Predicate._wrap(_PredicateUtils.onePredicate(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.MultiSet$Entry
import org.apache.commons.collections4.MultiSet as _MultiSet_Entry
_Entry = _MultiSet_Entry.Entry
from abc import abstractmethod, ABC
 
class Entry():
    """org.apache.commons.collections4.MultiSet.Entry"""
 
    @staticmethod
    def _wrap(java_value: _Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Entry):
        """
        Dynamic initializer for Entry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Entry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Entry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def hashCode(self, ):
        """public abstract int org.apache.commons.collections4.MultiSet$Entry.hashCode()"""
        pass

    @abstractmethod
    def getElement(self, ):
        """public abstract E org.apache.commons.collections4.MultiSet$Entry.getElement()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiSet$Entry.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def getCount(self, ):
        """public abstract int org.apache.commons.collections4.MultiSet$Entry.getCount()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.ResettableListIterator
import org.apache.commons.collections4.ResettableIterator as _ResettableIterator
_ResettableIterator = _ResettableIterator
from pyquantum_helper import override
import org.apache.commons.collections4.ResettableListIterator as _ResettableListIterator
_ResettableListIterator = _ResettableListIterator
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
import org.apache.commons.collections4.OrderedIterator as _OrderedIterator
_OrderedIterator = _OrderedIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class ResettableListIterator():
    """org.apache.commons.collections4.ResettableListIterator"""
 
    @staticmethod
    def _wrap(java_value: _ResettableListIterator) -> 'ResettableListIterator':
        return ResettableListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ResettableListIterator):
        """
        Dynamic initializer for ResettableListIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ResettableListIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ResettableListIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def reset(self, ):
        """public abstract void org.apache.commons.collections4.ResettableIterator.reset()"""
        pass

    @abstractmethod
    def nextIndex(self, ):
        """public abstract int java.util.ListIterator.nextIndex()"""
        pass

    @abstractmethod
    def previousIndex(self, ):
        """public abstract int java.util.ListIterator.previousIndex()"""
        pass

    @abstractmethod
    def previous(self, ):
        """public abstract E java.util.ListIterator.previous()"""
        pass

    @abstractmethod
    def next(self, ):
        """public abstract E java.util.ListIterator.next()"""
        pass

    @abstractmethod
    def add(self, arg0: object):
        """public abstract void java.util.ListIterator.add(E)"""
        pass

    @abstractmethod
    def hasPrevious(self, ):
        """public abstract boolean java.util.ListIterator.hasPrevious()"""
        pass

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.ListIterator.hasNext()"""
        pass

    @abstractmethod
    def hasPrevious(self, ):
        """public abstract boolean org.apache.commons.collections4.OrderedIterator.hasPrevious()"""
        pass

    @abstractmethod
    def previous(self, ):
        """public abstract E org.apache.commons.collections4.OrderedIterator.previous()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @abstractmethod
    def set(self, arg0: object):
        """public abstract void java.util.ListIterator.set(E)"""
        pass

    @abstractmethod
    def remove(self, ):
        """public abstract void java.util.ListIterator.remove()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.QueueUtils
import org.apache.commons.collections4.QueueUtils as _QueueUtils
_QueueUtils = _QueueUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.Queue as Queue
import java.util.Queue as _Queue
_Queue = _Queue
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class QueueUtils():
    """org.apache.commons.collections4.QueueUtils"""
 
    @staticmethod
    def _wrap(java_value: _QueueUtils) -> 'QueueUtils':
        return QueueUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _QueueUtils):
        """
        Dynamic initializer for QueueUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_QueueUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_QueueUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def unmodifiableQueue(arg0: 'Queue') -> 'Queue':
        """public static <E> java.util.Queue<E> org.apache.commons.collections4.QueueUtils.unmodifiableQueue(java.util.Queue<? extends E>)"""
        return Queue._wrap(_QueueUtils.unmodifiableQueue(arg0))

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
    def predicatedQueue(arg0: 'Queue', arg1: 'Predicate') -> 'Queue':
        """public static <E> java.util.Queue<E> org.apache.commons.collections4.QueueUtils.predicatedQueue(java.util.Queue<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return Queue._wrap(_QueueUtils.predicatedQueue(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def emptyQueue() -> 'Queue':
        """public static <E> java.util.Queue<E> org.apache.commons.collections4.QueueUtils.emptyQueue()"""
        return Queue._wrap(_QueueUtils.emptyQueue())

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
    def synchronizedQueue(arg0: 'Queue') -> 'Queue':
        """public static <E> java.util.Queue<E> org.apache.commons.collections4.QueueUtils.synchronizedQueue(java.util.Queue<E>)"""
        return Queue._wrap(_QueueUtils.synchronizedQueue(arg0))

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
    def transformingQueue(arg0: 'Queue', arg1: 'Transformer') -> 'Queue':
        """public static <E> java.util.Queue<E> org.apache.commons.collections4.QueueUtils.transformingQueue(java.util.Queue<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Queue._wrap(_QueueUtils.transformingQueue(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.IterableSortedMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.util.SequencedCollection as _SequencedCollection
_SequencedCollection = _SequencedCollection
import java.lang.Object as _object
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.Get as _Get
_Get = _Get
import java.util.SequencedSet as _SequencedSet
_SequencedSet = _SequencedSet
from abc import abstractmethod, ABC
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedCollection as SequencedCollection
import org.apache.commons.collections4.Put as _Put
_Put = _Put
import java.util.Map.Entry as Entry
import java.util.function.BiConsumer as BiConsumer
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import java.util.SortedMap as _SortedMap
_SortedMap = _SortedMap
import org.apache.commons.collections4.OrderedMap as _OrderedMap
_OrderedMap = _OrderedMap
import org.apache.commons.collections4.IterableSortedMap as _IterableSortedMap
_IterableSortedMap = _IterableSortedMap
import java.util.SortedMap as SortedMap
import java.util.SequencedSet as SequencedSet
import java.util.function.Function as Function
import java.util.SequencedMap as _SequencedMap
_SequencedMap = _SequencedMap
from builtins import bool
import java.util.Map as Map
 
class IterableSortedMap():
    """org.apache.commons.collections4.IterableSortedMap"""
 
    @staticmethod
    def _wrap(java_value: _IterableSortedMap) -> 'IterableSortedMap':
        return IterableSortedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IterableSortedMap):
        """
        Dynamic initializer for IterableSortedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IterableSortedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IterableSortedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.firstKey()"""
        pass

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.OrderedMap.mapIterator()"""
        pass

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollLastEntry())

    @abstractmethod
    def nextKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.nextKey(K)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def tailMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.tailMap(K)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def previousKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.previousKey(K)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K java.util.SortedMap.firstKey()"""
        pass

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @abstractmethod
    def lastKey(self, ):
        """public abstract K java.util.SortedMap.lastKey()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.SortedMap.entrySet()"""
        pass

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object._wrap(super(_SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).lastEntry())

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'._wrap(super(SortedMap, self).reversed())

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object._wrap(super(_SortedMap, self).putFirst(arg0, arg1))

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.Put.put(K,V)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.SortedMap.keySet()"""
        pass

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V java.util.Map.put(K,V)"""
        pass

    @abstractmethod
    def headMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.headMap(K)"""
        pass

    @abstractmethod
    def subMap(self, arg0: object, arg1: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.subMap(K,K)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.SortedMap.values()"""
        pass

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).firstEntry())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @abstractmethod
    def lastKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.lastKey()"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def comparator(self, ):
        """public abstract java.util.Comparator<? super K> java.util.SortedMap.comparator()"""
        pass

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.Get
import org.apache.commons.collections4.Get as _Get
_Get = _Get
from abc import abstractmethod, ABC
 
class Get():
    """org.apache.commons.collections4.Get"""
 
    @staticmethod
    def _wrap(java_value: _Get) -> 'Get':
        return Get(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Get):
        """
        Dynamic initializer for Get.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Get__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Get__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.Trie
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.util.SequencedCollection as _SequencedCollection
_SequencedCollection = _SequencedCollection
import java.lang.Object as _object
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.Get as _Get
_Get = _Get
import java.util.SequencedSet as _SequencedSet
_SequencedSet = _SequencedSet
from abc import abstractmethod, ABC
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedCollection as SequencedCollection
import org.apache.commons.collections4.Put as _Put
_Put = _Put
import java.util.Map.Entry as Entry
import java.util.function.BiConsumer as BiConsumer
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import java.util.SortedMap as _SortedMap
_SortedMap = _SortedMap
import org.apache.commons.collections4.OrderedMap as _OrderedMap
_OrderedMap = _OrderedMap
import java.util.SortedMap as SortedMap
import org.apache.commons.collections4.Trie as _Trie
_Trie = _Trie
import java.util.SequencedSet as SequencedSet
import java.util.function.Function as Function
import java.util.SequencedMap as _SequencedMap
_SequencedMap = _SequencedMap
from builtins import bool
import java.util.Map as Map
 
class Trie():
    """org.apache.commons.collections4.Trie"""
 
    @staticmethod
    def _wrap(java_value: _Trie) -> 'Trie':
        return Trie(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Trie):
        """
        Dynamic initializer for Trie.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Trie__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Trie__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.firstKey()"""
        pass

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.OrderedMap.mapIterator()"""
        pass

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollLastEntry())

    @abstractmethod
    def nextKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.nextKey(K)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def tailMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.tailMap(K)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def prefixMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> org.apache.commons.collections4.Trie.prefixMap(K)"""
        pass

    @abstractmethod
    def previousKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.previousKey(K)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K java.util.SortedMap.firstKey()"""
        pass

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @abstractmethod
    def lastKey(self, ):
        """public abstract K java.util.SortedMap.lastKey()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.SortedMap.entrySet()"""
        pass

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object._wrap(super(_SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).lastEntry())

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'._wrap(super(SortedMap, self).reversed())

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object._wrap(super(_SortedMap, self).putFirst(arg0, arg1))

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.Put.put(K,V)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.SortedMap.keySet()"""
        pass

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V java.util.Map.put(K,V)"""
        pass

    @abstractmethod
    def headMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.headMap(K)"""
        pass

    @abstractmethod
    def subMap(self, arg0: object, arg1: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.subMap(K,K)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.SortedMap.values()"""
        pass

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).firstEntry())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @abstractmethod
    def lastKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.lastKey()"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def comparator(self, ):
        """public abstract java.util.Comparator<? super K> java.util.SortedMap.comparator()"""
        pass

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.SetUtils
import java.util.SortedSet as _SortedSet
_SortedSet = _SortedSet
from builtins import str
import java.util.NavigableSet as NavigableSet
from pyquantum_helper import override
import java.util.HashSet as HashSet
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.SortedSet as SortedSet
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
import java.util.Set as Set
import org.apache.commons.collections4.SetUtils as _SetUtils
_SetUtils = _SetUtils
import java.lang.Integer as _int
import org.apache.commons.collections4.SetUtils as _SetUtils_SetView
_SetView = _SetUtils_SetView.SetView
import java.util.HashSet as _HashSet
_HashSet = _HashSet
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SetUtils():
    """org.apache.commons.collections4.SetUtils"""
 
    @staticmethod
    def _wrap(java_value: _SetUtils) -> 'SetUtils':
        return SetUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SetUtils):
        """
        Dynamic initializer for SetUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SetUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SetUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def disjunction(arg0: 'Set', arg1: 'Set') -> 'SetView':
        """public static <E> org.apache.commons.collections4.SetUtils$SetView<E> org.apache.commons.collections4.SetUtils.disjunction(java.util.Set<? extends E>,java.util.Set<? extends E>)"""
        return SetView._wrap(_SetUtils.disjunction(arg0, arg1))

    @staticmethod
    @overload
    def hashSet(*arg0: object) -> 'HashSet':
        """public static <E> java.util.HashSet<E> org.apache.commons.collections4.SetUtils.hashSet(E...)"""
        return HashSet._wrap(_SetUtils.hashSet(arg0))

    @staticmethod
    @overload
    def unmodifiableSet(*arg0: object) -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.unmodifiableSet(E...)"""
        return Set._wrap(_SetUtils.unmodifiableSet(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def emptySortedSet() -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.emptySortedSet()"""
        return SortedSet._wrap(_SetUtils.emptySortedSet())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def unmodifiableSortedSet(arg0: 'SortedSet') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.unmodifiableSortedSet(java.util.SortedSet<E>)"""
        return SortedSet._wrap(_SetUtils.unmodifiableSortedSet(arg0))

    @staticmethod
    @overload
    def orderedSet(arg0: 'Set') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.orderedSet(java.util.Set<E>)"""
        return Set._wrap(_SetUtils.orderedSet(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def intersection(arg0: 'Set', arg1: 'Set') -> 'SetView':
        """public static <E> org.apache.commons.collections4.SetUtils$SetView<E> org.apache.commons.collections4.SetUtils.intersection(java.util.Set<? extends E>,java.util.Set<? extends E>)"""
        return SetView._wrap(_SetUtils.intersection(arg0, arg1))

    @staticmethod
    @overload
    def transformedSet(arg0: 'Set', arg1: 'Transformer') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.transformedSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Set._wrap(_SetUtils.transformedSet(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableNavigableSet(arg0: 'NavigableSet') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.unmodifiableNavigableSet(java.util.NavigableSet<E>)"""
        return SortedSet._wrap(_SetUtils.unmodifiableNavigableSet(arg0))

    @staticmethod
    @overload
    def difference(arg0: 'Set', arg1: 'Set') -> 'SetView':
        """public static <E> org.apache.commons.collections4.SetUtils$SetView<E> org.apache.commons.collections4.SetUtils.difference(java.util.Set<? extends E>,java.util.Set<? extends E>)"""
        return SetView._wrap(_SetUtils.difference(arg0, arg1))

    @staticmethod
    @overload
    def predicatedSet(arg0: 'Set', arg1: 'Predicate') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.predicatedSet(java.util.Set<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return Set._wrap(_SetUtils.predicatedSet(arg0, arg1))

    @staticmethod
    @overload
    def synchronizedSet(arg0: 'Set') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.synchronizedSet(java.util.Set<E>)"""
        return Set._wrap(_SetUtils.synchronizedSet(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def emptyIfNull(arg0: 'Set') -> 'Set':
        """public static <T> java.util.Set<T> org.apache.commons.collections4.SetUtils.emptyIfNull(java.util.Set<T>)"""
        return Set._wrap(_SetUtils.emptyIfNull(arg0))

    @staticmethod
    @overload
    def predicatedSortedSet(arg0: 'SortedSet', arg1: 'Predicate') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.predicatedSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return SortedSet._wrap(_SetUtils.predicatedSortedSet(arg0, arg1))

    @staticmethod
    @overload
    def hashCodeForSet(arg0: 'Collection') -> int:
        """public static <T> int org.apache.commons.collections4.SetUtils.hashCodeForSet(java.util.Collection<T>)"""
        return int._wrap(_SetUtils.hashCodeForSet(arg0))

    @staticmethod
    @overload
    def predicatedNavigableSet(arg0: 'NavigableSet', arg1: 'Predicate') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.predicatedNavigableSet(java.util.NavigableSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return SortedSet._wrap(_SetUtils.predicatedNavigableSet(arg0, arg1))

    @staticmethod
    @overload
    def newIdentityHashSet() -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.newIdentityHashSet()"""
        return Set._wrap(_SetUtils.newIdentityHashSet())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def unmodifiableSet(arg0: 'Set') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.unmodifiableSet(java.util.Set<? extends E>)"""
        return Set._wrap(_SetUtils.unmodifiableSet(arg0))

    @staticmethod
    @overload
    def synchronizedSortedSet(arg0: 'SortedSet') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.synchronizedSortedSet(java.util.SortedSet<E>)"""
        return SortedSet._wrap(_SetUtils.synchronizedSortedSet(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def emptySet() -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.emptySet()"""
        return Set._wrap(_SetUtils.emptySet())

    @staticmethod
    @overload
    def union(arg0: 'Set', arg1: 'Set') -> 'SetView':
        """public static <E> org.apache.commons.collections4.SetUtils$SetView<E> org.apache.commons.collections4.SetUtils.union(java.util.Set<? extends E>,java.util.Set<? extends E>)"""
        return SetView._wrap(_SetUtils.union(arg0, arg1))

    @staticmethod
    @overload
    def transformedNavigableSet(arg0: 'NavigableSet', arg1: 'Transformer') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.transformedNavigableSet(java.util.NavigableSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return SortedSet._wrap(_SetUtils.transformedNavigableSet(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def isEqualSet(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.SetUtils.isEqualSet(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool._wrap(_SetUtils.isEqualSet(arg0, arg1))

    @staticmethod
    @overload
    def transformedSortedSet(arg0: 'SortedSet', arg1: 'Transformer') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.transformedSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return SortedSet._wrap(_SetUtils.transformedSortedSet(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.MultiValuedMap
import org.apache.commons.collections4.MultiValuedMap as _MultiValuedMap
_MultiValuedMap = _MultiValuedMap
import java.lang.Iterable as Iterable
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class MultiValuedMap():
    """org.apache.commons.collections4.MultiValuedMap"""
 
    @staticmethod
    def _wrap(java_value: _MultiValuedMap) -> 'MultiValuedMap':
        return MultiValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiValuedMap):
        """
        Dynamic initializer for MultiValuedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiValuedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiValuedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.MultiValuedMap.mapIterator()"""
        pass

    @abstractmethod
    def putAll(self, arg0: object, arg1: 'Iterable'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def removeMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.MultiValuedMap.clear()"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.MultiValuedMap.values()"""
        pass

    @abstractmethod
    def containsMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.isEmpty()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.MultiValuedMap.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def keys(self, ):
        """public abstract org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.MultiValuedMap.keys()"""
        pass

    @abstractmethod
    def entries(self, ):
        """public abstract java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.MultiValuedMap.entries()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.put(K,V)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.MultiValuedMap.keySet()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'MultiValuedMap'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.MultiValuedMap.get(K)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.MultiValuedMap.size()"""
        pass

    @abstractmethod
    def asMap(self, ):
        """public abstract java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.MultiValuedMap.asMap()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.IterableGet
import org.apache.commons.collections4.IterableGet as _IterableGet
_IterableGet = _IterableGet
import org.apache.commons.collections4.Get as _Get
_Get = _Get
from abc import abstractmethod, ABC
 
class IterableGet():
    """org.apache.commons.collections4.IterableGet"""
 
    @staticmethod
    def _wrap(java_value: _IterableGet) -> 'IterableGet':
        return IterableGet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IterableGet):
        """
        Dynamic initializer for IterableGet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IterableGet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IterableGet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IterableGet.mapIterator()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass