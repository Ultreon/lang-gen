from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.comparators.TransformingComparator as _TransformingComparator
_TransformingComparator = _TransformingComparator
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

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
 
class TransformingComparator():
    """org.apache.commons.collections4.comparators.TransformingComparator"""
 
    @staticmethod
    def _wrap(java_value: _TransformingComparator) -> 'TransformingComparator':
        return TransformingComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformingComparator):
        """
        Dynamic initializer for TransformingComparator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformingComparator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformingComparator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def __init__(self, arg0: 'Transformer'):
        """public org.apache.commons.collections4.comparators.TransformingComparator(org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        val = _TransformingComparator(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Transformer', arg1: 'Comparator'):
        """public org.apache.commons.collections4.comparators.TransformingComparator(org.apache.commons.collections4.Transformer<? super I, ? extends O>,java.util.Comparator<O>)"""
        val = _TransformingComparator(arg0, arg1)
        self.__wrapper = val

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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.comparators.TransformingComparator.compare(I,I)"""
        return int._wrap(super(_TransformingComparator, self).compare(arg0, arg1))

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.TransformingComparator.equals(java.lang.Object)"""
        return bool._wrap(super(_TransformingComparator, self).equals(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.TransformingComparator.hashCode()"""
        return int._wrap(super(TransformingComparator, self).hashCode())

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.comparators.TransformingComparator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.comparators.TransformingComparator as _TransformingComparator
_TransformingComparator = _TransformingComparator
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

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
 
class TransformingComparator():
    """org.apache.commons.collections4.comparators.TransformingComparator"""
 
    @staticmethod
    def _wrap(java_value: _TransformingComparator) -> 'TransformingComparator':
        return TransformingComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformingComparator):
        """
        Dynamic initializer for TransformingComparator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformingComparator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformingComparator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def __init__(self, arg0: 'Transformer'):
        """public org.apache.commons.collections4.comparators.TransformingComparator(org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        val = _TransformingComparator(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Transformer', arg1: 'Comparator'):
        """public org.apache.commons.collections4.comparators.TransformingComparator(org.apache.commons.collections4.Transformer<? super I, ? extends O>,java.util.Comparator<O>)"""
        val = _TransformingComparator(arg0, arg1)
        self.__wrapper = val

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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.comparators.TransformingComparator.compare(I,I)"""
        return int._wrap(super(_TransformingComparator, self).compare(arg0, arg1))

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.TransformingComparator.equals(java.lang.Object)"""
        return bool._wrap(super(_TransformingComparator, self).equals(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.TransformingComparator.hashCode()"""
        return int._wrap(super(TransformingComparator, self).hashCode())

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.comparators.TransformingComparator 
 
 
# CLASS: org.apache.commons.collections4.comparators.ReverseComparator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import org.apache.commons.collections4.comparators.ReverseComparator as _ReverseComparator
_ReverseComparator = _ReverseComparator
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
 
class ReverseComparator():
    """org.apache.commons.collections4.comparators.ReverseComparator"""
 
    @staticmethod
    def _wrap(java_value: _ReverseComparator) -> 'ReverseComparator':
        return ReverseComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReverseComparator):
        """
        Dynamic initializer for ReverseComparator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReverseComparator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReverseComparator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.ReverseComparator.equals(java.lang.Object)"""
        return bool._wrap(super(_ReverseComparator, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.comparators.ReverseComparator()"""
        val = _ReverseComparator()
        self.__wrapper = val

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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.comparators.ReverseComparator.compare(E,E)"""
        return int._wrap(super(_ReverseComparator, self).compare(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.ReverseComparator.hashCode()"""
        return int._wrap(super(ReverseComparator, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.comparators.ReverseComparator()"""
        val = _ReverseComparator()
        self.__wrapper = val

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
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @overload
    def __init__(self, arg0: 'Comparator'):
        """public org.apache.commons.collections4.comparators.ReverseComparator(java.util.Comparator<? super E>)"""
        val = _ReverseComparator(arg0)
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.comparators.FixedOrderComparator as _FixedOrderComparator_UnknownObjectBehavior
_UnknownObjectBehavior = _FixedOrderComparator_UnknownObjectBehavior.UnknownObjectBehavior
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnknownObjectBehavior():
    """org.apache.commons.collections4.comparators.FixedOrderComparator.UnknownObjectBehavior"""
 
    @staticmethod
    def _wrap(java_value: _UnknownObjectBehavior) -> 'UnknownObjectBehavior':
        return UnknownObjectBehavior(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnknownObjectBehavior):
        """
        Dynamic initializer for UnknownObjectBehavior.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnknownObjectBehavior__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnknownObjectBehavior__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def values() -> List['UnknownObjectBehavior']:
        """public static org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior[] org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior.values()"""
        return List[UnknownObjectBehavior]._wrap(_UnknownObjectBehavior.values())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'UnknownObjectBehavior':
        """public static org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior.valueOf(java.lang.String)"""
        return UnknownObjectBehavior._wrap(_UnknownObjectBehavior.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.collections4.comparators.FixedOrderComparator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.comparators.FixedOrderComparator as _FixedOrderComparator_UnknownObjectBehavior
_UnknownObjectBehavior = _FixedOrderComparator_UnknownObjectBehavior.UnknownObjectBehavior
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
import org.apache.commons.collections4.comparators.FixedOrderComparator as _FixedOrderComparator
_FixedOrderComparator = _FixedOrderComparator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
 
class FixedOrderComparator():
    """org.apache.commons.collections4.comparators.FixedOrderComparator"""
 
    @staticmethod
    def _wrap(java_value: _FixedOrderComparator) -> 'FixedOrderComparator':
        return FixedOrderComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FixedOrderComparator):
        """
        Dynamic initializer for FixedOrderComparator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FixedOrderComparator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FixedOrderComparator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAsEqual(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.FixedOrderComparator.addAsEqual(T,T)"""
        return bool._wrap(super(_FixedOrderComparator, self).addAsEqual(arg0, arg1))

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isLocked(self) -> bool:
        """public boolean org.apache.commons.collections4.comparators.FixedOrderComparator.isLocked()"""
        return bool._wrap(super(FixedOrderComparator, self).isLocked())

    @overload
    def getUnknownObjectBehavior(self) -> 'UnknownObjectBehavior':
        """public org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior org.apache.commons.collections4.comparators.FixedOrderComparator.getUnknownObjectBehavior()"""
        return 'UnknownObjectBehavior'._wrap(super(FixedOrderComparator, self).getUnknownObjectBehavior())

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

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.FixedOrderComparator.add(T)"""
        return bool._wrap(super(_FixedOrderComparator, self).add(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.FixedOrderComparator.hashCode()"""
        return int._wrap(super(FixedOrderComparator, self).hashCode())

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.FixedOrderComparator.equals(java.lang.Object)"""
        return bool._wrap(super(_FixedOrderComparator, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.comparators.FixedOrderComparator()"""
        val = _FixedOrderComparator()
        self.__wrapper = val

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
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @overload
    def __init__(self, arg0: 'List'):
        """public org.apache.commons.collections4.comparators.FixedOrderComparator(java.util.List<T>)"""
        val = _FixedOrderComparator(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.comparators.FixedOrderComparator.compare(T,T)"""
        return int._wrap(super(_FixedOrderComparator, self).compare(arg0, arg1))

    @overload
    def setUnknownObjectBehavior(self, arg0: 'UnknownObjectBehavior'):
        """public void org.apache.commons.collections4.comparators.FixedOrderComparator.setUnknownObjectBehavior(org.apache.commons.collections4.comparators.FixedOrderComparator$UnknownObjectBehavior)"""
        super(_FixedOrderComparator, self).setUnknownObjectBehavior(arg0)

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
    def __init__(self, *arg0: object):
        """public org.apache.commons.collections4.comparators.FixedOrderComparator(T...)"""
        val = _FixedOrderComparator(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.comparators.FixedOrderComparator()"""
        val = _FixedOrderComparator()
        self.__wrapper = val

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed()) 
 
 
# CLASS: org.apache.commons.collections4.comparators.ComparatorChain
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.BitSet as BitSet
import java.util.Comparator as Comparator
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import org.apache.commons.collections4.comparators.ComparatorChain as _ComparatorChain
_ComparatorChain = _ComparatorChain
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
 
class ComparatorChain():
    """org.apache.commons.collections4.comparators.ComparatorChain"""
 
    @staticmethod
    def _wrap(java_value: _ComparatorChain) -> 'ComparatorChain':
        return ComparatorChain(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ComparatorChain):
        """
        Dynamic initializer for ComparatorChain.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ComparatorChain__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ComparatorChain__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isLocked(self) -> bool:
        """public boolean org.apache.commons.collections4.comparators.ComparatorChain.isLocked()"""
        return bool._wrap(super(ComparatorChain, self).isLocked())

    @overload
    def setReverseSort(self, arg0: int):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.setReverseSort(int)"""
        super(_ComparatorChain, self).setReverseSort(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Comparator'):
        """public org.apache.commons.collections4.comparators.ComparatorChain(java.util.Comparator<E>)"""
        val = _ComparatorChain(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.comparators.ComparatorChain()"""
        val = _ComparatorChain()
        self.__wrapper = val

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.comparators.ComparatorChain()"""
        val = _ComparatorChain()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.comparators.ComparatorChain.compare(E,E) throws java.lang.UnsupportedOperationException"""
        return int._wrap(super(_ComparatorChain, self).compare(arg0, arg1))

    @overload
    def addComparator(self, arg0: 'Comparator', arg1: bool):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.addComparator(java.util.Comparator<E>,boolean)"""
        super(_ComparatorChain, self).addComparator(arg0, _boolean.valueOf(arg1))

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

    @overload
    def __init__(self, arg0: 'List'):
        """public org.apache.commons.collections4.comparators.ComparatorChain(java.util.List<java.util.Comparator<E>>)"""
        val = _ComparatorChain(arg0)
        self.__wrapper = val

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.comparators.ComparatorChain.size()"""
        return int._wrap(super(ComparatorChain, self).size())

    @overload
    def addComparator(self, arg0: 'Comparator'):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.addComparator(java.util.Comparator<E>)"""
        super(_ComparatorChain, self).addComparator(arg0)

    @overload
    def setComparator(self, arg0: int, arg1: 'Comparator', arg2: bool):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.setComparator(int,java.util.Comparator<E>,boolean)"""
        super(_ComparatorChain, self).setComparator(_int.valueOf(arg0), arg1, _boolean.valueOf(arg2))

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
    def __init__(self, arg0: 'Comparator', arg1: bool):
        """public org.apache.commons.collections4.comparators.ComparatorChain(java.util.Comparator<E>,boolean)"""
        val = _ComparatorChain(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def setComparator(self, arg0: int, arg1: 'Comparator'):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.setComparator(int,java.util.Comparator<E>) throws java.lang.IndexOutOfBoundsException"""
        super(_ComparatorChain, self).setComparator(_int.valueOf(arg0), arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.ComparatorChain.hashCode()"""
        return int._wrap(super(ComparatorChain, self).hashCode())

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'List', arg1: 'BitSet'):
        """public org.apache.commons.collections4.comparators.ComparatorChain(java.util.List<java.util.Comparator<E>>,java.util.BitSet)"""
        val = _ComparatorChain(arg0, arg1)
        self.__wrapper = val

    @overload
    def setForwardSort(self, arg0: int):
        """public void org.apache.commons.collections4.comparators.ComparatorChain.setForwardSort(int)"""
        super(_ComparatorChain, self).setForwardSort(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.ComparatorChain.equals(java.lang.Object)"""
        return bool._wrap(super(_ComparatorChain, self).equals(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.comparators.NullComparator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.Comparator as Comparator
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import org.apache.commons.collections4.comparators.NullComparator as _NullComparator
_NullComparator = _NullComparator
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NullComparator():
    """org.apache.commons.collections4.comparators.NullComparator"""
 
    @staticmethod
    def _wrap(java_value: _NullComparator) -> 'NullComparator':
        return NullComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NullComparator):
        """
        Dynamic initializer for NullComparator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NullComparator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NullComparator__wrapper":
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
    def __init__(self, ):
        """public org.apache.commons.collections4.comparators.NullComparator()"""
        val = _NullComparator()
        self.__wrapper = val

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingInt(arg0))

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
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Comparator', arg1: bool):
        """public org.apache.commons.collections4.comparators.NullComparator(java.util.Comparator<? super E>,boolean)"""
        val = _NullComparator(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.NullComparator.hashCode()"""
        return int._wrap(super(NullComparator, self).hashCode())

    @overload
    def __init__(self, arg0: 'Comparator'):
        """public org.apache.commons.collections4.comparators.NullComparator(java.util.Comparator<? super E>)"""
        val = _NullComparator(arg0)
        self.__wrapper = val

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.NullComparator.equals(java.lang.Object)"""
        return bool._wrap(super(_NullComparator, self).equals(arg0))

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.comparators.NullComparator.compare(E,E)"""
        return int._wrap(super(_NullComparator, self).compare(arg0, arg1))

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
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.comparators.NullComparator()"""
        val = _NullComparator()
        self.__wrapper = val

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @overload
    def __init__(self, arg0: bool):
        """public org.apache.commons.collections4.comparators.NullComparator(boolean)"""
        val = _NullComparator(_boolean.valueOf(arg0))
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.comparators.BooleanComparator
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.Comparator as Comparator
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
import org.apache.commons.collections4.comparators.BooleanComparator as _BooleanComparator
_BooleanComparator = _BooleanComparator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BooleanComparator():
    """org.apache.commons.collections4.comparators.BooleanComparator"""
 
    @staticmethod
    def _wrap(java_value: _BooleanComparator) -> 'BooleanComparator':
        return BooleanComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BooleanComparator):
        """
        Dynamic initializer for BooleanComparator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BooleanComparator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BooleanComparator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def compare(self, arg0: 'Boolean', arg1: 'Boolean') -> int:
        """public int org.apache.commons.collections4.comparators.BooleanComparator.compare(java.lang.Boolean,java.lang.Boolean)"""
        return int._wrap(super(_BooleanComparator, self).compare(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @staticmethod
    @overload
    def getFalseFirstComparator() -> 'BooleanComparator':
        """public static org.apache.commons.collections4.comparators.BooleanComparator org.apache.commons.collections4.comparators.BooleanComparator.getFalseFirstComparator()"""
        return BooleanComparator._wrap(_BooleanComparator.getFalseFirstComparator())

    @overload
    def sortsTrueFirst(self) -> bool:
        """public boolean org.apache.commons.collections4.comparators.BooleanComparator.sortsTrueFirst()"""
        return bool._wrap(super(BooleanComparator, self).sortsTrueFirst())

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
    def __init__(self, ):
        """public org.apache.commons.collections4.comparators.BooleanComparator()"""
        val = _BooleanComparator()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getTrueFirstComparator() -> 'BooleanComparator':
        """public static org.apache.commons.collections4.comparators.BooleanComparator org.apache.commons.collections4.comparators.BooleanComparator.getTrueFirstComparator()"""
        return BooleanComparator._wrap(_BooleanComparator.getTrueFirstComparator())

    @staticmethod
    @overload
    def booleanComparator(arg0: bool) -> 'BooleanComparator':
        """public static org.apache.commons.collections4.comparators.BooleanComparator org.apache.commons.collections4.comparators.BooleanComparator.booleanComparator(boolean)"""
        return BooleanComparator._wrap(_BooleanComparator.booleanComparator(_boolean.valueOf(arg0)))

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

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.comparators.BooleanComparator()"""
        val = _BooleanComparator()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: bool):
        """public org.apache.commons.collections4.comparators.BooleanComparator(boolean)"""
        val = _BooleanComparator(_boolean.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.BooleanComparator.hashCode()"""
        return int._wrap(super(BooleanComparator, self).hashCode())

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
        """public boolean org.apache.commons.collections4.comparators.BooleanComparator.equals(java.lang.Object)"""
        return bool._wrap(super(_BooleanComparator, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.comparators.ComparableComparator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Comparable as Comparable
import java.lang.String as _String
_String = _String
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import org.apache.commons.collections4.comparators.ComparableComparator as _ComparableComparator
_ComparableComparator = _ComparableComparator
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ComparableComparator():
    """org.apache.commons.collections4.comparators.ComparableComparator"""
 
    @staticmethod
    def _wrap(java_value: _ComparableComparator) -> 'ComparableComparator':
        return ComparableComparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ComparableComparator):
        """
        Dynamic initializer for ComparableComparator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ComparableComparator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ComparableComparator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def compare(self, arg0: 'Comparable', arg1: 'Comparable') -> int:
        """public int org.apache.commons.collections4.comparators.ComparableComparator.compare(E,E)"""
        return int._wrap(super(_ComparableComparator, self).compare(arg0, arg1))

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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.comparators.ComparableComparator()"""
        val = _ComparableComparator()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.comparators.ComparableComparator.hashCode()"""
        return int._wrap(super(ComparableComparator, self).hashCode())

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

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.comparators.ComparableComparator()"""
        val = _ComparableComparator()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def comparableComparator() -> 'ComparableComparator':
        """public static <E extends java.lang.Comparable<? super E>> org.apache.commons.collections4.comparators.ComparableComparator<E> org.apache.commons.collections4.comparators.ComparableComparator.comparableComparator()"""
        return ComparableComparator._wrap(_ComparableComparator.comparableComparator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.comparators.ComparableComparator.equals(java.lang.Object)"""
        return bool._wrap(super(_ComparableComparator, self).equals(arg0))

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